---
nav_title: Badges
article_title: Badges de fil d’actualité pour Android et FireOS
page_order: 3.2
platform: 
  - Android
  - FireOS
description: "Cet article de référence montre comment ajouter des badges de fil d’actualité et demander le nombre de cartes de fil d’actualité non lues à votre application Android ou FireOS."
channel:
  - news feed
  
---

# Badges

> Cet article de référence montre comment ajouter des badges de fil d’actualité et demander le nombre de cartes de fil d’actualité non lues à votre application Android ou FireOS.

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

## Demande de décompte de cartes de fil d’actualité non lues

Vous pouvez à tout moment demander le nombre de cartes non lues en appelant :

```java
getUnreadCardCount()
```

Pour plus d’informations, reportez-vous à notre [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-feed-updated-event/get-unread-card-count.html).

