---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale SDK pour React Native
platform: React Native
page_order: 1
description: "Cette référence présente le SDK React Native et explique comment l’intégrer nativement sur Android et iOS."

---

# Configuration initiale du SDK

Installer le SDK React Native Braze offre une fonctionnalité d’analytique de base et vous permet d’intégrer des messages in-app et des cartes de contenu pour iOS et Android à l’aide d’une seule codebase.

Vous devrez effectuer les étapes d’installation séparément sur les deux plates-formes.

Pour terminer l’installation, vous aurez besoin de la [clé API d’identification de l’application]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) ainsi que de l’[endpoint SDK]({{site.baseurl}}/api/basics/#endpoints). Les deux sont situés dans **Manage Settings** dans le tableau de bord.

## Étape 1 : Intégrez la bibliothèque Braze

Ajoutez le package SDK React Native Braze.

```bash
npm install react-native-appboy-sdk
# or using yarn
# yarn add react-native-appboy-sdk
```

## Étape 2 : Configuration native complète

{% tabs %}
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

#### Étape 2.2a : Installer les pods

Comme React Native lie automatiquement les bibliothèques à la plateforme native, vous pouvez installer le SDK avec l’aide de CocoaPods.

Dans le dossier racine du projet :

```bash
cd ios && pod install
```

#### Étape 2.2b : Configurer le SDK Braze


Ajouter l’importation SDK Appboy en haut du fichier `AppDelegate.m` :
```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Dans le même fichier, ajoutez l’extrait de code suivant avec la méthode `application:didFinishLaunchingWithOptions` :

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Ajoutez ensuite votre endpoint SDK dans le fichier `Info.plist`. Il se trouve dans le dossier de projet `ios`. Si vous travaillez dans Xcode :

1. Ajoutez une ligne avec le nom `Braze` et le type de `Dictionary`.
2. Pour ce dictionnaire, ajoutez une ligne avec le nom `Endpoint`, type `String` et comme valeur, saisissez votre [endpoint SDK]({{site.baseurl}}/api/basics/#endpoints). 

Sinon, ajoutez les éléments suivants au fichier :

```xml
<key>Braze</key>
  <dict>
    <key>Endpoint</key>
    <string>sdk.your-endpoint.com</string>
  </dict>
```

{% endtab %}
{% endtabs %}

## Étape 3 : Utilisation

Une fois installé, vous pouvez `import` la bibliothèque dans votre code React Native :

```javascript
import ReactAppboy from "react-native-appboy-sdk";
```

## Testez votre intégration de base

À ce stade, vous pouvez vérifier que le SDK est intégré en vérifiant les statistiques de session dans le tableau de bord. Si vous exécutez votre application sur une des deux plateformes, vous devriez voir une nouvelle session dans le tableau de bord (dans la section **Overview**).

Vous pouvez ouvrir une session pour un utilisateur particulier en appelant le code suivant dans votre application.

```javascript
ReactAppboy.changeUser("user-id");
```

Par exemple, vous pouvez attribuer l’ID utilisateur au démarrage de l’application :

```javascript
import React, { useEffect } from "react";
import ReactAppboy from "react-native-appboy-sdk";

const App = () => {
  useEffect(() => {
    ReactAppboy.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

Vous pouvez alors rechercher l’utilisateur avec `some-user-id` dans le tableau de bord sous **User Search** (Recherche d’utilisateur). Vous pouvez y vérifier que les données de session et du périphérique ont été enregistrées.


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/ "Android SDK Install"
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/ "iOS SDK Install"