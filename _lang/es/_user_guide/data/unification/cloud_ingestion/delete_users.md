---
nav_title: Eliminar usuarios con CDI
article_title: Eliminar usuarios con la ingesta de datos en la nube
page_order: 30
page_type: reference
description: "Esta página ofrece un resumen del proceso para eliminar usuarios con la ingesta de datos en la nube."

---

# Eliminar usuarios con la ingesta de datos en la nube

> En esta página se explica el proceso de eliminación de usuarios con la ingesta de datos en la nube.

Las sincronizaciones de eliminación de usuarios son compatibles con todos los orígenes de datos disponibles de Cloud Data Ingestion. 

## Configurar la integración 

Sigue el proceso estándar para [crear una nueva integración en el panel de Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) para el almacén de datos al que quieras conectarte. Asegúrate de incluir un rol que pueda acceder a la tabla de eliminación. En la página **Crear sincronización de importación**, configura el **Tipo de datos** en **Eliminar usuarios** para que se realicen las acciones adecuadas durante la ejecución de la integración para eliminar usuarios.

![]({% image_buster /assets/img/cloud_ingestion/deletion_1.png %})

## Configuración del origen de datos

Las tablas de origen para las eliminaciones de usuarios deben incluir uno o más tipos de identificadores de usuario y una marca de tiempo `UPDATED_AT`. Las columnas de carga útil no son compatibles con los datos de eliminación de usuarios.

### `UPDATED_AT`

Añade una marca de tiempo `UPDATED_AT` a tu tabla de origen. Esta marca de tiempo indica la hora en que se actualizó o añadió esta fila a la tabla. Braze sincroniza las filas en las que `UPDATED_AT` es posterior al último valor sincronizado. Las filas que coincidan exactamente con la marca de tiempo del límite pueden volver a sincronizarse si nuevas filas comparten esa misma marca de tiempo.

### Columnas de identificación de usuarios

Tu tabla puede contener una o más columnas de identificadores de usuario. Cada fila solo debe contener un identificador: `external_id`, la combinación de `alias_name` y `alias_label`, o `braze_id`. Una tabla de origen puede contener columnas para uno, dos o los tres tipos de identificadores.
- `EXTERNAL_ID` - Identifica al usuario que deseas actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
- `ALIAS_NAME` y `ALIAS_LABEL` - Estas dos columnas crean un objeto de alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.
- `BRAZE_ID` - El identificador de usuario de Braze. Lo genera el SDK de Braze y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de Cloud Data Ingestion. Para crear nuevos usuarios, especifica un ID de usuario externo o un alias de usuario. 

{% alert important %}
No incluyas una columna `PAYLOAD` en tu tabla para la eliminación de usuarios. Para evitar la eliminación accidental y permanente de usuarios, la sincronización fallará si se proporciona una columna de carga útil en la tabla de origen. Cualquier otra columna está permitida, pero Braze la ignorará.
{% endalert %}

{% tabs %}
{% tab Snowflake %}
```sql
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216)
);
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar
);
```
{% endtab %}

{% tab BigQuery %}
Crea una tabla con los siguientes campos:

| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
{% endtab %}

{% tab Databricks %}
Crea una tabla con los siguientes campos:

| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE OR ALTER TABLE [warehouse].[schema].[users_deletes] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
)
GO
```
{% endtab %}

{% endtabs %}

### Cómo funciona

Con la ingesta de datos en la nube de Braze, configuras una integración entre tu instancia de almacén de datos y el espacio de trabajo de Braze para sincronizar datos de forma periódica. Esta sincronización se ejecuta según la planificación que establezcas, y cada integración puede tener una planificación diferente. Las sincronizaciones pueden ejecutarse con una frecuencia de cada 15 minutos o tan esporádicamente como una vez al mes. Si necesitas sincronizaciones con una frecuencia superior a 15 minutos, habla con tu administrador del éxito del cliente o considera la posibilidad de utilizar llamadas a la API REST para la ingesta de datos en tiempo real.

Cuando se ejecuta una sincronización, Braze se conecta directamente a tu instancia de almacén de datos, recupera todos los datos nuevos de la tabla especificada y elimina los perfiles de usuario correspondientes en tu panel de Braze. 

{% alert warning %}
La eliminación de perfiles de usuario no se puede deshacer. Eliminará permanentemente a los usuarios, lo que puede causar discrepancias en tus datos. Consulta [eliminar un perfil de usuario]({{site.baseurl}}/help/help_articles/api/delete_user/) para obtener más información.
{% endalert %}

<br><br>