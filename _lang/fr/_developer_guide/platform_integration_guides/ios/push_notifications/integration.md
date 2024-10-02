---
nav_title: Intégration
article_title: Intégration Push pour iOS
platform: iOS
page_order: 0
description: "Cet article de référence traite de la manière d’intégrer des notifications push dans votre application iOS."
channel:
  - Notification push
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
  
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration de notifications push

## Étape 1 : Configurer les notifications push

Avant de pouvoir envoyer une notification push iOS à l’aide de Braze, vous devez fournir votre fichier de notification push ou certificat d’Apple. Vous pouvez présenter un fichier `.p8` (recommandé) ou un certificat `.p12`.

{% tabs local %}
  {% tab .p8 File (Recommended) %}
**Utilisation d’un fichier .p8 (jeton d’authentification)**

Comme décrit dans la [documentation du développeur](https://help.apple.com/developer-account/#/devcdfbb56a3) Apple :

1. Dans votre compte développeur, allez à [**Certificates, Identifiers & Profiles**](https://developer.apple.com/account/ios/certificate) (Certificats, Identifiants et Profils).
2. Dans **Keys (Clés)**, sélectionnez **All (Toutes)** et cliquez sur le bouton **Add (Ajouter)** (+) dans le coin supérieur droit.
3. Dans **Key Description** (Description de la clé), saisissez un nom unique pour la clé de signature.
4. Dans **Key Services (Services de la clé)**, cochez la case **APNS**, puis cliquez sur **Continue (Continuer)**. Cliquez sur **Confirm (Confirmer)**.
5. Notez l’ID de la clé. Cliquez sur **Download (Télécharger)** pour générer et télécharger la clé. Assurez-vous d’enregistrer le fichier téléchargé dans un endroit sécurisé, car vous ne pouvez pas le télécharger plus d’une fois.
6. Naviguez jusqu’à **Manage Settings > Settings** (Gérer les paramètres > Paramètres) dans le tableau de bord et téléchargez le fichier .p8 dans **Apple Push Certificate** (Certificat de notification push Apple).
7. Lorsque vous y êtes invité, saisissez également vos [bundle ID](https://developer.apple.com/account/ios/identifier/bundle/) (ID de lot), [key ID](https://developer.apple.com/account/ios/authkey) (ID clé), et [team ID](https://developer.apple.com/account/#/membership) (ID d’équipe) d’application. Cliquez sur **Save (Enregistrer)**.<br><br>

{% endtab %}
{% tab .p12 Certificate (Legacy) %}
**Utilisation d’un certificat .p12 (héritage)**

Vous pouvez également utiliser le schéma d’authentification plus ancien d’Apple (.p12 SSL certificates). Contrairement à la solution .p8, ces certificats expirent automatiquement chaque année et vous obligeront à les régénérer et les télécharger à nouveau. Braze vous enverra des rappels par e-mail à l’approche de l’expiration du certificat pour vous aider à ce que vos notifications continuent sans interruption, mais comme il s’agit d’un processus manuel, nous vous recommandons d’utiliser le schéma d’authentification .p8 à la place. Cependant, si vous le souhaitez, vous pouvez configurer et télécharger les certificats .p12 comme décrit dans la section suivante :

**Étape 1 : Générer une demande de signature de certificat**

1. Naviguez jusqu’au [iOS Provisioning Portal](https://developer.apple.com/ios/manage/overview/index.action) (Portail d’approvisionnement iOS)
2. Sélectionnez **Identifiants > Identifiants Apple** dans la barre latérale.
3. Sélectionnez votre application.
4. Si les notifications push ne sont pas activées, cliquez sur **Edit (Modifier)** pour mettre à jour les paramètres de l’application.<br>![]({% image_buster /assets/img_archive/AppleProvisioningOptions.png %})
5. Cochez la case **Enable (Activer)** et cliquez sur **Create Certificate (Créer un certificat)** sous le **Production SSL Certificate (Certificat SSL de production)**<br>![]({% image_buster /assets/img_archive/push_cert_gen.png %})
6. Suivez les instructions de l’assistant de certificat SSL. Vous devriez maintenant voir un état « Enabled » (Activé) pour indiquer que les notifications push sont activées.
7. Vous devez mettre à jour votre profil de provisionnement pour l’application après avoir créé vos certificats SSL. Un simple rafraîchissement de l’organiseur permettra de réaliser cela.

**Étape 2 : Exporter le certificat**

1. Téléchargez le certificat de production push que vous venez de créer et ouvrez-le avec l’application Keychain Access.
2. Dans Keychain Access, cliquez sur **My Certificates (Mes certificats)** et localisez votre certificat push.
3. Exportez-le en tant que fichier `.p12` et utilisez un mot de passe temporaire et non sécurisé (vous aurez besoin de ce mot de passe lors du téléchargement de votre certificat vers Braze).
4. Naviguez jusqu’à **Manage Settings > Settings** (Gérer les paramètres > Paramètres) dans le tableau de bord et téléchargez votre certificat de production dans **Apple Push Certificate** (Certificat de notification push Apple).

>  Vous pouvez télécharger vos certificats de notification push de développement ou de production vers le tableau de bord pour vos applications de profil de provisionnement de distribution, mais vous ne pouvez en avoir qu’un seul à la fois. Si vous souhaitez effectuer des tests répétés de notifications push une fois que votre application est mise en ligne dans l’App Store, nous vous recommandons de configurer un groupe d’applications ou une application distincts pour la version de développement de votre application.

{% endtab %}
{% endtabs %}


## Étape 2 : Activer les fonctionnalités de notification push

Dans les paramètres de votre projet, assurez-vous que sous l’onglet **Capabilities** (Fonctionnalités) de votre fonctionnalité **Push Notifications** (Notifications Push) est [activée](https://help.apple.com/developer-account/#/devcdfbb56a3).

![][24]

Si vous disposez de certificats push de développement et de production séparés, assurez-vous de décocher la case **Automatically manage signing** (Gestion automatique de la signature) dans l’onglet **General** (Généralités). Cela vous permettra de choisir différents profils d’approvisionnement pour chaque configuration, car la fonction de signature de code automatique de Xcode ne s’applique qu’aux signatures de développement.

![Les paramètres du projet Xcode affichant l’onglet « General » (Généralités). Dans cet onglet, l’option « Automatically manage signing » (Gérer automatiquement la signature) est décochée.][34]

## Étape 3 : Inscrivez-vous aux notifications push

L’exemple de code approprié doit être inclus dans la méthode de délégation `application:didFinishLaunchingWithOptions:` de votre application pour que l’appareil de vos utilisateurs s’enregistre auprès des APN. Assurez-vous d’appeler tout le code d’intégration push dans le thread principal de votre application.

Braze fournit également des catégories push par défaut pour la prise en charge des boutons d’action push, qui doivent être ajoutées manuellement à votre code d’enregistrement push. Consulter [push action buttons][35] (boutons d’action push) pour les étapes d’intégration supplémentaires.

{% alert warning %}
Si vous avez implémenté une invite de notification push personnalisée, comme décrit dans nos [meilleures pratiques de notifications push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/), assurez-vous d’employer le code suivant **à chaque exécution de l’application** une fois qu’ils ont accordé des autorisations push à votre application. **Les applications doivent se réenregistrer auprès des APN, car [les jetons de périphérique peuvent changer arbitrairement](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html).**
{% endalert %}

### Utilisation de l’infrastructure de notification utilisateur (iOS 10+)

Si vous utilisez l’infrastructure `UserNotifications` (recommandé) introduit dans iOS 10, ajoutez le code suivant à la méthode `application:didFinishLaunchingWithOptions:` de votre délégué d’application.

{% alert important %}
L’exemple de code suivant inclut l’intégration pour l’authentification de notification push provisoire (lignes 5 et 6). Si vous ne prévoyez pas d’utiliser l’autorisation provisoire dans votre application, vous pouvez supprimer les lignes du code qui ajoutent `UNAuthorizationOptionProvisional` aux options `requestAuthorization`.<br>Consultez [iOS notification options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) (Options de notification iOS) pour en savoir plus sur l’authentification push provisoire.
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

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
Vous devez attribuer votre objet délégué à l’aide de `center.delegate = self` manière synchronisée avant que votre application ne termine son lancement, de préférence dans `application:didFinishLaunchingWithOptions:`. Sans cela, votre application risque de ne pas recevoir les notifications push entrantes. Consulter la documentation d’Apple [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) pour en savoir plus.
{% endalert %}

### Sans infrastructure UserNotifications

Si vous utilisez l’infrastructure `UserNotifications`, ajoutez le code suivant à la méthode `application:didFinishLaunchingWithOptions:` de votre délégué d’application.

{% tabs %}
{% tab OBJECTIVE-C %}

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
{% tab OBJECTIVE-C %}

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

Le code suivant transmet les notifications push reçues à Braze et est nécessaire pour la journalisation des analytiques push et la gestion des liens. Assurez-vous d’appeler tout le code d’intégration push dans le thread principal de votre application.

### iOS 10+

Lors de la conception avec iOS 10+, nous vous recommandons d’intégrer l’infrastructure `UserNotifications` et de procéder comme suit :

{% tabs %}
{% tab OBJECTIVE-C %}

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

iOS 10 a mis à jour les comportements de sorte qu’il ne soit plus appelé `application:didReceiveRemoteNotification:fetchCompletionHandler:` lorsqu’une notification push est cliqué. Pour cette raison, si vous ne mettez pas à jour la construction sur iOS 10+ et utilisez l’infrastructure `UserNotifications`, vous devez utiliser Braze des deux délégués de style ancien, ce qui constitue une rupture par rapport à notre intégration précédente.

Pour les applications conçues avec des SDK < iOS 10, suivez les instructions suivantes :

{% tabs %}
{% tab OBJECTIVE-C %}

Pour activer le suivi d’ouverture sur les notifications push, ajoutez le code suivant à la méthode `application:didReceiveRemoteNotification:fetchCompletionHandler:` de votre application :

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Pour prendre en charge les analytiques des notifications push sur iOS 10, vous devez également ajouter le code suivant à la méthode de délégation `application:didReceiveRemoteNotification:` de votre application :

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

Pour prendre en charge les analytiques des notifications push sur iOS 10, vous devez également ajouter le code suivant à la méthode de délégation `application(_:didReceiveRemoteNotification:)` de votre application :

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## Étape 6 : Création de liens profonds

La création de liens profonds d’une notification push vers l’application est gérée automatiquement via notre documentation d’intégration push standard. Si vous souhaitez en savoir plus sur la façon d’ajouter des liens profonds vers des emplacements spécifiques dans votre application, consultez notre [cas d’utilisation avancée][10].

## Étape 7 : Tests d’unité (facultatif)

Pour ajouter une couverture de test aux étapes d’intégration que vous venez de suivre, implémentez les [tests d’unité][36] Push de Braze.

[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-implementation
[24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %}
[34]: {% image_buster /assets/img_archive/xcode8_auto_signing.png %}
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/
[36]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/unit_tests/
