---
nav_title: Rafraîchir le flux
article_title: "Rafraîchir le fil d'actualité pour Android et FireOS"
page_order: 7
platform: 
  - Android
  - FireOS
description: "Cet article de référence montre comment rafraîchir le fil d'actualité dans votre application Android ou FireOS."
channel:
  - news feed

---

# Rafraîchir le flux

> Cet article de référence montre comment rafraîchir le fil d'actualité dans votre application Android ou FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Vous pouvez mettre en file d’attente un rafraîchissement manuel du fil d'actualité Braze à tout moment en appelant :

```java
Braze.requestFeedRefresh()
```

Consultez notre [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html) pour plus d'informations.


