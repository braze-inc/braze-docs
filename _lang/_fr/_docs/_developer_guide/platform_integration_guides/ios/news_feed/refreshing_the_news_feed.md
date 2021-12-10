---
nav_title: Actualisation du flux d'actualités
article_title: Actualisation du flux d'actualités pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence montre comment actualiser le flux d'actualités dans votre application iOS."
channel:
  - fil d'actualité
---

# Actualisation du flux d'actualités

Vous pouvez demander manuellement à Braze d'actualiser le fil d'actualité de l'utilisateur dans `Appboy.h` en utilisant `- (void) requestFeedRefresh ;`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestFeedRefresh];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestFeedRefresh()
```

{% endtab %}
{% endtabs %}

Pour plus d'informations, voir le fichier d'en-tête [`Appboy.h`][15].


[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h Header File"
