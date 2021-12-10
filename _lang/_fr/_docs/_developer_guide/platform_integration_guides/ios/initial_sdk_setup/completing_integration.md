---
nav_title: Compléter l’intégration
article_title: Compléter l’intégration du SDK iOS
platform: iOS
description: "Cet article de référence montre comment finir d'intégrer le Braze SDK après l'avoir installé via l'une des options d'intégration."
page_order: 2
---

# Compléter l'intégration

## Exigences

Avant de suivre ces étapes, assurez-vous que vous avez intégré le SDK en utilisant l'une des options d'installation listées avant cette page.

## Étape 1 : Mettre à jour votre délégué à l'application

{% tabs %}
{% tab OBJECTIVE-C %}

Si vous intégrez le SDK Braze avec CocoaPods, Carthage, ou avec une [intégration dynamique manuelle]({{site.baseUrl}}/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), ajouter la ligne de code suivante à votre `AppDelegate.` fichier :

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Si vous intégrez avec Swift Package Manager ou avec une [intégration statique manuelle]({{site.baseUrl}}/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), utilisez cette ligne à la place :

```objc
#import "AppboyKit.h"
```

Dans votre fichier `AppDelegate.m` , ajoutez le snippet suivant dans votre application `:didFinishLaunchingWithOptions:` méthode :

```objc
[Appboy startWithApiKey:@"VOTRE APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Si vous intégrez le SDK Braze avec CocoaPods, Carthage, ou avec une [intégration dynamique manuelle]({{site.baseUrl}}/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), ajouter la ligne de code suivante à votre `AppDelegate. fichier wift`:

```swift
Importer Appboy_iOS_SDK
```

Si vous intégrez avec Swift Package Manager ou avec une [intégration statique manuelle]({{site.baseUrl}}/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), utilisez cette ligne à la place :

```swift
Importer AppboyKit
```

Pour plus d'informations sur l'utilisation du code Objective-C dans les projets Swift, veuillez consulter la [Documentation des développeurs Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Dans `AppDelegate.swift`, ajoutez un snippet suivant à votre application `(application : UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "VOTRE APP-IDENTIFIER-API-KEY", dans:application, withLaunchOptions:launchOptions)
```

{% endtab %}
{% endtabs %}

__Remarque__: Le singleton `sharedInstance` de Braze sera nul avant `startWithApiKey :` est appelé, car c'est une condition préalable à l'utilisation de toutes les fonctionnalités de Braze.

{% alert important %}
N'oubliez pas de mettre à jour `VOTRE APP-IDENTIFIER-API-KEY` avec la valeur correcte depuis votre page **Paramètres**. Pour plus d'informations sur où trouver votre clé API App Identifier, consultez notre [documentation API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key).
{% endalert %}

{% alert warning %}
N'oubliez pas d'initialiser Braze dans le fil de discussion principal de votre application. L'initialisation asynchrone peut conduire à des fonctionnalités cassées.
{% endalert %}


## Étape 2 : Spécifiez votre grappe de données

{% alert note %}
Notez qu'à partir de décembre 2019, les points de terminaison personnalisés ne sont plus donnés, si vous avez un point de terminaison personnalisé préexistant, vous pouvez continuer à l'utiliser. Pour plus de détails, reportez-vous à notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste de terminaux disponibles</a>.
{% endalert %}

### Configuration du point de terminaison de la compilation (recommandé)

Si donné un point de terminaison personnalisé préexistant...
- À partir de Braze iOS SDK v3.0.2, vous pouvez définir un point de terminaison personnalisé en utilisant le fichier `Info.plist`. Ajoutez le dictionnaire `Braze` à votre fichier `Info.plist`. À l'intérieur du dictionnaire `Braze` , ajoutez la sous-entrée de chaîne `Endpoint` et définissez la valeur à l'autorité de votre URL de terminaison personnalisée (par exemple, `sdk. ad-01.braze.com`, pas `https://sdk.iad-01.braze.com`). Notez qu'avant Braze iOS SDK v4.0.2, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

Votre représentant de Braze aurait déjà dû vous aviser du [bon terminaison]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/).

### Configuration du point de terminaison d'exécution

Si donné un point de terminaison personnalisé préexistant...
- Commence avec Braze iOS SDK v3.17. +, vous pouvez surcharger votre point de terminaison via la `ABKEndpointKey` dans le paramètre `appboyOptions` passé à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez la valeur à l'autorité de votre URL de terminaison personnalisée (par exemple, `sdk.iad-01.braze.com`, pas `https://sdk.iad-01.braze.com`).

{% alert important %}
Pour connaître votre grappe spécifique, veuillez vous adresser à votre Responsable du Service Clientèle ou contacter notre équipe d'assistance.
{% endalert %}

## Intégration du SDK terminée

Braze devrait maintenant collecter des données de votre application et votre intégration de base devrait être complète. {% if include.platform == 'iOS' %}Veuillez consulter les sections suivantes afin d'activer le suivi personnalisé des événements, les messages push, le fil d'actualité et la suite complète des fonctionnalités de Braze.{% endif %}

## Personnalisation de Braze au démarrage

Si vous souhaitez personnaliser Braze au démarrage, vous pouvez à la place utiliser la méthode d'initialisation de Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` et passer dans un `NSDictionary` optionnel de clés de démarrage de Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

Dans votre fichier `AppDelegate.m` , dans votre application `: didFinishLaunchingWithOptions:` , ajoutez la méthode Braze suivante :

```objc
[Appboy startWithApiKey:@"VOTRE APP-IDENTIFER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

Dans `AppDelegate.swift`, dans votre application `(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` méthode, ajouter la méthode Braze suivante :

```swift
Appboy.start(withApiKey: "VOTRE-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

où `appboyOptions` est un `dictionnaire` de valeurs de configuration de démarrage.

{% endtab %}
{% endtabs %}

__Note__: Cette méthode remplacerait le `startWithApiKey:inApplication:withLaunchOptions:` méthode d'initialisation d'en haut.

Cette méthode est appelée avec les paramètres suivants :

- `YOUR-APP-IDENTIFIER-API-KEY` – Votre [Identifiant d'application]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) clé API du tableau de bord Braze.
- `application` – L'application actuelle
- `launchOptions` – Les options `NSDictionary` que vous obtenez de `application:didFinishLaunchingWithOptions :`
- `appboyOptions` – Une option `NSDictionary` avec des valeurs de configuration de démarrage pour Braze

Voir [Appboy.h][1] pour une liste des clés de démarrage de Braze.

## Appboy.sharedInstance() et Swift nullability
Différente quelque peu de la pratique courante, le singleton `Appboy.sharedInstance()` est facultatif. La raison en est que, comme indiqué ci-dessus, `sharedInstance` est `nul` avant `startWithApiKey :` est appelée, et il y a des implémentations non standards mais non non valides dans lesquelles une initialisation retardée peut être utilisée.

Si vous appelez `startWithApiKey :` dans votre `didFinishLaunchingWithOptions :` déléguer avant tout accès à `sharedInstance` (l'implémentation standard), vous pouvez utiliser le chaînage optionnel, comme `Appboy. haredInstance()?.changeUser("testUser")`, pour éviter les vérifications encombrantes. Cela aura la parité avec une implémentation Objective-C qui a supposé une `sharedInstance` non nulle.

## Documentation

[La documentation complète de la classe iOS][2] est disponible pour fournir des conseils supplémentaires sur l'une des méthodes du SDK.

[1]: https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[2]: http://appboy.github.io/appboy-ios-sdk/docs/annotated.html "full iOS class documentation"
