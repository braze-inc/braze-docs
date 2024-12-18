---
nav_title: Integración de almacenes de datos
article_title: Integración de almacenes de datos
description: "Este artículo de referencia cubre cómo utilizar Braze Cloud Data Ingestion para sincronizar datos relevantes con su integración de Snowflake, Redshift, BigQuery y Databricks."
page_order: 2
page_type: reference

---

# Integraciones de almacenamiento de almacén de datos

> En este artículo se explica cómo utilizar Braze Cloud Data Ingestion (CDI) para sincronizar datos relevantes con su integración de Snowflake, Redshift, BigQuery y Databricks.

## Configuración del producto

Las integraciones de la ingesta de datos en la nube requieren cierta configuración en Braze y en tu instancia. Siga estos pasos para configurar la integración:

{% tabs %}
{% tab Snowflake %}
1. En su instancia de Snowflake, configure la(s) tabla(s) o vista(s) que desea sincronizar con Braze.
2. Cree una nueva integración en el salpicadero de Braze.
3. Recupera la clave pública proporcionada en panel de Braze y [añádela al usuario Snowflake para la autenticación](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Pruebe la integración e inicie la sincronización.
{% endtab %}
{% tab Redshift %}
1. Asegúrese de que se permite el acceso de Braze a las tablas de Redshift que desea sincronizar. Braze se conectará a Redshift a través de Internet.
2. En su instancia de Redshift, configure la(s) tabla(s) o vista(s) que desea sincronizar con Braze.
3. Cree una nueva integración en el salpicadero de Braze.
4. Pruebe la integración e inicie la sincronización.
{% endtab %}
{% tab BigQuery %}
1. Cree una cuenta de servicio y permita el acceso a los proyectos de BigQuery y a los conjuntos de datos que contienen los datos que desea sincronizar.  
2. En su cuenta de BigQuery, configure la(s) tabla(s) o vista(s) que desea sincronizar con Braze.   
3. Cree una nueva integración en el salpicadero de Braze.  
4. Pruebe la integración e inicie la sincronización.  
{% endtab %}
{% tab Databricks %}
1. Crea una cuenta de servicio y permite el acceso a los proyectos y conjuntos de datos de Databricks que contienen los datos que deseas sincronizar.  
2. En tu cuenta de Databricks, configura la(s) tabla(s) o vista(s) que deseas sincronizar con Braze.   
3. Cree una nueva integración en el salpicadero de Braze.  
4. Pruebe la integración e inicie la sincronización.

{% alert important %}
Puede haber de dos a cinco minutos de tiempo de calentamiento cuando Braze se conecte a las instancias Classic y Pro SQL, lo que provocará retrasos durante la configuración de la conexión y las pruebas, así como al inicio de las sincronizaciones programadas. El uso de una instancia SQL sin servidor minimizará el tiempo de calentamiento y mejorará el rendimiento de las consultas, pero puede dar lugar a costes de integración ligeramente superiores.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 1: Configurar tablas o vistas

{% tabs %}
{% tab Snowflake %}

#### Paso 1: Preparar la mesa

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

Puede nombrar la base de datos, el esquema y la tabla como desee, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - Hora a la que se actualizó o añadió esta fila a la tabla. Sólo se sincronizarán las filas que se hayan añadido o actualizado desde la última sincronización.
- **Columnas de identificador de usuario** \- Su tabla puede contener una o más columnas de identificador de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, o `braze_id`). Una tabla de origen puede tener columnas para uno, dos o los tres tipos de identificadores. 
    - `EXTERNAL_ID` - Identifica al usuario que desea actualizar. Esto debería coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario Braze. Esto lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de Cloud Data Ingestion. Para crear nuevos usuarios, especifique un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluye tanto el correo electrónico como el teléfono, utilizaremos el correo electrónico como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. 
- `PAYLOAD` - Se trata de una cadena JSON de los campos que desea sincronizar con el usuario en Braze.

#### Paso 2: Configurar el rol y los permisos de la base de datos

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Actualiza los nombres según sea necesario, pero los permisos deben coincidir con el ejemplo anterior.

#### Paso 3: Configura el almacén y da acceso al rol de Braze

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
El almacén deberá tener activado el indicador **de reanudación automática**. Si no es así, tendrá que conceder a Braze privilegios adicionales de `OPERATE` en el almacén para que podamos activarlo cuando llegue el momento de ejecutar la consulta.
{% endalert %}

#### Paso 4: Configura el usuario

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Después de este paso, compartirás la información de conexión con Braze y recibirás una clave pública para adjuntar al usuario.

{% alert note %}
Cuando conecte diferentes espacios de trabajo a la misma cuenta Snowflake, debe crear un usuario único para cada espacio de trabajo Braze en el que esté creando una integración. Dentro de un espacio de trabajo, puede reutilizar el mismo usuario en todas las integraciones, pero la creación de la integración fallará si un usuario de la misma cuenta Snowflake se duplica en todos los espacios de trabajo.
{% endalert %}

#### Paso 5: Permite las IP de Braze en la política de redes de Snowflake (opcional)

Dependiendo de la configuración de su cuenta Snowflake, puede que necesite permitir las siguientes direcciones IP en su política de red Snowflake. Para obtener más información sobre cómo activar esta opción, consulte la documentación pertinente de Snowflake sobre la [modificación de una política de red](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

| Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Para las instancias `EU-01` y `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`
{% endtab %}
{% tab Redshift %}

#### Paso 1: Preparar la mesa 

Opcionalmente, configura una nueva Base de datos y un nuevo Esquema para albergar tu tabla de origen
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Cree una tabla (o vista) para utilizarla en su integración CDI
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

Puede nombrar la base de datos, el esquema y la tabla como desee, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - Hora a la que se actualizó o añadió esta fila a la tabla. Sólo se sincronizarán las filas que se hayan añadido o actualizado desde la última sincronización.
- Columnas de identificación de usuarios. Su tabla puede contener una o más columnas de identificadores de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, o `braze_id`). Una tabla de origen puede tener columnas para uno, dos o los tres tipos de identificadores. 
    - `EXTERNAL_ID` - Identifica al usuario que desea actualizar. Esto debería coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario Braze. Esto lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de Cloud Data Ingestion. Para crear nuevos usuarios, especifique un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluye tanto el correo electrónico como el teléfono, utilizaremos el correo electrónico como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. 
- `PAYLOAD` - Se trata de una cadena JSON de los campos que desea sincronizar con el usuario en Braze.
 
#### Paso 2: Crear usuario y conceder permisos 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Estos son los permisos mínimos requeridos para este usuario. Si crea varias integraciones CDI, puede que desee conceder permisos a un esquema o gestionar los permisos mediante un grupo. 

#### Paso 3: Permitir el acceso a las IP Braze

Si tienes un cortafuegos u otras políticas de red, debes dar acceso de red a Braze a tu instancia de Redshift. Un ejemplo de punto final de URL de Redshift es "example-cluster.ap-northeast-2.redshift.amazonaws.com".

Algunas cosas importantes que hay que saber:
- Es posible que también tenga que cambiar sus grupos de seguridad para permitir que Braze acceda a sus datos en Redshift.
- Asegúrese de permitir explícitamente el tráfico entrante en las IP de la tabla y en el puerto utilizado para consultar su clúster Redshift (por defecto es 5439). Debe permitir explícitamente la conectividad TCP de Redshift en este puerto incluso si las reglas de entrada están configuradas para "permitir todo".
- El punto final del clúster Redshift debe ser de acceso público para que Braze se conecte a tu clúster.
     - Si no quieres que tu clúster de Redshift sea accesible públicamente, puedes configurar una VPC y una instancia EC2 para que utilicen un túnel SSH para acceder a los datos de Redshift. Consulte esta [publicación del Centro de conocimientos de AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine) para obtener más información.
 
Permita el acceso desde las siguientes IP correspondientes a la región de su cuadro de mandos Braze.

| Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Para las instancias `EU-01` y `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`
{% endtab %}
{% tab BigQuery %}

#### Paso 1: Preparar la mesa 

Si lo desea, puede crear un nuevo proyecto o conjunto de datos que contenga la tabla de origen.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Cree una o más tablas para utilizar en su integración CDI con los siguientes campos:

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
| `UPDATED_AT`| MARCA DE TIEMPO | REQUERIDO |
| `PAYLOAD`| JSON | REQUERIDO |
| `EXTERNAL_ID`| CADENA | NULABLE |
| `ALIAS_NAME`| CADENA | NULABLE |
| `ALIAS_LABEL`| CADENA | NULABLE |
| `BRAZE_ID`| CADENA | NULABLE |
| `EMAIL`| CADENA | NULABLE |
| `PHONE`| CADENA | NULABLE |

Puede nombrar el proyecto, el conjunto de datos y la tabla como desee, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - Hora a la que se actualizó o añadió esta fila a la tabla. Sólo se sincronizarán las filas que se hayan añadido o actualizado desde la última sincronización.
- Columnas de identificación de usuarios. Su tabla puede contener una o más columnas de identificadores de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, o `braze_id`). Una tabla de origen puede tener columnas para uno, dos o los tres tipos de identificadores. 
    - `EXTERNAL_ID` - Identifica al usuario que desea actualizar. Esto debería coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario Braze. Esto lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de Cloud Data Ingestion. Para crear nuevos usuarios, especifique un ID de usuario externo o un alias de usuario.
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluye tanto el correo electrónico como el teléfono, utilizaremos el correo electrónico como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente.
   email varchar,
   varchar phone_number,
- `PAYLOAD` - Se trata de una cadena JSON de los campos que desea sincronizar con el usuario en Braze.

#### Paso 2: Crear una cuenta de servicio y conceder permisos 

Cree una cuenta de servicio en GCP para que Braze la utilice para conectarse y leer datos de su(s) tabla(s). La cuenta de servicio debe tener los siguientes permisos: 

- **Usuario de conexión BigQuery:** Esto permitirá a Braze hacer conexiones
- **Usuario de BigQuery:** Esto proporcionará acceso a Braze para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- **Visor de datos BigQuery:** Esto proporcionará acceso a Braze para ver los conjuntos de datos y su contenido.
- **Usuario de BigQuery Job:** Esto proporcionará acceso a Braze para ejecutar trabajos

Tras crear la cuenta de servicio y conceder los permisos, genera una clave JSON. [Aquí](https://cloud.google.com/iam/docs/keys-create-delete) encontrará más información sobre cómo hacerlo. Actualizarás esto al panel de Braze más tarde. 

#### Paso 3: Permitir el acceso a las IP Braze    

Si tienes políticas de red en vigor, debes dar acceso de red Braze a tu instancia de BigQuery. Permita el acceso desde las siguientes IP correspondientes a la región de su panel de control Braze.  

| Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Para las instancias `EU-01` y `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`

{% endtab %}
{% tab Databricks %}

#### Paso 1: Preparar la mesa 

Opcionalmente, configure un nuevo Catálogo o Esquema para contener su tabla de origen.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Cree una o más tablas para utilizar en su integración CDI con los siguientes campos:


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
  payload STRING
);
```


| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| MARCA DE TIEMPO | REQUERIDO |
| `PAYLOAD`| STRING o STRUCT | REQUERIDO |
| `EXTERNAL_ID`| CADENA | NULABLE |
| `ALIAS_NAME`| CADENA | NULABLE |
| `ALIAS_LABEL`| CADENA | NULABLE |
| `BRAZE_ID`| CADENA | NULABLE |
| `EMAIL`| CADENA | NULABLE |
| `PHONE`| CADENA | NULABLE |

Puede nombrar el esquema y la tabla como desee, pero los nombres de las columnas deben coincidir con la definición anterior.

- `UPDATED_AT` - Hora a la que se actualizó o añadió esta fila a la tabla. Sólo se sincronizarán las filas que se hayan añadido o actualizado desde la última sincronización.
- Columnas de identificación de usuarios. Su tabla puede contener una o más columnas de identificadores de usuario. Cada fila solo debe contener un identificador (ya sea `external_id`, la combinación de `alias_name` y `alias_label`, o `braze_id`). Una tabla de origen puede tener columnas para uno, dos o los tres tipos de identificadores. 
    - `EXTERNAL_ID` - Identifica al usuario que desea actualizar. Esto debería coincidir con el valor `external_id` utilizado en Braze. 
    - `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`.
    - `BRAZE_ID` - El identificador de usuario Braze. Esto lo genera el SDK de Braze, y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de Cloud Data Ingestion. Para crear nuevos usuarios, especifique un ID de usuario externo o un alias de usuario. 
    - `EMAIL` - La dirección de correo electrónico del usuario. Si existen varios perfiles con la misma dirección de correo electrónico, se dará prioridad al perfil actualizado más recientemente. Si incluye tanto el correo electrónico como el teléfono, utilizaremos el correo electrónico como identificador principal.
    - `PHONE` - El número de teléfono del usuario. Si existen varios perfiles con el mismo número de teléfono, se dará prioridad al perfil actualizado más recientemente. 
- `PAYLOAD` - Se trata de una cadena o estructura de los campos que desea sincronizar con el usuario en Braze.

#### Paso 2: Crear un token de acceso  

Para que Braze pueda acceder a Databricks, es necesario crear un token de acceso personal.

1. En tu espacio de trabajo de Databricks, selecciona tu nombre de usuario de Databricks en la barra superior y, a continuación, selecciona **Configuración de usuario** en el desplegable.
2. En la pestaña Tokens de acceso, selecciona **Generar nuevo token**.
3. Introduzca un comentario que le ayude a identificar este token, como "Braze CDI", y cambie la vida útil del token a sin vida útil dejando la casilla Vida útil (días) vacía (en blanco).
4. Seleccione **Generar**.
5. Copie el token mostrado y seleccione **Hecho**.

Guarde el token en un lugar seguro hasta que necesite introducirlo en el panel de control de Braze durante el paso de creación de credenciales.

#### Paso 3: Permitir el acceso a las IP Braze    

Si tienes políticas de red en vigor, debes dar acceso de red Braze a tu instancia de Databricks. Permita el acceso desde las siguientes IP correspondientes a la región de su panel de control Braze.  

| Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07` | Para las instancias `EU-01` y `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`

{% endtab %}

{% endtabs %}

### Paso 2: Crear una nueva integración en el cuadro de mandos de Braze

{% tabs %}
{% tab Snowflake %}

Ve a **Integraciones de socios** > **Socios tecnológicos.** Busque la página Snowflake y seleccione **Crear nueva sincronización de importación**.

{% alert note %}
Si utiliza la [navegación más antigua]({{site.baseurl}}/navigation), vaya a **Socios tecnológicos**.
{% endalert %}

#### Paso 1: Añadir información de conexión Snowflake y tabla de origen

Introduce la información de tu almacén de datos Snowflake y la tabla de origen, y pasa al siguiente paso.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### Paso 2: Configurar los detalles de sincronización
A continuación, elige un nombre para la sincronización e introduce los correos electrónicos de los contactos. Utilizaremos esta información de contacto para notificarle cualquier error de integración, como la eliminación inesperada del acceso a la mesa.

Los correos electrónicos de contacto sólo recibirán notificaciones de errores globales o a nivel de sincronización, como falta de tablas, permisos y otros. No recibirán ediciones a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden ser los siguientes:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Sólo para sincronización de catálogos) No hay espacio en el nivel de catálogo

![]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en el panel de control de Braze para programar la sincronización periódica. Los tipos de datos admitidos son Atributos personalizados, Eventos personalizados y Eventos de compra, y el tipo de datos para una sincronización no se puede cambiar después de la creación. 

#### Añadir una clave pública al usuario Braze
En este punto, debe volver a Snowflake para completar la configuración. Añada la clave pública que aparece en el panel al usuario que creó para que Braze se conecte a Snowflake.

Para más información sobre cómo hacerlo, consulta la [documentación de Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si desea rotar las claves en cualquier momento, podemos generar un nuevo par de claves y proporcionarle la nueva clave pública.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

Ve a **Integraciones de socios** > **Socios tecnológicos.** Busque la página Redshift y seleccione **Crear nueva sincronización de importación**.

{% alert note %}
Si utiliza la [navegación más antigua]({{site.baseurl}}/navigation), vaya a **Socios tecnológicos**.
{% endalert %}

#### Paso 1: Añadir información de conexión Redshift y tabla de origen
Introduce la información de tu almacén de datos Redshift y la tabla de origen. Si utiliza un túnel de red privada, active el control deslizante e introduzca la información del túnel. A continuación, continúe con el siguiente paso.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### Paso 2: Configurar los detalles de sincronización
A continuación, elige un nombre para la sincronización e introduce los correos electrónicos de los contactos. Utilizaremos esta información de contacto para notificarle cualquier error de integración, como la eliminación inesperada del acceso a la mesa.

Los correos electrónicos de contacto sólo recibirán notificaciones de errores globales o a nivel de sincronización, como falta de tablas, permisos y otros. No recibirán ediciones a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden ser los siguientes:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Sólo para sincronización de catálogos) No hay espacio en el nivel de catálogo

![]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en el panel de control de Braze para programar la sincronización periódica. Los tipos de datos admitidos son Atributos personalizados, Eventos personalizados y Eventos de compra, y el tipo de datos para una sincronización no se puede cambiar después de la creación.
{% endtab %}
{% tab BigQuery %}

Ve a **Integraciones de socios** > **Socios tecnológicos.** Busque la página BigQuery y seleccione **Crear nueva sincronización de importación**.

{% alert note %}
Si utiliza la [navegación más antigua]({{site.baseurl}}/navigation), vaya a **Socios tecnológicos**.
{% endalert %}

#### Paso 1: Añadir información de conexión BigQuery y tabla de origen
Cargue la clave JSON y proporcione un nombre para la cuenta de servicio; a continuación, introduzca los detalles de su tabla de origen.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### Paso 2: Configurar los detalles de sincronización
A continuación, elige un nombre para la sincronización e introduce los correos electrónicos de los contactos. Utilizaremos esta información de contacto para notificarle cualquier error de integración, como la eliminación inesperada del acceso a la mesa.

Los correos electrónicos de contacto sólo recibirán notificaciones de errores globales o a nivel de sincronización, como falta de tablas, permisos y otros. No recibirán ediciones a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden ser los siguientes:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Sólo para sincronización de catálogos) No hay espacio en el nivel de catálogo

![]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en el panel de control de Braze para programar la sincronización periódica. Los tipos de datos soportados son Atributos Personalizados, Eventos Personalizados, Eventos de Compra y Borrados de Usuario. El tipo de datos de una sincronización no puede modificarse después de su creación. 

{% endtab %}
{% tab Databricks %}

Ve a **Integraciones de socios** > **Socios tecnológicos.** Busca la página Databricks y selecciona **Crear nueva sincronización de importación**.

{% alert note %}
Si utiliza la [navegación más antigua]({{site.baseurl}}/navigation), vaya a **Socios tecnológicos**.
{% endalert %}

#### Paso 1: Añadir información de conexión Databricks y tabla de origen
Introduce la información de tu almacén de datos Databricks y la tabla de origen, y pasa al siguiente paso.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### Paso 2: Configurar los detalles de sincronización
A continuación, elige un nombre para la sincronización e introduce los correos electrónicos de los contactos. Utilizaremos esta información de contacto para notificarle cualquier error de integración, como la eliminación inesperada del acceso a la mesa.

Los correos electrónicos de contacto sólo recibirán notificaciones de errores globales o a nivel de sincronización, como falta de tablas, permisos y otros. No recibirán ediciones a nivel de fila. Los errores globales indican problemas críticos con la conexión que impiden que se ejecuten las sincronizaciones. Estos problemas pueden ser los siguientes:

- Problemas de conectividad
- Falta de recursos
- Problemas de permisos
- (Sólo para sincronización de catálogos) No hay espacio en el nivel de catálogo

![]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

También elegirás el tipo de datos y la frecuencia de sincronización. La frecuencia puede ser desde cada 15 minutos hasta una vez al mes. Utilizaremos la zona horaria configurada en el panel de control de Braze para programar la sincronización periódica. Los tipos de datos admitidos son atributos personalizados, eventos personalizados, eventos de compra y eliminaciones de usuarios. El tipo de datos de una sincronización no puede modificarse después de su creación. 

{% endtab %}
{% endtabs %}

### Paso 3: Probar conexión

{% tabs %}
{% tab Snowflake %}

Vuelve al panel de control de Braze y selecciona **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}
{% tab Redshift %}
Vuelve al panel de control de Braze y selecciona **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endtab %}
{% tab Red privada Redshift %}

Vuelve al panel de control de Braze y selecciona **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endtab %}
{% tab BigQuery %}

Una vez introducidos todos los detalles de configuración de la sincronización, seleccione **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Databricks %}

Una vez introducidos todos los detalles de configuración de la sincronización, seleccione **Probar conexión**. Si tienes éxito, verás una vista previa de los datos. Si, por alguna razón, no podemos conectar, mostraremos un mensaje de error para ayudarte a solucionar el problema.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Debe probar con éxito una integración antes de que pueda pasar del estado Borrador al Activo. Si necesita salir de la página de creación, su integración se guardará y podrá volver a visitar la página de detalles para realizar cambios y pruebas.  
{% endalert %}

## Configurar integraciones o usuarios adicionales (opcional)

{% tabs %}
{% tab Snowflake %}
Puede configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puede reutilizar las credenciales existentes si se conecta a la cuenta Snowflake.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_4.png %})

Si reutiliza el mismo usuario y función en todas las integraciones, **no** tendrá que volver a añadir la clave pública.
{% endtab %}
{% tab Redshift %}
Puede configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puede reutilizar las credenciales existentes si se conecta a la misma cuenta de Snowflake o Redshift.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_9.png %})

Si reutiliza el mismo usuario en varias integraciones, no podrá eliminar el usuario en el panel de control de Braze hasta que se elimine de todas las sincronizaciones activas.
{% endtab %}
{% tab BigQuery %}

Puede configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puede reutilizar las credenciales existentes si se conecta a la misma cuenta de BigQuery.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_14.png %})

Si reutiliza el mismo usuario en varias integraciones, no podrá eliminar el usuario en el panel de control de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% tab Databricks %}

Puede configurar varias integraciones con Braze, pero cada integración debe configurarse para sincronizar una tabla diferente. Al crear sincronizaciones adicionales, puedes reutilizar las credenciales existentes si te conectas a la misma cuenta de Databricks.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_17.png %})

Si reutiliza el mismo usuario en varias integraciones, no podrá eliminar el usuario en el panel de control de Braze hasta que se elimine de todas las sincronizaciones activas.

{% endtab %}
{% endtabs %}

## Ejecución de la sincronización

{% tabs %}
{% tab Snowflake %}
Una vez activada, la sincronización se ejecutará según el calendario configurado durante la instalación. Si desea ejecutar la sincronización fuera del calendario normal de pruebas o recuperar los datos más recientes, seleccione **Sincronizar ahora**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
Una vez activada, la sincronización se ejecutará según el calendario configurado durante la instalación. Si desea ejecutar la sincronización fuera del calendario normal de pruebas o recuperar los datos más recientes, seleccione **Sincronizar ahora**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

Una vez activada, la sincronización se ejecutará según el calendario configurado durante la instalación. Si desea ejecutar la sincronización fuera del calendario normal de pruebas o recuperar los datos más recientes, seleccione **Sincronizar ahora**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

Una vez activada, la sincronización se ejecutará según el calendario configurado durante la instalación. Si desea ejecutar la sincronización fuera del calendario normal de pruebas o recuperar los datos más recientes, seleccione **Sincronizar ahora**. Esta ejecución no afectará a las futuras sincronizaciones programadas regularmente.

![]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_6.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_7.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_8.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_9.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_10.png %}
[6]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
