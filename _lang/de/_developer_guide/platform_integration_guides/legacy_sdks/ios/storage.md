---
nav_title: Lagerung
article_title: Speicher für iOS
platform: iOS
page_order: 8.9
page_type: reference
description: "Dieser Referenzartikel beschreibt die Eigenschaften auf Geräteebene, die vom Braze iOS SDK erfasst werden."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Lagerung

Dieser Artikel beschreibt die verschiedenen Eigenschaften auf Geräteebene, die bei der Verwendung des Braze iOS SDK erfasst werden.

## Eigenschaften des Geräts

Standardmäßig erfasst Braze die folgenden [Eigenschaften auf Geräteebene](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181), um die Personalisierung von Nachrichten auf der Grundlage von Gerät, Sprache und Zeitzone zu ermöglichen:

* Gerät Auflösung
* Netzbetreiber des Geräts
* Gebietsschema des Geräts
* Gerätemodell
* Betriebssystemversion
* IDFV (optional mit [iOS SDK v5.7.0+](https://github.com/braze-inc/braze-swift-sdk))
* Push aktiviert
* Zeitzone des Geräts
* Push-Authentifizierungsstatus
* Ad-Tracking aktiviert

{% alert note %}
Der Braze SDK sammelt IDFA nicht automatisch. Apps können optional IDFA an Braze weitergeben, indem sie unser `ABKIDFADelegate`-Protokoll implementieren. Apps müssen das ausdrückliche Opt-in des Endnutzers für das Tracking über das App-Tracking-Transparenz-Framework einholen, bevor sie IDFA an Braze weitergeben.
{% endalert %}

Konfigurierbare Felder des Geräts sind in der enum [`ABKDeviceOptions`](https://github.com/Appboy/appboy-ios-sdk/blob/4390e9eac8401bccdb81b053fa54eb87b1f6fcaa/Appboy-tvOS-SDK/AppboyTVOSKit.framework/Headers/Appboy.h#L179) definiert. Um das Feld des Geräts, das Sie in der Liste zulassen möchten, zu deaktivieren oder zu spezifizieren, weisen Sie das bitwise `OR` der gewünschten Felder zu [`ABKDeviceAllowlistKey`](https://github.com/Appboy/appboy-ios-sdk/blob/fed071000722673754da288cace15c1ff8aca432/AppboyKit/include/Appboy.h#L148) in `appboyOptions` von `startWithApiKey:inApplication:withAppboyOptions:` zu.

Um zum Beispiel die Zeitzone und die Gebietsschemasammlung zuzulassen, setzen Sie:
```
appboyOptions[ABKDeviceAllowlistKey] = @(ABKDeviceOptionTimezone | ABKDeviceOptionLocale);
```

Standardmäßig sind alle Felder aktiviert. Beachten Sie, dass ohne einige Eigenschaften nicht alle Features ordnungsgemäß funktionieren werden. Zum Beispiel funktioniert die Zustellung zur Ortszeit nicht ohne die Zeitzone.

Mehr über die automatisch erfassten Geräteeigenschaften zu erfahren Sie unter [SDK-Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 
