## Aufzeichnung des aktuellen Standorts

### Schritt 1: Konfigurieren Sie Ihr Projekt

{% alert important %}
Wenn Sie die Braze-Features für Standorte verwenden, muss Ihre App die Erlaubnis zur Nutzung der Standortdienste anfordern. Lesen Sie unbedingt [Apple Entwickler:in: Anfrage zur Autorisierung von Standortdiensten für Nutzer:innen](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services).
{% endalert %}

Um das Standort-Tracking zu aktivieren, öffnen Sie Ihr Xcode-Projekt und wählen Sie Ihre App aus. Auf dem Tab **Allgemein** fügen Sie das Modul `BrazeLocation` hinzu.

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
{% tab objektiv-c %}

Importieren Sie in Ihrer Datei `AppDelegate.m` das Modul `BrazeLocation`, das sich am Anfang der Datei befindet. Fügen Sie der Braze-Konfiguration eine Instanz von `BrazeLocationProvider` hinzu. Stellen Sie sicher, dass alle Änderungen an der Konfiguration vor dem Aufruf von `Braze(configuration:)` vorgenommen werden. Die verfügbaren Konfigurationen finden Sie unter `BRZConfigurationLocation`.

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

### Schritt 2: Den Standort des Nutzers:innen protokollieren

Als nächstes protokollieren Sie den letzten bekannten Standort des Nutzers:innen in Braze. Die folgenden Beispiele gehen davon aus, dass Sie die Braze-Instanz als Variable in Ihrem `AppDelegate` zugewiesen haben.

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
{% tab objektiv-c %}

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

{% alert tip %}
Für weitere Informationen siehe [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/).
{% endalert %}
