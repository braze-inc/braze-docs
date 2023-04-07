---
hidden: true
nav_title: Push Stories
article_title: Push Stories pour iOS
platform: iOS
page_order: 27
description: "Cet article montre comment configurer les Push Stories pour votre application iOS."
channel:
  - Notification push

---

# Configurer une Push Story

La fonction Push Story nécessite l’infrastructure `UNNotification` et iOS 10. Cette fonctionnalité est uniquement disponible à partir du SDK iOS version 3.2.1.

## Étape 1 : Activer les notifications push dans votre application

Suivez l’[intégration des notifications push][1] pour activer l’application dans votre application.

## Étape 2 : Ajout de la cible de l’extension de contenu de notification

Dans votre projet d’application, allez au menu **File > New > Target...** (Fichier > Nouveau > Cible...) et ajoutez une nouvelle cible `Notification Content Extension` et activez-la.

![][2]

Xcode doit générer une nouvelle cible pour vous et créer des fichiers automatiquement pour vous, notamment :

{% tabs %}
{% tab OBJECTIVE-C %}

- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

{% endtab %}
{% tab swift %}

- `NotificationViewController.swift`
- `MainInterface.storyboard`

{% endtab %}
{% endtabs %}

## Étape 3 : Activer les fonctionnalités

La fonction de l’historique de notification push nécessite le mode arrière-plan dans la section **Capabilities** (Fonctionnalités) de la cible de l’application principale. Après avoir activé les modes arrière-plan, sélectionnez **Background fetch** (Récupérer en arrière-plan) et **Remote Notification** (Notification à distance).

![][3]

Vous devez également ajouter `Capability App Groups`. Si vous n’avez pas de groupe d’apps dans votre application, allez sur **Capability (fonctionnalité)** de la cible de l’application principale, activez `App Groups`, et cliquez sur le bouton **+**. Utilisez l’ID de l’ensemble de votre application pour créer le groupe d’apps. Par exemple, si l’ID de l’ensemble de votre application est `com.company.appname`, vous pouvez nommer votre groupe d’apps `group.com.company.appname.xyz`. Vous devez activer le `App Groups` pour les cibles d’extension de contenu et de l’application principale.

{% alert important %}
Dans ce contexte`App Groups`, se réfère aux [Droit des groupes d’apps](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) d’Apple et non à votre ID de groupe d’apps Braze.
{% endalert %}

## Étape 4 : Ajouter l’infrastructure Push Story à votre application

{% tabs local %}
{% tab Swift Package Manager %}

Après avoir suivi le [Guide d’intégration du gestionnaire de paquets Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/), ajoutez `AppboyPushStory` à votre `Notification Content Extension` :

![Dans Xcode, sous infrastructures et bibliothèques, sélectionnez l’icône « + » pour ajouter une infrastructure.]({% image_buster /assets/img/ios/push_story/spm1.png %})

![]({% image_buster /assets/img/ios/push_story/spm2.png %})

{% endtab %}
{% tab Cocoapods %}

Ajoutez la ligne suivante à votre Podfile :

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Après avoir mis à jour le Podfile, naviguez jusqu’au répertoire de votre projet d’application Xcode dans votre terminal et exécutez `pod install`.

{% endtab %}
{% tab Manual %}

Téléchargez les dernières `AppboyPushStory.zip` de la [Page Github](https://github.com/Appboy/appboy-ios-sdk/releases), décompressez-le et ajoutez les fichiers suivants à `Notification Content Extension` de votre projet :
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![]({% image_buster /assets/img/ios/push_story/manual1.png %})

{% alert important %}
Assurez-vous que **Do Not Embed (Ne pas intégrer)** est sélectionné pour **AppboyPushStory.xcframework** sous la colonne **Embed (Intégrer)**.
{% endalert %}

Ajouter l’indicateur `-ObjC` à la `Notification Content Extension` de votre projet dans **Build Settings > Other Linker Flags** (Paramètres de création > Autres indicateurs de lien).

{% endtab %}
{% endtabs %}

## Étape 5 : Mise à jour de votre contrôleur de visualisation de notification

{% tabs %}
{% tab OBJECTIVE-C %}

Dans votre `NotificationViewController.h`, ajoutez les lignes suivantes pour ajouter de nouvelles propriétés et importer les fichiers d’en-tête :

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

Dans votre `NotificationViewController.m`, supprimez l’implémentation par défaut et ajouter le code suivant :

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  self.dataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               storiesView:self.storiesView
                                                                  appGroup:@"YOUR-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option))completion {
  UNNotificationContentExtensionResponseOption option = [self.dataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animated {
  [self.dataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab swift %}

Dans votre `NotificationViewController.swift`, ajoutez la ligne suivante pour importer les fichiers d’en-tête :

```swift
import AppboyPushStory
```

Puis, supprimez l’implémentation par défaut et ajoutez le code suivant :

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var dataSource: ABKStoriesViewDataSource?
    
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

## Étape 6 : Définissez le storyboard d’extension de contenu de notification

Ouvrez le storyboard `Notification Content Extension` et placez un nouveau `UIView` dans le contrôleur de visualisation de notification. Renommez la classe par `ABKStoriesView`. Faites en sorte que la largeur et la hauteur de la vue correspondent à la vue principale du contrôleur de visualisation de notification.

![][10]

![][11]

Ensuite, liez le contrôleur de visualisation de notification IBOutlet `storiesView` au `ABKStoriesView` ajouté.

![][13]

## Étape 7 : Définissez la plist d’extension de contenu de notification

Ouvrez le fichier `Info.plist` de `Notification Content Extension` et ajoutez et modifiez les clés suivantes dans `NSExtension \ NSExtensionAttributes` :

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (type `String`)
`UNNotificationExtensionDefaultContentHidden` = `YES` (type `Boolean`)
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` (type `Number`)

![][12]

## Étape 8 : Mise à jour de l’intégration Braze dans votre application principale

##### Option 1 : Exécution

Dans le dictionnaire `appboyOptions` utilisé pour configurer votre instance Braze, ajoutez une entrée `ABKPushStoryAppGroupKey` et définissez la valeur sur l’identifiant API de votre groupe d’apps.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"YOUR-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

##### Option 2 : Info.plist

Sinon, pour configurer le groupe d’applications Push Story de votre fichier `Info.plist`, ajoutez un dictionnaire nommé `Braze` à votre fichier `Info.plist`. À l’intérieur du dictionnaire `Braze`, ajoutez une sous-entrée de type chaîne de caractères `PushStoryAppGroup` et définissez la valeur sur votre identifiant de groupe d’apps. Notez qu’avant le SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {% image_buster /assets/img/ios/push_story/add_content_extension.png %}
[3]: {% image_buster /assets/img/ios/push_story/enable_background_mode.png %}
[4]: {% image_buster /assets/img/ios/push_story/add_app_groups.png %}
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/
[10]: {% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %}
[11]: {% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %}
[12]: {% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %}
[13]: {% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %}
