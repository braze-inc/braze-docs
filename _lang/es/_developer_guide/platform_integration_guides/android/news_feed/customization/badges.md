---
nav_title: Señales
article_title: Insignias de fuentes de noticias para Android y FireOS
page_order: 3.2
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia explica cómo añadir señales de canal de noticias y solicitar recuentos de tarjetas de canal de noticias no leídas a tu aplicación Android o FireOS."
channel:
  - news feed
  
---

# Señales

> Este artículo de referencia explica cómo añadir señales de canal de noticias y solicitar recuentos de tarjetas de canal de noticias no leídas a tu aplicación Android o FireOS.

{% alert note %}
Vamos a dejar de usar el canal de noticias. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Solicitar recuentos de tarjetas de canal de noticias no leídas

Puedes solicitar el número de tarjetas no leídas en cualquier momento llamando por teléfono:

```java
getUnreadCardCount()
```

Consulta nuestro [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-feed-updated-event/get-unread-card-count.html) para más información.

