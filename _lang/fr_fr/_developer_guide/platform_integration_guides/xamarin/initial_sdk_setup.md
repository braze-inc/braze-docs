---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 0
toc_headers: h2
description: "Cet article couvre la configuration initiale du SDK iOS, Android et FireOS pour la plate-forme Xamarin."
search_rank: 1
---

# Configuration initiale du SDK

> Découvrez comment installer le SDK Braze pour Xamarin. L’installation du SDK Braze vous fournira des fonctionnalités d’analytique de base ainsi que des messages in-app opérationnel avec lesquels vous pouvez engager vos utilisateurs. 

{% alert important %}
À partir de la `version 3.0.0`, ce SDK nécessite l'utilisation de .NET 6+ et supprime la prise en charge des projets utilisant le framework Xamarin.
À partir de la `version 4.0.0`, ce SDK suspend la prise en charge de Xamarin et de Xamarin.Forms et ajoute la prise en charge de .NET MAUI.
Voir [la politique de Microsoft](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin) concernant la fin du support de Xamarin.
{% endalert %}

## Étape 1 : Obtenir la liaison Xamarin

{% tabs %}
{% tab android %}
Une liaison Xamarin est une manière d’utiliser les bibliothèques natives dans les applications Xamarin. L’implémentation d’une liaison consiste à créer une interface C# avec la bibliothèque, puis à utiliser cette interface dans votre application.  Consultez la [documentation de Xamarin](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/). Il existe deux façons d'inclure la liaison du SDK de Braze : en utilisant NuGet ou en compilant à partir de la source.

{% subtabs local %}
{% subtab NuGet %}
La méthode d'intégration la plus simple consiste à obtenir le SDK de Braze à partir du référentiel central [NuGet.org](https://www.nuget.org/). Dans la barre latérale Visual Studio, cliquez avec le bouton droit de la souris le dossier `Packages` et cliquez sur `Add Packages...`.  Recherchez « Braze » et installez le package [`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/) dans votre projet.
{% endsubtab %}

{% subtab Source %}
La deuxième méthode d'intégration consiste à inclure la [source de liaison](https://github.com/braze-inc/braze-xamarin-sdk). Sous [`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding), vous trouverez notre code de source de liaison. Si vous ajoutez une référence de projet à ```BrazeAndroidBinding.csproj``` dans votre application Xamarin, cela entraînera la création de la liaison avec votre projet et vous fournira un accès au SDK Android Braze.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert important %}
Les liaisons iOS pour le SDK Xamarin version 4.0.0 et ultérieures utilisent le [SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk/), tandis que les versions précédentes utilisent l'[ancien SDK AppboyKit](https://github.com/Appboy/Appboy-ios-sdk).
{% endalert %}

Une liaison Xamarin est une manière d’utiliser les bibliothèques natives dans les applications Xamarin.  L’implémentation d’une liaison consiste à créer une interface C# avec la bibliothèque, puis à utiliser cette interface dans votre application. Il existe deux façons d'inclure la liaison du SDK de Braze : en utilisant NuGet ou en compilant à partir de la source.

{% subtabs local %}
{% subtab NuGet %}
La méthode d'intégration la plus simple consiste à obtenir le SDK de Braze à partir du référentiel central [NuGet.org](https://www.nuget.org/). Dans la barre latérale Visual Studio, cliquez avec le bouton droit de la souris le dossier `Packages` et cliquez sur `Add Packages...`.  Recherchez « Braze » et installez les derniers packages NuGet pour Xamarin iOS : [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit), [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)et [Braze.iOS.BrazeLocation]https://www.nuget.org/packages/Braze.iOS.BrazeLocation dans votre projet.

Nous fournissons également les packages de bibliothèques de compatibilité : [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat) et [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat) pour faciliter votre migration vers .NET MAUI.
{% endsubtab %}

{% subtab Source %}
La deuxième méthode d'intégration consiste à inclure la [source de liaison](https://github.com/braze-inc/braze-xamarin-sdk). Sous [`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding), vous trouverez notre code de source de liaison. Si vous ajoutez une référence de projet à ```BrazeiOSBinding.csproj``` dans votre application Xamarin, cela entraînera la création de la liaison avec votre projet et vous fournira un accès au SDK Android Braze. Assurez-vous que `BrazeiOSBinding.csproj` apparaît dans le dossier « Référence » de votre projet.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Étape 2 : Configurez votre instance Braze

{% tabs %}
{% tab android %}
### Étape 2.1 : Configurez le SDK de Braze dans Braze.xml

Maintenant que les bibliothèques ont été intégrées, vous devez créer un fichier `Braze.xml` dans le dossier `Resources/values` de votre projet. Le contenu de ce fichier devrait ressembler à l’extrait de code suivant :

{% alert note %}
Veillez à remplacer `YOUR_API_KEY` par la clé API qui se trouve dans **Paramètres** > **Clés API** dans le tableau de bord de Braze.
<br><br>
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous pouvez trouver les clés API dans la **Console de développement** > **Paramètres API**.
{% endalert %}

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
    <string translatable="false" name="com_braze_api_key">YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
  </resources>
```
Si vous incluez manuellement la source de la liaison, retirez `<item>NUGET</item>` de votre code.

{% alert tip %}
Pour voir un exemple de `Braze.xml`, consultez notre [exemple d'application Android MAUI.](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml)
{% endalert %}

### Étape 2.2 : Ajouter les autorisations requises au manifeste Android

Maintenant que vous avez ajouté votre clé API, vous devez ajouter les autorisations suivantes à votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
Pour obtenir un exemple de votre `AndroidManifest.xml`, voir l'exemple d'application [Android MAUI.](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml)

### Étape 2.3 : Suivre les sessions des utilisateurs et l'enregistrement des messages in-app.

Pour activer le suivi de session utilisateur et enregistrer votre application pour les messages in-app, ajoutez l’appel suivant à la méthode de cycle de vie `OnCreate()` de la classe `Application` dans votre application :

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab ios %}
Lors de la configuration de votre instance Braze, ajoutez l'extrait de code suivant pour configurer votre instance :

{% alert note %}
Veillez à remplacer `YOUR_API_KEY` par la clé API qui se trouve dans **Paramètres** > **Clés API** dans le tableau de bord de Braze.

Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous pouvez trouver les clés API dans la **Console de développement** > **Paramètres API**.
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

Voir le fichier `App.xaml.cs` dans l'exemple d'application [iOS MAUI.](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs) 
{% endtab %}
{% endtabs %}

## Étape 3 : Tester l'intégration

{% tabs %}
{% tab android %}
Vous pouvez désormais lancer votre application et voir les sessions enregistrées dans le tableau de bord de Braze (ainsi que les informations relatives à l'appareil et d'autres analyses/analytiques). Pour obtenir une explication approfondie des bonnes pratiques pour l'intégration SDK de base, consultez les [instructions d'intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).
{% endtab %}

{% tab ios %}
Vous pouvez maintenant lancer votre application et voir les sessions enregistrées dans le tableau de bord de Braze. Pour obtenir une explication approfondie des bonnes pratiques pour l'intégration SDK de base, consultez les [instructions d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/).

{% alert important %}
Notre liaison Xamarin publique actuelle pour le SDK pour iOS ne se connecte pas au SDK Facebook pour iOS (liaison des données sociales) et n’inclut pas l’envoi d’IDFA à Braze.
{% endalert %}
{% endtab %}
{% endtabs %}
