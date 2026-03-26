{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Configuration des notifications push {#setting-up-push-notifications}

### Étape 1 : Terminer la configuration initiale

{% tabs local %}
{% tab Expo %}
#### Conditions préalables

Avant de pouvoir utiliser Expo pour les notifications push, il est nécessaire de [configurer le plugin Braze Expo]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo).

#### Étape 1.1 : Mettre à jour votre fichier `app.json`

Mettez ensuite à jour votre fichier `app.json` pour Android et iOS :

- **Android :** Ajoutez l'option `enableFirebaseCloudMessaging`.
- **iOS :** Ajoutez l'option `enableBrazeIosPush`.

#### Étape 1.2 : Ajouter votre ID d'expéditeur Google

Tout d'abord, accédez à la console Firebase, ouvrez votre projet, puis sélectionnez <i class="fa-solid fa-gear"></i>&nbsp;**Paramètres** > **Paramètres du projet**.

![Le projet Firebase avec le menu « Paramètres » ouvert.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Sélectionnez **Messagerie Cloud**, puis sous **API Firebase Cloud Messaging (V1)**, copiez l'**ID de l'expéditeur** dans votre presse-papiers.

![La page « Messagerie Cloud » du projet Firebase avec l'« ID de l'expéditeur » mis en évidence.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Ensuite, ouvrez le fichier `app.json` de votre projet et attribuez à la propriété `firebaseCloudMessagingSenderId` l'ID de l'expéditeur figurant dans votre presse-papiers. Par exemple :

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

Notez que vous devrez utiliser ces paramètres au lieu des instructions de configuration natives si vous dépendez de bibliothèques de notifications push supplémentaires comme [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/).
{% endtab %}

{% tab Android Native %}
Si vous n'utilisez pas le plugin Braze Expo ou si vous préférez configurer ces paramètres de manière native, inscrivez-vous pour les notifications push en vous référant au [guide d'intégration native des notifications push Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/).
{% endtab %}

{% tab iOS Native %}
Si vous n'utilisez pas le plugin Braze Expo ou si vous préférez configurer ces paramètres de manière native, inscrivez-vous pour les notifications push en suivant les étapes suivantes du [guide d'intégration native des notifications push iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) :

#### Étape 1.1 : Demander les autorisations de notification push

Si vous ne prévoyez pas de demander les autorisations push au lancement de l'application, omettez l'appel `requestAuthorizationWithOptions:completionHandler:` dans votre AppDelegate. Passez ensuite à [l'étape 2](#reactnative_step-2-request-push-notifications-permission). Sinon, suivez le [guide d'intégration native iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

#### Étape 1.2 (facultative) : Migrer votre clé de notification push

Si vous utilisiez auparavant `expo-notifications` pour gérer votre clé de notification push, exécutez `expo fetch:ios:certs` dans le dossier racine de votre application. Cela téléchargera votre clé de notification push (un fichier .p8), qui peut ensuite être importée dans le tableau de bord de Braze.
{% endtab %}
{% endtabs %}

### Étape 2 : Demander l'autorisation de notification push

Utilisez la méthode `Braze.requestPushPermission()` (disponible à partir de la version 1.38.0) pour demander l'autorisation des notifications push à l'utilisateur sur iOS et Android 13+. Pour Android 12 et versions antérieures, cette méthode est sans effet.

Cette méthode prend un paramètre requis qui spécifie les autorisations que le SDK doit demander à l'utilisateur sur iOS. Ces options n'ont aucun effet sur Android.

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

#### Étape 2.1 : Écouter les notifications push (facultatif)

Vous pouvez également vous abonner aux événements lorsque Braze a détecté et traité une notification push entrante. Utilisez la clé d'écoute `Braze.Events.PUSH_NOTIFICATION_EVENT`.

{% alert important %}
Les événements de réception push sur iOS ne se déclenchent que pour les notifications au premier plan et les notifications en arrière-plan avec `content-available`. Ils ne se déclenchent pas pour les notifications reçues lorsque l'application est fermée, ni pour les notifications en arrière-plan sans le champ `content-available`.
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

##### Champs d'événements de notification push

Pour obtenir la liste complète des champs de notification push, consultez le tableau ci-dessous :

| Nom du champ         | Type      | Description |
| ------------------ | --------- | ----------- |
| `payload_type`     | Chaîne de caractères    | Spécifie le type de PAYLOAD de la notification. Les deux valeurs envoyées par le SDK React Native de Braze sont `push_opened` et `push_received`. |
| `url`              | Chaîne de caractères    | Spécifie l'URL ouverte par la notification. |
| `use_webview`      | Valeur booléenne   | Si la valeur est `true`, l'URL s'ouvrira in-app via une WebView modale. Si la valeur est `false`, l'URL s'ouvrira dans le navigateur de l'appareil. |
| `title`            | Chaîne de caractères    | Représente le titre de la notification. |
| `body`             | Chaîne de caractères    | Représente le corps ou le contenu textuel de la notification. |
| `summary_text`     | Chaîne de caractères    | Représente le texte résumé de la notification. Correspond à `subtitle` sur iOS. |
| `badge_count`      | Nombre   | Représente le nombre de badges de la notification. |
| `timestamp`        | Nombre | Représente l'heure à laquelle le PAYLOAD a été reçu par l'application. |
| `is_silent`        | Valeur booléenne   | Si la valeur est `true`, le PAYLOAD est reçu silencieusement. Pour plus de détails sur l'envoi de notifications push silencieuses sur Android, consultez [Notifications push silencieuses sur Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Pour plus de détails sur l'envoi de notifications push silencieuses sur iOS, consultez [Notifications push silencieuses sur iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `is_braze_internal`| Valeur booléenne   | La valeur sera `true` si un PAYLOAD de notification a été envoyé pour une fonctionnalité interne du SDK, comme la synchronisation des géorepérages, la synchronisation des Feature Flags ou le suivi des désinstallations. Le PAYLOAD est reçu silencieusement par l'utilisateur. |
| `image_url`        | Chaîne de caractères    | Spécifie l'URL associée à l'image de la notification. |
| `braze_properties` | Objet    | Représente les propriétés Braze associées à la campagne (paires clé-valeur). |
| `ios`              | Objet    | Représente les champs spécifiques à iOS. |
| `android`          | Objet    | Représente les champs spécifiques à Android. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 3 : Activer la création de liens profonds (facultatif)

Pour permettre à Braze de gérer les liens profonds dans les composants React lorsqu'une notification push est cliquée, commencez par mettre en œuvre les étapes décrites dans la bibliothèque [React Native Linking](https://reactnative.dev/docs/linking) ou avec la solution de votre choix. Suivez ensuite les étapes supplémentaires ci-dessous.

Pour en savoir plus sur les liens profonds, consultez notre [article de FAQ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% tabs local %}
{% tab Android Native %}
Si vous utilisez le [plugin Braze Expo]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option), vous pouvez gérer automatiquement les liens profonds des notifications push en définissant `androidHandlePushDeepLinksAutomatically` sur `true` dans votre `app.json`.

Pour gérer manuellement les liens profonds, consultez la documentation native Android : [Ajout de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking).

#### Étape 3.1 : Enregistrer le PAYLOAD de la notification push au lancement de l'application

{% alert note %}
Cette fonctionnalité est prise en charge à partir de la version 19.1.0 du SDK React Native.
{% endalert %}

Ajoutez `populateInitialPushPayloadFromIntent` à la méthode `onCreate()` de votre activité principale. Cet appel doit être effectué avant l'initialisation de React Native afin de capturer les données Intent initiales. Par exemple :

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)
  super.onCreate(savedInstanceState)
}
```

#### Étape 3.2 : Gérer les liens profonds à partir d'un état fermé

En plus des scénarios de base gérés par [React Native Linking](https://reactnative.dev/docs/linking), implémentez la méthode `Braze.getInitialPushPayload` et récupérez la valeur `url` pour prendre en compte les liens profonds provenant de notifications push qui ouvrent votre application lorsqu'elle n'est pas en cours d'exécution. Par exemple :

```javascript
// Handles deep links when an app is launched from a hard close via push click.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
Cette méthode nécessite la configuration native de l'étape 3.1 pour votre plateforme. Si vous utilisez le plugin Braze Expo, cela peut être géré automatiquement.
{% endalert %}

{% endtab %}
{% tab iOS Native %}

{% alert important %}
Pour gérer les liens profonds à partir des notifications push sur iOS, vous devez également configurer la gestion des liens dans votre couche native iOS.
{% endalert %}

Cela inclut l'enregistrement d'un schéma d'URL personnalisé et l'implémentation d'un gestionnaire d'URL dans votre `AppDelegate`. Pour les instructions complètes de configuration, consultez [Gestion des liens profonds]({{site.baseurl}}/developer_guide/platforms/swift/in_app_messages/deep_linking/?tab=objective-c) dans la documentation native iOS.
#### Étape 3.1 : Enregistrer le PAYLOAD de la notification push au lancement de l'application
{% alert note %}
Ignorez l'étape 3.1 si vous utilisez le plugin Braze Expo, car cette fonctionnalité est gérée automatiquement.
{% endalert %}

Pour iOS, ajoutez `populateInitialPayloadFromLaunchOptions` à la méthode `didFinishLaunchingWithOptions` de votre AppDelegate. Par exemple :

{% subtabs local %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // ... Perform regular React Native setup

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
{% endsubtab %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
) -> Bool {
  // ... Perform regular React Native setup

  let configuration = Braze.Configuration(apiKey: apiKey, endpoint: endpoint)
  configuration.triggerMinimumTimeInterval = 1
  configuration.logger.level = .info
  let braze = BrazeReactBridge.initBraze(configuration)
  AppDelegate.braze = braze
  registerForPushNotifications()
  BrazeReactUtils.shared().populateInitialPayload(fromLaunchOptions: launchOptions)

  return super.application(application, didFinishLaunchingWithOptions: launchOptions)
}
```
{% endsubtab %}
{% endsubtabs %}

#### Étape 3.2 : Gérer les liens profonds à partir d'un état fermé

En plus des scénarios de base gérés par [React Native Linking](https://reactnative.dev/docs/linking), implémentez la méthode `Braze.getInitialPushPayload` et récupérez la valeur `url` pour prendre en compte les liens profonds provenant de notifications push qui ouvrent votre application lorsqu'elle n'est pas en cours d'exécution. Par exemple :

```javascript
// Handles deep links when an app is launched from a hard close via push click.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
Cette méthode nécessite la configuration native de l'étape 3.1 pour votre plateforme. Si vous utilisez le plugin Braze Expo, cela peut être géré automatiquement.
{% endalert %}

#### Étape 3.3 : Activer les liens universels (facultatif)

Pour activer la prise en charge des [liens universels]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links), implémentez un délégué Braze qui détermine s'il convient d'ouvrir une URL donnée, puis enregistrez-le auprès de votre instance Braze.

{% subtabs local %}
{% subtab Swift %}
Créez un fichier `BrazeReactDelegate.swift` dans votre répertoire `iOS` et ajoutez le contenu suivant. Remplacez `YOUR_DOMAIN_HOST` par votre domaine réel.

```swift
import Foundation
import BrazeKit
import UIKit

class BrazeReactDelegate: NSObject, BrazeDelegate {

  /// This delegate method determines whether to open a given URL.
  /// Reference the context to get additional details about the URL payload.
  func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
    if let host = context.url.host,
       host.caseInsensitiveCompare("YOUR_DOMAIN_HOST") == .orderedSame {
      // Sample custom handling of universal links
      let application = UIApplication.shared
      let userActivity = NSUserActivity(activityType: NSUserActivityTypeBrowsingWeb)
      userActivity.webpageURL = context.url
      // Routes to the `continueUserActivity` method, which should be handled in your AppDelegate.
      application.delegate?.application?(
        application,
        continue: userActivity,
        restorationHandler: { _ in }
      )
      return false
    }
    // Let Braze handle links otherwise
    return true
  }
}
```

Ensuite, créez et enregistrez votre `BrazeReactDelegate` dans `didFinishLaunchingWithOptions` du fichier `AppDelegate.swift` de votre projet.

```swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  
  static var braze: Braze?
  
  // Keep a strong reference to the BrazeDelegate so it is not deallocated.
  private var brazeDelegate: BrazeReactDelegate?
  
  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Other setup code (e.g., Braze initialization)
    
    brazeDelegate = BrazeReactDelegate()
    AppDelegate.braze?.delegate = brazeDelegate
    return true
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
Créez un fichier `BrazeReactDelegate.h` dans votre répertoire `iOS`, puis ajoutez l'extrait de code suivant.

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

Ensuite, créez un fichier `BrazeReactDelegate.m` et ajoutez l'extrait de code suivant. Remplacez `YOUR_DOMAIN_HOST` par votre domaine réel.

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
{% endsubtab %}
{% endsubtabs %}

Pour un exemple d'intégration, consultez notre application modèle [ici](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm).
{% endtab %}
{% endtabs %}

### Étape 4 : Gérer les notifications au premier plan

La gestion des notifications au premier plan fonctionne différemment selon votre plateforme et votre configuration. Choisissez l'approche qui correspond à votre intégration :

{% tabs local %}
{% tab iOS %}
Pour iOS, la gestion des notifications au premier plan est identique à celle de l'intégration native Swift. Appelez `handleForegroundNotification(notification:)` dans votre implémentation de `UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)`.

Pour des informations détaillées et des exemples de code, consultez [Gestion des notifications au premier plan]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#handling-foreground-notifications) dans la documentation des notifications push Swift.
{% endtab %}

{% tab Android %}
Pour Android, la gestion des notifications au premier plan est identique à celle de l'intégration native Android. Appelez `BrazeFirebaseMessagingService.handleBrazeRemoteMessage` dans votre méthode `FirebaseMessagingService.onMessageReceived`.

Pour des informations détaillées et des exemples de code, consultez [Gestion des notifications au premier plan]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications) dans la documentation des notifications push Android.
{% endtab %}

{% tab Expo %}
Dans le flux de travail géré par Expo, il n'est pas nécessaire d'appeler directement les gestionnaires de notifications natifs. Utilisez l'API Expo Notifications pour contrôler la présentation au premier plan, tandis que le plugin Braze Expo gère automatiquement le traitement natif.

```javascript
import * as Notifications from 'expo-notifications';
import Braze from '@braze/react-native-sdk';

// Control foreground presentation in Expo
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,    // Show alert while in foreground
    shouldPlaySound: false,
    shouldSetBadge: false,
  }),
});

// React to Braze push events
const subscription = Braze.addListener('pushNotificationEvent', (event) => {
  console.log('Braze push event', {
    type: event.payload_type,   // "push_received" | "push_opened"
    title: event.title,
    url: event.url,
    is_silent: event.is_silent,
  });
  // Handle deep links, custom behavior, etc.
});

// Handle initial payload when app launches via push
Braze.getInitialPushPayload((payload) => {
  if (payload) {
    console.log('Initial push payload', payload);
  }
});
```

{% alert note %}
Dans le flux de travail géré par Expo, le plugin Braze Expo gère automatiquement le traitement push natif. Vous contrôlez l'interface utilisateur au premier plan via les options de présentation des notifications Expo indiquées ci-dessus.
{% endalert %}

Pour les intégrations en flux de travail bare, suivez plutôt les approches natives iOS et Android.
{% endtab %}
{% endtabs %}

### Étape 5 : Envoyer une notification push de test

À ce stade, vous devriez pouvoir envoyer des notifications aux appareils. Suivez les étapes ci-dessous pour tester votre intégration de notification push.

{% alert note %}
À partir de macOS 13, sur certains appareils, vous pouvez tester les notifications push iOS sur un simulateur iOS 16+ fonctionnant avec Xcode 14 ou une version ultérieure. Pour plus de détails, consultez les [notes de version de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Définissez un utilisateur actif dans l'application React Native en appelant la méthode `Braze.changeUserId('your-user-id')`.
2. Accédez à **Campagnes** et créez une nouvelle campagne de notification push. Choisissez les plateformes que vous souhaitez tester.
3. Rédigez votre notification de test et accédez à l'onglet **Test**. Ajoutez le même `user-id` que l'utilisateur test et cliquez sur **Envoyer le test**. Vous devriez recevoir la notification sur votre appareil sous peu.

![Une campagne de notification push Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire de test pour tester votre notification push.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Utilisation du plugin Expo

Une fois [les notifications push configurées pour Expo](#reactnative_setting-up-push-notifications), vous pouvez les utiliser pour gérer les comportements de notifications push suivants, sans avoir à écrire de code dans les couches natives Android ou iOS.

### Transférer les notifications push Android vers un FMS supplémentaire

Si vous souhaitez utiliser un Firebase Messaging Service (FMS) supplémentaire, vous pouvez spécifier un FMS de repli à appeler si votre application reçoit une notification push qui ne provient pas de Braze. Par exemple :

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

### Utiliser les extensions d'application avec Expo Application Services {#app-extensions}

Si vous utilisez Expo Application Services (EAS) et que vous avez activé `enableBrazeIosRichPush` ou `enableBrazeIosPushStories`, vous devrez déclarer les identifiants de bundle correspondants pour chaque extension d'application dans votre projet. Vous pouvez aborder cette étape de plusieurs manières, selon la façon dont votre projet est configuré pour gérer la signature de code avec EAS.

Une approche consiste à utiliser la configuration `appExtensions` dans votre fichier `app.json` en suivant la [documentation sur les extensions d'application](https://docs.expo.dev/build-reference/app-extensions/) d'Expo. Vous pouvez également définir le paramètre `multitarget` dans votre fichier `credentials.json` en suivant la [documentation sur les identifiants locaux](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project) d'Expo.

### Résolution des problèmes

Voici les étapes courantes de résolution des problèmes pour les intégrations de notifications push avec le SDK Braze React Native et le plugin Expo.

#### Les notifications push ne fonctionnent plus {#troubleshooting-stopped-working}

Si les notifications push via le plugin Expo ne fonctionnent plus :

1. Vérifiez que le SDK Braze continue de suivre les sessions.
2. Vérifiez que le SDK n'a pas été désactivé par un appel explicite ou implicite à `wipeData`.
3. Examinez les mises à jour récentes d'Expo ou de ses bibliothèques associées, car il pourrait y avoir des conflits avec votre configuration Braze.
4. Examinez les dépendances récemment ajoutées au projet et vérifiez si elles remplacent manuellement vos méthodes déléguées de notification push existantes.

{% alert tip %}
Pour les intégrations iOS, vous pouvez également consulter notre [tutoriel de configuration des notifications push](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications) pour vous aider à identifier les conflits potentiels avec les dépendances de votre projet.
{% endalert %}

#### Le jeton de l'appareil ne s'enregistre pas auprès de Braze {#troubleshooting-token-registration}

Si le jeton de votre appareil ne s'enregistre pas auprès de Braze, consultez d'abord [Les notifications push ne fonctionnent plus](#troubleshooting-stopped-working).

Si le problème persiste, il est possible qu'une dépendance distincte interfère avec votre configuration de notifications push Braze. Vous pouvez essayer de la supprimer ou appeler manuellement `Braze.registerPushToken` à la place.