---
nav_title: Pares clave-valor
article_title: Pares clave-valor de fuentes de noticias para la Web
platform: Web
page_order: 1
page_type: reference
description: "Este artículo explica cómo utilizar pares clave-valor en tus tarjetas de canal de noticias a través del SDK de Braze."
channel: news feed

---

# Pares clave-valor

> Este artículo explica cómo utilizar pares clave-valor en tus tarjetas de canal de noticias a través del SDK de Braze.

{% alert note %}
Vamos a dejar de usar el canal de noticias. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

Los objetos `Card` pueden llevar opcionalmente pares clave-valor como `extras`. Se pueden utilizar para enviar datos hacia abajo junto con una tarjeta para su posterior manipulación por la aplicación. Llama a `card.extras` para acceder a estos valores.

Consulta los JSDocs para obtener más información sobre [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) y [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html).

