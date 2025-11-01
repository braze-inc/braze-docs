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

> Los pasos de mensajería te permiten añadir un mensaje independiente donde quieras en tu Canvas.

\![Un paso de mensaje llamado "Promoción almuerzo" utilizando el canal de mensajería push.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## Crear un mensaje

Para crear un componente Mensaje, añade primero un paso a tu Canvas. Arrastra y suelta el componente desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **Mensaje**. 

### Paso 1: Selecciona tu canal de mensajería

Puedes seleccionar uno de los siguientes canales de mensajería: 
- Tarjetas de contenido
- Correo electrónico
- LÍNEA
- Notificaciones push
- SMS/MMS/RCS
- Mensajes dentro de la aplicación 
- Webhook
- WhatsApp

\![Una lista de los canales de mensajería disponibles para seleccionar en el paso Mensaje.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### Paso 2: Editar configuración de entrega

A continuación, puedes editar la configuración de la Entrega Inteligente, la anulación de las horas tranquilas y la validación de la entrega.

#### Intelligent Timing

Puedes habilitar [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) con una opción alternativa cuando el perfil de un usuario no tenga datos suficientes para calcular una hora óptima. Recomendamos habilitar Intelligent Timing y [el límite de tasa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) como comprobación adicional de cualquier retraso entre que los usuarios entran en el paso Mensaje y el envío real del mensaje.

Selecciona **Utilizar Intelligent Timing** en la pestaña **Configuración de la entrega**. Aquí puedes seleccionar la hora más popular o una hora alternativa específica. Si están habilitadas las Horas tranquilas, el paso Mensaje también te permite anular esta configuración.

#### Validaciones de entrega

Las validaciones de entrega proporcionan una comprobación adicional para confirmar que tu audiencia cumple los criterios de entrega en el envío del mensaje. Se recomienda esta configuración si están activadas las horas tranquilas, el Intelligent Timing o el límite de tasa. Puedes añadir un segmento o filtros adicionales para validar en el momento del envío del mensaje. Si un usuario no cumple las validaciones de entrega establecidas para un paso de Mensaje, saldrá del Canvas en ese paso.

\![La pestaña Configuración de entrega para la configuración del componente Mensaje. Se habilitan las Horas tranquilas y se selecciona la casilla de verificación Utilizar Intelligent Timing para entregar el mensaje a una hora óptima. Se habilitan las Validaciones de entrega para validar la audiencia en el envío de mensajes.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

## Cómo avanzan los usuarios

Todos los usuarios que entren en el paso Mensaje avanzarán al siguiente paso cuando se cumpla alguna de las siguientes condiciones:

- Se envía cualquier mensaje
- Un mensaje tiene limitación de frecuencia y no se envía
- Se cancela un mensaje
- Un usuario no está localizable por canal, por lo que el mensaje no se envía

{% raw %}
Si un Canvas basado en acciones es desencadenado por un mensaje SMS entrante, puedes hacer referencia a propiedades SMS en el primer paso (paso Mensaje) o en un paso Mensaje anidado bajo un paso Ruta de acción. Por ejemplo, en el paso Mensaje, podrías utilizar `{{sms.${inbound_message_body}}}` o `{{sms.${inbound_media_urls}}}`.
{% endraw %}

## Referencia a las propiedades de entrada del Canvas

Las propiedades de entrada al Canvas se configuran en el paso **Programa de entrada** de la creación de un Canvas e indicarán el desencadenante que introduce a un usuario en un Canvas. Estas propiedades también pueden acceder a las propiedades de las cargas útiles de entrada en los Lienzos desencadenados por la API. Nota que el objeto `canvas_entry_properties` tiene un límite de tamaño máximo de 50 KB. 

Las propiedades de entrada pueden utilizarse en Liquid en cualquier paso de Mensaje. Utiliza el siguiente Liquid cuando hagas referencia a estas propiedades de entrada: {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. Los eventos deben ser eventos personalizados o eventos de compra para poder utilizarse de esta forma.

{% alert note %}
En el caso concreto de los canales de mensajería dentro de la aplicación, sólo se puede hacer referencia a `canvas_entry_properties` en Canvas.
{% endalert %}

Utiliza el siguiente Liquid cuando hagas referencia a estas propiedades de entrada: {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. Ten en cuenta que los eventos deben ser eventos personalizados o eventos de compra para poder utilizarlos de esta forma.

{% raw %}
Por ejemplo, considera la siguiente petición: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Podrías añadir la palabra "zapatos" a un mensaje con el Líquido `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

También puedes aprovechar [las propiedades de entrada persistente]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) en cualquier paso de Mensaje para guiar a tus usuarios por pasos personalizados a lo largo de tu flujo de trabajo en Canvas.

### Propiedades del evento

Las propiedades del evento se refieren a las propiedades que configuras para los eventos personalizados y los eventos de la compra. Estas propiedades del evento pueden utilizarse en campañas con entrega basada en acciones, así como en Lienzos. 

En Canvas, las propiedades del evento personalizado y del evento de compra pueden utilizarse en Liquid en cualquier paso de Mensaje que siga a un paso de [Ruta de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). Por ejemplo, cuando hagas referencia a `event_properties`, utiliza este fragmento de código Liquid: {% raw %}``{{event_properties.${property_name}}}``{% endraw %} 

{% alert important %}
`event_properties` no puede utilizarse independientemente de los pasos de las Rutas de acción.
{% endalert %}

En el primer paso de Mensaje que sigue a una Ruta de acción, puedes utilizar `event_properties` relacionado con el evento al que se hace referencia en esa Ruta de acción. Puedes tener otros pasos (que no sean otras Rutas de Acción o pasos de Mensaje) entre este paso de Rutas de Acción y el paso de Mensaje. Ten en cuenta que sólo tendrás acceso a `event_properties` si tu paso de Mensaje puede remontarse a una ruta que no sea Todos los demás en un paso de Ruta de acción.

{% alert important %}
No puedes utilizar `event_properties` en el paso Mensaje principal. En su lugar, debes utilizar `canvas_entry_properties` o añadir un paso Rutas de acción con el evento correspondiente antes del paso Mensaje que incluye `event_properties`.
{% endalert %}

{% details Expand for original Canvas editor %}

Ya no puedes crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible sólo como referencia.

- `event_properties` no puede utilizarse en pasos completos programados. Sin embargo, puedes utilizar `event_properties` en el primer paso completo de un Canvas basado en acciones, aunque el paso completo esté programado.
- `canvas_entry_properties` sólo puede referenciarse en el primer paso completo de un Canvas.
- En el caso concreto de los canales de mensajería dentro de la aplicación, se puede hacer referencia a `canvas_entry_properties` en el editor Canvas original si tienes habilitadas las propiedades de entrada persistente como parte del acceso anticipado anterior.

{% enddetails %}

## Análisis

Consulta la tabla siguiente para ver las definiciones de las métricas del componente Mensaje: 

| Métrica | Descripción |
| --- | --- |
| _Entradas_ | El número de veces que se ha introducido el paso. Si tu Canvas vuelve a ser elegible y un usuario entra dos veces en un paso en Mensaje, se registrarán dos entradas. |
| _Pasar al siguiente paso_ | El número de entradas que pasaron al siguiente paso en Canvas. |
| _Envía_ | El número total de mensajes que ha enviado el paso. Si tu Canvas vuelve a ser elegible y un usuario entra dos veces en un paso en Mensaje, se registrarán dos entradas. |
| _Destinatarios únicos_ | El número de usuarios que han recibido mensajes de este paso. |
| _Evento de conversión primaria_ | El número de veces que se produjo un evento definido tras interactuar o ver un mensaje recibido de una campaña Braze. Define este evento al crear la campaña. |
| _Ingresos_ | Los ingresos totales en dólares de los destinatarios de la campaña dentro de la ventana de conversión primaria establecida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


