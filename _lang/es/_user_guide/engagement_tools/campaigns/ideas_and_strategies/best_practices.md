---
nav_title: Buenas prácticas
article_title: Buenas prácticas de campaña
page_order: 0
description: "Este artículo proporciona las mejores prácticas para crear y personalizar sus campañas."
tool: Campaign

---

# Buenas prácticas de campaña

## Las cuatro "T" de Braze

Braze recomienda que solo envíes datos de clientes que pretendas utilizar en la plataforma Braze. Ten en cuenta la filosofía de las "Cuatro T de Braze" para asegurarte de que sólo envías los datos que vas a utilizar:

- **Dirígete a** tus audiencias creando [segmentos de audiencia]({{site.baseurl}}/user_guide/engagement_tools/segments/).
- **Active** sus mensajes con envíos [basados en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) o [activados por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).
- **Plantilla** y personaliza tus mensajes con [la lógica condicional de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid).
- **Controle** la eficacia de sus campañas con [el seguimiento de conversiones]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Esto le permite optimizar los datos que envía a Braze y agilizará su capacidad para enviar mensajes a sus usuarios, al tiempo que le garantiza que no rastreará puntos de datos que su equipo no considere útiles a largo plazo. 

## Segmentación de usuarios

Con el tiempo, a medida que desarrolle sus campañas, es posible que note lagunas en su audiencia. En este punto crucial, puedes dirigirte a tus [usuarios inactivos]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/) con una campaña especializada utilizando la segmentación. 

### Especifica tu audiencia

Aproveche los segmentos y filtros para definir su audiencia. Considere a quién van dirigidos su campaña y sus mensajes. Con esta información clave, puede crear [campañas multicanal]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-you-create-a-multichannel-campaign) que ofrezcan la flexibilidad de elaborar sus mensajes en distintos canales para adaptarse a las preferencias de notificación de su público.

También es importante conocer a tus [usuarios activos]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/) para mostrar tu agradecimiento a tus usuarios constantes.

## Campañas multicanal

### Conocimiento de las características

Si tu objetivo es atraer a tus usuarios hacia una nueva característica o versión de la aplicación, utiliza una estrategia multicanal centrada en los canales dentro de la aplicación. [Los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) y las [tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) suelen ser menos molestos si el usuario no desea actualizar inmediatamente. 

Asegúrate de incluir [vínculos en profundidad]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) a la tienda de aplicaciones adecuada.

Convencer a los usuarios para que actualicen su aplicación o cambien la forma en que la utilizan puede ser difícil, así que hágales saber todas las ventajas de la nueva versión o funciones y cómo mejorará su experiencia con su aplicación. 

### Enviar sincronización

El momento oportuno es la clave. Cuando su objetivo sea convencer a los usuarios para que actualicen su aplicación, espere a que tengan una experiencia positiva dentro de la aplicación para preguntar a los usuarios. Para mantener el interés de su público, evite los mensajes repetitivos que puedan parecer intrusivos.

Con el tiempo, es posible que sus usuarios olviden ciertas funciones o no se fijen en las nuevas. Cuando se añadan nuevas funciones, asegúrate de informar a tus usuarios con [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/). Si los usuarios no están interactuando con las principales funciones de la aplicación, puede ser mejor recordarles cuándo están interactuando con su aplicación y cuándo sería útil esta nueva función. Nuestro artículo sobre [la adhesión voluntaria de datos]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) tiene más información sobre cómo garantizar que tu solicitud coincide con las expectativas de flujo de trabajo de los usuarios. 

## Valoraciones altas

Conseguir calificaciones de cinco estrellas en la tienda de aplicaciones está en la lista de deseos de todos los profesionales del marketing móvil. Sin embargo, conseguir valoraciones positivas no es tarea fácil porque requiere un trabajo extra por parte de tus usuarios. Aplicando nuestra funcionalidad de forma inteligente, podemos ayudarte a aumentar tu interacción con los clientes.

### Segmentar usuarios avanzados

Los usuarios avanzados pueden ser defensores de tu aplicación. A menudo, interactúan con su aplicación de forma constante y pueden aportar comentarios para mejorarla. Aunque difieren de una aplicación a otra, los usuarios avanzados suelen tener lo siguiente:

- Muchas sesiones registradas
- Ha utilizado la aplicación recientemente
- Gastar dinero y hacer compras

Para conseguir mejores valoraciones, pida a sus usuarios avanzados que revisen su aplicación en la tienda de aplicaciones, ya que es más probable que tengan cosas buenas que decir. Por ejemplo, puede crear un segmento denominado "Usuarios avanzados" con estos filtros:
- Ha utilizado estas aplicaciones más de 10 veces en los últimos 14 días
- Ha gastado más de 50 dólares

![Un ejemplo de segmento dirigido a usuarios avanzados de una aplicación.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Visitar la tienda de aplicaciones lleva tiempo a tus usuarios. Para maximizar la probabilidad de que hagan un esfuerzo adicional, pídales una valoración o reseña después de que hayan tenido una experiencia positiva con su aplicación. Por ejemplo, pregúnteles después de superar un nivel del juego o de realizar una compra utilizando un código de descuento. Nuestro artículo sobre [la inclusión voluntaria de datos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) contiene más información sobre las formas de garantizar que su solicitud coincide con las expectativas del flujo de trabajo de los usuarios.

## Programar tus campañas

Cuando edites programas de campaña o audiencias, toma nota de las siguientes buenas prácticas:

- **Campañas de programación única:** Puedes editar la campaña hasta la hora de envío programada.
- **Campañas programadas recurrentes:** Puedes editar la campaña hasta la hora de envío programada.
- **Campañas locales de tiempo de envío:** No hagas ediciones 24 horas antes de la hora de envío programada.
- **Campañas con tiempo de envío óptimo:** No hagas ediciones 24 horas antes de la medianoche del día previsto para el envío de la campaña.

{% alert note %}
Editar una campaña en vivo y cambiar la entrega a **Hora de envío local** hará que se ponga en cola un nuevo lote de mensajes, lo que significa que tus usuarios recibirán el mensaje dos veces debido a que el mensaje se pondrá en cola dos veces. Para evitarlo, primero detén la campaña original y luego lanza un duplicado tras actualizar la programación.
{% endalert %}

