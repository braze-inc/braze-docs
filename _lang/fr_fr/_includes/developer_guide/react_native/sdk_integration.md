## À propos du SDK React native Braze

L'intégration du SDK React native Braze fournit des fonctionnalités d'analyse de base et vous permet d'intégrer des messages in-app et des cartes de contenu pour iOS et Android à partir d'une seule base de code.

## Compatibilité avec la nouvelle architecture

La version minimale suivante du SDK est compatible avec toutes les applications utilisant [la nouvelle architecture de React native](https://reactnative.dev/docs/the-new-architecture/landing-page) :

{% sdk_min_versions reactnative:2.0.1 %}

À partir de la version 6.0.0 du SDK, Braze utilise un module React native Turbo, qui est compatible à la fois avec la nouvelle architecture et l'architecture pont héritée, ce qui signifie qu'aucune configuration supplémentaire n'est nécessaire.

{% alert warning %}
Si votre application iOS est conforme`RCTAppDelegate`et respecte notre configuration `AppDelegate`précédente, veuillez examiner les exemples fournis dans [la section Configuration native complète](#reactnative_step-2-complete-native-setup) afin d'éviter tout plantage lors de l'abonnement à des événements dans le module Turbo.
{% endalert %}

## Intégration du SDK React native

### Conditions préalables

Pour l'intégration du SDK, la version 0.71 ou ultérieure de React native est requise. Pour obtenir la liste complète des versions prises en charge, consultez notre [référentiel GitHub du SDK React Native](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

### Étape 1 : Intégrez la bibliothèque Braze

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

### Étape 2 : Veuillez sélectionner une option de configuration

Vous pouvez gérer le SDK Braze à l'aide du plugin Braze Expo ou via l'une des couches natives. Grâce au plugin Expo, vous pouvez configurer certaines fonctionnalités du SDK sans avoir à écrire de code dans aucune des couches natives. Veuillez sélectionner l'option qui correspond le mieux aux besoins de votre application.

{% tabs %}
{% tab Expo %}
#### Étape 2.1 : Installer le plugin Braze Expo

Assurez-vous que votre version du SDK React Native de Braze correspond au minimum à 1.37.0. Pour obtenir la liste complète des versions prises en charge, veuillez consulter le [référentiel Braze React native](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

Pour installer le plugin Braze Expo, veuillez exécuter la commande suivante :

```bash
npx expo install @braze/expo-plugin
```

#### Étape 2.2 : Ajoutez le plug-in à votre app.json

Dans votre `app.json`, ajoutez le Plugin Braze Expo. Vous pouvez fournir les options de configuration suivantes :

| Méthode                                        | Type    | Description                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | chaîne de caractères  | Obligatoire. La [clé API]({{site.baseurl}}/api/identifier_types/) de votre application Android, située dans votre tableau de bord de Braze sous **Gérer les paramètres**. |
| `iosApiKey`                                   | chaîne de caractères  | Obligatoire. La [clé API]({{site.baseurl}}/api/identifier_types/) de votre application iOS, située dans votre tableau de bord de Braze sous **Gérer les paramètres**.     |
| `baseUrl`                                     | chaîne de caractères  | Obligatoire. Le [endpoint SDK]({{site.baseurl}}/api/basics/#endpoints) de votre application, situé dans votre tableau de bord de Braze sous **Gérer les paramètres**.    |
| `enableBrazeIosPush`                          | booléen | iOS uniquement. Si vous devez utiliser Braze pour gérer les notifications push sur iOS. Introduites dans le SDK React Native v1.38.0 et Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | booléen | Android uniquement. Si vous devez utiliser Firebase Cloud Messaging pour les notifications push. Introduites dans le SDK React Native v1.38.0 et Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | chaîne de caractères  | Android uniquement. Votre ID expéditeur Firebase Cloud Messaging. Introduites dans le SDK React Native v1.38.0 et Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | Entier | Le délai de session Braze pour votre application en secondes.                                                                                               |
| `enableSdkAuthentication`                     | booléen | Détermine si la fonctionnalité [Authentification SDK](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) est activée.      |
| `logLevel`                                    | Entier | Le niveau de journal pour votre application. Le niveau de journalisation par défaut est 8 et enregistre un minimum d'informations. Pour activer la journalisation verbeuse pour le débogage, utilisez le niveau 0 du journal.    |
| `minimumTriggerIntervalInSeconds`             | Entier | Intervalle minimum en secondes entre les déclenchements. 30 secondes par défaut.                                                                           |
| `enableAutomaticLocationCollection`           | booléen | Collecte des données de localisation automatique activée ou non (si l’utilisateur l’autorise).                                                                                  |
| `enableGeofence`                              | booléen | Activation ou non des géorepérages.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | booléen | Demandes de géorepérage automatique ou non.                                                                                                  |
| `dismissModalOnOutsideTap`                    | booléen | iOS uniquement. Si un message in-app est ignoré lorsque l'utilisateur clique en dehors du message in-app.                                           |
| `androidHandlePushDeepLinksAutomatically`     | booléen | Android uniquement. Si le SDK Braze doit gérer automatiquement les liens profonds de notification push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | booléen | Android uniquement. Définit si le contenu textuel d'une notification push doit être interprété et rendu en tant que HTML en utilisant `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | chaîne de caractères  | Android uniquement. Définit la couleur d'accentuation de la notification Android.                                                                                                |
| `androidNotificationLargeIcon`                | chaîne de caractères  | Android uniquement. Définit l'icône large de la notification Android.                                                                                                  |
| `androidNotificationSmallIcon`                | chaîne de caractères  | Android uniquement. Définit l'icône de notification petite d'Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | booléen | iOS uniquement. Détermine si l'utilisateur doit être automatiquement invité à autoriser les notifications push au lancement de l'application.                                                          |
| `enableBrazeIosRichPush`                      | booléen | iOS uniquement. Faut-il activer les fonctionnalités push enrichies pour iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | booléen | iOS uniquement. Activer ou non les histoires push Braze pour iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | chaîne de caractères  | iOS uniquement. Le groupe d'applications utilisé pour les histoires Push iOS.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | booléen | iOS uniquement. Si l'ID de l'appareil utilisera un UUID généré de manière aléatoire.                                                                                       |
| `iosForwardUniversalLinks`                    | booléen | iOS uniquement. Indique si le SDK doit automatiquement reconnaître et transférer les liens universels vers les méthodes système (par défaut : `false`). Lorsque cette option est activée, le SDK transmettra automatiquement les liens universels aux méthodes système définies dans la section [Prise en charge des liens universels dans votre application](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/). Introduit dans React native SDK v11.1.0 et Expo Plugin v3.2.0. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Exemple de configuration :

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
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ],
    ]
  }
}
```

##### Configuration des icônes de notification push Android {#android-push-icons}

Lorsque vous utilisez`androidNotificationLargeIcon`  et `androidNotificationSmallIcon`, veuillez suivre ces bonnes pratiques pour un affichage correct des icônes :

###### Emplacement et format des icônes

Pour utiliser des icônes de notification push personnalisées avec le plugin Braze Expo :

1. Veuillez créer vos fichiers d'icônes conformément aux exigences Android détaillées dans la section [Exigences relatives aux icônes](#icon-requirements).
2. Veuillez les placer dans les répertoires natifs Android de votre projet à l'emplacement`android/app/src/main/res/drawable-<density>/`(par exemple, `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/`, ou similaire).
3. Sinon, si vous gérez des ressources dans votre répertoire React native, vous pouvez utiliser [la configuration des icônesapp.json](https://docs.expo.dev/versions/latest/config/app/#icon) d'Expo ou créer un [plugin de configuration Expo](https://docs.expo.dev/config-plugins/introduction/) pour copier les icônes dans les dossiers Android drawable pendant la précompilation.

Le plugin Braze Expo fait référence à ces icônes à l'aide du système de ressources graphiques d'Android.

###### Exigences relatives aux icônes

- **Petite icône :** Il est nécessaire que ce soit une silhouette blanche sur fond transparent (il s'agit d'une exigence de la plateforme Android).
- **Grande icône :** Peut être une image en couleur
- **Format :** Le format PNG est recommandé.
- **Dénomination :** Veuillez utiliser uniquement des lettres minuscules, des chiffres et des traits de soulignement (par exemple, `my_large_icon.png`)

###### Configuration dans app.json

Veuillez utiliser le`@drawable/`préfixe suivi du nom du fichier _sans_ l'extension. Par exemple, si votre fichier icône est nommé `large_icon.png`, veuillez le référencer comme suit `@drawable/large_icon`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
Veuillez ne pas utiliser de chemins d'accès relatifs (tels que `src/assets/images/icon.png`) ni inclure l'extension de fichier lorsque vous faites référence à des icônes. Le plugin Expo nécessite le`@drawable/`préfixe pour assurer la localisation correcte des icônes dans les dossiers natifs Android après le processus de précompilation.
{% endalert %}

###### Fonctionnement

Le plugin Braze Expo fait référence à vos fichiers icônes à partir des répertoires`drawable` Android. Lorsque vous exécutez `npx expo prebuild`, Expo génère la structure native du projet Android. Vos icônes doivent être présentes dans les dossiers `drawable`Android (placées manuellement ou copiées via un plugin de configuration) avant de créer le programme. Le plugin configure ensuite le SDK Braze pour qu'il utilise ces ressources dessinables par leur nom (sans chemin d'accès ni extension), c'est pourquoi le`@drawable/`préfixe est requis dans votre configuration.

Pour plus d'informations sur les icônes de notification Android, veuillez consulter [les directives relatives aux icônes de notification Android](https://developer.android.com/develop/ui/views/notifications#icon).

#### Étape 2.3 : Créer et exécuter votre application

La précompilation de votre application génère les fichiers natifs nécessaires au fonctionnement du plugin Braze Expo.

```bash
npx expo prebuild
```

Exécutez votre application tel qu’indiqué dans la [documentation Expo](https://docs.expo.dev/workflow/customizing/). Veuillez noter que si vous modifiez les options de configuration, il sera nécessaire de précompiler et de réexécuter l'application.
{% endtab %}

{% tab Android %}

#### Étape 2.1 : Ajouter notre référentiel

Dans votre projet de niveau supérieur `build.gradle`, ajoutez ce qui suit sous `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Cela ajoute Kotlin à votre projet.

#### Étape 2.2 : Configurer le SDK Braze

Pour vous connecter aux serveurs Braze, créez un fichier `braze.xml` dans le dossier `res/values` de votre projet. Collez le code suivant et remplacez la [clé API]({{site.baseurl}}/api/identifier_types/) et le [point de terminaison]({{site.baseurl}}/api/basics/#endpoints) par vos valeurs :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Ajoutez les autorisations requises à votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Avec la version 12.2.0 du SDK de Braze ou une version ultérieure, vous pouvez intégrer automatiquement la bibliothèque android-sdk-location en définissant `importBrazeLocationLibrary=true` dans votre fichier `gradle.properties`.
{% endalert %}

#### Étape 2.3 : Implémentez le suivi de session utilisateur

Les appels vers `openSession()` et `closeSession()` sont gérées automatiquement.
Ajoutez le code suivant à la méthode `onCreate()` de votre classe `MainApplication` :

{% subtabs local %}
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

#### Étape 2.4 : Gérer les mises à jour d’intention

Si votre activité principale a `android:launchMode` défini sur `singleTask`, ajoutez le code suivant à votre classe `MainActivity` :

{% subtabs local %}
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

#### Étape 2.1 : (Facultatif) Configurer le Podfile pour les XCFrameworks dynamiques

Pour importer certaines bibliothèques Braze, telles que BrazeUI, dans un fichier Objective-C++, il est nécessaire d'utiliser la`#import`syntaxe suivante. À partir de la version 7.4.0 du SDK Braze Swift, les binaires ont un [canal de distribution facultatif sous forme de XCFrameworks dynamiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic) qui sont compatibles avec cette syntaxe.

Si vous souhaitez utiliser ce canal de distribution, remplacez manuellement les emplacements des sources CocoaPods dans votre Podfile. Référez-vous à l'exemple ci-dessous et remplacez `{your-version}` par la version pertinente que vous souhaitez importer :

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

#### Étape 2.2 : Installer les pods

Comme React Native lie automatiquement les bibliothèques à la plateforme native, vous pouvez installer le SDK avec l’aide de CocoaPods.

Dans le dossier racine du projet :

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

#### Étape 2.3 : Configurer le SDK Braze

{% subtabs local %}
{% subtab SWIFT %}

Ajoutez le SDK Braze en haut du fichier `AppDelegate.swift` :
```swift
import BrazeKit
import braze_react_native_sdk
```

Dans la méthode `application(_:didFinishLaunchingWithOptions:)`, remplacez la [clé API]({{site.baseurl}}/api/identifier_types/) et le [point de terminaison]({{site.baseurl}}/api/basics/#endpoints) par les valeurs de votre application. Ensuite, créez l’instance Braze à l’aide de la configuration et créez une propriété statique sur `AppDelegate` pour un accès facile :

{% alert note %}
Notre exemple suppose une implémentation de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), qui fournit un certain nombre d'abstractions dans la configuration de React Native. Si vous utilisez une configuration différente pour votre application, assurez-vous d'ajuster votre implémentation en conséquence.
{% endalert %}

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Ajoutez le SDK Braze en haut du fichier `AppDelegate.m` :
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

Dans la méthode `application:didFinishLaunchingWithOptions:`, remplacez la [clé API]({{site.baseurl}}/api/identifier_types/) et le [point de terminaison]({{site.baseurl}}/api/basics/#endpoints) par les valeurs de votre application. Ensuite, créez l’instance Braze à l’aide de la configuration et créez une propriété statique sur `AppDelegate` pour un accès facile :

{% alert note %}
Notre exemple suppose une implémentation de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), qui fournit un certain nombre d'abstractions dans la configuration de React Native. Si vous utilisez une configuration différente pour votre application, assurez-vous d'ajuster votre implémentation en conséquence.
{% endalert %}

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

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

### Étape 3 : Veuillez importer la bibliothèque.

Ensuite, veuillez `import`intégrer la bibliothèque dans votre code React native. Pour plus de détails, veuillez consulter notre [exemple de projet](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject). 

```javascript
import Braze from "@braze/react-native-sdk";
```

### Étape 4 : Veuillez tester l'intégration (facultatif)

Pour tester l'intégration SDK, veuillez démarrer une nouvelle session sur l'une ou l'autre des plateformes pour un utilisateur en appelant le code suivant dans votre application.

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

Dans le tableau de bord de Braze, veuillez accéder à [la section Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search) et recherchez l'utilisateur dont l'ID correspond à `some-user-id`. Ici, vous pouvez vérifier que les données de session et d'appareil ont bien été enregistrées.

## Étapes suivantes

Après l'intégration du SDK Braze, vous pouvez commencer à mettre en œuvre les fonctionnalités d'envoi de messages courantes :

- [Notification push]({{site.baseurl}}/developer_guide/push_notifications/) : Configurez et envoyez des notifications push à vos utilisateurs.
- [Messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/): Affichez des messages contextuels au sein de votre application.
- [Bannières]({{site.baseurl}}/developer_guide/banners/) : Afficher des bannières continuelles dans l'interface de votre application
