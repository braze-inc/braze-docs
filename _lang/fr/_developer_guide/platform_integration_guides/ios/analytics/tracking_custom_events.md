---
nav_title: Suivre les événements personnalisés
article_title: Suivre les événements personnalisés pour iOS
platform: iOS
page_order: 2
description: "Cet article de référence explique comment ajouter et suivre des événements personnalisés pour votre application iOS."

---

{% multi_lang_include deprecations/objective-c.md %}

# Suivre les événements personnalisés pour iOS

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord.

Avant l’implémentation, assurez-vous d’étudier des exemples d’options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d’achat dans nos [meilleures pratiques][0] ainsi que nos remarques sur les [conventions de dénominations des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Ajouter un événement personnalisé

{% tabs %}
{% tab OBJECTIVE-C %}

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
{% tab OBJECTIVE-C %}

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

Reportez-vous à notre [documentation de classes][4] pour plus d’informations.

### Clés réservées {#event-reserved-keys}

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés de l’événement personnalisées :

- `time`
- `event_name`

## Ressources complémentaires

- Voir la déclaration de méthode dans le [fichier][2] `Appboy.h`. 
- Reportez-vous à la documentation [`logCustomEvent`][3] pour plus d’informations.

[0]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa "logcustomevent documentation"
[4]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79 "logcustomevent:withproperties documentation"
