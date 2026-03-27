---
nav_title: Integración de almacenes de datos
article_title: Integración de almacenes de datos
alias: /partners/databricks/
description: "Esta página explica cómo utilizar la ingesta de datos en la nube de Braze para sincronizar datos relevantes con tu integración de Snowflake, Redshift, BigQuery y Databricks."
page_order: 2
page_type: reference

---

# Integraciones de almacenamiento de almacén de datos

> Esta página explica cómo utilizar la ingesta de datos en la nube (CDI) de Braze para sincronizar datos relevantes con tu integración de Snowflake, Redshift, BigQuery y Databricks.

Esta página muestra los pasos de sincronización y origen que actualmente están en acceso anticipado (EA). Para los pasos e imágenes de la experiencia de disponibilidad general, despliega **Experiencia de disponibilidad general** a continuación.

## Configuración de integraciones de almacenes de datos

Las integraciones de la ingesta de datos en la nube requieren cierta configuración en Braze y en tu instancia de almacén de datos. Sigue estos pasos para configurar la integración:

{% tabs %}
{% tab Snowflake %}
1. En tu instancia de Snowflake, configura las tablas o vistas que quieras sincronizar con Braze.
2. Crea una nueva fuente de Snowflake en el dashboard de Braze.
3. Recupera la clave pública proporcionada en el dashboard de Braze y [añádela al usuario de Snowflake para la autenticación](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Crea una sincronización en el dashboard de Braze, prueba la integración e inicia la sincronización.

{% alert tip %}
La [guía de inicio rápido de Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) proporciona código de ejemplo y recorre los pasos necesarios para crear una canalización automatizada utilizando Snowflake Streams y CDI para sincronizar datos con Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Asegúrate de que se permite el acceso de Braze a las tablas de Redshift que deseas sincronizar. Braze se conecta a Redshift a través de Internet.
2. En tu instancia de Redshift, configura las tablas o vistas que quieras sincronizar con Braze.
3. Crea una nueva fuente y sincronización en el dashboard de Braze.
4. Prueba la integración e inicia la sincronización.
{% endtab %}
{% tab BigQuery %}
1. Crea una cuenta de servicio y permite el acceso a los proyectos de BigQuery y a los conjuntos de datos que contienen los datos que deseas sincronizar.  
2. En tu cuenta de BigQuery, configura las tablas o vistas que quieras sincronizar con Braze.   
3. Crea una nueva fuente y sincronización en el dashboard de Braze.  
4. Prueba la integración e inicia la sincronización. 
{% endtab %}
{% tab Databricks %}
1. Crea una cuenta de servicio y permite el acceso a los proyectos y conjuntos de datos de Databricks que contienen los datos que deseas sincronizar.  
2. En tu cuenta de Databricks, configura las tablas o vistas que quieras sincronizar con Braze.   
3. Crea una nueva fuente y sincronización en el dashboard de Braze.
4. Prueba la integración e inicia la sincronización.

{% alert important %}
Puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecta a las instancias Classic y Pro SQL, lo que puede provocar retrasos durante la configuración de la conexión y las pruebas, así como al inicio de las sincronizaciones programadas. El uso de una instancia SQL sin servidor minimiza el tiempo de calentamiento y mejora el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Crea un principal de servicio y concede acceso a las API de Fabric.
2. Configura un espacio de trabajo compartido y concede al principal de servicio acceso a él.
3. En el espacio de trabajo compartido de Fabric, configura las tablas o vistas que quieras sincronizar con Braze.   
4. Crea una nueva fuente y sincronización en el dashboard de Braze.  
5. Prueba la integración e inicia la sincronización.
{% endtab %}
{% endtabs %}

### Paso 1: Configurar tablas o vistas

{% tabs %}
{% tab Snowflake %}

#### Paso 1.1: Preparar la tabla

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Puedes nombrar la base de datos, el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora a la que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificador de usuario** - Tu tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, el correo electrónico se utilizará como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
- `PAYLOAD` - Se trata de una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.

#### Paso 1.2: Configurar el rol y los permisos de la base de datos

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Actualiza los nombres según sea necesario, pero los permisos deben coincidir con el ejemplo anterior.

#### Paso 1.3: Configurar el almacén y dar acceso al rol de Braze

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
El almacén debe tener activada la opción de **reanudación automática**. Si no es así, concede a Braze privilegios adicionales de `OPERATE` en el almacén para que Braze pueda activarlo cuando se ejecute la consulta.
{% endalert %}

#### Paso 1.4: Configurar el usuario

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Después de este paso, comparte la información de conexión con Braze para recibir una clave pública que adjuntar al usuario.

{% alert note %}
Cuando conectes diferentes espacios de trabajo a la misma cuenta de Snowflake, debes crear un usuario único para cada espacio de trabajo de Braze en el que estés creando una integración. Dentro de un espacio de trabajo, puedes reutilizar el mismo usuario en todas las integraciones, pero la creación de la integración falla si un usuario de la misma cuenta de Snowflake se duplica en distintos espacios de trabajo.
{% endalert %}

#### Paso 1.5: Permitir las IP de Braze en la política de redes de Snowflake (opcional)

Dependiendo de la configuración de tu cuenta de Snowflake, puede que necesites permitir las siguientes direcciones IP en tu política de red de Snowflake. Para obtener más información sobre cómo habilitarlo, consulta la documentación pertinente de Snowflake sobre la [modificación de una política de red](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Paso 1.1: Preparar la tabla 

Opcionalmente, configura una nueva base de datos y un nuevo esquema para albergar tu tabla de origen
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Crea una tabla (o vista) para utilizarla en tu integración CDI
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Puedes nombrar la base de datos, el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora a la que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificador de usuario** - Tu tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, el correo electrónico se utilizará como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
- `PAYLOAD` - Se trata de una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.
 
#### Paso 1.2: Crear usuario y conceder permisos

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Estos son los permisos mínimos requeridos para este usuario. Si creas varias integraciones CDI, puede que desees conceder permisos a un esquema o gestionar los permisos mediante un grupo. 

#### Paso 1.3: Permitir el acceso a las IP de Braze

Si tienes un cortafuegos u otras políticas de red, debes dar acceso de red a Braze a tu instancia de Redshift. Un ejemplo de punto de conexión URL de Redshift es "example-cluster.ap-northeast-2.redshift.amazonaws.com".

Algunas cosas importantes que debes saber:
- Es posible que también tengas que cambiar tus grupos de seguridad para permitir que Braze acceda a tus datos en Redshift.
- Asegúrate de permitir explícitamente el tráfico entrante en las IP de la tabla y en el puerto utilizado para consultar tu clúster de Redshift (por defecto es 5439). Debes permitir explícitamente la conectividad TCP de Redshift en este puerto incluso si las reglas de entrada están configuradas para "permitir todo".
- El punto de conexión del clúster de Redshift debe ser de acceso público para que Braze se conecte a tu clúster.
     - Si no quieres que tu clúster de Redshift sea accesible públicamente, puedes configurar una VPC y una instancia EC2 para que utilicen un túnel SSH para acceder a los datos de Redshift. Para más información, consulta esta [publicación del Centro de conocimientos de AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).
 
Permite el acceso desde las siguientes IP correspondientes a la región de tu dashboard de Braze.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Paso 1.1: Preparar la tabla 

Si lo deseas, puedes crear un nuevo proyecto o conjunto de datos que contenga la tabla de origen.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o más tablas para utilizar en tu integración CDI con los siguientes campos:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Puedes nombrar el proyecto, el conjunto de datos y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora a la que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificador de usuario** - Tu tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, el correo electrónico se utilizará como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
- `PAYLOAD` - Se trata de una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.

{% alert important %}
**Partición de BigQuery**

CDI admite particiones para BigQuery. Si realizas la partición mediante una función de `UPDATED_AT` (por ejemplo, con una granularidad diaria, semanal o por hora, dependiendo del tamaño del conjunto de datos), BigQuery puede recortar los datos que necesita analizar. Esto mejora el rendimiento y la eficiencia en tablas muy grandes.

No particiones por ningún otro campo. Prueba diferentes configuraciones para encontrar la mejor opción para tus datos específicos.

Todas las consultas CDI se filtran por `UPDATED_AT`, pero este comportamiento podría cambiar. Diseña el esquema de tu tabla de manera que las consultas _no_ requieran incluir esta cláusula.

Para obtener más información, consulta la [documentación sobre partición de BigQuery](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).
{% endalert %}

#### Paso 1.2: Crear una cuenta de servicio y conceder permisos 

Crea una cuenta de servicio en GCP para que Braze la utilice para conectarse y leer datos de tus tablas. La cuenta de servicio debe tener los siguientes permisos: 

- **BigQuery Connection User:** Permite a Braze realizar conexiones.
- **BigQuery User:** Proporciona a Braze acceso para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- **BigQuery Data Viewer:** Proporciona a Braze acceso para ver los conjuntos de datos y su contenido.
- **BigQuery Job User:** Proporciona a Braze acceso para ejecutar trabajos.

Tras crear la cuenta de servicio y conceder los permisos, genera una clave JSON. Para más información, consulta [Crear y eliminar claves de cuentas de servicio](https://cloud.google.com/iam/docs/keys-create-delete). La cargarás en el dashboard de Braze en un paso posterior. 

#### Paso 1.3: Permitir el acceso a las IP de Braze    

Si tienes políticas de red en vigor, debes dar acceso de red a Braze a tu instancia de BigQuery. Permite el acceso desde las siguientes IP correspondientes a la región de tu dashboard de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Paso 1.1: Preparar la tabla 

Opcionalmente, configura un nuevo catálogo o esquema para contener tu tabla de origen.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o más tablas para utilizar en tu integración CDI con los siguientes campos:


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| STRING, STRUCT o MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Puedes nombrar el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora a la que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificador de usuario** - Tu tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario. 
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, el correo electrónico se utilizará como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
- `PAYLOAD` - Se trata de una cadena o estructura de los campos que deseas sincronizar con el usuario en Braze.

#### Paso 1.2: Crear un token de acceso  

Para que Braze acceda a Databricks, es necesario crear un token de acceso personal.

1. En tu espacio de trabajo de Databricks, selecciona tu nombre de usuario de Databricks en la barra superior y, a continuación, selecciona **User Settings** en el desplegable.
2. En la pestaña Access tokens, selecciona **Generate new token**.
3. Introduce un comentario que te ayude a identificar este token, como "Braze CDI", y cambia la vida útil del token a sin vida útil dejando la casilla Lifetime (days) vacía (en blanco).
4. Selecciona **Generate**.
5. Copia el token mostrado y selecciona **Done**.

Guarda el token en un lugar seguro hasta que necesites introducirlo en el dashboard de Braze durante el paso de creación de credenciales.

#### Paso 1.3: Permitir el acceso a las IP de Braze    

Si tienes políticas de red en vigor, debes dar acceso de red a Braze a tu instancia de Databricks. Permite el acceso desde las siguientes IP correspondientes a la región de tu dashboard de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Paso 1.1: Configurar el principal de servicio y conceder acceso
Braze se conecta a tu almacén de Fabric utilizando un principal de servicio con autenticación Entra ID. Crea un nuevo principal de servicio para que lo utilice Braze y concede acceso a los recursos de Fabric según sea necesario. Braze necesita los siguientes datos para conectarse:    

* Tenant ID (también llamado directorio) de tu cuenta de Azure 
* Principal ID (también llamado ID de aplicación) del principal de servicio 
* Secreto de cliente para que Braze se autentique

1. En el portal de Azure, ve al centro de administración de Microsoft Entra y, a continuación, a App Registrations. 
2. Selecciona **+ New registration** en **Identity** > **Applications** > **App registrations**.
3. Introduce un nombre y, a continuación, selecciona `Accounts in this organizational directory only` como tipo de cuenta admitido. A continuación, selecciona **Register**. 
4. Selecciona la aplicación (principal de servicio) que acabas de crear y, a continuación, ve a **Certificates & secrets** > **+ New client secret**.
5. Introduce una descripción para el secreto y establece un periodo de caducidad para el secreto. Después, selecciona **Add**. 
6. Toma nota del secreto de cliente creado para utilizarlo en la configuración de Braze. 

{% alert note %}
Azure no permite la caducidad ilimitada de los secretos de principal de servicio. Recuerda actualizar las credenciales antes de que caduquen para mantener el flujo de datos hacia Braze.
{% endalert %}

#### Paso 1.2: Conceder acceso a los recursos de Fabric 
Proporciona acceso para que Braze se conecte a tu instancia de Fabric. En tu portal de administración de Fabric, ve a **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.    

* En **Developer settings**, habilita **Service principals can use Fabric APIs** para que Braze pueda conectarse utilizando Microsoft Entra ID.
* En **OneLake settings**, habilita **Users can access data stored in OneLake with apps external to Fabric** para que el principal de servicio pueda acceder a los datos desde una aplicación externa.

#### Paso 1.3: Configurar un espacio de trabajo compartido y conceder acceso

Cualquier recurso de Fabric que quieras conectar a Braze debe colocarse en un espacio de trabajo compartido. Si solo has estado usando el espacio de trabajo predeterminado **My Workspace**, crea un nuevo espacio de trabajo compartido:

1. En el menú de navegación, selecciona **Workspaces** y luego selecciona **+ New workspace**.
2. Introduce un **Name** para el espacio de trabajo y selecciona **Apply**.

Una vez que tengas un espacio de trabajo compartido, concede acceso al principal de servicio:

1. Selecciona el espacio de trabajo y luego selecciona **Manage Access**.
2. Selecciona **+ Add people or groups**.
3. Busca y selecciona el nombre del principal de servicio que creaste en el paso 1.1. Si no aparece, confirma que has habilitado la configuración **Service principals can use Fabric APIs** en el paso 1.2.
4. En el desplegable de rol, selecciona **Contributor**.

El principal de servicio ahora puede acceder a los recursos del almacén de Fabric en este espacio de trabajo a través de sus puntos de conexión SQL, incluido el almacén que se utilizará para Braze.

#### Paso 1.4: Preparar la tabla
Braze admite tanto tablas como vistas en Fabric Warehouses. Si necesitas crear un nuevo almacén, créalo dentro del espacio de trabajo compartido del paso 1.3. Ve a **Create > Data Warehouse > Warehouse** en la consola de Fabric.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Puedes nombrar el almacén, el esquema y la tabla o vista como quieras, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora a la que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificador de usuario** - Tu tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, el correo electrónico se utilizará como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
- `PAYLOAD` - Se trata de una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.


#### Paso 1.5: Obtener la cadena de conexión del almacén
Para recuperar el punto de conexión SQL de tu almacén, ve al **espacio de trabajo** en Fabric, pasa el ratón por encima del nombre del almacén en la lista de elementos y selecciona **Copy SQL connection string**.

![La página "Fabric Console" en Microsoft Azure, donde los usuarios deben recuperar la cadena de conexión SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Paso 1.6: Permitir IP de Braze en el cortafuegos (opcional)

Dependiendo de la configuración de tu cuenta de Microsoft Fabric, puede que necesites permitir las siguientes direcciones IP en tu cortafuegos para permitir el tráfico desde Braze. Para más información sobre cómo habilitarlo, consulta la documentación correspondiente sobre el [acceso condicional de Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Paso 2: Crear una nueva fuente en el dashboard de Braze

{% alert important %}
Los clientes que se incorporen en febrero de 2026 o después pueden tener acceso anticipado a la interfaz de CDI con fuentes y sincronizaciones separadas. En esta interfaz, crea una fuente antes de crear sincronizaciones para esa fuente. Varias sincronizaciones pueden usar la misma fuente.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

En el dashboard de Braze, ve a **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecciona **Add data source** y, a continuación, selecciona **Snowflake**.

#### Paso 2.1: Añadir información de conexión de Snowflake

Elige un nombre para tu fuente e introduce tus credenciales y configuración de Snowflake, y luego pasa al siguiente paso.

{% alert note %}
En el campo **Snowflake Account Locator**, introduce tu [identificador de cuenta](https://docs.snowflake.com/en/user-guide/admin-account-identifier) de Snowflake, que suele seguir un formato como `xy12345.us-east-1.aws`. No es lo mismo que el nombre de una base de datos o el nombre de un almacén.
{% endalert %} 

#### Paso 2.2: Añadir una clave pública al usuario de Braze

Después de introducir tus credenciales y configuración, haz clic en **Save credentials** y genera una clave RSA, luego vuelve a Snowflake para completar la configuración. Añade la clave pública que aparece en el dashboard al usuario que creaste para que Braze se conecte a Snowflake.

Para más información sobre cómo hacerlo, consulta la [documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si deseas rotar las claves en cualquier momento, Braze puede generar un nuevo par de claves y proporcionarte la nueva clave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

En el dashboard de Braze, ve a **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecciona **Add data source** y, a continuación, selecciona **Amazon Redshift**.

#### Paso 2.1: Añadir información de conexión de Redshift y tabla de origen

Elige un nombre para tu fuente e introduce tus credenciales y configuración de Redshift. Si utilizas un túnel de red privada, activa el control deslizante e introduce la información del túnel. A continuación, pasa al siguiente paso. 

{% alert note %}
En el dashboard de Braze, el campo **Database name** solo acepta letras (A–Z, a–z), números (0–9) y guiones bajos (_), aunque Amazon Redshift admite caracteres adicionales en los identificadores de bases de datos.
{% endalert %}

#### Paso 2.2: Probar conexión y conectar a la fuente

A continuación, selecciona **Test connection**. Si la prueba es exitosa, finaliza la configuración restante y haz clic en **Connect to Source**. Si la conexión falla, aparece un mensaje de error para ayudarte a solucionar el problema.
{% endtab %}
{% tab BigQuery %}

En el dashboard de Braze, ve a **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecciona **Add data source** y, a continuación, selecciona **Google BigQuery**.

#### Paso 2.1: Añadir información de conexión de BigQuery y tabla de origen

Elige un nombre para tu fuente. Luego, carga la clave JSON y proporciona un nombre para la cuenta de servicio. A continuación, introduce los campos de configuración restantes.

#### Paso 2.2: Probar conexión y conectar a la fuente

A continuación, selecciona **Test connection**. Si la prueba es exitosa, finaliza la configuración restante y haz clic en **Connect to Source**. Si la conexión falla, aparece un mensaje de error para ayudarte a solucionar el problema.

{% endtab %}
{% tab Databricks %}

En el dashboard de Braze, ve a **Data Settings** > **Cloud Data Ingestion** > **Sources**, selecciona **Add data source** y, a continuación, selecciona **Databricks**.

#### Paso 2.1: Añadir información de conexión de Databricks y tabla de origen

Elige un nombre para tu fuente e introduce tus credenciales y configuración de Databricks. A continuación, pasa al siguiente paso.

#### Paso 2.2: Probar conexión y conectar a la fuente

A continuación, selecciona **Test connection**. Si la prueba es exitosa, finaliza la configuración restante y haz clic en **Connect to Source**. Si la conexión falla, aparece un mensaje de error para ayudarte a solucionar el problema.

{% alert note %}
Debes probar con éxito una fuente antes de que pueda ser creada. Si cierras la página de creación, tu fuente no se guardará.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

En el dashboard de Braze, ve a Data Settings > Cloud Data Ingestion > Sources, selecciona **Add data source** y, a continuación, selecciona **Microsoft Fabric**.

#### Paso 2.1: Configurar una sincronización de ingesta de datos en la nube

Elige un nombre para tu fuente e introduce tus credenciales y configuración de Microsoft Fabric.
- **Credentials Name** es una etiqueta para estas credenciales en Braze; puedes establecer un valor descriptivo aquí
- Consulta los pasos de la sección 1 para obtener información detallada sobre cómo recuperar el Tenant ID, el Principal ID, el secreto de cliente y la cadena de conexión

#### Paso 2.2: Probar conexión y conectar a la fuente

A continuación, selecciona **Test connection**. Si la prueba es exitosa, finaliza la configuración restante y haz clic en **Connect to Source**. Si la conexión falla, aparece un mensaje de error para ayudarte a solucionar el problema.

{% alert note %}
Debes probar con éxito una fuente antes de que pueda ser creada. Si cierras la página de creación, tu fuente no se guardará.
{% endalert %}

{% endtab %}

{% endtabs %}

### Paso 3: Crear una nueva sincronización en el dashboard de Braze
Ve a **Data Settings** > **Cloud Data Ingestion** > **Syncs** y selecciona **Create data sync**.

{% tabs %}
{% tab Snowflake %}

#### Paso 3.1: Configurar los detalles de sincronización y probar la conexión
Elige un nombre para tu sincronización. Luego, selecciona cualquier fuente activa e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y haz clic en **Test Connection**.

Si la prueba es exitosa, aparece una vista previa de los datos. Selecciona **Next: Notifications** para continuar. Si la conexión falla, aparece un mensaje de error para ayudarte a solucionar el problema.

{% alert note %}
Debes probar con éxito una sincronización antes de avanzar a los siguientes pasos. Si necesitas salir de la página de creación de sincronización, haz clic en **Save as draft** para guardar tu trabajo en progreso.
{% endalert %}

#### Paso 3.2: Añadir preferencias de notificación
Introduce los correos electrónicos de contacto para las notificaciones de errores de sincronización. Braze utiliza esta información de contacto para enviar notificaciones sobre errores de integración, como la pérdida inesperada de acceso a la tabla.

Los correos electrónicos de contacto solo reciben notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No reciben problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. 

Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Solo para sincronización de catálogos) No hay espacio en el nivel de catálogo

#### Paso 3.3: Planificación
Por último, configura tu sincronización como no recurrente o recurrente.

Las sincronizaciones no recurrentes se pueden desencadenar manualmente o a través de la API.

Las sincronizaciones recurrentes pueden tener una frecuencia desde cada 15 minutos hasta una vez al mes. Braze utiliza la zona horaria configurada en tu dashboard de Braze para programar la sincronización recurrente.

{% endtab %}

{% tab Redshift %}

#### Paso 3.1: Configurar los detalles de sincronización y probar la conexión
Elige un nombre para tu sincronización. Luego, selecciona cualquier fuente activa e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y haz clic en **Test Connection**.

Si la prueba es exitosa, aparece una vista previa de los datos. Selecciona **Next: Notifications** para continuar. Si la conexión falla, aparece un mensaje de error para ayudarte a solucionar el problema.

{% alert note %}
Debes probar con éxito una sincronización antes de avanzar a los siguientes pasos. Si necesitas salir de la página de creación de sincronización, haz clic en **Save as draft** para guardar tu trabajo en progreso.
{% endalert %}

#### Paso 3.2: Añadir preferencias de notificación
Introduce los correos electrónicos de contacto para las notificaciones de errores de sincronización. Braze utiliza esta información de contacto para enviar notificaciones sobre errores de integración, como la pérdida inesperada de acceso a la tabla.

Los correos electrónicos de contacto solo reciben notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No reciben problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. 

Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos

(Solo para sincronización de catálogos) No hay espacio en el nivel de catálogo

#### Paso 3.3: Planificación
Por último, configura tu sincronización como no recurrente o recurrente.

Las sincronizaciones no recurrentes se pueden desencadenar manualmente o a través de la API.

Las sincronizaciones recurrentes pueden tener una frecuencia desde cada 15 minutos hasta una vez al mes. Braze utiliza la zona horaria configurada en tu dashboard de Braze para programar la sincronización recurrente.

{% endtab %}

{% tab BigQuery %}

#### Paso 3.1: Configurar los detalles de sincronización y probar la conexión
Elige un nombre para tu sincronización. Luego, selecciona cualquier fuente activa e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y haz clic en **Test Connection**.

Si la prueba es exitosa, aparece una vista previa de los datos. Selecciona **Next: Notifications** para continuar. Si la conexión falla, aparece un mensaje de error para ayudarte a solucionar el problema.

{% alert note %}
Debes probar con éxito una sincronización antes de avanzar a los siguientes pasos. Si necesitas salir de la página de creación de sincronización, haz clic en **Save as draft** para guardar tu trabajo en progreso.
{% endalert %}

#### Paso 3.2: Añadir preferencias de notificación
Introduce los correos electrónicos de contacto para las notificaciones de errores de sincronización. Braze utiliza esta información de contacto para enviar notificaciones sobre errores de integración, como la pérdida inesperada de acceso a la tabla.

Los correos electrónicos de contacto solo reciben notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No reciben problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos

(Solo para sincronización de catálogos) No hay espacio en el nivel de catálogo

#### Paso 3.3: Planificación
Por último, configura tu sincronización como no recurrente o recurrente.

Las sincronizaciones no recurrentes se pueden desencadenar manualmente o a través de la API.

Las sincronizaciones recurrentes pueden tener una frecuencia desde cada 15 minutos hasta una vez al mes. Braze utiliza la zona horaria configurada en tu dashboard de Braze para programar la sincronización recurrente.

{% endtab %}

{% tab Databricks %}

#### Paso 3.1: Configurar los detalles de sincronización y probar la conexión
Elige un nombre para tu sincronización. Luego, selecciona cualquier fuente activa e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y haz clic en **Test Connection**.

Si la prueba es exitosa, aparece una vista previa de los datos. Selecciona **Next: Notifications** para continuar. Si la conexión falla, aparece un mensaje de error para ayudarte a solucionar el problema.

{% alert note %}
Debes probar con éxito una sincronización antes de avanzar a los siguientes pasos. Si necesitas salir de la página de creación de sincronización, haz clic en **Save as draft** para guardar tu trabajo en progreso.
{% endalert %}

#### Paso 3.2: Añadir preferencias de notificación
Introduce los correos electrónicos de contacto para las notificaciones de errores de sincronización. Braze utiliza esta información de contacto para enviar notificaciones sobre errores de integración, como la pérdida inesperada de acceso a la tabla.

Los correos electrónicos de contacto solo reciben notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No reciben problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. 

Estos problemas pueden incluir lo siguiente:
- Problemas de conectividad
- Falta de recursos
- Problemas de permisos

(Solo para sincronización de catálogos) No hay espacio en el nivel de catálogo

#### Paso 3.3: Planificación
Por último, configura tu sincronización como no recurrente o recurrente.

Las sincronizaciones no recurrentes se pueden desencadenar manualmente o a través de la API.

Las sincronizaciones recurrentes pueden tener una frecuencia desde cada 15 minutos hasta una vez al mes. Braze utiliza la zona horaria configurada en tu dashboard de Braze para programar la sincronización recurrente.

{% endtab %}
{% tab Microsoft Fabric %}

#### Paso 3.1: Configurar los detalles de sincronización y probar la conexión

Elige un nombre para tu sincronización. Luego, selecciona cualquier fuente activa e introduce tu tabla de origen para la sincronización. Selecciona un tipo de datos y haz clic en **Test Connection**.

Si la prueba es exitosa, aparece una vista previa de los datos. Selecciona **Next: Notifications** para continuar. Si la conexión falla, aparece un mensaje de error para ayudarte a solucionar el problema.

{% alert note %}
Debes probar con éxito una sincronización antes de avanzar a los siguientes pasos. Si necesitas salir de la página de creación de sincronización, haz clic en **Save as draft** para guardar tu trabajo en progreso.
{% endalert %}

#### Paso 3.2: Añadir preferencias de notificación
Introduce los correos electrónicos de contacto para las notificaciones de errores de sincronización. Braze utiliza esta información de contacto para enviar notificaciones sobre errores de integración, como la pérdida inesperada de acceso a la tabla.

Los correos electrónicos de contacto solo reciben notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No reciben problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. 

Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos

(Solo para sincronización de catálogos) No hay espacio en el nivel de catálogo

#### Paso 3.3: Planificación
Por último, configura tu sincronización como no recurrente o recurrente.

Las sincronizaciones no recurrentes se pueden desencadenar manualmente o a través de la API.

Las sincronizaciones recurrentes pueden tener una frecuencia desde cada 15 minutos hasta una vez al mes. Braze utiliza la zona horaria configurada en tu dashboard de Braze para programar la sincronización recurrente.

{% endtab %}
{% endtabs %}

{% alert note %}
Debes probar con éxito una integración antes de que pueda pasar del estado Borrador al Activo. Si cierras la página de creación, tu integración se guarda y puedes volver a visitar la página de detalles para realizar cambios y pruebas.  
{% endalert %}

## Configurar integraciones o usuarios adicionales (opcional)

{% tabs %}
{% tab Snowflake %}
Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Snowflake.

Si reutilizas el mismo usuario y rol en todas las integraciones, no necesitas volver a añadir la clave pública.
{% endtab %}
{% tab Redshift %}
Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Snowflake o Redshift.

Si reutilizas el mismo usuario en varias integraciones, no podrás eliminar el usuario en el dashboard de Braze hasta que se elimine de todas las sincronizaciones activas.
{% endtab %}
{% tab BigQuery %}

Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de BigQuery.

Si reutilizas el mismo usuario en varias integraciones, no podrás eliminar el usuario en el dashboard de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% tab Databricks %}

Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Databricks.

Si reutilizas el mismo usuario en varias integraciones, no podrás eliminar el usuario en el dashboard de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% tab Microsoft Fabric %}

Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Fabric.

Si reutilizas el mismo usuario en varias integraciones, no podrás eliminar el usuario en el dashboard de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% endtabs %}

## Ejecución de la sincronización

{% tabs %}
{% tab Snowflake %}
Una vez activada, la sincronización se ejecuta según la planificación configurada durante la instalación. Si deseas ejecutar la sincronización fuera de la planificación normal de pruebas o recuperar los datos más recientes, selecciona **Sync Now**. Esta ejecución no afecta a las futuras sincronizaciones programadas regularmente.

{% endtab %}
{% tab Redshift %}
Una vez activada, la sincronización se ejecuta según la planificación configurada durante la instalación. Si deseas ejecutar la sincronización fuera de la planificación normal de pruebas o recuperar los datos más recientes, selecciona **Sync Now**. Esta ejecución no afecta a las futuras sincronizaciones programadas regularmente.

{% endtab %}
{% tab BigQuery %}

Una vez activada, la sincronización se ejecuta según la planificación configurada durante la instalación. Si deseas ejecutar la sincronización fuera de la planificación normal de pruebas o recuperar los datos más recientes, selecciona **Sync Now**. Esta ejecución no afecta a las futuras sincronizaciones programadas regularmente.

{% endtab %}
{% tab Databricks %}

Una vez activada, la sincronización se ejecuta según la planificación configurada durante la instalación. Si deseas ejecutar la sincronización fuera de la planificación normal de pruebas o recuperar los datos más recientes, selecciona **Sync Now**. Esta ejecución no afecta a las futuras sincronizaciones programadas regularmente.

{% endtab %}
{% tab Microsoft Fabric %}

Una vez activada, la sincronización se ejecuta según la planificación configurada durante la instalación. Si deseas ejecutar la sincronización fuera de la planificación normal de pruebas o recuperar los datos más recientes, selecciona **Sync Now**. Esta ejecución no afecta a las futuras sincronizaciones programadas regularmente.

{% endtab %}

{% endtabs %}

{% details Experiencia de disponibilidad general %}

## Configuración de integraciones de almacenes de datos

Las integraciones de la ingesta de datos en la nube requieren cierta configuración en Braze y en tu instancia de almacén de datos. Sigue estos pasos para configurar la integración:

{% tabs %}
{% tab Snowflake %}
1. En tu instancia de Snowflake, configura las tablas o vistas que quieras sincronizar con Braze.
2. Crea una nueva integración en el dashboard de Braze.
3. Recupera la clave pública proporcionada en el dashboard de Braze y [añádela al usuario de Snowflake para la autenticación](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Prueba la integración e inicia la sincronización.

{% alert tip %}
La [guía de inicio rápido de Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) proporciona código de ejemplo y recorre los pasos necesarios para crear una canalización automatizada utilizando Snowflake Streams y CDI para sincronizar datos con Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Asegúrate de que se permite el acceso de Braze a las tablas de Redshift que deseas sincronizar. Braze se conectará a Redshift a través de Internet.
2. En tu instancia de Redshift, configura las tablas o vistas que quieras sincronizar con Braze.
3. Crea una nueva integración en el dashboard de Braze.
4. Prueba la integración e inicia la sincronización.
{% endtab %}
{% tab BigQuery %}
1. Crea una cuenta de servicio y permite el acceso a los proyectos de BigQuery y a los conjuntos de datos que contienen los datos que deseas sincronizar.  
2. En tu cuenta de BigQuery, configura las tablas o vistas que quieras sincronizar con Braze.   
3. Crea una nueva integración en el dashboard de Braze.  
4. Prueba la integración e inicia la sincronización.  
{% endtab %}
{% tab Databricks %}
1. Crea una cuenta de servicio y permite el acceso a los proyectos y conjuntos de datos de Databricks que contienen los datos que deseas sincronizar.  
2. En tu cuenta de Databricks, configura las tablas o vistas que quieras sincronizar con Braze.   
3. Crea una nueva integración en el dashboard de Braze.  
4. Prueba la integración e inicia la sincronización.

{% alert important %}
Puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecte a las instancias Classic y Pro SQL, lo que provocará retrasos durante la configuración de la conexión y las pruebas, así como al inicio de las sincronizaciones programadas. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Crea un principal de servicio y concede acceso a las API de Fabric.
2. Configura un espacio de trabajo compartido y concede al principal de servicio acceso a él.
3. En el espacio de trabajo compartido de Fabric que creaste en el paso 2, configura las tablas o vistas que quieras sincronizar con Braze.   
4. Crea una nueva integración en el dashboard de Braze.  
5. Prueba la integración e inicia la sincronización.
{% endtab %}
{% endtabs %}

### Paso 1: Configurar tablas o vistas

{% tabs %}
{% tab Snowflake %}

#### Paso 1.1: Preparar la tabla

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Puedes nombrar la base de datos, el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora a la que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificador de usuario** - Tu tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, el correo electrónico se utilizará como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
- `PAYLOAD` - Se trata de una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.

#### Paso 1.2: Configurar el rol y los permisos de la base de datos

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Actualiza los nombres según sea necesario, pero los permisos deben coincidir con el ejemplo anterior.

#### Paso 1.3: Configurar el almacén y dar acceso al rol de Braze

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
El almacén debe tener activada la opción de **reanudación automática**. Si no es así, tendrás que conceder a Braze privilegios adicionales de `OPERATE` en el almacén para que podamos activarlo cuando llegue el momento de ejecutar la consulta.
{% endalert %}

#### Paso 1.4: Configurar el usuario

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Después de este paso, compartirás la información de conexión con Braze y recibirás una clave pública para adjuntar al usuario.

{% alert note %}
Cuando conectes diferentes espacios de trabajo a la misma cuenta de Snowflake, debes crear un usuario único para cada espacio de trabajo de Braze en el que estés creando una integración. Dentro de un espacio de trabajo, puedes reutilizar el mismo usuario en todas las integraciones, pero la creación de la integración fallará si un usuario de la misma cuenta de Snowflake se duplica en distintos espacios de trabajo.
{% endalert %}

#### Paso 1.5: Permitir las IP de Braze en la política de redes de Snowflake (opcional)

Dependiendo de la configuración de tu cuenta de Snowflake, puede que necesites permitir las siguientes direcciones IP en tu política de red de Snowflake. Para obtener más información sobre cómo habilitarlo, consulta la documentación pertinente de Snowflake sobre la [modificación de una política de red](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Paso 1.1: Preparar la tabla 

Opcionalmente, configura una nueva base de datos y un nuevo esquema para albergar tu tabla de origen
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Crea una tabla (o vista) para utilizarla en tu integración CDI
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Puedes nombrar la base de datos, el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora a la que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificador de usuario** - Tu tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, el correo electrónico se utilizará como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
- `PAYLOAD` - Se trata de una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.
 
#### Paso 1.2: Crear usuario y conceder permisos

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Estos son los permisos mínimos requeridos para este usuario. Si creas varias integraciones CDI, puede que desees conceder permisos a un esquema o gestionar los permisos mediante un grupo. 

#### Paso 1.3: Permitir el acceso a las IP de Braze

Si tienes un cortafuegos u otras políticas de red, debes dar acceso de red a Braze a tu instancia de Redshift. Un ejemplo de punto de conexión URL de Redshift es "example-cluster.ap-northeast-2.redshift.amazonaws.com".

Algunas cosas importantes que debes saber:
- Es posible que también tengas que cambiar tus grupos de seguridad para permitir que Braze acceda a tus datos en Redshift.
- Asegúrate de permitir explícitamente el tráfico entrante en las IP de la tabla y en el puerto utilizado para consultar tu clúster de Redshift (por defecto es 5439). Debes permitir explícitamente la conectividad TCP de Redshift en este puerto incluso si las reglas de entrada están configuradas para "permitir todo".
- El punto de conexión del clúster de Redshift debe ser de acceso público para que Braze se conecte a tu clúster.
     - Si no quieres que tu clúster de Redshift sea accesible públicamente, puedes configurar una VPC y una instancia EC2 para que utilicen un túnel SSH para acceder a los datos de Redshift. Consulta esta [publicación del Centro de conocimientos de AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine) para obtener más información.
 
Permite el acceso desde las siguientes IP correspondientes a la región de tu dashboard de Braze.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Paso 1.1: Preparar la tabla 

Si lo deseas, puedes crear un nuevo proyecto o conjunto de datos que contenga la tabla de origen.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o más tablas para utilizar en tu integración CDI con los siguientes campos:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Puedes nombrar el proyecto, el conjunto de datos y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora a la que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificador de usuario** - Tu tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, el correo electrónico se utilizará como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
- `PAYLOAD` - Se trata de una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.

{% alert important %}
**Partición de BigQuery**

CDI admite particiones para BigQuery. Si realizas la partición mediante una función de `UPDATED_AT` (por ejemplo, con una granularidad diaria, semanal o por hora, dependiendo del tamaño del conjunto de datos), BigQuery puede recortar los datos que necesita analizar. Esto mejora el rendimiento y la eficiencia en tablas muy grandes.

No particiones por ningún otro campo. Prueba diferentes configuraciones para encontrar la mejor opción para tus datos específicos.

Todas las consultas CDI se filtran por `UPDATED_AT`, pero este comportamiento podría cambiar. Diseña el esquema de tu tabla de manera que las consultas _no_ requieran incluir esta cláusula.

Para obtener más información, consulta la [documentación sobre partición de BigQuery](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).
{% endalert %}

#### Paso 1.2: Crear una cuenta de servicio y conceder permisos 

Crea una cuenta de servicio en GCP para que Braze la utilice para conectarse y leer datos de tus tablas. La cuenta de servicio debe tener los siguientes permisos: 

- **BigQuery Connection User:** Permitirá a Braze realizar conexiones.
- **BigQuery User:** Proporcionará a Braze acceso para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- **BigQuery Data Viewer:** Proporcionará a Braze acceso para ver los conjuntos de datos y su contenido.
- **BigQuery Job User:** Proporcionará a Braze acceso para ejecutar trabajos.

Tras crear la cuenta de servicio y conceder los permisos, genera una clave JSON. Para más información sobre cómo hacerlo, consulta [Crear y eliminar claves de cuentas de servicio](https://cloud.google.com/iam/docs/keys-create-delete). La cargarás en el dashboard de Braze más adelante. 

#### Paso 1.3: Permitir el acceso a las IP de Braze    

Si tienes políticas de red en vigor, debes dar acceso de red a Braze a tu instancia de BigQuery. Permite el acceso desde las siguientes IP correspondientes a la región de tu dashboard de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Paso 1.1: Preparar la tabla 

Opcionalmente, configura un nuevo catálogo o esquema para contener tu tabla de origen.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o más tablas para utilizar en tu integración CDI con los siguientes campos:


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| STRING, STRUCT o MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

Puedes nombrar el esquema y la tabla como desees, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora a la que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificador de usuario** - Tu tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario. 
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, el correo electrónico se utilizará como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
- `PAYLOAD` - Se trata de una cadena o estructura de los campos que deseas sincronizar con el usuario en Braze.

#### Paso 1.2: Crear un token de acceso  

Para que Braze acceda a Databricks, es necesario crear un token de acceso personal.

1. En tu espacio de trabajo de Databricks, selecciona tu nombre de usuario de Databricks en la barra superior y, a continuación, selecciona **User Settings** en el desplegable.
2. En la pestaña Access tokens, selecciona **Generate new token**.
3. Introduce un comentario que te ayude a identificar este token, como "Braze CDI", y cambia la vida útil del token a sin vida útil dejando la casilla Lifetime (days) vacía (en blanco).
4. Selecciona **Generate**.
5. Copia el token mostrado y selecciona **Done**.

Guarda el token en un lugar seguro hasta que necesites introducirlo en el dashboard de Braze durante el paso de creación de credenciales.

#### Paso 1.3: Permitir el acceso a las IP de Braze    

Si tienes políticas de red en vigor, debes dar acceso de red a Braze a tu instancia de Databricks. Permite el acceso desde las siguientes IP correspondientes a la región de tu dashboard de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Paso 1.1: Configurar el principal de servicio y conceder acceso
Braze se conectará a tu almacén de Fabric utilizando un principal de servicio con autenticación Entra ID. Crearás un nuevo principal de servicio para que lo utilice Braze y concederás acceso a los recursos de Fabric según sea necesario. Braze necesitará los siguientes datos para conectarse:    

* Tenant ID (también llamado directorio) de tu cuenta de Azure 
* Principal ID (también llamado ID de aplicación) del principal de servicio 
* Secreto de cliente para que Braze se autentique

1. En el portal de Azure, ve al centro de administración de Microsoft Entra y, a continuación, a App Registrations. 
2. Selecciona **+ New registration** en **Identity** > **Applications** > **App registrations**.
3. Introduce un nombre y, a continuación, selecciona `Accounts in this organizational directory only` como tipo de cuenta admitido. A continuación, selecciona **Register**. 
4. Selecciona la aplicación (principal de servicio) que acabas de crear y, a continuación, ve a **Certificates & secrets** > **+ New client secret**.
5. Introduce una descripción para el secreto y establece un periodo de caducidad para el secreto. Después, selecciona **Add**. 
6. Toma nota del secreto de cliente creado para utilizarlo en la configuración de Braze. 

{% alert note %}
Azure no permite la caducidad ilimitada de los secretos de principal de servicio. Recuerda actualizar las credenciales antes de que caduquen para mantener el flujo de datos hacia Braze.
{% endalert %}

#### Paso 1.2: Conceder acceso a los recursos de Fabric 
Proporcionarás acceso para que Braze se conecte a tu instancia de Fabric. En tu portal de administración de Fabric, ve a **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.    

* En **Developer settings**, habilita **Service principals can use Fabric APIs** para que Braze pueda conectarse utilizando Microsoft Entra ID.
* En **OneLake settings**, habilita **Users can access data stored in OneLake with apps external to Fabric** para que el principal de servicio pueda acceder a los datos desde una aplicación externa.

#### Paso 1.3: Configurar un espacio de trabajo compartido y conceder acceso

Cualquier recurso de Fabric que quieras conectar a Braze debe colocarse en un espacio de trabajo compartido. Si solo has estado usando el espacio de trabajo predeterminado **My Workspace**, crea un nuevo espacio de trabajo compartido:

1. En el menú de navegación, selecciona **Workspaces** y luego selecciona **+ New workspace**.
2. Introduce un **Name** para el espacio de trabajo y selecciona **Apply**.

Una vez que tengas un espacio de trabajo compartido, concede acceso al principal de servicio:

1. Selecciona el espacio de trabajo y luego selecciona **Manage Access**.
2. Selecciona **+ Add people or groups**.
3. Busca y selecciona el nombre del principal de servicio que creaste en el paso 1.1. Si no aparece, confirma que has habilitado la configuración **Service principals can use Fabric APIs** en el paso 1.2.
4. En el desplegable de rol, selecciona **Contributor**.

El principal de servicio ahora puede acceder a los recursos del almacén de Fabric en este espacio de trabajo a través de sus puntos de conexión SQL, incluido el almacén que utilizarás para Braze.

#### Paso 1.4: Preparar la tabla
Braze admite tanto tablas como vistas en Fabric Warehouses. Si necesitas crear un nuevo almacén, créalo dentro del espacio de trabajo compartido del paso 1.3. Ve a **Create > Data Warehouse > Warehouse** en la consola de Fabric.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Puedes nombrar el almacén, el esquema y la tabla o vista como quieras, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora a la que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas donde `UPDATED_AT` es posterior al último valor sincronizado. Las filas en la marca de tiempo exacta del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.
- **Columnas de identificador de usuario** - Tu tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluyes tanto el correo electrónico como el teléfono, el correo electrónico se utilizará como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
- `PAYLOAD` - Se trata de una cadena JSON de los campos que deseas sincronizar con el usuario en Braze.


#### Paso 1.5: Obtener la cadena de conexión del almacén
Necesitarás el punto de conexión SQL de tu almacén para que Braze pueda conectarse. Para recuperarlo, ve al **espacio de trabajo** en Fabric, y en la lista de elementos, pasa el ratón por encima del nombre del almacén y selecciona **Copy SQL connection string**.

![La página "Fabric Console" en Microsoft Azure, donde los usuarios deben recuperar la cadena de conexión SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Paso 1.6: Permitir IP de Braze en el cortafuegos (opcional)

Dependiendo de la configuración de tu cuenta de Microsoft Fabric, puede que necesites permitir las siguientes direcciones IP en tu cortafuegos para permitir el tráfico desde Braze. Para más información sobre cómo habilitarlo, consulta la documentación correspondiente sobre el [acceso condicional de Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Paso 2: Crear una nueva integración en el dashboard de Braze

{% alert important %}
Los clientes que se incorporen en febrero de 2026 o después pueden tener acceso anticipado a la interfaz de CDI con fuentes y sincronizaciones separadas. En esta interfaz, crea una fuente antes de crear sincronizaciones para esa fuente. Varias sincronizaciones pueden usar la misma fuente.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

En el dashboard de Braze, ve a **Data Settings** > **Cloud Data Ingestion**, selecciona **Create New Data Sync** y, a continuación, selecciona **Snowflake Import**.

#### Paso 2.1: Añadir información de conexión de Snowflake y tabla de origen

Introduce la información de tu almacén de datos de Snowflake y la tabla de origen, y pasa al siguiente paso.

{% alert note %}
En el campo **Snowflake Account Locator**, introduce tu [identificador de cuenta](https://docs.snowflake.com/en/user-guide/admin-account-identifier) de Snowflake, que suele seguir un formato como `xy12345.us-east-1.aws`. No es lo mismo que el nombre de una base de datos o el nombre de un almacén.
{% endalert %}

#### Paso 2.2: Configurar los detalles de sincronización

A continuación, elige un nombre para la sincronización e introduce los correos electrónicos de contacto. Utilizaremos esta información de contacto para notificarte cualquier error de integración, como la eliminación inesperada del acceso a la tabla.

Los correos electrónicos de contacto solo recibirán notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No recibirán problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Solo para sincronización de catálogos) No hay espacio en el nivel de catálogo

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en tu dashboard de Braze para programar la sincronización periódica. Los tipos de datos admitidos son Atributos personalizados, Eventos personalizados y Eventos de compra, y el tipo de datos de una sincronización no se puede cambiar después de la creación. 

#### Añadir una clave pública al usuario de Braze

En este punto, debes volver a Snowflake para completar la configuración. Añade la clave pública que aparece en el dashboard al usuario que creaste para que Braze se conecte a Snowflake.

Para más información sobre cómo hacerlo, consulta la [documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si deseas rotar las claves en cualquier momento, podemos generar un nuevo par de claves y proporcionarte la nueva clave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

En el dashboard de Braze, ve a **Data Settings** > **Cloud Data Ingestion**, selecciona **Create New Data Sync** y, a continuación, selecciona **Amazon Redshift Import**.

#### Paso 2.1: Añadir información de conexión de Redshift y tabla de origen

Introduce la información de tu almacén de datos de Redshift y la tabla de origen. Si utilizas un túnel de red privada, activa el control deslizante e introduce la información del túnel. A continuación, pasa al siguiente paso. 

{% alert note %}
En el dashboard de Braze, el campo **Database name** solo acepta letras (A–Z, a–z), números (0–9) y guiones bajos (_), aunque Amazon Redshift admite caracteres adicionales en los identificadores de bases de datos.
{% endalert %}

#### Paso 2.2: Configurar los detalles de sincronización

A continuación, elige un nombre para la sincronización e introduce los correos electrónicos de contacto. Utilizaremos esta información de contacto para notificarte cualquier error de integración, como la eliminación inesperada del acceso a la tabla.

Los correos electrónicos de contacto solo recibirán notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No recibirán problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Solo para sincronización de catálogos) No hay espacio en el nivel de catálogo

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en tu dashboard de Braze para programar la sincronización periódica. Los tipos de datos admitidos son Atributos personalizados, Eventos personalizados y Eventos de compra, y el tipo de datos de una sincronización no se puede cambiar después de la creación. 
{% endtab %}
{% tab BigQuery %}

En el dashboard de Braze, ve a **Data Settings** > **Cloud Data Ingestion**, selecciona **Create New Data Sync** y, a continuación, selecciona **Google BigQuery Import**.

#### Paso 2.1: Añadir información de conexión de BigQuery y tabla de origen

Carga la clave JSON y proporciona un nombre para la cuenta de servicio; a continuación, introduce los detalles de tu tabla de origen.

#### Paso 2.2: Configurar los detalles de sincronización

A continuación, elige un nombre para la sincronización e introduce los correos electrónicos de contacto. Utilizaremos esta información de contacto para notificarte cualquier error de integración, como la eliminación inesperada del acceso a la tabla.

Los correos electrónicos de contacto solo recibirán notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No recibirán problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Solo para sincronización de catálogos) No hay espacio en el nivel de catálogo

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en tu dashboard de Braze para programar la sincronización periódica. Los tipos de datos admitidos son Atributos personalizados, Eventos personalizados, Eventos de compra y eliminaciones de usuarios. El tipo de datos de una sincronización no puede modificarse después de su creación. 

{% endtab %}
{% tab Databricks %}

En el dashboard de Braze, ve a **Data Settings** > **Cloud Data Ingestion**, selecciona **Create New Data Sync** y, a continuación, selecciona **Databricks Import**.

#### Paso 2.1: Añadir información de conexión de Databricks y tabla de origen

Introduce la información de tu almacén de datos de Databricks y la tabla de origen, y pasa al siguiente paso.

#### Paso 2.2: Configurar los detalles de sincronización

A continuación, elige un nombre para la sincronización e introduce los correos electrónicos de contacto. Utilizaremos esta información de contacto para notificarte cualquier error de integración, como la eliminación inesperada del acceso a la tabla.

Los correos electrónicos de contacto solo recibirán notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No recibirán problemas a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Solo para sincronización de catálogos) No hay espacio en el nivel de catálogo

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en tu dashboard de Braze para programar la sincronización periódica. Los tipos de datos admitidos son atributos personalizados, eventos personalizados, eventos de compra y eliminaciones de usuarios. El tipo de datos de una sincronización no puede modificarse después de su creación. 

{% endtab %}
{% tab Microsoft Fabric %}

#### Paso 2.1: Configurar una sincronización de ingesta de datos en la nube

Crearás una nueva sincronización de datos para Microsoft Fabric. En el dashboard de Braze, ve a **Data Settings** > **Cloud Data Ingestion**, selecciona **Create New Data Sync** y, a continuación, selecciona **Microsoft Fabric Import**.

#### Paso 2.2: Añadir información de conexión de Microsoft Fabric y tabla de origen

Introduce la información de las credenciales de tu almacén de Microsoft Fabric y la tabla de origen, y pasa al siguiente paso.

- Credentials Name es una etiqueta para estas credenciales en Braze; puedes establecer un valor descriptivo aquí
- Consulta los pasos de la sección 1 para obtener información detallada sobre cómo recuperar el Tenant ID, el Principal ID, el secreto de cliente y la cadena de conexión

#### Paso 2.3: Configurar los detalles de sincronización

A continuación, configura los siguientes detalles para tu sincronización: 

- Nombre de la sincronización 
- Tipo de datos - Los tipos de datos admitidos son atributos personalizados, eventos personalizados, eventos de compra, catálogos y eliminaciones de usuarios. El tipo de datos de una sincronización no puede modificarse después de su creación. 
- Frecuencia de sincronización - La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en tu dashboard de Braze para programar la sincronización periódica. 
  - Las sincronizaciones no periódicas se pueden desencadenar manualmente o a través de la [API]({{site.baseurl}}/api/endpoints/cdi) 

#### Paso 2.4: Configurar las preferencias de notificación

A continuación, introduce los correos electrónicos de contacto. Utilizaremos esta información de contacto para notificarte cualquier error de integración, como la eliminación inesperada del acceso a la tabla, o alertarte cuando determinadas filas no se actualicen.

Por defecto, los correos electrónicos de contacto solo recibirán notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden incluir lo siguiente:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Solo para sincronización de catálogos) No hay espacio en el nivel de catálogo

También puedes configurar alertas para problemas a nivel de fila, o elegir recibir una alerta cada vez que una sincronización se ejecute correctamente. 

{% endtab %}

{% endtabs %}

### Paso 3: Probar conexión

{% tabs %}
{% tab Snowflake %}

Vuelve al dashboard de Braze y selecciona **Test connection**. Si tiene éxito, verás una vista previa de los datos. Si por alguna razón no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Vuelve al dashboard de Braze y selecciona **Test connection**. Si tiene éxito, verás una vista previa de los datos. Si por alguna razón no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.
{% endsubtab %}

{% subtab Private Network %}
Vuelve al dashboard de Braze y selecciona **Test connection**. Si tiene éxito, verás una vista previa de los datos. Si por alguna razón no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

Una vez introducidos todos los detalles de configuración de la sincronización, selecciona **Test connection**. Si tiene éxito, verás una vista previa de los datos. Si por alguna razón no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

{% endtab %}

{% tab Databricks %}

Una vez introducidos todos los detalles de configuración de la sincronización, selecciona **Test connection**. Si tiene éxito, verás una vista previa de los datos. Si por alguna razón no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

{% endtab %}
{% tab Microsoft Fabric %}

Una vez introducidos todos los detalles de configuración de la sincronización, selecciona **Test connection**. Si tiene éxito, verás una vista previa de los datos. Si por alguna razón no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

{% endtab %}
{% endtabs %}

{% alert note %}
Debes probar con éxito una integración antes de que pueda pasar del estado Borrador al Activo. Si necesitas salir de la página de creación, tu integración se guardará y podrás volver a visitar la página de detalles para realizar cambios y pruebas.  
{% endalert %}

## Configurar integraciones o usuarios adicionales (opcional)

{% tabs %}
{% tab Snowflake %}
Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Snowflake.

Si reutilizas el mismo usuario y rol en todas las integraciones, **no** tendrás que volver a añadir la clave pública.
{% endtab %}
{% tab Redshift %}
Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Snowflake o Redshift.

Si reutilizas el mismo usuario en varias integraciones, no podrás eliminar el usuario en el dashboard de Braze hasta que se elimine de todas las sincronizaciones activas.
{% endtab %}
{% tab BigQuery %}

Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de BigQuery.

Si reutilizas el mismo usuario en varias integraciones, no podrás eliminar el usuario en el dashboard de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% tab Databricks %}

Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Databricks.

Si reutilizas el mismo usuario en varias integraciones, no podrás eliminar el usuario en el dashboard de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% tab Microsoft Fabric %}

Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Fabric.

Si reutilizas el mismo usuario en varias integraciones, no podrás eliminar el usuario en el dashboard de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% endtabs %}

## Ejecución de la sincronización

{% tabs %}
{% tab Snowflake %}
Una vez activada, la sincronización se ejecutará según la planificación configurada durante la instalación. Si deseas ejecutar la sincronización fuera de la planificación normal de pruebas o recuperar los datos más recientes, selecciona **Sync Now**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

{% endtab %}
{% tab Redshift %}
Una vez activada, la sincronización se ejecutará según la planificación configurada durante la instalación. Si deseas ejecutar la sincronización fuera de la planificación normal de pruebas o recuperar los datos más recientes, selecciona **Sync Now**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

{% endtab %}
{% tab BigQuery %}

Una vez activada, la sincronización se ejecutará según la planificación configurada durante la instalación. Si deseas ejecutar la sincronización fuera de la planificación normal de pruebas o recuperar los datos más recientes, selecciona **Sync Now**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

{% endtab %}
{% tab Databricks %}

Una vez activada, la sincronización se ejecutará según la planificación configurada durante la instalación. Si deseas ejecutar la sincronización fuera de la planificación normal de pruebas o recuperar los datos más recientes, selecciona **Sync Now**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

{% endtab %}
{% tab Microsoft Fabric %}

Una vez activada, la sincronización se ejecutará según la planificación configurada durante la instalación. Si deseas ejecutar la sincronización fuera de la planificación normal de pruebas o recuperar los datos más recientes, selecciona **Sync Now**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

{% endtab %}

{% endtabs %}

{% enddetails %}