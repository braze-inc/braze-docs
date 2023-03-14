---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale SDK pour React Native
platform: React Native
page_order: 1
description: "Cette référence présente le SDK React Native et explique comment l’intégrer nativement sur Android et iOS."
search_rank: 1
---

# Configuration initiale du SDK

Installer le SDK React Native Braze offre une fonctionnalité d’analytique de base et vous permet d’intégrer des messages in-app et des cartes de contenu pour iOS et Android à l’aide d’une seule codebase.

Vous devrez effectuer les étapes d’installation séparément sur les deux plates-formes.

Pour terminer l’installation, vous aurez besoin de la [clé API d’identification de l’application]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) ainsi que de l’[endpoint SDK]({{site.baseurl}}/api/basics/#endpoints). Les deux sont situés dans **Manage Settings** dans le tableau de bord.

## Étape 1 : Intégrez la bibliothèque Braze

{% alert note %}
Braze React Native SDK v1.38.0 et supérieures exigent au minimum React Native v0.64 et supérieures. Le SDK React Native de Braze n’est pas encore compatible avec la nouvelle architecture React Native.
{% endalert %}

{% tabs local %}
{% tab bash %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab fil %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

## Étape 2 : Configuration native complète

{% tabs %}
{% tab Expo %}

#### Étape 2.1 : Installez le plugin Braze Expo

Assurez-vous que votre version de Braze React Native SDK correspond au minimum à 1.37.0. Puis, installer le plugin Braze Expo.

```bash
expo install @braze/expo-plugin
```

#### Étape 2.2 : Ajoutez le plugin à votre app.json

Dans votre `app.json`, ajoutez le Plugin Braze Expo. Vous pouvez fournir les options de configuration suivantes :

| Méthode                                    | Type     | Description                                                                                                                                            |
| ------------------------------------------| ---------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `androidApiKey`                           | chaîne de caractères   |  Obligatoire. La clé API pour votre application Android.                                                                                                   |
| `iosApiKey`                               | chaîne de caractères   |  Obligatoire. La clé API pour votre application iOS.                                                                                                       |
| `baseUrl`                                 | chaîne de caractères   |  Obligatoire. Le [SDK endpoint]({{site.baseurl}}/api/basics/#endpoints) pour votre application.                                                            |
| `enableBrazeIosPush`                      | booléen  |  iOS uniquement. Si vous devez utiliser Braze pour gérer les notifications push sur iOS. Introduites dans React Native SDK v1.38.0 et Expo Plugin v0.4.0.                    |
| `enableFirebaseCloudMessaging`            | booléen  |  Android uniquement. Si vous devez utiliser Firebase Cloud Messaging pour les notifications push. Introduites dans React Native SDK v1.38.0 et Expo Plugin v0.4.0.          |
| `firebaseCloudMessagingSenderId`          | chaîne de caractères   |  Android uniquement. Votre ID expéditeur Firebase Cloud Messaging. Introduites dans React Native SDK v1.38.0 et Expo Plugin v0.4.0.                                 |
| `sessionTimeout`                          | Entier  |  Le délai de session Braze pour votre application en secondes.                                                                                            |
| `enableSdkAuthentication`                 | booléen  |  Activer ou non la fonctionnalité [SDK Authentication](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication).   |
| `logLevel`                                | Entier  |  Le niveau de journal pour votre application. Le niveau de journal par défaut est de 8 et va journaliser le minimum d’informations. Pour activer la journalisation verbeuse pour le débogage, utilisez le niveau 0 du journal. |
| `minimumTriggerIntervalInSeconds`         | Entier  |  Intervalle minimum en secondes entre les déclenchements. 30 secondes par défaut.                                                                        |
| `enableAutomaticLocationCollection`       | booléen  |  Collecte de localisation automatique activée ou non (si l’utilisateur l’autorise).                                                                               |
| `enableGeofence`                          | booléen  |  Activation ou non des geofences.                                                                                                                        |
| `enableAutomaticGeofenceRequests`         | booléen  |  Demandes de geofence automatique ou non.                                                                                               |
| `dismissModalOnOutsideTap`                | booléen  |  iOS uniquement. Le message in-app modal sera rejeté ou non lorsque l’utilisateur clique à l’extérieur du message in-app.                                        |
| `androidHandlePushDeepLinksAutomatically` | booléen  |  Android uniquement. Si le SDK Braze doit gérer automatiquement les liens profonds de notification push.                                                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Configuration exemple :

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
        }
      ],
    ]
  }
}
```

#### Étape 2.3 : Construire et exécuter votre application

La préconstruction de votre application génère les fichiers natifs nécessaires au fonctionnement de Braze SDK.

```bash
expo prebuild
```

Exécutez votre application tel qu’indiqué dans les [Expo docs](https://docs.expo.dev/workflow/customizing/). Veuillez remarquer que les changements des options de configuration vont vous demander de préconstruire et d’exécuter à nouveau l’application.

{% endtab %}
{% tab Android %}

#### Étape 2.1a : Ajouter notre référentiel

Dans votre projet de premier niveau `build.gradle`, ajoutez les éléments suivants comme référentiels dans `allprojects` > `repositories` :

```gradle
allprojects {
  repositories {
    ...
    maven { url "https://appboy.github.io/appboy-android-sdk/sdk" }
  }
}
```

#### Étape 2.1b : Configurer le SDK Braze

Pour vous connecter aux serveurs Braze, créez un fichier `braze.xml` dans le dossier `res/values` de votre projet. Collez le code suivant et remplacez la clé API et l’endpoint par vos valeurs :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Ajoutez les autorisations requises à votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### Étape 2.1c : Implémentez le suivi de session utilisateur

Les appels vers `openSession()` et `closeSession()` sont gérées automatiquement.
Ajoutez le code suivant à la méthode `onCreate()` de votre classe `MainApplication` :

{% subtabs global %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

#### Étape 2.1d : Gérer les mises à jour d’intention

Si votre activité principale a `android:launchMode` défini sur `singleTask`, ajoutez le code suivant à votre classe `MainActivity` :

{% subtabs global %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

#### Étape 2.1 : Installer les pods

Comme React Native lie automatiquement les bibliothèques à la plateforme native, vous pouvez installer le SDK avec l’aide de CocoaPods.

Dans le dossier racine du projet :

```bash
cd ios && pod install
```

#### Étape 2.2 : Configurer le SDK Braze

{% subtabs global %}
{% subtab OBJECTIVE-C %}

Ajoutez le SDK Braze en haut du fichier `AppDelegate.m` :
```objc
@import BrazeKit;
```

Dans la méthode `application:didFinishLaunchingWithOptions:`, remplacez la clé API et l’endpoint par les valeurs de votre application. Ensuite, créez l’instance Braze à l’aide de la configuration et créez une propriété statique sur AppDelegate pour un accès facile : 

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze bridge
  id<RCTBridgeDelegate> moduleInitializer = [[BrazeReactBridge alloc] init];
  RCTBridge *bridge = [[RCTBridge alloc] initWithDelegate:moduleInitializer
                                            launchOptions:launchOptions];
  RCTRootView *rootView = [[RCTRootView alloc] initWithBridge:bridge
                                                   moduleName:@"<YOUR_PROJECT_NAME>"
                                            initialProperties:nil];
  self.bridge = rootView.bridge;

  // Configure views in the application
  self.window = [[UIWindow alloc] initWithFrame:[UIScreen mainScreen].bounds];
  UIViewController *rootViewController = [UIViewController new];
  rootViewController.view = rootView;
  self.window.rootViewController = rootViewController;
  [self.window makeKeyAndVisible];

  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                    endpoint:@"<BRAZE_ENDPOINT>"];
  // - Enable logging and customize the configuration here
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Étape 3 : Utilisation

Une fois installé, vous pouvez `import` la bibliothèque dans votre code React Native :

```javascript
import Braze from "@braze/react-native-sdk";
```

Consultez notre [exemple de projet](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) pour plus d’informations.

## Testez votre intégration de base

À ce stade, vous pouvez vérifier que le SDK est intégré en vérifiant les statistiques de session dans le tableau de bord. Si vous exécutez votre application sur une des deux plateformes, vous devriez voir une nouvelle session dans le tableau de bord (dans la section **Overview**).

Vous pouvez démarrer une session pour un utilisateur particulier en appelant le code suivant dans votre application.

```javascript
Braze.changeUser("userId");
```

Par exemple, vous pouvez attribuer l’ID utilisateur au démarrage de l’application :

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

Vous pouvez alors rechercher l’utilisateur avec `some-user-id` dans le tableau de bord sous [User Search][user-search] (Recherche d’utilisateur). Vous pouvez y vérifier que les données de session et du périphérique ont été enregistrées.


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/ "Android SDK Install"
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/ "iOS SDK Install"
[user-search]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search
