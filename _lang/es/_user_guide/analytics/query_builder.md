---
nav_title: Generador de consultas
article_title: Generador de consultas
page_order: 15
page_type: reference
description: "Este artículo de referencia describe cómo crear informes utilizando datos Braze de Snowflake en el Generador de consultas."
tool: Reports
---

# Generador de consultas

> El Generador de consultas genera informes utilizando datos Braze en Snowflake. El Generador de consultas incluye [plantillas de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) SQL predefinidas para empezar, o bien puede escribir sus propias consultas SQL personalizadas para obtener aún más información.

Dado que el Generador de consultas permite el acceso directo a algunos datos de clientes, solo puedes acceder a él si tienes el [permiso]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "Ver PII".

## Ejecutar informes en el Generador de consultas

Para ejecutar un informe del Generador de consultas:

1. Vaya a **Análisis** > **Generador de consultas**.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), encontrará **el Generador de consultas** en **Datos**.
{% endalert %}

{:start="2"}
2\. Seleccione **Crear consulta SQL**. Si necesita inspiración o ayuda para elaborar su consulta, seleccione **Plantilla de consulta** y elija una plantilla de la lista. De lo contrario, seleccione **Editor SQL** para ir directamente al editor.
3\. Su informe recibe automáticamente un nombre con la fecha y hora actuales. Pase el ratón por encima del nombre y seleccione <i class="fas fa-pencil" alt="Edit"></i> para dar un nombre significativo a su consulta SQL.
4\. Escribe tu consulta SQL en el editor u [obtén ayuda de AI](#ai-query-builder) en la pestaña **Generador de consultas AI**. Si escribe su propio SQL, consulte [Escribir consultas SQL personalizadas](#custom-sql) para conocer los requisitos y los recursos.
5\. Seleccione **Ejecutar consulta**.
6\. Guarda tu consulta.
7\. Para descargar un CSV de su informe, seleccione **Exportar**.

![Generador de consultas que muestra los resultados de la consulta con plantilla "Interacción e ingresos del canal en los últimos 30 días".]({% image_buster /assets/img_archive/query_builder.png %})

Los resultados de cada informe pueden generarse una vez al día. Si ejecuta el mismo informe más de una vez en un día natural, verá los mismos resultados en ambos informes.

### Plantillas de consulta

Accede a las plantillas de consulta seleccionando **Crear consulta SQL** > **Plantilla de consulta** al crear un informe por primera vez.

Consulte [Plantillas de consulta]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) para ver una lista de las plantillas disponibles.

### Plazo de los datos

Todas las consultas muestran datos de los últimos 60 días. 

## Generar SQL con el Generador de consultas con IA

El Generador de consultas con IA aprovecha [la GPT](https://openai.com/gpt-4), impulsada por OpenAI, para recomendar SQL para tu consulta.

![][2]{: style="max-width:60%;" }

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

### Solución de problemas

Su consulta puede fallar por cualquiera de las siguientes razones:

- Errores de sintaxis en la consulta SQL
- Tiempo de espera de procesamiento (después de 6 minutos)
    - Los informes que tarden más de 6 minutos en ejecutarse agotarán el tiempo de espera.
    - Si se agota el tiempo de espera de un informe, intente limitar el intervalo de tiempo en el que consulta los datos o consulte un conjunto de datos más específico.

## Utilización de variables

Utilice variables para utilizar tipos de variables predefinidas en SQL para referenciar valores sin necesidad de copiar manualmente el valor. Por ejemplo, en lugar de copiar manualmente el ID de una campaña en el editor SQL, puede utilizar {% raw %}`{{campaign.${My campaign}}}`{% endraw %} para seleccionar directamente una campaña en un desplegable de la pestaña **Variables**.

![][3]

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

![][4]{: style="max-width:50%;"}

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

![][5]{: style="max-width:50%;"}

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

#### Productos

Para seleccionar una lista de nombres de productos.

- **Valor de sustitución:** Los nombres de los productos van entre comillas simples y separados por comas, como en `product1, product2`
- **Ejemplo de uso:** {% raw %}`product_id IN ({{products.${product name (optional)}}})`{% endraw %}

#### Eventos personalizados

Para seleccionar una lista de eventos personalizados.

- **Valor de sustitución:** Los nombres de propiedades de eventos personalizados se separan por comas, como en `event1, event2`
- **Ejemplo de uso:** {% raw %}`name = ‘{{custom_events.${event names)}}}’`{% endraw %}

#### Propiedades personalizadas de los eventos

Para seleccionar una lista de nombres de propiedades de eventos personalizados. Debe utilizarse con la variable de eventos personalizados.

- **Valor de sustitución:** Los nombres de propiedades de eventos personalizados se separan por comas, como en `property1, property2`
- **Ejemplo de uso:** {% raw %}`name = ‘{{custom_event_properties.${property names)}}}’`{% endraw %}

#### Espacio de trabajo

Para seleccionar un espacio de trabajo.

- **Valor de sustitución:** ID BSON del espacio de trabajo
- **Ejemplo de uso:** {% raw %}`workspace_id = ‘{{workspace.${app_group_id}}}’`{% endraw %}

#### Catálogos

Para seleccionar catálogos.

- **Valor de sustitución:** ID BSON del catálogo
- **Ejemplo de uso:** {% raw %}`catalog_id = ‘{{catalogs.${catalog}}}’`{% endraw %}

#### Campos del catálogo

Para seleccionar los campos del catálogo. Debe utilizarse con la variable catálogos.

- **Valor de sustitución:** Nombres de los campos del catálogo
- **Ejemplo de uso:** {% raw %}`field_name = '{{catalog_fields.${some name}}}’`{% endraw %}

#### Opciones {#options}

Para seleccionar entre una lista de opciones.

- **Valor de sustitución:** El valor de las opciones seleccionadas
- **Ejemplo de uso:**
    - Para seleccionar desplegable: {% raw %}`{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}
        - `is_multi_select` permite especificar si el usuario final puede seleccionar más de una opción
    - Para el botón de radio: {% raw %}`{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}

#### Segmentos

Para seleccionar segmentos que tengan activado [el seguimiento de Analytics]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/).

- **Valor de sustitución:** El ID analítico del segmento, que corresponde a los ID almacenados en la columna `user_segment_membership_ids` en las tablas en las que esta columna está disponible.
- **Ejemplo de uso:** {% raw %}`{{segments.${analytics_segments}}}`{% endraw %}

#### Cadena

Para cambiar valores de cadenas repetitivas entre ejecuciones de informes. Utilice esta variable para evitar codificar un valor varias veces en su SQL.

- **Valor de sustitución:** La cadena tal cual, sin comillas
- **Ejemplo de uso:** {% raw %}`{{string.${some name}}}`{% endraw %}

#### Etiquetas

Para seleccionar etiquetas para campañas y lienzos.

- **Valor de sustitución:** Campañas y lienzos con identificadores BSON separados por comas y entre comillas que están asociados a las etiquetas seleccionadas
- **Ejemplo de uso:** {% raw %}`{{tags.${some tags}}}`{% endraw %}

### Metadatos variables

Se pueden adjuntar metadatos a una variable para cambiar su comportamiento añadiendo los metadatos con un carácter de tubo ( | ) a continuación del nombre de la variable. El orden de los metadatos es indiferente y puede añadir cualquier número de ellos. Además, todos los tipos de metadatos se pueden utilizar para cualquier variable, excepto los metadatos especiales que son específicos de determinadas variables (se indicará en esos casos). El uso de todos los metadatos es opcional y se utiliza para cambiar el comportamiento de las variables por defecto.

**Ejemplo de uso:** {% raw %}`{{string.${my var}| is_required: ‘false’ | description: ‘My optional string var’}}`{% endraw %}

#### Visible

Para saber si las variables son visibles. Todas las variables son visibles por defecto en la pestaña **Variables**, donde puede introducir valores.

Existen varias variables especiales cuyo valor depende de otra variable, como por ejemplo si otra variable tiene un valor. Estas variables especiales están marcadas como no visibles para que no aparezcan en la pestaña **Variables**.

**Ejemplo de uso:** `visible: ‘false’`

#### Obligatoria

Para saber si las variables son obligatorias por defecto. Un valor vacío para una variable suele conducir a una consulta incorrecta.

**Ejemplo de uso:** `required: ‘false’`

#### Pedido

Para seleccionar la posición de la variable en la pestaña **Variables**.

**Ejemplo de uso:** `order: ‘1’`

#### Incluir comillas simples

Para rodear los valores de una variable con comillas simples.

**Ejemplo de uso:** `include_quotes: ‘true’`

#### Incluir comillas dobles

Para rodear los valores de una variable con comillas dobles.

**Ejemplo de uso:** `include_double_quotes: ‘true’`

#### Selección múltiple

Para saber si el desplegable de selección permite una selección única o múltiple. Por ahora, sólo puede incluir estos metadatos si utiliza la variable [Opciones](#options).

**Ejemplo de uso:** `is_multi_select: ‘true’`

![][7]{: style="max-width:50%;"}

#### Botón de radio

Para mostrar opciones como botones de radio en lugar de un desplegable de selección en la pestaña **Variables**. Puede incluir estos metadatos sólo si utiliza la variable [Opciones](#options).

**Ejemplo de uso:** `is_radio_button: ‘true’`

![][6]{: style="max-width:50%;"}

#### Opciones 

Para proporcionar la lista de opciones seleccionables en forma de etiqueta y valor. La etiqueta es lo que se muestra y el valor es lo que sustituye a la variable cuando se selecciona la opción. Puede incluir estos metadatos sólo si utiliza la variable [Opciones](#options).

**Ejemplo de uso:** `options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'`

#### Marcador de posición

Para especificar el texto del marcador de posición que aparece en el campo de entrada de la variable.

**Ejemplo de uso:** `placeholder: ‘enter some value’`

#### Descripción

Para especificar el texto de descripción que aparece bajo el campo de entrada de la variable.

**Ejemplo de uso:** `description: ‘some description’`

#### Valor predeterminado

Para especificar el valor por defecto de la variable cuando no se especifica ningún valor.

**Ejemplo de uso:** `default_value: ‘5’`

#### Ocultar etiqueta

Para ocultar la etiqueta del nombre de la variable. El nombre de la variable se utiliza como etiqueta por defecto.

**Ejemplo de uso:** `hide_label: ‘true’`

### Variables especiales

Las siguientes variables pueden utilizarse con otras variables:

#### Presencia o ausencia del valor de otra variable

Para saber si el valor de una variable está lleno. Esto es útil para variables opcionales en las que se desea cortocircuitar una condición si no se rellena el valor de una variable.

- **Valor de sustitución:** `true` o `false` en función del valor de la otra variable
- **Ejemplo de uso:** {% raw %}`{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}`{% endraw %}

`type` y `name` se refieren a la variable referenciada. Por ejemplo, para cortocircuitar la siguiente variable opcional: {% raw %}`{{campaigns.${messaging}}` puede utilizar lo siguiente:
`{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: ‘false’}})`{% endraw %}

## Tiempo de espera del informe

Los informes que tarden más de seis minutos en ejecutarse agotarán el tiempo de espera. Si se trata de la primera consulta que ejecutas desde hace tiempo, puede tardar más en procesarse y, por tanto, es más probable que se agote el tiempo de espera. Si esto ocurre, intente ejecutar el informe de nuevo.

Si un informe se agota o presenta errores incluso después de reintentarlo, póngase en contacto con [el servicio de asistencia]({{site.baseurl}}/help/support#braze-support).

## Datos y resultados

Los resultados, y las exportaciones de resultados, son tablas que pueden contener hasta 1.000 filas. Para informes que requieran grandes cantidades de datos, utilice otra herramienta como [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) o [las API de exportación]({{site.baseurl}}/api/endpoints/export) de Braze.

## Control del uso del Generador de consultas

Cada espacio de trabajo Braze dispone de 5 créditos Snowflake al mes. Cada vez que se ejecuta una consulta o se previsualiza una tabla, se utiliza una pequeña parte de un crédito Snowflake.

{% alert note %}
Los créditos copo de nieve no se comparten entre funciones. Por ejemplo, los créditos de las extensiones de segmentos SQL y del Generador de consultas son independientes entre sí.
{% endalert %}

El uso de créditos está correlacionado con el tiempo de ejecución de su consulta SQL. Cuanto mayor sea el tiempo de ejecución, mayor será la parte del crédito Snowflake que costará una consulta. El tiempo de ejecución puede variar en función de la complejidad y el tamaño de las consultas a lo largo del tiempo. Cuanto más complejas y frecuentes sean las consultas, mayor será la asignación de recursos y más rápido el tiempo de ejecución.

Los créditos no se utilizan al escribir, editar o guardar informes dentro del editor Braze SQL. Tus créditos volverán a ser 5 el primer día de cada mes a las 12 am UTC. Puede controlar el uso mensual de su crédito en la parte superior de la página del Generador de consultas.

![Query Builder que muestra la cantidad de créditos utilizados en el mes en curso.][1]{: style="max-width:60%;"}

Cuando alcances el límite de crédito, no podrás ejecutar consultas, pero podrás crear, editar y guardar informes SQL. Si desea adquirir más créditos del Generador de consultas, póngase en contacto con su gestor de cuenta.

[1]: {% image_buster /assets/img_archive/query_builder_credits.png %}
[2]: {% image_buster /assets/img_archive/query_builder_ai_tab.png %}
[3]: {% image_buster /assets/img_archive/sql_variables_panel.png %}
[4]: {% image_buster /assets/img_archive/query_builder_time_range.png %}
[5]: {% image_buster /assets/img_archive/sql_variables_canvases.png %}
[6]: {% image_buster /assets/img_archive/sql_variables_campaigns.png %}
[7]: {% image_buster /assets/img_archive/sql_variables_productname.png %}
