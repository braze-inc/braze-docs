---
nav_title: Android
article_title: Intégration SDK Android pour Unity
platform: 
  - Unity
  - Android
page_order: 0
description: "Cet article de référence couvre l’intégration SDK Android pour la plateforme Unity."
search_rank: .9
---

# Intégration SDK Android

> Cet article de référence couvre l’intégration SDK Android pour la plateforme Unity. Suivez ces instructions pour utiliser Braze dans votre application Unity.

## Étape 1 : Choisissez votre package Braze Unity

Le [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) Braze regroupe des liaisons natives pour les plateformes Android et iOS, ainsi qu’une interface C#.

Plusieurs paquets de Braze Unity peuvent être téléchargés sur la [page des versions de Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases):
 
- `Appboy.unitypackage`
    - Ce package regroupe les SDK Android et iOS Braze et la dépendance [SDWebImage](https://github.com/SDWebImage/SDWebImage) du SDK iOS, nécessaire pour le fonctionnement approprié des messages in-app de Braze et des fonctionnalités de cartes de contenu sur iOS. L’infrastructure SDWebImage est utilisée pour télécharger et afficher des images, y compris des GIF. Si vous avez l’intention d’utiliser la fonctionnalité Braze dans son intégralité, téléchargez et importez ce package.
- `Appboy-nodeps.unitypackage`
    - Ce package est similaire à `Appboy.unitypackage`, à l’exception du framework [SDWebImage](https://github.com/SDWebImage/SDWebImage) qui n’est pas présent. Ce package est utile si vous ne souhaitez pas que l’infrastructure SDWebImage soit présente dans votre application iOS.

**iOS**: Pour savoir si vous avez besoin de la dépendance [SDWebimage](https://github.com/SDWebImage/SDWebImage) pour votre projet iOS, consultez le site [iOS in-app message documentation]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/).<br>
**Android**: À partir d’Unity 2.6.0, l’artefact groupé du SDK Braze Android nécessite les dépendances [AndroidX](https://developer.android.com/jetpack/androidx). Si vous utilisiez auparavant un `jetified unitypackage`, alors vous pouvez effectuer une transition en toute sécurité vers le `unitypackage` correspondant.

## Étape 2 : Importer le package

Dans Unity Editor, importez le package dans votre projet Unity en sélectionnant **Actifs > Importer un package > Personnaliser le package**. Cliquez ensuite sur **Importer**.

Vous pouvez également suivre les instructions pour [Importer un package d’actifs Unity](https://docs.unity3d.com/Manual/AssetPackages.html) pour accéder à un guide plus détaillé sur l’importation des packages Unity personnalisés. 

{% alert note %}
Si vous souhaitez importer le plug-in iOS ou Android uniquement, désélectionnez le sous-répertoire `Plugins/Android` ou `Plugins/iOS` lors de l’importation du Braze `.unitypackage`.
{% endalert %}

## Étape 3 : Mise à jour de votre AndroidManifest.xml

Les projets Android Unity nécessitent un [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) pour exécuter l’application. De plus, Braze nécessite plusieurs ajouts à votre [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) pour fonctionner.

### Configurer le AndroidManifest.xml

Si votre application n’a pas de `AndroidManifest.xml`, vous pouvez utiliser ce qui suit comme modèle. Sinon, si vous avez déjà un `AndroidManifest.xml`, assurez-vous que l’une des sections manquantes suivantes est ajoutée à votre `AndroidManifest.xml` existant.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:theme="@style/UnityThemeSelector"
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

> Votre `AndroidManifest.xml` doit présent dans `Assets/Plugins/Android/AndroidManifest.xml`. Consultez la [documentation d'Unity AndroidManifest](https://docs.unity3d.com/Manual/android-manifest.html) pour plus d'informations.

> Toutes les classes d’activités enregistrées dans votre `AndroidManifest.xml` doit être entièrement intégrées au SDK Braze pour Android. Si vous ajoutez votre propre classe d’activités, vous devez suivre les [Instructions d’intégration d’activités Unity](#extending-braze-unity-player) pour vous assurer que les analyses sont collectées.

{% alert note %}
Votre `AndroidManifest.xml` final ne doit contenir qu’une seule activité avec `"android.intent.category.LAUNCHER"` présent.
{% endalert %}

### Mettez à jour le site AndroidManifest.xml avec le nom de votre paquet

Pour trouver le nom de votre paquet, cliquez sur **Fichier > Paramètres de création > Paramètres du lecteur > Onglet Android.**
![]({% image_buster /assets/img_archive/UnityPackageName.png %})

Dans votre `AndroidManifest.xml`, toutes les instances de `REPLACE_WITH_YOUR_PACKAGE_NAME` doivent être remplacées par `Package Name` par rapport à l’étape précédente.

## Étape 4 : Ajouter des dépendances gradle {#unity-android-gradle-configuration}

Pour ajouter des dépendances gradle à votre projet Unity, activez d'abord ["Custom Main Gradle Template"](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) dans vos paramètres de publication. Ceci créera un modèle gradle que votre projet utilisera. Un fichier gradle gère la mise en place des dépendances et d'autres paramètres du projet au moment de la création. Pour plus d'informations, consultez l'exemple d'application Braze Unity à la rubrique [mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle).

Les dépendances suivantes sont requises :

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

Vous pouvez également définir ces dépendances à l'aide du [gestionnaire de dépendances externes.](https://github.com/googlesamples/unity-jar-resolver)

## Étape 5 : Configurer le SDK Braze {#unity-static-configuration}

Braze fournit une solution Unity native pour l’automatisation de l’intégration Unity Android. 

1. Dans Unity Editor, ouvrez les paramètres de configuration de Braze en sélectionnant **Braze > Configuration Braze**.
2. Cochez la case **Automatiser l'intégration d'Unity Android**.
3. Dans le champ **Clé API Braze**, saisissez la clé API de votre application qui se trouve dans **Gérer les paramètres** depuis le tableau de bord de Braze.

{% alert note %}
Cette intégration automatique ne doit pas être utilisée avec un fichier `braze.xml` créé manuellement, car les valeurs de configuration peuvent entrer en conflit pendant le projet. Si vous avez besoin d’un `braze.xml` manuel, désactivez l’intégration automatique.
{% endalert %}

## Intégration SDK de base terminée

Braze devrait maintenant collecter des données depuis votre application et votre intégration de base devrait être terminée. Pour plus d'informations sur l'intégration des notifications push, consultez les articles suivants : [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), les [messages in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/) et les [cartes de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

Pour en savoir plus sur les options d'intégration SDK avancées, consultez la rubrique [Implémentation avancée]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#android-sdk-advanced).

