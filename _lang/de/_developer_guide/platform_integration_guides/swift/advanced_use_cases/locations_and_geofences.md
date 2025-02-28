---
nav_title: Standorte und Geoofences
article_title: Standorte und Geofences für iOS
platform: Swift
page_order: 4
description: "Dieser Referenzartikel beschreibt, wie Sie Standorte und Geofences in das Swift SDK implementieren."
Tool:
  - Location

---

# Standorte und Geoofences

> Dieser Artikel behandelt die Einrichtung von Geofences für Ihre iOS SDK-Integration. Geofences sind nur in ausgewählten Braze Paketen verfügbar. Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, um loszulegen.

Das Kernstück des Realtime-Standortangebots von Braze ist das Konzept des [Geofence]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences). Ein Geofence ist ein virtuelles geografisches Gebiet, das als Breiten- und Längengrad in Kombination mit einem Radius dargestellt wird und einen Kreis um eine bestimmte globale Position bildet.

{% alert important %}
Ab iOS 14 funktionieren Geoofences nicht mehr zuverlässig für Nutzer, die ihren ungefähren Standort angeben möchten.
{% endalert %}

## Schritt 1: Push im Hintergrund aktivieren

Um unsere Strategie zur Geofence-Synchronisierung vollständig nutzen zu können, müssen Sie zusätzlich zur Standard-Push-Integration die [stillen Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) aktivieren.

## Schritt 2: Braze Standortdienste aktivieren
Die Standortdienste von Braze müssen über das SDK [aktiviert werden](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/). Sie sind standardmäßig nicht aktiviert.

## Schritt 3: Geofences aktivieren

Aktivieren Sie Geofences, indem Sie `location.geofencesEnabled` auf `true` für das Objekt `configuration` setzen, das die Instanz initialisiert.[`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) Instanz. Weitere Konfigurationsoptionen von `location` finden Sie [hier](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).
{% tabs %}
{% tab schnell %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

### Konfigurieren von Geoofences für Hintergrundberichte

Standardmäßig werden Geofences nur überwacht, wenn sich Ihre App im Vordergrund befindet oder wenn sie über eine `Always`-Autorisierung verfügt (die alle Anwendungszustände überwacht).

Sie können jedoch entscheiden, ob Sie Geofence-Ereignisse überwachen möchten, wenn Ihre App im Hintergrund läuft oder wenn sie über eine `When In Use`-Autorisierung verfügt, indem Sie die `Background Mode -> Location updates`-Fähigkeit zu Ihrem Xcode-Projekt hinzufügen und `allowBackgroundGeofenceUpdates` aktivieren. So kann Braze den Status "in use" Ihrer App verlängern, indem es kontinuierlich Updates des Standorts überwacht.

`allowBackgroundGeofenceUpdates` funktioniert nur, wenn sich Ihre App im Hintergrund befindet. Wenn es wieder geöffnet wird, werden die vorhandenen Hintergrundprozesse angehalten, sodass die Vordergrundprozesse stattdessen priorisiert werden können.

{% alert important %}
Um Batterieverbrauch und Rate-Limiting zu vermeiden, sollten Sie `distanceFilter` auf einen Wert konfigurieren, der den spezifischen Anforderungen Ihrer App entspricht. Wenn Sie `distanceFilter` auf einen höheren Wert einstellen, wird verhindert, dass Ihre App den Nutzerstandort zu häufig anfragt.
{% endalert %}

## Schritt 4: Auf Braze Background-Push prüfen

Braze synchronisiert Geofences mit Geräten über Push-Benachrichtigungen im Hintergrund. Befolgen Sie den Artikel [Ignorieren von Silent Push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/), um sicherzustellen, dass Ihre Anwendung beim Empfang von Braze Geofence-Synchronisierungsbenachrichtigungen keine unerwünschten Aktionen ausführt.

## Schritt 5: Strings zur Beschreibung der Standortverwendung zu Ihrem Info.plist hinzufügen

Fügen Sie den Schlüssel `NSLocationAlwaysUsageDescription`, `NSLocationAlwaysAndWhenInUseUsageDescription` oder `NSLocationWhenInUseUsageDescription` zu Ihrem `info.plist` mit einem `String`-Wert hinzu, der eine Beschreibung enthält, warum Ihre Anwendung ein Tracking der Standorte benötigt.

Diese Beschreibung wird angezeigt, wenn die Standortabfrage des Systems eine Autorisierung verlangt, und sollte Ihren Benutzern die Vorteile der Standortverfolgung deutlich erklären.

## Schritt 6: Autorisierungsanfrage durch den Nutzer

Sie können eine [`When In Use`](#when-in-use)- oder eine[`Always`](#always)-Autorisierung anfordern.

### When In Use

Um eine `When In Use`-Anfrage zu stellen, verwenden Sie die Methode `requestWhenInUseAuthorization()`:

{% tabs %}
{% tab schnell %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endtab %}

{% tab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endtab %}
{% endtabs %}

### Immer

Standardmäßig gewährt `requestAlwaysAuthorization()` Ihrer App nur die `When In Use`-Autorisierung und fordert die Nutzer nach einiger Zeit erneut zur `Always`-Autorisierung auf. Sie können Ihre Nutzer aber auch sofort auffordern, zuerst `requestWhenInUseAuthorization()` und dann `requestAlwaysAuthorization()` aufzurufen, nachdem Sie die anfängliche `When In Use`-Autorisierung erhalten haben.

{% alert important %}
Sie können nur ein einziges Mal sofort eine `Always` Autorisierung anfordern.
{% endalert %}

{% tabs %}
{% tab schnell %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endtab %}

{% tab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endtab %}
{% endtabs %}

## Schritt 7: Aktivieren Sie Geofences auf dem Dashboard

Unter iOS können nur bis zu 20 Geofences für eine bestimmte App gespeichert werden. Wenn Geofences aktiviert sind, wird Braze einige dieser 20 verfügbaren Slots verwenden. Um eine versehentliche oder unerwünschte Unterbrechung anderer geofence-bezogener Funktionen in Ihrer App zu verhindern, müssen Standort-Geofences für einzelne Apps auf dem Dashboard aktiviert werden. Damit unsere Serviceleistungen; Dienste korrekt funktionieren, überprüfen Sie, ob Ihre App nicht alle verfügbaren Geofence-Spots nutzt.

Es gibt zwei Möglichkeiten, Geoofences für eine bestimmte App zu aktivieren: über die Seite **Standorte** oder über die Seite **Einstellungen verwalten**.

### Enablement von GeoFences auf der Seite Standorte

Aktivieren Sie Geoofences auf der Seite **Standorte** des Dashboards.

1. Gehen Sie zu **Zielgruppe** > Standorte.
{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Standorte** unter **Engagement**.
{% endalert %}

{:start="2"}
2\. Unter der Karte wird beispielsweise die Anzahl der Apps in Ihrem Workspace angezeigt, für die Geofencing derzeit aktiviert ist: **0 von 1 Apps mit aktiviertem Geofencing** Klicken Sie auf diesen Text.
3\. Wählen Sie die App aus, um das Geofencing zu aktivieren. Klicken Sie auf **Erledigt.**
![Geofence-Optionen auf der Seite "Standorte".]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Enablement von Geofences über die Seite Einstellungen verwalten

Aktivieren Sie Geofences in den Einstellungen Ihrer App.

1. Gehen Sie zu **Einstellungen** > **App-Einstellungen**.
{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie GeoFences unter **Einstellungen verwalten** > Einstellungen.
{% endalert %}

{:start="2"}
2\. Wählen Sie die App aus, für die Sie das Geofencing aktivieren möchten.
3\. Wählen Sie das Kontrollkästchen **Geofences Enablement** aus. Klicken Sie auf **Speichern.**

![Das Geofencing-Kontrollkästchen auf den Braze-Einstellungsseiten.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Deaktivieren von automatischen Geofence-Anfragen

Sie können automatische Geofencing-Anfragen in Ihrem `configuration`-Objekt deaktivieren, das an [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)) weitergegeben wurde. Stellen Sie `automaticGeofenceRequests` auf `false` ein. Zum Beispiel:

{% tabs %}
{% tab schnell %}

```swift
let configuration = Braze.Configuration(
  apiKey: "{BRAZE_API_KEY}",
  endpoint: "{BRAZE_ENDPOINT}"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:{BRAZE_API_KEY}
                                  endpoint:{BRAZE_ENDPOINT}];
configuration.automaticGeofencesRequest = NO;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

Wenn Sie sich für diese Option entscheiden, müssen Sie die Geofences manuell anfragen, damit das Feature funktioniert.

## Geofencing manuell anfordern

Wenn das Braze SDK Geofences zur Überwachung aus dem Backend anfragt, meldet es den aktuellen Nutrzerstandort und erhält Geofences, die auf der Grundlage des gemeldeten Standorts als optimal relevant eingestuft werden. Es gibt ein Rate-Limits für eine Geofence-Aktualisierung pro Sitzung.

Um den Standort zu kontrollieren, den das SDK für den Empfang der relevantesten Geofences meldet, können Sie das Geofencing manuell anfragen, indem Sie den Breiten- und Längengrad eines Standorts angeben. Es wird empfohlen, automatische Geofencing-Anfragen zu deaktivieren, wenn Sie diese Methode verwenden. Verwenden Sie dazu den folgenden Code:

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

