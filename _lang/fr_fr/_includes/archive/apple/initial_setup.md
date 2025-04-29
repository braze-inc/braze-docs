L’installation du SDK Braze vous fournira des fonctionnalités d’analyse de base{% if include.platform == 'iOS' %} ainsi que des messages in-app opérationnels avec lesquels vous pouvez engager vos utilisateurs{% endif %}.

Le SDK Braze pour {{include.platform}} doit être installé ou mis à jour à l’aide de [CocoaPods][apple_initial_setup_1], un gestionnaire de dépendances pour les projets Objective-C et Swift. CocoaPods offre une simplicité supplémentaire pour l’intégration et la mise à jour.

## {{include.platform}} Intégration SDK CocoaPods

### Étape 1 : Installer CocoaPods

L'installation du SDK via le site {{include.platform}} [CocoaPods][apple_initial_setup_1] automatise la majeure partie du processus d'installation pour vous. Avant de commencer ce processus, vérifiez que vous utilisez la [version 2.0.0 de Ruby][apple_initial_setup_2] ou une version ultérieure. Notez qu'il n'est pas nécessaire de connaître la syntaxe de Ruby pour installer ce SDK.

Exécutez simplement la commande suivante pour démarrer :

```bash
$ sudo gem install cocoapods
```

**Remarque** : Si vous êtes invité à remplacer l’exécutable `rake`, reportez-vous à la rubrique [Instructions de démarrage sur CocoaPods.org][apple_initial_setup_3] pour plus de détails.

**Remarque** : Si vous rencontrez des problèmes concernant CocoaPods, veuillez consulter le [Guide de résolution des problèmes CocoaPods][apple_initial_setup_25].

### Étape 2 : Construction du Podfile

Maintenant que vous avez installé CocoaPods Ruby Gem, vous devez créer un fichier dans votre répertoire de projet Xcode nommé `Podfile`.

Ajoutez la ligne suivante à votre Podfile :

```
target 'YourAppTarget' do
  pod 'Appboy-{{include.platform}}-SDK'
end
```

**Remarque** : Nous vous suggérons la version Braze afin que les mises à jour du pod récupèrent automatiquement tout ce qui est plus petit qu’une mise à jour mineure de la version. Cela se présente sous la forme 'pod 'Appboy-{{include.platform}}-SDK' ~> Major.Minor.Build'. Si vous souhaitez intégrer automatiquement la toute dernière version du SDK Braze, même avec des modifications majeures, vous pouvez utiliser `pod 'Appboy-{{include.platform}}-SDK'` dans votre Podfile.
{% if include.platform == 'iOS' %}
**Remarque** : Si vous n’utilisez pas l’IU Braze par défaut et que vous ne souhaitez pas introduire la dépendance SDWebImage, veuillez pointer votre dépendance Braze dans votre Podfile vers notre sous-spécification Core, comme `pod 'Appboy-iOS-SDK/Core'` dans votre Podfile. {% endif %}

### Étape 3 : Installer le SDK Braze

Pour installer le SDK CocoaPods Braze, accédez au répertoire de votre projet d’application Xcode au sein de votre terminal et exécutez la commande suivante :
```
pod install
```

À ce stade, vous devriez pouvoir ouvrir le nouvel espace de travail du projet Xcode créé par CocoaPods. Assurez-vous d’utiliser cet espace de travail Xcode au lieu de votre projet Xcode. 

![Nouvel espace de travail][apple_initial_setup_15]

### Étape 4 : Mettre à jour la délégation de votre application

{% tabs %}
{% tab OBJECTIF-C %}

Ajoutez la ligne de code suivante à votre fichier `AppDelegate.m` :

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

Dans votre fichier `AppDelegate.m`, ajoutez l’extrait de code suivant au sein de votre méthode `application:didFinishLaunchingWithOptions` :

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Si vous intégrez le SDK Braze avec des CocoaPods, Carthage ou via une intégration manuelle dynamique, ajoutez la ligne de code suivante à votre fichier `AppDelegate.swift` :

```swift
{% if include.platform == 'iOS' %}import Appboy_iOS_SDK{% else %}import AppboyTVOSKit{% endif %}
```

Pour plus d’informations sur l’utilisation du code Objective-C dans les projets Swift, consultez la [documentation des développeurs Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Dans `AppDelegate.swift`, ajoutez l’extrait de code suivant à votre `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` :

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

**Remarque** : Le singleton `sharedInstance` de Braze sera nul avant que `startWithApiKey:` ne soit appelé, car il s'agit d'une condition préalable à l'utilisation de toute fonctionnalité de Braze.

{% endtab %}
{% endtabs %}

{% alert important %}
Veillez à mettre à jour `YOUR-API-KEY` avec la valeur correcte à partir de votre page Gérer les paramètres.
{% endalert %}

{% alert warning %}
Assurez-vous d’initialiser Braze dans le fil principal de votre application. L’initialisation asynchrone peut entraîner un échec de la fonctionnalité.
{% endalert %}


### Étape 5 : Spécifiez votre endpoint ou cluster de données personnalisé

{% alert note %}
Depuis décembre 2019, les endpoints personnalisés ne sont plus distribués ; si vous avez un endpoint personnalisé préexistant, vous pouvez continuer à l’utiliser. Pour plus de détails, consultez notre <a href="{{site.baseurl}}/api/basics/#endpoints">liste d’endpoints disponibles</a>.
{% endalert %}

Votre conseiller Braze devrait déjà vous avoir indiqué le [endpoint correct]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuration des endpoints de compilation (recommandée)
Si un endpoint personnalisé préexistant est donné...
- À partir du SDK Braze pour iOS v3.0.2, vous pouvez définir un endpoint personnalisé à l’aide du fichier `Info.plist`. Ajouter le dictionnaire `Appboy` à votre fichier Info.plist. À l’intérieur du dictionnaire `Appboy`, ajoutez la sous-entrée de chaîne `Endpoint` et définissez la valeur à l’autorité de votre URL d’endpoint personnalisé (par exemple, `sdk.iad-01.braze.com`, pas `https://sdk.iad-01.braze.com`).

#### Configuration du endpoint d’exécution

Si un endpoint personnalisé préexistant est donné...
- À partir du SDK Braze pour iOS v3.17.0+, vous pouvez remplacer votre endpoint par `ABKEndpointKey` à l’intérieur du paramètre `appboyOptions` transmis à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez la valeur à l’autorité de votre URL d’endpoint personnalisé (par exemple, `sdk.iad-01.braze.com`, pas `https://sdk.iad-01.braze.com`).

{% alert note %}
La prise en charge de la configuration des endpoints lors de l’exécution à l’aide de `ABKAppboyEndpointDelegate` a été supprimée dans le SDK Braze pour iOS v3.17.0. Si vous utilisez déjà `ABKAppboyEndpointDelegate`, notez que dans les versions de la version 3.14.1 à v3.16.0 du SDK Braze pour iOS, toute référence à `dev.appboy.com` dans votre méthode `getApiEndpoint()` doit être remplacé par une référence à `sdk.iad-01.braze.com`.
{% endalert %}

{% alert important %}
Pour découvrir votre groupe spécifique, veuillez vous adresser à votre gestionnaire du succès des clients ou contacter notre équipe d’assistance.
{% endalert %}

### Intégration SDK terminée

Braze devrait maintenant collecter des données depuis votre application et votre intégration de base devrait être terminée. {% if include.platform == 'iOS' %}Veuillez consulter les sections suivantes afin d'activer le suivi des événements personnalisés, les messages push, le fil d'actualité et la suite complète des fonctionnalités de Braze.{% else %}Veuillez noter que lors de la compilation de votre application tvOS et de toute autre bibliothèque tierce, le Bitcode doit être activé.{% endif %}

### Mettre à jour le SDK Braze par CocoaPods

Pour mettre à jour un Cocoapod, exécutez les commandes suivantes dans votre répertoire de projet :

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

**Remarque** : Cette méthode remplacerait la méthode d’initialisation `startWithApiKey:inApplication:withLaunchOptions:`.

Cette méthode est utilisée avec les paramètres suivants :

- `YOUR-API-KEY` : la clé API de votre application depuis le tableau de bord de Braze
- `application` : l’application actuelle
- `launchOptions` : les options `NSDictionary` que vous obtenez de `application:didFinishLaunchingWithOptions:`
- `appboyOptions` : un `NSDictionary` facultatif contenant les valeurs de configuration de démarrage de Braze

Voir [Appboy.h][apple_initial_setup_5] pour obtenir la liste des touches de démarrage de Braze.

## Valeurs nulles Swift et Appboy.sharedInstance()
Légèrement différent de la pratique courante, le singleton `Appboy.sharedInstance()` est facultatif. Cela est dû au fait que `sharedInstance` est `nil` avant l’appel de `startWithApiKey:`, et qu’il existe des implémentations non standard et non valides dans lesquelles une initialisation retardée peut être utilisée.

Si vous utilisez `startWithApiKey:` dans votre délégation `didFinishLaunchingWithOptions:` avant tout accès à `sharedInstance` d’Appboy (l’implémentation standard), vous pouvez utiliser des chaînages facultatifs, comme `Appboy.sharedInstance()?.changeUser("testUser")`, pour éviter des vérifications fastidieuses. Il y aura parité avec une implémentation Objective-C qui a supposé un `sharedInstance` non nul.

[apple_initial_setup_1]: http://cocoapods.org/
[apple_initial_setup_2]: https://www.ruby-lang.org/en/installation/
[apple_initial_setup_3]: http://guides.cocoapods.org/using/getting-started.html "Instructions pour l'installation de CocoaPods"
[apple_initial_setup_4]: http://guides.cocoapods.org/syntax/podfile.html
[apple_initial_setup_5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[apple_initial_setup_8]: #manual-sdk-integration
[apple_initial_setup_12]: #appboy-podfiles-for-non-64-bit-apps
[apple_initial_setup_15]: {% image_buster /assets/img_archive/podsworkspace.png %}
[apple_initial_setup_17]: http://guides.cocoapods.org/using/getting-started.html#updating-cocoapods
[apple_initial_setup_19]: https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html
[apple_initial_setup_21]: {{ site.baseurl }}/partner_integrations/#attribution-integration
[apple_initial_setup_25]: http://guides.cocoapods.org/using/troubleshooting.html "Guide de résolution des problèmes de CocoaPods"
[apple_initial_setup_27]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md "iOS Changelog"
[apple_initial_setup_31]: {{ site.baseurl }}/developer_guide/rest_api/basics/#endpoints
[apple_initial_setup_32]: {{ site.baseurl }}/support_contact/
