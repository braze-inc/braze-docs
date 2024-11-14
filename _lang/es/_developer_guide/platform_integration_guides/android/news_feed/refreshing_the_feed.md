---
nav_title: Actualizar el canal
article_title: Actualizar la fuente de noticias para Android y FireOS
page_order: 7
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia muestra cómo actualizar la fuente de noticias en tu aplicación Android o FireOS."
channel:
  - news feed

---

# Actualizar la fuente

> Este artículo de referencia muestra cómo actualizar la fuente de noticias en tu aplicación Android o FireOS.

{% alert note %}
Vamos a dejar de usar el canal de noticias. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

Puedes poner en cola una actualización manual del canal de noticias Braze en cualquier momento haciendo el siguiente llamado:

```java
Braze.requestFeedRefresh()
```

Consulta nuestro [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html) para más información.


