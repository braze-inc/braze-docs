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

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Puedes poner en cola una actualización manual del canal de noticias Braze en cualquier momento haciendo el siguiente llamado:

```java
Braze.requestFeedRefresh()
```

Consulta nuestro [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html) para más información.


