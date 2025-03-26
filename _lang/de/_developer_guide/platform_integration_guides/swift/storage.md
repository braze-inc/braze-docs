---
nav_title: Lagerung
article_title: Speicher für iOS
platform: Swift
page_order: 8.9
page_type: reference
description: "Dieser Referenzartikel beschreibt die Eigenschaften auf Geräteebene, die vom Braze iOS Swift SDK erfasst werden."
---

# Lagerung

> Dieser Artikel beschreibt die verschiedenen Eigenschaften auf Geräteebene, die bei der Verwendung des Braze iOS Swift SDK erfasst werden.

## Eigenschaften des Geräts

Standardmäßig erfasst Braze die folgenden [Eigenschaften auf Geräteebene](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty), um die Personalisierung von Nachrichten nach Gerät, Sprache und Zeitzone zu ermöglichen:

* Netzbetreiber des Geräts (siehe Hinweis, dass [`CTCarrier` veraltet](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier) ist)
* Gebietsschema des Geräts
* Gerätemodell
* Betriebssystemversion
* Push-Autorisierungsstatus
* Push Display Optionen
* Push aktiviert
* Gerät Auflösung
* Zeitzone des Geräts

{% alert note %}
Der Braze SDK sammelt IDFA nicht automatisch. Apps können optional die IDFA an Braze weitergeben, indem sie die nachfolgenden Methoden direkt implementieren. Apps müssen das ausdrückliche Opt-in für das Tracking durch den Endnutzer über das App Tracking Transparency Framework einholen, bevor sie die IDFA an Braze weitergeben.

1. Um den Status des Werbe-Trackings festzulegen, verwenden Sie [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Um die IDFA (Identifier for Advertisers ) festzulegen, verwenden Sie [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}

Die konfigurierbaren Felder des Geräts sind in der enum [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty) definiert. Um das Feld, das Sie in der Liste zulassen möchten, zu deaktivieren oder zu spezifizieren, fügen Sie die Felder der Eigenschaft [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) Eigenschaft des `configuration`-Objekts hinzu.

Um zum Beispiel die Erfassung der Zeitzone und des Gebietsschemas zuzulassen:

{% tabs %}
{% tab schnell %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endtab %}
{% endtabs %}

Standardmäßig sind alle Felder aktiviert. Beachten Sie, dass ohne bestimmte Eigenschaften nicht alle Features ordnungsgemäß funktionieren. Zum Beispiel funktioniert die Zustellung zur Ortszeit nicht ohne die Zeitzone.

Mehr über die automatisch erfassten Geräteeigenschaften zu erfahren Sie unter [Datenerfassung mit SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).

