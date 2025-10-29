{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Mise en place des notifications push {#setting-up-push-notifications}

### Étape 1 : Terminer la configuration initiale

{% tabs local %}
{% tab Expo %}
#### Conditions préalables

Avant de pouvoir utiliser Expo pour les notifications push, vous devez [configurer le plugin Expo de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo).

#### Étape 1.1 : Mettez à jour votre fichier `app.json` 

Mettez ensuite à jour votre fichier `app.json` pour Android et iOS :

- **Android :** Ajoutez l'option `enableFirebaseCloudMessaging`.
- **iOS :** Ajoutez l'option `enableBrazeIosPush`.

#### Étape 1.2 : Ajouter votre ID d'expéditeur Google

Tout d'abord, accédez à la console Firebase, ouvrez votre projet, puis sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres du projet**.

![Le projet Firebase avec le menu Paramètres ouvert.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Sélectionnez **Messagerie Cloud**, puis sous **API Firebase Cloud Messaging (V1)**, copiez l'**ID de l'expéditeur** dans votre presse-papiers.

![La page Messagerie Cloud du projet Firebase avec l'ID de l'expéditeur mis en évidence.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Ensuite, ouvrez le fichier `app.json` de votre projet et attribuez à la propriété `firebaseCloudMessagingSenderId` l'ID de l'expéditeur figurant dans votre presse-papiers. Par exemple :

```
"firebaseCloudMessagingSenderId": "693679403398"
```

#### Étape 1.3 : Ajouter le chemin d'accès à votre JSON Google Services

Dans le fichier `app.json` de votre projet, ajoutez le chemin d'accès à votre fichier `google-services.json`. Ce fichier est nécessaire lors de la définition de `enableFirebaseCloudMessaging: true` dans votre configuration.

```json
{
  "expo": {
    "android": {
      "googleServicesFile": "PATH_TO_GOOGLE_SERVICES"
    },
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true
        }
      ],
    ]
  }
}
```

Notez que vous devrez utiliser ces paramètres au lieu des instructions de configuration natives si vous dépendez de bibliothèques de notifications push supplémentaires comme [Expo Notifications.](https://docs.expo.dev/versions/latest/sdk/notifications/)
{% endtab %}

{% tab Android Native %}
Si vous n'utilisez pas le plugin Braze Expo, ou si vous souhaitez plutôt configurer ces paramètres de manière native, inscrivez-vous à push en vous référant au [guide d'intégration native de push Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/).
{% endtab %}

{% tab Natif iOS %}
Si vous n'utilisez pas le plugin Braze Expo, ou si vous souhaitez plutôt configurer ces paramètres de manière native, inscrivez-vous à push en vous référant aux étapes suivantes du [guide de l'intégration push iOS native :]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)

#### Étape 1.1 : Demande d'autorisation de pousser

Si vous n'avez pas l'intention de demander des permissions push au lancement de l'application, omettez l'appel à `requestAuthorizationWithOptions:completionHandler:` dans votre AppDelegate. Passez ensuite à l'[étape 2](#reactnative_step-2-request-push-notifications-permission). Sinon, suivez le [guide d'intégration native d'iOS.]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)

#### Étape 1.2 (facultative) : Migrer votre clé de notifications push

Si vous utilisiez auparavant `expo-notifications` pour gérer votre clé de notification push, exécutez `expo fetch:ios:certs` dans le dossier racine de votre application. Cela téléchargera votre clé de notification push (un fichier .p8), qui peut ensuite être téléchargée sur le tableau de bord de Braze.
{% endtab %}
{% endtabs %}

### Étape 2 : Demander une autorisation de notification push

Utilisez la méthode `Braze.requestPushPermission()` (disponible sur v1.38.2 et supérieures) pour demander une autorisation des notifications push à l’utilisateur sur iOS et Android 13 et supérieurs. Pour Android 12 et inférieurs, cette méthode n’est pas opérationnelle.

Cette méthode intègre in paramètre requis qui précise les autorisations que SDK doit demander à l’utilisateur sur iOS. Ces options n’ont pas d’effet sur Android.

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

#### Étape 2.1 : Écouter les notifications push (facultatif)

Vous pouvez en outre vous abonner aux événements au cours desquels Braze a détecté et traité une notification push entrante. Utilisez la clé d'auditeur `Braze.Events.PUSH_NOTIFICATION_EVENT`.

{% alert important %}
Les événements iOS push reçus ne se déclenchent que pour les notifications en avant-plan et `content-available` pour les notifications en arrière-plan. Il ne se déclenchera pas pour les notifications reçues alors qu'elles sont terminées ou pour les notifications d'arrière-plan sans le champ `content-available`.
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

##### Champs d'événements de la notification push

Pour obtenir une liste complète des champs de notifications push, reportez-vous au tableau ci-dessous :

| Nom du champ         | Type      | Description |
| ------------------ | --------- | ----------- |
| `payload_type`     | Chaîne de caractères    | Spécifie le type de charge utile de la notification. Les deux valeurs envoyées par le SDK React native de Braze sont `push_opened` et `push_received`. |
| `url`              | Chaîne de caractères    | Spécifie l'URL qui a été ouvert par la notification. |
| `use_webview`      | Valeur booléenne   | Si la valeur est `true`, l'URL s'ouvrira dans l'application, dans une fenêtre WebView modale. Si la valeur est `false`, l'URL s'ouvrira dans le navigateur de l'appareil. |
| `title`            | Chaîne de caractères    | Représente le titre de la notification. |
| `body`             | Chaîne de caractères    | Représente le corps ou le contenu du texte de la notification. |
| `summary_text`     | Chaîne de caractères    | Représente le texte résumé de la notification. Celle-ci est mappée à partir de `subtitle` sur iOS. |
| `badge_count`      | Nombre   | Représente le nombre de badges de la notification. |
| `timestamp`        | Nombre | Représente l'heure à laquelle la charge utile a été reçue par l'application. |
| `is_silent`        | Valeur booléenne   | Si la valeur est `true`, la charge utile est reçue en silence. Pour plus de détails sur l'envoi de notifications push silencieuses sur Android, reportez-vous à la section [Notifications push silencieuses sur Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Pour plus de détails sur l'envoi de notifications push silencieuses sur iOS, reportez-vous à la section [Notifications push silencieuses sur iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `is_braze_internal`| Valeur booléenne   | Cette adresse sera `true` si une charge utile de notification a été envoyée pour une fonctionnalité interne du SDK, telle que la synchronisation des géorepérages, la synchronisation des indicateurs de fonctionnalités ou le suivi des désinstallations. La charge utile est reçue silencieusement par l'utilisateur. |
| `image_url`        | Chaîne de caractères    | Spécifie l'URL associée à l'image de notification. |
| `braze_properties` | Objet    | Représente les propriétés de Braze associées à la campagne (paires clé-valeur). |
| `ios`              | Objet    | Représente les champs spécifiques à iOS. |
| `android`          | Objet    | Représente les champs spécifiques à Android. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 3 : Activer la création de liens profonds (facultatif)

Pour permettre à Braze de gérer les liens profonds à l'intérieur des composants React lorsqu'une notification push est cliquée, mettez d'abord en œuvre les étapes décrites dans la bibliothèque [React Native Linking](https://reactnative.dev/docs/linking), ou avec la solution de votre choix. Ensuite, suivez les étapes supplémentaires ci-dessous.

Pour en savoir plus sur les liens profonds, consultez notre [article de FAQ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% tabs local %}
{% tab Android Native %}
Si vous utilisez le [plugin Braze Expo]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option), vous pouvez gérer automatiquement les liens profonds de notification push en réglant `androidHandlePushDeepLinksAutomatically` sur `true` dans votre `app.json`.

Pour gérer manuellement les liens profonds, reportez-vous à la documentation native d'Android : [Création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking).

{% endtab %}
{% tab Natif iOS %}
#### Étape 3.1 : Stocker la charge utile de la notification push au lancement de l'application.
{% alert note %}
Sautez l'étape 3.1 si vous utilisez le plugin Braze Expo, car cette fonctionnalité est gérée automatiquement.
{% endalert %}

Pour iOS, ajoutez `populateInitialPayloadFromLaunchOptions` à la méthode `didFinishLaunchingWithOptions` de votre AppDelegate. Par exemple :

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  self.moduleName = @"BrazeProject";
  self.initialProps = @{};

  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  configuration.triggerMinimumTimeInterval = 1;
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  [self registerForPushNotifications];
  [[BrazeReactUtils sharedInstance] populateInitialPayloadFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

#### Étape 3.2 : Gestion des liens profonds à partir d'un état fermé

En plus des scénarios de base gérés par [React Native Linking](https://reactnative.dev/docs/linking), mettez en œuvre la méthode `Braze.getInitialPushPayload` et récupérez la valeur `url` pour prendre en compte les liens profonds issus des notifications push qui ouvrent votre application lorsqu'elle n'est pas en cours d'exécution. Par exemple :

```javascript
// Handles deep links when an iOS app is launched from a hard close via push click.
// This edge case is not handled in the React Native Linking library and is provided as a workaround by Braze.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
Braze fournit cette solution de contournement car l'API de liaison de React Native ne prend pas en charge ce scénario en raison d'une condition de concurrence au démarrage de l'appli.
{% endalert %}

#### Étape 3.3 Activer les liens universels (facultatif)

Pour activer la prise en charge de la [liaison universelle]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links), créez un fichier `BrazeReactDelegate.h` dans votre répertoire `iOS`, puis ajoutez l'extrait de code suivant.

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

Ensuite, créez un fichier `BrazeReactDelegate.m` et ajoutez-y l'extrait de code suivant. Remplacez `YOUR_DOMAIN_HOST` par votre domaine réel.

```objc
#import "BrazeReactDelegate.h"
#import <UIKit/UIKit.h>

@implementation BrazeReactDelegate

/// This delegate method determines whether to open a given URL.
///
/// Reference the `BRZURLContext` object to get additional details about the URL payload.
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"YOUR_DOMAIN_HOST"]) {
    // Sample custom handling of universal links
    UIApplication *application = UIApplication.sharedApplication;
    NSUserActivity* userActivity = [[NSUserActivity alloc] initWithActivityType:NSUserActivityTypeBrowsingWeb];
    userActivity.webpageURL = context.url;
    // Routes to the `continueUserActivity` method, which should be handled in your `AppDelegate`.
    [application.delegate application:application
                 continueUserActivity:userActivity restorationHandler:^(NSArray<id<UIUserActivityRestoring>> * _Nullable restorableObjects) {}];
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}

@end
```

Ensuite, créez et enregistrez votre `BrazeReactDelegate` dans `didFinishLaunchingWithOptions` du fichier `AppDelegate.m` de votre projet.

```objc
#import "BrazeReactUtils.h"
#import "BrazeReactDelegate.h"

@interface AppDelegate ()

// Keep a strong reference to the BrazeDelegate to ensure it is not deallocated.
@property (nonatomic, strong) BrazeReactDelegate *brazeDelegate;

@end

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // Other setup code

  self.brazeDelegate = [[BrazeReactDelegate alloc] init];
  braze.delegate = self.brazeDelegate;
}
```

Pour un exemple d'intégration, référez-vous à notre exemple d'application [ici.](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm)
{% endtab %}
{% endtabs %}

### Étape 4 : Envoyer une notification push test

À ce stade, vous devriez pouvoir envoyer des notifications aux appareils. Suivez ces étapes pour tester votre intégration de notification push.

{% alert note %}
À partir de macOS 13, sur certains appareils, vous pouvez tester les notifications push d'iOS sur un simulateur iOS 16+ fonctionnant avec Xcode 14 ou une version plus récente. Pour plus de détails, reportez-vous aux [notes de version de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Définissez un utilisateur actif dans l'application React native en appelant la méthode `Braze.changeUserId('your-user-id')`.
2. Allez dans **Campagnes** et créez une nouvelle campagne de notification push. Choisissez les plateformes que vous souhaitez tester.
3. Composez votre notification test et sélectionnez l’onglet **Test**. Ajoutez le même `user-id` que l'utilisateur test et cliquez sur **Envoyer le test**. Vous devriez recevoir rapidement la notification sur votre appareil.

![Une campagne push de Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire test pour tester votre notification push.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Utiliser le plugin Expo

Après avoir [configuré les notifications push pour Expo](#reactnative_setting-up-push-notifications), vous pouvez l'utiliser pour gérer les comportements de notifications push suivants - sans avoir besoin d'écrire le moindre code dans les couches natives d'Android ou d'iOS.

### Transférer les notifications push Android vers un autre FMS

Si vous souhaitez utiliser un service de messagerie Firebase (FMS) supplémentaire, vous pouvez spécifier un FMS de repli à appeler si votre application reçoit une notification push qui ne provient pas de Braze. Par exemple :

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "androidFirebaseMessagingFallbackServiceEnabled": true,
          "androidFirebaseMessagingFallbackServiceClasspath": "com.company.OurFirebaseMessagingService"
        }
      ]
    ]
  }
}
```

### Utiliser les extensions d'applications avec Expo Application Services {#app-extensions}

Si vous utilisez Expo Application Services (EAS) et que vous avez activé `enableBrazeIosRichPush` ou `enableBrazeIosPushStories`, vous devrez déclarer les identifiants de bundle correspondants pour chaque extension d'application dans votre projet. Vous pouvez aborder cette étape de plusieurs manières, selon la façon dont votre projet est configuré pour gérer la signature de code avec EAS.

Une approche consiste à utiliser la configuration `appExtensions` dans votre fichier `app.json` en suivant la [documentation sur les extensions d’applications](https://docs.expo.dev/build-reference/app-extensions/) d’Expo. Vous pouvez également définir le paramètre `multitarget` dans votre fichier `credentials.json` en suivant la [documentation sur les identifiants locaux](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project) d’Expo.

### Résolution des problèmes

Voici les étapes de résolution des problèmes les plus courantes pour les intégrations de notifications push avec le SDK React Native et le plugin Expo de Braze.

#### Les notifications push ne fonctionnent plus {#troubleshooting-stopped-working}

Si les notifications push via le plugin Expo ont cessé de fonctionner :

1. Vérifiez que le SDK de Braze assure toujours le suivi des sessions.
2. Vérifiez que le SDK n'a pas été désactivé par un appel explicite ou implicite à `wipeData`.
3. Examinez les mises à jour récentes d'Expo ou des bibliothèques associées, car il peut y avoir des conflits avec votre configuration Braze.
4. Examinez les dépendances de projet récemment ajoutées et vérifiez si elles remplacent manuellement vos méthodes de délégué de notification push existantes.

{% alert tip %}
Pour les intégrations iOS, vous pouvez également vous référer à notre [tutoriel de configuration des notifications push](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications) pour vous aider à identifier les conflits potentiels avec les dépendances de votre projet.
{% endalert %}

#### Le jeton de l'appareil ne s'enregistre pas dans Braze {#troubleshooting-token-registration}

Si le jeton de votre appareil ne s'enregistre pas dans Braze, examinez d'abord les [notifications push qui ne fonctionnent plus.](#troubleshooting-stopped-working)

Si votre problème persiste, il se peut qu'une dépendance distincte interfère avec votre configuration de notification push de Braze. Vous pouvez essayer de le supprimer ou d'appeler manuellement `Braze.registerPushToken` à la place.
