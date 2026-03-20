---
nav_title: Sincronizar y eliminar datos de la cuenta
article_title: Sincronizar los datos de la cuenta mediante CDI
page_order: 4
page_type: reference
description: "Aprende a sincronizar los datos de tu cuenta de Braze utilizando CDI."

---

# Sincronizar los datos de la cuenta mediante CDI

> Aprende a sincronizar los datos de tu cuenta de Braze utilizando CDI.

{% alert important %}
[Los objetos de cuenta](https://braze.com/unlisted_docs/account_opportunity_object/) están en fase beta y son necesarios para utilizar esta característica. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en la beta.
{% endalert %}

## Requisitos previos

Antes de poder sincronizar los datos de tu cuenta mediante CDI, deberás [configurar el esquema de tus cuentas](https://braze.com/unlisted_docs/account_opportunity_object/).

{% alert note %}
Realiza actualizaciones en el esquema de tu cuenta solo cuando la sincronización esté pausada o no esté planificada, para evitar conflictos entre los datos de tu almacén de datos y el esquema en Braze.
{% endalert %}

## Cómo funciona la sincronización

- Cada sincronización importa filas donde `UPDATED_AT` es posterior a la última marca de tiempo sincronizada. Las filas que coinciden exactamente con la marca de tiempo límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo. Para más información, consulta [Evitar la resincronización de filas con marcas de tiempo duplicadas]({{site.baseurl}}/user_guide/data/cloud_ingestion/best_practices/#avoid-resyncing-rows-with-duplicate-timestamps).
- Los datos de la integración crean o actualizan cuentas basándose en el `id` proporcionado.
- Si `DELETED` es `true`, la cuenta se elimina.
- La sincronización no registra puntos de datos, pero todos los datos sincronizados cuentan para el uso total de tus cuentas, medido por el total de datos almacenados; no es necesario limitarse solo a los datos modificados.
- Los campos que no se encuentran en el esquema de tus cuentas se descartan; actualiza el esquema antes de sincronizar los nuevos campos.
- Puedes actualizar, reanudar o pausar una sincronización pasando el cursor por encima del nombre de la sincronización y seleccionando la acción correspondiente.

## Sincroniza los datos de tu cuenta

Puedes sincronizar los datos de tu cuenta utilizando CDI a través de un almacén de datos o un almacenamiento de archivos.

{% tabs local %}
{% tab Data Warehouse %}
Para integrar tu origen de datos con tu almacén de datos:

{% subtabs %}
{% subtab Snowflake %}

1. Crea una tabla de origen en Snowflake. Utiliza los nombres del ejemplo o elige tus propios nombres de base de datos, esquema y tabla. También puedes utilizar una vista o una vista materializada en lugar de una tabla.
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the account to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Name of the account to be created or updated
         NAME VARCHAR(16777216) NOT NULL,
         --Account fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The account associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. Crea un rol, un almacén y un usuario, y concede permisos. Si ya tienes credenciales de otra sincronización, puedes reutilizarlas; asegúrate de que tengan acceso a la tabla de cuentas.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Si utilizas políticas de red, añade las IP de Braze a la lista de permitidas para que el servicio CDI pueda conectarse. Para consultar la lista de IP, ve a [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. En el panel de Braze, ve a **Data Settings** > **Cloud Data Ingestion** y crea una nueva sincronización.
5. Introduce los detalles de conexión (o reutiliza los existentes) y luego añade la tabla de origen.
6. Selecciona el tipo de sincronización **Accounts** y luego introduce el nombre de la integración y la planificación. 
7. Elige la frecuencia de sincronización.
8. Añade la clave pública del dashboard al usuario que creaste. Esto requiere un usuario con acceso `SECURITYADMIN` o superior en Snowflake. 
9. Selecciona **Test Connection** para confirmar la configuración. 
10. Cuando hayas terminado, guarda la sincronización.

{% endsubtab %}
{% subtab Redshift %}

1. Crea una tabla de origen en Redshift. Utiliza los nombres del ejemplo o elige tus propios nombres de base de datos, esquema y tabla. También puedes utilizar una vista o una vista materializada en lugar de una tabla.
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the account to be created or updated
       id varchar not null,
       --Name of the account to be created or updated
       name varchar not null,
       --Account fields and values that should be added or updated
       payload varchar(max),
       --The account associated with this ID should be deleted
       deleted boolean
    )
    ```
2. Crea un usuario y concede permisos. Si ya tienes credenciales de otra sincronización, puedes reutilizarlas; asegúrate de que tengan acceso a la tabla de cuentas.
    {% raw %}
    ```sql 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE ACCOUNTS_SYNC TO braze_user;
    ```
    {% endraw %}
3. Si tienes un firewall o políticas de red, permite el acceso de Braze a tu instancia de Redshift. Para consultar la lista de IP, ve a [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab BigQuery %}

1. (Opcional) Crea un nuevo proyecto o conjunto de datos para tu tabla de origen.  
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. Crea la tabla de origen para tu integración CDI:  
    ```sql
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp,
      id STRING,
      name STRING,
      payload JSON,
      deleted BOOLEAN
    );
    ```

    Consulta lo siguiente al crear tu tabla de origen:

    | Nombre del campo | Tipo | ¿Obligatorio? |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | Sí |
    | `PAYLOAD` | JSON | Sí |
    | `ID` | String | Sí |
    | `NAME` | String | Sí |
    | `DELETED` | Boolean | Opcional |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="3"}
3. Crea un usuario y concede permisos. Si ya tienes credenciales de otra sincronización, puedes reutilizarlas siempre que tengan acceso a la tabla de cuentas.

    | Permiso | Propósito |
    |------------|---------|
    | BigQuery Connection User | Permite a Braze conectarse. |
    | BigQuery User | Permite a Braze ejecutar consultas, leer metadatos y listar tablas. |
    | BigQuery Data Viewer | Permite a Braze ver conjuntos de datos y su contenido. |
    | BigQuery Job User | Permite a Braze ejecutar trabajos. |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

    Después de conceder los permisos, genera una clave JSON. Consulta [Crear y eliminar claves](https://cloud.google.com/iam/docs/keys-create-delete) para obtener instrucciones. La cargarás en el panel de Braze más adelante.

{:start="4"}
4. Si utilizas políticas de red, permite que las IP de Braze accedan a tu instancia de BigQuery. Para consultar la lista de IP, ve a [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Databricks %}

1. Crea un catálogo o esquema para tu tabla de origen.  
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. Crea la tabla de origen para tu integración CDI:  
    ```sql
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp(),
      id STRING,
      name STRING,
      payload STRING, STRUCT, or MAP,
      deleted BOOLEAN
    );
    ```

    Consulta lo siguiente al crear tu tabla de origen:

    | Nombre del campo | Tipo | ¿Obligatorio? |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | Sí |
    | `PAYLOAD` | String, Struct, or Map | Sí |
    | `ID` | String | Sí |
    | `NAME` | String | Sí |
    | `DELETED` | Boolean | Opcional |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="3"}
3. Crea un token de acceso personal en Databricks:
    1. Selecciona tu nombre de usuario y luego selecciona **User Settings**.  
    2. En la pestaña **Access tokens**, selecciona **Generate new token**.  
    3. Añade un comentario para identificar el token, como "Braze CDI".  
    4. Deja **Lifetime (days)** en blanco para que no expire y luego selecciona **Generate**.  
    5. Copia y guarda el token de forma segura para usarlo en el panel de Braze.

{:start="4"}
4. Si utilizas políticas de red, permite que las IP de Braze accedan a tu instancia de Databricks. Para consultar la lista de IP, ve a [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Microsoft Fabric %}

1. Crea una o más tablas para tu integración CDI con estos campos:
    ```sql
    CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
    (
      UPDATED_AT DATETIME2(6) NOT NULL,
      PAYLOAD VARCHAR NOT NULL,
      ID VARCHAR NOT NULL,
      NAME VARCHAR NOT NULL,
      DELETED BIT
    )
    GO
    ```

{:start="2"}
2. Crea un service principal y concede permisos. Si ya tienes credenciales de otra sincronización, puedes reutilizarlas; asegúrate de que tengan acceso a la tabla de cuentas.

{:start="3"}
3. Si utilizas políticas de red, permite que las IP de Braze accedan a tu instancia de Microsoft Fabric. Para consultar la lista de IP, ve a [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab File Storage %}
Para sincronizar datos de cuentas desde almacenamiento de archivos, crea un archivo de origen con los siguientes campos.

| Campo | ¿Obligatorio? | Descripción |  
| --- | --- | --- |  
| `ID` | Sí | ID de la cuenta a actualizar o crear |  
| `NAME` | Sí | Nombre de la cuenta |  
| `PAYLOAD` | Sí | Cadena JSON de los campos a sincronizar con la cuenta en Braze |  
| `DELETED` | Opcional | Booleano que indica si se debe eliminar la cuenta de Braze |  
| `UPDATED_AT` | _*No compatible_ | El almacenamiento de archivos no admite columnas `UPDATED_AT` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Los nombres de archivo deben seguir las reglas de AWS y ser únicos. Añade marcas de tiempo para ayudar a garantizar la unicidad. Para más información sobre la sincronización con Amazon S3, consulta [Integraciones de almacenamiento de archivos]({{site.baseurl}}/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

Los siguientes ejemplos muestran formatos JSON y CSV válidos para sincronizar datos de cuentas desde almacenamiento de archivos.

{% subtabs %}
{% subtab JSON Accounts %}
```jsonl  
{"id":"s3-qa-0","name":"account0","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"id":"s3-qa-1","name":"account1","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":true}
{"id":"s3-qa-2","name":"account2","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":false}
{"id":"s3-qa-3","name":"account3","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
```  

{% alert important %}
Cada línea del archivo de origen debe contener JSON válido o, de lo contrario, el archivo se omitirá. 
{% endalert %}
{% endsubtab %}
{% subtab CSV Accounts with Delete %}
```plaintext  
ID,NAME,PAYLOAD,DELETED
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}",TRUE 
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}",FALSE
```
{% endsubtab %}
{% subtab CSV Accounts without Delete %}
```plaintext  
ID,NAME,PAYLOAD
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}"
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}"
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Crear una vista de sincronización

Crear una vista de sincronización en tu almacén de datos permite que el origen se actualice automáticamente sin necesidad de reescribir consultas adicionales.

Por ejemplo, si tienes una tabla de datos de cuentas llamada `account_details_1` con `account_id`, `account_name` y tres atributos adicionales, podrías crear una vista de sincronización como la siguiente:

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS 
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    account_id as id,
    account_name as name,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "account_details_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    account_id as id,
    account_name as name,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "account_details_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    account_id as ID,
    account_name as NAME,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.account_details_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    account_id as ID,
    account_name as NAME,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.account_details_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [BRAZE_CLOUD_PRODUCTION].[INGESTION].[ACCOUNTS_SYNC]
AS SELECT 
    account_id as ID,
    account_name as NAME,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[account_details_1] ;
```
{% endtab %}
{% endtabs %}