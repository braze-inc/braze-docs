## Registro de la ubicación actual

### Paso 1: Configura tu proyecto

{% alert important %}
Al utilizar las características de ubicación de Braze, tu aplicación es responsable de solicitar autorización para utilizar los servicios de ubicación. No dejes de consultar [Desarrollador de Apple: Solicitud de autorización a los servicios de ubicación del usuario](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services).
{% endalert %}

Para habilitar el seguimiento de ubicación, abre tu proyecto de Xcode y selecciona tu aplicación. En la pestaña **General**, añade el módulo `BrazeLocation`.

{% tabs %}
{% tab swift %}

En tu archivo `AppDelegate.swift`, importa el módulo `BrazeLocation` en la parte superior del archivo. Añade una instancia de `BrazeLocationProvider` a la configuración de Braze, asegurándote de que todos los cambios en la configuración se realizan antes de llamar a `Braze(configuration:)`. Consulta `Braze.Configuration.Location` para ver las configuraciones disponibles.

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
{% tab objetivo-c %}

En tu archivo `AppDelegate.m`, importa el módulo `BrazeLocation` en la parte superior del archivo. Añade una instancia de `BrazeLocationProvider` a la configuración de Braze, asegurándote de que todos los cambios en la configuración se realizan antes de llamar a `Braze(configuration:)`. Consulta `BRZConfigurationLocation` para ver las configuraciones disponibles.

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

### Paso 2: Registrar la ubicación del usuario

A continuación, registra en Braze la última ubicación conocida del usuario. Los siguientes ejemplos suponen que has asignado la instancia de Braze como variable en tu `AppDelegate`.

{% tabs %}
{% tab swift %}

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
{% tab objetivo-c %}

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
Para más información, consulta [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/).
{% endalert %}
