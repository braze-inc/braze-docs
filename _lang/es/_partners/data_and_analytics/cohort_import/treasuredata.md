---
nav_title: Treasure Data
article_title: Importación de cohortes de datos del Tesoro
description: "Este artículo de referencia describe la funcionalidad de importación de cohortes de Treasure Data."
alias: /partners/treasure_data_cohort_import/
page_type: partner
search_tag: Partner

---
# Importación de cohortes de Treasure Data

> Este artículo describe cómo importar cohortes de usuarios de Treasure Data a Braze para que pueda enviar campañas específicas basadas en datos que sólo pueden existir en su almacén.

{% alert important %}
Esta función está actualmente en fase beta. Para más información, ponte en contacto con tus representantes de Treasure Data y Braze.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Treasure Data | Se necesita una cuenta de [Treasure Data](https://www.treasuredata.com/) para beneficiarse de esta asociación. |
| Clave de importación de datos Braze | Esto se puede capturar en el panel Braze desde **Integraciones de socios** > **Socios tecnológicos** y luego seleccionar **Treasure Data**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
| Dirección IP estática de Treasure Data | La dirección IP estática de Treasure Data es el punto de acceso y la fuente del enlace para esta Integración. Para determinar la dirección IP estática, ponte en contacto con tu representante de éxito del cliente de Treasure Data o con el soporte técnico de Treasure Data. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de la importación de datos

### Paso 1: Obtenga su clave de importación de datos Braze

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Treasure Data**. Aquí encontrarás tu punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puede crear una nueva o invalidar una existente.

### Paso 2: Crear una conexión de datos

Antes de crear tu conexión de datos en Treasure Data, tendrás que autenticarte. Primero, selecciona **Centro de integraciones** y, a continuación, **Catálogo**.

![Catálogo de Treasure Data Integrations Hub]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %}) 

Busque la integración Braze en el **catálogo**, pase el ratón por encima del icono y seleccione **Crear autenticación**. Introduzca sus credenciales, asigne un nombre a la autenticación y seleccione **Hecho**.

![Catálogo de Treasure Data Integrations Hub]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %}) 

### Paso 3: Define la audiencia de tu cohorte

Sincronice sus cohortes con Braze mediante una activación en **Audience Studio** o ejecutando una consulta en **Data Workbench**.

{% alert important %}
Sólo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

{% tabs local %}
{% tab Workbench de datos %}
#### Paso 3.1: Define tu consulta

{% alert note %}
Las columnas de consulta deben especificarse con los nombres de columna y el tipo de datos exactos. Las columnas de consulta deben incluir al menos una de las columnas: `user_ids`, `device_ids`, o la columna de alias de soldadura coincide con la configuración en la interfaz de usuario. Sólo se añadirán a una cohorte los perfiles de usuario que existan en Braze. La importación de cohortes no creará nuevos perfiles de usuario.
{% endalert %}

1. Vaya a **Data Workbench** > **Queries**.
2. Seleccione **Nueva consulta**.
3. Ejecute la consulta para validar el conjunto de resultados.

![Catálogo de Treasure Data Integrations Hub]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### Casos de uso: Sincronización de cohortes por identificador

{% subtabs local %}
{% subtab Syncing External IDs %}
Aquí tienes una tabla de ejemplo en Treasure Data:

| external_id |	correo electrónico	| Id_dispositivo |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
El nombre de la columna debe ser `user_ids` o la sincronización fallará.
{% endalert %}

Para sincronizar cohortes utilizando el ID externo, ejecute la siguiente consulta:

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

Tras ejecutar la consulta, estos alias de usuario se añadirán a la cohorte en Braze:

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
Aquí tienes una tabla de ejemplo en Treasure Data:

| external_id |	correo electrónico	| Id_dispositivo |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

Para sincronizar cohortes utilizando el alias de usuario, ejecute la siguiente consulta:

```sql
SELECT
  email
FROM
  example_cohort_table
```

Tras ejecutar la consulta, estos alias de usuario se añadirán a la cohorte en Braze:

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
Aquí tienes una tabla de ejemplo en Treasure Data:

| external_id |	correo electrónico	| Id_dispositivo |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
El nombre de la columna debe ser `device_ids` o la sincronización fallará.
{% endalert %}

Para sincronizar cohortes utilizando el ID de dispositivo, ejecute la siguiente consulta:

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

Tras ejecutar la consulta, estos ID de dispositivo se añadirán a la cohorte en Braze:

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### Paso 3.2: Especifique el destino de la exportación de resultados

Una vez creada la consulta, seleccione **Exportar resultados**. Puede seleccionar una autenticación existente, como la creada en los últimos pasos, o crear una nueva autenticación que se utilizará para la salida. 

![Catálogo de Treasure Data Integrations Hub]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %}) 


| Asignación de resultados de exportación |	Descripción	| 
| ----------- | ----------- |
| ID de cohorte	| Este es el identificador de cohorte backend que se enviará a Braze. 	|
| Nombre de la cohorte (opcional)	| Este es el nombre que aparecerá dentro del Filtro de cohortes en la herramienta de segmentación Braze. Si no se configura, se utilizará `Cohort ID` como `Cohort Name`.	|
| Operación	| Se utiliza para determinar si la consulta debe añadir o eliminar perfiles de la cohorte en Braze.	| 
| Alias (opcional) | Cuando se define, el nombre de la columna correspondiente dentro de su consulta se enviará como `alias_label`, y los valores de cada fila de la columna se enviarán como `alias_name`.	| 
| Número de hilos | Número de llamadas concurrentes a la API. |

Sigue [los pasos de Treasure Data](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget) para configurar tu exportación según tu caso de uso.

#### Paso 3.3: Ejecutar la consulta

Guarde la consulta con un nombre y ejecútela, o simplemente ejecútela. Una vez completada con éxito la consulta, el resultado de la misma se exporta automáticamente a Braze.

{% endtab %}
{% tab Estudio de audiencia %}
#### Paso 3.1: Crear una activación

Cree un nuevo segmento o elija un segmento existente para sincronizarlo con Braze como cohorte. Dentro del segmento, seleccione **Crear activación**.

#### Paso 3.2: Rellena tus datos de activación

![Detalles de activación de las integraciones de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %}) 

| Configuración detallada de la activación |	Descripción	| 
| ----------- | ----------- |
| Nombre de activación	| El nombre de su activación.	|
| Descripción de la activación| Breve descripción de la activación.	|
| Autenticación	| Elija la autenticación de cohorte Braze creada en el paso 2.	| 
| ID de cohorte	| Este es el identificador de cohorte backend que se enviará a Braze. 	|
| Nombre de la cohorte (opcional)	| Este es el nombre que aparecerá dentro del Filtro de cohortes en la herramienta de segmentación Braze. Si no se configura, se utilizará `Cohort ID` como `Cohort Name`.	|
| Operación	| Se utiliza para determinar si la consulta debe añadir o eliminar perfiles de la cohorte en Braze.	| 
| Alias (opcional) | Cuando se define, el nombre de la columna correspondiente dentro de su consulta se enviará como `alias_label`, y los valores de cada fila de la columna se enviarán como `alias_name`.	| 
| Número de hilos | Número de llamadas concurrentes a la API. |

#### Paso 3.3: Configurar la asignación de salidas

![Activación de la integración de datos de Treasure Data Mapeado de salida]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %}) 

| Asignación de salida de activación |	Descripción	| 
| ----------- | ----------- |
| Columnas de atributos	| Determine las columnas de su base de datos de segmentos que se asignarán como identificadores al sincronizar perfiles con una cohorte Braze.	|
| Creador de cadenas| El constructor de cadenas no es necesario para la integración Braze.	|

{% alert important %}
 - Si se utiliza `device_id` como identificador, el **nombre de la columna de salida** debe ser `device_ids`.
 - Cuando utilice alias como identificador, el **Nombre de columna de salida** debe ser el nombre de la columna correspondiente dentro de su consulta se enviará como `alias_label`, y los valores de cada fila de la columna se enviarán como `alias_name`.
 - Si se utiliza `external_id` como identificador, el **nombre de la columna de salida** debe ser `user_ids`.
{% endalert %}

Se ignorarán todos los nombres de columnas no relevantes o con nombres erróneos. Puedes elegir utilizar más de un identificador en tus sincronizaciones.

#### Paso 3.4: Define tu calendario de activación

Defina el calendario de sincronización que desee y guarde la activación.

![Calendario de activación de las integraciones de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### Paso 4: Crear un segmento Braze a partir de la exportación de datos del Tesoro

En Braze, vaya a **Segmentos**, cree un nuevo segmento y seleccione **Cohortes de datos de tesorería** como filtro. Desde aquí, puedes elegir qué cohorte de Treasure Data deseas incluir. Una vez creado su segmento de cohorte de Treasure Data, puede seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

![Catálogo de Treasure Data Integrations Hub]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %}) 

## Coincidencia de usuarios

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden ser emparejados por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.
