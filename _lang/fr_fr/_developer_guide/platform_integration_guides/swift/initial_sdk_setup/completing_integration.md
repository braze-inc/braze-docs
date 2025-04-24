---
nav_title: Terminer l’intégration
article_title: "Terminer l'intégration SDK Swift"
platform: Swift
description: "Cet article de référence montre comment terminer l'intégration du SDK Swift de Braze après l'avoir installé via l'une des options d'intégration."
page_order: 2

---

# Terminer l’intégration

> Avant de suivre ces étapes, assurez-vous d'avoir intégré le SDK Swift pour iOS à l'aide du [gestionnaire de paquets swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) ou de [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/).

## Mettre à jour la délégation de votre application

{% tabs %}
{% tab swift %}

Ajoutez la ligne de code suivante à votre fichier `AppDelegate.swift` pour importer les fonctionnalités incluses dans le SDK Swift de Braze :

```swift
import BrazeKit
```


Ensuite, ajoutez une propriété statique à votre classe `AppDelegate` afin de conserver une référence forte à l'instance de Braze pendant toute la durée de vie de votre application :

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

Enfin, dans `AppDelegate.swift`, ajoutez l'extrait de code suivant à votre méthode `application:didFinishLaunchingWithOptions:` :

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

Mettez à jour `YOUR-APP-IDENTIFIER-API-KEY` et `YOUR-BRAZE-ENDPOINT` avec la valeur correcte à partir de la page **Paramètres de l'application.**  Consultez nos [types d'identifiants d'API]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) pour plus d'informations sur l'endroit où trouver la clé API de votre identifiant d'appli.

{% endtab %}
{% tab OBJECTIF-C %}

Ajoutez la ligne de code suivante à votre fichier `AppDelegate.m` :

```objc
@import BrazeKit;
```

Ensuite, ajoutez une variable statique à votre fichier `AppDelegate.m` afin de conserver une référence à l'instance de Braze pendant toute la durée de vie de votre application :

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

Enfin, dans votre fichier `AppDelegate.m`, ajoutez l'extrait de code suivant dans votre méthode `application:didFinishLaunchingWithOptions:` :

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

Mettez à jour `YOUR-APP-IDENTIFIER-API-KEY` et `YOUR-BRAZE-ENDPOINT` avec la valeur correcte à partir de votre page **Gérer les paramètres.**  Consultez notre [documentation sur l'API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) pour savoir où trouver la clé API de votre identifiant d'application.

{% endtab %}
{% endtabs %}


## Intégration SDK terminée

À ce stade, votre intégration de base devrait être terminée. Braze devrait maintenant collecter des données depuis votre application. Suivez les autres articles de ce guide d'intégration pour mettre en œuvre et personnaliser l'ensemble des fonctionnalités et des canaux d'envoi de messages de Braze.

## Ressources complémentaires

Notre [documentation de référence sur le SDK - ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/ "la documentation complète sur les classes iOS -") fournit des informations et des conseils supplémentaires sur chaque symbole du SDK.

