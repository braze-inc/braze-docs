---
nav_title: Standort-Tracking
article_title: Standort-Tracking für iOS
platform: Swift
page_order: 6
description: "Dieser Artikel zeigt, wie Sie das Standort-Tracking für das Swift SDK konfigurieren."
Tool:
  - Location

---

# Standort-Tracking

> Standardmäßig deaktiviert Braze das Standort-Tracking. Das Standort-Tracking wird aktiviert, nachdem die Host-Anwendung die Nutzererlaubnis für das Standort-Tracking erhalten hat. Wenn Nutzer dem Standort-Tracking zugestimmt haben, protokolliert Braze beim Start der Sitzung einen einzigen Standort für jeden Nutzer.

## Aktivierunug des automatischen Standort-Trackings

Gehen Sie die [Dokumentation über die Erlaubnisanforderung für Standortdienste](https://developer.apple.com/documentation/corelocation/requesting_authorization_to_use_location_services) durch und konfigurieren Sie die Strings entsprechend für Ihre App. Wenn Sie die Braze-Features für Standorte verwenden, muss Ihre App die Erlaubnis zur Nutzung der Standortdienste anfordern. 

Um das Standort-Tracking zu aktivieren, fügen Sie das Modul `BrazeLocation` auf dem Tab **Allgemein** Ihrer Anwendungskonfigurationsseite hinzu.

{% tabs %}
{% tab schnell %}

Importieren Sie in Ihrer Datei `AppDelegate.swift` das Modul `BrazeLocation`, das sich am Anfang der Datei befindet. Fügen Sie der Braze-Konfiguration eine Instanz von `BrazeLocationProvider` hinzu. Stellen Sie sicher, dass alle Änderungen an der Konfiguration vor dem Aufruf von `Braze(configuration:)` vorgenommen werden. Die verfügbaren Konfigurationen finden Sie unter `Braze.Configuration.Location`.

```swift
import UIKit
import BrazeKit
import BrazeLocation

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    configuration.logger.level = .info
    configuration.location.brazeLocationProvider = BrazeLocationProvider()
    configuration.location.automaticLocationCollection = true
    configuration.location.geofencesEnabled = true
    configuration.location.automaticGeofenceRequests = true
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze

    return true
  }

}

```

{% endtab %}
{% tab OBJECTIVE-C %}

Importieren Sie in Ihrer Datei `AppDelegate.m` das Modul `BrazeLocation`, das sich am Anfang der Datei befindet. Fügen Sie der Braze-Konfiguration eine Instanz `BrazeLocationProvider` hinzu. Stellen Sie sicher, dass alle Änderungen an der Konfiguration vor dem Aufruf von Braze(configuration:) vorgenommen werden. Die verfügbaren Konfigurationen finden Sie unter `BRZConfigurationLocation`.

```objc
#import "AppDelegate.h"

@import BrazeKit;
@import BrazeLocation;

@implementation AppDelegate

#pragma mark - Lifecycle

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration =
      [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                      endpoint:brazeEndpoint];
  configuration.logger.level = BRZLoggerLevelInfo;
  configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
  configuration.location.automaticLocationCollection = YES;
  configuration.location.geofencesEnabled = YES;
  configuration.location.automaticGeofenceRequests = YES;
  Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}

@end
```

{% endtab %}
{% endtabs %}

### Übergabe von Standort-Daten an Braze

Die folgenden Methoden können verwendet werden, um den letzten bekannten Nutzerstandort manuell festzulegen. Diese Beispiele gehen davon aus, dass Sie die Braze-Instanz als Variable im AppDelegate zugewiesen haben.



{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.user.setLastKnownLocation(latitude:latitude,
                                             longitude:longitude)
```

```swift
AppDelegate.braze?.user.setLastKnownLocation(latitude:latitude,
                                             longitude:longitude,
                                             altitude:altitude,
                                             horizontalAccuracy:horizontalAccuracy,
                                             verticalAccuracy:verticalAccuracy)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.user setLastKnownLocationWithLatitude:latitude
                                               longitude:longitude
                                      horizontalAccuracy:horizontalAccuracy];

```

```objc
[AppDelegate.braze.user setLastKnownLocationWithLatitude:latitude
                                               longitude:longitude
                                      horizontalAccuracy:horizontalAccuracy
                                                altitude:altitude
                                        verticalAccuracy:verticalAccuracy];

```

{% endtab %}
{% endtabs %}

Refernzieren Sie unter [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/) für weitere Informationen.

