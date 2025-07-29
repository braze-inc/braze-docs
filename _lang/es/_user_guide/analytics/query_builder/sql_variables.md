---
nav_title: Variables SQL
article_title: Generador de consultas Variables SQL
page_order: 2
page_type: reference
description: "Aprende a utilizar variables en el Generador de consultas, para que puedas reutilizar tus consultas y evitar codificar datos en tu código."
tool: Reports
---

# Generador de consultas Variables SQL

> Aprende a utilizar variables SQL en el Generador de consultas, para que puedas reutilizar tus consultas y evitar codificar datos en tu código.

## ¿Por qué utilizar variables SQL?

Las ventajas de utilizar variables SQL son

- Ahorre tiempo creando una variable de campaña para seleccionarla de una lista al crear su informe, en lugar de pegar los ID de campaña.
- Intercambie valores añadiendo variables que le permitan reutilizar el informe para casos de uso ligeramente diferentes en el futuro (como un evento personalizado diferente).
- Reduzca los errores del usuario al editar su SQL reduciendo la cantidad de edición necesaria para cada informe. Los compañeros de equipo que se sienten más cómodos con SQL pueden crear informes que los compañeros de equipo menos técnicos pueden utilizar después.

## Utilización de variables

### Paso 1: Añade una variable

Para añadir una variable a tu consulta, utiliza la siguiente sintaxis:

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

Sustituye lo siguiente:

| Marcador de posición      | Descripción                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | El tipo de variable predefinida que quieras utilizar, como `campaign` o `catalog_fields`. Para ver la lista completa, consulta [Tipos de variables admitidos](#variable-types). |
| `custom_label` | La etiqueta utilizada para identificar la variable en la pestaña **Variables** de tu Generador de consultas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

En el siguiente ejemplo, se consulta el número total de usuarios entre el primer y el último día de un mes para una campaña. A cada variable se le asignará un valor en el paso siguiente.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### Paso 2: Asignar un valor

Por predeterminado, la pestaña **Variables** no se muestra en el Generador de consultas. Sólo aparece después de añadir tu primera variable a la consulta. Allí podrás asignarle un valor. Los valores concretos que puedes elegir dependerán del [tipo](#variable-types) específico de esa variable.

En el siguiente ejemplo, se asigna un valor a la campaña "Lanzamiento de características en verano", junto con el primer y el último día de junio de 2025.

![La pestaña "Variable" del Generador de consultas muestra el ejemplo dado.]({% image_buster /assets/img/query_builder_example.png %})

## Tipos de variables generales {#variable-types}

### Número

`number` puede utilizarse en combinación con otras variables que no sean cadenas. Acepta cualquier número positivo o negativo, incluidos los decimales, como `5.5`.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Cadena

Para cambiar valores de cadenas repetitivas entre ejecuciones de informes. Utilice esta variable para evitar codificar un valor varias veces en su SQL.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Lista {#list}

Para seleccionar entre una lista de opciones.

{% tabs local %}
{% tab elige uno %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab elige varios %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Botón de radio

Para mostrar opciones como botones de radio en lugar de un desplegable de selección en la pestaña **Variables**. No se puede utilizar solo, sino en combinación con una [lista](#list).

{% tabs %}
{% tab uso %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Un botón de radio de ejemplo renderizado en Braze.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### Selección múltiple

Para saber si el desplegable de selección permite una selección única o múltiple. No se puede utilizar solo, sino en combinación con una [lista](#list).

{% tabs %}
{% tab uso %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![Un ejemplo de lista de selección múltiple renderizada en Braze.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### Opciones 

Para proporcionar la lista de opciones seleccionables en forma de etiqueta y valor. La etiqueta es lo que se muestra y el valor es lo que sustituye a la variable cuando se selecciona la opción. No se puede utilizar solo, sino en combinación con una [lista](#list).

{% tabs %}
{% tab uso %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Tipos de variables específicas de Braze

### Intervalo de fechas

Para mostrar un calendario en el que seleccionar fechas. Sustituye `start_date` y `end_date` por una marca de tiempo Unix en segundos para una fecha especificada en UTC, como `1696517353`. Opcionalmente, puedes configurar sólo una `start_date` o `end_date` para mostrar sólo una fecha en el calendario. Si las etiquetas de tus `start_date` y `end_date` no coinciden, se tratarán como dos fechas distintas, en lugar de como un intervalo de fechas.

{% tabs %}
{% tab uso %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

Puedes establecer el intervalo de fechas en cualquiera de las siguientes opciones. Si se utilizan tanto `start_date` como `end_date` y comparten la misma etiqueta, se mostrarán todas las opciones. De lo contrario, si sólo se utiliza una, sólo se mostrará la opción especificada.

| Opción | Descripción | Valores requeridos |
| --- | --- | --- |
| Relativo | Especifica los últimos X días | Requiere `start_date` |
| Fecha de inicio | Especifica una fecha de inicio | Requiere `start_date` |
| Fecha de finalización | Especifica una fecha final | Requiere `end_date` |
| Intervalo de fechas | Especifica tanto la fecha de inicio como la de finalización | Requiere `start_date` y `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Tu Liquid se utilizará para mostrar un calendario dentro del intervalo de fechas indicado:

![Un ejemplo de calendario renderizado en Braze.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Campañas

{% tabs local %}
{% tab una campaña %}
Para seleccionar una campaña. Si compartes la misma etiqueta con un Canvas, aparecerá un botón de opción en la pestaña **Variables** para seleccionar entre Canvas o campaña.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab múltiples campañas %}
Para campañas de selección múltiple. Si compartes la misma etiqueta con un Canvas, aparecerá un botón de opción en la pestaña **Variables** para seleccionar entre Canvas o campaña.

- **Valor de sustitución:** ID BSON de las campañas

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab variantes de campaña %}
Para seleccionar las variantes de campaña que pertenecen a la campaña seleccionada. Debe utilizarse junto con una variable de campaña o campañas.

- **Valor de sustitución:** ID de API de variantes de campaña, cadenas delimitadas por comas como `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Todas las variables de campaña y Canvas deben utilizar los mismos identificadores para sincronizar los estados dentro de un mismo grupo.
{% endalert %}

### Canvas

{% tabs local %}
{% tab un lienzo %}
Para seleccionar un lienzo. Si compartes la misma etiqueta con una campaña, aparecerá un botón de opción en la pestaña **Variables** para seleccionar entre Canvas o campaña.

- **Valor de sustitución:** ID BSON del Canvas

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab múltiples lienzos %}
Para seleccionar varios lienzos. Si compartes la misma etiqueta con una campaña, aparecerá un botón de opción dentro de la pestaña **Variables** para seleccionar entre Canvas o campaña.

- **Valor de sustitución:** ID BSON de los Canvas

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab variantes en Canvas %}
Para seleccionar las variantes del lienzo que pertenecen a un lienzo elegido. Debe utilizarse con una variable Lienzo o Lienzos. Establece uno o más ID de API de variantes en Canvas, como una cadena separada por comas, como en `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab un paso en Canvas %}
Para seleccionar un paso del lienzo que pertenezca a un lienzo elegido. Debe utilizarse con una variable Canvas.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab múltiples pasos en Canvas %}
Para seleccionar los pasos del lienzo que pertenecen a los lienzos elegidos. Debe utilizarse con una variable Lienzo o Lienzos.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Todas las variables de campaña y Canvas deben utilizar los mismos identificadores para sincronizar los estados dentro de un mismo grupo.
{% endalert %}

### Productos

`products` se utiliza para seleccionar uno o varios productos del panel de Braze.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab ejemplo %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Eventos personalizados

Selecciona uno o varios eventos personalizados o propiedades del evento personalizadas de una lista.

{% tabs local %}
{% tab evento %}
`custom_events` se utiliza para seleccionar uno o varios eventos personalizados del panel de Braze.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab example %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name = '{{custom_events.${Purchased Game}}}';
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab propiedades %}
`custom_event_properties` se utiliza para seleccionar una o más propiedades del evento personalizado seleccionado actualmente.  Requiere una variable de configuración `custom_events`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Espacio de trabajo

`workspace` se utiliza para seleccionar un único espacio de trabajo del panel Braze.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Catálogos

Selecciona uno o varios catologs o campos de catologs de una lista.

{% tabs local %}
{% tab catálogos %}
`catalogs` se utiliza para seleccionar uno o varios catálogos del panel de Braze.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab campos del católogo %}
`catalog_fields` se utiliza para configurar uno o varios campos del catálogo seleccionado actualmente. Requiere una variable de configuración `catalogs`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Segmentos

Para seleccionar segmentos que tengan activado [el seguimiento de Analytics]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/). Ajústalo al ID de análisis del segmento, que corresponde a los ID almacenados en la columna `user_segment_membership_ids` en las tablas en las que esta columna está disponible.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Etiquetas

Para seleccionar etiquetas para campañas y lienzos. Establece en Campañas y Lienzos los ID de BSON separados por comas que están asociados a las etiquetas seleccionadas.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Metadatos variables

Se pueden adjuntar metadatos a una variable para cambiar su comportamiento, añadiendo los metadatos con un carácter pipa ( | ) a continuación de la etiqueta de la variable. El orden de los metadatos no importa y puedes añadir cualquier número de ellos. Además, todos los tipos de metadatos se pueden utilizar para cualquier variable, excepto los metadatos especiales que son específicos de determinadas variables (se indicará en esos casos). El uso de todos los metadatos es opcional y se utiliza para cambiar el comportamiento de las variables predeterminadas.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Booleano

Para saber si el valor de una variable está lleno. Esto es útil para variables opcionales en las que quieras cortocircuitar una condición si no se rellena el valor de una variable. Puede ajustarse a `true` o `false` en función del valor de la otra variable.

{% tabs %}
{% tab uso %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` y `name` se refieren a la variable referenciada. Por ejemplo, para cortocircuitar la siguiente variable opcional: {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### Visible

Para saber si las variables son visibles. Todas las variables son visibles por defecto en la pestaña **Variables**, donde puede introducir valores.

Existen varias variables especiales cuyo valor depende de otra variable, como por ejemplo si otra variable tiene un valor. Estas variables especiales están marcadas como no visibles para que no aparezcan en la pestaña **Variables**.

{% tabs %}
{% tab uso %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### Obligatoria

Para saber si las variables son obligatorias por defecto. Un valor vacío para una variable suele conducir a una consulta incorrecta.

{% tabs %}
{% tab uso %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### Pedido

Para seleccionar la posición de la variable en la pestaña **Variables**.

{% tabs %}
{% tab uso %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### Incluir citas

{% tabs local %}
{% tab comillas simples %}
Para rodear los valores de una variable con comillas simples.

{% subtabs %}
{% subtab usage %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab comillas dobles %}
Para rodear los valores de una variable con comillas dobles.

{% subtabs %}
{% subtab usage %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Marcador de posición

Para especificar el texto del marcador de posición que aparece en el campo de entrada de la variable.

{% tabs %}
{% tab uso %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### Descripción

Para especificar el texto de descripción que aparece bajo el campo de entrada de la variable.

{% tabs %}
{% tab uso %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### Valor predeterminado

Para especificar el valor por defecto de la variable cuando no se especifica ningún valor.

{% tabs %}
{% tab uso %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### Ocultar etiqueta

Para ocultar la etiqueta de la variable.

{% tabs %}
{% tab uso %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}
