## Limites de débit

Les notifications push sont limitées en débit, n'ayez donc pas peur d'en envoyer autant que votre application en a besoin. iOS et les serveurs du service de notification push (APN) d'Apple contrôleront la fréquence à laquelle elles sont délivrées, et vous n'aurez pas d'ennuis si vous en envoyez trop. Si vos notifications push sont limitées, elles peuvent être retardées jusqu’à la prochaine fois que l’appareil envoie un paquet persistant ou reçoit une autre notification.

## Mise en place des notifications push

### Étape 1 : Téléchargez votre jeton APN

{% multi_lang_include developer_guide/swift/apns_token.md %}

### Étape 2 : Activer les fonctionnalités de notification push

Dans Xcode, accédez à la section **Signage et capacités de** la cible principale de l'app et ajoutez la capacité de notifications push.

![La section "Signing & Capabilities" dans un projet Xcode.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### Étape 3 : Mise en place de la manutention par poussée

Vous pouvez utiliser le SDK Swift pour automatiser le traitement des notifications à distance reçues de Braze. C'est la façon la plus simple de gérer les notifications push et c'est la méthode de gestion recommandée.

{% tabs local %}
{% tab Automatique %}
#### Étape 3.1 : Activer l'automatisation dans la propriété push

Pour activer l'intégration automatique des notifications push, définissez la propriété `automation` de la configuration `push` sur `true` :

{% subtabs %}
{% subtab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endsubtab %}
{% endsubtabs %}

Cela demande au SDK de :
- Enregistrer votre application pour les notifications push dans le système.
- Demander l'autorisation/permission de la notification push lors de l'initialisation.
- Fournir dynamiquement des implémentations pour les méthodes de délégation du système liées à la notification push.

{% alert note %}
Les étapes d'automatisation réalisées par le SDK sont compatibles avec les intégrations préexistantes de traitement des notifications push dans votre base de code. Le SDK automatise uniquement le traitement des notifications à distance reçues de Braze. Tout gestionnaire de système implémenté pour traiter vos propres notifications à distance ou celles d'un autre SDK tiers continue à fonctionner lorsque l’`automation` est activée.
{% endalert %}

{% alert warning %}
Le SDK doit être initialisé sur le fil de discussion principal pour permettre l'automatisation des notifications push. L'initialisation du SDK doit avoir lieu avant la fin du lancement de l'application ou dans l'implémentation des [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) de votre AppDelegate.
Si votre application nécessite une configuration supplémentaire avant l'initialisation du SDK, veuillez consulter la page de documentation [Initialisation différée]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift).
{% endalert %}

#### Étape 3.2 : Remplacer les configurations individuelles (en option)

Pour un contrôle plus précis, chaque étape d'automatisation peut être activée ou désactivée individuellement :

{% subtabs %}
{% subtab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endsubtab %}
{% endsubtabs %}

Voir [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) pour connaître toutes les options disponibles et [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) pour plus d'informations sur le comportement de l'automatisation.
{% endtab %}

{% tab Manual (Manuel) %}
{% alert note %}
Si vous comptez sur les notifications push pour des comportements supplémentaires spécifiques à votre appli, vous pouvez toujours utiliser l'intégration push automatique au lieu de l'intégration manuelle des notifications push. La méthode [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) permet d'être informé des notifications à distance traitées par Braze.
{% endalert %}

#### Étape 3.1 : S'inscrire aux notifications push avec les APN

Incluez l'exemple de code approprié dans la [méthode de délégation`application:didFinishLaunchingWithOptions:` ](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) de votre application afin que les appareils de vos utilisateurs puissent s'enregistrer auprès des APN. Assurez-vous d’appeler tout le code d’intégration push dans le thread principal de votre application.

Braze fournit également des catégories push par défaut pour la prise en charge des boutons d’action push, qui doivent être ajoutées manuellement à votre code d’enregistrement push. Reportez-vous aux [boutons d'action push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) pour connaître les étapes d'intégration supplémentaires.

Ajoutez le code suivant à la méthode `application:didFinishLaunchingWithOptions:` de votre délégué d'application. 

{% alert note %}
L’exemple de code suivant inclut l’intégration pour l’authentification de notification push provisoire (lignes 5 et 6). Si vous ne prévoyez pas d’utiliser l’autorisation provisoire dans votre application, vous pouvez supprimer les lignes du code qui ajoutent `UNAuthorizationOptionProvisional` aux options `requestAuthorization`.<br>Consultez les [options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) pour en savoir plus sur l'authentification provisoire par push.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

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

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Vous devez attribuer votre objet délégué à l’aide de `center.delegate = self` manière synchronisée avant que votre application ne termine son lancement, de préférence dans `application:didFinishLaunchingWithOptions:`. Sans cela, votre application risque de ne pas recevoir les notifications push entrantes. Consultez la documentation d'Apple [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) pour en savoir plus.
{% endalert %}

#### Étape 3.2 : Enregistrer des jetons avec Braze

Une fois l'enregistrement des APN terminé, transmettez le `deviceToken` généré à Braze pour activer les notifications push pour l'utilisateur.  

{% subtabs %}
{% subtab Swift %}

Ajoutez le code suivant à la méthode `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` de votre application :

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Ajoutez le code suivant à la méthode `application:didRegisterForRemoteNotificationsWithDeviceToken:` de votre application :

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
La méthode de délégation `application:didRegisterForRemoteNotificationsWithDeviceToken:` est appelée chaque fois après que `application.registerForRemoteNotifications()` soit employée. <br><br>Si vous migrez vers Braze depuis un autre service de notification push et que l’appareil de votre utilisateur a déjà enregistré des APN, cette méthode collectera des jetons à partir des enregistrements existants la prochaine fois que la méthode est utilisée, et les utilisateurs n’auront pas à se réabonner aux notifications push.
{% endalert %}

#### Étape 3.3 : Activer la gestion des notifications push

Ensuite, transmettez les notifications push reçues à Braze. Cette étape est nécessaire pour la journalisation de l'analyse/analytique push et la gestion des liens. Assurez-vous d’appeler tout le code d’intégration push dans le thread principal de votre application.

##### Traitement par défaut des notifications push

{% subtabs %}
{% subtab Swift %}
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
{% endsubtab %}

{% subtab OBJECTIVE-C %}
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
{% endsubtab %}
{% endsubtabs %}

##### Gestion des notifications push au premier plan

{% subtabs %}
{% subtab Swift %}
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
{% endsubtab %}

{% subtab OBJECTIVE-C %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Notifications d'essais {#push-testing}

Si vous souhaitez tester des notifications push et in-app à l’aide de la ligne de commande, vous pouvez envoyer une seule notification par le terminal via cURL et [l’API d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` - disponible dans **Réglages** > **Clés API**.
- `YOUR_EXTERNAL_USER_ID` - disponible sur la page **Recherche d'utilisateurs.**  Pour plus d'informations, reportez-vous à la rubrique [Attribution d'ID d'utilisateur]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id).
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

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

## Amorces de notifications push {#push-primers}

Les campagnes d'amorces de notifications push encouragent vos utilisateurs à activer les notifications push sur leur appareil pour votre appli. Ceci peut se faire sans personnalisation du SDK, grâce à notre [amorce de notifications push sans code]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Gestion dynamique des passerelles APN

La gestion dynamique de la passerelle du service de notification push d'Apple (APNs) améliore la fiabilité et l'efficacité des notifications push d'iOS en détectant automatiquement l'environnement APNs adéquat. Auparavant, vous deviez sélectionner manuellement des environnements APN (développement ou production) pour vos notifications push, ce qui entraînait parfois des configurations de passerelle incorrectes, des échecs de réception/distribution et des erreurs `BadDeviceToken`.

Grâce à la gestion dynamique des passerelles APN, vous aurez :

- **Amélioration de la fiabilité :** Les notifications sont toujours envoyées à l'environnement des APN corrects, ce qui réduit les échecs de réception/distribution.
- **Configuration simplifiée :** Vous n'avez plus besoin de gérer manuellement les paramètres des passerelles APN.
- **Résilience aux erreurs :** Les valeurs invalides ou manquantes de la passerelle sont traitées avec élégance, ce qui permet d'assurer un service ininterrompu.

### Conditions préalables

Braze prend en charge la gestion des passerelles APN dynamiques pour les notifications push sur iOS avec la condition de version du SDK suivante :

{% sdk_min_versions swift:10.0.0 %}

### Fonctionnement

Lorsqu'une app iOS s'intègre au SDK Swift de Braze, elle envoie des données liées à l'appareil, notamment [...] [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment) à l'API SDK de Braze, si elle est disponible. La valeur `apns_gateway` indique si l'application utilise l'environnement APN de développement (`dev`) ou de production (`prod`).

Braze enregistre également la valeur de la passerelle signalée pour chaque appareil. Si une nouvelle valeur de passerelle valide est reçue, Braze met automatiquement à jour la valeur stockée.

Lorsque Braze envoie une notification push :

- Si une valeur de passerelle valide (dev ou prod) est enregistrée pour l'appareil, Braze l'utilise pour déterminer l'environnement APN correct.
- Si aucune valeur de passerelle n'est enregistrée, Braze utilise par défaut l'environnement des APN configuré dans la page **Paramètres de l'application.** 

### Foire aux questions

#### Pourquoi cette fonctionnalité a-t-elle été introduite ?

Grâce à la gestion dynamique des passerelles APN, l'environnement adéquat est sélectionné automatiquement. Auparavant, vous deviez configurer manuellement la passerelle APN, ce qui pouvait entraîner des erreurs sur `BadDeviceToken`, l'invalidation des jetons et d'éventuels problèmes de limitation du débit des APN.

#### Quel est l'impact sur la performance de la réception/distribution ?

Cette fonctionnalité améliore les taux de réception/distribution en acheminant toujours les jetons push vers l'environnement des APN corrects, évitant ainsi les échecs causés par des passerelles mal configurées.

#### Puis-je désactiver cette fonctionnalité ?

La gestion dynamique des passerelles APN est activée par défaut et permet d'améliorer la fiabilité. Si vous avez des cas d'utilisation spécifiques qui nécessitent une sélection manuelle de la passerelle, contactez l'[assistance de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/).
