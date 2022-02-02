---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Xamarin
platform:
  - Xamarin
  - iOS
  - Android
page_order: 0
description: "Cet article couvre la configuration initiale iOS, Android et FireOS SDK pour la plate-forme Xamarin."
---

# Configuration initiale du SDK

L'installation du Braze SDK vous fournira des fonctionnalités d'analyse de base ainsi que des messages dans l'application avec lesquels vous pouvez engager vos utilisateurs.

## Android

### Étape 1 : Obtenir la liaison Xamarin

Une liaison Xamarin est un moyen d'utiliser des bibliothèques natives dans les applications Xamarin. L'implémentation d'une liaison consiste à construire une interface C# à la bibliothèque, puis à utiliser cette interface dans votre application.  Voir [la documentation de Xamarin][2].

Il y a deux façons d'inclure la liaison Braze SDK.

#### Option 1 : Nuget

La méthode d'intégration la plus simple consiste à obtenir les Bindings Braze SDK du dépôt central [Nuget.org][9]. Dans la barre latérale Visual Studio, faites un clic droit sur le dossier `Packages` et cliquez sur `Ajouter des Packages...`.  Recherchez 'Braze' et installez le package [`AppboyPlatform.AndroidBinding`][13] dans votre projet.

#### Option 2 : Source

La deuxième méthode d'intégration est d'inclure la source de liaison trouvée [ici][3].  Under `appboy-component\src\android` you will find our binding source code; adding a project reference to the `AppboyPlatform.XamarinAndroidBinding.csproj` in your Xamarin application will cause the binding to be built with your project and provide you access to the Braze Android SDK.

> Le paquet Braze Nuget dépend du paquet [`Xamarin.Android.Support.v4`][12] Nuget .

### Étape 2 : Configurer le Braze SDK dans braze.xml
Maintenant que les bibliothèques ont été intégrées, vous devez créer un fichier `braze.xml` dans le dossier `Ressources/valeurs` de votre projet. Le contenu de ce fichier devrait ressembler à l'extrait de code suivant :

> Assurez-vous de remplacer `REPLACE_WITH_YOUR_API_KEY` par la clé API située sur la page [Paramètres][4] du tableau de bord Braze.

```java
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
    <string name="com_braze_api_key">REPLACE_WITH_YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">VOTRE_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    </resources>
```

### Étape 3 : Ajouter les autorisations requises au manifeste Android
Maintenant que vous avez ajouté votre clé API, vous devez ajouter les permissions suivantes à votre fichier `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

### Étape 4 : Suivi des sessions utilisateur et inscription des messages dans l'application
Pour activer le suivi de session utilisateur et enregistrer votre application pour les messages dans l'application, ajouter l'appel suivant à la méthode `OnCreate()` du cycle de vie de la classe `Application` dans votre application :

```csharp
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```

### Intégration du SDK terminée

Vous devriez maintenant être en mesure de lancer votre application et de voir les sessions enregistrées sur le tableau de bord Braze (ainsi que les informations sur l'appareil et d'autres analyses).

> Consultez les [instructions d'intégration Android][8] pour une discussion plus approfondie sur les meilleures pratiques pour l'intégration de base du SDK.

## iOS

### Étape 1 : Obtenir la liaison Xamarin

Une liaison Xamarin est un moyen d'utiliser des bibliothèques natives dans les applications Xamarin.  L'implémentation d'une liaison consiste à construire une interface C# à la bibliothèque, puis à utiliser cette interface dans votre application.

Il y a deux façons d'inclure la liaison Braze SDK.

#### Option 1 : Nuget

La méthode d'intégration la plus simple consiste à obtenir les Bindings Braze SDK du dépôt central [Nuget.org][19]. Dans la barre latérale Visual Studio, cliquez avec le bouton droit sur le dossier `Packages` et cliquez sur `Ajouter des Packages...`.  Recherchez 'Braze' et installez le paquet [`AppboyPlatformXamariniOSBinding`][111] dans votre projet.

#### Option 2 : Source

La deuxième méthode d'intégration est d'inclure la source de liaison trouvée [ici][113].  Dans [notre dépôt github][17] vous trouverez notre code source de liaison ; en ajoutant une référence de projet à l' `AppboyPlatformXamariniOSBinding. sproj` dans votre application Xamarin entraînera la construction de la liaison avec votre projet et vous donnera accès au SDK iOS Braze. Veuillez vous assurer que `AppboyPlatformXamariniOSBinding` s'affiche dans le dossier « Référence » de votre projet.

### Étape 2 : Mettez à jour votre délégué d'application et déclarez l'utilisation de Xamarin

Dans votre fichier `AppDelegate.cs` , ajoutez le snippet suivant dans votre méthode `FinishedLaunching`:

> Assurez-vous de mettre à jour `VOTRE API-KEY` avec la valeur correcte de votre page \[Settings\]\[5\].

```csharp
// C#
 Appboy.StartWithApiKey ("YOUR-API-KEY", UIApplication.SharedApplication, options);
 Appboy.SharedInstance.SdkFlavor = ABKSDKFlavor.Xamarin;
```

**Exemple d'implémentation**

Voir le fichier `AppDelegate.cs` dans l'échantillon d'application [TestApp.XamariniOS][110].

### Étape 3 : Ajoutez votre point de terminaison SDK à votre fichier info.plist

Dans votre fichier `Info.plist` , ajoutez le snippet suivant :

> Assurez-vous de mettre à jour `VOTRE SDK-ENDPOINT` avec la valeur correcte de votre page \[Settings\]\[5\].

```csharp
// C#
<key>Braze</key>
<dict>
 <key>Point d'extrémité</key>
 <string>VOTRE-SDK-ENDPOINT</string>
</dict>
```

Vous pouvez éventuellement inclure des logs verbeux en incluant le snippet suivant :

```csharp
// C#
<key>Braze</key>
<dict>
 <key>LogLevel</key>
 <string>0</string>
 <key>Point d'extrémité</key>
 <string>VOTRE SDK-ENDPOINT</string>
</dict>
```

Notez qu'avant Braze iOS SDK v4.0.2, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

### Intégration du SDK terminée

Braze devrait maintenant collecter des données de votre application et votre intégration de base devrait être complète. Veuillez consulter les sections suivantes afin d'activer le suivi personnalisé des événements, les messages push, le fil d'actualité et l'ensemble des fonctionnalités de Braze.

> Notre Xamarin actuel de liaison publique pour le SDK iOS ne se connecte pas au SDK Facebook iOS (lien de données sociales) et n'inclut pas l'envoi de l'IDFA à Braze.

[2]: http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/
[3]: https://github.com/Appboy/appboy-xamarin-bindings
[4]: https://dashboard-01.braze.com/app_settings/app_settings/ "Settings"
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/
[9]: https://www.nuget.org/
[12]: https://www.nuget.org/packages/Xamarin.Android.Support.v4/
[13]: https://www.nuget.org/packages/AppboyPlatform.AndroidBinding/
[17]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/src/ios-unified
[110]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples/ios-unified/TestApp.XamariniOS
[111]: https://www.nuget.org/packages/AppboyPlatformXamariniOSBinding/

