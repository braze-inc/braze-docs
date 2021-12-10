---
nav_title: Android
article_title: Intégration d'Android SDK pour l'unité
platform:
  - Unité
  - Android
page_order: 0
description: "Cet article de référence couvre l'intégration d'Android SDK pour la plate-forme Unity."
---

# Intégration de SDK Android

Suivez les instructions ci-dessous pour faire fonctionner Braze dans votre application Unity. Si vous effectuez une transition depuis une intégration manuelle, veuillez lire les instructions sur [Transitioning From a Manual to an Automated Integration][5].

## Étape 1 : Choisissez votre paquet Braze Unity

Braze [`.unitypackage`][41] regroupe des liaisons natives pour les plates-formes Android et iOS, ainsi qu'une interface C# .

Il y a plusieurs paquets Braze Unity disponibles pour le téléchargement sur la [Page des versions de Braze Unity][42]:

* `Pack Appboy.unity`
    - Ce paquet contient les SDK Braze Android et iOS ainsi que la dépendance [SDWebImage][unity-1] pour le SDK iOS, qui est nécessaire pour la bonne fonctionnalité de la messagerie In-App de Braze, et des cartes de contenu sur iOS. Le framework [SDWebImage][unity-1] est utilisé pour télécharger et afficher des images, y compris des GIFs. Si vous avez l'intention d'utiliser toutes les fonctionnalités de Braze, téléchargez et importez ce paquet.<br>
* `Appboy-nodeps.unitypackage`
    - Ce paquet est similaire à `Appboy.unitypackage` sauf que le framework [SDWebImage][unity-1] n'est pas présent. Ce package est utile si vous ne voulez pas du framework [SDWebImage][unity-1] présent dans votre application iOS. <br><br>

> iOS: Pour voir si vous avez besoin de la dépendance [SDWebImage][unity-1] pour votre projet iOS, veuillez visiter la \[Documentation de Message In-App iOS\]\[unity-4\].<br><br>Android : Depuis Unity 2.6.0, l'artefact fourni par Braze Android SDK nécessite des dépendances  [AndroidX][unity-3] d'AndroidX. Si vous utilisiez précédemment un `paquet d'unité jetifié`, vous pouvez alors passer en toute sécurité au `paquet d'unité correspondant` ci-dessus.

## Étape 2 : Importer le paquet

1. Dans l'éditeur Unity, importez le paquet dans votre projet Unity en naviguant vers `Assets > Importer Paquet > Paquet personnalisé`.
2. Cliquez sur __Importer__.

Sinon, suivez les instructions de l'unité pour [Importation de paquets d'actifs][41] pour un guide plus détaillé sur l'importation de paquets Unity personnalisés.

{% alert note %}
Si vous souhaitez seulement importer le plugin iOS/Android, désélectionnez le sous-répertoire `Plugins/Android`/`Plugins/iOS` lors de l'importation de Braze `. nitypackage`.
{% endalert %}

## Étape 3 : Mise à jour de votre AndroidManifest.xml

Les projets Android Unity nécessitent un [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) pour être présent pour exécuter l'application. De plus, Braze nécessite plusieurs ajouts à votre [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) pour fonctionner.

#### Partie 1 : Configuration du AndroidManifest.xml

Si votre application n'a pas de `AndroidManifest.xml`, vous pouvez utiliser ce qui suit comme modèle. Sinon, si vous avez déjà un `AndroidManifest.xml`, assurez-vous que toutes les sections manquantes ci-dessous sont ajoutées à votre `AndroidManifest.xml` existant.

```xml
<?xml version="1. " encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <! - Applique les méthodes nécessaires à Braze pour s'assurer que les analyses sont collectées et que les notifications push sont transmises correctement à l'application Unity. -->
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

    <! - Un FirebaseMessagingService spécifique à Braze utilisé pour gérer les notifications push. -->
    <service android:name="com.appboy.AppboyFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>

    <!-- BroadcastReceiver used to forward certain Braze push notification events to Unity -->
    <receiver android:name="com.appboy.unity.AppboyUnityPushBroadcastReceiver" android:exported="false" >
      <intent-filter>
        <action android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_PUSH_RECEIVED" />
        <action android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_NOTIFICATION_OPENED" />
        <action android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_PUSH_DELETED" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

> Votre `AndroidManifest.xml` devrait exister sous `Assets/Plugins/Android/AndroidManifest.xml`. Veuillez consulter [la documentation de Unity AndroidManifest](https://docs.unity3d.com/Manual/android-manifest.html) pour plus d'informations.

> Toutes les classes d'activité enregistrées dans votre fichier `AndroidManifest.xml` doivent être entièrement intégrées au SDK Android Braze. Si vous ajoutez votre propre classe d'activité, vous devez suivre les instructions d'intégration de l'activité d'unité [Braze](#extending-braze-unity-player) pour vous assurer que les analyses sont collectées.

{% alert note %}
Votre dernier `AndroidManifest.xml` ne doit contenir qu'une seule activité avec `"android.intent.category.LAUNCHER"` présent.
{% endalert %}

#### Partie 2 : Trouver le nom de votre paquet

- Cliquez sur Fichier -> Paramètres de Build -> Paramètres du lecteur -> Onglet Android ![Nom du paquet Unity]({% image_buster /assets/img_archive/UnityPackageName.png %})

#### Partie 3 : Faire des remplacements dans le Manifest AndroidManifest

Dans votre `AndroidManifest.xml`, toutes les instances de `REPLACE_WITH_YOUR_PACKAGE_NAME` doivent être remplacées par votre `nom de paquet` depuis l'étape précédente.

### Étape 4 : Ajouter des dépendances de gradle {#unity-android-gradle-configuration}

Les dépendances suivantes sont requises :

```groovy
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.5.21"

// Les deux sont nécessaires si vous utilisez l'activité par défaut des Cartes de Contenu sur Android
implémentation "androidx.swiperefreshlayout:swiperefreshlayout:+"
implémentation "androidx.recyclerview:recyclerview:+"
```

Des exemples sur comment ajouter ces dépendances en utilisant les outils Unity sont fournis ci-dessous.

#### Modèle de gradle personnalisé

[Modèle Gradle personnalisé](https://docs.unity3d.com/Manual/android-gradle-overview.html)

```groovy
dépendances {
  implémentation "org.jetbrains.kotlin:kotlin-stdlib:1.5.21"
}
```

#### Gestionnaire de dépendances externes pour l'unité

[Gestionnaire de dépendances externes pour l'unité](https://github.com/googlesamples/unity-jar-resolver)

```xml
<dependencies>
  <androidPackages>
    <androidPackage spec="org.jetbrains.kotlin:kotlin-stdlib:1.5.21" />
  </androidPackages>
</dependencies>
```

### Étape 5 : Configurer le SDK {#unity-static-configuration}

Braze fournit une solution native Unity pour automatiser l'intégration d'Unity Android.

1. Dans l'éditeur d'unité, ouvrez les paramètres de configuration de Braze en naviguant sur Braze > Braze Configuration.
2. Cochez la case "Automate Unity Android Integration".
3. Dans le champ "Braze API Key", entrez la clé API de votre application depuis le tableau de bord Braze.

> Votre clé API Braze se trouve dans la page **Paramètres** du tableau de bord Braze. Pour connaître votre cluster ou votre point de terminaison spécifique, veuillez demander à votre Customer Success Manager ou ouvrir un [ticket de support]({{site.baseurl}}/braze_support).

{% alert note %}
Cette intégration automatique ne doit pas être utilisée en conjonction avec un brasier `créé manuellement. ml` fichier car les valeurs de configuration peuvent entrer en conflit lors de la construction du projet. Si vous avez besoin de l'utilisation d'un manuel `braze.xml`, veuillez désactiver l'intégration automatique.
{% endalert %}

## Intégration de base du SDK terminée

Braze devrait maintenant collecter des données de votre application et votre intégration de base devrait être complète.

- __Push__: Voir la documentation push [Android][53] ou [iOS][50] pour des informations sur l'intégration de push.
- __Messages In-App__: Voir la documentation [Message In-App][34] pour des informations sur l'intégration des messages dans l'application.
- __Cartes de Contenu__: Voir la documentation [Cartes de Contenu][40] pour des informations sur l'intégration des Cartes de Contenu.
- __Flux d'actualités__: Voir la [documentation du flux d'actualité][35] pour des informations sur l'intégration du flux d'actualités.

## Options de mise en œuvre avancées supplémentaires

### Extension du lecteur d'unité de Braze (Android) {#extending-braze-unity-player}

L'exemple `AndroidManifest.xml` fichier fourni a une classe d'activité enregistrée, [`AppboyUnityPlayerActivity`](https://github.com/Appboy/appboy-android-sdk/blob/e67e09f785adeff075a5d7710e79f41ed3676a6a/android-sdk-unity/src/main/java/com/appboy/unity/AppboyUnityPlayerActivity.java). Cette classe est intégrée au Braze SDK et étend `UnityPlayerActivity` à la gestion de sessions, à l'enregistrement de messages dans l'application, à l'enregistrement de l'analyse des notifications push, et plus encore. Voir [cette documentation](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) pour plus d'informations sur l'extension de la classe `UnityPlayerActivity`.

Si vous créez votre propre `UnityPlayerActivity` personnalisé dans une bibliothèque ou un projet de plugin vous devrez étendre l' `AppboyUnityPlayerActivity de Braze` pour intégrer votre fonctionnalité personnalisée avec Braze.

> Avant de commencer à travailler sur l'extension de `AppboyUnityPlayerActivity`, suivez nos instructions pour intégrer Braze dans votre projet Unity.

1. Ajoutez le SDK Android Braze comme dépendance à votre bibliothèque ou projet de plugin comme décrit dans les instructions d'intégration [Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).
2. Intégrez notre Unity `.aar`, qui contient la fonctionnalité spécifique de Braze à votre projet de bibliothèque Android que vous construisez pour Unity. Le `appboy-unity.aar` est disponible sur notre [dépôt public](https://github.com/Appboy/appboy-unity-sdk/tree/master/Assets/Plugins/Android). Une fois notre bibliothèque Unity intégrée, modifiez votre `UnityPlayerActivity` pour étendre `AppboyUnityPlayerActivity`.
3. Exportez votre bibliothèque ou projet de plugin et déposez-le dans `/<your-project>/Assets/Plugins/Android` comme d'habitude. N'incluez pas de code source Braze dans votre bibliothèque ou votre plugin car ils seront déjà présents dans `/<your-project>/Assets/Plugins/Android`.
4. Éditez votre `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` pour spécifier votre `AppboyUnityPlayerActivity` sous-classe comme activité principale.

Vous devriez maintenant pouvoir empaqueter un `. pk` de l'IDE d'unité qui est entièrement intégré à Braze et contient votre fonctionnalité personnalisée `UnityPlayerActivity`.
[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/

[5]: #transitioning-from-manual-to-automated-integration
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/news_feed/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[42]: https://github.com/Appboy/appboy-unity-sdk/releases
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/
[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-3]: https://developer.android.com/jetpack/androidx
