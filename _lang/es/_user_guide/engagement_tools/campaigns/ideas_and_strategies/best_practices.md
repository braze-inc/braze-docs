---
nav_title: Buenas prácticas
article_title: Buenas prácticas de campaña
page_order: 0
description: "Este artículo proporciona las mejores prácticas para crear y personalizar tus campañas."
tool: Campaign

---

# Mejores prácticas de campaña

## Las cuatro "T" del Braze

Braze recomienda que sólo envíes datos de clientes que pretendas utilizar en la plataforma Braze. Ten en cuenta la filosofía de las "Cuatro T de Braze" para asegurarte de que sólo envías los datos que vas a utilizar:

- **Dirígete a** tus audiencias creando [segmentos de público]({{site.baseurl}}/user_guide/engagement_tools/segments/).
- **Desencadena** tus mensajes con una entrega [basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) o [desencadenada por la API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).
- **Plantilla** y personaliza tus mensajes con [la lógica condicional Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid).
- **Sigue** la eficacia de tus campañas con [el seguimiento de la conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Esto te permite optimizar los datos que envías a Braze y agilizará tu capacidad para enviar mensajes a tus usuarios, a la vez que garantiza que no haya puntos de datos de seguimiento que tu equipo no considere útiles a largo plazo. 

## Segmentación de usuarios

A medida que desarrolles tus campañas, es posible que notes lagunas en tu audiencia. En este punto crucial, puedes dirigirte a tus [usuarios rezagados]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/) con una campaña especializada utilizando la segmentación. 

### Identifica a tu audiencia

Aprovecha los segmentos y filtros para definir tu audiencia. Ten en cuenta a quién van dirigidos tu campaña y tus mensajes. Con esta información clave, puedes crear [campañas multicanal]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-you-create-a-multichannel-campaign) que ofrezcan la flexibilidad de construir tus mensajes en diferentes canales para adaptarse a las preferencias de notificación de tu audiencia.

También es importante conocer a tus [usuarios activos]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/) para mostrar tu agradecimiento a tus usuarios constantes.

## Campañas multicanal

### Conocimiento de las características

Si tu objetivo es atraer a tus usuarios hacia una nueva característica o versión de la aplicación, utiliza una estrategia multicanal centrada en los canales dentro de la aplicación. [Los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) y las [tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) suelen ser menos molestos si el usuario no desea actualizar inmediatamente. 

Asegúrate de incluir [vínculos en profundidad]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) a la tienda de aplicaciones adecuada.

Convencer a los usuarios para que actualicen su aplicación o cambien la forma en que utilizan tu aplicación puede ser difícil, así que hazles saber todas las ventajas de la nueva versión o características y cómo mejorará su experiencia con tu aplicación. 

### Enviar sincronización

¡El momento oportuno es la clave! Cuando tu objetivo sea convencer a los usuarios para que actualicen su aplicación, espera a que tengan una experiencia positiva dentro de la aplicación para preguntar a los usuarios. Para mantener la interacción de tu audiencia, evita la mensajería repetitiva que pueda parecer intrusiva.

Con el tiempo, tus usuarios pueden olvidar ciertas características o no darse cuenta de nuevas características. Cuando se añadan nuevas características, asegúrate de informar a tus usuarios con [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/). Si los usuarios no están interactuando con las principales características de la aplicación, quizá sea mejor recordarles cuándo están interactuando con tu aplicación y cuándo sería útil esta nueva característica. Nuestro artículo sobre [la adhesión voluntaria de datos]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) tiene más información sobre cómo garantizar que tu solicitud coincide con las expectativas de flujo de trabajo de los usuarios. 

## Altas tasas

Conseguir puntuaciones de cinco estrellas en la tienda de aplicaciones está en la lista de deseos de todo especialista en marketing móvil. Sin embargo, conseguir valoraciones positivas no es tarea fácil porque requiere un trabajo extra por parte de tus usuarios. Aplicando nuestra funcionalidad de forma inteligente, podemos ayudarte a aumentar tu interacción con los clientes.

### Dirigirse a usuarios avanzados

Los usuarios avanzados pueden ser defensores de tu aplicación. A menudo, interactúan con tu aplicación de forma constante y pueden aportar comentarios para mejorarla. Aunque difieren de una aplicación a otra, los usuarios avanzados suelen tener lo siguiente:

- Muchas sesiones registradas
- He utilizado la aplicación recientemente
- Gastar dinero y hacer compras

Para asegurarte unas tasas más altas, pide a tus usuarios avanzados que revisen tu aplicación en la tienda de aplicaciones, ya que es más probable que tengan cosas buenas que decir. Por ejemplo, podrías crear un segmento llamado "Usuarios avanzados" con estos filtros:
- Ha utilizado estas aplicaciones más de 10 veces en los últimos 14 días
- Ha gastado más de 50 dólares

Ejemplo de segmento dirigido a usuarios avanzados de una aplicación.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Visitar la tienda de aplicaciones lleva tiempo a tus usuarios. Para maximizar la probabilidad de que hagan un esfuerzo adicional, pide una valoración o una reseña después de que hayan tenido una experiencia positiva con tu aplicación. Por ejemplo, pregúntales después de superar un nivel del juego o de hacer una compra utilizando un código de descuento. Nuestro artículo sobre [la adhesión voluntaria de datos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) tiene más información sobre las formas de garantizar que tu solicitud coincide con las expectativas de flujo de trabajo de los usuarios.

## Programar tus campañas

Cuando edites programas de campaña o audiencias, toma nota de las siguientes buenas prácticas:

- **Campañas de programación única:** Puedes editar la campaña hasta la hora de envío programada.
- **Campañas programadas recurrentes:** Puedes editar la campaña hasta la hora de envío programada.
- **Campañas locales de tiempo de envío:** No hagas ediciones 24 horas antes de la hora de envío programada.
- **Campañas con tiempo de envío óptimo:** No hagas ediciones 24 horas antes de la medianoche del día previsto para el envío de la campaña.

{% alert note %}
Editar una campaña en vivo y cambiar la entrega a **Hora de envío local** hará que se ponga en cola un nuevo lote de mensajes, lo que significa que tus usuarios recibirán el mensaje dos veces debido a que el mensaje se pondrá en cola dos veces. Para evitarlo, primero detén la campaña original y luego lanza un duplicado tras actualizar la programación.
{% endalert %}

