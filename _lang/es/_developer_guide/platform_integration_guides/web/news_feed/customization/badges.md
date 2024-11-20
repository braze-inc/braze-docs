---
nav_title: Señales
article_title: Insignias de fuentes de noticias para Web
platform: Web
page_order: 3
page_type: reference
description: "Este artículo explica cómo solicitar el recuento de tarjetas de canales de noticias no leídos y utilizar esa información para alimentar las señales de tu aplicación Web."
channel: news feed

---

# Señales

> Este artículo explica cómo solicitar el recuento de tarjetas de canales de noticias no leídos y utilizar esa información para alimentar las señales de tu aplicación Web.

{% alert note %}
Vamos a dejar de usar el canal de noticias. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Solicitar recuentos de tarjetas de canal de noticias no leídas

Puedes solicitar el número de tarjetas no leídas en cualquier momento llamando por teléfono:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

Suele utilizarse para activar señales que indican cuántas tarjetas de canal de noticias hay sin leer. Consulta [los JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html) para más información. Ten en cuenta que Braze no actualizará las tarjetas de canal de noticias al cargar una nueva página (y, por tanto, esta función devolverá 0) hasta que muestres la fuente o llames a `braze.requestFeedRefresh();`

