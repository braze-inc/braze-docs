---
nav_title: Rafraîchir le flux
article_title: Actualisation du fil d’actualité pour iOS
platform: iOS
page_order: 6
description: "Cet article de référence montre comment actualiser le fil d’actualité dans votre application iOS."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Actualisation du fil d’actualités

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Vous pouvez demander manuellement à Braze d’actualiser le fil d’actualité de l’utilisateur dans `Appboy.h` en utilisant `- (void) requestFeedRefresh;`. Par exemple :

{% tabs %}
{% tab OBJECTIF-C %}

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

Pour plus d'informations, consultez le `Appboy.h` [fichier d'en-tête](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.hFichier d'en-Tête").


