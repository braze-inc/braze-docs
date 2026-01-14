{% alert important %}
Ab iOS 14 funktionieren Geoofences nicht mehr zuverlässig für Nutzer:innen, die nur ihren ungefähren Standort angeben möchten.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Einrichten von Geofences {#setting-up-geofences}

### Schritt 1: Enablement in Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Schritt 2: Aktivieren Sie die Standortdienste Ihrer App

Standardmäßig sind die Standortdienste von Braze nicht aktiviert. Um sie in Ihrer App zu aktivieren, führen Sie die folgenden Schritte aus. Eine Schritt-für-Schritt-Anleitung finden Sie unter [Tutorial: Braze Standorte und Geofences](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### Schritt 2.1: Fügen Sie das Modul `BrazeLocation` hinzu.

Öffnen Sie in Xcode den Tab **Allgemein**. Fügen Sie unter **Frameworks, Bibliotheken und eingebettete Inhalte** das Modul `BrazeLocation` hinzu.

![Fügen Sie das Modul BrazeLocation zu Ihrem Xcode-Projekt hinzu]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### Schritt 2.2: Aktualisieren Sie Ihr `Info.plist`

Weisen Sie in Ihrem `info.plist` einem der folgenden Schlüssel den Wert `String` zu, der beschreibt, warum Ihre Anwendung den Standort verfolgen muss. Dieser String wird angezeigt, wenn Ihre Nutzer:innen zur Eingabe von Standortleistungen; Diensten aufgefordert werden. Erklären Sie daher deutlich, welchen Wert die Aktivierung dieses Features für Ihre App hat.

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist Standort-Strings in Xcode]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Apple hat `NSLocationAlwaysUsageDescription` veraltet. Weitere Informationen finden Sie in der [Dokumentation von Apple für Entwickler:in.](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription)
{% endalert %}

### Schritt 3: Enablement von Geoofences in Ihrem Code

Im Code Ihrer App aktivieren Sie GeoFozences, indem Sie `location.geofencesEnabled` auf `true` im `configuration` Objekt setzen, das die [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) Instanz initialisiert. Für weitere `location` Konfigurationsoptionen siehe [Braze Swift SDK referenzieren](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).

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

// Additional configuration customization...

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

// Additional configuration customization...

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### Schritt 3.1: Enablement von Hintergrundberichten (optional)

Standardmäßig werden Geofence-Ereignisse nur überwacht, wenn sich Ihre App im Vordergrund befindet oder über eine `Always` Autorisierung verfügt, die alle Anwendungszustände überwacht.

Sie können jedoch auch Geofence-Ereignisse überwachen, wenn Ihre App im Hintergrund läuft oder über eine [`When In Use` Autorisierung](#swift_request-authorization) verfügt. 

Um diese zusätzlichen Geofence-Ereignisse zu überwachen, öffnen Sie Ihr Xcode-Projekt und gehen Sie dann zu **Signing & Capabilities**. Aktivieren Sie unter **Hintergrundmodi** die Option **Standort-Updates**.

![In Xcode, Hintergrundmodus > Standort Updates]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

Als nächstes aktivieren Sie `allowBackgroundGeofenceUpdates` im Code Ihrer App. So kann Braze den Status "In Betrieb" Ihrer App verlängern, indem es kontinuierlich Updates des Standorts überwacht. Diese Einstellung funktioniert nur, wenn sich Ihre App im Hintergrund befindet. Wenn die App wieder geöffnet wird, werden alle bestehenden Hintergrundprozesse angehalten und stattdessen Vordergrundprozesse priorisiert.

{% tabs %}
{% tab schnell %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true

// Determines the number of meters required to trigger a new location update.
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

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

{% alert important %}
Um Batterieverbrauch und Rate-Limiting zu vermeiden, konfigurieren Sie `distanceFilter` auf einen Wert, der den spezifischen Anforderungen Ihrer App entspricht. Wenn Sie `distanceFilter` auf einen höheren Wert einstellen, wird verhindert, dass Ihre App den Nutzerstandort zu häufig anfragt.
{% endalert %}

### Schritt 4: Autorisierung anfragen {#request-authorization}

Wenn Sie eine Autorisierung von einem Nutzer:innen anfordern, fragen Sie entweder `When In Use` oder `Always` an.

{% tabs local %}
{% tab Wenn Sie in Gebrauch sind %}
Um eine `When In Use`-Anfrage zu stellen, verwenden Sie die Methode `requestWhenInUseAuthorization()`:

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Immer %}
Standardmäßig gewährt `requestAlwaysAuthorization()` Ihrer App nur die `When In Use`-Autorisierung und fordert die Nutzer nach einiger Zeit erneut zur `Always`-Autorisierung auf.

Sie können Ihre Nutzer:innen jedoch auch sofort auffordern, zuerst `requestWhenInUseAuthorization()` und dann `requestAlwaysAuthorization()` aufzurufen, nachdem Sie die erste Autorisierung von `When In Use` erhalten haben.

{% alert important %}
Sie können nur ein einziges Mal sofort eine `Always` Autorisierung anfordern.
{% endalert %}

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Schritt 5: Überprüfen Sie den Push im Hintergrund

Braze synchronisiert Geofences mit Geräten über Push-Benachrichtigungen im Hintergrund. Befolgen Sie diese Anweisungen, um [stille Push-Benachrichtigungen einzurichten]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift), damit Geofence-Updates vom Server richtig verarbeitet werden.

{% alert note %}
Um sicherzustellen, dass Ihre Anwendung beim Empfang von Geofence-Synchronisierungsbenachrichtigungen von Braze keine unerwünschten Aktionen ausführt, folgen Sie dem Artikel [Ignorieren von Silent Push]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).
{% endalert %}

## Manuelle Anfrage für Geofences {#manually-request-geofences}

Wenn das Braze SDK Geofences aus dem Backend anfragt, meldet es den aktuellen Standort des Nutzers und erhält Geofences, die auf der Grundlage des gemeldeten Standorts als optimal relevant eingestuft werden.

Um den Standort zu kontrollieren, den das SDK meldet, um die relevantesten Geoofences zu erhalten, können Sie Geoofences manuell anfragen, indem Sie die gewünschten Koordinaten angeben.

### Schritt 1: Setzen Sie `automaticGeofenceRequests` auf `false`

Sie können automatische Geofencing-Anfragen in Ihrem `configuration`-Objekt deaktivieren, das an [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)) weitergegeben wurde. Stellen Sie `automaticGeofenceRequests` auf `false` ein.

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

### Schritt 2: Rufen Sie `requestGeofences` manuell auf.

Fragen Sie in Ihrem Code Geofences mit dem entsprechenden Breiten- und Längengrad an.

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

## Häufig gestellte Fragen (FAQ) {#faq}

#### Warum erhalte ich keine GeoFences auf meinem Gerät?

Um zu überprüfen, ob GeoFencing auf Ihrem Gerät empfangen wird, verwenden Sie zunächst das [Tool SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk), um die Protokolle des SDK zu prüfen. Sie können dann sehen, ob Geofences erfolgreich vom Server empfangen werden und ob es irgendwelche bemerkenswerten Fehler gibt.

Nachstehend finden Sie weitere mögliche Gründe, warum Geofences auf Ihrem Gerät nicht empfangen werden können:

##### Einschränkungen des iOS Betriebssystems

Das Betriebssystem iOS erlaubt es nur, bis zu 20 Geofences für eine bestimmte App zu speichern. Wenn Geofences aktiviert sind, wird Braze einige dieser 20 verfügbaren Slots verwenden.

Um eine versehentliche oder unerwünschte Unterbrechung anderer geofence-bezogener Funktionen in Ihrer App zu verhindern, müssen Standort-Geofences für einzelne Apps auf dem Dashboard aktiviert werden. Damit unsere Serviceleistungen; Dienste korrekt funktionieren, überprüfen Sie, ob Ihre App nicht alle verfügbaren Geofence-Spots nutzt.

##### Rate-Limiting

Braze hat ein Limit von 1 Geofence-Aktualisierung pro Sitzung, um unnötige Anfragen zu vermeiden.

#### Wie funktioniert es, wenn ich sowohl Braze- als auch Nicht-Braze-Features für Geofence verwende?

Wie bereits erwähnt, ist es unter iOS zulässig, dass eine einzelne App maximal 20 Geofences einspeichert. Dieser Speicher wird sowohl von Braze- als auch von Nicht-Braze-Geofences gemeinsam genutzt und wird von [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) verwaltet.

Wenn Ihre App beispielsweise 20 Geofences enthält, die nicht von Braze stammen, gibt es keinen Speicherplatz für das Tracking von Braze-Geofences (oder umgekehrt). Um neue Geoofences zu erhalten, müssen Sie [die Standort-APIs von Apple](https://developer.apple.com/documentation/corelocation) verwenden, um die Überwachung einiger der bestehenden Geoofences auf dem Gerät zu beenden.

#### Kann das Feature Geofences verwendet werden, wenn ein Gerät offline ist?

Ein Gerät muss nur dann mit dem Internet verbunden sein, wenn eine Aktualisierung erfolgt. Sobald es erfolgreich Geofences vom Server empfangen hat, ist es möglich, einen Geofence-Eingang oder -Ausgang zu protokollieren, selbst wenn das Gerät offline ist. Das liegt daran, dass der Standort eines Geräts getrennt von seiner Internetverbindung funktioniert.

Nehmen wir an, ein Gerät hat zu Beginn der Sitzung erfolgreich GeoFences empfangen und registriert und geht dann offline. Wenn er dann in einen dieser registrierten Geoofences eintritt, kann er eine Braze Kampagne triggern.

#### Warum werden GeoFences nicht überwacht, wenn meine App im Hintergrund läuft/beendet wird?

Ohne `Always` Autorisierung schränkt Apple die Ausführung von Standort Services ein, wenn eine App nicht benutzt wird. Dies wird durch das Betriebssystem erzwungen und liegt außerhalb der Kontrolle des Braze SDK. Braze bietet zwar separate Konfigurationen für die Ausführung von Diensten, während sich die App im Hintergrund befindet, aber es gibt keine Möglichkeit, diese Einschränkungen für Apps zu umgehen, die ohne ausdrückliche Genehmigung des Nutzers:innen beendet werden.