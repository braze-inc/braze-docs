---
nav_title: Rafraîchissement du flux
article_title: Rafraîchissement du flux de la carte de contenu pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence couvre comment implémenter le rafraîchissement de la carte de contenu dans votre application iOS."
channel:
  - cartes de contenu
---

# Rafraîchissement du flux

## Rafraîchissement des cartes de contenu

Vous pouvez demander manuellement à Braze d'actualiser les cartes de contenu de l'utilisateur en utilisant la méthode `requestContentCardsRefresh :` sur l'interface `Appboy`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestContentCardsRefresh];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestContentCardsRefresh()
```

{% endtab %}
{% endtabs %}

Pour plus d'informations, voir le fichier d'en-tête [`Appboy.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
