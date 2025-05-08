---
nav_title: Monitoramento de localização
article_title: Monitoramento de localização para iOS
platform: Swift
page_order: 6
description: "Este artigo mostra como configurar o monitoramento de localização para o Swift SDK."
Tool:
  - Location

---

# monitoramento de localização

> Por padrão, a Braze desativa o monitoramento de localização. Ativamos o monitoramento de localização depois que o aplicativo host aceita o rastreamento de localização e obtém permissão do usuário. Desde que os usuários tenham aceitado o monitoramento de localização, o Braze registrará um único local para cada usuário no início da sessão.

## Ativação do monitoramento automático de localização

Acesse [Solicitar autorização para serviços locais](https://developer.apple.com/documentation/corelocation/requesting_authorization_to_use_location_services) e certifique-se de configurar as strings de finalidade de seu aplicativo. Ao usar os recursos de localização do Braze, seu aplicativo é responsável por solicitar autorização para usar os serviços de localização. 

Para ativar o monitoramento de localização, adicione o módulo `BrazeLocation` na guia **General (Geral** ) da página de configuração do aplicativo.

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
{% tab OBJECTIVE C %}

Em seu arquivo `AppDelegate.m`, importe o módulo `BrazeLocation` na parte superior do arquivo. Adicione uma instância de `BrazeLocationProvider` à configuração da Braze, conferindo se todas as alterações na configuração estão feitas antes de chamar Braze(configuration:). Consulte `BRZConfigurationLocation` para ver as configurações disponíveis.

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

### Passagem de dados de localização para a Braze

Os métodos a seguir podem ser usados para definir manualmente o último local conhecido do usuário. Esses exemplos pressupõem que você atribuiu a instância do Braze como uma variável no AppDelegate.



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
{% tab OBJECTIVE C %}

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

Consulte [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/) Para saber mais.

