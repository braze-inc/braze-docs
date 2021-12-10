---
nav_title: Boutons d'action
article_title: Boutons d'action push pour iOS
platform: iOS
page_order: 0.2
description: "Cet article couvre la façon d'implémenter des boutons d'action dans vos notifications push iOS."
channel:
  - Pousser
---

# Boutons d'action {#push-action-buttons-integration}

Braze iOS SDK prend en charge les catégories push par défaut, y compris la gestion des URL pour chaque bouton d'action push. Actuellement, les catégories par défaut ont quatre ensembles de boutons d'action push : `Accepter`/`Refuser`, `Oui`/`Non`, `Confirmer`/`Annuler` et `Plus`.

!\[Illustration of Notification Action\]\[13\]

Pour enregistrer les catégories de push par défaut de Braze, suivez les instructions d’intégration ci-dessous:

## Étape 1 : Ajouter des catégories de push par défaut Braze

Utilisez le code suivant pour vous inscrire aux catégories de push par défaut de Braze lorsque vous [vous inscrivez pour push][36]:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Pour la notification d'utilisateur. ramework (iOS 10+ uniquement)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationNotificationCenter] setNotificationCategories:appboyCategories];

// Pour UIUserNotificationSettings (avant iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories] ;
[[UIApplication sharedApplication] registerUserNotificationSettings:settings] ;
```

{% endtab %}
{% tab swift %}

```swift
// Pour UserNotification.framework (iOS 10+ seulement)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// Pour UIUserNotificationSettings (avant iOS 10)
let appboyCategories = ABKPushUtils. etAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

Cliquer sur les boutons d'action push avec le mode d'activation en arrière-plan ne fermera que la notification et n'ouvrira pas l'application. Les clics de bouton analytiques pour ces actions seront vidés sur le serveur la prochaine fois que l'utilisateur ouvrira l'application.

> Si vous souhaitez créer vos propres catégories de notification personnalisées, consultez notre documentation sur la personnalisation du bouton [d'action][37].

## Étape 2 : Activer la gestion interactive des push

Si vous utilisez le Framework de Notification et que vous avez implémenté [Délégués de Braze][39], vous devriez déjà avoir cette méthode intégrée.

Pour activer la gestion des boutons d'action poussée, y compris les clics d'analyse et de routage d'URL, ajoutez le code suivant à la `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` méthode déléguée:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:centre
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(centre,
                                                didReceve: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

Si vous n'utilisez pas le Framework de Notification UN, vous devrez ajouter le code suivant à l'application `de votre application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` pour activer la gestion des boutons d'action push de Braze:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identificateur
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifiant,
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Nous recommandons fortement que les personnes utilisant `handleActionWithIdentifier` commencent à utiliser UNNotification Framework. Nous le recommandons en raison de la [dépréciation de handleActionWithIdentifier](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Personnalisation de la catégorie push

En plus de fournir un ensemble de [catégories de push par défaut][2], Braze prend en charge les catégories et actions de notification personnalisées. Une fois que vous enregistrez des catégories dans votre application, vous pouvez utiliser le tableau de bord Braze pour envoyer des catégories de notification à vos utilisateurs.

> Si vous n'utilisez pas le framework `UserNotifications` , veuillez consulter cette [documentation de catégories alternatives][31].

Ces catégories peuvent ensuite être affectées aux notifications push via notre tableau de bord pour déclencher les configurations des boutons d'action de votre conception. Voici un exemple qui tire parti de la "LIKE_CATEGORY" affichée sur l'appareil!

!\[Exemple de personnalisation de catégorie Push\]\[17\]
[13]: {% image_buster /assets/img_archive/iOS8Action.gif %} [17]: {% image_buster /assets/img_archive/push_example_category.png %}

[36]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/#push-category-customization
[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling
[31]: https://developer.apple.com/reference/uikit/uiusernotificationcategory
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/