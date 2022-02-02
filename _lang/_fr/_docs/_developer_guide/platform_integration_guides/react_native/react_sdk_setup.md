---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour React Native
platform: React Natif
page_order: 1
description: "Cette référence introduit le React Native SDK et explique comment l'intégrer nativement sur Android et iOS."
---

# Configuration initiale du SDK

L'installation du Braze React Native SDK fournit des fonctionnalités d'analyse de base et vous permet d'intégrer des messages et des cartes de contenu dans l'application pour iOS et Android avec une seule base de code.

Vous devrez effectuer séparément les étapes d'installation sur les deux plateformes.

Pour terminer l'installation, vous aurez besoin de la clé API [App Identifier]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) ainsi que du [point de terminaison SDK]({{site.baseurl}}/api/basics/#endpoints). Les deux sont situées dans la **Console développeur** sous **Paramètres** dans le tableau de bord.

## Étape 1 : Intégrer la bibliothèque Braze

Ajoutez le paquet Braze React Native SDK.

```bash
npm install react-native-appboy-sdk
# ou en utilisant yarn
# yarn add react-native-appboy-sdk
```

## Étape 2 : Terminer la configuration native

{% tabs %}
{% tab Android %}

#### Étape 2.1a : Ajouter notre dépôt

Dans votre projet de premier niveau `build.gradle`, ajoutez ce qui suit en tant que dépôts dans `tous les projets` -> `dépôts`:

```gradle
allprojects {
  dépôts {
...
    maven { url "https://appboy.github.io/appboy-android-sdk/sdk" }
  }
}
```

#### Étape 2.1b : Configurer le SDK Braze

Pour se connecter aux serveurs de Braze, créez un fichier `braze.xml` dans le dossier `res/values` de votre projet. Collez le code suivant et remplacez la clé API et le point de terminaison par vos valeurs :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">VOTRE_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Ajoutez les permissions requises à votre fichier `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### Étape 2.1c: Implémenter le suivi de la session utilisateur

Les appels à `openSession()` et `closeSession()` sont gérés automatiquement. Ajoute le code suivant à la méthode `onCreate()` de ta classe `MainApplication`:

{% subtabs global %}
{% subtab JAVA %}
```java
importer com.appboy.AppboyLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
...
    registerActivityLifecycleCallbacks(new AppboyLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
importer com.appboy.AppboyLifecycleCallbackListener

surcharger fun onCreate() {
    super.onCreate()
...
    registerActivityLifecycleCallbacks(AppboyLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

#### Étape 2.1: gérer les mises à jour d'intention

Si votre activité principale a `android:launchMode` défini à `singleTask`, ajoutez le code suivant à votre classe `Activité principale`:

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
remplacer le fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

#### Étape 2.2 : Installer les pods

Puisque React Native relie automatiquement les bibliothèques à la plate-forme native, vous pouvez installer le SDK à l'aide de CocoaPods.

À partir du dossier racine du projet :

```bash
cd ios && installation de pod
```

#### Étape 2.2b : Configurer le SDK Braze


Ajouter l'importation Appboy SDK en haut du fichier `AppDelegate.m`:
```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Dans le même fichier, ajoutez le snippet suivant dans la méthode `application:didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"VOTRE APP-IDENTIFIER-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Ensuite, ajoutez votre point de terminaison SDK dans le fichier `Info.plist`. Il est situé dans le dossier du projet `ios`. Si vous travaillez en Xcode :

1. Ajoute une ligne avec le nom `Braze` et le type de `Dictionnaire`.
2. À ce dictionnaire, ajoutez une ligne avec le nom `Endpoint`, type `String` et en tant que valeur, entrez votre point de terminaison [SDK]({{site.baseurl}}/api/basics/#endpoints).

Sinon, ajoutez les éléments suivants au fichier :

```xml
<key>Braze</key>
  <dict>
    <key>Point d'extrémité</key>
    <string>sdk.your-endpoint.com</string>
  </dict>
```

{% endtab %}
{% endtabs %}

## Étape 3 : Utilisation

Une fois installé, vous pouvez `importer` la bibliothèque dans votre code React Native :

```javascript
importer ReactAppboy depuis "react-native-appboy-sdk";
```

## Testez votre intégration de base

À ce stade, vous pouvez vérifier que le SDK est intégré en vérifiant les statistiques de session dans le tableau de bord. Si vous exécutez votre application sur l'une ou l'autre des plateformes, vous devriez voir une nouvelle session dans le tableau de bord (dans la section **Aperçu**).

Vous pouvez ouvrir une session pour un utilisateur en particulier en appelant le code suivant dans votre application.

```javascript
ReactAppboy.changeUser("user-id");
```

Par exemple, vous pouvez assigner l'ID de l'utilisateur au démarrage de l'application :

```javascript
importer React, { useEffect } de "react";
importer ReactAppboy de "react-native-appboy-sdk";

const App = () => {
  useEffect(() => {
    ReactAppboy. hangeUser("une-user-id");
  }, []);

  retour (
    <div>
...
    </div>
  )
```

Vous pouvez ensuite rechercher l'utilisateur avec `une-user-id` dans le tableau de bord sous **Recherche d'utilisateur**. Là, vous pouvez vérifier que les données de session et de périphérique ont été enregistrées.
