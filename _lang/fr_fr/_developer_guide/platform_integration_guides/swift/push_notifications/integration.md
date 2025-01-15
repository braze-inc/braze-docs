---
nav_title: Intégration
article_title: Intégration Push pour iOS
platform: Swift
page_order: 0
description: "Cet article de référence explique comment configurer les notifications push iOS pour le SDK Swift de Braze."
channel:
  - push
  
---

# Intégration de notifications Push

> Cet article de référence explique comment configurer les notifications push iOS pour le SDK Swift de Braze.

[Les notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) vous permettent d'envoyer des notifications depuis votre appli lorsque des événements importants se produisent. Vous pouvez envoyer une notification push lorsque vous avez de nouveaux messages instantanés à envoyer, des alertes d’actualité à envoyer ou le dernier épisode de l’émission télévisée préférée de votre utilisateur prêt à être téléchargé pour un visionnage hors ligne. Les notifications push peuvent également être [silencieuses]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/), n'étant utilisées que pour mettre à jour l'interface de votre appli ou déclencher des travaux en arrière-plan. 

Les notifications push sont idéales pour le contenu sporadique, mais immédiatement important, alors que le délai entre les récupérations en arrière-plan peut ne pas être acceptable. Les notifications push peuvent également être beaucoup plus efficaces que la récupération en arrière-plan, car votre application ne démarre que si nécessaire. 

Les notifications push sont limitées en débit, n'ayez donc pas peur d'en envoyer autant que votre application en a besoin. iOS et les serveurs du service de notification push (APN) d'Apple contrôleront la fréquence à laquelle elles sont délivrées, et vous n'aurez pas d'ennuis si vous en envoyez trop. Si vos notifications push sont limitées, elles peuvent être retardées jusqu’à la prochaine fois que l’appareil envoie un paquet persistant ou reçoit une autre notification.

## Configuration initiale

### Étape 1 : Téléchargez votre certificat d'APN

Avant de pouvoir envoyer une notification push iOS à l'aide de Braze, vous devez fournir votre fichier de notifications push `.p8` fourni par Apple. Comme décrit dans la [documentation du développeur Apple](https://developer.apple.com/documentation/usernotifications) :

1. Dans votre compte de développeur Apple, allez dans [**Certificats, identifiants et profils**](https://developer.apple.com/account/ios/certificate).
2. Sous **Clés**, sélectionnez **Tous** et cliquez sur le bouton d'ajout (+) dans le coin supérieur droit.
3. Sous **Description de la clé**, saisissez un nom unique pour la clé de signature.
4. Sous **Services clés**, cochez la case **Service de notification push d'Apple (APN)**, puis cliquez sur **Continuer.** Cliquez sur **Confirmer**.
5. Notez l’ID de la clé. Cliquez sur **Télécharger** pour générer et télécharger la clé. Assurez-vous d’enregistrer le fichier téléchargé dans un endroit sécurisé, car vous ne pouvez pas le télécharger plus d’une fois.
6. Dans Braze, allez dans **Paramètres** > **Paramètres des applications** et téléchargez le fichier `.p8` sous **Certificat de notification push Apple**. Vous pouvez charger votre certificat de notifications push de développement ou de production. Pour tester les notifications push une fois que votre application est en ligne dans l'App Store, il est recommandé de créer un espace de travail distinct pour la version de développement de votre application.
7. Lorsque vous y êtes invité, saisissez l'[ID d'offre groupée](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), l'[ID de clé](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/) et l'[ID d’équipe](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id) de votre application, puis cliquez sur **Enregistrer**.

{% alert note %}
Si vous utilisez l'[ancienne version de la navigation]({{site.baseurl}}/navigation), vous pouvez télécharger votre fichier `.p8` à partir de **Gérer les paramètres** > **Paramètres**.
{% endalert %}

### Étape 2 : Activer les fonctionnalités de notification push

Dans Xcode, accédez à la section **Signage et capacités de** la cible principale de l'app et ajoutez la capacité de notifications push.

![La section "Signing & Capabilities" dans un projet Xcode.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

## Intégration automatique de la poussée

Le SDK Swift propose une approche basée uniquement sur la configuration pour automatiser le traitement des notifications à distance reçues de Braze. Cette approche est la manière la plus simple d'intégrer les notifications push et est recommandée pour la plupart des clients.

Pour activer l'intégration automatique des notifications push, définissez la propriété `automation` de la configuration `push` sur `true` :

{% tabs %}
{% tab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endtab %}
{% endtabs %}

Cela demande au SDK de :
- Enregistrer votre application pour les notifications push dans le système.
- Demander l'autorisation/permission de la notification push lors de l'initialisation.
- Fournir dynamiquement des implémentations pour les méthodes de délégation du système liées à la notification push.

{% alert note %}
Les étapes d'automatisation réalisées par le SDK sont compatibles avec les intégrations préexistantes de traitement des notifications push dans votre base de code. Le SDK automatise uniquement le traitement des notifications à distance reçues de Braze. Tout gestionnaire de système implémenté pour traiter vos propres notifications à distance ou celles d'un autre SDK tiers continue à fonctionner lorsque l’`automation` est activée.
{% endalert %}

{% alert warning %}
Le SDK doit être initialisé sur le fil de discussion principal pour permettre l'automatisation des notifications push. L'initialisation du SDK doit avoir lieu avant la fin du lancement de l'application ou dans l'implémentation des [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) de votre AppDelegate.
Si votre application nécessite une configuration supplémentaire avant l'initialisation du SDK, veuillez consulter la page de documentation [Initialisation différée]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/).
{% endalert %}

### Remplacer des configurations individuelles

Pour un contrôle plus précis, chaque étape d'automatisation peut être activée ou désactivée individuellement :

{% tabs %}
{% tab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endtab %}
{% endtabs %}

Voir [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) pour connaître toutes les options disponibles et [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) pour plus d'informations sur le comportement de l'automatisation.

Vous pouvez sauter la section suivante et passer à la [création de liens profonds](#deep-linking) si vous utilisez l'intégration push automatique.

## Intégration manuelle par poussée

Les notifications push peuvent également être intégrées manuellement. Cette section décrit les étapes nécessaires à cette intégration. 

{% alert note %}
Si vous comptez sur les notifications push pour des comportements supplémentaires spécifiques à votre appli, vous pouvez toujours utiliser l'intégration push automatique au lieu de l'intégration manuelle des notifications push. La méthode [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) permet d'être informé des notifications à distance traitées par Braze.
{% endalert %}

### Étape 1 : S'inscrire aux notifications push avec les APN

Incluez l'exemple de code approprié dans la [méthode de délégation`application:didFinishLaunchingWithOptions:` ](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) de votre application afin que les appareils de vos utilisateurs puissent s'enregistrer auprès des APN. Assurez-vous d’appeler tout le code d’intégration push dans le thread principal de votre application.

Braze fournit également des catégories push par défaut pour la prise en charge des boutons d’action push, qui doivent être ajoutées manuellement à votre code d’enregistrement push. Reportez-vous aux [boutons d'action push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/) pour connaître les étapes d'intégration supplémentaires.

Ajoutez le code suivant à la méthode `application:didFinishLaunchingWithOptions:` de votre délégué d'application. 

{% alert note %}
L’exemple de code suivant inclut l’intégration pour l’authentification de notification push provisoire (lignes 5 et 6). Si vous ne prévoyez pas d’utiliser l’autorisation provisoire dans votre application, vous pouvez supprimer les lignes du code qui ajoutent `UNAuthorizationOptionProvisional` aux options `requestAuthorization`.<br>Consultez les [options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) pour en savoir plus sur l'authentification provisoire par push.
{% endalert %}

{% tabs %}
{% tab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
Vous devez attribuer votre objet délégué à l’aide de `center.delegate = self` manière synchronisée avant que votre application ne termine son lancement, de préférence dans `application:didFinishLaunchingWithOptions:`. Sans cela, votre application risque de ne pas recevoir les notifications push entrantes. Consultez la documentation d'Apple [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) pour en savoir plus.
{% endalert %}

### Étape 2 : Enregistrer des jetons avec Braze

Une fois l'enregistrement des APN terminé, transmettez le `deviceToken` généré à Braze pour activer les notifications push pour l'utilisateur.  

{% tabs %}
{% tab Swift %}

Ajoutez le code suivant à la méthode `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` de votre application :

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endtab %}
{% tab OBJECTIF-C %}

Ajoutez le code suivant à la méthode `application:didRegisterForRemoteNotificationsWithDeviceToken:` de votre application :

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endtab %}
{% endtabs %}

{% alert important %}
La méthode de délégation `application:didRegisterForRemoteNotificationsWithDeviceToken:` est appelée chaque fois après que `application.registerForRemoteNotifications()` soit employée. <br><br>Si vous migrez vers Braze depuis un autre service de notification push et que l’appareil de votre utilisateur a déjà enregistré des APN, cette méthode collectera des jetons à partir des enregistrements existants la prochaine fois que la méthode est utilisée, et les utilisateurs n’auront pas à se réabonner aux notifications push.
{% endalert %}

### Étape 3 : Activer la gestion des notifications push

Ensuite, transmettez les notifications push reçues à Braze. Cette étape est nécessaire pour la journalisation de l'analyse/analytique push et la gestion des liens. Assurez-vous d’appeler tout le code d’intégration push dans le thread principal de votre application.

#### Traitement par défaut des notifications push

{% tabs %}
{% tab Swift %}
Pour activer la gestion du push par défaut de Braze, ajoutez le code suivant à la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de votre application :

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

Ensuite, ajoutez ce qui suit à la méthode `userNotificationCenter(_:didReceive:withCompletionHandler:)` de votre application :

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endtab %}

{% tab OBJECTIF-C %}
Pour activer la gestion du push par défaut de Braze, ajoutez le code suivant à la méthode `application:didReceiveRemoteNotification:fetchCompletionHandler:` de votre application :

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

Puis ajoutez le code suivant à la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de votre application :

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endtab %}
{% endtabs %}

#### Gestion des notifications push au premier plan

{% tabs %}
{% tab Swift %}
Pour activer les notifications push au premier plan et permettre à Braze de les reconnaître lorsqu'elles sont reçues, implémentez `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`. Si un utilisateur appuie sur votre notification au premier plan, le délégué push de `userNotificationCenter(_:didReceive:withCompletionHandler:)` sera appelé et Braze enregistrera l'événement push click.

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endtab %}

{% tab OBJECTIF-C %}
Pour activer les notifications push au premier plan et permettre à Braze de les reconnaître lorsqu'elles sont reçues, implémentez `userNotificationCenter:willPresentNotification:withCompletionHandler:`. Si un utilisateur appuie sur votre notification au premier plan, le délégué push de `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` sera appelé et Braze enregistrera l'événement push click.

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endtab %}
{% endtabs %}

## Création de liens profonds

La création de liens profonds d’une notification push vers l’application est gérée automatiquement via notre documentation d’intégration push standard. Si vous souhaitez en savoir plus sur la création de liens profonds vers des emplacements/localisations spécifiques dans votre application, consultez nos [cas d'utilisation avancés]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-implementation).

## S'abonner aux mises à jour par notification push

Pour accéder aux charges utiles des notifications push traitées par Braze, utilisez la méthode [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/).

Vous pouvez utiliser le paramètre `payloadTypes` pour indiquer si vous souhaitez vous abonner à des notifications concernant des événements push ouverts, des événements push reçus ou les deux.

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
Gardez à l'esprit que les événements reçus par les notifications push ne se déclenchent que pour les notifications au premier plan et pour les notifications en arrière-plan `content-available`. Il ne se déclenchera pas pour les notifications reçues alors qu'elles sont terminées ou pour les notifications d'arrière-plan sans le champ `content-available`.
{% endalert %}

{% endtab %}

{% tab OBJECTIF-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
Gardez à l'esprit que les événements reçus par les notifications push ne se déclenchent que pour les notifications au premier plan et pour les notifications en arrière-plan `content-available`. Il ne se déclenchera pas pour les notifications reçues alors qu'elles sont terminées ou pour les notifications d'arrière-plan sans le champ `content-available`.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
Lorsque vous utilisez l'intégration push automatique, `subscribeToUpdates(_:)` est le seul moyen d'être informé des notifications à distance traitées par Braze. Les méthodes système `UIAppDelegate` et `UNUserNotificationCenterDelegate` ne sont pas appelées lorsque la notification est traitée automatiquement par Braze.
{% endalert %}

{% alert tip %}
Créez votre abonnement de notification push dans `application(_:didFinishLaunchingWithOptions:)` pour vous assurer que votre abonnement est déclenché après qu'un utilisateur final a tapé sur une notification alors que votre appli est dans un état terminé.
{% endalert %}

## Tester {#push-testing}

Si vous souhaitez tester des notifications push et in-app à l’aide de la ligne de commande, vous pouvez envoyer une seule notification par le terminal via cURL et [l’API d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` - disponible dans **Réglages** > **Clés API**.
- `YOUR_EXTERNAL_USER_ID` - disponible sur la page **Recherche d'utilisateurs.**  Pour plus d'informations, reportez-vous à la rubrique [Attribution d'ID d'utilisateur]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id).
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), ces pages se trouvent à un emplacement/localisation différent : <br>\- Les **clés API** sont situées dans la **console de développement** > **Paramètres API**. <br>\- L’option **Rechercher des utilisateurs** est située dans **Utilisateurs** > **Recherche d'utilisateurs**
{% endalert %}

Dans l'exemple suivant, l'instance `US-01` est utilisée. Si vous n'êtes pas sur cette instance, reportez-vous à notre [documentation API]({{site.baseurl}}/api/basics/) pour savoir à quel endpoint adresser vos requêtes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Amorces de notifications push {#push-primers}

Les campagnes d'amorces de notifications push encouragent vos utilisateurs à activer les notifications push sur leur appareil pour votre appli. Ceci peut se faire sans personnalisation du SDK, grâce à notre [amorce de notifications push sans code]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

