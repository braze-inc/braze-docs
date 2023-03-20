---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 0
description: "Cet article couvre la configuration initiale du SDK iOS, Android et FireOS pour la plate-forme Xamarin."
search_rank: 1
---

# Configuration initiale du SDK

L’installation du SDK Braze vous fournira des fonctionnalités d’analytique de base ainsi que des messages in-app opérationnel avec lesquels vous pouvez engager vos utilisateurs.

## Android

### Étape 1 : Obtenir la liaison Xamarin

Une liaison Xamarin est une manière d’utiliser les bibliothèques natives dans les applications Xamarin. L’implémentation d’une liaison consiste à créer une interface C# avec la bibliothèque, puis à utiliser cette interface dans votre application.  Consultez la [documentation de Xamarin][2].

Il existe deux manières d’inclure la liaison du SDK de Braze :

#### Option 1 : NuGet

La méthode d’intégration la plus simple implique d’obtenir le SDK Braze à partir du référentiel central [Nuget.org][9]. Dans la barre latérale Visual Studio, cliquez avec le bouton droit de la souris le dossier `Packages` et cliquez sur `Add Packages… (Ajouter des packages…)`.  Recherchez « Braze » et installez le package [`AppboyPlatform.AndroidBinding`][13] dans votre projet.

#### Option 2 : Source

La deuxième méthode d’intégration consiste à inclure la [source de liaison][3]. Sous `appboy-component\src\android`, vous trouverez notre code de source de liaison, si vous ajoutez une référence de projet à ```AppboyPlatform.XamarinAndroidBinding.csproj``` dans votre application Xamarin, cela va provoquer la construction de la liaison avec votre projet et vous fournir un accès à Braze Android SDK.

>  Le package NuGet de Braze dépend du package NuGet [`Xamarin.Android.Support.v4`][12].

### Étape 2 : Configurer le SDK Braze en braze.xml
Maintenant que les bibliothèques ont été intégrées, vous devez créer un fichier `braze.xml` dans le dossier `Resources/values` de votre projet. Le contenu de ce fichier devrait ressembler à l’extrait de code suivant :

>  Assurez-vous de remplacer `REPLACE_WITH_YOUR_API_KEY` avec la clé API située dans la page **Developer Console (Console du développeur)** du tableau de bord de Braze.

```java
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
    <string name="com_braze_api_key">REPLACE_WITH_YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
    </resources>
```
Si vous incluez manuellement la source de la liaison, retirez `<item>NUGET</item>` de votre code.

### Étape 3 : Ajouter les autorisations requises au manifeste Android
Maintenant que vous avez ajouté votre clé API, vous devez ajouter les autorisations suivantes à votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

### Étape 4 : Suivre les sessions utilisateur et s’enregistrer pour les messages in-app
Pour activer le suivi de session utilisateur et enregistrer votre application pour les messages in-app, ajoutez l’appel suivant à la méthode de cycle de vie `OnCreate()` de la classe `Application` dans votre application :

```csharp
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```

### Intégration SDK terminée

Vous devriez maintenant pouvoir lancer votre application et voir les sessions s’enregistrer sur le tableau de bord de Braze (ainsi que les informations sur les appareils et autre analytique).  

> Consulter les [instructions d’intégration Android][8] pour une explication approfondie des bonnes pratiques pour l’intégration SDK de base.

## iOS

### Étape 1 : Obtenir la liaison Xamarin

Une liaison Xamarin est une manière d’utiliser les bibliothèques natives dans les applications Xamarin.  L’implémentation d’une liaison consiste à créer une interface C# avec la bibliothèque, puis à utiliser cette interface dans votre application.

Il existe deux manières d’inclure la liaison du SDK de Braze.

#### Option 1 : NuGet

La méthode d’intégration la plus simple implique d’obtenir le SDK Braze à partir du référentiel central [Nuget.org][19]. Dans la barre latérale Visual Studio, cliquez avec le bouton droit de la souris le dossier `Packages` et cliquez sur `Add Packages… (Ajouter des packages…)`.  Recherchez « Braze » et installez le package [`AppboyPlatformXamariniOSBinding`][111] dans votre projet.

#### Option 2 : Source

La deuxième méthode d’intégration consiste à inclure la [source de liaison][113]. Dans [notre dépôt GitHub repo][17], vous trouverez notre code de source de liaison, si vous ajoutez une référence de projet à ```AppboyPlatformXamariniOSBinding.csproj``` dans votre application Xamarin, cela va provoquer la construction de la liaison avec votre projet et vous fournir un accès à Braze Android SDK. Assurez-vous que `AppboyPlatformXamariniOSBinding` apparaît dans le dossier « Référence » de votre projet.

### Étape 2 : Mettez à jour votre délégué d’application et déclarez l’utilisation de Xamarin

Dans votre fichier `AppDelegate.cs`, ajoutez l’extrait de code suivant au sein de votre méthode `FinishedLaunching` :

>  Asssurez-vous de bien mettre à jour `YOUR-API-KEY` à l’aide de la valeur correcte figurant sur la page **Developer Console (Console du développeur)**.

```csharp
// C#
 Appboy.StartWithApiKey ("YOUR-API-KEY", UIApplication.SharedApplication, options);
 Appboy.SharedInstance.SdkFlavor = ABKSDKFlavor.Xamarin;
 Appboy.SharedInstance.AddSdkMetadata(new []{ ABKSdkMetadata.ABKSdkMetadataXamarin, ABKSdkMetadata.ABKSdkMetadataNuGet });
```
Si vous incluez manuellement la source de la liaison, retirez `ABKSdkMetadata.ABKSdkMetadataNuGet` de votre code.

**Exemple d’implémentation**

Consultez le fichier `AppDelegate.cs` dans l’exemple d’application [TestApp.XamariniOS][110].

### Étape 3 : Ajoutez votre endpoint SDK à votre fichier info.plist

Dans votre fichier `Info.plist` ajoutez l’extrait de code suivant :

>  Assurez-vous de mettre à jour `YOUR-SDK-ENDPOINT` avec la valeur correcte de votre page [Settings (Paramètres)][5].

```csharp
// C#
<key>Braze</key>
<dict>
 <key>Endpoint</key>
 <string>YOUR-SDK-ENDPOINT</string>
</dict>
```

Vous pouvez éventuellement inclure l’enregistrement verbeux en ajoutant l’extrait de code suivant :

```csharp
// C#
<key>Braze</key>
<dict>
 <key>LogLevel</key>
 <string>0</string>
 <key>Endpoint</key>
 <string>YOUR-SDK-ENDPOINT</string>
</dict>
```

Notez qu’avant le SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

### Intégration SDK terminée

Braze devrait maintenant collecter des données depuis votre application et votre intégration de base devrait être terminée. Consultez les articles suivants pour activer le [suivi des événements personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events), l’[envoi de messages de notification push]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/push_notifications/) et la suite complète de fonctionnalités Braze.

>  Notre liaison Xamarin publique actuelle pour le SDK pour iOS ne se connecte pas au SDK Facebook pour iOS (liaison des données sociales) et n’inclut pas l’envoi d’IDFA à Braze.

[2]: http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/
[3]: https://github.com/braze-inc/braze-xamarin-sdk
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/
[9]: https://www.nuget.org/
[12]: https://www.nuget.org/packages/Xamarin.Android.Support.v4/
[13]: https://www.nuget.org/packages/AppboyPlatform.AndroidBinding/
[113]: https://github.com/braze-inc/braze-xamarin-sdk
[17]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/ios-unified
[19]: https://www.nuget.org/
[110]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-unified/TestApp.XamariniOS
[111]: https://www.nuget.org/packages/AppboyPlatformXamariniOSBinding/

