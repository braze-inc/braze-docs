---
nav_title: Terminer l’intégration
article_title: Terminer l’intégration SDK iOS
platform: iOS
description: "Cet article de référence montre comment terminer l’intégration du SDK Braze après l’avoir installé via l’une des options d’intégration."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Terminer l’intégration

Avant de suivre ces étapes, assurez-vous d'avoir intégré le SDK en utilisant [Carthage]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/carthage_integration/), [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/cocoapods/), le [gestionnaire de paquets swift]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/) ou une intégration [manuelle]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/).

## Étape 1 : Mettre à jour la délégation de votre application

{% tabs %}
{% tab OBJECTIF-C %}

Si vous intégrez le SDK Braze avec des CocoaPods, Carthage ou avec une [intégration manuelle dynamique]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), ajoutez la ligne de code suivante à votre fichier `AppDelegate.m` :

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Si vous procédez à une intégration avec le gestionnaire de paquets swift ou à une [intégration manuelle statique]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), utilisez cette ligne à la place :

```objc
#import "AppboyKit.h"
```

Ensuite, dans votre fichier `AppDelegate.m`, ajoutez l’extrait de code suivant à l’aide de votre méthode `application:didFinishLaunchingWithOptions:` :

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

Mettez à jour `YOUR-APP-IDENTIFIER-API-KEY` avec la valeur correcte à partir de votre page **Gérer les paramètres**. Consultez notre [documentation sur l'API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) pour savoir où trouver la clé API de votre identifiant d'application.

{% endtab %}
{% tab swift %}

Si vous intégrez le SDK Braze avec des CocoaPods, Carthage ou avec une [intégration manuelle dynamique]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), ajoutez la ligne de code suivante à votre fichier `AppDelegate.swift` :

```swift
import Appboy_iOS_SDK
```

Si vous procédez à une intégration avec le gestionnaire de paquets swift ou à une [intégration manuelle statique]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), utilisez cette ligne à la place :

```swift
import AppboyKit
```
Reportez-vous à la [Documentation des développeurs Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html) pour plus d’informations sur l’utilisation du code Objective-C dans les projets Swift.

Ensuite, dans `AppDelegate.swift`, ajoutez l’extrait de code suivant à votre `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` :

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Mettez à jour `YOUR-APP-IDENTIFIER-API-KEY` avec la valeur correcte à partir de votre page **Gérer les paramètres**. Consultez notre [documentation sur l'API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) pour savoir où trouver la clé API de votre identifiant d'application.

{% endtab %}
{% endtabs %}

{% alert note %}
Le singleton `sharedInstance` sera nul avant que `startWithApiKey:` ne soit appelé, car il s'agit d'une condition préalable à l'utilisation de toute fonctionnalité de Braze.
{% endalert %}

{% alert warning %}
Assurez-vous d’initialiser Braze dans le fil principal de votre application. L’initialisation asynchrone peut entraîner un échec de la fonctionnalité.
{% endalert %}


## Étape 2 : Spécifier votre cluster de données

{% alert note %}
Notez que depuis décembre 2019, les points de terminaison personnalisés ne sont plus donnés. Si vous disposez d’un endpoint personnalisé préexistant, vous pouvez continuer à l’utiliser. Pour plus de détails, consultez notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste d’endpoints disponibles</a>.
{% endalert %}

### Configuration des endpoints de compilation (recommandée)

Si vous avez un endpoint personnalisé préexistant :
- À partir du SDK Braze pour iOS v3.0.2, vous pouvez définir un endpoint personnalisé à l’aide du fichier `Info.plist`. Ajouter le dictionnaire `Braze` à votre fichier `Info.plist`. À l’intérieur du dictionnaire `Braze`, ajoutez la sous-entrée de chaîne `Endpoint` et définissez la valeur à l’autorité de votre URL de endpoint personnalisé (par exemple, `sdk.iad-01.braze.com`, pas `https://sdk.iad-01.braze.com`). Notez qu’avant SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

Votre conseiller Braze devrait déjà vous avoir indiqué le [endpoint correct]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/).

### Configuration du endpoint d’exécution

Si vous avez un endpoint personnalisé préexistant :
- À partir du SDK Braze pour iOS v3.17.0+, vous pouvez remplacer votre endpoint par `ABKEndpointKey` à l’intérieur du paramètre `appboyOptions` transmis à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez la valeur à l’autorité de votre URL d’endpoint personnalisé (par exemple, `sdk.iad-01.braze.com`, pas `https://sdk.iad-01.braze.com`).

## Intégration SDK terminée

Braze devrait maintenant collecter des données depuis votre application et votre intégration de base devrait être terminée. Consultez les articles suivants pour activer le [suivi des événements personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/), l'[envoi de messages push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) et la suite complète des fonctionnalités de Braze.

## Personnaliser Braze au démarrage

Si vous souhaitez personnaliser Braze au démarrage, vous pouvez utiliser la méthode d’initialisation Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` et transmettre un `NSDictionary` facultatif des touches de démarrage Braze.
{% tabs %}
{% tab OBJECTIF-C %}

Dans votre fichier `AppDelegate.m`, au sein de votre méthode `application:didFinishLaunchingWithOptions:`, ajoutez la méthode Braze suivante :

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

Notez que cette méthode remplacera la méthode d’initialisation `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% tab swift %}

Dans `AppDelegate.swift`, avec votre méthode `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, ajoutez la méthode Braze suivante, avec `appboyOptions` un `Dictionary` des valeurs de configuration de démarrage :

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

Notez que cette méthode remplacera la méthode d’initialisation `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% endtabs %}

Cette méthode est utilisée avec les paramètres suivants :

- `YOUR-APP-IDENTIFIER-API-KEY` – Votre clé API d’[identifiant d’application]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) du tableau de bord de Braze.
- `application` – L’application actuelle.
- `launchOptions` – Les options `NSDictionary` que vous obtenez de `application:didFinishLaunchingWithOptions:`.
- `appboyOptions` – Un `NSDictionary` facultatif avec les valeurs de configuration de démarrage de Braze.

Voir [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h) pour obtenir la liste des touches de démarrage de Braze.

## Valeurs nulles Swift et Appboy.sharedInstance()
Légèrement différent de la pratique courante, le singleton `Appboy.sharedInstance()` est facultatif. Cela est dû au fait que `sharedInstance` est `nil` avant l’appel de `startWithApiKey:`, et qu’il existe des implémentations non standard et non valides dans lesquelles une initialisation retardée peut être utilisée.

Si vous utilisez `startWithApiKey:` dans votre délégation `didFinishLaunchingWithOptions:` avant tout accès à `sharedInstance` d’Appboy (l’implémentation standard), vous pouvez utiliser des chaînages facultatifs, comme `Appboy.sharedInstance()?.changeUser("testUser")`, pour éviter des vérifications fastidieuses. Il y aura parité avec une implémentation Objective-C qui a supposé un `sharedInstance` non nul.

## Ressources complémentaires

Une [documentation complète sur les classes iOS ](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html "(documentation complète sur les classes iOS)") est disponible pour fournir des conseils supplémentaires sur toutes les méthodes du SDK.

