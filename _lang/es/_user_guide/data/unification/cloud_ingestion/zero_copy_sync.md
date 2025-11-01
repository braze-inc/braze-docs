---
nav_title: Personalización de copia cero
article_title: Personalización de copia cero mediante CDI
page_order: 4
page_type: reference
description: "Esta página ofrece un resumen de cómo desencadenar Lienzos Braze utilizando CDI."
---

# Personalización de copia cero mediante CDI

> Aprende a desencadenar Canvas utilizando CDI para una personalización sin copia. Esta característica accede a información específica del usuario desde tu solución de almacenamiento de datos y la pasa a un Canvas de destino. Los pasos en Canvas pueden incluir opcionalmente campos de personalización que no persisten en los perfiles de usuario Braze.

{% alert important %}
Los desencadenantes del CDI Canvas están actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Sincronizar desencadenadores de Canvas

### Pasos de inicio rápido

Si ya estás familiarizado con el CDI de Braze, nota que la configuración para desencadenar una sincronización con Canvas sigue de cerca el proceso de [las integraciones CDI de datos de usuario]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/), con las siguientes salvedades:

- Sólo se admiten identificadores ID externos o alias de usuario. El correo electrónico y los números de teléfono no son identificadores admitidos.  
- Sólo se pueden sincronizar los usuarios existentes de Braze. No se pueden crear nuevos usuarios.  
- `properties` sustituye a la columna `payload`. Se trata de una cadena JSON de los campos que quieres utilizar como propiedades de entrada en Canvas para la personalización.

Para empezar, selecciona el tipo de datos **Desencadenadores de Canvas** al crear una nueva sincronización.

### Utilizar desencadenadores de Canvas 

#### Paso 1: Configurar el origen de datos para desencadenar Canvas

{% tabs %}
{% tab Snowflake %}

##### Paso 1.1: Configura tu tabla de fuentes en Snowflake

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

Puedes nombrar la base de datos, el esquema y la tabla como quieras, pero los nombres de las columnas deben coincidir con la definición anterior.

* `UPDATED_AT`: La hora a la que se actualizó o añadió esta fila a la tabla. Sólo se sincronizarán las filas añadidas o actualizadas desde la última sincronización.  
* O `external_id` o `alias_name` y `alias_label` como columna identificadora del usuario. Identifican a los usuarios para los que quieres desencadenar la mensajería de Canvas.  
  * `EXTERNAL_ID`: Identifica al usuario para entrar en el Canvas. Debe coincidir con el valor `external_id` utilizado en Braze.  
  * `ALIAS_NAME` y `ALIAS_LABEL`: Estas columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero sólo un alias_name por `alias_label`.  
* `PROPERTIES`: Una cadena JSON de campos para que estén disponibles como propiedades de personalización en tu Canvas. Debe contener información específica del usuario.

{% alert note %}
Las propiedades no son necesarias para cada fila o usuario. Sin embargo, los valores de las propiedades deben ser una cadena JSON válida. Introduce una cadena `{}` vacía si no hay propiedades para la fila.
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

Si tu cuenta tiene políticas de red, habilita las IP de Braze para habilitar la conexión del servicio CDI. Para ver la lista de IP, consulta [Ingestión de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).  

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

Puedes nombrar la base de datos, el esquema y la tabla como quieras, pero los nombres de las columnas deben coincidir con la definición anterior.

* `UPDATED_AT`: La hora a la que se actualizó o añadió esta fila a la tabla. Sólo se sincronizarán las filas añadidas o actualizadas desde la última sincronización.  
* O `external_id` o `alias_name` y `alias_label` como columna identificadora del usuario. Identifican a los usuarios para los que quieres desencadenar la mensajería de Canvas.  
  * `EXTERNAL_ID`: Identifica al usuario para entrar en el Canvas. Debe coincidir con el valor `external_id` utilizado en Braze.  
  * `ALIAS_NAME` y `ALIAS_LABEL`: Estas columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y alias_label especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero sólo un `alias_name` por `alias_label`.  
* `PROPERTIES`: Una cadena JSON de campos para que estén disponibles como propiedades de personalización en tu Canvas. Debe contener información específica del usuario.

{% alert note %}
Las propiedades no son necesarias para cada fila o usuario. Sin embargo, los valores de las propiedades deben ser una cadena JSON válida. Introduce una cadena `{}` vacía si no hay propiedades para la fila.
{% endalert %}

##### Paso 1.2: Configurar credenciales

Configura un rol, un almacén y un usuario y concede los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen de los desencadenantes de Canvas.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Paso 1.3: Configurar políticas de red 

Si tu cuenta tiene políticas de red, habilita las IP de Braze para habilitar la conexión del servicio CDI. Para ver la lista de IP, consulta [Ingestión de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Paso 1.1: Crea un nuevo proyecto o conjunto de datos para tu tabla de origen (opcional)

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Paso 1.2: Configura tu tabla de origen en BigQuery
Consulta lo siguiente cuando crees tu tabla de origen:  

| Nombre del campo | Tipo | ¿Es necesario? | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | Marca de tiempo | Sí | 
| **`PROPERTIES`** | JSON | Sí | 
| **`EXTERNAL_ID`** | CADENA | NULABLE | 
| **`ALIAS_NAME`** | CADENA | NULABLE | 
| **`ALIAS_LABEL`** | CADENA | NULABLE |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Las propiedades no son necesarias para cada fila o usuario. Sin embargo, los valores de las propiedades deben ser una cadena JSON válida. Introduce una cadena `{}` vacía si no hay propiedades para la fila.
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
| Usuario de conexión a BigQuery | Permite que Braze se conecte. |
| Usuario de BigQuery | Permite a Braze ejecutar consultas, leer metadatos y listar tablas. |
| Visor de datos BigQuery | Permite a Braze ver conjuntos de datos y contenidos. |
| Usuario de BigQuery Job | Permite a Braze ejecutar trabajos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Tras conceder los permisos, genera una clave JSON. Consulta las instrucciones para [crear y eliminar claves](https://cloud.google.com/iam/docs/keys-create-delete). Más tarde lo cargarás en el panel de Braze.

##### Paso 1.4: Configurar políticas de red 
Si tu cuenta tiene políticas de red, habilita las IP de Braze para habilitar la conexión del servicio CDI. Para ver la lista de IP, consulta [Ingestión de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Paso 1.1: Crea un catálogo o esquema para tu tabla de origen.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Paso 1.2: Configura tu tabla de origen en Databricks

Consulta lo siguiente cuando crees tu tabla de origen:

| Nombre del campo | Tipo | Necesario |
| :---- | :---- | :---- |
| `UPDATED_AT` | Marca de tiempo | Sí |
| `PROPERTIES` | JSON | Sí |
| `EXTERNAL_ID` | CADENA |  NULABLE |
| `ALIAS_NAME` | CADENA | NULABLE |
| `ALIAS_LABEL` | CADENA | NULABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Puedes nombrar el esquema y la tabla como quieras, pero los nombres de las columnas deben coincidir con la definición anterior.

* `UPDATED_AT`: La hora a la que se actualizó o añadió esta fila a la tabla. Sólo se sincronizarán las filas añadidas o actualizadas desde la última sincronización.  
* O `external_id` o `alias_name` y `alias_label` como columna identificadora del usuario. Identifican a los usuarios para los que quieres desencadenar la mensajería de Canvas.  
  * `EXTERNAL_ID`: Identifica al usuario para entrar en el Canvas. Debe coincidir con el valor `external_id` utilizado en Braze.  
  * `ALIAS_NAME` y `ALIAS_LABEL`: Estas columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero sólo un alias_name por `alias_label`.  
* `PROPERTIES`: Una cadena o estructura de campos para que estén disponibles como propiedades de personalización en tu Canvas. Debe contener información específica del usuario.

{% alert note %}
Las propiedades no son necesarias para cada fila o usuario. Sin embargo, los valores de las propiedades deben ser cadenas JSON válidas. Introduce una cadena `{}` vacía si no hay propiedades para la fila.
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

1. Selecciona tu nombre de usuario y, a continuación, selecciona **Configuración de usuario.**  
2. En la pestaña **Tokens de acceso**, selecciona **Generar nuevo token.**  
3. Añade un comentario para identificar el token, como "Braze CDI".  
4. Deja **Vida útil (días** ) en blanco para que no caduque y selecciona **Generar**.  
5. Copia y guarda el token de forma segura para utilizarlo en el panel de Braze.

##### Paso 1.4: Configurar políticas de red 

Si tu cuenta tiene políticas de red, habilita las IP de Braze para habilitar la conexión del servicio CDI. Para ver la lista de IP, consulta [Ingestión de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Fabric %}

##### Paso 1.1: Configura tu tabla de fuentes en Fabric

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

Crea un servicio principal y concede permisos. Si ya tienes credenciales de otra sincronización, puedes reutilizarlas; sólo tienes que asegurarte de que tienen acceso a la tabla de cuentas.

##### Paso 1.3: Configurar políticas de red 

Si tu cuenta tiene políticas de red, habilita las IP de Braze para habilitar la conexión del servicio CDI. Para ver la lista de IP, consulta [Ingestión de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab File Storage %}

Para sincronizar los desencadenantes de Canvas desde el almacenamiento de archivos, crea un archivo fuente con los siguientes campos.

| Campo | Necesario | Descripción |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Sí, uno de `external_id` o `alias_name`, y `alias_label` | Esto identifica al usuario que quieres actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. |
| `ALIAS_NAME` y `ALIAS_LABEL` | Sí, uno de `external_id` o `alias_name` y `alias_label` | Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`. |
| `PROPERTIES` | Sí | Cadena JSON de campos para que estén disponibles como propiedades de personalización en tu Canvas. Debe contener información específica del usuario. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Los nombres de los archivos deben seguir las normas de AWS y ser únicos. Añade marcas de tiempo para garantizar que sea único. Para obtener más información sobre la sincronización con Amazon S3, consulta [Integraciones de almacenamiento de archivos](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### Paso 2: Configura tu Canvas de destino

1. Configura tu Canvas de destino para desencadenar Canvas. Crea un Canvas nuevo o selecciona uno ya existente desencadenado por la API. Consulta [Tipos de horario]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types) de [entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types) para obtener instrucciones sobre cómo crear un Canvas con un tipo de horario de entrega desencadenado por la API.
2. Tras seleccionar el tipo de programa de entrega desencadenado por la API, continúa con la configuración del Canvas y construye tu Canvas. Los lienzos pueden ir desde simples envíos de un solo mensaje hasta complejos flujos de trabajo de clientes con múltiples pasos.
3. Dentro de tus pasos en Canvas, utiliza [las propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) para personalizar los mensajes con los campos de propiedades que piensas sincronizar desde tu tabla de origen.
  * Por ejemplo, si en el Paso 1 has instrumentado un campo de propiedades para `account_balance`, utilizarías la siguiente plantilla Liquid para personalizar tu mensajería: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Después de construir tu Canvas, lánzalo y procede al [Paso 3](#step-3-create-your-zero-copy-sync).

#### Paso 3: Crea tu copia cero de sincronización

Con tu configuración de origen completa y el Canvas de destino iniciado, crea una nueva sincronización de datos:

1. En Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube**.
1. Configura la conexión introduciendo los detalles de la conexión (o reutiliza las credenciales existentes) y la tabla de origen del [Paso 1](#step-1-set-up-data-source-for-canvas-triggers).
2. Da un nombre a la integración.
3. Selecciona el tipo de datos de **los desencadenantes de Canvas**.
4. Elige tu Canvas de destino (del [Paso 2](#step-2-configure-your-destination-canvas)).
5. Elige una frecuencia de sincronización.
6. Configura las preferencias de notificación.
7. Selecciona **Probar conexión** para confirmar que todo funciona como se espera. Si te conectas a Snowflake, añade primero la clave pública que aparece en el panel al usuario creado para Braze para conectarte a Snowflake. Para completar este paso, necesitarás acceso **SECURITYADMIN** o superior en Snowflake. 
8. Guarda la sincronización para empezar a desencadenar Canvas.

Cuando se ejecute la sincronización, los usuarios de tu tabla de origen empezarán a entrar en el Canvas. Utiliza los análisis de Canvas y la página de registros de sincronización de la ingesta de datos en la nube para controlar el rendimiento.

{% alert tip %}  
Revisa toda tu configuración (desde el comportamiento de sincronización hasta la configuración de Canvas) para evitar envíos inesperados. Las configuraciones de Canvas, como la limitación de tasa, el límite de frecuencia y los filtros de segmentación, pueden refinar aún más la entrega de mensajes.<br><br>Recomendamos realizar una prueba con una audiencia pequeña o de prueba antes de poner en práctica los casos de uso en producción.
{% endalert %}

### Consideraciones

Los desencadenantes de CDI Canvas utilizan tu límite de velocidad de la API REST para `/canvas/trigger/send`. Si utilizas este punto final simultáneamente con desencadenadores CDI Canvas y tu integración API REST, espera que el uso combinado cuente para tu límite de velocidad.

Aunque los desencadenantes del CDI Canvas están en acceso temprano, ten en cuenta los siguientes detalles:

* Hasta 5 sincronizaciones activas del desencadenador Canvas por espacio de trabajo  
* Cada ejecución de sincronización introducirá usuarios en su respectivo Canvas de destino a una tasa máxima de aproximadamente 3,75 millones de usuarios por hora.  
  * Prepárate para tiempos de entrada de la fuente al Canvas más largos cuando:  
    * Sincronización de más de 3,75M de usuarios por ejecución de sincronización.  
    * Utiliza los desencadenantes del CDI Canvas cuando ya estés saturando el límite de velocidad de tu API REST para [ `/canvas/trigger/send`.]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit)