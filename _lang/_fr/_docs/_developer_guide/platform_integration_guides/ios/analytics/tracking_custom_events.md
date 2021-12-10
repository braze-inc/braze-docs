---
nav_title: Événements personnalisés de suivi
article_title: Suivi des événements personnalisés pour iOS
platform: iOS
page_order: 2
description: "Cet article de référence couvre comment ajouter et suivre des événements personnalisés pour votre application iOS."
---

# Suivi des événements personnalisés pour iOS

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les habitudes d'utilisation de votre application et pour segmenter vos utilisateurs par leurs actions sur le tableau de bord.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés vs. achetez des événements dans notre section [Meilleures pratiques][], ainsi que nos notes sur [les conventions de nommage d'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Ajout d'un événement personnalisé

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"VOTRE_EVENT_NAME"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("VOTRE_EVENT_NAME")
```

{% endtab %}
{% endtabs %}

### Ajout de propriétés

Vous pouvez ajouter des métadonnées sur les événements personnalisés en passant un `NSDictionary` rempli avec `NSNumber`, `NSString`, ou `valeurs NSDate`.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"VOTRE_EVENT_NAME" withProperties:@{@"key1":"value1"}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("VOTRE_EVENT_NAME", withProperties:["key1":"value1"])
```

{% endtab %}
{% endtabs %}

Consultez notre [documentation de classe][4] pour plus d'informations.

### Clés réservées {#event-reserved-keys}

Les clés suivantes sont __RESERVES__ et __NE PEUT PAS__ être utilisées comme propriétés d'événement personnalisées:

- `Heure`
- `nom_événement`

**Informations supplémentaires**

- Voir la déclaration de méthode dans le fichier [`Appboy.h`][2]. - De plus, vous pouvez vous référer à la [documentation logCustomEvent][3] pour plus d'informations.

[Meilleures pratiques]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa "logcustomevent documentation"
[4]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79 "logcustomevent:withproperties documentation"
