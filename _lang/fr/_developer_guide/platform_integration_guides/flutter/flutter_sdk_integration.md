---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Flutter
platform: Flutter
page_order: 1
description: "Cette référence présente le SDK Flutter et explique comment l’intégrer nativement sur Android et iOS."
search_rank: 1
---

# Configuration initiale du SDK

> Cet article de référence explique comment installer le SDK Braze pour Flutter. Suivez ces instructions pour installer le [SDK Braze pour Flutter][1] qui contient un package permettant aux intégrateurs d’utiliser les API Braze dans les [applications Flutter][2] écrites dans Dart.

Ce plug-in offre une fonctionnalité d’analytique de base et vous permet d’intégrer des messages in-app et des cartes de contenu pour iOS et Android à l’aide d’une base de code unique.

{% alert note %}
Vous devrez effectuer les étapes d’installation séparément sur les deux plates-formes.
{% endalert %}

## Conditions préalables

Pour terminer l’installation, vous aurez besoin de la [clé API d’identification de l’application][3] ainsi que de l’[endpoint SDK][4]. Les deux sont situés dans **Manage Settings (Gérer les paramètres)** dans le tableau de bord.

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

Pour vous connecter aux serveurs Braze, créez un fichier `braze.xml` dans le dossier `android/res/values` de votre projet. Collez le code suivant et remplacez la clé d’identification API et l’endpoint par vos valeurs :

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
Ajoutez l’importation SDK Braze en haut du fichier `AppDelegate.swift` :
```swift
import BrazeKit
import braze_plugin
```

Dans le même fichier, créez l’objet de configuration Braze dans la méthode `application(_:didFinishLaunchingWithOptions:)` et remplacez la clé API et le endpoint par les valeurs de votre application. Ensuite, créez l’instance Braze à l’aide de la configuration et créez une propriété statique sur `AppDelegate` pour un accès facile :

```swift
static var braze: Braze? = nil

func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // Setup Braze
  let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>"
  )
  // - Enable logging or customize configuration here
  configuration.logger.level = .info
  let braze = BrazePlugin.initBraze(configuration)
  AppDelegate.braze = braze

  return true
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
Importez `BrazeKit` en haut du fichier `AppDelegate.m` :
```objc
@import BrazeKit;
```

Dans le même fichier, créez l’objet de configuration Braze dans la méthode `application:didFinishLaunchingWithOptions:` et remplacez la clé API et le endpoint par les valeurs de votre application. Ensuite, créez l’instance Braze à l’aide de la configuration et créez une propriété statique sur `AppDelegate` pour un accès facile :

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration =
      [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                      endpoint:@"<BRAZE_ENDPOINT>"];
  // - Enable logging or customize configuration here
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazePlugin initBraze:configuration];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Étape 3 : Utilisation

Pour importer le plug-in dans votre code Dart, utilisez ce qui suit :

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Puis, initialisez une instance du plug-in Braze en appelant `new BrazePlugin()` comme dans [notre exemple d’application][6].

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
