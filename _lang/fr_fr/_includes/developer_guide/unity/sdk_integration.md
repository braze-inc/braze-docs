## À propos du SDK d'Unity Braze

Pour obtenir la liste complète des types, fonctions, variables et autres, consultez le [fichier de déclaration d'Unity](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs). En outre, si vous avez déjà intégré Unity manuellement pour iOS, vous pouvez [passer à une intégration automatisée](#unity_automated-integration) à la place.

## Intégration du SDK Unity

### Conditions préalables

Avant de commencer, vérifiez que votre environnement est pris en charge par la [dernière version du SDK Braze Unity](https://github.com/braze-inc/braze-unity-sdk/releases).

### Étape 1 : Choisissez votre package Braze Unity

{% tabs %}
{% tab Android %}
Le [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) Braze regroupe des liaisons natives pour les plateformes Android et iOS, ainsi qu’une interface C#.

Plusieurs paquets de Braze Unity peuvent être téléchargés sur la [page des versions de Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases):
 
- `Appboy.unitypackage`
    - Ce package regroupe les SDK Android et iOS Braze et la dépendance [SDWebImage](https://github.com/SDWebImage/SDWebImage) du SDK iOS, nécessaire pour le fonctionnement approprié des messages in-app de Braze et des fonctionnalités de cartes de contenu sur iOS. L’infrastructure SDWebImage est utilisée pour télécharger et afficher des images, y compris des GIF. Si vous avez l’intention d’utiliser la fonctionnalité Braze dans son intégralité, téléchargez et importez ce package.
- `Appboy-nodeps.unitypackage`
    - Ce package est similaire à `Appboy.unitypackage`, à l’exception du framework [SDWebImage](https://github.com/SDWebImage/SDWebImage) qui n’est pas présent. Ce package est utile si vous ne souhaitez pas que l’infrastructure SDWebImage soit présente dans votre application iOS.

{% alert note %}
À partir d’Unity 2.6.0, l’artefact groupé du SDK Braze Android nécessite les dépendances [AndroidX](https://developer.android.com/jetpack/androidx). Si vous utilisiez auparavant un `jetified unitypackage`, alors vous pouvez effectuer une transition en toute sécurité vers le `unitypackage` correspondant.
{% endalert %}
{% endtab %}

{% tab Swift %}
Le [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) Braze regroupe des liaisons natives pour les plateformes Android et iOS, ainsi qu’une interface C#.

Le package Braze Unity est disponible au téléchargement sur la [page des versions de Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases) avec deux options d'intégration :

1. `Appboy.unitypackage` uniquement
  - Ce paquet regroupe les SDK Android et iOS de Braze sans aucune dépendance supplémentaire. Cette méthode d'intégration ne permet pas d’utiliser pleinement l’envoi de messages in-app et les fonctionnalités de cartes de contenu de Braze sur iOS. Si vous avez l'intention d'utiliser toutes les fonctionnalités de Braze sans code personnalisé, utilisez plutôt l'option ci-dessous.
  - Pour utiliser cette option d'intégration, assurez-vous que la case à côté de `Import SDWebImage dependency` est *décochée* dans l'interface utilisateur Unity sous Configuration Braze.
2. `Appboy.unitypackage` avec `SDWebImage`
  - Cette option d'intégration regroupe les SDK Android et iOS de Braze et la dépendance [SDwebimage](https://github.com/SDWebImage/SDWebImage) pour le SDK iOS, qui est nécessaire au bon fonctionnement de la messagerie in-app de Braze, et des fonctionnalités des cartes de contenu sur iOS. Le cadre `SDWebImage` est utilisé pour télécharger et afficher des images, y compris des GIF. Si vous avez l’intention d’utiliser la fonctionnalité Braze dans son intégralité, téléchargez et importez ce package.
  - Pour importer automatiquement `SDWebImage`, veillez à *cocher* la case à côté de `Import SDWebImage dependency` dans l'interface utilisateur Unity sous Configuration Braze.

{% alert note %}
Pour savoir si vous avez besoin de la dépendance [SDWebimage](https://github.com/SDWebImage/SDWebImage) pour votre projet iOS, consultez le site [iOS in-app message documentation]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).
{% endalert %}
{% endtab %}
{% endtabs %}

### Étape 2 : Importer le package

{% tabs %}
{% tab Android %}
Dans Unity Editor, importez le package dans votre projet Unity en sélectionnant **Actifs > Importer un package > Personnaliser le package**. Cliquez ensuite sur **Importer**.

Vous pouvez également suivre les instructions pour [Importer un package d’actifs Unity](https://docs.unity3d.com/Manual/AssetPackages.html) pour accéder à un guide plus détaillé sur l’importation des packages Unity personnalisés. 

{% alert note %}
Si vous souhaitez importer le plug-in iOS ou Android uniquement, désélectionnez le sous-répertoire `Plugins/Android` ou `Plugins/iOS` lors de l’importation du Braze `.unitypackage`.
{% endalert %}
{% endtab %}

{% tab Swift %}
Dans Unity Editor, importez le package dans votre projet Unity en sélectionnant **Actifs > Importer un package > Personnaliser le package**. Cliquez ensuite sur **Importer**.

Vous pouvez également suivre les instructions pour [Importer un package d’actifs Unity](https://docs.unity3d.com/Manual/AssetPackages.html) pour accéder à un guide plus détaillé sur l’importation des packages Unity personnalisés. 

{% alert note %}
Si vous souhaitez importer le plug-in iOS ou Android uniquement, désélectionnez le sous-répertoire `Plugins/Android` ou `Plugins/iOS` lors de l’importation du Braze `.unitypackage`.
{% endalert %}
{% endtab %}
{% endtabs %}

### Étape 3 : Configurer le SDK

{% tabs %}
{% tab Android %}
#### Étape 3.1 : Configurer `AndroidManifest.xml`

Pour remplir [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) de fonctionner. Si votre application n’a pas de `AndroidManifest.xml`, vous pouvez utiliser ce qui suit comme modèle. Sinon, si vous avez déjà un `AndroidManifest.xml`, assurez-vous que l’une des sections manquantes suivantes est ajoutée à votre `AndroidManifest.xml` existant.

1. Allez dans le répertoire `Assets/Plugins/Android/` et ouvrez votre fichier `AndroidManifest.xml`. Il s'agit de l'[emplacement/localisation par défaut dans l'éditeur Unity](https://docs.unity3d.com/Manual/android-manifest.html).
2. Dans votre site `AndroidManifest.xml`, ajoutez les permissions et activités requises dans le modèle suivant.
3. Lorsque vous aurez terminé, votre site `AndroidManifest.xml` ne devrait contenir qu'une seule activité avec `"android.intent.category.LAUNCHER"`.

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

{% alert important %}
Toutes les classes d'activité enregistrées dans votre fichier `AndroidManifest.xml` doivent être pleinement intégrées au SDK Android de Braze, sinon vos analyses/analytiques ne seront pas collectées. Si vous ajoutez votre propre classe d'activité, veillez à [étendre le lecteur Braze Unity](#unity_extend-unity-player) afin d'éviter ce problème.
{% endalert %}

#### Étape 3.2 : Mettez à jour `AndroidManifest.xml` avec le nom de votre paquet

Pour trouver le nom de votre paquet, cliquez sur **Fichier > Paramètres de création > Paramètres du lecteur > Onglet Android.**

![]({% image_buster /assets/img_archive/UnityPackageName.png %})

Dans votre `AndroidManifest.xml`, toutes les instances de `REPLACE_WITH_YOUR_PACKAGE_NAME` doivent être remplacées par `Package Name` par rapport à l’étape précédente.

#### Étape 3.3 : Ajouter les dépendances gradle

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

#### Étape 3.4 : Automatiser l'intégration d'Unity dans Android

Braze fournit une solution Unity native pour l’automatisation de l’intégration Unity Android. 

1. Dans Unity Editor, ouvrez les paramètres de configuration de Braze en sélectionnant **Braze > Configuration Braze**.
2. Cochez la case **Automatiser l'intégration d'Unity Android**.
3. Dans le champ **Clé API Braze**, saisissez la clé API de votre application qui se trouve dans **Gérer les paramètres** depuis le tableau de bord de Braze.

{% alert note %}
Cette intégration automatique ne doit pas être utilisée avec un fichier `braze.xml` créé manuellement, car les valeurs de configuration peuvent entrer en conflit pendant le projet. Si vous avez besoin d’un `braze.xml` manuel, désactivez l’intégration automatique.
{% endalert %}
{% endtab %}

{% tab Swift %}
#### Étape 3.1 : Définir votre clé API

Braze fournit une solution Unity native pour l’automatisation de l’intégration Unity iOS. Cette solution modifie le projet Xcode conçu à l’aide du [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) et des sous-classes `UnityAppController` de Unity avec la macro `IMPL_APP_CONTROLLER_SUBCLASS`.

1. Dans Unity Editor, ouvrez les paramètres de configuration de Braze en sélectionnant **Braze > Configuration Braze**.
2. Cochez la case **Automatiser l'intégration d'Unity iOS**.
3. Dans le champ **Clé API Braze**, saisissez la clé API de votre application qui se trouve dans **Gérer les paramètres.**

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

Si votre application utilise déjà une autre sous-classe `UnityAppController`, vous devrez fusionner votre implémentation de sous-classe avec `AppboyAppDelegate.mm`.
{% endtab %}
{% endtabs %}

## Personnaliser le package Unity

### Étape 1 : Cloner le dépôt

Dans votre terminal, clonez le [dépôt GitHub Braze Unity SDK](https://github.com/braze-inc/braze-unity-sdk), puis naviguez jusqu'à ce dossier :

{% tabs local %}
{% tab MacOS %}
```bash
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd ~/PATH/TO/DIRECTORY/braze-unity-sdk
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd C:\PATH\TO\DIRECTORY\braze-unity-sdk
```
{% endtab %}
{% endtabs %}

### Étape 2 : Exporter un paquet à partir d'un référentiel

Tout d'abord, lancez Unity et laissez-le tourner en arrière-plan. Ensuite, à la racine du référentiel, exécutez la commande suivante pour exporter le paquet vers `braze-unity-sdk/unity-package/`.

{% tabs local %}
{% tab MacOS %}
```bash
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -nographics -projectPath "$(pwd)" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
"%UNITY_PATH%" -batchmode -nographics -projectPath "%PROJECT_ROOT%" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit	
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Si vous rencontrez des problèmes après avoir exécuté ces commandes, consultez [Unity : Arguments de la ligne de commande](https://docs.unity3d.com/2017.2/Documentation/Manual/CommandLineArguments.html).
{% endalert %}

### Étape 3 : Importer le paquet dans Unity

1. Dans Unity, importez le paquet souhaité dans votre projet Unity en naviguant vers **Assets** > **Import Package** > **Custom Package.**
2. S'il y a des fichiers que vous ne voulez pas importer, désélectionnez-les maintenant.
3. Personnalisez le paquet Unity exporté, situé à l'emplacement/localisation `Assets/Editor/Build.cs`.

## Passer à une intégration automatisée (Swift uniquement) {#automated-integration}

Pour profiter de l’intégration automatisée iOS proposée dans le SDK Unity de Braze, suivez ces étapes pour passer d’un mode manuel à une intégration automatisée.

1. Supprimez tous les codes liés à Braze de votre sous-classe `UnityAppController` de projet Xcode.
2. Supprimez les bibliothèques iOS de Braze de votre projet Unity ou Xcode (telles que `Appboy_iOS_SDK.framework` et `SDWebImage.framework`).
3. Importez à nouveau le paquet Braze Unity dans votre projet. Pour une description complète, voir [Étape 2 : Importez le paquet](#unity_step-2-import-the-package).
4. Définissez à nouveau votre clé API. Pour une description complète, voir [Étape 3.1 : Définissez votre clé API](#unity_step-31-set-your-api-key).

## Configurations optionnelles

### Consignation prolixe

Pour activer la journalisation verbeuse dans l'éditeur Unity, procédez comme suit :

1. Ouvrez les paramètres de configuration de Braze en sélectionnant **Braze** > **Configuration de Braze**.
2. Cliquez sur le menu déroulant **Afficher les paramètres Android de Braze**.
3. Dans le champ **Niveau de journalisation du SDK**, saisissez la valeur 0.

### Compatibilité Prime 31

Pour utiliser le plug-in Unity de Braze avec les plug-ins Prime31, modifiez le `AndroidManifest.xml` de votre projet pour utiliser les classes d’activité compatibles Prime31. Modifier toutes les références de
`com.braze.unity.BrazeUnityPlayerActivity` vers `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

### Amazon Device Messaging (ADM)

Braze prend en charge l'intégration d'[ADM push](https://developer.amazon.com/public/apis/engage/device-messaging) dans les applications Unity. Si vous souhaitez intégrer ADM push, créez un fichier appelé `api_key.txt` contenant votre clé API ADM et placez-le dans le dossier `Plugins/Android/assets/`.  Pour plus d'informations sur l'intégration d'ADM avec Braze, consultez nos [instructions d'intégration d'ADM push.]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=unity)

### Extension du lecteur Braze Unity (Android uniquement) {#extend-unity-player}

L'exemple de fichier `AndroidManifest.xml` fourni contient une classe d'activité enregistrée, [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). Cette classe est intégrée au SDK Braze et étend `UnityPlayerActivity` à la gestion des sessions, l’enregistrement des messages in-app, la journalisation des analyses des notifications push et bien plus encore. Voir [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) pour plus d'informations sur l'extension de la classe `UnityPlayerActivity`.

Si vous créez votre propre `UnityPlayerActivity` dans un projet de bibliothèque ou de plugin, vous devrez étendre notre `BrazeUnityPlayerActivity` pour intégrer votre fonctionnalité personnalisée avec Braze. Avant de commencer à travailler sur l’extension `BrazeUnityPlayerActivity`, suivez nos instructions pour intégrer Braze dans votre projet Unity.

1. Ajoutez le SDK Android de Braze en tant que dépendance à votre bibliothèque ou à votre projet de plug-in comme décrit dans les [instructions d'intégration du SDK Android de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).
2. Intégrez notre `.aar` Unity, qui contient notre fonctionnalité spécifique à Unity, à votre projet de bibliothèque Android que vous constituez pour Unity. Le `appboy-unity.aar` est disponible dans notre [dépôt public](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android). Une fois que notre bibliothèque Unity a été intégrée avec succès, modifiez votre `UnityPlayerActivity` pour étendre `BrazeUnityPlayerActivity`.
3. Exportez votre bibliothèque ou votre projet de plug-in et déposez-le dans `/<your-project>/Assets/Plugins/Android` de manière habituelle. N’incluez pas de code source Braze dans votre bibliothèque ou votre plug-in, car ils seront déjà présents dans `/<your-project>/Assets/Plugins/Android`.
4. Modifier votre `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` pour spécifier votre sous-classe `BrazeUnityPlayerActivity` comme activité principale.

Vous devriez maintenant pouvoir mettre en package un `.apk` depuis l’IDE Unity qui est entièrement intégré à Braze et contient votre fonctionnalité `UnityPlayerActivity` personnalisée.

## Résolution des problèmes

### Erreur : "Le fichier n'a pas pu être lu

Les erreurs ressemblant à ce qui suit peuvent être ignorées en toute sécurité. Le logiciel Apple utilise une extension PNG exclusive appelée CgBI, qu’Unity ne reconnaît pas. Ces erreurs n’affecteront ni votre iOS ni l’affichage approprié des images associées dans le paquet Braze.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
