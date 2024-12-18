---
nav_title: Migración desde el canal de noticias
article_title: Migración desde el canal de noticias
page_order: 10
description: "Este artículo de referencia proporciona orientación sobre la migración del canal de noticias a las tarjetas de contenido de Braze."
channel:
  - content cards
  - news feed
  
---

# Migración del canal de noticias a las tarjetas de contenido

{% alert note %}
Vamos a dejar de usar el canal de noticias. Braze recomienda a los clientes que utilizan nuestra herramienta News Feed que se pasen a nuestro canal de mensajería Content Cards: es más flexible, personalizable y fiable.
{% endalert %}

> Pasar del canal de noticias a las tarjetas de contenido lleva tiempo, ¡pero es fácil! No se puede migrar automáticamente el contenido de News Feed a Content Cards: hay que integrar Content Cards desde cero. Sin embargo, con la nueva flexibilidad de las Tarjetas de contenido, no creemos que lo eches de menos ni que te importe.

Póngase en contacto con su gestor de cuentas Braze para obtener más información.

## Características y funciones

Las tarjetas de contenido ofrecen muchas funciones que no admite el canal de noticias, por ejemplo, opciones de entrega adicionales, como la entrega basada en acciones y API, y análisis mejorados, como el seguimiento de conversiones.

Al planificar la migración de la fuente de noticias a las tarjetas de contenido, es importante tener en cuenta las principales diferencias entre las tarjetas de contenido y la fuente de noticias:

- **Segmentación:** La segmentación de las tarjetas de contenido puede evaluarse en el momento en que se envían los mensajes o en el momento en que la tarjeta se visualiza por primera vez. La segmentación del canal de noticias se evalúa en el momento en que se ven las tarjetas del canal de noticias.
- **Personalización:** La personalización de las tarjetas de contenido puede planificarse en el momento en que se envían los mensajes o en el momento en que la tarjeta se visualiza por primera vez. La personalización de las tarjetas de noticias se planifica en el momento en que se visualizan las tarjetas de noticias.

En la tabla siguiente se describen las diferencias entre las características del canal de noticias y las tarjetas de contenido:

| Característica | Canal de noticias | Tarjetas de contenido |
|---|---|---|
| Campañas multivariantes y multicanal | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-check" title="Con soporte"></i> |
| Entrega programada, basada en acciones y basada en API | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-check" title="Con soporte"></i> |
| Mensajes creados por la API | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-check" title="Con soporte"></i> |
| Pruebas A/B | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-check" title="Con soporte"></i> |
| [Descartar y fijar tarjetas][4] | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-check" title="Con soporte"></i> |
| [Análisis enriquecido][3] (por ejemplo, seguimiento de conversiones) | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-check" title="Con soporte"></i> |
| [Disponible en Canvas][2] | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-check" title="Con soporte"></i> |
| [Contenido conectado][5] | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-check" title="Con soporte"></i> |
| Personalización y segmentación | Plantilla en impresión | Plantilla de envío o primera impresión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Aplicación

- Las tarjetas de contenido y la fuente de noticias son productos separados, por lo que es necesaria una integración sencilla para su aplicación o sitio web con el fin de utilizar las tarjetas de contenido.
- Si lo deseas, las tarjetas del canal de noticias existentes tendrán que migrarse manualmente a campañas de tarjeta de contenido cuando realices el cambio.
- Las tarjetas de contenido no están pensadas para utilizarse al mismo tiempo que el canal de noticias, ya que son un sustituto de este último.
- Actualmente, las tarjetas de contenido no admiten categorías. Las categorías se pueden conseguir mediante [personalización y pares clave-valor][1].


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
