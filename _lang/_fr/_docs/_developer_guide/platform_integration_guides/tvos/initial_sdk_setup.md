---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour tvOS
platform: tvOS
page_order: 0
page_type: Référence
description: "Cette page couvre les étapes initiales de l'installation du SDK tvOS Braze."
---

# Configuration initiale du SDK

**Note**: Notre SDK tvOS prend actuellement en charge les fonctionnalités d'analyse et la récupération des données du flux d'actualités.  Pour ajouter une application tvOS dans votre tableau de bord, veuillez ouvrir un [ticket de support][support].

L'installation du Braze SDK vous fournira des fonctionnalités d'analyse basiques.

Le SDK tvOS Braze devrait être installé ou mis à jour en utilisant [CocoaPods][apple_initial_setup_1], un gestionnaire de dépendance pour les projets Objective-C et Swift. CocoaPods fournit une simplicité supplémentaire pour l'intégration et la mise à jour.

## Intégration de tvOS SDK CocoaPod

### Étape 1 : Installer CocoaPods

Installer le SDK via le tvOS [CocoaPod][apple_initial_setup_1] automatise la majorité du processus d'installation pour vous. Avant de commencer ce processus, assurez-vous que vous utilisez [Ruby version 2.0.0][apple_initial_setup_2] ou plus. Ne vous inquiétez pas, la connaissance de la syntaxe de Ruby n'est pas nécessaire pour installer ce SDK.

Exécutez simplement la commande suivante pour commencer :

```bash
$ sudo gem install coapods
```

__Note__: Si vous êtes invité à écraser l'exécutable `rake` veuillez vous référer aux [Directions de démarrage sur CocoaPods. rg][apple_initial_setup_3] pour plus de détails.

__Note__: Si vous avez des problèmes concernant les CocoaPods, veuillez vous référer au [Guide de dépannage CocoaPods][apple_initial_setup_25].

### Étape 2 : Construire le podfile

Maintenant que vous avez installé la gemme Ruby de CocoaPods, vous allez avoir besoin de créer un fichier dans le répertoire de votre projet Xcode nommé `Podfile`.

Ajoutez la ligne suivante à votre fichier Podfile:

```
la cible 'YourAppTarget' fait
  pod 'Appboy-tvOS-SDK'
fin
```

__Note__: Nous vous suggérons la version Braze afin que les mises à jour de pod saisissent automatiquement tout ce qui est plus petit qu'une mise à jour mineure. Cela ressemble à 'pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build'. Si vous voulez intégrer la dernière version de Braze SDK automatiquement même avec des changements majeurs, vous pouvez utiliser `pod 'Appboy-tvOS-SDK'` dans votre Podfile.

### Étape 3 : Installation du Braze SDK

Pour installer Braze SDK Cocoapod, accédez au répertoire de votre projet d'application Xcode dans votre terminal et exécutez la commande suivante :
```
Installation du pod
```

À ce stade, vous devriez être en mesure d'ouvrir le nouvel espace de travail du projet Xcode créé par CocoaPods. Assurez-vous d'utiliser cet espace de travail Xcode au lieu de votre projet Xcode.

!\[Nouveau espace de travail\]\[apple_initial_setup_15\]

### Étape 4 : Mise à jour du délégué de votre application

{% tabs %}
{% tab OBJECTIVE-C %}

Ajoute la ligne de code suivante à ton fichier `AppDelegate.m`:

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

Dans votre fichier `AppDelegate.m` , ajoutez le snippet suivant dans votre application `: didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"VOTRE API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Si vous intégrez le SDK Braze avec CocoaPods ou Carthage, ajoutez la ligne de code suivante à votre fichier `AppDelegate.swift`:

```swift
import AppboyTVOSKit
```

Pour plus d'informations sur l'utilisation du code Objective-C dans les projets Swift, veuillez consulter la [Documentation des développeurs Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Dans `AppDelegate.swift`, ajoutez un snippet suivant à votre application `(application : UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "VOTRE-API-KEY", dans:application, withLaunchOptions:launchOptions)
```

__Remarque__: Le singleton `sharedInstance` de Braze sera nul avant `startWithApiKey :` est appelé, car c'est une condition préalable à l'utilisation de toutes les fonctionnalités de Braze.

{% endtab %}
{% endtabs %}

{% alert important %}
Assurez-vous de mettre à jour `VOTRE API-KEY` avec la valeur correcte à partir de la page des paramètres de votre application.
{% endalert %}

{% alert warning %}
N'oubliez pas d'initialiser Braze dans le fil de discussion principal de votre application. L'initialisation asynchrone peut conduire à des fonctionnalités cassées.
{% endalert %}


### Étape 5 : Spécifiez votre point de terminaison personnalisé ou cluster de données

{% alert note %}
Notez qu'à partir de décembre 2019, les points de terminaison personnalisés ne sont plus donnés, si vous avez un point de terminaison personnalisé préexistant, vous pouvez continuer à l'utiliser. Pour plus de détails, reportez-vous à notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste de terminaux disponibles</a>.
{% endalert %}

Votre représentant de Braze aurait déjà dû vous aviser du [bon terminaison]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuration du point de terminaison de la compilation (recommandé)
Si un point de terminaison personnalisé est préexistant...
- À partir de Braze iOS SDK v3.0.2, vous pouvez définir un point de terminaison personnalisé en utilisant le fichier `Info.plist`. Ajoutez le dictionnaire `Appboy` à votre fichier Info.plist. À l'intérieur du dictionnaire `Appboy` , ajoutez la sous-entrée de chaîne `Endpoint` et définissez la valeur à l'autorité de votre URL de terminaison personnalisée (par exemple, `sdk. ad-01.braze.com`, pas `https://sdk.iad-01.braze.com`).

#### Configuration du point de terminaison d'exécution

Si un point de terminaison personnalisé est préexistant...
- Commence avec Braze iOS SDK v3.17. +, vous pouvez surcharger votre point de terminaison via la `ABKEndpointKey` dans le paramètre `appboyOptions` passé à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez la valeur à l'autorité de votre URL de terminaison personnalisée (par exemple, `sdk.iad-01.braze.com`, pas `https://sdk.iad-01.braze.com`).

{% alert note %}
La prise en charge des terminaux lors de l'exécution en utilisant `ABKAppboyEndpointDelegate` a été supprimée dans Braze iOS SDK v3.17.0. Si vous utilisez déjà `ABKAppboyEndpointDelegate`, notez que dans Braze iOS SDK versions v3.14.1 à v3.16.0, toute référence à `dev. ppboy.com` dans votre méthode `getApiEndpoint()` doit être remplacé par une référence à `sdk.iad-01.braze.com`.
{% endalert %}

{% alert important %}
Pour connaître votre grappe spécifique, veuillez vous adresser à votre Responsable du Service Clientèle ou contacter notre équipe d'assistance.
{% endalert %}

### Intégration du SDK terminée

Braze devrait maintenant collecter des données de votre application et votre intégration de base devrait être complète. Veuillez noter que lors de la compilation de votre application tvOS et de toute autre bibliothèque tierce, Bitcode doit être activé.

### Mise à jour du Braze SDK via CocoaPods

Pour mettre à jour une Cocoapod exécutez simplement les commandes suivantes dans le répertoire de votre projet :

```
mise à jour du pod
```

## Personnalisation de Braze au démarrage

Si vous souhaitez personnaliser Braze au démarrage, vous pouvez à la place utiliser la méthode d'initialisation de Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` et passer dans un `NSDictionary` optionnel de clés de démarrage de Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

Dans votre fichier `AppDelegate.m` , dans votre application `: didFinishLaunchingWithOptions` , ajoutez la méthode Braze suivante :

```objc
[Appboy startWithApiKey:@"VOTRE API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

Dans `AppDelegate.swift`, dans votre application `(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` méthode, ajouter la méthode Braze suivante :

```swift
Appboy.start(withApiKey: "VOTRE-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

où `appboyOptions` est un `dictionnaire` de valeurs de configuration de démarrage.

{% endtab %}
{% endtabs %}

__Note__: Cette méthode remplacerait le `startWithApiKey:inApplication:withLaunchOptions:` méthode d'initialisation d'en haut.

Cette méthode est appelée avec les paramètres suivants :

- `YOUR-API-KEY` – La clé API de votre application à partir du tableau de bord Braze
- `application` – L'application actuelle
- `launchOptions` – Les options `NSDictionary` que vous obtenez de `application:didFinishLaunchingWithOptions :`
- `appboyOptions` – Une option `NSDictionary` avec des valeurs de configuration de démarrage pour Braze

Voir [Appboy.h][apple_initial_setup_5] pour une liste des clés de démarrage de Braze.

## Appboy.sharedInstance() et Swift nullability
Différente quelque peu de la pratique courante, le singleton `Appboy.sharedInstance()` est facultatif. La raison en est que, comme indiqué ci-dessus, `sharedInstance` est `nul` avant `startWithApiKey :` est appelée, et il y a des implémentations non standards mais non non valides dans lesquelles une initialisation retardée peut être utilisée.

Si vous appelez `startWithApiKey :` dans votre `didFinishLaunchingWithOptions :` déléguer avant tout accès à `sharedInstance` (l'implémentation standard), vous pouvez utiliser le chaînage optionnel, comme `Appboy. haredInstance()?.changeUser("testUser")`, pour éviter les vérifications encombrantes. Cela aura la parité avec une implémentation Objective-C qui a supposé une `sharedInstance` non nulle.

## Options d'intégration manuelle

Vous pouvez également intégrer notre SDK tvOS manuellement - il suffit de récupérer le Framework de notre [Public Repo][1] et d'initialiser Braze comme décrit ci-dessus.

## Identifier les utilisateurs et rapporter des analyses
Consultez notre documentation [iOS][3] pour plus d'informations sur la configuration des identifiants d'utilisateur, la journalisation des événements personnalisés, les paramètres des attributs des utilisateurs. Vous devriez également consulter nos notes sur [les conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).
[apple_initial_setup_15]: {% image_buster /assets/img_archive/podsworkspace.png %} [apple_initial_setup_21]: {{ site.baseurl }}/partner_integrations/#attribution-integration [apple_initial_setup_31]: {{ site.baseurl }}/developer_guide/rest_api/basics/#endpoints [apple_initial_setup_32]: {{ site.baseurl }}/support_contact/

[1]: https://github.com/appboy/appboy-ios-sdk
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[support]: {{site.baseurl}}/braze_support/
[apple_initial_setup_1]: http://cocoapods.org/
[apple_initial_setup_1]: http://cocoapods.org/
[apple_initial_setup_2]: https://www.ruby-lang.org/en/installation/
[apple_initial_setup_3]: http://guides.cocoapods.org/using/getting-started.html "CocoaPods Installation Directions"
[apple_initial_setup_5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[apple_initial_setup_25]: http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods Troubleshooting Guide"
