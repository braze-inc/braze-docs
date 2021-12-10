---
nav_title: Flux d'actualité
article_title: Flux d'actualité pour tvOS
platform: tvOS
page_order: 2
page_type: Référence
description: "Cette page décrit comment récupérer et afficher les données du flux de nouvelles dans votre application tvOS."
---

# Flux d'actualité

Le fil d'actualité est un flux de contenu entièrement personnalisable dans l'application pour vos utilisateurs. Notre ciblage et segmentation vous permettent de créer un flux de contenu qui est individuellement adapté aux intérêts de chaque utilisateur. Selon leur position dans le cycle de vie de l'utilisateur et la nature de votre application, Il peut s'agir d'un serveur de contenu embarqué, d'un centre de publicité, d'un centre d'accomplissement ou d'un centre d'information générique.

## Intégration des flux tvOS
Notre SDK tvOS prend en charge la récupération de vos données de flux de nouvelles, de sorte que vous pouvez afficher le fil d'actualité dans votre application avec votre propre interface utilisateur.  Pour récupérer le flux d'actualités, appeler

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSArray *feedCards = [[Appboy sharedInstance].feedController getNewsFeedCards];
```

{% endtab %}
{% tab swift %}

```swift
let feedCards = Appboy.sharedInstance()?.feedController.newsFeedCards
```

{% endtab %}
{% endtabs %}

puis analyser chaque carte en inspectant sa classe.
