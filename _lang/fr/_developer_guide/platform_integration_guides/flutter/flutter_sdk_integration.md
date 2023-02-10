---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Flutter
platform: Flutter
page_order: 1
description: "Cette référence présente le SDK Flutter et explique comment l’intégrer nativement sur Android et iOS."
search_rank: 1
---

# Configuration initiale du SDK

Suivez ces instructions pour installer le [SDK Braze pour Flutter][1] qui contient un package permettant aux intégrateurs d’utiliser les API Braze dans les [applications Flutter ][2] rédigées dans Dart. Ce plug-in offre une fonctionnalité d’analytique de base et vous permet d’intégrer des messages in-app et des cartes de contenu pour iOS et Android à l’aide d’une base de code unique.

{% alert note %}
Vous devrez effectuer les étapes d’installation séparément sur les deux platesformes.
{% endalert %}

## Conditions préalables

Pour terminer l’installation, vous aurez besoin de la [clé API ][3]d’identification de l’application[ ainsi que de l’endpoint SDK][4]. Les deux sont situés dans **Manage Settings** dans le tableau de bord.

Avant de suivre ces étapes, installez et configurez le [SDK Flutter][5].

## Étape 1 : Intégrez la bibliothèque Braze

Ajoutez le kit SDK Braze pour Flutter à partir de la ligne de commande.

```bash
flutter pub add braze_plugin
```

Cela ajoutera la ligne appropriée à votre `pubspec.yaml`.

## Étape 2 : Configuration native complète

{% tabs %}
{% tab Android %}

Pour vous connecter aux serveurs Braze, créez un fichier `braze.xml` dans le dossier `android/res/values` de votre projet. Collez le code suivant et remplacez la clé d’identification API et le endpoint par vos valeurs :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Ajoutez les autorisations requises à votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% endtab %}
{% tab iOS %}
{% subtabs global %}
{% subtab SWIFT %}
Ajouter l’importation SDK Appboy en haut du fichier `AppDelegate.swift` :
```swift
import Appboy_iOS_SDK
```

Dans le même fichier, ajoutez l’extrait de code suivant dans votre `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> méthode Bool` et remplacer la clé d’identifiant d’API par votre valeur :

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
Ajouter l’importation SDK Appboy en haut du fichier `AppDelegate.m` :
```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Dans le même fichier, ajoutez l’extrait de code suivant dans la méthode `application:didFinishLaunchingWithOptions` et remplacez la clé d’identification API par votre valeur :

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```
{% endsubtab %}
{% endsubtabs %}

Ajoutez ensuite votre endpoint SDK dans le fichier `Info.plist`. Il se trouve dans le dossier de projet `ios`. Si vous travaillez dans Xcode, procédez comme suit :

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

Pour importer le plug-in dans votre code Dart, utilisez ce qui suit :

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Puis, initialisez une instance du plug-in Braze en appelant `new BrazePlugin()` comme dans [notre exemple d’application.][6].

## Testez votre intégration de base

À ce stade, vous pouvez vérifier que le SDK est intégré en vérifiant les statistiques de session dans le tableau de bord. Si vous exécutez votre application sur une des deux plateformes, vous devriez voir une nouvelle session dans le tableau de bord (dans la section **Overview**).

Vous pouvez ouvrir une session pour un utilisateur particulier en appelant le code suivant dans votre application.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

Recherchez ensuite l’utilisateur avec `{some-user-id}` dans le tableau de bord sous **User Search**. Vous pouvez y vérifier que les données de session et d’appareil ont été enregistrées.

[1]: https://pub.dev/packages/braze_plugin
[2]: https://flutter.dev/
[3]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[4]: {{site.baseurl}}/api/basics/#endpoints
[5]: https://docs.flutter.dev/get-started/install
[6]: https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart
