---
nav_title: Seguimiento de ubicación
article_title: Seguimiento de ubicación para iOS
platform: Swift
page_order: 6
description: "En este artículo se muestra cómo configurar el seguimiento de ubicación para el SDK Swift."
Tool:
  - Location

---

# seguimiento de ubicación

> De manera predeterminada, Braze desactiva el seguimiento de ubicación. Habilitamos el seguimiento de ubicación después de que la aplicación anfitriona haya optado por el seguimiento de ubicación y haya obtenido el permiso del usuario. Siempre que los usuarios hayan optado por el seguimiento de ubicación, Braze registrará una única ubicación para cada usuario al inicio de la sesión.

## Habilitación del seguimiento de ubicación automático

Repasa [Solicitar autorización para servicios de ubicación](https://developer.apple.com/documentation/corelocation/requesting_authorization_to_use_location_services) y asegúrate de configurar las cadenas de propósito de tu aplicación. Al utilizar las características de ubicación de Braze, tu aplicación es responsable de solicitar autorización para utilizar los servicios de ubicación. 

Para habilitar el seguimiento de ubicación, añade el módulo `BrazeLocation` en la pestaña **General** de la página de configuración de tu aplicación.

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
{% tab OBJETIVO-C %}

En tu archivo `AppDelegate.m`, importa el módulo `BrazeLocation` en la parte superior del archivo. Añade una instancia de `BrazeLocationProvider` a la configuración de Braze, asegurándote de que todos los cambios en la configuración se realizan antes de llamar a Braze(configuration:). Consulta `BRZConfigurationLocation` para ver las configuraciones disponibles.

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

### Pasar datos de ubicación a Braze

Se pueden utilizar los siguientes métodos para establecer manualmente la última ubicación conocida del usuario. Estos ejemplos suponen que has asignado la instancia de Braze como variable en el AppDelegate.



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
{% tab OBJETIVO-C %}

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

Consulta [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/) para más información.

