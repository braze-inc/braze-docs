---
nav_title: Boutons d’action
article_title: Boutons d’action push pour iOS
platform: iOS
page_order: 1
description: "Cet article de référence traite de la manière d’implémenter les boutons d’action dans vos notifications push iOS."
channel:
  - Notification push

---

# Boutons d’action {#push-action-buttons-integration}

Le SDK Braze pour iOS prend en charge les catégories de notifications push par défaut, y compris la prise en charge de la gestion d’URL pour chaque bouton d’action push. Actuellement, les catégories par défaut ont quatre ensembles de boutons d’action push : `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel`, et `More`. 

![Un GIF d’une notification push est développé afin d’afficher deux boutons d’action personnalisables.][13]

Pour enregistrer les catégories de notifications push par défaut de Braze, suivez les instructions d’intégration :

## Étape 1 : Ajoutez les catégories de notifications push par défaut de Braze

Utilisez le code suivant pour inscrire les catégories de notifications push par défaut de Braze lorsque vous [vous inscrivez aux notifications push][36] :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// For UserNotification.framework (iOS 10+ only)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:appboyCategories];

// For UIUserNotificationSettings (before iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
// For UserNotification.framework (iOS 10+ only)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// For UIUserNotificationSettings (before iOS 10)
let appboyCategories = ABKPushUtils.getAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

Cliquer sur les boutons d’action push avec le mode d’activation en arrière-plan ne fera que rejeter la notification et n’ouvrira pas l’application. Lorsque l’utilisateur ouvrira à nouveau l’application, l’analyse de clics de bouton pour ces actions sera transmise au serveur.

Si vous souhaitez créer vos propres catégories de notifications personnalisées, consultez [Personnalisation des boutons d’action][37].

## Étape 2 : Activer la gestion interactive des notifications push

Si vous utilisez l’infrastructure `UNNotification` et avez implémenté les [délégués][39] de Braze, cette méthode devrait déjà être intégrée. 

Pour activer la gestion des boutons d’action push de Braze, y compris l’analyse des clics et le routage des URL, ajoutez le code suivant à la méthode de délégation `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de votre application :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                                didReceive: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

Si vous n’utilisez pas UNNotification Framework, vous devrez ajouter le code suivant au `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` de votre application afin d’activer la gestion des boutons d’action de Braze :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identifier
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifier,
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Nous recommandons fortement aux personnes utilisant `handleActionWithIdentifier` de commencer à utiliser l’infrastructure `UNNotification`. Et cela en raison de la désapprobation de [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Personnalisation de la catégorie de notifications push

En plus de fournir un ensemble de [catégories de notifications push par défaut][2], Braze prend en charge les catégories et actions de notifications personnalisées. Une fois que vous avez enregistré les catégories dans votre application, vous pouvez utiliser le tableau de bord de Braze pour envoyer des catégories de notification à vos utilisateurs.

Si vous n’utilisez pas l’infrastructure `UserNotifications`, voir la documentation sur les [catégories alternatives][31].

Ces catégories peuvent ensuite être affectées aux notifications push via notre tableau de bord pour déclencher les configurations des boutons d’action de votre conception. Voici un exemple qui tire parti du `LIKE_CATEGORY` affiché sur l’appareil :

![Un message de notification push affichant deux boutons d’action push « unlike » (je n’aime plus) et « like » (j’aime).][17]


[13]: {% image_buster /assets/img_archive/iOS8Action.gif %}
[14]: https://developer.apple.com/reference/usernotifications/unnotificationcategory "Categories Docs"
[17]: {% image_buster /assets/img_archive/push_example_category.png %}
[36]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/#push-category-customization
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
[31]: https://developer.apple.com/documentation/usernotifications/unnotificationcategory
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/
