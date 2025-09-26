---
nav_title: Generador de consultas
article_title: Generador de consultas
page_order: 15
description: "Este artículo de referencia describe cómo crear informes utilizando datos Braze de Snowflake en el Generador de consultas."
tool: Reports
alias: /query_builder/
---

# Generador de consultas

> El Generador de consultas genera informes utilizando datos Braze en Snowflake. El Generador de consultas incluye [plantillas de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) SQL predefinidas para empezar, o bien puede escribir sus propias consultas SQL personalizadas para obtener aún más información.

Dado que el Generador de consultas permite el acceso directo a algunos datos de clientes, solo puedes acceder a él si tienes el [permiso]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "Ver PII".

## Ejecutar informes en el Generador de consultas

Para ejecutar un informe del Generador de consultas:

1. Vaya a **Análisis** > **Generador de consultas**.
2. Seleccione **Crear consulta SQL**. Si necesita inspiración o ayuda para elaborar su consulta, seleccione **Plantilla de consulta** y elija una plantilla de la lista. De lo contrario, seleccione **Editor SQL** para ir directamente al editor.
3. Su informe recibe automáticamente un nombre con la fecha y hora actuales. Pase el ratón por encima del nombre y seleccione <i class="fas fa-pencil" alt="Edit"></i> para dar un nombre significativo a su consulta SQL.
4. Escribe tu consulta SQL en el editor u [obtén ayuda de AI](#ai-query-builder) en la pestaña **Generador de consultas AI**. Si escribe su propio SQL, consulte [Escribir consultas SQL personalizadas](#custom-sql) para conocer los requisitos y los recursos.
5. Seleccione **Ejecutar consulta**.
6. Guarda tu consulta.
7. Para descargar un CSV de su informe, seleccione **Exportar**.

![Generador de consultas que muestra los resultados de la consulta con plantilla "Interacción e ingresos del canal en los últimos 30 días".]({% image_buster /assets/img_archive/query_builder.png %})

Los resultados de cada informe pueden generarse una vez al día. Si ejecuta el mismo informe más de una vez en un día natural, verá los mismos resultados en ambos informes.

### Plantillas de consulta

Accede a las plantillas de consulta seleccionando **Crear consulta SQL** > **Plantilla de consulta** al crear un informe por primera vez.

Consulte [Plantillas de consulta]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) para ver una lista de las plantillas disponibles.

### Plazo de los datos

Todas las consultas muestran datos de los últimos 60 días.

### Zona horaria del Constructor de consultas

La zona horaria predeterminada para consultar nuestra base de datos Snowflake es UTC. Como resultado, puede haber algunas discrepancias de datos entre tu página de **interacción con el canal de correo electrónico** (que sigue la zona horaria de tu empresa) y los resultados de tu Generador de consultas.

Para convertir la zona horaria en los resultados de tu consulta, añade el siguiente SQL a tu consulta y personalízalo para la zona horaria de tu empresa:

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

## Generar SQL con el Generador de consultas con IA

El Generador de consultas con IA aprovecha [la GPT](https://openai.com/gpt-4), impulsada por OpenAI, para recomendar SQL para tu consulta.

![El constructor de consultas SQL AI.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

Generar SQL con el Generador de consultas con IA

1. Tras crear un informe en el Generador de consultas, selecciona la pestaña **Generador de consultas con IA**.
2. Escriba su consulta o seleccione una consulta de ejemplo y seleccione **Generar** para traducir su consulta a SQL.
3. Revise el SQL generado para asegurarse de que parece correcto y, a continuación, seleccione **Insertar en el editor**.

### Consejos

- Familiarícese con las [tablas de datos Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponibles. Pedir datos que no existen en estas tablas puede hacer que ChatGPT invente una tabla falsa.
- Familiarízate con las [reglas de escritura SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) para esta característica. El incumplimiento de estas normas provocará un error.
- Puedes enviar hasta 20 consultas por minuto con el Generador de Consultas con IA.

### ¿Cómo se utilizan y envían mis datos a OpenAI?
<!-- Contact Legal for changes. -->

Para generar tu SQL, Braze enviará tus solicitudes a la Plataforma API de OpenAI. Todas las consultas enviadas a OpenAI desde Braze son anónimas, lo que significa que OpenAI no podrá identificar desde quién se envió la consulta a menos que usted incluya información identificable de forma única en el contenido que proporcione. Como se detalla en [los Compromisos de la Plataforma API de OpenAI](https://openai.com/policies/api-data-usage-policies), los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar o mejorar sus modelos y se eliminarán al cabo de 30 días. Asegúrate de que cumples las políticas de OpenAI relevantes para ti, incluida la [Política de uso](https://openai.com/policies/usage-policies). Braze no ofrece garantías de ningún tipo con respecto a los contenidos generados por IA. 

## Redacción de consultas SQL personalizadas {#custom-sql}

Escriba su consulta SQL utilizando [la sintaxis Snowflake](https://docs.snowflake.com/en/sql-reference). Consulte la [referencia de la tabla]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) para obtener una lista completa de las tablas y columnas disponibles para su consulta.

Para ver los detalles de la tabla en el Generador de consultas:

1. En la página **Generador de consultas**, abra el panel **Referencia** y seleccione **Tablas de datos disponibles** para ver las tablas de datos disponibles y sus nombres.
3. Seleccione <i class="fas fa-chevron-down" alt=""></i> **Ver detalles** para ver la descripción de la tabla e información sobre las columnas de la tabla, como los tipos de datos.
4. Para insertar el nombre de la tabla en su SQL, seleccione <i class="fas fa-copy" title="Copiar nombre de tabla al editor SQL"></i>.

Para utilizar consultas preescritas proporcionadas por Braze, seleccione **Plantilla de consulta** al crear un informe por primera vez en el Generador de consultas.

Restringir su consulta a un periodo de tiempo específico le ayudará a generar resultados más rápidamente. A continuación se muestra un ejemplo de consulta que obtiene el número de compras y los ingresos generados durante la última hora.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Esta consulta recupera el número de envíos de correo electrónico en el último mes:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Si consultas por las columnas `CANVAS_ID`, `CANVAS_VARIATION_API_ID`, o `CAMPAIGN_ID`, sus nombres asociados se incluirán automáticamente en la tabla de resultados. No es necesario que los incluyas en la propia consulta `SELECT`.

| Nombre ID | Columna de nombre asociado |
| --- | --- |
| `CANVAS_ID` | Nombre del Canvas |
| `CANVAS_VARIATION_API_ID` | Nombre de la variante en Canvas |
| `CAMPAIGN_ID` | Nombre de la campaña |
{: .reset-td-br-1 .reset-td-br-2 }

Esta consulta recupera los tres ID y sus columnas de nombre asociadas con un máximo de 100 filas:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### Rellena automáticamente el nombre de la variante de campaña

Si quieres que el nombre de la variante de campaña se rellene automáticamente, incluye el nombre de la columna `MESSAGE_VARIATION_API_ID` en tu consulta, como en este ejemplo:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### Solución de problemas

Su consulta puede fallar por cualquiera de las siguientes razones:

- Errores de sintaxis en la consulta SQL
- Tiempo de espera de procesamiento (después de 6 minutos)
    - Los informes que tarden más de 6 minutos en ejecutarse agotarán el tiempo de espera.
    - Si se agota el tiempo de espera de un informe, intente limitar el intervalo de tiempo en el que consulta los datos o consulte un conjunto de datos más específico.

## Utilización de variables

Utilice variables para utilizar tipos de variables predefinidas en SQL para referenciar valores sin necesidad de copiar manualmente el valor. Por ejemplo, en lugar de copiar manualmente el ID de una campaña en el editor SQL, puede utilizar {% raw %}`{{campaign.${My campaign}}}`{% endraw %} para seleccionar directamente una campaña en un desplegable de la pestaña **Variables**.

Una vez creada una variable, aparecerá en la pestaña **Variables** de su informe del Generador de consultas. Entre las ventajas de utilizar variables SQL se incluyen:

- Ahorre tiempo creando una variable de campaña para seleccionarla de una lista al crear su informe, en lugar de pegar los ID de campaña.
- Intercambie valores añadiendo variables que le permitan reutilizar el informe para casos de uso ligeramente diferentes en el futuro (como un evento personalizado diferente).
- Reduzca los errores del usuario al editar su SQL reduciendo la cantidad de edición necesaria para cada informe. Los compañeros de equipo que se sienten más cómodos con SQL pueden crear informes que los compañeros de equipo menos técnicos pueden utilizar después.

### Directrices

Las variables deben ajustarse a la siguiente sintaxis de Liquid: {% raw %}`{{ type.${name}}}`{% endraw %}, donde `type` debe ser uno de los tipos aceptados y `name` puede ser cualquier cosa que elija. Las etiquetas de estas variables son por defecto el nombre de la variable.

Por defecto, todas las variables son obligatorias (y su informe no se ejecutará a menos que se seleccionen los valores de las variables) excepto el intervalo de fechas, que por defecto es de los últimos 30 días cuando no se proporciona el valor.

### Tipos de variables

Se aceptan los siguientes tipos de variables:

- [Número](#number)
- [Intervalo de fechas](#date-range)
- [Mensajería](#messaging)
- [Productos](#products)
- [Eventos personalizados](#custom-events)
- [Propiedades de los eventos personalizados](#custom-event-properties)
- [Espacio de trabajo](#workspace)
- [Catálogos](#catalogs)
- [Campos del catálogo](#catalog-fields)
- [Opciones](#options)
- [Segmentos](#segments)
- [Cadena](#string)
- [Etiquetas](#tags)

#### Número

- **Valor de sustitución:** El valor proporcionado, como `5.5`
- **Ejemplo de uso:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### Intervalo de fechas

Si utiliza `start_date` y `end_date`, deben tener el mismo nombre para que pueda utilizarlos como intervalo de fechas.

##### Ejemplos de valores

El tipo de intervalo de fechas puede ser relativo, fecha de inicio, fecha final o intervalo de fechas.

Se muestran los cuatro tipos si se utilizan `start_date` y `end_date` con el mismo nombre. Si sólo se utiliza uno, sólo se mostrarán los tipos correspondientes.

| Tipo de intervalo de fechas | Descripción | Valores requeridos |
| --- | --- | --- |
| Relativo | Especifica los últimos X días | Requiere `start_date` |
| Fecha de inicio | Especifica una fecha de inicio | Requiere `start_date` |
| Fecha de finalización | Especifica una fecha final | Requiere `end_date` |
| Intervalo de fechas | Especifica tanto la fecha de inicio como la de finalización | Requiere `start_date` y `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **Valor de sustitución:** Sustituye `start_date` y `end_date` por una marca de tiempo Unix en segundos para una fecha especificada en UTC, como `1696517353`.
- **Ejemplo de uso:** Para todas las variables relativas, fecha de inicio, fecha final y rango de fechas:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - Puede utilizar `start_date` o `end_date` si no desea un intervalo de fechas.

#### Mensajería

Todas las variables de mensajería deben compartir el mismo identificador cuando se desea unir su estado en un grupo.

##### Canvas

Para seleccionar un lienzo. Si comparte el mismo nombre con una campaña, aparecerá un botón de opción en la pestaña **Variables** para seleccionar el lienzo o la campaña.

- **Valor de sustitución:** ID BSON del Canvas
- **Ejemplo de uso:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### Canvas

Para seleccionar varios lienzos. Si comparte el mismo nombre con una campaña, aparecerá un botón de opción en la pestaña **Variables** para seleccionar el lienzo o la campaña.

- **Valor de sustitución:** ID BSON de los Canvas
- **Ejemplo de uso:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campaña

Para seleccionar una campaña. Si comparte el mismo nombre con un lienzo, aparecerá un botón de opción en la pestaña **Variables** para seleccionar el lienzo o la campaña.

- **Valor de sustitución:** ID BSON de la campaña
- **Ejemplo de uso:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### Campañas

Para campañas de selección múltiple. Si comparte el mismo nombre con un lienzo, aparecerá un botón de opción en la pestaña **Variables** para seleccionar el lienzo o la campaña.

- **Valor de sustitución:** ID BSON de las campañas
- **Ejemplo de uso:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Variantes de campaña

Para seleccionar las variantes de campaña que pertenecen a la campaña seleccionada. Debe utilizarse junto con una variable de campaña o campañas.

- **Valor de sustitución:** ID de API de variantes de campaña, cadenas delimitadas por comas como `api-id1, api-id2`.
- **Ejemplo de uso:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Variantes de Canvas

Para seleccionar las variantes del lienzo que pertenecen a un lienzo elegido. Debe utilizarse con una variable Lienzo o Lienzos.

- **Valor de sustitución:** ID de API de las variantes en Canvas, cadenas delimitadas por comas como en `api-id1, api-id2`.
- **Ejemplo de uso:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Paso en Canvas

Para seleccionar un paso del lienzo que pertenezca a un lienzo elegido. Debe utilizarse con una variable Canvas.

- **Valor de sustitución:** ID de API del paso Canvas
- **Ejemplo de uso:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### Pasos en Canvas

Para seleccionar los pasos del lienzo que pertenecen a los lienzos elegidos. Debe utilizarse con una variable Lienzo o Lienzos.

- **Valor de sustitución:** ID de API del paso Canvas
- **Ejemplo de uso:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}
