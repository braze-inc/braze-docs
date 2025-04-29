## Enregistrement de l'emplacement/localisation actuel

### Étape 1 : Configurez votre projet

{% alert important %}
Lors de l'utilisation des fonctionnalités d'emplacement/localisation de Braze, il incombe à votre application de demander l'autorisation d'utiliser les services de localisation. Ne manquez pas de consulter le site [Apple Developer : Demande d'autorisation pour les services d'emplacement/localisation de l'utilisateur](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services).
{% endalert %}

Pour activer l'emplacement/localisation, ouvrez votre projet Xcode et sélectionnez votre appli. Dans l'onglet **Général**, ajoutez le module `BrazeLocation`.

{% tabs %}
{% tab swift %}

Dans votre fichier `AppDelegate.swift`, importez le module `BrazeLocation` au début du fichier. Ajoutez une instance `BrazeLocationProvider` à la configuration de Braze, en veillant à ce que toutes les modifications apportées à la configuration soient effectuées avant d'appeler `Braze(configuration:)`. Consultez le site `Braze.Configuration.Location` pour connaître les configurations disponibles.

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

Dans votre fichier `AppDelegate.m`, importez le module `BrazeLocation` au début du fichier. Ajoutez une instance `BrazeLocationProvider` à la configuration de Braze, en veillant à ce que toutes les modifications apportées à la configuration soient effectuées avant d'appeler `Braze(configuration:)`. Consultez le site `BRZConfigurationLocation` pour connaître les configurations disponibles.

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

### Étape 2 : Enregistrer l'emplacement/localisation de l'utilisateur

Ensuite, enregistrez dans Braze le dernier emplacement/localisation connu de l'utilisateur. Les exemples suivants supposent que vous avez assigné l'instance de Braze en tant que variable dans votre site `AppDelegate`.

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
Pour plus d'informations, voir [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/).
{% endalert %}
