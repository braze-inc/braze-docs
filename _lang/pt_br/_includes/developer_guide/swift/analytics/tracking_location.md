## Registro do local atual

### Etapa 1: Configure seu projeto

{% alert important %}
Ao usar os recursos de localização do Braze, seu aplicativo é responsável por solicitar autorização para usar os serviços de localização. Não deixe de acessar [Apple Developer: Solicitação de autorização para serviços de local do usuário](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services).
{% endalert %}

Para ativar o monitoramento de localização, abra seu projeto Xcode e selecione seu app. Na guia **General (Geral** ), adicione o módulo `BrazeLocation`.

{% tabs %}
{% tab swift %}

Em seu arquivo `AppDelegate.swift`, importe o módulo `BrazeLocation` na parte superior do arquivo. Adicione uma instância de `BrazeLocationProvider` à configuração da Braze, conferindo se todas as alterações na configuração estão feitas antes de chamar `Braze(configuration:)`. Consulte `Braze.Configuration.Location` para ver as configurações disponíveis.

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
{% tab objective-c %}

Em seu arquivo `AppDelegate.m`, importe o módulo `BrazeLocation` na parte superior do arquivo. Adicione uma instância de `BrazeLocationProvider` à configuração da Braze, conferindo se todas as alterações na configuração estão feitas antes de chamar `Braze(configuration:)`. Consulte `BRZConfigurationLocation` para ver as configurações disponíveis.

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

### Etapa 2: Registre o local do usuário

Em seguida, registre o último local conhecido do usuário no Braze. Os exemplos a seguir pressupõem que você atribuiu a instância do Braze como uma variável em seu site `AppDelegate`.

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
{% tab objective-c %}

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
Para saber mais, consulte [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/).
{% endalert %}
