---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour tvOS
platform: tvOS
page_order: 0
page_type: reference
description: "Cette page couvre les étapes de configuration initiales du SDK Braze pour tvOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuration initiale du SDK

> Cet article de référence explique comment installer le SDK Braze pour tvOS. L’installation du SDK Braze vous fournira des fonctionnalités d’analyse de base.

{% alert note %}
Notre SDK tvOS prend actuellement en charge la fonctionnalité d’analyse. Pour ajouter une appli tvOS dans votre tableau de bord, ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).
{% endalert %}

Le SDK Braze pour tvOS doit être installé ou mis à jour à l’aide de [CocoaPods](http://cocoapods.org/), un gestionnaire de dépendances pour les projets Objective-C et Swift. CocoaPods offre une simplicité supplémentaire pour l’intégration et la mise à jour.

## Intégration SDK CocoaPods de tvOS

### Étape 1 : Installer CocoaPods

L’installation du SDK via le tvOS [CocoaPods](http://cocoapods.org/) permet d’automatiser la majeure partie du processus d’installation. Avant de commencer ce processus, assurez-vous que vous utilisez la [version Ruby 2.0.0](https://www.ruby-lang.org/en/installation/) ou une version ultérieure.

Exécutez la commande suivante pour démarrer :

```bash
$ sudo gem install cocoapods
```

- Si vous êtes invité à écraser l'exécutable `rake`, reportez-vous à la section [Démarrage - CocoaPods](http://guides.cocoapods.org/using/getting-started.html "Instructions d'installation de") sur CocoaPods.org pour plus de détails.
- Si vous avez des problèmes concernant CocoaPods, reportez-vous au [guide de résolution des problèmes de CocoaPodsCocoaPods](http://guides.cocoapods.org/using/troubleshooting.html "Troubleshooting Guide.")

### Étape 2 : Construction du Podfile

Maintenant que vous avez installé CocoaPods Ruby Gem, vous devez créer un fichier dans votre répertoire de projet Xcode nommé `Podfile`.

Ajoutez la ligne suivante à votre Podfile :

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

Nous vous suggérons la version Braze afin que les mises à jour du pod récupèrent automatiquement tout ce qui est plus petit qu’une mise à jour mineure de la version. Cela ressemble à `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`. Si vous souhaitez intégrer automatiquement la dernière version de Braze SDK, même avec des modifications majeures, vous pouvez utiliser `pod 'Appboy-tvOS-SDK'` dans votre Podfile.

### Étape 3 : Installer le SDK Braze

Pour installer le SDK CocoaPods Braze, accédez au répertoire de votre projet d’application Xcode au sein de votre terminal et exécutez la commande suivante :
```
pod install
```

À ce stade, vous devriez pouvoir ouvrir le nouvel espace de travail du projet Xcode créé par CocoaPods. Assurez-vous d’utiliser cet espace de travail Xcode au lieu de votre projet Xcode. 

![]({% image_buster /assets/img_archive/podsworkspace.png %})

### Étape 4 : Mettre à jour la délégation de votre application

{% tabs %}
{% tab OBJECTIF-C %}

Ajoutez la ligne de code suivante à votre fichier `AppDelegate.m` :

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

Dans votre fichier `AppDelegate.m`, ajoutez l’extrait de code suivant au sein de votre méthode `application:didFinishLaunchingWithOptions` :

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Enfin, mettez à jour `YOUR-API-KEY` avec la valeur correcte à partir de votre page **Gérer les paramètres**.

{% endtab %}
{% tab swift %}

Si vous intégrez le SDK Braze avec des CocoaPods, Carthage ou via une intégration manuelle dynamique, ajoutez la ligne de code suivante à votre fichier `AppDelegate.swift` :

```swift
import AppboyTVOSKit
```

Pour plus d'informations sur l'utilisation du code Objective-C dans les projets Swift, consultez la [documentation du développeur Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Dans `AppDelegate.swift`, ajoutez l’extrait de code suivant à votre `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` :

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Ensuite, mettez à jour `YOUR-API-KEY` avec la valeur correcte à partir de votre page **Gérer les paramètres.** 

Notre singleton `sharedInstance` sera nul avant que `startWithApiKey:` ne soit appelé, car il s'agit d'une condition préalable à l'utilisation de toute fonctionnalité de Braze.

{% endtab %}
{% endtabs %}

{% alert warning %}
Assurez-vous d’initialiser Braze dans le fil principal de votre application. L’initialisation asynchrone peut entraîner un échec de la fonctionnalité.
{% endalert %}

### Étape 5 : Spécifiez votre endpoint ou cluster de données personnalisé

{% alert note %}
À partir de décembre 2019, les endpoints personnalisés ne sont plus fournis. Si vous disposez d’un endpoint personnalisé préexistant, vous pouvez continuer à l’utiliser. Pour plus de détails, consultez notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste d’endpoints disponibles</a>.
{% endalert %}

Votre conseiller Braze devrait déjà vous avoir indiqué le [endpoint correct]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuration des endpoints de compilation (recommandée)
Si vous avez un endpoint personnalisé préexistant :
- À partir du SDK Braze pour iOS v3.0.2, vous pouvez définir un endpoint personnalisé à l’aide du fichier `Info.plist`. Ajouter le dictionnaire `Appboy` à votre fichier Info.plist. À l’intérieur du dictionnaire `Appboy`, ajoutez la sous-entrée de chaîne de caractères `Endpoint` et définissez la valeur sur l'autorité de votre URL d’endpoint personnalisé (par exemple, `sdk.iad-01.braze.com`, et non `https://sdk.iad-01.braze.com`).

#### Configuration du endpoint d’exécution
Si vous avez un endpoint personnalisé préexistant :
- À partir du SDK Braze pour iOS v3.17.0+, vous pouvez remplacer votre endpoint par `ABKEndpointKey` à l’intérieur du paramètre `appboyOptions` transmis à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez la valeur sur l'autorité de votre URL d’endpoint personnalisé (par exemple, `sdk.iad-01.braze.com`, et non `https://sdk.iad-01.braze.com`).

{% alert note %}
La prise en charge de la configuration des endpoints lors de l’exécution à l’aide de `ABKAppboyEndpointDelegate` a été supprimée dans le SDK Braze pour iOS v3.17.0. Si vous utilisez déjà `ABKAppboyEndpointDelegate`, notez que dans les versions de la version 3.14.1 à v3.16.0 du SDK Braze pour iOS, toute référence à `dev.appboy.com` dans votre méthode `getApiEndpoint()` doit être remplacé par une référence à `sdk.iad-01.braze.com`.
{% endalert %}

### Intégration SDK terminée

Braze devrait maintenant collecter des données depuis votre application et votre intégration de base devrait être terminée. Notez que lors de la compilation de votre application tvOS et de toute autre bibliothèque tierce, Bitcode doit être activé.

### Mettre à jour le SDK Braze par CocoaPods

Pour mettre à jour un CocoaPod, exécutez simplement les commandes suivantes dans votre répertoire de projet :

```
pod update
```

## Personnaliser Braze au démarrage

Si vous souhaitez personnaliser Braze au démarrage, vous pouvez utiliser la méthode d’initialisation Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` et transmettre un `NSDictionary` facultatif des touches de démarrage Braze.
{% tabs %}
{% tab OBJECTIF-C %}

Dans votre fichier `AppDelegate.m`, au sein de votre méthode `application:didFinishLaunchingWithOptions`, ajoutez la méthode Braze suivante :

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

Dans `AppDelegate.swift`, au sein de votre méthode `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, ajoutez la méthode Braze suivante :

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

où `appboyOptions` est un `Dictionary` de valeurs de configuration de démarrage.

{% endtab %}
{% endtabs %}

Cette méthode remplacera la méthode d’initialisation `startWithApiKey:inApplication:withLaunchOptions:` et sera employée avec les paramètres suivants :

- `YOUR-API-KEY` : La clé API de votre application se trouve sous **Gérer les paramètres** dans le tableau de bord de Braze.
- `application` : L’application actuelle.
- `launchOptions` : Les options `NSDictionary` que vous obtenez de `application:didFinishLaunchingWithOptions:`.
- `appboyOptions` : Un `NSDictionary` facultatif avec les valeurs de configuration de démarrage de Braze.

Voir [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) pour obtenir la liste des touches de démarrage de Braze.

## Valeurs nulles Swift et Appboy.sharedInstance()
Légèrement différent de la pratique courante, le singleton `Appboy.sharedInstance()` est facultatif. Cela est dû au fait que `sharedInstance` est `nil` avant l’appel de `startWithApiKey:`, et qu’il existe des implémentations non standard et non valides dans lesquelles une initialisation retardée peut être utilisée.

Si vous utilisez `startWithApiKey:` dans votre délégation `didFinishLaunchingWithOptions:` avant tout accès à `sharedInstance` d’Appboy (l’implémentation standard), vous pouvez utiliser des chaînages facultatifs, comme `Appboy.sharedInstance()?.changeUser("testUser")`, pour éviter des vérifications fastidieuses. Il y aura parité avec une implémentation Objective-C qui a supposé un `sharedInstance` non nul.

## Options d’intégration manuelle

Vous pouvez également intégrer notre SDK tvOS manuellement - il vous suffit de récupérer le Framework depuis notre [Dépôt public](https://github.com/appboy/appboy-ios-sdk) et d'initialiser Braze comme indiqué dans les sections précédentes.

## Identification des utilisateurs et analyse des rapports
Consultez notre [documentation iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) pour obtenir des informations sur la définition des ID utilisateurs, la journalisation des événements personnalisés, la définition des attributs clients. Nous vous recommandons également de vous familiariser avec les [conventions de dénomination de nos événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

