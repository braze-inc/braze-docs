---
nav_title: Eventos personalizados
article_title: Eventos personalizados
page_order: 9
page_type: reference
description: "En este artículo se describen los eventos y propiedades personalizados, la segmentación, el uso, las propiedades de entrada de Canvas, dónde ver los análisis relevantes y mucho más."
search_rank: 2
---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Eventos personalizados

> Este artículo describe los eventos personalizados y sus propiedades, los filtros de segmentación relacionados, las propiedades de entrada en Canvas, los análisis relevantes y mucho más. Para conocer los eventos de Braze en general, consulta [Eventos]({{site.baseurl}}/user_guide/data/custom_data/events/).

Los eventos personalizados son acciones realizadas por tus usuarios o actualizaciones sobre ellos. Cuando se registran eventos personalizados, pueden desencadenar cualquier número y tipo de campañas de seguimiento. A continuación, puedes utilizar [filtros de segmentación](#segmentation-filters) para segmentar a los usuarios en función de lo recientes y frecuentes que hayan sido esos eventos personalizados. Esto hace que los eventos personalizados sean los más adecuados para el seguimiento de interacciones de usuario de alto valor dentro de tu aplicación.

## Ejemplos

Algunos casos habituales de uso de eventos personalizados son:

- Desencadenar una campaña o Canvas basada en un evento personalizado utilizando [la entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)
- Segmentar a los usuarios por el número de veces que realizaron un evento personalizado, cuándo se produjo el evento por última vez y similares
- Utilizar el panel de [análisis de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) para ver un agregado de la frecuencia con la que se ha producido cada evento
- Encontrar análisis adicionales mediante informes de [embudo]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) y [retención]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) 
- Aprovechar [las propiedades de entrada persistentes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) para utilizar metadatos de tu evento de cliente para la personalización en tus pasos en Canvas
- Generar análisis más sofisticados con [Currents]({{site.baseurl}}/user_guide/data/braze_currents/)
- Configuración de [eventos de excepción]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events#canvas-exception-events) de Canvas para definir cuándo los usuarios no deben avanzar al siguiente paso de tu Canvas

## Gestión de eventos personalizados

Puedes gestionar, crear o bloquear eventos personalizados en el panel yendo a **Configuración de datos** > **Eventos personalizados**.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar **Eventos personalizados** en **Administrar configuración**.
{% endalert %}

Seleccione el menú situado junto a un evento personalizado para realizar las siguientes acciones:

### Agregando a la lista de bloqueo

Puedes bloquear eventos personalizados individuales a través del menú de acciones, o seleccionar y bloquear hasta 100 eventos en bloque. 

Cuando bloqueas un evento personalizado:

- No se recogerán datos futuros para ese evento.
- Los datos existentes no estarán disponibles a menos que se desbloquee ese evento.
- Ese evento no aparecerá en los filtros ni en los gráficos.

Además, si un evento personalizado bloqueado es referenciado actualmente por filtros o desencadenantes en otras áreas de Braze, aparecerá un modal de advertencia explicando que todas las instancias de los filtros o desencadenantes que lo referencian serán eliminadas y archivadas.

### Añadir descripciones

Puede añadir una descripción a un evento personalizado después de crearlo si dispone del [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Seleccione **Editar descripción** para el evento personalizado e introduzca lo que desee, como una nota para su equipo.

## Añadir etiquetas

Puedes añadir etiquetas a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "Gestionar eventos, atributos, compras". Las etiquetas pueden utilizarse para filtrar la lista de eventos.

### Visualización de informes de uso

El informe de uso enumera todos los Canvases, campañas y segmentos que utilizan un evento personalizado específico. La lista no incluye los usos de Liquid. 

Puedes ver hasta 100 informes de uso a la vez seleccionando las casillas de verificación de varios eventos personalizados y, a continuación, seleccionando **Ver informe de uso**.

## Exportar datos

Para exportar la lista de eventos personalizados como un archivo CSV, selecciona el botón **Exportar todo** en la parte superior de la página. Se generará el archivo CSV y se le enviará por correo electrónico un enlace de descarga.

## Registro de eventos personalizados

Los eventos personalizados requieren una configuración adicional. Consulta la lista siguiente para obtener documentación sobre cada plataforma, donde encontrarás información sobre los métodos utilizados para registrar eventos personalizados y sobre cómo añadir propiedades y cantidades a tus eventos personalizados.

{% details Ampliar para documentación por plataforma %}

- [Android y FireOS]({{site.baseurl}}/developer_guide/platforms/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platforms/swift/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platforms/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platforms/roku/analytics/logging_custom_events/)

{% enddetails %}

## Almacenamiento de eventos personalizado

Todos los datos almacenados en el **perfil de usuario**, incluidos los metadatos de eventos personalizados (primera o última aparición, recuento total y X en Y a lo largo de 30 días), se conservan indefinidamente mientras cada perfil esté [activo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Filtros de segmentación

La siguiente tabla muestra los filtros disponibles para segmentar a los usuarios por eventos personalizados.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el evento personalizado se ha producido **más de X veces** | **MÁS DE** | **NÚMERO** |
| Comprobar si el evento personalizado se ha producido **menos de X veces** | **MENOS DE** | **NÚMERO** |
| Comprueba si el evento personalizado se ha producido **exactamente X número de veces** | **EXACTAMENTE** | **NÚMERO** |
| Comprueba si el evento personalizado ocurrió por última vez **después de X fecha** | **DESPUÉS DE** | **TIME** |
| Comprobar si el evento personalizado ocurrió por última vez **antes de X fecha** | **ANTES** | **TIME** |
| Compruebe si el evento personalizado se produjo por última vez **hace más de X días** | **MÁS DE** | **NÚMERO DE DÍAS DESPUÉS** (Número positivo) |
| Compruebe si el evento personalizado se produjo por última vez **hace menos de X días** | **MENOS DE** | **NÚMERO DE DÍAS DESPUÉS** (Número positivo) |
| Compruebe si el evento personalizado se ha producido **más de X (máx. = 50) veces.** | **MÁS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado se ha producido **menos de X (Máx. = 50) veces** | **MENOS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprueba si el evento personalizado ocurrió **exactamente X (Máx. = 50) número de veces** | **EXACTAMENTE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Análisis

Braze anota el número de veces que se han producido eventos personalizados y la última vez que los realizó cada usuario para la segmentación. Para ver estos análisis, ve a **Análisis** > **Informe de eventos personalizados**.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar el informe de **Eventos personalizados** en **Datos**.
{% endalert %}

En la página **Informe de eventos personalizados** del panel, puedes ver de forma agregada la frecuencia con la que se produce cada evento personalizado. Las líneas grises superpuestas en la serie temporal indican la última vez que se envió una campaña, lo que resulta útil para ver cómo afectaron tus campañas a la actividad de los eventos personalizados.

![Gráfico de recuento de eventos personalizados en la página Eventos personalizados del cuadro de mandos que muestra las tendencias de un evento personalizado.][8]

También puede utilizar **filtros** para desglosar sus eventos personalizados por hora, usuarios medios mensuales (MAU), segmentos o fórmulas de KPI. 

![Filtros personalizados del gráfico de eventos][9]{: style="max-width:40%;"}

{% alert tip %}
[Incrementa los atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) para mantener un contador de una acción del usuario similar a un evento personalizado. Sin embargo, no puedes ver datos de atributos personalizados en una serie temporal. Las acciones de los usuarios que no necesiten analizarse en una serie temporal deben registrarse utilizando este método.
{% endalert %}

### ¿Por qué no se muestran los análisis de los eventos personalizados?

Los segmentos creados con datos de eventos personalizados no pueden mostrar datos históricos anteriores a su creación.

## Propiedades personalizadas de los eventos

Las propiedades de eventos personalizadas son metadatos o atributos de eventos personalizados que describen una ocurrencia específica de un evento. Estas propiedades pueden utilizarse para cualificar aún más las condiciones desencadenantes, aumentar la personalización de la mensajería, hacer un seguimiento de las conversiones y generar análisis más sofisticados mediante la exportación de datos sin procesar.

Las propiedades del evento personalizado no se almacenan en el perfil Braze y, por tanto, no consumen puntos de datos (consulta [Puntos de datos](#data-points) para ver las excepciones).

{% alert important %}
Cada evento o compra personalizada puede tener hasta 256 propiedades de evento personalizadas distintas. Si se registra un evento personalizado o una compra con más de 256 propiedades, sólo se capturarán y estarán disponibles para su uso las 256 primeras.
{% endalert %}

### Formato previsto

Los valores de las propiedades deben ser un objeto donde las claves son los nombres de las propiedades y los valores son los valores de las propiedades. Los nombres de las propiedades deben ser cadenas no vacías de menos o igual a 255 caracteres, sin signos de dólar al principio (`$`).

Los valores de las propiedades pueden ser cualquiera de los siguientes tipos de datos:

| Tipo de datos | Descripción |
| --- | --- |
| Números | Como [números enteros](https://en.wikipedia.org/wiki/Integer) o [flotantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleanos | Valor de `true` o `false`. |
| Fechas y horas | Formateados como cadenas en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) o `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. No se admite dentro de matrices. |
| Cadenas | 255 caracteres o menos. |
| Matrices | Las matrices no pueden incluir fechas. |
| Objetos | Los objetos se ingieren como cadenas. |
| Objetos anidados | Objetos que están dentro de otros objetos. Para más información, consulte la sección de este artículo sobre [Objetos anidados](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Los objetos de propiedades del evento que contienen valores de matrices u objetos pueden tener una carga útil de propiedades del evento de hasta 100 KB.

Puede cambiar el tipo de datos de su propiedad de evento personalizada, pero tenga en cuenta las consecuencias de [cambiar los tipos de datos]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) después de que se hayan recopilado los datos.

### Uso de propiedades de eventos personalizadas

Las propiedades de eventos personalizados pueden utilizarse para calificar los desencadenantes de campañas, realizar un seguimiento de las conversiones y personalizar los mensajes.

#### Mensajes de activación

Utiliza propiedades del evento personalizadas para delimitar aún más tu audiencia para una campaña o Canvas concretos. Por ejemplo, si tienes una aplicación de comercio electrónico y quieres enviar un mensaje a un usuario cuando abandone su carrito, puedes añadir una propiedad de evento personalizada de `cart value` para mejorar tu audiencia objetivo y permitir una mayor personalización de la campaña.

![Filtros de propiedades de eventos personalizados para una tarjeta abandonada. Se combinan dos filtros con un operador AND para enviar esta campaña a los usuarios que abandonaron su tarjeta con un valor de carrito entre 100 y 200 dólares][16]

Las propiedades de eventos personalizados anidados también se admiten en [entrega basada en acciones][19].

![Filtros de propiedades de eventos personalizados para una tarjeta abandonada. Se selecciona un filtro si alguno de los artículos del carrito tiene un precio superior a 100 dólares.][20]

#### Personalizar los mensajes

También puede utilizar propiedades de evento personalizadas para la personalización dentro de la plantilla de mensajería. Cualquier campaña que utilice [entrega basada en acciones][19] con un evento desencadenante puede utilizar propiedades de evento personalizadas de ese evento para la personalización de la mensajería.

Por ejemplo, si tienes una aplicación de juegos y quieres enviar un mensaje a los usuarios que completaron un nivel, podrías personalizar aún más tu mensaje con una propiedad para el tiempo que tardaron los usuarios en completar ese nivel. En este ejemplo, el mensaje se personaliza para tres segmentos diferentes utilizando la [lógica condicional][18]. La propiedad de evento personalizada llamada `time_spent` puede incluirse en el mensaje llamando a ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

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
Si el usuario no tiene conexión a Internet, los mensajes desencadenados dentro de la aplicación con propiedades del evento personalizadas con plantillas (por ejemplo, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) fallarán y no se mostrarán.
{% endalert %}

Para obtener una lista completa de las etiquetas Liquid que harán que los mensajes in-app se entreguen como mensajes in-app con plantilla, consulte [Preguntas frecuentes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/).

##### Consideraciones sobre los filtros

- **Llamadas a la API:** Al realizar llamadas a la API y utilizar el filtro "está en blanco", una propiedad de evento personalizada se considera "en blanco" si se excluye de la llamada. Por ejemplo, si incluyera `"event_property": ""`, sus usuarios se considerarían "no en blanco".
- **Enteros:** Cuando filtre por una propiedad de evento personalizada numérica y el número sea muy grande, no utilice el filtro "exactamente". Si un número es demasiado grande, es posible que se redondee a una longitud determinada, por lo que el filtro no funcionará como se espera.

#### Segmentación

Utiliza la segmentación de propiedades de eventos para dirigirte a los usuarios en función de los eventos personalizados realizados y las propiedades asociadas a esos eventos. Esto aumenta tus opciones de filtrado al segmentar por compras y eventos personalizados.

Las propiedades de los eventos personalizados se actualizan en tiempo real para cualquier segmento que los utilice. Puedes administrar propiedades yendo a **Configuración de datos** > **Eventos personalizados** y seleccionando **Administrar propiedades** para el evento personalizado asociado. Las propiedades de eventos personalizadas utilizadas en determinados filtros de segmentos tienen un historial retrospectivo máximo de 30 días.

##### Añadir propiedades del evento para la segmentación

Necesitarás [permisos de usuario]({{site.baseurl}}/user_guide/data/data_points/#viewing-data-point-usage) de "Gestionar la segmentación de propiedades de eventos personalizados" para crear segmentos basados en la recencia y frecuencia de las propiedades de los eventos.

Para añadir propiedades del evento para la segmentación, haz lo siguiente:

1. Ve a tu evento personalizado y selecciona **Gestionar propiedades**.
2. Selecciona el conmutador **Habilitar segmentación** para añadir la propiedad del evento para la segmentación. Puedes acceder a opciones de filtrado adicionales al segmentar.

Los filtros de segmentación de propiedades del evento incluyen:

- Ha realizado un evento personalizado con la propiedad A con valor B, X veces en los últimos Y días.
- Ha realizado alguna compra con la propiedad A con valor B, X veces en los últimos Y días.
- Añade la posibilidad de segmentar de 1 a 30 días.

![Un grupo de filtrar que "tiene 'Carrito Abandonado' con propiedad 'número de itmes' y valor '2' 'más de' 1'1 veces en los últimos '30' días naturales".][3]

Los datos sólo se registran para una determinada propiedad del evento una vez que ha sido habilitada por tu administrador del éxito del cliente, y las propiedades del evento sólo están disponibles a partir de esa fecha en adelante.

##### Puntos de datos

En lo que respecta al uso de suscripciones, las propiedades de eventos personalizados habilitadas para la segmentación con los siguientes filtros se contabilizan como puntos de datos independientes, además del punto de datos contabilizado por el propio evento personalizado:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propiedades de entrada en el lienzo y propiedades de eventos

Puedes utilizar `canvas_entry_properties` y `event_properties` en tus recorridos de usuario de Canvas. Consulta las [propiedades de la entrada y las propiedades del evento en]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) Canvas para obtener más información y ejemplos.

{% tabs local %}
{% tab Propiedades de entrada del lienzo %}

[Las propiedades de entrada del lienzo]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) son las propiedades que se asignan a los lienzos basados en acciones o activados por la API. El objeto `canvas_entry_properties` tiene un límite de tamaño máximo de 50 KB.

{% alert note %}
En el caso concreto de los canales de mensajes integrados en la aplicación, sólo se puede hacer referencia a `canvas_entry_properties` en Canvas Flow y en el editor Canvas original si tienes activadas las propiedades de entrada persistente en el editor original como parte del acceso anticipado anterior.
{% endalert %}

Para la mensajería del Flujo Canvas, `canvas_entry_properties` puede utilizarse en cualquier paso en Canvas con este formato Liquid: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Tenga en cuenta que los eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta manera. 

#### Caso de uso

{% raw %}
Supongamos que una tienda minorista, RetailApp, tiene la siguiente petición: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. RetailApp puede incluir el nombre del producto (zapatos) en un mensaje con la función Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

RetailApp también puede activar el envío de mensajes específicos para diferentes propiedades de `product_name` en un Canvas dirigido a los usuarios después de que hayan activado un evento de compra. Por ejemplo, pueden enviar mensajes diferentes a los usuarios que compraron zapatos y a los usuarios que compraron otra cosa añadiendo el siguiente Líquido en un paso de Mensaje.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Ampliar para el editor Canvas original %}

A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible sólo como referencia.

Para los lienzos construidos con el editor original, `canvas_entry_properties` sólo puede referenciarse en el primer paso completo de un lienzo.

{% enddetails %}
{% endtab %}

{% tab Propiedades de los eventos %}

{% alert important %}
No puedes utilizar `event_properties` en el paso Mensaje principal. En su lugar, debe utilizar `canvas_entry_properties` o añadir un paso Rutas de acción con el evento correspondiente **antes** del paso Mensaje que incluye `event_properties`.
{% endalert %}

Las propiedades de eventos se refieren a las propiedades que usted establece para los eventos y compras personalizados. Estos `event_properties` se pueden utilizar en campañas con entrega basada en acciones y Lienzos.

En el Flujo del lienzo, las propiedades de eventos personalizados y eventos de compra se pueden utilizar en Liquid en cualquier paso de Mensaje que siga a un paso de Rutas de acción. Asegúrese de utilizar {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} si hace referencia a estos `event_properties`. Estos eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta forma en el componente Mensaje.

En el primer paso de Mensaje que sigue a una Ruta de Acción, puede utilizar `event_properties` relacionado con el evento al que se hace referencia en esa Ruta de Acción. Estos `event_properties` sólo pueden utilizarse si el usuario realizó realmente la acción (y no fue al grupo Todos los demás). Puede tener otros pasos (que no sean otra Ruta de Acción o paso de Mensaje) entre esta Ruta de Acción y el paso de Mensaje.

{% details Ampliar para el editor Canvas original %}

A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible sólo como referencia.

En el editor Canvas original, `event_properties` no puede utilizarse en pasos completos programados. Sin embargo, puede utilizar `event_properties` en el primer paso completo de un Canvas basado en acciones, incluso si el paso completo está programado.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Objetos anidados {#nested-objects}

Puede utilizar objetos anidados (objetos dentro de otro objeto) para enviar datos JSON anidados como propiedades de eventos y compras personalizados. Estos datos anidados pueden utilizarse para plantillas de información personalizada en los mensajes, desencadenar envíos de mensajes y segmentar a los usuarios.

Para saber más, consulta nuestra página dedicada a [los objetos anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

## Almacenamiento personalizado de propiedades de eventos

Las propiedades de eventos personalizados están diseñadas para ayudarle a aumentar la precisión de la segmentación y hacer que los mensajes parezcan aún más personalizados. Las propiedades de los eventos personalizados pueden almacenarse en Braze tanto a corto como a largo plazo.

Puedes segmentar basándote en los valores de las propiedades del evento de dos formas:

1. **En un plazo de 30 días:** El personal de soporte de Braze puede habilitar la segmentación de propiedades de eventos basándose en la frecuencia y recurrencia de valores específicos de propiedades de eventos dentro de segmentos Braze. Si quieres aprovechar las propiedades del evento dentro de los segmentos, ponte en contacto con tu ejecutivo de cuentas o administrador del éxito del cliente de Braze. Esta opción afectará al uso de datos.<br><br>
2. **Dentro y fuera de los 30 días:** Para cubrir la segmentación de propiedades de eventos tanto a corto como a largo plazo, puede utilizar [Extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Esta característica segmenta a los usuarios basándose en eventos personalizados y propiedades del evento de los que se ha hecho un seguimiento en los últimos dos años. Esta opción no afectará al uso de datos.

Póngase en contacto con su gestor de éxito de clientes de Braze para que le recomiende el mejor enfoque en función de sus necesidades específicas.

[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[3]: {% image_buster /assets/img/nested_object3.png %}
[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[9]: {% image_buster /assets/img/custom_events_report_filters.png %}
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"
