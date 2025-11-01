---
nav_title: Sincronizar y eliminar datos del catálogo
article_title: Sincronizar y eliminar datos del catálogo
page_order: 4
page_type: reference
description: "Esta página ofrece un resumen de cómo sincronizar los datos del catálogo."

---

# Sincronizar y eliminar datos del catálogo

> En esta página se explica cómo sincronizar los datos del catálogo.
 
## Paso 1: Crear un nuevo catálogo

Antes de crear una nueva integración de Cloud Data Ingestion (CDI) para [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/), tienes que crear un nuevo catálogo o identificar un catálogo existente que quieras utilizar para la integración. Hay varias formas de crear un catálogo nuevo y cualquiera de ellas funcionará para la integración CDI:
- Cargar un [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-1-upload-csv)
- Crea un catálogo en [el panel de Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-2-create-in-browser) o durante la configuración de CDI.
- Crea un catálogo utilizando el [punto final Crear catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)

Cualquier cambio en el esquema del catálogo (por ejemplo, añadir nuevos campos o cambiar el tipo de campo) debe hacerse a través del panel del catálogo antes de que los datos actualizados se sincronicen a través de CDI. Recomendamos realizar estas actualizaciones cuando la sincronización esté en pausa o no esté programada para ejecutarse, a fin de evitar conflictos entre los datos de tu almacén de datos y el esquema en Braze.

## Paso 2: Integrar la ingesta de datos en la nube con los datos del catálogo
La configuración de una sincronización de catálogos sigue de cerca el proceso de [las integraciones CDI de datos de usuario]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup). 

{% tabs %}
{% tab Snowflake %}

1. Configura una tabla de fuentes en Snowflake. Puedes utilizar los nombres del siguiente ejemplo o elegir tus propios nombres de base de datos, esquema y tabla. También puedes utilizar una vista o una vista materializada en lugar de una tabla.
  ```json
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the catalog item to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Catalog fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The catalog item associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. Set up a role, warehouse, and user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.
    ```json
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. If your Snowflake account has network policies, allowlist the Braze IPs so the CDI service can connect. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. In the Braze dashboard, navigate to **Technology Partners** > **Snowflake**, and create a new sync.
5. Enter connection details (or reuse existing credentials) and the source table.
6. Proceed to step 2 of the setup flow, select the “Catalogs” sync type, and input the integration name and schedule. Note that the name of the integration should **exactly match** the name of the catalog you previously created.
7. Choose a sync frequency and proceed to the next step.
8. Add the public key displayed on the dashboard to the user you created for Braze to connect to Snowflake. To complete this step, you will need someone with `SECURITYADMIN` access or higher in Snowflake. 
9. Select **Test Connection** so that everything works as expected. 
10. Save the sync, and use the synced catalog data for all your personalization use cases. 
{% endtab %}
{% tab Redshift %}

1. Set up a source table in Redshift. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.
    ```json
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the catalog item to be created or updated
       id varchar not null,
       --Catalog fields and values that should be added or updated
       payload varchar(max),
       --The catalog item associated with this ID should be deleted
       deleted boolean
    )
    ```
2. Set up a user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.
    {% raw %}
    ```json 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. If you have a firewall or other network policies, you must give Braze network access to your Redshift instance. Allow access from the below IPs corresponding to your Braze dashboard’s region. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. Optionally, set up a new project or dataset to hold your source table. 

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o varias tablas para utilizarlas en tu integración CDI con los siguientes campos:

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| NOMBRE DEL CAMPO | TIPO | MODO |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUERIDO |
| CARGA ÚTIL | JSON | REQUERIDO |
| ID | CADENA | REQUERIDO |
| SUPRIMIDO | BOOLEAN | OPCIONAL |

{:start="2"}

2. Configura un usuario y concédele los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen del catálogo.
La cuenta de servicio debe tener los siguientes permisos:
- Usuario de conexión a BigQuery: Esto permitirá a Braze establecer conexiones.
- Usuario de BigQuery: Esto proporcionará acceso a Braze para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- Visor de datos BigQuery: Esto proporcionará acceso a Braze para ver los conjuntos de datos y su contenido.
- Usuario de BigQuery Job: Esto proporcionará acceso a Braze para ejecutar trabajos<br><br>Tras crear la cuenta de servicio y conceder los permisos, genera una clave JSON. Consulta [Claves crear y borrar](https://cloud.google.com/iam/docs/keys-create-delete) para más información. Actualizarás esto al panel de Braze más tarde.

{:start="3"}
3\. Si tienes políticas de red en vigor, debes dar acceso de red Braze a tu instancia de BigQuery. Para obtener una lista de IP, consulta la [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Configura una tabla de origen en Databricks. Puedes utilizar los nombres del ejemplo siguiente o elegir tus nombres de catálogo, esquema y tabla. También puedes utilizar una vista o una vista materializada en lugar de una tabla.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  id STRING,
  deleted BOOLEAN,
  payload STRING, STRUCT, or MAP
);
```

| NOMBRE DEL CAMPO | TIPO | MODO |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUERIDO |
| CARGA ÚTIL | CADENA, ESTRUCTURA o MAPA | REQUERIDO |
| ID | CADENA | REQUERIDO |
| SUPRIMIDO | BOOLEAN | NULABLE |

{:start="2"}

2. Crea un token de acceso personal en tu espacio de trabajo Databricks.

- a. Selecciona tu nombre de usuario de Databricks y, a continuación, selecciona **Configuración de usuario** en el menú desplegable.
- b. En la pestaña **Tokens de acceso**, selecciona **Generar nuevo token**.
- c. Introduce un comentario que te ayude a identificar este token, como "Braze CDI". 
- d. Cambia la duración del token a sin duración dejando en blanco la casilla **Duración (días)**. Selecciona **Generar**.
- e. Copia el token mostrado y selecciona **Hecho**. 
- f. Guarda el token en un lugar seguro hasta que necesites introducirlo durante el paso de creación de credenciales en el panel de Braze.

{:start="3"}
3\. Si tienes políticas de red en vigor, debes dar acceso de red Braze a tu instancia de Databricks. Para ver una lista de IP, consulta la página de [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Microsoft Fabric %}

Crea una o varias tablas para utilizarlas en tu integración CDI con los siguientes campos:

```json
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  ID VARCHAR NOT NULL,
  DELETED BIT
)
GO
```

{:start="2"}

2. Configura un servicio principal y concede los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas; sólo tienes que asegurarte de ampliar el acceso a la tabla de origen del catálogo. Para saber más sobre cómo crear una nueva entidad de seguridad de servicio y sus credenciales, consulta la página [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views). 

{:start="3"}
3\. Si tienes políticas de red en vigor, debes dar acceso de red a Braze a tu instancia de Microsoft Fabric. Para ver una lista de IP, consulta la [Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab S3 %}
Configura tus archivos de origen en S3 proporcionando archivos JSON o CSV. Tenlo en cuenta:

- Los archivos no pueden incluir una columna `UPDATED_AT`   
- Puedes incluir un campo opcional `DELETED` para marcar los elementos a eliminar 

{% subtabs %}
{% subtab JSON %}
```json
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```
{% endsubtab %}

{% subtab CSV %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
{% endsubtab %}
{% endsubtabs %}

Para más detalles sobre la configuración, consulta [Integraciones de almacenamiento de archivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/).

{% endtab %}
{% endtabs %}

## Cómo funciona la integración

Cada vez que se ejecute la sincronización, Braze extraerá todas las filas en las que `UPDATED_AT` sea igual o posterior a la última marca de tiempo sincronizada. Te recomendamos que crees una vista en tu almacén de datos a partir de los datos de tu catálogo para configurar una tabla de origen que se actualice completamente cada vez que se ejecute una sincronización. Con las vistas, no tendrás que reescribir la consulta cada vez.

Por ejemplo, si tienes una tabla de datos de productos (`product_catalog_1`) con `product_id` y tres atributos adicionales, podrías sincronizar la siguiente vista:

{% tabs %}
{% tab Snowflake %}
```json
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS 
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    product_id as id,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    Product_id as id,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab BigQuery %}
```json
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Databricks %}
```json
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE VIEW [braze].[user_update_example]
AS SELECT 
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- Los datos obtenidos de la integración se utilizarán para crear o actualizar elementos en el catálogo de destino basándose en el `id` proporcionado.
- Si la opción ELIMINADO está establecida en `true`, se eliminará el elemento del catálogo correspondiente.
- La sincronización no registrará puntos de datos, pero todos los datos sincronizados contarán para el uso total de tu catálogo; este uso se mide en función de los datos totales almacenados, por lo que no tienes que preocuparte de sincronizar sólo los datos modificados.
