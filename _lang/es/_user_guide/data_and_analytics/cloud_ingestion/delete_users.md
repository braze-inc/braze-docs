---
nav_title: Eliminar usuarios con CDI 
article_title: Eliminar usuarios con la ingestión de datos en la nube
page_order: 30
page_type: reference
description: "Este artículo de referencia ofrece una visión general del proceso de eliminación de usuarios con Cloud Data Ingestion."

---

# Borrar usuarios con la ingesta de datos en la nube

Las sincronizaciones de eliminación de usuarios son compatibles con todas las fuentes de datos de Cloud Data Ingestion disponibles. 

## Configuración de la integración 

Siga el proceso estándar para [crear una nueva integración en el cuadro de mandos de Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) para el almacén de datos al que desea conectarse. Asegúrese de incluir un rol que pueda acceder a la tabla de borrado. En la página **Crear sincronización de importación**, establezca el **Tipo de datos** en **Eliminar usuarios**. Esto garantizará que se realicen las acciones adecuadas durante la ejecución de la integración para eliminar usuarios.

![]({% image_buster /assets/img/cloud_ingestion/deletion_1.png %})

## Configuración de los datos de origen 

Las tablas de origen para los borrados de usuarios deben incluir uno o más tipos de identificadores de usuario y una marca de tiempo `UPDATED_AT`. Las columnas de carga útil no son compatibles con los datos de borrado de usuario.

### `UPDATED_AT`

Añade una marca de tiempo `UPDATED_AT` a tu tabla de origen. Esta marca de tiempo indica la hora en que se actualizó o añadió esta fila a la tabla. Braze sólo sincronizará las filas que se hayan añadido o actualizado desde la última sincronización.

### Columnas de identificación de usuarios

Su tabla puede contener una o más columnas de identificadores de usuario. Cada fila sólo debe contener un identificador: `external_id`, la combinación de `alias_name` y `alias_label`, o `braze_id`. Una tabla de origen puede contener columnas para uno, dos o los tres tipos de identificadores.
- `EXTERNAL_ID` - Identifica al usuario que desea actualizar. Esto debería coincidir con el valor `external_id` utilizado en Braze. 
- `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero sólo un `alias_name` por `alias_label`.
- `BRAZE_ID` - El identificador de usuario Braze. Esto lo genera el SDK de Braze y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de Cloud Data Ingestion. Para crear nuevos usuarios, especifique un ID de usuario externo o un alias de usuario. 

{% alert important %}
No incluya una columna `PAYLOAD` en su tabla para la eliminación de usuarios. Para evitar la eliminación accidental y permanente de usuarios, la sincronización fallará si se proporciona una columna de carga útil en la tabla de origen. Cualquier otra columna está permitida, pero será ignorada por Braze.
{% endalert %}

{% tabs %}
{% tab Snowflake %}
```json
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
```json
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
Cree una tabla con los siguientes campos:

| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| MARCA DE TIEMPO | REQUERIDO |
| `EXTERNAL_ID`| CADENA | NULABLE |
| `ALIAS_NAME`| CADENA | NULABLE |
| `ALIAS_LABEL`| CADENA | NULABLE |
| `BRAZE_ID`| CADENA | NULABLE |
{% endtab %}

{% tab Databricks %}
Cree una tabla con los siguientes campos:

| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| MARCA DE TIEMPO | REQUERIDO |
| `EXTERNAL_ID`| CADENA | NULABLE |
| `ALIAS_NAME`| CADENA | NULABLE |
| `ALIAS_LABEL`| CADENA | NULABLE |
| `BRAZE_ID`| CADENA | NULABLE |
{% endtab %}
{% endtabs %}

### Cómo funciona

Con Braze Cloud Data Ingestion, puede configurar una integración entre su instancia de almacén de datos y el espacio de trabajo Braze para sincronizar los datos de forma periódica. Esta sincronización se ejecuta según el calendario que establezcas, y cada integración puede tener un calendario diferente. Las sincronizaciones pueden ser tan frecuentes como cada 15 minutos o tan infrecuentes como una vez al mes. Para los clientes que necesiten sincronizaciones con una frecuencia superior a 15 minutos, hable con su gestor de éxito de clientes o considere la posibilidad de utilizar llamadas a la API REST para la ingestión de datos en tiempo real.

Cuando se ejecuta una sincronización, Braze se conectará directamente a su instancia de almacén de datos, recuperará todos los datos nuevos de la tabla especificada y eliminará los perfiles de usuario correspondientes en su cuadro de mandos Braze. 

{% alert warning %}
La eliminación de perfiles de usuario no se puede deshacer. Eliminará permanentemente los usuarios que puedan causar discrepancias en sus datos. Consulte [Eliminar un perfil de usuario]({{site.baseurl}}/help/help_articles/api/delete_user/) para obtener más información.
{% endalert %}

<br><br>