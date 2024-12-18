---
nav_title: Suivre les événements personnalisés
article_title: Suivre les événements personnalisés pour iOS
platform: Swift
page_order: 2
description: "Cet article de référence explique comment ajouter et suivre des événements personnalisés pour le SDK Swift."

---

# Suivre les événements personnalisés

> Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord.

Avant la mise en œuvre, assurez-vous de consulter des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [meilleures pratiques]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), ainsi que nos notes sur les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Ajouter un événement personnalisé

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% endtabs %}

### Ajouter des propriétés

Vous pouvez ajouter des métadonnées sur les événements personnalisés en transmettant un `Dictionary` rempli avec des valeurs `Int`, `Double`, `String`, `Bool` ou `Date`.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logCustomEvent(
  name: "YOUR-EVENT-NAME",
  properties: [
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
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
                       properties:@{
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
{% endtabs %}

### Clés réservées {#event-reserved-keys}

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d’événement personnalisé :

- `time`
- `event_name`

## Ressources complémentaires

- Reportez-vous à la documentation de [`logCustomEvent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logcustomevent(name:properties:fileid:line:) "documentation logcustomevent") pour plus d'informations.

