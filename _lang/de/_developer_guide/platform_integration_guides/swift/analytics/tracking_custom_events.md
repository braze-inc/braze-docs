---
nav_title: Verfolgen von benutzerdefinierten Ereignissen
article_title: Verfolgen von benutzerdefinierten Ereignissen für iOS
platform: Swift
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Events für das Swift SDK hinzufügen und tracken können."

---

# Tracking von angepassten Events

> Sie können in Braze benutzerdefinierte Ereignisse aufzeichnen, um mehr über die Nutzungsmuster Ihrer App zu erfahren und Ihre Benutzer nach ihren Aktionen auf dem Dashboard zu segmentieren.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die benutzerdefinierte Ereignisse, benutzerdefinierte Attribute und Kaufereignisse bieten, in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) sowie unsere Hinweise zu den [Namenskonventionen für Ereignisse]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Hinzufügen eines angepassten Events

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% endtabs %}

### Hinzufügen von Eigenschaften

Sie können Metadaten zu angepassten Events hinzufügen, indem Sie ein `Dictionary` mit den Werten `Int`, `Double`, `String`, `Bool` oder `Date` übergeben.

{% tabs %}
{% tab schnell %}

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
{% tab OBJECTIVE-C %}

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

### Reservierte Schlüssel {#event-reserved-keys}

Die folgenden Schlüssel sind reserviert und können nicht als benutzerdefinierte Ereigniseigenschaften verwendet werden:

- `time`
- `event_name`

## Zusätzliche Ressourcen

- Siehe dazu die [`logCustomEvent`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logcustomevent(name:properties:fileid:line:) "logcustomevent Dokumentation") für weitere Informationen.

