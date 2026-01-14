{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également mettre en place [les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), ce qui implique l'implémentation du framework `UNNotification`.

La version minimale suivante du SDK est requise pour recevoir les contenus push :

{% sdk_min_versions swift:5.0.0 %}

## Mise en place des contenus push

### Étape 1 : Ajout de la cible d'extension de contenu de notification {#notification-content-extension}

Dans votre projet d'application, sélectionnez **Fichier > Nouveau > Cible**, ajoutez une nouvelle cible `Notification Content Extension` et activez-la.

![]({% image_buster /assets/img/swift/push_story/add_content_extension.png %})

Xcode doit générer une nouvelle cible pour vous et créer des fichiers automatiquement pour vous, notamment :

- `NotificationViewController.swift`
- `MainInterface.storyboard`

### Étape 2 : Activation des capacités {#enable-capabilities}

Dans Xcode, ajoutez la capacité Modes d'arrière-plan en utilisant le volet **Signature et capacités** pour la cible principale de l'application. Sélectionnez les cases à cocher **Récupération en arrière-plan** et **Notifications à distance**.

![]({% image_buster /assets/img/swift/push_story/enable_background_mode.png %})

#### Ajouter un groupe d'applications

De plus, depuis le volet **Signature et capacités** dans Xcode, ajoutez la capacité Groupes d’applications à votre cible d'application principale ainsi qu'aux cibles d'extension de contenu de notification. Ensuite, cliquez sur le bouton **+**. Utilisez l’ID de l’ensemble de votre application pour créer le groupe d'applications. Par exemple, si l’ID de l’ensemble de votre application est `com.company.appname`, vous pouvez nommer votre groupe d'applications `group.com.company.appname.xyz`.

{% alert important %}
Les groupes d'applications dans ce contexte font référence à l'[App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) d'Apple et non à votre identifiant de l'espace de travail Braze (anciennement groupe d'applications).
{% endalert %}

Si vous n'ajoutez pas votre application à un groupe d'applications, votre application peut ne pas remplir certains champs de la charge utile de la notification push et ne fonctionnera pas entièrement comme prévu.

### Étape 3 : Ajout du framework Push Story à votre application {#enable-capabilities}

{% tabs local %}
{% tab Gestionnaire de paquets Swift %}

Après avoir suivi le [Guide d’intégration du gestionnaire de paquets Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), ajoutez `BrazePushStory` à votre `Notification Content Extension` :

![Dans Xcode, sous Infrastructures et bibliothèques, sélectionnez l’icône « + » pour ajouter un framework.]({% image_buster /assets/img/swift/push_story/spm1.png %})

![]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Ajoutez la ligne suivante à votre Podfile :

```ruby
target 'YourAppTarget' do
pod 'BrazeKit'
pod 'BrazeUI'
pod 'BrazeLocation'
end

target 'YourNotificationContentExtensionTarget' do
pod 'BrazePushStory'
end

# Only include the below if you want to also integrate Rich Push
target 'YourNotificationServiceExtensionTarget' do
pod 'BrazeNotificationService'
end
```

{% alert note %}
Pour savoir comment implémenter des notifications push riches, consultez [Notifications enrichies]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager).
{% endalert %}

Après avoir mis à jour le Podfile, naviguez jusqu’au répertoire de votre projet d’application Xcode dans votre terminal et exécutez `pod install`.

{% endtab %}
{% tab Manual (Manuel) %}

Téléchargez le dernier `BrazePushStory.zip` depuis la [page GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), extrayez-le et ajoutez le `BrazePushStory.xcframework` à l’`Notification Content Extension` de votre projet.

![]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
Assurez-vous que **Ne pas intégrer** est sélectionné pour **BrazePushStory.xcframework** dans la colonne **Intégrer**.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 4 : Mise à jour de votre contrôleur de visualisation de notification {#enable-capabilities}

Dans `NotificationViewController.swift`, ajoutez la ligne suivante pour importer les fichiers d'en-tête :

```swift
import BrazePushStory
```

Ensuite, remplacez l'implémentation par défaut en héritant de [`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/) :

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### Gestion personnalisée des événements d'histoire push

Si vous souhaitez implémenter votre propre logique personnalisée pour gérer les événements de notification d'histoire push, héritez de `BrazePushStory.NotificationViewController` comme ci-dessus et remplacez les méthodes [`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:)) comme ci-dessous.

```swift
import BrazePushStory
import UserNotifications
import UserNotificationsUI

class NotificationViewController: BrazePushStory.NotificationViewController {
  override func didReceive(_ notification: UNNotification) {
    super.didReceive(notification)
    
    // Custom handling logic
  }
  
  override func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    super.didReceive(response, completionHandler: completion)
    
    // Custom handling logic
  }
}
```

### Étape 5 : Définir le fichier plist de l'extension de contenu de notification {#notification-content-extension}

Ouvrez le fichier `Info.plist` de l’`Notification Content Extension`, puis ajoutez et modifiez les clés suivantes sous `NSExtension \ NSExtensionAttributes` :

| Clé                                              | Type    | Valeur                  |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | Chaîne de caractères  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | Valeur booléenne | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | Nombre  | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | Valeur booléenne | `YES`                  |

Votre fichier `Info.plist` doit correspondre à l'image suivante :

![]({% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %})

### Étape 6 : Mise à jour de l'intégration Braze dans votre application principale {#update-braze}

Avant d'initialiser Braze, assignez le nom de votre groupe d'applications à la propriété [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) de votre configuration Braze.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```
