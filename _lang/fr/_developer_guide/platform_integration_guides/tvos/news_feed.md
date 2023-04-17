---
nav_title: Fil d’actualité
article_title: Fil d’actualité pour vos tvOS
platform: tvOS
page_order: 10
page_type: reference
description: "Cette page explique comment récupérer et afficher les données du fil d’actualités dans votre application tvOS."

---

# Intégration du fil d’actualité

> Cet article explique comment configurer un fil d’actualité pour la plateforme tvOS.

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

## Intégration du flux tvOS

Notre SDK tvOS prend en charge la récupération des données de votre fil d’actualités, afin que vous puissiez afficher le fil d’actualité dans votre application avec votre propre interface utilisateur personnalisée. Pour récupérer le fil d’actualité, appelez les méthodes suivantes, puis analysez chaque carte en inspectant sa classe.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSArray *feedCards =  [[Appboy sharedInstance].feedController getNewsFeedCards];
```

{% endtab %}
{% tab swift %}

```swift
let feedCards = Appboy.sharedInstance()?.feedController.newsFeedCards
```

{% endtab %}
{% endtabs %}
