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

Le Braze [`.unitypackage`][41] regroupe des liaisons natives pour les plateformes Android et iOS, ainsi qu’une interface C#.

Il existe plusieurs packages Braze Unity disponibles au téléchargement sur la [Page des versions de Braze Unity][42] :
 
- `Appboy.unitypackage`
    - Ce package regroupe les SDK Android et iOS Braze et la dépendance [SDWebImage][unity-1] du SDK iOS, nécessaire pour le fonctionnement approprié des messages in-app de Braze et des fonctionnalités de carte de contenu sur iOS. L’infrastructure SDWebImage est utilisée pour télécharger et afficher des images, y compris des GIF. Si vous avez l’intention d’utiliser la fonctionnalité Braze dans son intégralité, téléchargez et importez ce package.
- `Appboy-nodeps.unitypackage`
    - Ce package est similaire à `Appboy.unitypackage` à l’exception de l’infrastructure [SDWebImage][unity-1] qui n’est pas présente. Ce package est utile si vous ne souhaitez pas que l’infrastructure SDWebImage soit présente dans votre application iOS.

**iOS :** Pour voir si vous avez besoin de la dépendance [SDWebImage][unity-1] pour votre projet iOS, consultez la [Documentation sur les messages in-app iOS][unity-4].<br>
**Android :** À partir d’Unity 2.6.0, l’artefact SDK groupé de Braze Android nécessite les dépendances [AndroidX][unity-3]. Si vous utilisiez auparavant un `jetified unitypackage`, alors vous pouvez effectuer une transition en toute sécurité vers le `unitypackage` correspondant.

## Étape 2 : Importer le package

Dans Unity Editor, importez le package dans votre projet Unity en naviguant vers **Actifs > Importer un package > Personnaliser le package**. Cliquez ensuite sur **Importer**.

Sinon, suivez les instructions pour [Importer un package d’actifs Unity][41] pour un guide plus détaillé sur l’importation des packages Unity personnalisés. 

{% alert note %}
Si vous souhaitez importer le plug-in iOS ou Android uniquement, désélectionnez le sous-répertoire `Plugins/Android` ou `Plugins/iOS` lors de l’importation du Braze `.unitypackage`.
{% endalert %}

## Étape 3 : Mettre à jour votre AndroidManifest.xml

Les projets Android Unity nécessitent un [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) pour exécuter l’application. De plus, Braze nécessite plusieurs ajouts à votre [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) pour fonctionner.

### Configurer le fichier AndroidManifest.xml

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
    <activity android:name="com.appboy.unity.AppboyUnityPlayerActivity" 
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

> Votre `AndroidManifest.xml` doit présent dans `Assets/Plugins/Android/AndroidManifest.xml`. Voir le [Documentation Unity AndroidManifest](https://docs.unity3d.com/Manual/android-manifest.html) pour plus d’informations.

> Toutes les classes d’activités enregistrées dans votre `AndroidManifest.xml` doit être entièrement intégrées au SDK Braze pour Android. Si vous ajoutez votre propre classe d’activités, vous devez suivre les [Instructions d’intégration d’activité Unity](#extending-braze-unity-player) pour vous assurer que l’analyse soit collectée.

{% alert note %}
Votre `AndroidManifest.xml` final ne doit contenir qu’une seule activité avec `"android.intent.category.LAUNCHER"` présent.
{% endalert %}

### Mettre à jour AndroidManifest.xml avec le nom de votre package

Pour trouver le nom de votre package, cliquez sur **Fichier > Créer des paramètres > Paramètres du lecteur > Onglet Android**.
![]({% image_buster /assets/img_archive/UnityPackageName.png %})

Dans votre `AndroidManifest.xml`, toutes les instances de `REPLACE_WITH_YOUR_PACKAGE_NAME` doivent être remplacées par `Package Name` par rapport à l’étape précédente.

## Étape 4 : Ajouter des dépendances gradle {#unity-android-gradle-configuration}

Les dépendances suivantes sont requises :

```groovy
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.5.21"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2"

// Both are required if using the default Content Cards Activity on Android
implementation "androidx.swiperefreshlayout:swiperefreshlayout:+"
implementation "androidx.recyclerview:recyclerview:+"
```

Voici des exemples d’ajout de ces dépendances à l’aide des outils Unity :

##### [Modèle Gradle personnalisé](https://docs.unity3d.com/Manual/android-gradle-overview.html)

```groovy
dependencies {
  implementation "org.jetbrains.kotlin:kotlin-stdlib:1.5.21"
  implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2"
}
```
##### [Responsable de la dépendance externe pour Unity](https://github.com/googlesamples/unity-jar-resolver)

```xml
<dependencies>
  <androidPackages>
    <androidPackage spec="org.jetbrains.kotlin:kotlin-stdlib:1.5.21" />
    <androidPackage spec="org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2" />
  </androidPackages>
</dependencies>
```

## Étape 5 : Configurer le SDK Braze {#unity-static-configuration}

Braze fournit une solution Unity native pour l’automatisation de l’intégration Unity Android. 

1. Dans Unity Editor, ouvrez les paramètres de configuration de Braze en naviguant jusqu’à **Braze > Configuration Braze**.
2. Cochez la case **Automatiser l’intégration d’Unity Android**.
3. Dans le champ « Clé API Braze », saisissez la clé API de votre application présente dans **Gérer les paramètres** sur le tableau de bord de Braze.

{% alert note %}
Cette intégration automatique ne doit pas être utilisée avec un fichier `braze.xml` créé manuellement, car les valeurs de configuration peuvent entrer en conflit pendant le projet. Si vous avez besoin d’un `braze.xml` manuel, désactivez l’intégration automatique.
{% endalert %}

## Intégration SDK de base terminée

Braze devrait maintenant collecter des données depuis votre application et votre intégration de base devrait être terminée. Consultez les articles suivants pour plus d’informations sur l’intégration des notifications push ([Android][53] et [iOS][50]), [Messages in-app][34] et [Cartes de contenu][40].

## Options d’implémentation avancées supplémentaires

### Étendre le moteur Unity de Braze (Android) {#extending-braze-unity-player}

Le fichier `AndroidManifest.xml` (exemple) fourni a une classe d’activité enregistrée, [`AppboyUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e67e09f785adeff075a5d7710e79f41ed3676a6a/android-sdk-unity/src/main/java/com/appboy/unity/AppboyUnityPlayerActivity.java). Cette classe est intégrée au SDK Braze et étend `UnityPlayerActivity` à la gestion des sessions, l’enregistrement des messages in-app, la journalisation des analyses des notifications push et bien plus encore. Voir [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) pour plus d’informations sur l’extension de la classe `UnityPlayerActivity`.

Si vous créez votre propre `UnityPlayerActivity` personnalisé dans une bibliothèque ou un projet de plug-in, vous devrez étendre `AppboyUnityPlayerActivity` de Braze pour intégrer votre fonctionnalité personnalisée à Braze. Avant de commencer à travailler sur l’extension `AppboyUnityPlayerActivity`, suivez nos instructions pour intégrer Braze dans votre projet Unity.
1. Ajoutez le SDK Braze pour Android en tant que dépendance à votre bibliothèque ou à votre projet de plug-in comme décrit dans les [Instructions d’intégration du SDK Braze pour Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).
2. Intégrer notre `.aar` Unity, qui contient la fonctionnalité spécifique Unity de Braze, à votre projet de bibliothèque Android que vous construisez pour Unity. Le `appboy-unity.aar` est disponible à partir de notre [dépôt public](https://github.com/Appboy/appboy-unity-sdk/tree/master/Assets/Plugins/Android). Une fois que notre bibliothèque Unity a été intégrée avec succès, modifiez votre `UnityPlayerActivity` pour étendre `AppboyUnityPlayerActivity`.
3. Exportez votre bibliothèque ou votre projet de plug-in et déposez-le dans `/<your-project>/Assets/Plugins/Android` de manière habituelle. N’incluez pas de code source Braze dans votre bibliothèque ou votre plug-in, car ils seront déjà présents dans `/<your-project>/Assets/Plugins/Android`.
4. Modifier votre `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` pour spécifier votre sous-classe `AppboyUnityPlayerActivity` comme activité principale.

Vous devriez maintenant pouvoir mettre en package un `.apk` depuis l’IDE Unity qui est entièrement intégré à Braze et contient votre fonctionnalité `UnityPlayerActivity` personnalisée.

[5]: #transitioning-from-manual-to-automated-integration
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/news_feed/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[42]: https://github.com/Appboy/appboy-unity-sdk/releases
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/
[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-2]: https://firebase.google.com/docs/unity/setup
[unity-3]: https://developer.android.com/jetpack/androidx
[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/
