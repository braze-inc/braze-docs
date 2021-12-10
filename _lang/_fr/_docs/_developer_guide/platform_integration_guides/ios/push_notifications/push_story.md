---
nav_title: Envoyer des histoires
article_title: Envoyer des histoires pour iOS
platform: iOS
page_order: 28
description: "Cet article montre comment configurer Push Stories pour votre application iOS."
channel:
  - Pousser
---

# Configuration de l'Histoire Push

La fonction Push Story nécessite le Framework de Notification et iOS 10. La fonctionnalité n'est disponible que depuis iOS SDK version 3.2.1.

## Étape 1 : Activez le push dans votre application

Veuillez suivre [L'intégration des notifications Push][1] pour activer le push dans votre application.

## Étape 2 : Ajout de la cible de l'extension de contenu de notification

Dans votre projet d'application, allez dans le menu "Fichier"->"Nouveau"->"Cible...", ajoutez une nouvelle cible "Extension de contenu de notification" et activez-la.

!\[Ajouter une extension de contenu\]\[2\]

Xcode devrait générer une nouvelle cible pour vous et créer des fichiers automatiquement pour vous incluant:

{% tabs %}
{% tab OBJECTIVE-C %}

- `h`
- `NotificationViewController.m`
- `Tableau de bord principal`

{% endtab %}
{% tab swift %}

- `Rapide`
- `Tableau de bord principal`

{% endtab %}
{% endtabs %}

## Étape 3 : Activer les capacités

Le mode d'arrière-plan dans la section Capacités de la cible de l'application principale est requis par la fonction Histoire Push Story . Après avoir activé les modes d'arrière-plan, sélectionnez "Recherche d'arrière-plan" et "Notification à distance".

!\[Activer le mode arrière-plan\]\[3\]

Vous devez également ajouter des `Groupes d'applications de capacité`. Si vous n'avez pas de groupe d'applications dans votre application, allez à la capacité de la cible principale de l'application, activez les `Groupes d'Applications` et cliquez sur le "+". Utilisez l'ID du bundle de votre application pour créer le groupe d'applications. Par exemple, si l'ID du bundle de votre application est `com.company.appname`, vous pouvez nommer votre groupe d'application `group.com.company.appname.xyz`. Vous devez activer les `Groupes d’applications` pour la cible principale de l’application et la cible de l’extension de contenu.

{% alert important %}
Remarque : `Groupes d'Applications` dans ce contexte se réfèrent à l'Apple's [_Groupes d'Applications droit_](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) et non à votre ID de Groupe d'Applications Braze.
{% endalert %}

!\[Ajouter des groupes d'applications\]\[4\]

## Étape 4 : Ajouter le framework Push Story à votre application

### Gestionnaire de paquets rapide

Après avoir suivi le guide d'intégration [Swift Package Manager][5], ajoutez simplement `AppboyPushStory` à votre extension de contenu de notification :

!\[Ajouter AppboyPushStory\]\[6\]

!\[Ajouter AppboyPushStory\]\[7\]

### Cocoapodes

Ajoutez la ligne suivante à votre fichier Podfile:

```ruby
cible 'VotreExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Après la mise à jour du fichier Podfile, accédez au répertoire de votre projet d'application Xcode dans votre terminal et exécutez `pod install`

### Intégration manuelle

Téléchargez la dernière `AppboyPushStory. ip` de la [page de publication de Github][8], décompressez-la et ajoutez les fichiers suivants à l'extension de contenu de notification de votre projet :
- `Ressources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

!\[Ajouter AppboyPushStory.xcframework\]\[9\]

{% alert important %}
Assurez-vous que `Ne pas intégrer` est sélectionné pour `AppboyPushStory.xcframework` sous la colonne `Embed`.
{% endalert %}

Ajoutez le drapeau `-ObjC` à l'extension de contenu de notification de votre projet dans _Paramètres de construction ->Autres drapeaux de lien_.

## Étape 5 : Mise à jour de votre contrôleur d'affichage des notifications

{% tabs %}
{% tab OBJECTIVE-C %}

Dans votre `NotificationViewController.h`, ajoutez les lignes suivantes pour ajouter de nouvelles propriétés et importer les fichiers d'en-tête :

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

Dans votre `NotificationViewController.m`, supprimez l'implémentation par défaut et ajoutez le code suivant :

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  même. ataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               histoiresView:self. toriesView
                                                                  appGroup:@"VOTRE-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option)){
  UNNotificationContentExtensionResponseOption = [self. ataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animée {
  [self. ataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab swift %}

Dans votre `NotificationViewController.swift`, ajoutez la ligne suivante pour importer les fichiers d'en-tête :

```swift
Importer AppboyPushStory
```

Ensuite, supprimez l'implémentation par défaut et ajoutez le code suivant :

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var source de données: ABKStoriesViewDataSource?

  func didReceive(_ notification: UNNotification) {
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "YOUR-APP-GROUP-IDENTIFIER")
  }

  func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    if dataSource != nil {
      let option: UNNotificationContentExtensionResponseOption = dataSource!.didReceive(response)
      completion(option)
    }
  }

  override func viewWillDisappear(_ animated: Bool) {
    dataSource?.viewWillDisappear()
    super.viewWillDisappear(animated)
  }
}
```

{% endtab %}
{% endtabs %}

## Étape 6 : Définissez le storyboard de l'extension de contenu de notification

-       Ouvrez le storyboard de l'extension de contenu de notification et placez un nouveau `UIView` dans le contrôleur de la vue des notifications. Renomme la classe en `ABKStoriesView`. Rendre la largeur de la vue et la hauteur automatiquement redimensionnables correspondant au cadre de vue principale du contrôleur de la vue des notifications.

!\[Voir la classe\]\[10\]

!\[Taille de la vue\]\[11\]

-       Associez l'IBOutlet `storiesView` du contrôleur de notification à l'ajouté `ABKStoriesView`.

!\[Voir Outlet\]\[13\]

## Étape 7 : Définir l'extension de contenu de notification plist

Ouvrir le fichier Info.plist de l'extension de contenu de notification et ajouter/modifier les clés suivantes sous `NSExtension \ NSExtensionAttributes`:

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (`String` type) `UNNotificationExtensionDefaultContentHidden` = `YES` (`Boolean` type) `UNNotificationExtensionInitialContentSizeRatio` = `0.65` (`Number` type)

!\[Réglages de la liste\]\[12\]

## Étape 8 : Mettre à jour l'intégration de Braze dans votre application principale

##### Option 1 : Exécution

Dans le dictionnaire `appboyOptions` utilisé pour configurer votre instance Braze, ajoutez une entrée `ABKPushStoryAppGroupKey` et définissez la valeur à votre identifiant de groupe d'applications.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"VOTRE-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"VOTRE-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppAppAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions : [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

##### Option 2 : Info.plist

Vous pouvez également configurer le groupe d'applications Push Story à partir de vos infos `. liste` fichier, ajoutez un dictionnaire nommé `Braze` à votre fichier `Info.plist`. Dans le dictionnaire `Braze` , ajoutez une sous-entrée `PushStoryAppGroup` de type chaîne et définissez la valeur à votre identifiant de groupe d'applications. Notez qu'avant Braze iOS SDK v4.0.2, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.
[2]: {% image_buster /assets/img/ios/push_story/add_content_extension.png %} [3]: {% image_buster /assets/img/ios/push_story/enable_background_mode. ng %} [4]: {% image_buster /assets/img/ios/push_story/add_app_groups.png %} [6]: {% image_buster /assets/img/ios/push_story/spm1.png %} [7]: {% image_buster /assets/img/ios/push_story/spm2. ng %} [9]: {% image_buster /assets/img/ios/push_story/manual1.png %} [10]: {% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %} [11]: {% image_buster /assets/img/ios/push_story/abkstoriesview_size. ng %} [12]: {% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %} [13]: {% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/
[8]: https://github.com/Appboy/appboy-ios-sdk/releases
