---
nav_title: Rafraîchir le flux
article_title: Actualisation du flux de carte de contenu pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence explique l’implémentation de cartes de contenu en actualisant votre application iOS."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Rafraîchir le flux

## Rafraîchir les cartes de contenu

Vous pouvez demander manuellement à Braze d’actualiser les cartes de contenu de l’utilisateur à l’aide de la méthode `requestContentCardsRefresh:` dans l’interface `Appboy` :
{% tabs %}
{% tab OBJECTIF-C %}

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

Pour plus d'informations, voir le `Appboy.h` [fichier d'en-tête](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
