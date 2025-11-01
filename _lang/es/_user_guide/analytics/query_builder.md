---
nav_title: Generador de consultas
article_title: Generador de consultas
page_order: 15
description: "Este artículo de referencia describe cómo crear informes utilizando datos Braze de Snowflake en el Generador de consultas."
tool: Reports
alias: /query_builder/
---

# Generador de consultas

> El Generador de consultas genera informes utilizando datos de Braze en Snowflake. El Generador de consultas incluye [plantillas de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) SQL predefinidas para que puedas empezar, o puedes escribir tus propias consultas SQL personalizadas para obtener aún más información.

Como el Generador de consultas permite el acceso directo a algunos datos de clientes, sólo puedes acceder a él si tienes el permiso "Ver PII".

## Ejecutar informes en el Generador de consultas

Para ejecutar un informe del Generador de informes:

1. Ve a **Análisis** > **Generador de consultas**.
2. Selecciona **Crear consulta SQL**. Si necesitas inspiración o ayuda para elaborar tu consulta, selecciona **Plantilla de consulta** y elige una plantilla de la lista. Si no, selecciona **Editor SQL** para ir directamente al editor.
3. Tu informe recibe automáticamente un nombre con la fecha y hora actuales. Pasa el ratón por encima del nombre y selecciona <i class="fas fa-pencil" alt="Edit"></i> para dar un nombre significativo a tu consulta SQL.
4. Escribe tu consulta SQL en el editor u [obtén ayuda de AI](#ai-query-builder) en la pestaña **Generador de consultas AI**. Si escribes tu propio SQL, consulta [Escribir consultas SQL personalizadas](#custom-sql) para conocer los requisitos y recursos.
5. Selecciona **Ejecutar consulta**.
6. Guarda tu consulta.
7. Para descargar un CSV de tu informe, selecciona **Exportar**.

\![Generador de consultas que muestra los resultados de la consulta con plantilla "Interacción e ingresos del canal en los últimos 30 días".]({% image_buster /assets/img_archive/query_builder.png %})

Los resultados de cada informe pueden generarse una vez al día. Si ejecutas el mismo informe más de una vez en un día natural, verás los mismos resultados en ambos informes.

### Plantillas de consulta

Accede a las plantillas de consulta seleccionando **Crear consulta SQL** > **Plantilla de consulta** al crear un informe por primera vez.

Consulta [Plantillas de consulta]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) para ver una lista de las plantillas disponibles.

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

### Historial de consultas

La sección **Historial de consultas** del Generador de consultas muestra tus consultas ejecutadas anteriormente para ayudarte a hacer un seguimiento y reutilizar tu trabajo. El historial de consultas se conserva durante siete días, lo que significa que las consultas con más de siete días de antigüedad se eliminan automáticamente.

Si necesitas auditar el uso de las consultas durante periodos más largos o mantener registros de más de siete días, te recomendamos exportar o guardar los resultados de consultas importantes antes de que caduquen.

## Generar SQL con el Generador de consultas AI

El Generador de consultas de IA aprovecha [la GPT](https://openai.com/gpt-4), impulsada por OpenAI, para recomendar SQL para tu consulta.

El generador de consultas SQL AI.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

Para generar SQL con el Generador de consultas AI:

1. Después de crear un informe en el Generador de consultas, selecciona la pestaña **AI Generador de consultas**.
2. Escribe tu consulta o selecciona una consulta de ejemplo y selecciona **Generar** para traducir tu consulta a SQL.
3. Revisa el SQL generado para asegurarte de que parece correcto y, a continuación, selecciona **Insertar en el editor**.

### Consejos

- Familiarízate con las [tablas de datos Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponibles. Pedir datos que no existen en estas tablas puede hacer que ChatGPT invente una tabla falsa.
- Familiarízate con las [reglas de escritura SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) para esta característica. No seguir estas reglas provocará un error.
- Puedes enviar hasta 20 consultas por minuto con el Generador de Consultas AI.

### ¿Cómo se utilizan y envían mis datos a OpenAI?
<!-- Contact Legal for changes. -->

Para generar tu SQL, Braze enviará tus peticiones a la Plataforma API de OpenAI. Todas las consultas enviadas a OpenAI desde Braze son anónimas, lo que significa que OpenAI no podrá identificar desde quién se envió la consulta a menos que incluyas información identificadora única en el contenido que proporciones. Como se detalla en [los Compromisos de la Plataforma API de Open](https://openai.com/policies/api-data-usage-policies)AI, los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar o mejorar sus modelos y se eliminarán al cabo de 30 días. Asegúrate de que cumples las políticas de OpenAI relevantes para ti, incluida la [Política de uso](https://openai.com/policies/usage-policies). Braze no ofrece garantías de ningún tipo con respecto a cualquier contenido generado por IA. 

## Escribir consultas SQL personalizadas {#custom-sql}

Escribe tu consulta SQL utilizando [la sintaxis Snowflake](https://docs.snowflake.com/en/sql-reference). Consulta la [referencia de la tabla]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) para obtener una lista completa de las tablas y columnas disponibles para ser consultadas.

Para ver los detalles de la tabla en el Generador de consultas:

1. En la página **Generador de consultas**, abre el panel **Referencia** y selecciona **Tablas de datos disponibles** para ver las tablas de datos disponibles y sus nombres.
3. Selecciona <i class="fas fa-chevron-down" alt=""></i> **Ver detalles** para ver la descripción de la tabla e información sobre las columnas de la tabla, como los tipos de datos.
4. Para insertar el nombre de la tabla en tu SQL, selecciona <i class="fas fa-copy" title="Copiar nombre de tabla al editor SQL"></i>.

Para utilizar consultas preescritas proporcionadas por Braze, selecciona **Plantilla de consulta** al crear un informe por primera vez en el Generador de informes.

Restringir tu consulta a un periodo de tiempo concreto te ayudará a generar resultados más rápidamente. A continuación se muestra una consulta de ejemplo que obtiene el número de compras y los ingresos generados en la última hora.

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

Tu consulta puede fallar por alguna de las siguientes razones:

- Errores de sintaxis en tu consulta SQL
- Tiempo de espera de procesamiento (tras 6 minutos)
    - Los informes que tarden más de 6 minutos en ejecutarse agotarán el tiempo de espera.
    - Si se agota el tiempo de espera de un informe, intenta limitar el intervalo de tiempo en el que estás consultando datos o consulta un conjunto de datos más específico.

## Utilizar variables

Utiliza variables para utilizar tipos de variables predefinidos en SQL para referenciar valores sin necesidad de copiar manualmente el valor. Por ejemplo, en lugar de copiar manualmente el ID de una campaña en el editor SQL, puedes utilizar {% raw %}`{{campaign.${My campaign}}}`{% endraw %} para seleccionar directamente una campaña en un desplegable de la pestaña **Variables**.

Una vez creada una variable, aparecerá en la pestaña **Variables** de tu informe del Generador de informes. Las ventajas de utilizar variables SQL son

- Ahorra tiempo creando una variable de campaña para seleccionarla de una lista al crear tu informe, en lugar de pegar los ID de campaña.
- Intercambia valores añadiendo variables que te permitan reutilizar el informe para casos de uso ligeramente distintos en el futuro (como un evento personalizado diferente).
- Reduce los errores del usuario al editar tu SQL reduciendo la cantidad de edición necesaria para cada informe. Los compañeros que se sientan más cómodos con SQL pueden crear informes que los compañeros menos técnicos podrán utilizar después.

### Directrices

Las variables deben ajustarse a la siguiente sintaxis Liquid: {% raw %}`{{ type.${name}}}`{% endraw %}, donde `type` debe ser uno de los tipos aceptados y `name` puede ser cualquier cosa que elijas. Las etiquetas de estas variables están predeterminadas al nombre de la variable.

Por defecto, todas las variables son obligatorias (y tu informe no se ejecutará a menos que se seleccionen los valores de las variables) excepto el intervalo de fechas, que por defecto es de los últimos 30 días cuando no se proporciona el valor.

### Tipos de variables

Se aceptan los siguientes tipos de variables:

- [Número](#number)
- [Rango de fechas](#date-range)
- [Mensajería](#messaging)
- [Productos](#products)
- [Eventos personalizados](#custom-events)
- [Propiedades del evento personalizadas](#custom-event-properties)
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

#### Rango de fechas

Si utilizas `start_date` y `end_date`, deben tener el mismo nombre para que puedas utilizarlos como intervalo de fechas.

##### Ejemplos de valores

El tipo de intervalo de fechas puede ser relativo, fecha de inicio, fecha final o intervalo de fechas.

Se muestran los cuatro tipos si se utilizan `start_date` y `end_date` con el mismo nombre. Si sólo se utiliza uno, sólo se mostrarán los tipos correspondientes.

| Tipo de intervalo de fechas | Descripción | Valores requeridos |
| --- | --- | --- |
| Relativa | Especifica los últimos X días | Requiere `start_date` |
| Fecha de inicio | Especifica una fecha de inicio | Requiere `start_date` |
| Fecha de extremo a extremo | Especifica una fecha de finalización | Requiere `end_date` |
| Rango de fechas | Especifica una fecha de inicio y otra de fin | Requiere tanto `start_date` como `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **Valor de sustitución:** Sustituye `start_date` y `end_date` por una marca de tiempo Unix en segundos para una fecha especificada en UTC, como `1696517353`.
- **Ejemplo de uso:** Para todas las variables relativas, fecha de inicio, fecha final y rango de fechas:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - Puedes utilizar `start_date` o `end_date` si no quieres un intervalo de fechas.

#### Mensajería

Todas las variables de mensajería deben compartir el mismo identificador cuando quieras unir su estado en un grupo.

##### Canvas

Para seleccionar un Canvas. Si compartes el mismo nombre con una campaña, aparecerá un botón de opción en la pestaña **Variables** para seleccionar entre Canvas o campaña.

- **Valor de sustitución:** Canvas BSON ID
- **Ejemplo de uso:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### Lienzos

Para seleccionar varios Lienzos. Si compartes el mismo nombre con una campaña, aparecerá un botón de opción dentro de la pestaña **Variables** para seleccionar entre Canvas o campaña.

- **Valor de sustitución:** Lienzos BSON ID
- **Ejemplo de uso:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campaña

Para seleccionar una campaña. Si compartes el mismo nombre con un Canvas, aparecerá un botón de opción en la pestaña **Variables** para seleccionar entre Canvas o campaña.

- **Valor de sustitución:** ID BSON de la campaña
- **Ejemplo de uso:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### Campañas

Para campañas de selección múltiple. Si compartes el mismo nombre con un Canvas, aparecerá un botón de opción en la pestaña **Variables** para seleccionar entre Canvas o campaña.

- **Valor de sustitución:** ID BSON de las campañas
- **Ejemplo de uso:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Variantes de campaña

Para seleccionar las variantes de campaña que pertenecen a la campaña seleccionada. Debe utilizarse junto con una variable de campaña o campañas.

- **Valor de sustitución:** ID de API de variantes de campaña, cadenas delimitadas por comas como `api-id1, api-id2`.
- **Ejemplo de uso:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Variantes en Canvas

Para seleccionar variantes en Canvas que pertenezcan a un Canvas elegido. Debe utilizarse con una variable Canvas o Lienzos.

- **Valor de sustitución:** ID de API de las variantes en Canvas, cadenas delimitadas por comas como en `api-id1, api-id2`.
- **Ejemplo de uso:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Paso en Canvas

Para seleccionar un paso en Canvas que pertenezca a un Canvas elegido. Debe utilizarse con una variable Canvas.

- **Valor de sustitución:** ID de la API del paso en Canvas
- **Ejemplo de uso:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### Pasos en Canvas

Para seleccionar los pasos en Canvas que pertenecen a los Lienzos elegidos. Debe utilizarse con una variable Canvas o Lienzos.

- **Valor de sustitución:** Pasos en Canvas ID de API
- **Ejemplo de uso:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}
