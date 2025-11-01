## Intégration du SDK Swift

Vous pouvez intégrer et personnaliser le SDK Swift à l'aide du gestionnaire de paquets swift (SPM), de CocoaPods ou de méthodes d'intégration manuelles. Pour plus d'informations sur les différents symboles du SDK, consultez la [documentation de référence de Braze Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/).

### Conditions préalables

Avant de commencer, vérifiez que votre environnement est pris en charge par la [dernière version du SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk#version-information).

### Étape 1 : Installez le SDK Swift de Braze

Nous vous recommandons d'utiliser le [gestionnaire de paquets swift (SwiftPM](https://swift.org/package-manager/) ) ou [CocoaPods](http://cocoapods.org/) pour installer le SDK Swift de Braze. Vous pouvez également installer le SDK manuellement.

{% tabs local %}
{% tab Gestionnaire de paquets Swift %}
#### Étape 1.1 : Importer la version SDK

Ouvrez votre projet et naviguez vers les paramètres de votre projet. Sélectionnez l'onglet **Paquets Swift** et cliquez sur le bouton d'ajout <i class="fas fa-plus"></i> sous la liste des paquets.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
À partir de la version 7.4.0, le SDK Braze Swift dispose de canaux de distribution supplémentaires sous la forme de [XCFrameworks statiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) et de [XCFrameworks dynamiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Si vous souhaitez utiliser l'un de ces formats à la place, suivez les instructions d'installation de leur dépôt respectif.
{% endalert %}

Saisissez l'URL de notre référentiel de SDK Swift iOS `https://github.com/braze-inc/braze-swift-sdk` dans le champ de texte. Dans la section **Dependency Rule (Règle de dépendance)**, sélectionnez la version du SDK. Enfin, cliquez sur **Ajouter un paquet**.

![]({% image_buster /assets/img/importsdk_example.png %})

#### Étape 1.2 : Sélectionnez vos paquets

Le SDK Swift de Braze sépare les fonctionnalités en bibliothèques autonomes pour offrir aux développeurs un meilleur contrôle sur les fonctionnalités à importer dans leurs projets.

| Offre         | Détails                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | Bibliothèque SDK principale avec prise en charge des analyses et des notifications push.                                                                                        |
| `BrazeLocation` | Bibliothèque de localisations avec prise en charge des analyses de localisation et de la surveillance des géorepérages.                                                                              |
| `BrazeUI`       | Bibliothèque d'interface utilisateur fournie par Braze pour les messages in-app, les cartes de contenu et les bannières. Importez cette bibliothèque si vous avez l'intention d'utiliser les composants d'interface utilisateur par défaut. |

{: .ws-td-nw-1}

##### À propos des bibliothèques de vulgarisation

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) et [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) sont des modules d'extension qui fournissent des fonctionnalités supplémentaires et ne doivent pas être ajoutés directement à la cible de votre application principale. Suivez plutôt les guides liés pour les intégrer séparément dans leurs extensions cibles respectives.
{% endalert %}

| Offre                    | Détails                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | Bibliothèque d'extension du service de notification prenant en charge les notifications push riches. |
| `BrazePushStory`           | Bibliothèque d'extension de contenu de notification fournissant un support pour les contenus push.            |

{: .ws-td-nw-1}

Sélectionnez le paquet qui correspond le mieux à vos besoins et cliquez sur **Ajouter un paquet**. Veillez à sélectionner au moins `BrazeKit`.

![]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### Étape 1.1 : Installer CocoaPods

Pour une description complète, consultez le [guide de démarrage de](https://guides.cocoapods.org/using/getting-started.html) CocoaPods. Sinon, vous pouvez exécuter la commande suivante pour commencer rapidement :

```bash
$ sudo gem install cocoapods
```

Si vous êtes bloqué, consultez le guide de résolution des problèmes de CocoaPods.

#### Étape 1.2 : Construction du Podfile

Ensuite, créez un fichier dans le répertoire de votre projet Xcode nommé `Podfile`.

{% alert note %}
À partir de la version 7.4.0, le SDK Braze Swift dispose de canaux de distribution supplémentaires sous la forme de [XCFrameworks statiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) et de [XCFrameworks dynamiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Si vous souhaitez utiliser l'un de ces formats à la place, suivez les instructions d'installation de leur dépôt respectif.
{% endalert %}

Ajoutez la ligne suivante à votre Podfile :

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` contient la bibliothèque principale du SDK, avec la prise en charge des analyses et des notifications push.

Nous vous suggérons la version Braze afin que les mises à jour du pod récupèrent automatiquement tout ce qui est plus petit qu’une mise à jour mineure de la version. Cela ressemble à `pod 'BrazeKit' ~> Major.Minor.Build`. Si vous souhaitez intégrer automatiquement la dernière version de Braze SDK, même avec des modifications majeures, vous pouvez utiliser `pod 'BrazeKit'` dans votre Podfile.

##### A propos des bibliothèques supplémentaires

Le SDK Swift de Braze sépare les fonctionnalités en bibliothèques autonomes pour offrir aux développeurs un meilleur contrôle sur les fonctionnalités à importer dans leurs projets. En plus de `BrazeKit`, vous pouvez ajouter les bibliothèques suivantes à votre Podfile :

| Bibliothèque               | Détails                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | Bibliothèque de localisations avec prise en charge des analyses de localisation et de la surveillance des géorepérages.                                                                              |
| `pod 'BrazeUI'`       | Bibliothèque d'interface utilisateur fournie par Braze pour les messages in-app, les cartes de contenu et les bannières. Importez cette bibliothèque si vous avez l'intention d'utiliser les composants d'interface utilisateur par défaut. |

{: .ws-td-nw-1}

###### Bibliothèques d'extension

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) et [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) sont des modules d'extension qui fournissent des fonctionnalités supplémentaires et ne doivent pas être ajoutés directement à la cible de votre application principale. Au lieu de cela, vous devrez créer des cibles d'extension distinctes pour chacun de ces modules et importer les modules Braze dans leurs cibles correspondantes.

| Bibliothèque                          | Détails                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | Bibliothèque d'extension du service de notification prenant en charge les notifications push riches. |
| `pod 'BrazePushStory'`           | Bibliothèque d'extension de contenu de notification fournissant un support pour les contenus push.            |

{: .ws-td-nw-1}

#### Étape 1.3 : Installer le SDK

Pour installer le SDK Cocoapod Braze, accédez au répertoire de votre projet d’application Xcode au sein de votre terminal et exécutez la commande suivante :
```
pod install
```

À ce stade, vous devriez pouvoir ouvrir le nouvel espace de travail du projet Xcode créé par CocoaPods. Assurez-vous d’utiliser cet espace de travail Xcode au lieu de votre projet Xcode.

![Un dossier d'exemple de Braze agrandi pour montrer le nouveau `BrazeExample.workspace`.]({% image_buster /assets/img/braze_example_workspace.png %})

#### Mise à jour du SDK à l'aide de CocoaPods

Pour mettre à jour un Cocoapod, il vous suffit de lancer la commande suivante dans votre répertoire de projet :

```
pod update
```
{% endtab %}

{% tab Manual (Manuel) %}
#### Étape 1.1 : Téléchargez le SDK Braze

Accédez à la [page du SDK Braze sur GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), puis téléchargez `braze-swift-sdk-prebuilt.zip`.

![Page du SDK Braze sur GitHub.]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### Étape 1.2 : Choisissez vos frameworks

Le SDK Swift Braze contient une série de XCFrameworks autonomes, ce qui vous donne la liberté d'intégrer les fonctionnalités que vous souhaitez sans avoir besoin de toutes les intégrer. Référez-vous au tableau suivant pour choisir vos XCFrameworks :

| Offre                    | Requis ? | Description                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Oui       | Bibliothèque SDK principale avec prise en charge des analyses et des notifications push.                                                                                                                                                                                                                                                         |
| `BrazeLocation`            | Non        | Bibliothèque de localisations avec prise en charge des analyses de localisation et de la surveillance des géorepérages.                                                                                                                                                                                                                                               |
| `BrazeUI`                  | Non        | Bibliothèque d'interface utilisateur fournie par Braze pour les messages in-app, les cartes de contenu et les bannières. Importez cette bibliothèque si vous avez l'intention d'utiliser les composants d'interface utilisateur par défaut.                                                                                                                                                                      |
| `BrazeNotificationService` | Non        | Bibliothèque d'extension de service de notification qui fournit une prise en charge des notifications push enrichies. N'ajoutez pas cette bibliothèque directement à la cible de votre application principale, mais [ajoutez plutôt la bibliothèque `BrazeNotificationService` séparément](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).                 |
| `BrazePushStory`           | Non        | Bibliothèque d'extension de contenu de notification qui fournit une prise en charge des Push Stories. N'ajoutez pas cette bibliothèque directement à la cible de votre application principale, mais [ajoutez plutôt la bibliothèque `BrazePushStory` séparément](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                                 |
| `BrazeKitCompat`           | Non        | Bibliothèque de compatibilité contenant toutes les classes et méthodes `Appboy` et `ABK*` qui étaient disponibles dans le `Appboy-iOS-SDK` version 4.X.X. Pour plus de détails sur l'utilisation, reportez-vous au scénario de migration minimal dans le [guide de migration](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/).            |
| `BrazeUICompat`            | Non        | Bibliothèque de compatibilité contenant toutes les classes et méthodes `ABK*` qui étaient disponibles dans la bibliothèque `AppboyUI` du `Appboy-iOS-SDK` version 4.X.X. Pour plus de détails sur l'utilisation, reportez-vous au scénario de migration minimal dans le [guide de migration](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | Non        | Dépendance utilisée uniquement par `BrazeUICompat` dans le scénario de migration minimal.                                                                                                                                                                                                                                                           |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Étape 1.3 : Préparez vos fichiers

Décidez si vous souhaitez utiliser des XCFrameworks **statiques** ou **dynamiques**, puis préparez vos fichiers :

1. Créez un répertoire temporaire pour vos XCFrameworks.
2. Dans `braze-swift-sdk-prebuilt`, ouvrez le répertoire `dynamic` et déplacez `BrazeKit.xcframework` dans votre répertoire. Votre répertoire devrait être similaire à ce qui suit :
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Déplacez chacun de vos [XCFrameworks choisis](#swift_step-2-choose-your-frameworks) dans votre répertoire temporaire. Votre répertoire devrait être similaire à ce qui suit :
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### Étape 1.4 : Intégrez vos frameworks

Ensuite, intégrez les XCFrameworks **dynamiques** ou **statiques** que vous [avez préparés précédemment](#swift_step-3-prepare-your-files) :

Dans votre projet Xcode, sélectionnez votre cible de build, puis **Général**. Sous **Frameworks, bibliothèques et contenu intégré**, faites glisser et déposez les [fichiers que vous avez préparés précédemment](#swift_step-3-prepare-your-files).

![Exemple de projet Xcode avec chaque bibliothèque Braze définie sur Intégrer et signer.]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
À partir du SDK Swift 12.0.0, vous devez toujours sélectionner **Embed & Sign** pour les XCFrameworks de Braze, tant pour les variantes statiques que dynamiques. Cela permet de s'assurer que les ressources des frameworks sont correctement intégrées dans votre bundle d'application.
{% endalert %}

{% alert tip %}
Pour activer la prise en charge du format GIF, ajoutez `SDWebImage.xcframework`, situé dans `braze-swift-sdk-prebuilt/static` ou `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}

#### Erreurs courantes pour les projets Objective-C

Si votre projet Xcode ne contient que des fichiers Objective-C, il se peut que vous obteniez des erreurs de « symbole manquant » lorsque vous essayez de créer votre projet. Pour corriger ces erreurs, ouvrez votre projet et ajoutez un fichier Swift vide à votre arborescence de fichiers. Ceci obligera votre chaîne d'outils de création à intégrer [Swift Runtime](https://support.apple.com/kb/dl1998) et à lier les frameworks appropriés pendant le temps de création.

```bash
FILE_NAME.swift
```

Remplacez `FILE_NAME` par n'importe quelle chaîne sans espace. Votre fichier devrait ressembler à ce qui suit :

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### Étape 2 : Configuration de l'initialisation différée (en option)

Vous pouvez choisir de retarder l'initialisation du SDK Braze Swift, ce qui est utile si votre application doit charger la configuration ou attendre le consentement de l'utilisateur avant de démarrer le SDK. L'initialisation différée garantit que les notifications push de Braze sont mises en file d'attente jusqu'à ce que le SDK soit prêt.

Pour ce faire, appelez `Braze.prepareForDelayedInitialization()` le plus tôt possible - idéalement à l'intérieur ou avant votre `application(_:didFinishLaunchingWithOptions:)`.

{% alert note %}
Cela s'applique uniquement aux notifications push de Braze. Les autres notifications push sont gérées normalement par les délégués du système.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objectif-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
[`Braze.prepareForDelayedInitialization(pushAutomation:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) accepte un paramètre facultatif `pushAutomation`. Si la valeur est `nil`, toutes les fonctionnalités d'automatisation du push sont activées, à l'exception de la demande d'autorisation du push au lancement.
{% endalert %}

### Étape 3 : Mettre à jour la délégation de votre application

{% alert important %}
Ce qui suit suppose que vous avez déjà ajouté un `AppDelegate` à votre projet (qui n'est pas généré par défaut). Si vous ne prévoyez pas d'en utiliser un, veillez à initialiser le SDK de Braze le plus tôt possible, par exemple lors du lancement de l'application.
{% endalert %}

{% subtabs local %}
{% subtab swift %}
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

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs local %}

## Configurations optionnelles

### Journalisation

#### Niveaux de journalisation

Le niveau de journalisation par défaut pour le SDK Braze Swift est `.error`- c'est également le niveau minimum pris en charge lorsque les journaux sont activés. Voici la liste complète des niveaux de journalisation :

| Swift       | Objectif-C              | Description                                                  |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | (Par défaut) Enregistre les informations de débogage + `.info` + `.error`.    |
| `.info`     | `BRZLoggerLevelInfo`     | Enregistrer des informations générales sur le SDK (changements au niveau des utilisateurs, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Erreurs de journalisation.                                                  |
| `.disabled` | `BRZLoggerLevelDisabled` | Aucun enregistrement n'a lieu.                                           |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Réglage du niveau de journalisation

Vous pouvez attribuer le niveau de journalisation au moment de l'exécution dans votre objet `Braze.Configuration`. Pour plus de détails sur l'utilisation, voir [`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}
