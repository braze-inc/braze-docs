---
nav_title: Intégration
article_title: Intégration Push pour iOS
platform: iOS
page_order: 0
description: "Cet article de référence traite de la manière d’intégrer des notifications push dans votre application iOS."
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'
  
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration de notifications push

## Étape 1 : Téléchargez votre jeton APN

 %} developer_guide/swift/apns_token.md

## Étape 2 : Activer les fonctionnalités de notification push

Dans les paramètres de votre projet, assurez-vous que sous l'onglet **Capacités**, votre capacité de **notifications push** est basculée.

![]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

Si vous disposez de certificats push distincts pour le développement et la production, veillez à décocher la case **Gérer automatiquement la signature** dans l'onglet **Général**. Cela vous permettra de choisir différents profils d’approvisionnement pour chaque configuration, car la fonction de signature de code automatique de Xcode ne s’applique qu’aux signatures de développement.

![Les paramètres du projet Xcode affichant l’onglet « General » (Généralités). Dans cet onglet, l'option "Gérer automatiquement la signature" est décochée.]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## Étape 3 : Inscrivez-vous aux notifications push

L’exemple de code approprié doit être inclus dans la méthode de délégation `application:didFinishLaunchingWithOptions:` de votre application pour que l’appareil de vos utilisateurs s’enregistre auprès des APN. Assurez-vous d’appeler tout le code d’intégration push dans le thread principal de votre application.

Braze fournit également des catégories push par défaut pour la prise en charge des boutons d’action push, qui doivent être ajoutées manuellement à votre code d’enregistrement push. Reportez-vous aux [boutons d'action push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons/) pour connaître les étapes d'intégration supplémentaires.

{% alert warning %}
Si vous avez mis en place une invite de poussée personnalisée comme décrit dans nos [meilleures pratiques de poussée]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/troubleshooting/), assurez-vous que vous appelez le code suivant à **chaque fois que l'application s'exécute** après qu'ils ont accordé des autorisations de poussée à votre application. **Les applications doivent se réenregistrer auprès des APN, car [les jetons d'appareils peuvent changer arbitrairement](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html).**
{% endalert %}

### Utilisation de l’infrastructure de notification utilisateur (iOS 10+)

Si vous utilisez l’infrastructure `UserNotifications` (recommandé) introduit dans iOS 10, ajoutez le code suivant à la méthode `application:didFinishLaunchingWithOptions:` de votre délégué d’application.

{% alert important %}
L’exemple de code suivant inclut l’intégration pour l’authentification de notification push provisoire (lignes 5 et 6). Si vous ne prévoyez pas d’utiliser l’autorisation provisoire dans votre application, vous pouvez supprimer les lignes du code qui ajoutent `UNAuthorizationOptionProvisional` aux options `requestAuthorization`.<br>Consultez les [options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) pour en savoir plus sur l'authentification provisoire par push.
{% endalert %}

{% tabs %}
{% tab OBJECTIF-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
Vous devez attribuer votre objet délégué à l’aide de `center.delegate = self` manière synchronisée avant que votre application ne termine son lancement, de préférence dans `application:didFinishLaunchingWithOptions:`. Sans cela, votre application risque de ne pas recevoir les notifications push entrantes. Consultez la documentation d'Apple [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) pour en savoir plus.
{% endalert %}

### Sans infrastructure UserNotifications

Si vous utilisez l’infrastructure `UserNotifications`, ajoutez le code suivant à la méthode `application:didFinishLaunchingWithOptions:` de votre délégué d’application.

{% tabs %}
{% tab OBJECTIF-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}


## Étape 4 : Enregistrer des jetons avec Braze

Une fois l’enregistrement des APN terminé, la méthode suivante doit être modifiée pour transmettre le résultat `deviceToken` à Braze pour que l’utilisateur soit activé pour les notifications push :

{% tabs %}
{% tab OBJECTIF-C %}

Ajoutez le code suivant à votre méthode `application:didRegisterForRemoteNotificationsWithDeviceToken:` :

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

Ajoutez le code suivant à la méthode `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` de votre application :

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
La méthode de délégation `application:didRegisterForRemoteNotificationsWithDeviceToken:` est appelée chaque fois après que `[[UIApplication sharedApplication] registerForRemoteNotifications]` soit employée. Si vous migrez vers Braze depuis un autre service de notification push et que l’appareil de votre utilisateur a déjà enregistré des APN, cette méthode collectera des jetons à partir des enregistrements existants la prochaine fois que la méthode est utilisée, et les utilisateurs n’auront pas à se réabonner aux notifications push.
{% endalert %}

## Étape 5 : Activer la gestion des notifications push

Le code suivant transmet les notifications push reçues à Braze et est nécessaire pour la journalisation des analyses push et la gestion des liens. Assurez-vous d’appeler tout le code d’intégration push dans le thread principal de votre application.

### iOS 10+

Lors de la conception avec iOS 10+, nous vous recommandons d’intégrer l’infrastructure `UserNotifications` et de procéder comme suit :

{% tabs %}
{% tab OBJECTIF-C %}

Ajoutez le code suivant à la méthode `application:didReceiveRemoteNotification:fetchCompletionHandler:` de votre application :

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Puis ajoutez le code suivant à la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de votre application :

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**Gestion des notifications push de premier plan**

Pour afficher une notification push lorsque l’application est au premier plan, implémentez `userNotificationCenter:willPresentNotification:withCompletionHandler:` :

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

Si vous cliquez sur la notification de premier plan, la notification push iOS 10 déléguée `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` sera appelée, et Braze enregistrera un événement clic Push.

{% endtab %}
{% tab swift %}

Ajoutez le code suivant à la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de votre application :

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

Puis ajoutez le code suivant à la méthode `userNotificationCenter(_:didReceive:withCompletionHandler:)` de votre application :

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**Gestion des notifications push de premier plan**

Pour afficher une notification push lorsque l’application est au premier plan, implémentez `userNotificationCenter(_:willPresent:withCompletionHandler:)` :

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

Si vous cliquez sur la notification de premier plan, la notification push iOS 10 déléguée `userNotificationCenter(_:didReceive:withCompletionHandler:)` sera appelée, et Braze enregistrera un événement clic Push.

{% endtab %}
{% endtabs %}

### Pré-iOS 10

iOS 10 a mis à jour les comportements de sorte qu’il ne soit plus appelé `application:didReceiveRemoteNotification:fetchCompletionHandler:` lorsqu’une notification push est cliqué. Pour cette raison, si vous ne mettez pas à jour la création sur iOS 10+ et utilisez l’infrastructure `UserNotifications`, vous devez utiliser Braze des deux délégués de style ancien, ce qui constitue une rupture par rapport à notre intégration précédente.

Pour les applications conçues avec des SDK < iOS 10, suivez les instructions suivantes :

{% tabs %}
{% tab OBJECTIF-C %}

Pour activer le suivi d’ouverture sur les notifications push, ajoutez le code suivant à la méthode `application:didReceiveRemoteNotification:fetchCompletionHandler:` de votre application :

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Pour prendre en charge les analyses des notifications push sur iOS 10, vous devez également ajouter le code suivant à la méthode de délégation `application:didReceiveRemoteNotification:` de votre application :

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

Pour activer le suivi d’ouverture sur les notifications push, ajoutez le code suivant à la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de votre application :

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

Pour prendre en charge les analyses des notifications push sur iOS 10, vous devez également ajouter le code suivant à la méthode de délégation `application(_:didReceiveRemoteNotification:)` de votre application :

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## Étape 6 : Création de liens profonds

La création de liens profonds d’une notification push vers l’application est gérée automatiquement via notre documentation d’intégration push standard. Si vous souhaitez en savoir plus sur la création de liens profonds vers des emplacements/localisations spécifiques dans votre application, consultez nos [cas d'utilisation avancés]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-implementation).

## Étape 7 : Tests d’unité (facultatif)

Pour ajouter une couverture de test pour les étapes d'intégration que vous venez de suivre, mettez en œuvre les [tests unitaires push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests/).

