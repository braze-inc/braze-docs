---
nav_title: Mensaje 
article_title: Mensaje 
alias: "/message_step/"
page_order: 5
page_type: reference
description: "Este artículo de referencia explica cómo crear un mensaje independiente utilizando el paso Mensaje."
tool: Canvas

---

# Mensaje 

> Los pasos de mensaje te permiten añadir un mensaje independiente donde quieras en tu Flujo del lienzo.

![][1]{: style="float:right;max-width:25%;margin-left:15px;"}

## Crear un mensaje

Para crear un componente Mensaje, añade primero un paso a tu Canvas. Arrastre y suelte el componente desde la barra lateral, o haga clic en el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y seleccione **Mensaje**. 

### Configurar mensajes

Todos los usuarios que entren en el paso Mensaje avanzarán al siguiente paso cuando se cumpla alguna de las siguientes condiciones:
- Se envía cualquier mensaje
- Un mensaje tiene un límite de frecuencia y no se envía
- Se cancela un mensaje
- Un usuario no está localizable por canal, por lo que el mensaje no se envía

![Configure los ajustes de Mensajes para un paso de Mensaje que incluya la opción de seleccionar su canal de mensajes y personalizar los ajustes de entrega.][2]{: style="max-width:75%;"}

{% raw %}
Si un Canvas basado en acciones se activa mediante un mensaje SMS entrante, puede hacer referencia a las propiedades de SMS en el primer paso (paso Mensaje) o en un paso Mensaje anidado bajo un paso Ruta de acción. Por ejemplo, en el paso Mensaje, podrías utilizar `{{sms.${inbound_message_body}}}` o `{{sms.${inbound_media_urls}}}`.
{% endraw %}

### Editar la configuración de entrega

El componente Mensaje también incluye opciones de entrega inteligente, anulación de las horas de silencio y validación de la entrega. Puede activar [el Cronometraje Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) con una opción alternativa cuando el perfil de un usuario no tenga suficientes datos para calcular un tiempo óptimo. Recomendamos activar la temporización inteligente y la [limitación de velocidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) como comprobación adicional de cualquier retraso entre que los usuarios entran en el paso Mensaje y el envío real del mensaje.

Seleccione **Utilizar sincronización inteligente** en la pestaña **Configuración de entrega**. Aquí puede seleccionar la hora más popular o una hora alternativa específica. Si las Horas de Silencio están activadas, el paso Mensaje también le permite anular esta configuración.

Las validaciones de entrega proporcionan una comprobación adicional para confirmar que su público cumple los criterios de entrega en el envío del mensaje. Este ajuste se recomienda si están activadas las horas de silencio, la temporización inteligente o la limitación de velocidad. Puede añadir un segmento o filtros adicionales para validar en el momento del envío del mensaje. Si un usuario no cumple las validaciones de entrega establecidas para un paso de Mensaje, saldrá del Canvas en el paso.

![La pestaña Configuración de entrega para la configuración del componente Mensaje. Las horas de silencio están activadas y la casilla de verificación Utilizar sincronización inteligente está seleccionada para enviar el mensaje a una hora óptima. Las validaciones de entrega se activan para validar la audiencia en el envío del mensaje.][4]{: style="max-width:80%;"}

### Propiedades de entrada del lienzo

Las propiedades de entrada al lienzo se configuran en el paso Programación de entradas de la creación de un lienzo e indicarán el desencadenante que introduce a un usuario en un lienzo. Estas propiedades también pueden acceder a las propiedades de las cargas útiles de entrada en los lienzos activados por API. El objeto `canvas_entry_properties` tiene un límite de tamaño máximo de 50 KB. 

{% alert note %}
Para los canales de mensajes in-app específicamente, `canvas_entry_properties` sólo puede ser referenciado en Canvas Flow y en el editor Canvas original si tienes activadas las propiedades de entrada persistente en el editor original como parte del acceso anticipado anterior.
{% endalert %}

#### Canvas Flow

Para la mensajería del Flujo del lienzo, las propiedades de entrada se pueden utilizar en Liquid en cualquier paso de Mensaje. Utilice el siguiente Líquido cuando haga referencia a estas propiedades de entrada: {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Los eventos deben ser eventos personalizados o eventos de compra para poder utilizarse de esta forma.

Utilice el siguiente Líquido cuando haga referencia a estas propiedades de entrada: {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %}. Tenga en cuenta que los eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta manera.

{% raw %}
Por ejemplo, considere la siguiente petición: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Podrías añadir la palabra "zapatos" a un mensaje con el `{{canvas_entry_properties.${product_name}}}` de Liquid.
{% endraw %}

También puede aprovechar [las propiedades de entrada persistentes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) en cualquier paso de Mensaje para guiar a sus usuarios a través de pasos personalizados en todo el flujo de trabajo de Canvas.

#### Flujo de trabajo original

Para los lienzos construidos con el editor original, `canvas_entry_properties` sólo puede referenciarse en el primer paso completo de un lienzo.

### Propiedades del evento

Las propiedades de eventos se refieren a las propiedades que usted establece para los eventos y compras personalizados. Estos `event_properties` se pueden utilizar en campañas con entrega basada en la acción, así como Lienzos. 

#### Canvas Flow

En el Flujo del lienzo, las propiedades de eventos personalizados y eventos de compra se pueden utilizar en Liquid en cualquier paso de Mensaje que siga a un paso de [Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). Para Canvas Flow, utilice este líquido `` {% raw %} {{event_properties.${property_name}}} {% endraw %}`` cuando haga referencia a estos `event_properties`. Estos eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta forma en el componente Mensaje.

{% alert important %}
`event_properties` no puede utilizarse independientemente de las Rutas de Acción para el Flujo del lienzo.
{% endalert %}

En el primer paso de Mensaje que sigue a una Ruta de Acción, puede utilizar `event_properties` relacionado con el evento al que se hace referencia en esa Ruta de Acción. Puede tener otros pasos (que no sean otro paso de Rutas de acción o Mensaje) entre este paso de Rutas de acción y el paso de Mensaje. Ten en cuenta que solo tendrás acceso a `event_properties` si tu paso de Mensaje puede remontarse a una ruta que no sea Todos los demás en un paso de Ruta de acción.

#### Flujo de trabajo original

`event_properties` se puede utilizar en el primer paso completo en un Canvas basado en acciones utilizando el flujo de trabajo original, incluso si el paso completo está programado. 

{% alert important %}
Para el Canvas Flow y el editor original, no puedes utilizar `event_properties` en el paso Mensaje principal. En su lugar, debe utilizar `canvas_entry_properties` o añadir un paso Rutas de acción con el evento correspondiente antes del paso Mensaje que incluye `event_properties`.
{% endalert %}

Para más información y ejemplos, consulta las [propiedades de entrada y las propiedades de evento de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/).


## Análisis

Consulte en la tabla siguiente las definiciones de las métricas de los componentes de los mensajes: 

| Métrica | Descripción |
| --- | --- |
| Entradas | El número de veces que se ha introducido el paso. Si su Lienzo tiene reeleccionabilidad y un usuario introduce un paso de Mensaje dos veces, se registrarán dos entradas. |
| Continúa con el paso siguiente | Número de entradas que han pasado a la etapa siguiente en el lienzo. |
| Envíos | El número total de mensajes que el paso ha enviado. Si el usuario vuelve a ser apto para el Canvas e introduce un paso de Mensaje dos veces, se registrarán dos entradas. |
| Destinatarios únicos | El número de usuarios que han recibido mensajes de este paso. |
| Evento de conversión primaria | El número de veces que se ha producido un evento definido después de interactuar o ver un mensaje recibido de una campaña Braze. Este evento se define al crear la campaña. |
| Ingresos | Los ingresos totales en dólares de los destinatarios de la campaña dentro de la ventana de conversión primaria establecida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]{: style="max-width:20%;"}


[1]: {% image_buster /assets/img/canvas_components/message_step1.png %}
[2]: {% image_buster /assets/img/canvas_components/message_step2.png %}
[3]: {% image_buster /assets/img/canvas_components/message_step3.png %}
[4]: {% image_buster /assets/img/canvas_components/message_step4.png %}
