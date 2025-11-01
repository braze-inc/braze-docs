---
nav_title: Borrar usuarios con CDI
article_title: Borrar usuarios con la ingesta de datos en la nube
page_order: 30
page_type: reference
description: "Este pgae proporciona un resumen del proceso de eliminación de usuarios con la Ingesta de Datos en la Nube."

---

# Borrar usuarios con la ingesta de datos en la nube

> En esta página se explica el proceso de eliminación de usuarios con la Ingesta de Datos en la Nube.

Las sincronizaciones de eliminación de usuarios son compatibles con todos los orígenes de datos disponibles de la Ingesta de Datos en la Nube. 

## Configurar la integración 

Sigue el proceso estándar para [crear una nueva integración en el panel de Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) para el almacén de datos al que quieras conectarte. Asegúrate de incluir un rol que pueda acceder a la tabla de borrado. En la página **Crear sincronización de importación**, establece el **Tipo de datos** en **Eliminar usuarios** para que se realicen las acciones adecuadas durante la ejecución de la integración para eliminar usuarios.

\![]({% image_buster /assets/img/cloud_ingestion/deletion_1.png %})

## Configuración del origen de datos

Las tablas de origen de los borrados de usuarios deben incluir uno o varios tipos de identificador de usuario y una marca de tiempo `UPDATED_AT`. Las columnas de carga útil no son compatibles con los datos de borrado del usuario.

### `UPDATED_AT`

Añade una marca de tiempo `UPDATED_AT` a tu tabla de origen. Esta marca de tiempo indica la hora a la que se actualizó o añadió esta fila a la tabla. Braze sólo sincronizará las filas que se hayan añadido o actualizado desde la última sincronización.

### Columnas identificadoras de usuario

Tu tabla puede contener una o varias columnas de identificador de usuario. Cada fila sólo debe contener un identificador: o bien `external_id`, o bien la combinación de `alias_name` y `alias_label`, o bien `braze_id`. Una tabla de origen puede contener columnas para uno, dos o los tres tipos de identificador.
- `EXTERNAL_ID` - Esto identifica al usuario que quieres actualizar. Debe coincidir con el valor `external_id` utilizado en Braze. 
- `ALIAS_NAME` y `ALIAS_LABEL` \- Estas dos columnas crean un objeto alias de usuario. `alias_name` debe ser un identificador único, y `alias_label` especifica el tipo de alias. Los usuarios pueden tener varios alias con diferentes etiquetas, pero sólo un `alias_name` por `alias_label`.
- `BRAZE_ID` - El identificador de usuario Braze. Lo genera el SDK de Braze y no se pueden crear nuevos usuarios utilizando un ID de Braze a través de la ingesta de datos en la nube. Para crear nuevos usuarios, especifica un ID externo o un alias de usuario. 

{% alert important %}
No incluyas una columna `PAYLOAD` en tu tabla para la eliminación de usuarios. Para evitar la eliminación accidental y permanente de usuarios, la sincronización fallará si se proporciona una columna de carga útil en la tabla de origen. Cualquier otra columna está permitida, pero será ignorada por Braze.
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
Crea una tabla con los siguientes campos:

| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUERIDO |
| `EXTERNAL_ID`| CADENA | NULABLE |
| `ALIAS_NAME`| CADENA | NULABLE |
| `ALIAS_LABEL`| CADENA | NULABLE |
| `BRAZE_ID`| CADENA | NULABLE |
{% endtab %}

{% tab Databricks %}
Crea una tabla con los siguientes campos:

| Nombre del campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUERIDO |
| `EXTERNAL_ID`| CADENA | NULABLE |
| `ALIAS_NAME`| CADENA | NULABLE |
| `ALIAS_LABEL`| CADENA | NULABLE |
| `BRAZE_ID`| CADENA | NULABLE |
{% endtab %}
{% tab Microsoft Fabric %}
```json
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

Con la ingesta de datos en la nube Braze, configuras una integración entre tu instancia de almacén de datos y el espacio de trabajo Braze para sincronizar los datos de forma periódica. Esta sincronización se ejecuta según el calendario que tú establezcas, y cada integración puede tener un calendario diferente. Las sincronizaciones pueden ser tan frecuentes como cada 15 minutos o tan infrecuentes como una vez al mes. Para los clientes que necesiten sincronizaciones con una frecuencia superior a 15 minutos, habla con tu administrador del éxito del cliente, o considera la posibilidad de utilizar llamadas a la API REST para la ingesta de datos en tiempo real.

Cuando se ejecuta una sincronización, Braze se conectará directamente a tu instancia de almacén de datos, recuperará todos los datos nuevos de la tabla especificada y eliminará los perfiles de usuario correspondientes en tu panel Braze. 

{% alert warning %}
La eliminación de perfiles de usuario no se puede deshacer. Eliminará permanentemente a los usuarios que puedan causar discrepancias en tus datos. Consulta [Eliminar un perfil de usuario]({{site.baseurl}}/help/help_articles/api/delete_user/) para más información.
{% endalert %}

<br><br>