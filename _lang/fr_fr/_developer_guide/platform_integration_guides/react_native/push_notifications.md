---
nav_title: Notifications push
article_title: Notifications Push pour React Native
platform: React Native
page_order: 2
toc_headers: h2
description: "Cet article couvre les notifications push sur React Native."
channel: push

---

# Intégration de notifications Push

> Cet article de référence explique comment paramétrer les notifications push pour React Native. L’intégration des notifications push nécessite de configurer séparément chaque plateforme native. Suivez les guides respectifs listés pour terminer l’installation.

## Étape 1 : Terminer la configuration initiale

{% tabs %}
{% tab Expo %}
Définissez les options `enableBrazeIosPush` et `enableFirebaseCloudMessaging` dans votre fichier `app.json` pour activer le push pour iOS et Android, respectivement. Consultez les instructions de configuration [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/#step-2-complete-native-setup) pour plus de détails.

Notez que vous devrez utiliser ces paramètres au lieu des instructions de configuration natives si vous dépendez de bibliothèques de notifications push supplémentaires comme [Expo Notifications.](https://docs.expo.dev/versions/latest/sdk/notifications/)
{% endtab %}

{% tab Android %}
### Étape 1.1 : Enregistrer la notification push

Enregistrez-vous pour les notifications push en utilisant l'API Firebase Cloud Messaging (FCM) de Google. Pour accéder à une présentation complète, reportez-vous aux étapes suivantes du [guide d'intégration des notifications push Native Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/) :

1. [Ajoutez Firebase à votre projet]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Ajoutez Cloud Messaging à vos dépendances]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Créez un compte de service]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Générez des identifiants JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Téléchargez vos informations d'identification JSON sur Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

### Étape 1.2 : Ajouter votre ID d'expéditeur Google

Tout d'abord, accédez à la console Firebase, ouvrez votre projet, puis sélectionnez <i class="fa-solid fa-gear"></i> **Paramètres** > **Paramètres du projet**.

![Le projet Firebase avec le menu Paramètres ouvert.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Sélectionnez **Messagerie Cloud**, puis sous **API Firebase Cloud Messaging (V1)**, copiez l'**ID de l'expéditeur** dans votre presse-papiers.

![La page Messagerie Cloud du projet Firebase avec l'ID de l'expéditeur mis en évidence.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Ensuite, ouvrez le fichier `app.json` de votre projet et attribuez à la propriété `firebaseCloudMessagingSenderId` l'ID de l'expéditeur figurant dans votre presse-papiers. Par exemple :

```
"firebaseCloudMessagingSenderId": "693679403398"
```

### Étape 1.3 : Ajouter le chemin d'accès à votre JSON Google Services

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
{% endtab %}

{% tab iOS %}
### Étape 1.1 : Télécharger les certificats APN

Générez un certificat pour le service de notification push d'Apple (APNs) et téléchargez-le dans le tableau de bord de Braze. Pour accéder à une description complète, voir [Charger votre certificat APN]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

### Étape 1.2 : Choisissez une méthode d'intégration

Si vous n'avez pas l'intention de demander des autorisations de notifications push au lancement de l'application, omettez l'appel `requestAuthorizationWithOptions:completionHandler:` dans votre AppDelegate, puis passez à l'[étape 2](#step-2-request-push-notifications-permission). Sinon, suivez le [guide d'intégration native d'iOS.]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)

Lorsque vous avez terminé, passez à l' [étape 1.3.](#step-13-migrate-your-push-key)

### Étape 1.3 : Migrer votre clé de notifications push

Si vous utilisiez auparavant `expo-notifications` pour gérer votre clé de notification push, exécutez `expo fetch:ios:certs` dans le dossier racine de votre application. Cela téléchargera votre clé de notification push (un fichier .p8), qui peut ensuite être téléchargée sur le tableau de bord de Braze.
{% endtab %}
{% endtabs %}

## Étape 2 : Demander une autorisation de notification push

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

### Étape 2.1 : Écouter les notifications push (facultatif)

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

#### Champs d'événements de la notification push

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
| `is_silent`        | Valeur booléenne   | Si la valeur est `true`, la charge utile est reçue en silence. Pour plus de détails sur l'envoi de notifications push silencieuses sur Android, reportez-vous à la section [Notifications push silencieuses sur Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications). Pour plus de détails sur l'envoi de notifications push silencieuses sur iOS, reportez-vous à la section [Notifications push silencieuses sur iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/). |
| `is_braze_internal`| Valeur booléenne   | Cette adresse sera `true` si une charge utile de notification a été envoyée pour une fonctionnalité interne du SDK, telle que la synchronisation des géorepérages, la synchronisation des indicateurs de fonctionnalités ou le suivi des désinstallations. La charge utile est reçue silencieusement par l'utilisateur. |
| `image_url`        | Chaîne de caractères    | Spécifie l'URL associée à l'image de notification. |
| `braze_properties` | Objet    | Représente les propriétés de Braze associées à la campagne (paires clé-valeur). |
| `ios`              | Objet    | Représente les champs spécifiques à iOS. |
| `android`          | Objet    | Représente les champs spécifiques à Android. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 3 : Activer la création de liens profonds (facultatif)

Pour permettre à Braze de gérer les liens profonds à l'intérieur des composants React lorsqu'une notification push est cliquée, suivez les étapes supplémentaires.

{% tabs %}
{% tab Expo %}
Notre [exemple d'application BrazeProject](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) contient un exemple complet de liens profonds mis en œuvre. Pour en savoir plus sur les liens profonds, consultez notre [article de FAQ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% endtab %}
{% tab Android %}
Pour Android, la création de liens profonds est identique à la [création de liens profonds sur les applications Android natives]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-add-deep-links). Si vous souhaitez que le SDK de Braze gère automatiquement les liens profonds des notifications push, définissez `androidHandlePushDeepLinksAutomatically: true` dans votre `app.json`.

{% endtab %}
{% tab iOS %}
### Étape 3.1 : Ajouter des fonctions de création de liens profonds

Pour iOS, ajoutez `populateInitialUrlFromLaunchOptions` à la méthode `didFinishLaunchingWithOptions` de votre AppDelegate. Par exemple :

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
  [[BrazeReactUtils sharedInstance] populateInitialUrlFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

### Étape 3.2 : Configurer la gestion des liens profonds

Utilisez la méthode `Linking.getInitialURL()` pour les liens profonds qui ouvrent votre application, et la méthode `Braze.getInitialURL` pour les liens profonds à l'intérieur des notifications push qui ouvrent votre application lorsqu'elle n'est pas en cours d'exécution. Par exemple :

```javascript
Linking.getInitialURL()
  .then(url => {
    if (url) {
      console.log('Linking.getInitialURL is ' + url);
      showToast('Linking.getInitialURL is ' + url);
      handleOpenUrl({ url });
    }
  })
  .catch(err => console.error('Error getting initial URL', err));

// Handles deep links when an iOS app is launched from a hard close via push click.
Braze.getInitialURL(url => {
  if (url) {
    console.log('Braze.getInitialURL is ' + url);
    showToast('Braze.getInitialURL is ' + url);
    handleOpenUrl({ url });
  }
});
```
{% alert note %}
Braze fournit cette solution de contournement car l'API de liaison de React Native ne prend pas en charge ce scénario en raison d'une condition de concurrence au démarrage de l'appli.
{% endalert %}
{% endtab %}
{% endtabs %}

## Étape 4 : Tester l’affichage des notifications push

À ce stade, vous devriez pouvoir envoyer des notifications aux appareils. Suivez ces étapes pour tester votre intégration de notification push.

{% alert note %}
À partir de macOS 13, sur certains appareils, vous pouvez tester les notifications push d'iOS sur un simulateur iOS 16+ fonctionnant avec Xcode 14 ou une version plus récente. Pour plus de détails, reportez-vous aux [notes de version de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Définissez un utilisateur actif dans l’application React en appelant la méthode `Braze.changeUserId('your-user-id')`.
2. Allez dans **Campagnes** et créez une nouvelle campagne de notification push. Choisissez les plateformes que vous souhaitez tester.
3. Composez votre notification test et sélectionnez l’onglet **Test**. Ajoutez le même `user-id` que l'utilisateur test et cliquez sur **Envoyer le test**. Vous devriez recevoir rapidement la notification sur votre appareil.

![Une campagne push de Braze montrant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire test pour tester votre notification push.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Transférer les notifications push Android vers un autre FMS

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

## Configurer les extensions d'applications avec Expo

### Activation des notifications push riches pour iOS

{% alert tip %}
Les notifications push riches sont disponibles par défaut pour Android.
{% endalert %}

Pour activer les notifications push enrichies sur iOS à l'aide d'Expo, configurez la propriété `enableBrazeIosRichPush` sur `true` dans votre objet `expo.plugins` dans `app.json` :

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

Enfin, ajoutez l'identifiant du bundle de cette extension d'application à la configuration des informations d'identification de votre projet : `<your-app-bundle-id>.BrazeExpoRichPush`. Pour plus de détails sur ce processus, reportez-vous à la section [Utiliser les extensions d'applications avec Expo Application Services](#app-extensions).

### Activation des contenus push pour iOS

{% alert tip %}
Les contenus push sont disponibles par défaut pour Android.
{% endalert %}

Pour activer les contenus push sur iOS à l'aide d'Expo, assurez-vous qu'un groupe d'applications est défini pour votre application. Pour plus d'informations, voir [Ajouter un groupe d'applications]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

Ensuite, configurez la propriété `enableBrazeIosPushStories` sur `true` et attribuez votre ID de groupe d'applications à `iosPushStoryAppGroup` dans votre objet `expo.plugins` dans `app.json` :

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

Enfin, ajoutez l'identifiant du bundle de cette extension d'application à la configuration des informations d'identification de votre projet : `<your-app-bundle-id>.BrazeExpoPushStories`. Pour plus de détails sur ce processus, reportez-vous à la section [Utiliser les extensions d'applications avec Expo Application Services](#app-extensions).

{% alert warning %}
Si vous utilisez les contenus push avec Expo Application Services, assurez-vous d'utiliser l’indicateur `EXPO_NO_CAPABILITY_SYNC=1` lors de l'exécution de `eas build`. Il existe un problème connu dans la ligne de commande qui supprime la capacité des groupes d'applications du profil de provisionnement de votre extension.
{% endalert %}

### Utiliser les extensions d'applications avec Expo Application Services {#app-extensions}

Si vous utilisez Expo Application Services (EAS) et que vous avez activé `enableBrazeIosRichPush` ou `enableBrazeIosPushStories`, vous devrez déclarer les identifiants de bundle correspondants pour chaque extension d'application dans votre projet. Vous pouvez aborder cette étape de plusieurs manières, selon la façon dont votre projet est configuré pour gérer la signature de code avec EAS.

Une approche consiste à utiliser la configuration `appExtensions` dans votre fichier `app.json` en suivant la [documentation sur les extensions d’applications](https://docs.expo.dev/build-reference/app-extensions/) d’Expo. Vous pouvez également définir le paramètre `multitarget` dans votre fichier `credentials.json` en suivant la [documentation sur les identifiants locaux](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project) d’Expo.

