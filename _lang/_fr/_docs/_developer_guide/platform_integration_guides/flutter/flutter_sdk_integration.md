---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Flutter
platform: Flution
page_order: 1
description: "Cette référence introduit le Flutter SDK et explique comment l'intégrer nativement sur Android et iOS."
---

# Configuration initiale du SDK

Suivez ces instructions pour installer le [Braze Flutter SDK][1] qui contient un package permettant aux intégrateurs d'utiliser les API Braze dans [applis Flutter][2] écrites en Dart. Ce plugin fournit des fonctionnalités d'analyse de base et vous permet d'intégrer des messages dans l'application et des cartes de contenu pour iOS et Android avec une base de code unique.

{% alert note %}
Vous devrez effectuer séparément les étapes d'installation sur les deux plateformes.
{% endalert %}

## Pré-requis

Pour terminer l'installation, vous aurez besoin de la clé API [App Identifier][3] ainsi que du [point de terminaison SDK][4]. Les deux sont situées dans la **Console développeur** sous **Paramètres** dans le tableau de bord.

Avant de suivre les étapes ci-dessous, veuillez installer et configurer [le Flutter SDK][5].

## Étape 1 : Intégrer la bibliothèque Braze

Ajoutez le paquet Braze Flutter SDK à partir de la ligne de commande.

```bash
flutter pub ajouter braze_plugin
```

Ceci ajoutera la ligne appropriée à votre `pubspec.yaml`.

## Étape 2 : Terminer la configuration native

{% tabs %}
{% tab Android %}

Pour vous connecter aux serveurs Braze, créez un fichier `braze.xml` dans le dossier `android/res/values` de votre projet. Collez le code suivant et remplacez la clé API et le point de terminaison par vos valeurs :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">VOTRE_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">VOTRE_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Ajoutez les permissions requises à votre fichier `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% endtab %}

{% tab iOS %}

{% subtabs global %}
{% subtab SWIFT %}
Ajouter l'importation Appboy SDK en haut du fichier `AppDelegate.swift`:
```swift
Importer Appboy_iOS_SDK
```

Dans le même fichier, ajoutez le snippet suivant dans l'application `(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` méthode :

```swift
Appboy.start(withApiKey: "VOTRE APP-IDENTIFIER-API-KEY", dans:application, withLaunchOptions:launchOptions)
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
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
{% endsubtab %}
{% endsubtabs %}

Ensuite, ajoutez votre point de terminaison SDK dans le fichier `Info.plist`. Il est situé dans le dossier du projet `ios`. Si vous travaillez en Xcode, effectuez les étapes suivantes :

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

Pour importer le plugin dans votre code Dart utilisez ce qui suit :

```dart
Importer 'package:braze_plugin/braze_plugin.dart';
```

Ensuite, initialisez une instance du plugin Braze en appelant `nouveau BrazePlugin()` comme dans [notre exemple d'application][6].

## Testez votre intégration de base

À ce stade, vous pouvez vérifier que le SDK est intégré en vérifiant les statistiques de session dans le tableau de bord. Si vous exécutez votre application sur l'une ou l'autre des plateformes, vous devriez voir une nouvelle session dans le tableau de bord (dans la section **Aperçu**).

Vous pouvez ouvrir une session pour un utilisateur en particulier en appelant le code suivant dans votre application.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("une-user-id");
```

Ensuite, recherchez l'utilisateur avec `un-user-id` dans le tableau de bord sous **Recherche d'utilisateur**. Là, vous pouvez vérifier que les données de session et de périphérique ont été enregistrées.

[1]: https://pub.dev/packages/braze_plugin
[2]: https://flutter.dev/
[3]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[4]: {{site.baseurl}}/api/basics/#endpoints
[5]: https://docs.flutter.dev/get-started/install
[6]: https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart
