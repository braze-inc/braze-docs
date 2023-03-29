---
nav_title: Rafraîchir le flux
article_title: Rafraîchir le fil d'actualité pour Android et FireOS
page_order: 7
platform: 
  - Android
  - FireOS
description: "Cet article de référence montre comment rafraîchir le fil d'actualité dans votre application Android ou FireOS."
channel:
  - fil d’actualité

---

# Rafraîchir le flux

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Vous pouvez mettre en file d’attente un rafraîchissement manuel du fil d'actualité Braze à tout moment en appelant :

```java
Braze.requestFeedRefresh()
```

Consultez notre [KDoc][16] pour plus d’informations.


[16]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html
