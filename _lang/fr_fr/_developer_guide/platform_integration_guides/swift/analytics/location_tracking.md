---
nav_title: Suivi de localisation
article_title: Suivi de la localisation pour iOS
platform: Swift
page_order: 6
description: "Cet article montre comment configurer le suivi des localisations pour le SDK Swift."
Tool:
  - Location

---

# Suivi de localisation

> Par défaut, Braze désactive le suivi de la localisation. Nous autorisons le suivi de la localisation après que l’application hôte a choisi le suivi de la localisation et obtenu l’autorisation de l’utilisateur. Si les utilisateurs ont opté pour le suivi de la localisation, Braze enregistrera une localisation unique pour chaque utilisateur au démarrage de la session.

## Activer le suivi automatique de la localisation

Consultez la rubrique [Demander une autorisation pour les services d'emplacement/localisation](https://developer.apple.com/documentation/corelocation/requesting_authorization_to_use_location_services) et assurez-vous de configurer les chaînes de caractères de l'objectif de votre application. Lors de l'utilisation des fonctionnalités d'emplacement/localisation de Braze, il incombe à votre application de demander l'autorisation d'utiliser les services de localisation. 

Pour activer l'emplacement/localisation, ajoutez le module `BrazeLocation` dans l'onglet **Général** de la page de configuration de votre application.

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
{% tab OBJECTIF-C %}

Dans votre fichier `AppDelegate.m`, importez le module `BrazeLocation` au début du fichier. Ajoutez une instance `BrazeLocationProvider` à la configuration de Braze, en vous assurant que toutes les modifications apportées à la configuration sont effectuées avant d'appeler Braze(configuration :). Consultez le site `BRZConfigurationLocation` pour connaître les configurations disponibles.

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

### Transfert des données de localisation vers Braze

Les méthodes suivantes peuvent être utilisées pour définir manuellement le dernier emplacement/localisation connu de l'utilisateur. Ces exemples supposent que vous avez assigné l'instance de Braze en tant que variable dans l'AppDelegate.



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
{% tab OBJECTIF-C %}

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

Pour plus d'informations, reportez-vous à [`Braze.User.swift`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/).

