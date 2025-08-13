---
nav_title: Standort-Tracking
article_title: Standort-Tracking für iOS
platform: iOS
page_order: 6
description: "Dieser Artikel zeigt, wie Sie das Standort-Tracking für Ihre iOS-Anwendung konfigurieren."
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Standort-Tracking für iOS

Standardmäßig deaktiviert Braze das Standort-Tracking. Wir aktivieren das Standort-Tracking, nachdem sich die Host-Anwendung für das Standort-Tracking entschieden und die Erlaubnis des Nutzers eingeholt hat. Wenn er/sie dem Standort-Tracking zugestimmt hat, protokolliert Braze beim Start der Sitzung einen einzigen Standort für jeden Nutzer.

{% alert important %}
Damit das Standort-Tracking in iOS 14 auch für den ungefähren Standort zuverlässig funktioniert, müssen Sie Ihr SDK mindestens auf die Version `3.26.1` aktualisieren.
{% endalert %}

## Automatisches Standort-Tracking aktivieren

Ab Braze iOS SDK `v3.17.0` ist das Standort-Tracking standardmäßig deaktiviert. Sie können das automatische Standort-Tracking über die Datei `Info.plist` aktivieren. Fügen Sie das Wörterbuch `Braze` zu Ihrer Datei `Info.plist` hinzu. Fügen Sie im Wörterbuch `Braze` den booleschen Untereintrag `EnableAutomaticLocationCollection` hinzu und setzen Sie den Wert auf `YES`. Beachten Sie, dass vor Braze iOS SDK v4.0.2 der Wörterbuchschlüssel `Appboy` anstelle von `Braze` verwendet werden muss.

Sie können das automatische Standort-Tracking beim Start der App auch über die Methode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). Setzen Sie im Wörterbuch `appboyOptions` `ABKEnableAutomaticLocationCollectionKey` auf `YES`. Zum Beispiel:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableAutomaticLocationCollectionKey : @(YES) }];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableAutomaticLocationCollectionKey : true ])
```

{% endtab %}
{% endtabs %}

### Übergabe von Standort-Daten an Braze

Die folgenden beiden Methoden können verwendet werden, um den letzten bekannten Standort manuell festzulegen.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy];

```

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy
                                                      altitude:altitude
                                              verticalAccuracy:verticalAccuracy];

```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy)
```

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy, altitude: altitude, verticalAccuracy: verticalAccuracy)
```

{% endtab %}
{% endtabs %}

Refernzieren Sie unter [`ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKUser.h) für weitere Informationen.

