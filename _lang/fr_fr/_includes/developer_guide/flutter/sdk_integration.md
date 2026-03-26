## À propos du SDK Flutter Braze

Une fois le SDK Braze Flutter intégré sur Android et iOS, vous pourrez utiliser l'API Braze dans vos [applications Flutter](https://flutter.dev/) écrites en Dart. Ce plug-in offre des fonctionnalités d'analyse de base et vous permet d'intégrer des messages in-app et des cartes de contenu pour iOS et Android à l'aide d'une base de code unique.

## Intégration du SDK Flutter

### Conditions préalables

Avant d'intégrer le SDK Braze Flutter, vous devez effectuer les opérations suivantes :

| Prérequis | Description |
| --- | --- |
| Identifiant d'application API Braze | Pour trouver l'identifiant de votre application, rendez-vous dans **Paramètres** > **API et identifiants** > **Identifiants d'application**. Pour plus d'informations, consultez [Types d'identifiants API]({{site.baseurl}}/api/identifier_types/#app-identifier).|
| Endpoint du SDK Braze | L'URL de votre endpoint SDK (par exemple, `sdk.<cluster>.braze.com`). Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
| SDK Flutter | Installez le [SDK Flutter](https://docs.flutter.dev/get-started/install) officiel et assurez-vous qu'il répond aux exigences de [la version minimale prise en charge](https://github.com/braze-inc/braze-flutter-sdk#requirements) par le SDK Braze Flutter. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 1 : Intégrez la bibliothèque Braze

Ajoutez le package du SDK Braze Flutter depuis la ligne de commande. Cela ajoutera la ligne appropriée à votre `pubspec.yaml`.

```bash
flutter pub add braze_plugin
```

### Étape 2 : Configuration complète du SDK natif

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

#### 2.1 Configurer Android

##### Fournir les identifiants à la compilation

Créez un fichier `braze.xml` dans le dossier `android/res/values` de votre projet. La clé API et l'endpoint sont fournis au moment de l'exécution depuis Dart, ils ne sont donc pas requis dans ce fichier. Pour activer l'initialisation différée, ajoutez `com_braze_enable_delayed_initialization` au fichier :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
  <!-- API key and endpoint are not required here. They are set at runtime via Dart. -->
</resources>
```

##### Fournir les identifiants au moment de l'exécution

Vous pouvez également activer l'initialisation différée de manière programmatique dans votre `MainActivity.kt` :

```kotlin
import com.braze.Braze

class MainActivity : FlutterActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    Braze.enableDelayedInitialization(context = this)
  }
}
```

Ajoutez les autorisations requises à votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 Configurer iOS

Dans votre méthode `application(_:didFinishLaunchingWithOptions:)` existante, ajoutez un appel à `BrazePlugin.configure(_:postInitialization:)` pour enregistrer votre configuration. L'instance Braze est créée ultérieurement lorsque `initialize()` est appelé depuis Dart. La clé API et l'endpoint ne sont pas définis ici.

{% subtabs %}
{% subtab SWIFT %}

Ajoutez le code suivant à votre fichier `AppDelegate.swift` :

```swift
import BrazeKit
import braze_plugin

// ...

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // ... your existing didFinishLaunchingWithOptions setup ...

  BrazePlugin.configure(
    { configuration in
      configuration.logger.level = .info
      // Set other non-API-key configurations here, such as:
      // configuration.push.automation = true
      // configuration.sessionTimeout = 60
    },
    postInitialization: { braze in
      // Optional: Customize the Braze instance after creation.
      // For example, set a custom in-app message presenter:
      // let customPresenter = CustomInAppMessagePresenter()
      // braze.inAppMessagePresenter = customPresenter
    }
  )

  return true
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Ajoutez le code suivant à votre fichier `AppDelegate.m` :

```objc
@import BrazeKit;
@import braze_plugin;

// ...

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazePlugin configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    // Set other non-API-key configurations here, such as:
    // configuration.push.automation = ...
    // configuration.sessionTimeout = 60;
  } postInitialization:^(Braze *braze) {
    // Optional: customize the Braze instance after creation.
  }];

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazePlugin.configure()` ne fait qu'enregistrer votre configuration. Aucune instance Braze n'existe tant que `initialize()` n'est pas appelé depuis Dart. N'appelez donc aucune méthode du SDK Braze dans l'AppDelegate après `configure()`.
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

#### 2.1 Configurer Android

Pour vous connecter aux serveurs Braze, créez un fichier `braze.xml` dans le dossier `android/res/values` de votre projet. Collez le code suivant et remplacez la clé API d'identification et l'endpoint par vos valeurs :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Ajoutez les autorisations requises à votre fichier `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 Configurer iOS

{% subtabs %}
{% subtab SWIFT %}
Ajoutez l'importation du SDK Braze en haut du fichier `AppDelegate.swift` :
```swift
import BrazeKit
import braze_plugin
```

Dans le même fichier, créez l'objet de configuration Braze dans la méthode `application(_:didFinishLaunchingWithOptions:)` et remplacez la clé API et l'endpoint par les valeurs de votre application. Ensuite, créez l'instance Braze à l'aide de la configuration et créez une propriété statique sur `AppDelegate` pour y accéder facilement :

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
Importez le SDK Braze en haut du fichier `AppDelegate.m` :
```objc
@import BrazeKit;
@import braze_plugin;
```

Dans le même fichier, créez l'objet de configuration Braze dans la méthode `application:didFinishLaunchingWithOptions:` et remplacez la clé API et l'endpoint par les valeurs de votre application. Ensuite, créez l'instance Braze à l'aide de la configuration et créez une propriété statique sur `AppDelegate` pour y accéder facilement :

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

### Étape 3 : Configurez le plug-in

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Importez le plug-in et créez une instance unique de `BrazePlugin` :

```dart
import 'package:braze_plugin/braze_plugin.dart';

final BrazePlugin braze = BrazePlugin();
```

Appelez ensuite `initialize()` avec votre clé API d'identifiant d'application et votre endpoint SDK pour créer l'instance Braze. Consultez les options ci-dessous pour savoir où appeler cette méthode dans votre application.

#### Initialisation standard

Pour initialiser le SDK au démarrage de votre application, appelez `initialize()` dans `initState()` :

```dart
@override
void initState() {
  super.initState();
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### Initialisation différée

Pour reporter l'initialisation du SDK à un moment ultérieur de la session — par exemple, après que l'utilisateur a donné son consentement ou s'est connecté — appelez `initialize()` lorsque vous êtes prêt :

```dart
// ...
void onUserConsent() {
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

{% alert warning %}
Les notifications push et les liens profonds reçus avant l'appel à `initialize()` ne sont pas traités sur iOS. Sur Android, les liens profonds provenant des notifications push ne sont pas résolus tant que le SDK attend d'être initialisé. Si votre application repose sur les notifications push ou les liens profonds au lancement, utilisez plutôt l'[initialisation standard](#standard-initialization).
{% endalert %}

#### Clés API spécifiques à chaque plateforme

Étant donné que vos applications Android et iOS utilisent des clés API différentes, utilisez la détection de plateforme :

```dart
import 'dart:io' show Platform;

if (Platform.isAndroid) {
  braze.initialize("<ANDROID_API_KEY>", "<BRAZE_ENDPOINT>");
} else if (Platform.isIOS) {
  braze.initialize("<IOS_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### Réinitialisation

Vous pouvez appeler `initialize()` plusieurs fois pour réinitialiser le SDK avec une clé API et un endpoint différents en cours de session. Chaque appel détruit l'instance Braze précédente et en crée une nouvelle.

{% alert important %}
Afin d'éviter tout comportement indéfini, n'allouez et n'utilisez qu'une seule instance de `BrazePlugin` dans votre code Dart. Tous les appels de méthodes du SDK effectués avant `initialize()` sont ignorés sur iOS. Appelez donc `initialize()` avant d'utiliser toute autre méthode Braze.
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Pour importer le plug-in dans votre code Dart, utilisez ce qui suit :

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Ensuite, initialisez une instance du plug-in Braze en appelant `new BrazePlugin()` comme dans [notre exemple d'application](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

{% alert important %}
Afin d'éviter tout comportement indéfini, n'allouez et n'utilisez qu'une seule instance de `BrazePlugin` dans votre code Dart.
{% endalert %}

{% endtab %}
{% endtabs %}

## Test de l'intégration
Vous pouvez vérifier que le SDK est correctement intégré en consultant les statistiques de session dans le tableau de bord. Si vous exécutez votre application sur l'une ou l'autre plateforme, vous devriez voir apparaître une nouvelle session dans le tableau de bord (dans la section **Aperçu**).

Ouvrez une session pour un utilisateur spécifique en appelant le code suivant dans votre application.

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

```dart
BrazePlugin braze = BrazePlugin();
braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% endtabs %}

Recherchez l'utilisateur `{some-user-id}` dans le tableau de bord sous **Audience** > **Rechercher des utilisateurs**. Vous pouvez y vérifier que les données de session et d'appareil ont bien été enregistrées.