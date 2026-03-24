---
nav_title: Eventos personalizados
article_title: Eventos personalizados
page_order: 9
page_type: reference
description: "En este artículo se describen los eventos y propiedades personalizados, la segmentación, el uso, las propiedades de entrada de Canvas, dónde ver los análisis relevantes y mucho más."
search_rank: 2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"} Eventos personalizados

> Este artículo describe los eventos personalizados y sus propiedades, los filtros de segmentación relacionados, las propiedades de entrada en Canvas, los análisis relevantes y mucho más. Para conocer los eventos de Braze en general, consulta [Eventos]({{site.baseurl}}/user_guide/data/custom_data/events/).

Los eventos personalizados son acciones realizadas por tus usuarios o actualizaciones sobre ellos. Cuando se registran eventos personalizados, pueden desencadenar cualquier número y tipo de campañas de seguimiento. A continuación, puedes utilizar [filtros de segmentación](#segmentation-filters) para segmentar a los usuarios en función de lo recientes y frecuentes que hayan sido esos eventos personalizados. Esto hace que los eventos personalizados sean los más adecuados para el seguimiento de interacciones de usuario de alto valor dentro de tu aplicación.

## Casos de uso

Algunos casos habituales de uso de eventos personalizados son:

- Desencadenar una campaña o Canvas basándose en un evento personalizado utilizando [la entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)
- Segmentar a los usuarios por el número de veces que realizaron un evento personalizado, cuándo se produjo el evento por última vez y similares
- Utilizar el dashboard de [análisis de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) para ver un agregado de la frecuencia con la que se ha producido cada evento
- Encontrar análisis adicionales mediante informes de [embudo]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) y [retención]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)
- Aprovechar [las propiedades de entrada persistentes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) para utilizar metadatos de tu evento de cliente para la personalización en tus pasos en Canvas
- Generar análisis más sofisticados con [Currents]({{site.baseurl}}/user_guide/data/braze_currents/)
- Configurar [criterios de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) para definir cuándo los usuarios deben salir de tu Canvas

## Gestión de eventos personalizados

Puedes gestionar, crear o bloquear eventos personalizados en el dashboard yendo a **Configuración de datos** > **Eventos personalizados**.

Selecciona el menú situado junto a un evento personalizado para realizar las siguientes acciones:

### Añadir a la lista de bloqueo

Puedes bloquear eventos personalizados individuales a través del menú de acciones, o seleccionar y bloquear hasta 100 eventos de forma masiva. 

Cuando bloqueas un evento personalizado:

- No se recogerán datos futuros para ese evento.
- Los datos existentes no estarán disponibles a menos que se desbloquee ese evento.
- Ese evento no aparecerá en los filtros ni en los gráficos.

Además, si un evento personalizado bloqueado es referenciado actualmente por filtros o desencadenantes en otras áreas de Braze, aparecerá un modal de advertencia explicando que todas las instancias de los filtros o desencadenantes que lo referencian serán eliminadas y archivadas.

### Añadir descripciones

Puedes añadir una descripción a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Selecciona **Editar descripción** para el evento personalizado e introduce lo que desees, como una nota para tu equipo.

## Añadir etiquetas

Puedes añadir etiquetas a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "Gestionar eventos, atributos, compras". Las etiquetas pueden utilizarse para filtrar la lista de eventos.

### Ver informes de uso

El informe de uso enumera todos los Canvas, campañas y segmentos que utilizan un evento personalizado específico. La lista no incluye los usos de Liquid. 

Puedes ver hasta 100 informes de uso a la vez seleccionando las casillas de verificación de varios eventos personalizados y, a continuación, seleccionando **Ver informe de uso**.

## Exportar datos

Para exportar la lista de eventos personalizados como un archivo CSV, selecciona el botón **Exportar todo** en la parte superior de la página. Se generará el archivo CSV y se te enviará por correo electrónico un enlace de descarga.

## Registro de eventos personalizados

Los eventos personalizados requieren una configuración adicional. Consulta la lista siguiente para obtener documentación sobre cada plataforma, donde encontrarás información sobre los métodos utilizados para registrar eventos personalizados y sobre cómo añadir propiedades y cantidades a tus eventos personalizados.

{% details Ampliar para ver la documentación por plataforma %}

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=unity)
- [.NET MAUI (antes Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Almacenamiento de eventos personalizados

Todos los datos almacenados en el **perfil de usuario**, incluidos los metadatos de eventos personalizados (primera o última aparición, recuento total y X en Y a lo largo de 30 días), se conservan indefinidamente mientras cada perfil esté [activo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Filtros de segmentación

La siguiente tabla muestra los filtros disponibles para segmentar a los usuarios por eventos personalizados.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el evento personalizado se ha producido **más de X veces** | **MÁS DE** | **NÚMERO** |
| Comprobar si el evento personalizado se ha producido **menos de X veces** | **MENOS DE** | **NÚMERO** |
| Comprobar si el evento personalizado se ha producido **exactamente X número de veces** | **EXACTAMENTE** | **NÚMERO** |
| Comprobar si el evento personalizado ocurrió por última vez **después de la fecha X** | **DESPUÉS DE** | **TIME** |
| Comprobar si el evento personalizado ocurrió por última vez **antes de la fecha X** | **ANTES** | **TIME** |
| Comprobar si el evento personalizado se produjo por última vez **hace más de X días** | **MÁS DE** | **NÚMERO DE DÍAS ATRÁS** (Número positivo) |
| Comprobar si el evento personalizado se produjo por última vez **hace menos de X días** | **MENOS DE** | **NÚMERO DE DÍAS ATRÁS** (Número positivo) |
| Comprobar si el evento personalizado se ha producido **más de X (máx. = 50) veces** | **MÁS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado se ha producido **menos de X (máx. = 50) veces** | **MENOS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado ocurrió **exactamente X (máx. = 50) número de veces** | **EXACTAMENTE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Análisis

Braze registra el número de veces que se han producido eventos personalizados y la última vez que los realizó cada usuario para la segmentación. Para ver estos análisis, ve a **Análisis** > **Informe de eventos personalizados**.

En la página **Informe de eventos personalizados** del dashboard, puedes ver de forma agregada la frecuencia con la que se produce cada evento personalizado. Las líneas grises superpuestas en la serie temporal indican la última vez que se envió una campaña, lo que resulta útil para ver cómo tus campañas afectaron a la actividad de los eventos personalizados.

![Gráfico de recuento de eventos personalizados en la página Eventos personalizados del dashboard que muestra las tendencias de un evento personalizado.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

También puedes utilizar **Filtros** para desglosar tus eventos personalizados por hora, usuarios medios mensuales (MAU), segmentos o fórmulas de KPI. 

![Filtros del gráfico de eventos personalizados]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Incrementa los atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) para mantener un contador de una acción del usuario similar a un evento personalizado. Sin embargo, no puedes ver datos de atributos personalizados en una serie temporal. Las acciones de los usuarios que no necesiten analizarse en una serie temporal deben registrarse utilizando este método.
{% endalert %}

### ¿Por qué no se muestran los análisis de los eventos personalizados?

Los segmentos creados con datos de eventos personalizados no pueden mostrar datos históricos anteriores a su creación.

## Propiedades de eventos personalizados

Las propiedades de eventos personalizados son metadatos o atributos de eventos personalizados que describen una ocurrencia específica de un evento. Estas propiedades pueden utilizarse para cualificar aún más las condiciones desencadenantes, aumentar la personalización de la mensajería, hacer un seguimiento de las conversiones y generar análisis más sofisticados mediante la exportación de datos sin procesar.

Las propiedades de eventos personalizados no se almacenan en el perfil de Braze y, por lo tanto, no registran puntos de datos (consulta [Puntos de datos](#data-points) para excepciones).

{% alert important %}
Cada evento personalizado o compra puede tener hasta 256 propiedades de evento personalizadas distintas. Si se registra un evento personalizado o una compra con más de 256 propiedades, solo se capturarán y estarán disponibles para su uso las 256 primeras.
{% endalert %}

### Formato previsto

Los valores de las propiedades deben ser un objeto donde las claves son los nombres de las propiedades y los valores son los valores de las propiedades. Los nombres de las propiedades deben ser cadenas no vacías de 255 caracteres o menos, sin signos de dólar al principio (`$`).

Los valores de las propiedades pueden ser cualquiera de los siguientes tipos de datos:

| Tipo de datos | Descripción |
| --- | --- |
| Números | Como [números enteros](https://en.wikipedia.org/wiki/Integer) o [flotantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleanos | Valor de `true` o `false`. |
| Fechas y horas | Formateados como cadenas en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) o `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. No se admiten dentro de matrices. |
| Cadenas | 255 caracteres o menos. |
| Matrices | Las matrices no pueden incluir fechas. |
| Objetos anidados | Objetos que están dentro de otros objetos. Para más información, consulta la sección de este artículo sobre [Objetos anidados](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Los objetos de propiedades del evento que contienen valores de matrices u objetos pueden tener una carga útil de propiedades del evento de hasta 100&nbsp;KB.

Los tipos de datos de los valores de las propiedades se detectan y procesan de forma similar a los valores de [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/), con dos diferencias clave:

- **Conversión de cadena a hora:** Los valores de cadena que coinciden con un formato de hora reconocido se convierten automáticamente a un tipo de fecha y hora. Esto significa que algunos valores de cadena no pueden almacenarse tal cual en las propiedades del evento.
- **Sin coerción de tipo:** No hay coerción automática de tipo para las propiedades del evento. Si un filtro desencadenante espera un valor numérico de `5`, un valor de cadena de `"5"` no coincidirá. Lo mismo se aplica a las plantillas de Liquid y a los datos de eventos de Currents.

Estos comportamientos también se aplican a las [propiedades de eventos de compra]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#purchase-properties).

Puedes cambiar el tipo de datos de tu propiedad de evento personalizada, pero ten en cuenta las consecuencias de [cambiar los tipos de datos]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) después de que se hayan recopilado los datos.

#### Claves reservadas

No puedes utilizar claves reservadas como nombres de propiedades del evento. Si usas una clave reservada en el objeto `properties`, se devolverá el error "Campo 'properties' no válido".

| Propiedad | Clave reservada |
| --- | --- |
| Eventos personalizados | `time` y `event_name` | 
| Eventos de compra |`time`, `product_id`, `quantity`, `event_name`, `price`, `currency` | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Uso de propiedades de eventos personalizados

Las propiedades de eventos personalizados pueden utilizarse para calificar los desencadenantes de campañas, realizar un seguimiento de las conversiones y personalizar los mensajes.

#### Desencadenar mensajes

Utiliza propiedades de eventos personalizados para delimitar aún más tu audiencia para una campaña o Canvas concretos. Por ejemplo, si tienes una aplicación de comercio electrónico y quieres enviar un mensaje a un usuario cuando abandone su carrito, puedes añadir una propiedad de evento personalizada de `item price` para mejorar tu audiencia objetivo y permitir una mayor personalización de la campaña.

![Filtros de propiedades de eventos personalizados para un carrito abandonado. Se combinan dos filtros con un operador AND para enviar esta campaña a los usuarios que abandonaron su carrito con un precio de artículo entre 100 y 200 dólares.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Las propiedades de eventos personalizados anidadas también son compatibles con [la entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

![Filtros de propiedades de eventos personalizados para un carrito abandonado. Se selecciona un filtro si alguno de los artículos del carrito tiene un precio superior a 100 dólares.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png")

#### Personalizar mensajes

También puedes utilizar propiedades de eventos personalizados para la personalización dentro de la plantilla de mensajería. Cualquier campaña que utilice [la entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) con un evento desencadenante puede utilizar las propiedades del evento personalizado de ese evento para la personalización de los mensajes.

Por ejemplo, si tienes una aplicación de juegos y quieres enviar un mensaje a los usuarios que completaron un nivel, podrías personalizar aún más tu mensaje con una propiedad para el tiempo que tardaron los usuarios en completar ese nivel. En este ejemplo, el mensaje se personaliza para tres segmentos distintos utilizando [lógica condicional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/). La propiedad de evento personalizada llamada `time_spent` puede incluirse en el mensaje llamando a ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Si el usuario no tiene conexión a Internet, los mensajes dentro de la aplicación desencadenados con propiedades de eventos personalizados con plantillas (por ejemplo, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) fallarán y no se mostrarán.
{% endalert %}

Para obtener una lista completa de las etiquetas de Liquid que harán que los mensajes dentro de la aplicación se entreguen como mensajes dentro de la aplicación con plantilla, consulta [Preguntas frecuentes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/).

##### Consideraciones sobre los filtros

- **Llamadas a la API:** Al realizar llamadas a la API y utilizar el filtro "está en blanco", una propiedad de evento personalizada se considera "en blanco" si se excluye de la llamada. Por ejemplo, si incluyeras `"event_property": ""`, tus usuarios se considerarían "no en blanco".
- **Enteros:** Cuando filtres por una propiedad de evento personalizada numérica y el número sea muy grande, no utilices el filtro "exactamente". Si un número es demasiado grande, es posible que se redondee a una longitud determinada, por lo que el filtro no funcionará como se espera.

#### Segmentación

Utiliza la segmentación de propiedades de eventos para dirigirte a los usuarios en función de los eventos personalizados realizados y las propiedades asociadas a esos eventos. Esto aumenta tus opciones de filtrado al segmentar por compras y eventos personalizados.

Las propiedades de los eventos personalizados se actualizan en tiempo real para cualquier segmento que los utilice. Puedes administrar las propiedades yendo a **Configuración de datos** > **Eventos personalizados** y seleccionando **Administrar propiedades** para el evento personalizado asociado. Las propiedades de eventos personalizados utilizadas en determinados filtros de segmentos tienen un historial retrospectivo máximo de 30 días.

##### Añadir propiedades del evento para la segmentación

Necesitas el [permiso de usuario]({{site.baseurl}}/user_guide/data/data_points/#viewing-data-point-usage) "Editar la segmentación de las propiedades de los eventos personalizados" para crear segmentos basados en la actualidad y la frecuencia de las propiedades del evento.

{% multi_lang_include deprecations/user_permissions.md %}

De forma predeterminada, puedes tener 20 propiedades del evento segmentables por espacio de trabajo. Ponte en contacto con tu director de cuentas de Braze para aumentar este límite.

Para añadir propiedades del evento para la segmentación, haz lo siguiente:

1. Ve a tu evento personalizado y selecciona **Gestionar propiedades**.
2. Selecciona el conmutador **Habilitar segmentación** para añadir la propiedad del evento para la segmentación. Puedes acceder a opciones de filtrado adicionales al segmentar.

Los filtros de segmentación de propiedades del evento incluyen:

- Ha realizado un evento personalizado con la propiedad A con valor B, X veces en los últimos Y días.
- Ha realizado alguna compra con la propiedad A con valor B, X veces en los últimos Y días.
- Añade la posibilidad de segmentar de 1 a 30 días.

![Un grupo de filtros que tiene «Carrito abandonado» con la propiedad «número de artículos» y un valor 2 más de una vez en los últimos 30 días naturales.]({% image_buster /assets/img/nested_object3.png %})

Los datos solo se registran para una propiedad del evento determinada después de habilitarla, y las propiedades del evento solo están disponibles a partir de esa fecha en adelante.

##### Puntos de datos

En lo que respecta al uso de suscripciones, las propiedades de eventos personalizados habilitadas para la segmentación con los siguientes filtros se contabilizan como puntos de datos independientes, además del punto de datos contabilizado por el propio evento personalizado:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propiedades de entrada en Canvas y propiedades de eventos

{% multi_lang_include canvas_entry_event_properties.md %}

### Objetos anidados {#nested-objects}

Puedes utilizar objetos anidados (objetos dentro de otro objeto) para enviar datos JSON anidados como propiedades de eventos personalizados y compras. Estos datos anidados pueden utilizarse para crear plantillas de información personalizada en los mensajes, desencadenar envíos de mensajes y segmentar a los usuarios.

Para saber más, consulta nuestra página dedicada a [los objetos anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

## Almacenamiento de propiedades de eventos personalizados

Las propiedades de eventos personalizados están diseñadas para ayudarte a aumentar la precisión de la segmentación y hacer que los mensajes parezcan aún más personalizados. Las propiedades de los eventos personalizados pueden almacenarse en Braze tanto a corto como a largo plazo.

Puedes segmentar basándote en los valores de las propiedades del evento de las siguientes formas:

- **En un plazo de 30 días:** Puedes utilizar la segmentación de propiedades del evento basada en la frecuencia y la actualidad de valores específicos de propiedades del evento dentro de los segmentos de Braze. Esta opción afecta al uso de datos.<br><br>
- **Dentro y más allá de los 30 días:** Para cubrir la segmentación de propiedades de eventos tanto a corto como a largo plazo, puedes utilizar [extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Esta característica segmenta a los usuarios basándose en eventos personalizados y propiedades del evento de los que se ha hecho un seguimiento en los últimos dos años. Esta opción no afecta al uso de datos.<br><br>
- **Canvas con matrices de atributos personalizados:** Crea y lanza un Canvas que se desencadene con el evento personalizado. Configura un paso de **Actualización de usuario** que utilice **Añadir elemento** para agregar la propiedad del evento a una matriz de atributos personalizados en el perfil de usuario, y luego segmenta a los usuarios utilizando filtros en esa matriz de atributos personalizados en lugar de filtros de propiedades del evento. Esta opción afecta al uso de datos porque cada actualización de la matriz de atributos personalizados consume puntos de datos. Para más detalles de implementación, consulta [Pasos de actualización de usuario en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) y [matrices de atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/#arrays).

Ponte en contacto con tu administrador del éxito del cliente de Braze para que te recomiende el mejor enfoque en función de tus necesidades específicas.