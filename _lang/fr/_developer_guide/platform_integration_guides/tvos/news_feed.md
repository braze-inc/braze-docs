---
nav_title: Fil d’actualité
article_title: Fil d’actualité pour vos tvOS
platform: tvOS
page_order: 10
page_type: reference
description: "Cette page explique comment récupérer et afficher les données du fil d’actualités dans votre application tvOS."

---

# Fil d’actualité

Le fil d’actualités est un fil de contenu in-app entièrement personnalisable pour vos utilisateurs. Notre ciblage et notre segmentation vous permettent de créer un fil de contenu individuel, adapté aux intérêts de chaque utilisateur. Selon leur position dans le cycle de vie de l’utilisateur et la nature de votre application, il peut s’agir d’un serveur de contenu d’onboarding, d’un centre de publicité, de réalisation ou d’actualités génériques.

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
