---
nav_title: Verfolgen von benutzerdefinierten Ereignissen
article_title: Verfolgen von benutzerdefinierten Ereignissen für iOS
platform: iOS
page_order: 2
description: "Dieser referenzierte Artikel beschreibt, wie Sie angepasste Events für Ihre iOS-Anwendung hinzufügen und tracken können."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Tracking von angepassten Events für iOS

Sie können in Braze benutzerdefinierte Ereignisse aufzeichnen, um mehr über die Nutzungsmuster Ihrer App zu erfahren und Ihre Benutzer nach ihren Aktionen auf dem Dashboard zu segmentieren.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die benutzerdefinierte Ereignisse, benutzerdefinierte Attribute und Kaufereignisse bieten, in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) sowie unsere Hinweise zu den [Namenskonventionen für Ereignisse]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

## Hinzufügen eines angepassten Events

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"YOUR_EVENT_NAME"];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.logCustomEvent("YOUR_EVENT_NAME")
```

{% endtab %}
{% endtabs %}

### Hinzufügen von Eigenschaften

Sie können Metadaten zu angepassten Events hinzufügen, indem Sie ein `NSDictionary` mit den Werten `NSNumber`, `NSString` oder `NSDate` übergeben.

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
{% tab schnell %}

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

Weitere Informationen finden Sie in unserer [Dokumentation zu den Klassen](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a4f0051d73d85cb37f63c232248124c79).

### Reservierte Schlüssel {#event-reserved-keys}

Die folgenden Schlüssel sind reserviert und können nicht als benutzerdefinierte Ereigniseigenschaften verwendet werden:

- `time`
- `event_name`

## Zusätzliche Ressourcen

- Siehe die Methodendeklaration in der [Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`. 
- Weitere Informationen finden Sie in der Dokumentation zu [`logCustomEvent`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad80c39e8c96482a77562a5b1a1d387aa).

