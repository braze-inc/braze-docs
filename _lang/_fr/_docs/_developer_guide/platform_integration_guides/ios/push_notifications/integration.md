---
nav_title: Intégration
article_title: Intégration push pour iOS
platform: iOS
page_order: 0
description: "Cet article explique comment intégrer les notifications push dans votre application iOS."
channel:
  - Pousser
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'
---

# Intégration Push

## Étape 1 : Configurer les notifications push

Avant de pouvoir envoyer une notification push iOS en utilisant Braze, vous devez fournir votre fichier de notification Push ou un certificat d'Apple. Vous pouvez présenter soit un fichier `.p8` (recommandé) soit un certificat `.p12`.

{% tabs local %}
  {% tab .p8 File (Recommended) %}
__Utilisation d'un fichier .p8 (jetons d'authentification)__

Comme décrit sur [cette page](https://help.apple.com/developer-account/#/devcdfbb56a3):

1. Dans votre compte développeur, allez dans [Certificats, Identifiants & Profils](https://developer.apple.com/account/ios/certificate).
2. Sous Touches, sélectionnez Tout et cliquez sur le bouton Ajouter (+) dans le coin supérieur droit.
3. Sous Description de la clé, entrez un nom unique pour la clé de signature.
4. Sous Services clés, sélectionnez la case à cocher APN, puis cliquez sur Continuer. Cliquez sur Confirmer.
5. Notez l'ID de la clé. Cliquez sur Télécharger pour générer et télécharger la clé maintenant.

> Lorsque vous téléchargez la clé, elle est enregistrée comme un fichier texte avec une extension de fichier .p8. Enregistrez le fichier dans un endroit sécurisé car la clé **n'est pas enregistrée dans votre compte développeur et vous ne pourrez plus le télécharger**.

6. Naviguez vers la page [Paramètres](https://dashboard-01.braze.com/app_settings/app_settings) dans le tableau de bord et téléchargez le fichier .p8.
7. Lorsque vous y êtes invité, entrez également l'ID de votre [application Bundle](https://developer.apple.com/account/ios/identifier/bundle/), le [Key Id](https://developer.apple.com/account/ios/authkey), et votre [Team Id](https://developer.apple.com/account/#/membership). Cliquez sur `Enregistrer`.

{% endtab %}
{% tab .p12 Certificate (Legacy) %}
__Utiliser un certificat .p12 (ancien)__

Alternativement, vous pouvez utiliser les anciennes méthodes d'authentification d'Apple (certificats SSL .p12). Contrairement à la solution .p8 décrite ci-dessus, ces certificats expirent automatiquement chaque année et vous demanderont de les régénérer et de les retélécharger. Braze vous enverra des rappels par e-mail lorsque le certificat approchera de l'expiration pour aider vos notifications à continuer ininterrompu, mais comme il s'agit d'un processus manuel, nous vous recommandons d'utiliser ce qui précède . 8 schémas d'authentification à la place.  Cependant, si vous le souhaitez, vous pouvez configurer et télécharger les certificats .p12 comme décrit ici :

__Étape 1 : Générer une demande de signature de certificat__

1. Accédez au [portail de provisioning iOS](https://developer.apple.com/ios/manage/overview/index.action)
2. Sélectionnez Identifiants > ID d'application dans la barre latérale de gauche<br>![Mise en place d'iOS]({% image_buster /assets/img_archive/ios_provisioning.png %})
3. Sélectionnez votre application.
4. Si les notifications push ne sont pas activées, cliquez sur Modifier pour mettre à jour les paramètres de l'application<br>![Options d'AppleProvisioning]({% image_buster /assets/img_archive/AppleProvisioningOptions.png %})
5. Cochez la case Activer et cliquez sur Créer un certificat sous le certificat SSL de production<br>![iOSPush32]({% image_buster /assets/img_archive/push_cert_gen.png %})
6. Suivez les instructions de l'assistant de certificat SSL. Vous devriez maintenant voir un statut vert pour indiquer que le push est activé.

> Vous devez mettre à jour votre profil de provisioning pour l'application après avoir créé vos certificats SSL. Un simple "Actualiser" dans l'organisateur va accomplir cela.

__Étape 2 : Exporter le certificat__

1. Téléchargez le certificat de production push que vous venez de créer et ouvrez-le avec l'application Keychain Access.
2. Dans Keychain Access, cliquez sur Mes certificats et localisez votre certificat push.
3. Exportez-le comme un fichier `.p12` et utilisez un mot de passe temporaire et non sécurisé (vous aurez besoin de ce mot de passe lors du téléchargement de votre certificat sur Braze).
4. Accédez à la page [Paramètres](https://dashboard-01.braze.com/app_settings/app_settings) dans le tableau de bord et téléchargez votre certificat de production.

![Envoyer l'exemple de téléversement]({% image_buster /assets/img_archive/push_cert_upload.png %})

> Vous pouvez télécharger vos certificats de développement ou de production sur le tableau de bord de vos applications de profil de provisioning de distribution, mais vous ne pouvez avoir qu'un seul actif à la fois. En tant que tel, si vous souhaitez effectuer des tests répétés des notifications push une fois que votre application est mise en ligne dans l'App Store, Nous vous recommandons de configurer un groupe d'applications séparé ou une application pour la version de développement de votre application.

  {% endtab %}
{% endtabs %}


## Étape 2 : Activer les capacités push

Dans les paramètres de votre projet, assurez-vous que sous l'onglet `Capacités` votre capacité `Notifications` est activée. tel que décrit sur [cette page](https://help.apple.com/developer-account/#/devcdfbb56a3).

!\[activer la notification push\]\[24\]

> Si vous avez des certificats de développement et de production séparés, assurez-vous de décocher la case `Gérer automatiquement la signature` dans l’onglet `Général`. Cela vous permettra de choisir différents profils de provisioning pour chacune de vos configurations de compilation, car la fonctionnalité de signature automatique du code Xcode ne fait que la signature de développement. !\[xcode 8 auto signing\]\[34\]

## Étape 3 : S'inscrire pour les notifications push

L'exemple de code approprié ci-dessous doit être inclus dans l'application `de votre application:didFinishLaunchingWithOptions:` méthode déléguée pour l'enregistrement de vos utilisateurs avec les APN.

Braze fournit également des catégories de push par défaut pour la prise en charge des boutons d'action push qui doivent être ajoutés manuellement à votre code d'enregistrement push. Consultez notre [documentation sur les boutons d'action de poussée][35] pour des étapes d'intégration supplémentaires.

> Si vous avez implémenté une invite push personnalisée comme décrit dans nos [meilleures pratiques de push][], assurez-vous que vous appelez le code suivant **TOUS LES fois que l'application s'exécute** après qu'ils accordent des autorisations push à votre application. **Les applications ont besoin de se réinscrire avec des APN comme [les jetons de périphérique peuvent changer arbitrairement][19].**

{% alert warning %}
Assurez-vous d'appeler tous les codes d'intégration push dans le fil de discussion principal de votre application.
{% endalert %}

### Utilisation du framework de notification utilisateur (iOS 10+)

Si vous utilisez le framework `UserNotifications` (recommandé) qui a été introduit dans iOS 10, ajouter le code suivant à l'application `:didFinishLaunchingWithOptions :` méthode de votre délégué d'application.

{% alert important %}
L'exemple de code ci-dessous inclut l'intégration pour l'authentification Provisional Push (lignes 5 et 6 dans l'onglet `Objective-C` ; lignes 5 et 6 dans l'onglet `Swift`. Si vous ne prévoyez pas d'utiliser une autorisation provisoire dans votre application, vous pouvez supprimer les lignes de code qui ajoutent `UNAuthorizationOptionProvisional` aux options `requestAuthorization` dans l'extrait de code ci-dessus. En savoir plus sur [l'authentification provisoire, les options de notification iOS et iOS 12 ici]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_options_ios/).
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  centre. elegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12. , *)) {
  options = options | UNAuthorizationOptionProvision;
  }
  [centre requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL accordé, NSError * _Nullable error) {
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
  center.delegate = self as ? UNUserNotificationCenterDelegate
  options var : UNAuthorizationOptions = [.alert, .sound, . adge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options. awValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (accordé, erreur) dans
    Appboy.sharedInstance()?. ushAuthorization(fromUserNotificationCenter: accorted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, . ound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
Vous devez assigner votre objet délégué en utilisant `center.delegate = self` synchronément avant que votre application ne finisse de démarrer, de préférence dans `application:didFinishLaunchingWithOptions:`. Si vous ne le faites pas, votre application risque de manquer les notifications push entrantes. For more information, visit Apple's [`UNUserNotificationCenterDelegate` documentation](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate).
{% endalert %}

### Sans framework UserNotifications

Si vous n'utilisez pas le framework `UserNotifications` , ajoutez le code suivant à l'application `: didFinishLaunchingWithOptions :` méthode de votre délégué d'application:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplicationApplication] registerUserNotificationSettings:settings];
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


## Étape 4 : Enregistrer les jetons push avec Braze

Une fois l'inscription des APN terminée, la méthode suivante doit être modifiée pour passer le `deviceToken` à Braze afin que l'utilisateur soit activé pour les notifications push :

{% tabs %}
{% tab OBJECTIVE-C %}

Ajoutez le code suivant à votre application `: didRegisterForRemoteNotificationsWithDeviceToken :` méthode :

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

Ajoute le code suivant à l'application `de votre application (_:didRegisterForRemoteNotificationsWithDeviceToken:)` méthode :

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
L'application `: didRegisterForRemoteNotificationsWithDeviceToken:` la méthode déléguée est appelée à chaque fois après `[[UIApplication sharedApplication] registerForRemoteNotifications]` est appelée. Si vous êtes en train de migrer vers Braze à partir d'un autre service push et que l'appareil de votre utilisateur est déjà enregistré avec les APNs, cette méthode collectera des jetons à partir des enregistrements existants la prochaine fois que la méthode sera appelée, et les utilisateurs n'auront pas à réopter pour pousser.
{% endalert %}

## Étape 5 : Activer la gestion des push

Le code suivant passe les notifications push reçues le long de Braze et est nécessaire pour la journalisation des analyses push et la gestion des liens.

{% alert warning %}
Assurez-vous d'appeler tous les codes d'intégration push dans le fil de discussion principal de votre application.
{% endalert %}

### iOS 10 +

Lors de la compilation sur iOS 10+, nous vous recommandons d'intégrer le framework `UserNotifications` et de faire ce qui suit :

{% tabs %}
{% tab OBJECTIVE-C %}

Ajoutez le code suivant à l'application `de votre application:didReceiveRemoteNotification:fetchCompletionHandler:` méthode :

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Ensuite, ajoutez le code suivant à votre application `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` méthode :

```objc
[[Appboy sharedInstance] userNotificationCenter:centre
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**Manipulation des Push au premier plan**

Pour afficher une notification push lorsque l'application est au premier plan, implémentez `userNotificationCenter:willPresentNotification:withCompletionHandler:`:

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)centre
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14. , *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

Si la notification de premier plan est cliquée, le délégué de push iOS 10 `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` sera appelé et Braze enregistrera un événement push clic.

{% endtab %}
{% tab swift %}

Ajoute le code suivant à l'application `de votre application (_:didReceiveRemoteNotification:fetchCompletionHandler:)` méthode :

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

Ensuite, ajoutez le code suivant à la méthode `userNotificationCenter(_:didReceive:withCompletionHandler:)` de votre application:

```swift
Appboy.sharedInstance()?.userNotificationCenter(centre,
                                               didReceve: response,
                                               withCompletionHandler: completionHandler)
```

**Manipulation des Push au premier plan**

Pour afficher une notification push lorsque l'application est au premier plan, implémentez `userNotificationCenter(_:willPresent:withCompletionHandler:)`:

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              notification willPresent : NON Notification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14. , *) {
    completionHandler([.list, . anner]);
  } else {
    completionHandler([.alert]);
  }
}
```

Si la notification de premier plan est cliquée, le délégué de push iOS 10 `userNotificationCenter(_:didReceive:withCompletionHandler:)` sera appelé et Braze enregistrera un événement push click.

{% endtab %}
{% endtabs %}

### Pre-iOS 10

iOS 10 a mis à jour le comportement de telle sorte qu'il n'appelle plus `application:didReceiveRemoteNotification:fetchCompletionHandler:` lorsqu'un push est cliqué.  Pour cette raison, si vous ne mettez pas à jour pour compiler avec iOS 10+ et utilisez le framework `UserNotifications` vous devez appeler Braze des deux anciens délégués, ce qui est une rupture par rapport à notre intégration précédente.

Pour les applications construisant contre les SDKs < iOS 10, utilisez les instructions suivantes :

{% tabs %}
{% tab OBJECTIVE-C %}

Pour activer le traçage des notifications push, ajoutez le code suivant à l'application `de votre application:didReceiveRemoteNotification:fetchCompletionHandler:` méthode :

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Pour prendre en charge l'analyse push sur iOS 10, vous devez également ajouter le code suivant à l'application `de votre application:didReceiveRemoteNotification:` méthode déléguée :

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

Pour activer le traçage des notifications push, ajoutez le code suivant à l'application `de votre application (_:didReceiveRemoteNotification:fetchCompletionHandler:)`:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

Pour prendre en charge l'analyse push sur iOS 10, vous devez également ajouter le code suivant à l'application `de votre application (_:didReceiveRemoteNotification:)` méthode déléguée :

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## Étape 6 : Liaison profonde

Les liens profonds depuis une poussée vers l'application sont automatiquement gérés via notre documentation standard d'intégration push. Si vous souhaitez en savoir plus sur comment ajouter des liens profonds à des emplacements spécifiques dans votre application, voir notre section [Cas d'utilisation avancé sur Deep Linking pour iOS][10].
[24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %} [34]: {% image_buster /assets/img_archive/xcode8_auto_signing.png %}


[meilleures pratiques de push]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-implementation
[19]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html
[35]: #push-action-buttons-integration
