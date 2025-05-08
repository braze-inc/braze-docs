---
nav_title: Contenu push
article_title: Push Stories pour iOS
platform: iOS
page_order: 27
description: "Cet article de référence montre comment configurer les Push Stories pour votre application iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configurer une Push Story

La fonction Push Story nécessite l’infrastructure `UNNotification` et iOS 10. Cette fonctionnalité est uniquement disponible à partir du SDK iOS version 3.2.1.

## Étape 1 : Activer les notifications push dans votre application

Suivez l'[intégration de la notification push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) pour activer le push dans votre app.

## Étape 2 : Ajout de la cible de l’extension de contenu de notification

Dans votre projet d’application, sélectionnez **Fichier > Nouveau > Cible...**, ajoutez une nouvelle cible `Notification Content Extension` et activez-la.

![]({% image_buster /assets/img/ios/push_story/add_content_extension.png %})

Xcode doit générer une nouvelle cible pour vous et créer des fichiers automatiquement pour vous, notamment :

{% tabs %}
{% tab OBJECTIF-C %}

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

La fonctionnalité Push Story nécessite le mode arrière-plan dans la section **Capacités** de l'objectif principal de l'application. Après avoir activé les modes d’arrière-plan, sélectionnez **Récupérer en arrière-plan** et **Notifications à distance**.

![]({% image_buster /assets/img/ios/push_story/enable_background_mode.png %})

### Ajouter un groupe d'applications

Vous devez également ajouter `Capability App Groups`. Si vous n’avez pas de groupe d'applications dans votre application, sélectionnez la **capacité** de la cible de l’application principale, activez les `App Groups` et cliquez sur le bouton **+**. Utilisez l’ID de l’ensemble de votre application pour créer le groupe d'applications. Par exemple, si l’ID de l’ensemble de votre application est `com.company.appname`, vous pouvez nommer votre groupe d'applications `group.com.company.appname.xyz`. Vous devez activer le `App Groups` pour les cibles d’extension de contenu et de l’application principale.

{% alert important %}
Dans ce contexte, `App Groups` se réfère aux [droits des groupes d'applications](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) d’Apple et non à votre ID d'espace de travail (anciennement groupe d'applications) de Braze.
{% endalert %}

Si vous n'ajoutez pas votre application à un groupe d'applications, votre application risque de ne pas remplir certains champs de la charge utile de push et ne fonctionnera pas complètement comme prévu.

## Étape 4 : Ajouter l’infrastructure Push Story à votre application

{% tabs local %}
{% tab Gestionnaire de paquets Swift %}

Après avoir suivi le [Guide d’intégration du gestionnaire de paquets Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/), ajoutez `AppboyPushStory` à votre `Notification Content Extension` :

![Dans Xcode, sous infrastructures et bibliothèques, sélectionnez l’icône « + » pour ajouter un framework.]({% image_buster /assets/img/ios/push_story/spm1.png %})

![]({% image_buster /assets/img/ios/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Ajoutez la ligne suivante à votre Podfile :

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Après avoir mis à jour le Podfile, naviguez jusqu’au répertoire de votre projet d’application Xcode dans votre terminal et exécutez `pod install`.

{% endtab %}
{% tab Manual (Manuel) %}

Téléchargez la dernière version de `AppboyPushStory.zip` depuis la [page GitHub](https://github.com/Appboy/appboy-ios-sdk/releases), décompressez-la et ajoutez les fichiers suivants à l’`Notification Content Extension` de votre projet :
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![]({% image_buster /assets/img/ios/push_story/manual1.png %})

{% alert important %}
Assurez-vous que l'option **Ne pas incorporer** est sélectionnée pour **AppboyPushStory.xcframework** dans la colonne **Embed**.
{% endalert %}

Ajoutez l’indicateur `-ObjC` à l'`Notification Content Extension` de votre projet dans **Paramètres de création > Autres indicateurs de lien**.

{% endtab %}
{% endtabs %}

## Étape 5 : Mise à jour de votre contrôleur de visualisation de notification

{% tabs %}
{% tab OBJECTIF-C %}

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

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %})

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %})

Ensuite, liez le contrôleur de visualisation de notification IBOutlet `storiesView` au `ABKStoriesView` ajouté.

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %})

## Étape 7 : Définissez la plist d’extension de contenu de notification

Ouvrez le fichier `Info.plist` de `Notification Content Extension` et ajoutez et modifiez les clés suivantes dans `NSExtension \ NSExtensionAttributes` :

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (type `String`)
`UNNotificationExtensionDefaultContentHidden` = `YES` (type `Boolean`)
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` (type `Number`)

![]({% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %})

## Étape 8 : Mise à jour de l’intégration Braze dans votre application principale

##### Option 1 : Exécution

Dans le dictionnaire `appboyOptions` utilisé pour configurer votre instance Braze, ajoutez une entrée `ABKPushStoryAppGroupKey` et définissez la valeur de l'identifiant API de votre espace de travail.

{% tabs %}
{% tab OBJECTIF-C %}

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

##### Option 2 : Info.plist

Alternativement, pour configurer l'espace de travail Push Story à partir de votre fichier `Info.plist`, ajoutez un dictionnaire nommé `Braze` à votre fichier `Info.plist`. Dans le dictionnaire `Braze`, ajoutez une sous-entrée `PushStoryAppGroup` de type chaîne de caractères et définissez la valeur de l'identifiant de votre espace de travail. Notez qu’avant le SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

## Étapes suivantes

Reportez-vous ensuite aux étapes relatives à l'intégration des [boutons d'action]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/), qui est nécessaire pour que les boutons s'affichent dans un message Push Story.


