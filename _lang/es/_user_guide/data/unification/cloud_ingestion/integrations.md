---
nav_title: Integraciones de almacenes de datos
article_title: Integraciones de almacenes de datos
description: "Esta página explica cómo utilizar Braze Cloud Data Ingestion para sincronizar datos relevantes con tu integración de Snowflake, Redshift, BigQuery y Databricks."
page_order: 2
page_type: reference

---

# Integraciones de almacenamiento de almacén de datos

> Esta página explica cómo utilizar Braze Cloud Data Ingestion (CDI) para sincronizar datos relevantes con tu integración de Snowflake, Redshift, BigQuery y Databricks.

## Configuración de integraciones de almacenes de datos

Las integraciones de la ingesta de datos en la nube requieren cierta configuración en Braze y en tu instancia de almacén de datos. Sigue estos pasos para configurar la integración:

{% tabs %}
{% tab Snowflake %}
1. En tu instancia de Snowflake, configura las tablas o vistas que quieras sincronizar con Braze.
2. Crea una nueva integración en el panel de Braze.
3. Recupera la clave pública proporcionada en el panel de Braze y [añádela al usuario Snowflake para la autenticación](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Prueba la integración e inicia la sincronización.

{% alert tip %}
La [guía de inicio rápido de Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) proporciona un código de ejemplo y recorre los pasos necesarios para crear una canalización automatizada utilizando Snowflake Streams y CDI para sincronizar datos con Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Asegúrate de que se permite el acceso de Braze a las tablas de Redshift que quieres sincronizar. Braze se conectará a Redshift a través de Internet.
2. En tu instancia de Redshift, configura las tablas o vistas que quieras sincronizar con Braze.
3. Crea una nueva integración en el panel de Braze.
4. Prueba la integración e inicia la sincronización.
{% endtab %}
{% tab BigQuery %}
1. Crea una cuenta de servicio y permite el acceso al proyecto o proyectos BigQuery y al conjunto o conjuntos de datos que contienen los datos que quieres sincronizar.  
2. En tu cuenta de BigQuery, configura las tablas o vistas que quieras sincronizar con Braze.   
3. Crea una nueva integración en el panel de Braze.  
4. Prueba la integración e inicia la sincronización.  
{% endtab %}
{% tab Databricks %}
1. Crea una cuenta de servicio y permite el acceso a los proyectos y conjuntos de datos de Databricks que contengan los datos que deseas sincronizar.  
2. En tu cuenta de Databricks, configura las tablas o vistas que quieras sincronizar con Braze.   
3. Crea una nueva integración en el panel de Braze.  
4. Prueba la integración e inicia la sincronización.

{% alert important %}
Puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecte a las instancias SQL Clásica y Pro, lo que provocará retrasos durante la configuración y prueba de la conexión, así como al inicio de las sincronizaciones programadas. Utilizar una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede suponer unos costes de integración ligeramente superiores.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Crea un principal de servicio y permite el acceso al espacio de trabajo de Fabric que se utilizará para tu integración.   
2. En tu espacio de trabajo de Fabric, configura las tablas o vistas que quieras sincronizar con Braze.   
3. Crea una nueva integración en el panel de Braze.  
4. Prueba la integración e inicia la sincronización.
{% endtab %}
{% endtabs %}

### Paso 1: Configurar tablas o vistas

{% tabs %}
{% tab Snowflake %}

#### Paso 1.1: Configura la mesa

```json
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
     --If you include both email and phone, we will use the email as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Puedes nombrar la base de datos, el esquema y la tabla como quieras, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora en que se actualizó o añadió esta fila a la tabla. Sólo sincronizaremos las filas que se hayan añadido o actualizado desde la última sincronización.
- **Columnas** de identificador de usuario - Tu tabla puede contener una o varias columnas de identificador de usuario. Cada fila sólo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Esto identifica al usuario que quieres actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero sólo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad para las actualizaciones al perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, utilizaremos el correo electrónico como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. 
- `PAYLOAD` - Se trata de una cadena JSON de los campos que quieres sincronizar con el usuario en Braze.

#### Paso 1.2: Configura el rol y los permisos de la base de datos

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Actualiza los nombres según sea necesario, pero los permisos deben coincidir con el ejemplo anterior.

#### Paso 1.3: Configurar el almacén y dar acceso al rol Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
El almacén debe tener activada la bandera de **reanudación automática**. Si no es así, tendrás que conceder a Braze privilegios adicionales de `OPERATE` en el almacén para que podamos activarlo cuando llegue el momento de ejecutar la consulta.
{% endalert %}

#### Paso 1.4: Configurar el usuario

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Tras este paso, compartirás la información de conexión con Braze y recibirás una clave pública para adjuntar al usuario.

{% alert note %}
Cuando conectes diferentes espacios de trabajo a la misma cuenta Snowflake, debes crear un usuario único para cada espacio de trabajo Braze en el que estés creando una integración. Dentro de un espacio de trabajo, puedes reutilizar el mismo usuario en todas las integraciones, pero la creación de la integración fallará si un usuario de la misma cuenta de Snowflake está duplicado en todos los espacios de trabajo.
{% endalert %}

#### Paso 1.5: Permitir IPs Braze en la política de red Snowflake (opcional)

Dependiendo de la configuración de tu cuenta Snowflake, puede que tengas que permitir las siguientes direcciones IP en tu política de red Snowflake. Para más información sobre cómo habilitarlo, consulta la documentación correspondiente de Snowflake sobre la [modificación de una política de red](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Paso 1.1: Configura la mesa 

Opcionalmente, configura una nueva Base de Datos y un nuevo Esquema para albergar tu tabla de origen
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Crea una tabla (o vista) para utilizarla en tu integración CDI
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, we will use the email as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Puedes nombrar la base de datos, el esquema y la tabla como quieras, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora en que se actualizó o añadió esta fila a la tabla. Sólo sincronizaremos las filas que se hayan añadido o actualizado desde la última sincronización.
- **Columnas** de identificador de usuario - Tu tabla puede contener una o varias columnas de identificador de usuario. Cada fila sólo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Esto identifica al usuario que quieres actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero sólo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad para las actualizaciones al perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, utilizaremos el correo electrónico como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. 
- `PAYLOAD` - Se trata de una cadena JSON de los campos que quieres sincronizar con el usuario en Braze.
 
#### Paso 1.2: Crear usuario y conceder permisos 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Estos son los permisos mínimos requeridos para este usuario. Si creas varias integraciones CDI, tal vez quieras conceder permisos a un esquema o administrar los permisos mediante un grupo. 

#### Paso 1.3: Permitir el acceso a las IP Braze

Si tienes un cortafuegos u otras políticas de red, debes dar acceso de red a Braze a tu instancia de Redshift. Un ejemplo de punto final de URL de Redshift es "ejemplo-cluster.ap-noreste-2.redshift.amazonaws.com".

Algunas cosas importantes que debes saber:
- Es posible que también tengas que cambiar tus grupos de seguridad para permitir que Braze acceda a tus datos en Redshift.
- Asegúrate de permitir explícitamente el tráfico entrante en las IP de la tabla y en el puerto utilizado para consultar tu clúster Redshift (predeterminado es 5439). Debes permitir explícitamente la conectividad TCP de Redshift en este puerto, aunque las reglas de entrada estén configuradas como "permitir todo".
- El punto final del clúster Redshift debe ser de acceso público para que Braze se conecte a tu clúster.
     - Si no quieres que tu clúster de Redshift sea accesible públicamente, puedes configurar una VPC y una instancia EC2 para que utilicen un túnel SSH para acceder a los datos de Redshift. Consulta esta [publicación del Centro de conocimientos de AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine) para obtener más información.
 
Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Paso 1.1: Configura la mesa 

Opcionalmente, configura un nuevo proyecto o conjunto de datos para albergar tu tabla de origen.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o varias tablas para utilizarlas en tu integración CDI con los siguientes campos:

```json
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
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUERIDO |
| `PAYLOAD`| JSON | REQUERIDO |
| `EXTERNAL_ID`| CADENA | NULABLE |
| `ALIAS_NAME`| CADENA | NULABLE |
| `ALIAS_LABEL`| CADENA | NULABLE |
| `BRAZE_ID`| CADENA | NULABLE |
| `EMAIL`| CADENA | NULABLE |
| `PHONE`| CADENA | NULABLE |

Puedes nombrar el proyecto, el conjunto de datos y la tabla como quieras, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora en que se actualizó o añadió esta fila a la tabla. Sólo sincronizaremos las filas que se hayan añadido o actualizado desde la última sincronización.
- **Columnas** de identificador de usuario - Tu tabla puede contener una o varias columnas de identificador de usuario. Cada fila sólo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Esto identifica al usuario que quieres actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero sólo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad para las actualizaciones al perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, utilizaremos el correo electrónico como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
   correo electrónico varchar,
   phone_number varchar,
- `PAYLOAD` - Se trata de una cadena JSON de los campos que quieres sincronizar con el usuario en Braze.

#### Paso 1.2: Crear una cuenta de servicio y conceder permisos 

Crea una cuenta de servicio en GCP para que Braze la utilice para conectarse y leer datos de tu(s) tabla(s). La cuenta de servicio debe tener los siguientes permisos: 

- **Usuario de conexión a BigQuery:** Esto permitirá a Braze establecer conexiones
- **Usuario de BigQuery:** Esto proporcionará acceso a Braze para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- **Visor de datos BigQuery:** Esto proporcionará acceso a Braze para ver los conjuntos de datos y su contenido.
- **Usuario de BigQuery Job:** Esto proporcionará acceso a Braze para ejecutar trabajos

Tras crear la cuenta de servicio y conceder los permisos, genera una clave JSON. Consulta más información sobre cómo hacerlo [aquí](https://cloud.google.com/iam/docs/keys-create-delete). Más tarde lo actualizarás en el panel de Braze. 

#### Paso 1.3: Permitir el acceso a las IP Braze    

Si tienes políticas de red en vigor, debes dar acceso de red Braze a tu instancia de Big Query. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Paso 1.1: Configura la mesa 

Opcionalmente, configura un nuevo Catálogo o Esquema para albergar tu tabla de origen.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o varias tablas para utilizarlas en tu integración CDI con los siguientes campos:


```json
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
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUERIDO |
| `PAYLOAD`| CADENA, ESTRUCTURA o MAPA | REQUERIDO |
| `EXTERNAL_ID`| CADENA | NULABLE |
| `ALIAS_NAME`| CADENA | NULABLE |
| `ALIAS_LABEL`| CADENA | NULABLE |
| `BRAZE_ID`| CADENA | NULABLE |
| `EMAIL`| CADENA | NULABLE |
| `PHONE`| CADENA | NULABLE |

Puedes nombrar el esquema y la tabla como quieras, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora en que se actualizó o añadió esta fila a la tabla. Sólo sincronizaremos las filas que se hayan añadido o actualizado desde la última sincronización.
- **Columnas** de identificador de usuario - Tu tabla puede contener una o varias columnas de identificador de usuario. Cada fila sólo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Esto identifica al usuario que quieres actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero sólo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID externo o un alias de usuario. 
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad para las actualizaciones al perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, utilizaremos el correo electrónico como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. 
- `PAYLOAD` - Se trata de una cadena o estructura de los campos que quieres sincronizar con el usuario en Braze.

#### Paso 1.2: Crear un token de acceso  

Para que Braze acceda a Databricks, es necesario crear un token de acceso personal.

1. En tu espacio de trabajo de Databricks, selecciona tu nombre de usuario de Databricks en la barra superior y, a continuación, selecciona **Configuración de usuario** en el desplegable.
2. En la pestaña Tokens de acceso, selecciona **Generar nuevo token**.
3. Introduce un comentario que te ayude a identificar este token, como "Braze CDI", y cambia la duración del token a sin duración dejando la casilla Duración (días) vacía (en blanco).
4. Selecciona **Generar**.
5. Copia el token mostrado y selecciona **Hecho**.

Guarda el token en un lugar seguro hasta que necesites introducirlo en el panel de Braze durante el paso de creación de credenciales.

#### Paso 1.3: Permitir el acceso a las IP Braze    

Si tienes políticas de red en vigor, debes dar acceso de red Braze a tu instancia de Databricks. Permite el acceso desde las siguientes IP correspondientes a la región de tu panel de Braze.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Paso 1.1: Configurar el principal del servicio y conceder acceso
Braze se conectará a tu almacén Fabric utilizando un principal de servicio con autenticación Entra ID. Crearás un nuevo principal de servicio para que lo utilice Braze, y concederás acceso a los recursos de Fabric según sea necesario. Braze necesitará los siguientes datos para conectarse:    

* Tenant ID (también llamado directorio) de tu cuenta Azure 
* ID de la entidad de seguridad (también llamado ID de aplicación) para la entidad de seguridad del servicio 
* Secreto de cliente para que Braze se autentique

1. En el portal de Azure, ve al centro de administración de Microsoft Entra y, a continuación, a Registros de aplicaciones. 
2. Selecciona **\+ Nuevo registro** en **Identidad** > **Aplicaciones** > **Registros de aplicaciones**.
3. Introduce un nombre y, a continuación, selecciona `Accounts in this organizational directory only` como tipo de cuenta admitido. A continuación, selecciona **Registro**. 
4. Selecciona la aplicación (servicio principal) que acabas de crear y, a continuación, ve a **Certificados & secretos** > **\+ Nuevo secreto de cliente**.
5. Introduce una descripción para el secreto y establece un periodo de caducidad para el secreto. Después, selecciona **Añadir**. 
6. Toma nota del secreto de cliente creado para utilizarlo en la configuración de Braze. 

{% alert note %}
Azure no permite la caducidad ilimitada de los secretos de principal de servicio. Recuerda actualizar las credenciales antes de que caduquen para mantener el flujo de datos a Braze.
{% endalert %}

#### Paso 1.2: Conceder acceso a los recursos de Fabric 
Proporcionarás acceso para que Braze se conecte a tu instancia de Fabric. En tu portal de administración de Fabric, ve a **Configuración** > **Gobierno e información** > **Portal de administración** > **Configuración de inquilinos**.    

* En la **configuración del desarrollador** habilita "Los principales del servicio pueden utilizar APIs de Fabric" para que Braze pueda conectarse utilizando Microsoft Entra ID.
* En la **configuración de OneLake** habilita "Los usuarios pueden acceder a los datos almacenados en OneLake con aplicaciones externas a Fabric" para que el principal del servicio pueda acceder a los datos de una aplicación externa.


#### Paso 1.3: Configura la mesa
Braze admite tanto tablas como vistas en Fabric Warehouses. Si necesitas crear un nuevo almacén, ve a **Crear > Almacén de datos > Almacén** en la consola Fabric. 

```json
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
  --If you include both email and phone, we will use the email as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Puedes nombrar el almacén, el esquema y la tabla o vista como quieras, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - La hora en que se actualizó o añadió esta fila a la tabla. Sólo sincronizaremos las filas que se hayan añadido o actualizado desde la última sincronización.
- **Columnas** de identificador de usuario - Tu tabla puede contener una o varias columnas de identificador de usuario. Cada fila sólo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, `braze_id`, `email` o `phone`). Una tabla de origen puede tener columnas para uno, dos, tres, cuatro o los cinco tipos de identificadores.
    - `EXTERNAL_ID` - Esto identifica al usuario que quieres actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero sólo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario Braze. Lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad para las actualizaciones al perfil actualizado más recientemente. Si incluyes tanto correo electrónico como teléfono, utilizaremos el correo electrónico como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. 
- `PAYLOAD` - Se trata de una cadena JSON de los campos que quieres sincronizar con el usuario en Braze.


#### Paso 1.4: Obtener cadena de conexión al almacén 
Necesitarás el punto final SQL de tu almacén para que Braze pueda conectarse. Para recuperarla, ve al **espacio de trabajo** en Fabric, y en la lista de elementos, pasa el ratón por encima del nombre del almacén y selecciona **Copiar cadena de conexión SQL**.

\![La página "Fabric Console" de Microsoft Azure, donde los usuarios deben recuperar la cadena de conexión SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Paso 1.5: Permitir IPs de Braze en el Cortafuegos (Opcional)

Dependiendo de la configuración de tu cuenta Microsoft Fabric, puede que tengas que permitir las siguientes direcciones IP en tu cortafuegos para permitir el tráfico desde Braze. Para más información sobre cómo habilitarlo, consulta la documentación correspondiente sobre el [Acceso Condicional Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Paso 2: Crea una nueva integración en el panel de Braze

{% tabs %}
{% tab Snowflake %}

En el Dashbord Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube**, selecciona **Crear nueva sincronización de datos** y, a continuación, **Snowflake Importar**.

#### Paso 2.1: Añadir información de conexión Snowflake y tabla de origen

Introduce la información de tu almacén de datos Snowflake y la tabla de origen, y pasa al siguiente paso.

\![La página "Crear nueva sincronización de importación" para Snowflake en el panel de Braze con datos de ejemplo introducidos en el Paso 1: "Configurar la conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### Paso 2.2: Configurar los detalles de la sincronización

A continuación, elige un nombre para tu sincronización e introduce los correos electrónicos de contacto. Utilizaremos esta información de contacto para notificarte cualquier error de integración, como la eliminación inesperada del acceso a la tabla.

Los correos electrónicos de contacto sólo recibirán notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No recibirán ediciones a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden ser los siguientes

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Sólo para sincronización de catálogos) El nivel de catálogo no tiene espacio

\![La página "Crear nueva sincronización de importación" para Snowflake en el panel de Braze con datos de ejemplo añadidos en el Paso 2: "Configurar detalles de sincronización".]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en tu panel de Braze para programar la sincronización recurrente. Los tipos de datos admitidos son Atributos personalizados, Eventos personalizados y Eventos de compra, y el tipo de datos de una sincronización no puede cambiarse después de la creación. 

#### Añadir una clave pública al usuario Braze

En este punto, debes volver a Snowflake para completar la configuración. Añade la clave pública que aparece en el panel al usuario que creaste para que Braze se conecte a Snowflake.

Para más información sobre cómo hacerlo, consulta la [documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si quieres rotar las claves en cualquier momento, podemos generar un nuevo par de claves y proporcionarte la nueva clave pública.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

En el Dashbord de Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube**, selecciona **Crear nueva sincronización de datos** y, a continuación, selecciona **Importación de Amazon Redshift**.

#### Paso 2.1: Añade la información de conexión a Redshift y la tabla de origen

Introduce la información de tu almacén de datos Redshift y la tabla de origen. Si utilizas un túnel de red privada, alterna el control deslizante e introduce la información del túnel. Luego pasa al siguiente paso.

\![La página "Crear nueva sincronización de importación" para Redshift en el panel de Braze, configurada en el paso 1: "Configurar la conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### Paso 2.2: Configurar los detalles de la sincronización

A continuación, elige un nombre para tu sincronización e introduce los correos electrónicos de contacto. Utilizaremos esta información de contacto para notificarte cualquier error de integración, como la eliminación inesperada del acceso a la tabla.

Los correos electrónicos de contacto sólo recibirán notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No recibirán ediciones a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden ser los siguientes

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Sólo para sincronización de catálogos) El nivel de catálogo no tiene espacio

\![La página "Crear nueva sincronización de importación" para Redshift en el panel de Braze con algunos datos de ejemplo añadidos en el paso 2: "Configurar detalles de sincronización".]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en tu panel de Braze para programar la sincronización recurrente. Los tipos de datos admitidos son Atributos personalizados, Eventos personalizados y Eventos de compra, y el tipo de datos de una sincronización no puede cambiarse después de la creación.
{% endtab %}
{% tab BigQuery %}

En el Dashbord de Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube**, selecciona **Crear nueva sincronización de datos** y, a continuación, selecciona **Importación de Google BigQuery**.

#### Paso 2.1: Añade la información de conexión de BigQuery y la tabla de origen

Sube la clave JSON y proporciona un nombre para la cuenta de servicio, después introduce los detalles de tu tabla de origen.

\![La página "Crear nueva sincronización de importación" para BigQuery en el panel de Braze, configurada en el Paso 1: "Configurar la conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### Paso 2.2: Configurar los detalles de la sincronización

A continuación, elige un nombre para tu sincronización e introduce los correos electrónicos de contacto. Utilizaremos esta información de contacto para notificarte cualquier error de integración, como la eliminación inesperada del acceso a la tabla.

Los correos electrónicos de contacto sólo recibirán notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No recibirán ediciones a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden ser los siguientes

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Sólo para sincronización de catálogos) El nivel de catálogo no tiene espacio

\![La página "Crear nueva sincronización de importación" para BigQuery en el panel de Braze, configurada en el paso 2: "Configurar detalles de sincronización".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en tu panel de Braze para programar la sincronización recurrente. Los tipos de datos admitidos son Atributos personalizados, Eventos personalizados, Eventos de compra y Borrados de usuario. El tipo de datos de una sincronización no puede cambiarse después de su creación. 

{% endtab %}
{% tab Databricks %}

En el Dashbord de Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube**, selecciona **Crear nueva sincronización de datos** y, a continuación, selecciona **Importación de Databricks**.

#### Paso 2.1: Añadir información de conexión Databricks y tabla de origen

Introduce la información de tu almacén de datos Databricks y la tabla de origen, y pasa al siguiente paso.

\![La página "Crear nueva sincronización de importación" para Databricks en el panel de Braze, configurada en el Paso 1: "Configurar la conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### Paso 2.2: Configurar los detalles de la sincronización

A continuación, elige un nombre para tu sincronización e introduce los correos electrónicos de contacto. Utilizaremos esta información de contacto para notificarte cualquier error de integración, como la eliminación inesperada del acceso a la tabla.

Los correos electrónicos de contacto sólo recibirán notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. No recibirán ediciones a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden ser los siguientes

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Sólo para sincronización de catálogos) El nivel de catálogo no tiene espacio

\![La página "Crear nueva sincronización de importación" para Databricks en el panel de Braze, configurada en el paso 2: "Configurar detalles de sincronización".]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en tu panel de Braze para programar la sincronización recurrente. Los tipos de datos admitidos son atributos personalizados, eventos personalizados, eventos de compra y eliminaciones de usuarios. El tipo de datos de una sincronización no puede cambiarse después de su creación. 

{% endtab %}
{% tab Microsoft Fabric %}

#### Paso 2.1: Configurar una sincronización de la ingesta de datos en la nube

Crearás una nueva sincronización de datos para Microsoft Fabric. En el panel de control de Braze, ve a **Configuración de datos** > **Ingesta de datos en la nube**, selecciona **Crear nueva sincronización de datos** y, a continuación, selecciona **Importar Microsoft Fabric**.

#### Paso 2.2: Añadir información de conexión Microsoft Fabric y tabla de origen

Introduce la información de tus credenciales del almacén Microsoft Fabric y la tabla de origen, y pasa al siguiente paso.

- Nombre de credenciales es una etiqueta para estas credenciales en Braze, puedes establecer un valor útil aquí
- Consulta los pasos de la sección 1 para saber cómo recuperar el ID de arrendatario, el ID de principal, el secreto de cliente y la cadena de conexión.

\![La página "Crear nueva sincronización de importación" para Microsoft en el panel de Braze, configurada en el Paso 1: "Configurar la conexión".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_1.png %})

#### Paso 2.3: Configurar los detalles de la sincronización

A continuación, configura los siguientes detalles para tu sincronización: 

- Nombre de sincronización 
- Tipo de datos - Los tipos de datos admitidos son atributos personalizados, eventos personalizados, eventos de compra, catálogos y eliminaciones de usuarios. El tipo de datos de una sincronización no puede cambiarse después de su creación. 
- Frecuencia de sincronización - La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en tu panel de Braze para programar la sincronización recurrente. 
  - Las sincronizaciones no periódicas pueden desencadenarse manualmente o a través de la [API]({{site.baseurl}}/api/endpoints/cdi) 

\![La página "Crear nueva sincronización de importación" para Microsoft Fabric en el panel de Braze, configurada en el paso 2: "Configurar detalles de sincronización".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_2.png %})


#### Paso 2.4: Configurar las preferencias de notificación

A continuación, introduce los correos electrónicos de contacto. Utilizaremos esta información de contacto para notificarte cualquier error de integración, como la eliminación inesperada del acceso a la tabla, o alertarte cuando determinadas filas no se actualicen .

Por predeterminado, los correos electrónicos de contacto sólo recibirán notificaciones de errores globales o a nivel de sincronización, como tablas que faltan, permisos y otros. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden ser los siguientes

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Sólo para sincronización de catálogos) El nivel de catálogo no tiene espacio

También puedes configurar alertas para problemas a nivel de fila, o elegir recibir una alerta cada vez que una sincronización se ejecute correctamente. 

\![La página "Crear nueva sincronización de importación" para Microsoft Fabric en el panel de Braze, configurada en el paso 3: "Configurar preferencias de notificación".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_3.png %})


{% endtab %}

{% endtabs %}

### Paso 3: Conexión de prueba

{% tabs %}
{% tab Snowflake %}

Vuelve al panel de Braze y selecciona **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

\![La página "Crear nueva sincronización de importación" para Snowflake en el panel de Braze con el Paso 3: "Conexión de prueba" que muestra una clave pública RSA.]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Vuelve al panel de Braze y selecciona **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

\![La página "Crear nueva sincronización de importación" para Redshift en el panel de Braze, configurada en el paso 3: "Prueba de conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endsubtab %}

{% subtab Private Network %}
Vuelve al panel de Braze y selecciona **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

\![La página "Crear nueva sincronización de importación" para Red Privada Redshift en el panel de Braze, con el Paso 4: "Conexión de prueba" que muestra una clave pública RSA.]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

Una vez introducidos todos los detalles de configuración de tu sincronización, selecciona **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

\![La página "Crear nueva sincronización de importación" para BigQuery en el panel de Braze, configurada en el paso 3: "Prueba de conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}

{% tab Databricks %}

Una vez introducidos todos los detalles de configuración de tu sincronización, selecciona **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

\![La página "Crear nueva sincronización de importación" para Databricks en el panel de Braze, configurada en el paso 3: "Prueba de conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Microsoft Fabric %}

Una vez introducidos todos los detalles de configuración de tu sincronización, selecciona **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

\![La página "Crear nueva sincronización de importación" para Microsoft Fabric en el panel de Braze, configurada en el paso 4: "Prueba de conexión".]({% image_buster /assets/img/cloud_ingestion/fabric_setup_4.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Debes probar con éxito una integración antes de que pueda pasar del estado Borrador al Activo. Si necesitas salir de la página de creación, tu integración se guardará y podrás volver a visitar la página de detalles para realizar cambios y pruebas.  
{% endalert %}

## Configura integraciones o usuarios adicionales (opcional)

{% tabs %}
{% tab Snowflake %}
Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la cuenta de Snowflake.

\![La página "Crear nueva sincronización de importación" para Snowflake en el panel de Braze, con el desplegable "Seleccionar credenciales" abierto en el paso 1: "Configurar la conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_4.png %})

Si reutilizas el mismo usuario y función en distintas integraciones, **no** tendrás que volver a añadir la clave pública.
{% endtab %}
{% tab Redshift %}
Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Snowflake o Redshift.

\![La página "Crear nueva sincronización de importación" para Redshift en el panel de Braze, con el desplegable "Seleccionar credenciales" abierto en el paso 1: "Configurar la conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_9.png %})

Si reutilizas el mismo usuario en distintas integraciones, no podrás eliminar el usuario en el panel de Braze hasta que se elimine de todas las sincronizaciones activas.
{% endtab %}
{% tab BigQuery %}

Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de BigQuery.

\![La página "Crear nueva sincronización de importación" para BigQuery en el panel de Braze, con el desplegable "Seleccionar credenciales" abierto en el paso 1: "Configurar la conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_14.png %})

Si reutilizas el mismo usuario en distintas integraciones, no podrás eliminar el usuario en el panel de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% tab Databricks %}

Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Databricks.

\![La página "Crear nueva sincronización de importación" para Databricks en el panel de Braze, con el desplegable "Seleccionar credenciales" abierto en el paso 1: "Configurar la conexión".]({% image_buster /assets/img/cloud_ingestion/ingestion_17.png %})

Si reutilizas el mismo usuario en distintas integraciones, no podrás eliminar el usuario en el panel de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% tab Microsoft Fabric %}

Puedes configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Fabric.

Si reutilizas el mismo usuario en distintas integraciones, no podrás eliminar el usuario en el panel de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% endtabs %}

## Ejecutar la sincronización

{% tabs %}
{% tab Snowflake %}
Cuando esté activada, tu sincronización se ejecutará según el horario configurado durante la configuración. Si quieres ejecutar la sincronización fuera del programa normal de pruebas o para obtener los datos más recientes, selecciona **Sincronizar ahora**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

La página "Importar datos" de Snowflake en el panel de Braze muestra la opción "Sincronizar ahora" en el menú de elipses verticales.]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
Cuando esté activada, tu sincronización se ejecutará según el horario configurado durante la configuración. Si quieres ejecutar la sincronización fuera del programa normal de pruebas o para obtener los datos más recientes, selecciona **Sincronizar ahora**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

La página "Importar datos" de Redshift en el panel de Braze muestra la opción "Sincronizar ahora" en el menú de elipses verticales.]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

Cuando esté activada, tu sincronización se ejecutará según el horario configurado durante la configuración. Si quieres ejecutar la sincronización fuera del programa normal de pruebas o para obtener los datos más recientes, selecciona **Sincronizar ahora**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

La página "Importar datos" de BigQuery en el panel de Braze muestra la opción "Sincronizar ahora" en el menú de elipses verticales.]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

Cuando esté activada, tu sincronización se ejecutará según el horario configurado durante la configuración. Si quieres ejecutar la sincronización fuera del programa normal de pruebas o para obtener los datos más recientes, selecciona **Sincronizar ahora**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

La página "Importar datos" de Databricks en el panel de Braze muestra la opción "Sincronizar ahora" en el menú de elipses verticales.]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% tab Microsoft Fabric %}

Cuando esté activada, tu sincronización se ejecutará según el horario configurado durante la configuración. Si quieres ejecutar la sincronización fuera del programa normal de pruebas o para obtener los datos más recientes, selecciona **Sincronizar ahora**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

{% endtab %}

{% endtabs %}

