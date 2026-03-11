{% multi_lang_include developer_guide/prerequisites/swift.md %} Il vous sera également nécessaire de [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Configuration des notifications push riches

### Étape 1 : Création d’une extension de service

Pour créer une [extension de service de notification](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), naviguez vers **Fichier > Nouveau > Cible** dans Xcode et sélectionnez **Extension de service de notification.**

![]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Assurez-vous que l'option **Embed In Application (Intégrer dans l'application** ) est activée pour intégrer l'extension dans votre application.

### Étape 2 : Configuration de l'extension du service de notification

Une extension de service de notification est un binaire propre qui est intégré à votre application. Elle doit être configurée dans le [portail des développeurs Apple](https://developer.apple.com) avec son propre ID d'application et son propre profil de provisionnement.

L'ID du bundle de l'extension du service de notification doit être distinct de l'ID du bundle de votre application principale. Par exemple, si l’ID de lot de votre application est `com.company.appname`, vous pouvez utiliser `com.company.appname.AppNameServiceExtension` pour votre extension de service.

### Étape 3 : Ajouter un groupe d'applications

Dans Xcode, veuillez ajouter la fonctionnalité Groupe d'applications à partir du volet **Signing&Capabilities** à votre cible d'application principale ainsi qu'à la cible Notification Service Extension. Ensuite, cliquez sur le bouton **+**. Utilisez l’ID de l’ensemble de votre application pour créer le groupe d'applications. Par exemple, si l’ID de l’ensemble de votre application est `com.company.appname`, vous pouvez nommer votre groupe d'applications `group.com.company.appname.xyz`.

{% alert important %}
Les groupes d'applications dans ce contexte font référence à l'[App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) d'Apple et non à votre identifiant de l'espace de travail Braze (anciennement groupe d'applications).
{% endalert %}

Il est nécessaire de disposer d'un groupe d'applications partagé afin que votre application principale et l'extension de service de notification puissent accéder aux données partagées. Si vous n'ajoutez pas votre application à un groupe d'applications, il est possible que certains champs de la charge utile push ne soient pas renseignés et que votre application ne fonctionne pas correctement.

### Étape 4 : Intégration de riches notifications push

Pour obtenir un guide étape par étape sur l'intégration des notifications push enrichies avec `BrazeNotificationService`, reportez-vous à notre [tutoriel](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

Pour voir un exemple, reportez-vous à l'utilisation dans [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) de notre application Exemples.

#### Ajouter le framework de notifications push enrichies à votre application

{% tabs local %}
{% tab Swift Package Manager %}

Après avoir suivi le [Guide d'intégration du gestionnaire de paquets Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), ajoutez `BrazeNotificationService` à votre `Notification Service Extension` en procédant comme suit :

1. Dans Xcode, sous Infrastructures et bibliothèques, sélectionnez l'icône d’ajout <i class="fas fa-plus"></i> pour ajouter un framework. <br><br>![L'icône « + » se trouve sous « Frameworks » et « Libraries » dans Xcode.]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. Sélectionnez le cadre "BrazeNotificationService". <br><br>![Le cadre « BrazeNotificationService » peut être sélectionné dans la fenêtre modale/boîte de dialogue modale, etc.]({% image_buster /assets/img_archive/rich_notification2.png %})

{% endtab %}
{% tab CocoaPods %}

Ajoutez ce qui suit à votre Podfile :

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

{% alert note %}
Pour savoir comment mettre en œuvre les contenus push, consultez la [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).
{% endalert %}

Après avoir mis à jour le Podfile, naviguez jusqu’au répertoire de votre projet d’application Xcode dans votre terminal et exécutez `pod install`.

{% endtab %}

{% tab Manual %}

Pour ajouter `BrazeNotificationService.xcframework` à votre `Notification Service Extension`, voir [Intégration manuelle]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/).

![]({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### Utiliser votre propre UNNotificationServiceExtension

Si vous devez utiliser votre propre UNNotificationServiceExtension, vous pouvez à la place appeler [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) dans votre méthode `didReceive`.

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

### Étape 5 : Configuration du groupe d'applications dans Braze

Avant d'initialiser Braze, assignez le nom de votre groupe d'applications à la propriété [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) de votre configuration Braze.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

### Étape 6 : Créer une notification enrichie dans votre tableau de bord

Votre équipe marketing peut également créer des notifications enrichies à partir du tableau de bord. Veuillez créer une notification push via le compositeur de notifications push et joindre une image ou un GIF, ou fournir une URL hébergeant une image, un GIF ou une vidéo. Notez que les ressources sont téléchargées à la réception des notifications push, vous devez donc prévoir des pics importants et synchrones de demandes si vous hébergez votre contenu.
