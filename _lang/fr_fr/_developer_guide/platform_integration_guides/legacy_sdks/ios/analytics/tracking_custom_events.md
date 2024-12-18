---
nav_title: Suivre les événements personnalisés
article_title: Suivre les événements personnalisés pour iOS
platform: iOS
page_order: 2
description: "Cet article de référence explique comment ajouter et suivre des événements personnalisés pour votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Suivre les événements personnalisés pour iOS

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord.

Avant la mise en œuvre, assurez-vous de consulter des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [meilleures pratiques]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), ainsi que nos notes sur les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Ajouter un événement personnalisé

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("YOUR_EVENT_NAME")
```

{% endtab %}
{% endtabs %}

### Ajouter des propriétés

Vous pouvez ajouter des métadonnées sur les événements personnalisés en passant un `NSDictionary` renseigné avec `NSNumber`, `NSString`, ou `NSDate` valeurs.

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR-EVENT-NAME"
                         withProperties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent(
  "YOUR-EVENT-NAME",
  withProperties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```

{% endtab %}
{% endtabs %}

Pour plus d'informations, consultez la documentation de notre [classelogcustomevent](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79 ":withproperties").

### Clés réservées {#event-reserved-keys}

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d’événement personnalisé :

- `time`
- `event_name`

## Ressources complémentaires

- Voir la déclaration de la méthode dans le [fichier](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`. 
- Reportez-vous à la documentation de [`logCustomEvent`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa "documentation logcustomevent") pour plus d'informations.

