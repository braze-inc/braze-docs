## À propos du SDK Flutter Braze

Une fois que vous aurez effectué l'intégration du SDK Braze Flutter sur Android et iOS, vous pourrez utiliser l'API Braze dans vos [applications Flutter](https://flutter.dev/) écrites en Dart. Ce plug-in offre une fonctionnalité d’analytique de base et vous permet d’intégrer des messages in-app et des cartes de contenu pour iOS et Android à l’aide d’une base de code unique.

## Intégration du SDK Flutter

### Conditions préalables

Avant d'effectuer l'intégration du SDK Braze Flutter, veuillez effectuer les opérations suivantes :

| Prérequis | Description |
| --- | --- |
| Identifiant de l'application API Braze | Pour trouver l'identifiant de votre application, veuillez vous rendre dans **Réglages** > **API et identifiants** > **Identifiants d'application**. Pour plus d'informations, veuillez consulter [Types d'identifiants API]({{site.baseurl}}/api/identifier_types/#app-identifier).|
| Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
| SDK Flutter | Veuillez installer le [SDK Flutter](https://docs.flutter.dev/get-started/install) officiel et vous assurer qu'il répond aux exigences de [la version minimale prise en charge](https://github.com/braze-inc/braze-flutter-sdk#requirements) par le SDK Braze Flutter. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 1 : Intégrez la bibliothèque Braze

Ajoutez le kit SDK Braze pour Flutter à partir de la ligne de commande. Cela ajoutera la ligne appropriée à votre `pubspec.yaml`.

```bash
flutter pub add braze_plugin
```

### Étape 2 : Configuration complète du SDK natif

{% tabs %}
{% tab Android %}

Pour vous connecter aux serveurs Braze, créez un fichier `braze.xml` dans le dossier `android/res/values` de votre projet. Collez le code suivant et remplacez la clé d’identification API et l’endpoint par vos valeurs :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
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

override func application(
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

### Étape 3 : Configurez le plugin

Pour importer le plug-in dans votre code Dart, utilisez ce qui suit :

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Ensuite, initialisez une instance du plug-in Braze en appelant `new BrazePlugin()` comme dans [notre exemple d'application](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

{% alert important %}
Afin d'éviter tout comportement indéfini, veuillez allouer et utiliser une seule instance de  `BrazePlugin`dans votre code Dart.
{% endalert %}

## Test de l'intégration

Vous pouvez vérifier que l'intégration SDK est bien réalisée en consultant les statistiques de session dans le tableau de bord. Si vous exécutez votre application sur l'une ou l'autre plateforme, vous devriez voir une nouvelle session dans le tableau de bord (dans la section **Aperçu** ).

Veuillez ouvrir une session pour un utilisateur spécifique en appelant le code suivant dans votre application.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

Veuillez rechercher `{some-user-id}`l'utilisateur dans le tableau de bord sous **Audience** > **Rechercher des utilisateurs**. Vous pouvez y vérifier que les données de session et d’appareil ont été enregistrées.

