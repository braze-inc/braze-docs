---
nav_title: Standorte &amp; Geoofences
article_title: Standort &amp; Geofences für iOS
platform: iOS
page_order: 6
description: "Dieser Referenzartikel beschreibt, wie Sie Standorte und Geofences in Ihrer iOS-Anwendung implementieren."
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Standorte und Geoofences

Zur Unterstützung von Geofences für iOS:

1. Ihre Integration muss Push-Benachrichtigungen im Hintergrund unterstützen.
2. Braze Geofences [müssen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/#enabling-automatic-location-tracking) über das SDK aktiviert werden, entweder implizit durch Aktivieren der Standorterfassung oder explizit durch Aktivieren der Geofence-Erfassung. Sie sind standardmäßig nicht aktiviert.

{% alert important %}
Ab iOS 14 funktionieren Geoofences nicht mehr zuverlässig für Nutzer, die lediglich ihren ungefähren Standort angeben möchten.
{% endalert %}

## Schritt 1: Push im Hintergrund aktivieren

Um unsere Strategie zur Synchronisierung von Geofence vollständig nutzen zu können, müssen Sie zusätzlich zur standardmäßigen Push-Integration die [Hintergrund-Push-Funktion]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#use-silent-remote-notifications-to-trigger-background-work) aktivieren.

## Schritt 2: Geofences aktivieren

Abhängig davon, ob die automatische Standorterfassung aktiviert ist, sind GeoFences standardmäßig aktiviert. Sie können Geofences über die Datei `Info.plist` aktivieren. Fügen Sie das Wörterbuch `Braze` zu Ihrer Datei `Info.plist` hinzu. Fügen Sie im Wörterbuch `Braze` den booleschen Untereintrag `EnableGeofences` hinzu und setzen Sie den Wert auf `YES`. Beachten Sie, dass vor Braze iOS SDK v4.0.2 der Wörterbuchschlüssel `Appboy` anstelle von `Braze` verwendet werden muss.

Sie können Geofences auch beim Start der App aktivieren, indem Sie die [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) Methode. Setzen Sie im Wörterbuch `appboyOptions` `ABKEnableGeofencesKey` auf `YES`. Zum Beispiel:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## Schritt 3: Auf Braze Background-Push prüfen

Braze synchronisiert Geofences mit Geräten über Push-Benachrichtigungen im Hintergrund. Befolgen Sie den Artikel zur [iOS-Anpassung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push/), um sicherzustellen, dass Ihre Anwendung keine unerwünschten Aktionen ausführt, wenn Sie Braze-Benachrichtigungen zur Geofence-Synchronisierung erhalten.

## Schritt 4: Fügen Sie NSLocationAlwaysUsageDescription zu Ihrem Info.plist

Fügen Sie `info.plist` die Schlüssel `NSLocationAlwaysUsageDescription` und `NSLocationAlwaysAndWhenInUseUsageDescription` mit einem `String`-Wert hinzu, der beschreibt, warum Ihre Anwendung den Standort tracken muss. Beide Schlüssel sind ab iOS 11 erforderlich.
Diese Beschreibung wird angezeigt, wenn die Standortabfrage des Systems eine Autorisierung verlangt, und sollte Ihren Benutzern die Vorteile der Standortverfolgung deutlich erklären.

## Schritt 5: Freigabe vom Nutzer anfordern

Das Feature "Geofences" ist nur funktionsfähig, wenn die Standortfreigabe auf `Always` festgelegt ist.

Verwenden Sie den folgenden Code, um die Standortfreigabe `Always` anzufordern:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## Schritt 6: Aktivieren Sie Geofences auf dem Dashboard

Unter iOS können nur bis zu 20 Geofences für eine bestimmte App gespeichert werden. Durch die Verwendung von Standorten werden einige dieser 20 verfügbaren Geofence-Slots verbraucht. Um eine versehentliche oder unerwünschte Unterbrechung anderer geofence-bezogener Funktionen in Ihrer App zu verhindern, müssen Standort-Geofences für einzelne Apps auf dem Dashboard aktiviert werden.

Damit die Ortung korrekt funktioniert, sollten Sie außerdem sicherstellen, dass Ihre App nicht alle verfügbaren Geofence-Punkte nutzt.

### Aktivieren Sie Geofences auf der Seite Standorte:

![Die Geofence-Optionen auf der Seite Standorte von Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Aktivieren Sie Geofences auf der Einstellungsseite:

![Das Geofence-Kontrollkästchen auf den Braze-Einstellungsseiten.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Deaktivieren von automatischen Geofence-Anfragen

Ab iOS SDK Version 3.21.3 können Sie automatische Geofences-Anfragen deaktivieren. Verwenden Sie hierzu die Datei `Info.plist`. Fügen Sie das Wörterbuch `Braze` zu Ihrer Datei `Info.plist` hinzu. Fügen Sie im Wörterbuch `Braze` den booleschen Untereintrag `DisableAutomaticGeofenceRequests` hinzu und setzen Sie den Wert auf `YES`.

Über die Methode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) können automatische Geofence-Anfragen auch zur Startzeit der App deaktiviert werden. Setzen Sie im Wörterbuch `appboyOptions` `ABKDisableAutomaticGeofenceRequestsKey` auf `YES`. Zum Beispiel:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

Wenn Sie sich für diese Option entscheiden, müssen Sie die Geofences manuell anfragen, damit das Feature funktioniert.

## Geofencing manuell anfordern

Wenn das Braze SDK Geofences zur Überwachung aus dem Backend anfragt, meldet es den aktuellen Nutrzerstandort und erhält Geofences, die auf der Grundlage des gemeldeten Standorts als optimal relevant eingestuft werden. Es gibt ein Rate-Limit von einer Geofence-Aktualisierung pro Sitzung.

Um den Standort zu kontrollieren, den das SDK für den Empfang der relevantesten Geofences meldet, können Sie ab iOS SDK Version 3.21.3 Geofences manuell anfragen, indem Sie den Breiten- und Längengrad eines Standorts angeben. Es wird empfohlen, bei Verwendung dieser Methode automatische Geofence-Anfragen zu deaktivieren. Verwenden Sie dazu den folgenden Code:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}


