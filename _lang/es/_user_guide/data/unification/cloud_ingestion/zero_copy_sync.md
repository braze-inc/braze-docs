---
nav_title: Personalización sin copia
article_title: Personalización sin copia utilizando CDI
page_order: 4
page_type: reference
description: "Esta página ofrece un resumen sobre cómo desencadenar Braze Canvas utilizando CDI."
---

# Personalización sin copia utilizando CDI

> Aprende a sincronizar los desencadenantes de Canvas utilizando CDI para una personalización sin copia. Esta característica accede a información específica del usuario desde tu solución de almacenamiento de datos y la transfiere a un Canvas de destino. Los pasos en Canvas pueden incluir opcionalmente campos de personalización que no se conservan en los perfiles de usuario de Braze.

{% multi_lang_include early_access_beta_alert.md feature='CDI Canvas triggers' %}

## Sincronización de los desencadenantes de Canvas

### Pasos para una puesta en marcha rápida

Si ya estás familiarizado con Braze CDI, ten en cuenta que la configuración de la sincronización de desencadenantes de Canvas sigue muy de cerca el proceso de [las integraciones de CDI de datos de usuario]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/), con las siguientes salvedades:

- Solo se admiten identificadores de ID externo o alias de usuario. Los correos electrónicos y los números de teléfono no son identificadores válidos.  
- Solo se pueden sincronizar los usuarios existentes de Braze. No se pueden crear nuevos usuarios.  
- `properties` reemplaza la columna `payload`. Es una cadena JSON de los campos que deseas utilizar como propiedades de entrada de Canvas para la personalización.

Para empezar, selecciona el tipo de datos **Canvas Triggers** al crear una nueva sincronización.

### Uso de los desencadenantes de Canvas 

#### Paso 1: Configurar el origen de datos para los desencadenantes de Canvas

{% tabs %}
{% tab Snowflake %}

##### Paso 1.1: Configura tu tabla de origen en Snowflake

Puedes utilizar los nombres del siguiente ejemplo o elegir tus propios nombres de base de datos, esquema y tabla. También puedes utilizar una vista o una vista materializada en lugar de una tabla.  

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id or alias_name and alias_label is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     PROPERTIES VARCHAR(16777216)
);
```

Puedes nombrar la base de datos, el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

* `UPDATED_AT`: La hora en que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en el límite exacto de la marca de tiempo pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.  
* `external_id` o `alias_name` y `alias_label` como columna identificadora del usuario. Estos identifican a los usuarios para los que deseas desencadenar la mensajería de Canvas.  
  * `EXTERNAL_ID`: Identifica al usuario para que entre en Canvas. Debe coincidir con el valor `external_id` utilizado en Braze.  
  * `ALIAS_NAME` y `ALIAS_LABEL`: Estas columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero solo un alias_name por `alias_label`.  
* `PROPERTIES`: Una cadena JSON de campos que estarán disponibles como propiedades de personalización en tu Canvas. Debe contener información específica del usuario.

{% alert note %}
No es necesario que todas las filas o usuarios tengan propiedades. Sin embargo, los valores de las propiedades deben ser una cadena JSON válida. Introduce una cadena `{}` vacía si no hay propiedades para la fila.
{% endalert %}

##### Paso 1.2: Configurar credenciales

Configura un rol, un almacén y un usuario, y concede los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen de los desencadenantes de Canvas.  

```sql

CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;

```

##### Paso 1.3: Configurar políticas de red

Si tu cuenta tiene políticas de red, incluye las direcciones IP de Braze en la lista de permitidos para habilitar la conexión del servicio CDI. Para ver la lista de direcciones IP, consulta [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

{% endtab %}
{% tab Redshift %}

##### Paso 1.1: Configura tu tabla de origen en Redshift

Puedes utilizar los nombres del siguiente ejemplo o elegir tus propios nombres de base de datos, esquema y tabla. También puedes utilizar una vista o una vista materializada en lugar de una tabla.

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
    updated_at timestamptz default sysdate not null,
    --at least one of external_id or alias_name and alias_label is required
    external_id varchar not null,.
    --if using user alias, both alias_name and alias_label are required
    alias_label varchar,
    alias_name varchar,
    properties varchar(max)
 );
```

Puedes nombrar la base de datos, el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

* `UPDATED_AT`: La hora en que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en el límite exacto de la marca de tiempo pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.  
* `external_id` o `alias_name` y `alias_label` como columna identificadora del usuario. Estos identifican a los usuarios para los que deseas desencadenar la mensajería de Canvas.  
  * `EXTERNAL_ID`: Identifica al usuario para que entre en Canvas. Debe coincidir con el valor `external_id` utilizado en Braze.  
  * `ALIAS_NAME` y `ALIAS_LABEL`: Estas columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y alias_label especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero solo un `alias_name` por `alias_label`.  
* `PROPERTIES`: Una cadena JSON de campos que estarán disponibles como propiedades de personalización en tu Canvas. Debe contener información específica del usuario.

{% alert note %}
No es necesario que todas las filas o usuarios tengan propiedades. Sin embargo, los valores de las propiedades deben ser una cadena JSON válida. Introduce una cadena `{}` vacía si no hay propiedades para la fila.
{% endalert %}

##### Paso 1.2: Configurar credenciales

Configura un rol, un almacén y un usuario, y concede los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen de los desencadenantes de Canvas.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Paso 1.3: Configurar políticas de red 

Si tu cuenta tiene políticas de red, incluye las direcciones IP de Braze en la lista de permitidos para habilitar la conexión del servicio CDI. Para ver la lista de direcciones IP, consulta [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Paso 1.1: Crea un nuevo proyecto o conjunto de datos para tu tabla de origen (opcional)

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Paso 1.2: Configura tu tabla de origen en BigQuery
Consulta lo siguiente al crear tu tabla de origen:  

| Nombre del campo | Tipo | ¿Es obligatorio? | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | Marca de tiempo | Sí | 
| **`PROPERTIES`** | JSON | Sí | 
| **`EXTERNAL_ID`** | STRING | NULLABLE | 
| **`ALIAS_NAME`** | STRING | NULLABLE | 
| **`ALIAS_LABEL`** | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
No es necesario que todas las filas o usuarios tengan propiedades. Sin embargo, los valores de las propiedades deben ser una cadena JSON válida. Introduce una cadena `{}` vacía si no hay propiedades para la fila.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties JSON
);
```

##### Paso 1.3: Configurar credenciales

Crea un usuario y concédele permisos. Si ya tienes credenciales de otra sincronización, puedes reutilizarlas siempre que tengan acceso a la tabla de desencadenantes de Canvas.

| Permiso | Propósito |
| :---- | :---- |
| Usuario de conexión de BigQuery | Permite que Braze se conecte. |
| Usuario de BigQuery | Permite a Braze ejecutar consultas, leer metadatos y enumerar tablas. |
| Visor de datos de BigQuery | Permite a Braze ver conjuntos de datos y contenidos. |
| Usuario de tareas de BigQuery | Permite a Braze ejecutar trabajos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Después de conceder los permisos, genera una clave JSON. Consulta [Crear y eliminar claves](https://cloud.google.com/iam/docs/keys-create-delete) para obtener instrucciones. La subirás más tarde al panel de Braze.

##### Paso 1.4: Configurar políticas de red 
Si tu cuenta tiene políticas de red, incluye las direcciones IP de Braze en la lista de permitidos para habilitar la conexión del servicio CDI. Para ver la lista de direcciones IP, consulta [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Paso 1.1: Crea un catálogo o esquema para tu tabla de origen

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Paso 1.2: Configura tu tabla de origen en Databricks

Consulta lo siguiente al crear tu tabla de origen:

| Nombre del campo | Tipo | Obligatoria |
| :---- | :---- | :---- |
| `UPDATED_AT` | Marca de tiempo | Sí |
| `PROPERTIES` | JSON | Sí |
| `EXTERNAL_ID` | STRING |  NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Puedes nombrar el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

* `UPDATED_AT`: La hora en que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en el límite exacto de la marca de tiempo pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.  
* `external_id` o `alias_name` y `alias_label` como columna identificadora del usuario. Estos identifican a los usuarios para los que deseas desencadenar la mensajería de Canvas.  
  * `EXTERNAL_ID`: Identifica al usuario para que entre en Canvas. Debe coincidir con el valor `external_id` utilizado en Braze.  
  * `ALIAS_NAME` y `ALIAS_LABEL`: Estas columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero solo un alias_name por `alias_label`.  
* `PROPERTIES`: Una cadena o estructura de campos que estarán disponibles como propiedades de personalización en tu Canvas. Debe contener información específica del usuario.

{% alert note %}
No es necesario que todas las filas o usuarios tengan propiedades. Sin embargo, los valores de las propiedades deben ser cadenas JSON válidas. Introduce una cadena `{}` vacía si no hay propiedades para la fila.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties STRING, STRUCT, or MAP
);
```

##### Paso 1.3: Configurar credenciales 

Crea un token de acceso personal en Databricks:

1. Selecciona tu nombre de usuario y, a continuación, selecciona **User Settings.**  
2. En la pestaña **Access tokens**, selecciona **Generate new token.**  
3. Añade un comentario como identificador del token, como "Braze CDI".  
4. Deja en blanco el campo **Lifetime (days)** para que no haya fecha de caducidad y, a continuación, selecciona **Generate**.  
5. Copia y guarda el token de forma segura para utilizarlo en el panel de Braze.

##### Paso 1.4: Configurar políticas de red 

Si tu cuenta tiene políticas de red, incluye las direcciones IP de Braze en la lista de permitidos para habilitar la conexión del servicio CDI. Para ver la lista de direcciones IP, consulta [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Fabric %}

##### Paso 1.1: Configura tu tabla de origen en Fabric

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PROPERTIES VARCHAR NOT NULL,
  --at least one of external_id or alias_name and alias_label is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR
)
GO
```

##### Paso 1.2: Configurar credenciales 

Crea una entidad de servicio y concede permisos. Si ya tienes credenciales de otra sincronización, puedes reutilizarlas, solo asegúrate de que tengan acceso a la tabla de cuentas.

##### Paso 1.3: Configurar políticas de red 

Si tu cuenta tiene políticas de red, incluye las direcciones IP de Braze en la lista de permitidos para habilitar la conexión del servicio CDI. Para ver la lista de direcciones IP, consulta [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

Para sincronizar los desencadenantes de Canvas desde el almacenamiento de archivos, crea un archivo de origen con los siguientes campos.

| Campo | Obligatoria | Descripción |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Sí, uno de `external_id` o `alias_name`, y `alias_label` | Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Sí, uno de `external_id` o `alias_name` y `alias_label` | Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero solo un `alias_name` por `alias_label`. |
| `PROPERTIES` | Sí | Cadena JSON de campos que estarán disponibles como propiedades de personalización en tu Canvas. Debe contener información específica del usuario. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Los nombres de los archivos deben seguir las reglas de AWS y ser únicos. Añade marcas de tiempo para garantizar la unicidad. Para obtener más información sobre la sincronización con Amazon S3, consulta [Integraciones de almacenamiento de archivos](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Paso 2: Configura tu Canvas de destino

1. Configura tu Canvas de destino para los desencadenantes de Canvas. Crea un Canvas nuevo o selecciona uno existente que se desencadene por API. Consulta [Tipos de programación de entradas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types) para obtener instrucciones sobre cómo crear un Canvas con un tipo de programación de entrega desencadenado por API.
2. Después de seleccionar el tipo de programación de entrega desencadenada por API, continúa con la configuración y crea tu Canvas. Los Canvas pueden variar desde simples envíos de un solo mensaje hasta complejos flujos de trabajo para clientes con múltiples pasos.
3. Dentro de tus pasos en Canvas, utiliza [las propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) para personalizar los mensajes con los campos de propiedades que planeas sincronizar desde tu tabla de origen.
  * Por ejemplo, si en el paso 1 instrumentaste un campo de propiedades para `account_balance`, utilizarías la siguiente plantilla Liquid para personalizar tu mensaje: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Después de crear tu Canvas, lánzalo y continúa con [el paso 3](#step-3-create-your-zero-copy-sync).

#### Paso 3: Crea tu sincronización sin copia

Una vez completada la configuración del origen de datos y lanzado el Canvas, crea una nueva sincronización de datos:

1. En Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube**.
1. Configura la conexión introduciendo los datos de conexión (o reutiliza las credenciales existentes) y la tabla de origen del [paso 1](#step-1-set-up-data-source-for-canvas-triggers).
2. Proporciona un nombre para la integración.
3. Selecciona el tipo de datos **Canvas Triggers**.
4. Elige tu Canvas de destino (del [paso 2](#step-2-configure-your-destination-canvas)).
5. Elige una frecuencia de sincronización.
6. Configura las preferencias de notificación.
7. Selecciona **Test Connection** para confirmar que todo funciona según lo previsto. Si te conectas a Snowflake, primero añade la clave pública que se muestra en el dashboard al usuario creado para que Braze se conecte a Snowflake. Para completar este paso, necesitarás acceso **SECURITYADMIN** o superior en Snowflake. 
8. Guarda la sincronización para comenzar a sincronizar los desencadenantes de Canvas.

Cuando se ejecute la sincronización, los usuarios de tu tabla de origen comenzarán a entrar en el Canvas. Utiliza los análisis de Canvas y la página de registros de sincronización de la ingesta de datos en la nube para supervisar el rendimiento.

{% alert tip %}  
Revisa toda la configuración (desde el comportamiento de sincronización hasta la configuración de Canvas) para evitar envíos inesperados. Las configuraciones de Canvas, como la limitación de velocidad, la limitación de frecuencia y los filtros de segmentación, pueden refinar aún más la entrega de mensajes.<br><br>Recomendamos realizar una prueba con una audiencia reducida o de prueba antes de implementar casos de uso en producción.
{% endalert %}

### Consideraciones

Los desencadenantes de CDI Canvas utilizan tu límite de velocidad de la API REST para `/canvas/trigger/send`. Si utilizas este punto de conexión simultáneamente con los desencadenantes de CDI Canvas y tu integración de API REST, ten en cuenta que el uso combinado se contabilizará en tu límite de velocidad.

Mientras los desencadenantes de CDI Canvas se encuentran en fase de acceso anticipado, ten en cuenta los siguientes detalles:

* Hasta 5 sincronizaciones activas de desencadenantes de Canvas por espacio de trabajo  
* Cada ejecución de sincronización introducirá a los usuarios en su Canvas de destino respectivo a una tasa máxima de aproximadamente 3,75 millones de usuarios por hora.  
  * Prepárate para tiempos de entrada más largos desde el origen hasta Canvas cuando:  
    * Sincronices más de 3,75 millones de usuarios por cada ejecución de sincronización.  
    * Uses los desencadenantes de CDI Canvas cuando ya hayas saturado el [límite de velocidad]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit) de tu API REST [para `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit).