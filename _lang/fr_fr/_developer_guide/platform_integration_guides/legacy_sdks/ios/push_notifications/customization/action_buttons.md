---
nav_title: Boutons d’action
article_title: Boutons d’action push pour iOS
platform: iOS
page_order: 1
description: "Cet article de référence traite de la manière d’implémenter les boutons d’action dans vos notifications push iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Boutons d’action {#push-action-buttons-integration}

Le SDK Braze pour iOS prend en charge les catégories de notifications push par défaut, y compris la prise en charge de la gestion d’URL pour chaque bouton d’action push. Actuellement, les catégories par défaut ont quatre ensembles de boutons d’action push : `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel`, et `More`. 

![GIF d'un message push tiré vers le bas pour afficher deux boutons d'action personnalisables.]({% image_buster /assets/img_archive/iOS8Action.gif %})

Pour enregistrer nos catégories push par défaut, suivez les instructions d'intégration :

## Étape 1 : Ajoutez les catégories de notifications push par défaut de Braze

Utilisez le code suivant pour vous inscrire à nos catégories push par défaut lorsque vous [vous inscrivez à push :]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze)

{% tabs %}
{% tab OBJECTIF-C %}

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

Si vous souhaitez créer vos propres catégories de notifications personnalisées, consultez la [personnalisation des boutons d'action]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/#push-category-customization).

## Étape 2 : Activer la gestion interactive des notifications push

Si vous utilisez le cadre `UNNotification` et que vous avez mis en œuvre des [délégués]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling) Braze, cette méthode devrait déjà être intégrée. 

Pour activer la gestion de notre bouton d'action push, y compris l'analyse des clics et le routage des URL, ajoutez le code suivant à la méthode de délégation de votre application `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` :

{% tabs %}
{% tab OBJECTIF-C %}

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

Si vous n'utilisez pas UNNotification Framework, vous devrez ajouter le code suivant au site `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` de votre application pour activer la gestion de nos boutons d'action push :

{% tabs %}
{% tab OBJECTIF-C %}

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
Nous recommandons fortement aux personnes utilisant `handleActionWithIdentifier` de commencer à utiliser l’infrastructure `UNNotification`. Nous recommandons cette solution en raison de la dépréciation de l'option [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Personnalisation de la catégorie de notifications push

En plus de fournir un ensemble de [catégories de push par défaut]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/), Braze prend en charge les catégories et actions de notification personnalisées. Après avoir enregistré des catégories dans votre application, vous pouvez utiliser le tableau de bord de Braze pour envoyer des catégories de notification à vos utilisateurs.

Si vous n'utilisez pas le cadre `UserNotifications`, consultez la documentation sur les [catégories alternatives.](https://developer.apple.com/documentation/usernotifications/unnotificationcategory) 

Ces catégories peuvent ensuite être affectées aux notifications push via notre tableau de bord pour déclencher les configurations des boutons d’action de votre conception. Voici un exemple qui tire parti du `LIKE_CATEGORY` affiché sur l’appareil :

![Un message envoyant deux boutons d'action push "unlike" et "like".]({% image_buster /assets/img_archive/push_example_category.png %})


