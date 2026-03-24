---
nav_title: Sincronizar y eliminar datos del catálogo
article_title: Sincronizar y eliminar datos de catálogo
page_order: 4
page_type: reference
description: "Esta página ofrece un resumen de cómo sincronizar los datos del catálogo."

---

# Sincronizar y eliminar datos del catálogo

> En esta página se explica cómo sincronizar los datos del catálogo.
 
## Paso 1: Crear un nuevo catálogo

Antes de crear una nueva integración de ingesta de datos en la nube (CDI) para [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/), tienes que crear un nuevo catálogo o identificar un catálogo existente que quieras utilizar para la integración. Existen varias formas de crear un nuevo catálogo y cualquiera de ellas funcionará para la integración CDI:
- Cargar un [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-1-upload-csv)
- Crear un catálogo en el [panel de Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-2-create-in-browser) o durante la configuración de CDI.
- Crear un catálogo utilizando el [punto de conexión Crear catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)

Cualquier cambio en el esquema del catálogo (por ejemplo, añadir nuevos campos o cambiar el tipo de campo) debe realizarse a través del dashboard del catálogo antes de que los datos actualizados se sincronicen a través de CDI. Recomendamos realizar estas actualizaciones cuando la sincronización esté en pausa o no esté programada para ejecutarse, a fin de evitar conflictos entre los datos de tu almacén de datos y el esquema en Braze.

## Paso 2: Integrar la ingesta de datos en la nube con los datos del catálogo
La configuración de una sincronización de catálogos sigue de cerca el proceso de [las integraciones CDI de datos de usuario]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup). 

{% tabs %}
{% tab Snowflake %}

1. Configura una tabla de origen en Snowflake. Puedes utilizar los nombres del siguiente ejemplo o elegir tus propios nombres de base de datos, esquema y tabla. También puedes utilizar una vista o una vista materializada en lugar de una tabla.
  ```sql
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
2. Configura un rol, un almacén y un usuario, y concede los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen del catálogo.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Si tu cuenta de Snowflake tiene políticas de red, añade las IP de Braze a la lista de permitidas para que el servicio CDI pueda conectarse. Para ver una lista de IP, consulta la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. En el dashboard de Braze, ve a **Socios tecnológicos** > **Snowflake** y crea una nueva sincronización.
5. Introduce los detalles de conexión (o reutiliza las credenciales existentes) y la tabla de origen.
6. Continúa con el paso 2 del flujo de configuración, selecciona el tipo de sincronización "Catalogs" e introduce el nombre de la integración y la planificación. Ten en cuenta que el nombre de la integración debe **coincidir exactamente** con el nombre del catálogo que creaste anteriormente.
7. Elige una frecuencia de sincronización y continúa con el siguiente paso.
8. Añade la clave pública que se muestra en el dashboard al usuario que creaste para que Braze se conecte a Snowflake. Para completar este paso, necesitarás a alguien con acceso `SECURITYADMIN` o superior en Snowflake. 
9. Selecciona **Probar conexión** para verificar que todo funciona como se espera. 
10. Guarda la sincronización y utiliza los datos del catálogo sincronizados para todos tus casos de uso de personalización. 
{% endtab %}
{% tab Redshift %}

1. Configura una tabla de origen en Redshift. Puedes utilizar los nombres del siguiente ejemplo o elegir tus propios nombres de base de datos, esquema y tabla. También puedes utilizar una vista o una vista materializada en lugar de una tabla.
    ```sql
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
2. Configura un usuario y concede los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen del catálogo.
    {% raw %}
    ```sql 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. Si tienes un firewall u otras políticas de red, debes dar acceso de red a Braze a tu instancia de Redshift. Permite el acceso desde las IP que se indican a continuación, correspondientes a la región de tu dashboard de Braze. Para ver una lista de IP, consulta la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. Opcionalmente, configura un nuevo proyecto o conjunto de datos para alojar tu tabla de origen. 

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Crea una o más tablas para utilizar en tu integración CDI con los siguientes campos:

```sql
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
| UPDATED_AT | TIMESTAMP | OBLIGATORIO |
| PAYLOAD | JSON | OBLIGATORIO |
| ID | STRING | OBLIGATORIO |
| DELETED | BOOLEAN | OPCIONAL |

{:start="2"}

2. Configura un usuario y concede los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas, pero asegúrate de ampliar el acceso a la tabla de origen del catálogo. 
La cuenta de servicio debe tener los siguientes permisos:
- BigQuery Connection User: permite a Braze realizar conexiones.
- BigQuery User: proporciona a Braze acceso para ejecutar consultas, leer metadatos de conjuntos de datos y listar tablas.
- BigQuery Data Viewer: proporciona a Braze acceso para ver los conjuntos de datos y su contenido.
- BigQuery Job User: proporciona a Braze acceso para ejecutar trabajos.<br><br>Tras crear la cuenta de servicio y conceder los permisos, genera una clave JSON. Consulta [Crear y eliminar claves](https://cloud.google.com/iam/docs/keys-create-delete) para obtener más información. La cargarás en el dashboard de Braze más adelante.

{:start="3"}
3. Si tienes políticas de red en vigor, debes dar acceso de red a Braze a tu instancia de BigQuery. Para ver una lista de IP, consulta la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Configura una tabla de origen en Databricks. Puedes utilizar los nombres del siguiente ejemplo o elegir tus propios nombres de catálogo, esquema y tabla. También puedes utilizar una vista o una vista materializada en lugar de una tabla.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```sql
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
| UPDATED_AT | TIMESTAMP | OBLIGATORIO |
| PAYLOAD | STRING, STRUCT o MAP | OBLIGATORIO |
| ID | STRING | OBLIGATORIO |
| DELETED | BOOLEAN | NULABLE |

{:start="2"}

2. Crea un token de acceso personal en tu espacio de trabajo de Databricks.

- a. Selecciona tu nombre de usuario de Databricks y, a continuación, selecciona **Configuración de usuario** en el menú desplegable.
- b. En la pestaña **Tokens de acceso**, selecciona **Generar nuevo token**.
- c. Introduce un comentario que te ayude a identificar este token, como "Braze CDI". 
- d. Cambia la duración del token a sin duración dejando en blanco la casilla **Duración (días)**. Selecciona **Generar**.
- e. Copia el token mostrado y selecciona **Hecho**. 
- f. Guarda el token en un lugar seguro hasta que necesites introducirlo durante el paso de creación de credenciales en el dashboard de Braze.

{:start="3"}
3. Si tienes políticas de red en vigor, debes dar acceso de red a Braze a tu instancia de Databricks. Para ver una lista de IP, consulta la página de [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Microsoft Fabric %}

Crea una o más tablas para utilizar en tu integración CDI con los siguientes campos:

```sql
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

2. Configura un principal de servicio y concede los permisos adecuados. Si ya tienes credenciales de una sincronización existente, puedes reutilizarlas; solo asegúrate de ampliar el acceso a la tabla de origen del catálogo. Para saber más sobre cómo crear un nuevo principal de servicio y sus credenciales, consulta la página de [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views). 

{:start="3"}
3. Si tienes políticas de red en vigor, debes dar acceso de red a Braze a tu instancia de Microsoft Fabric. Para ver una lista de IP, consulta la [ingesta de datos en la nube]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab S3 %}
Configura tus archivos fuente en S3 proporcionando archivos JSON o CSV. Ten en cuenta lo siguiente:

- Los archivos no pueden incluir una columna `UPDATED_AT`.  
- Puedes incluir un campo opcional `DELETED` para marcar los elementos que deseas eliminar. 

{% subtabs %}
{% subtab JSON %}
```jsonl
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

Para obtener más información sobre la configuración, consulta [Integraciones de almacenamiento de archivos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/).

{% endtab %}
{% endtabs %}

## Cómo funciona la integración

Cada vez que se ejecuta la sincronización, Braze extrae todas las filas en las que `UPDATED_AT` sea posterior al último valor sincronizado. Las filas que coincidan exactamente con la marca de tiempo del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo. Recomendamos crear una vista en tu almacén de datos a partir de los datos del catálogo para configurar una tabla de origen que se actualice completamente cada vez que se ejecute una sincronización. Con las vistas, no tendrás que reescribir la consulta cada vez.

Por ejemplo, si tienes una tabla de datos de productos (`product_catalog_1`) con `product_id` y tres atributos adicionales, podrías sincronizar la siguiente vista:

{% tabs %}
{% tab Snowflake %}
```sql
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
```sql
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
```sql
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
```sql
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
```sql
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
- Si DELETED está configurado como `true`, se eliminará el elemento de catálogo correspondiente.
- La sincronización no registrará puntos de datos, pero todos los datos sincronizados se contabilizarán en el uso total del catálogo; este uso se mide en función del total de datos almacenados, por lo que no necesitas preocuparte por sincronizar solo los datos modificados.