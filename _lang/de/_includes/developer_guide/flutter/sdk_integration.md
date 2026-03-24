## Informationen zum Flutter Braze SDK

Nachdem Sie das Braze Flutter SDK auf Android und iOS integriert haben, können Sie die Braze-API in Ihren mit Dart geschriebenen [Flutter-Apps](https://flutter.dev/) verwenden. Dieses Plugin bietet grundlegende Analytics-Funktionen und ermöglicht die Integration von In-App-Nachrichten und Content-Cards für iOS und Android mit einer einzigen Codebasis.

## Integration des Flutter SDK

### Voraussetzungen

Bevor Sie das Braze Flutter SDK integrieren, müssen Sie Folgendes erledigen:

| Voraussetzung | Beschreibung |
| --- | --- |
| Braze API-App-Bezeichner | Um den Bezeichner Ihrer App zu finden, gehen Sie zu **Einstellungen** > **APIs und Kennungen** > **App-Bezeichner**. Weitere Informationen finden Sie unter [API-Bezeichner-Typen]({{site.baseurl}}/api/identifier_types/#app-identifier).|
| Braze SDK-Endpunkt | Ihre SDK-Endpunkt-URL (z. B. `sdk.<cluster>.braze.com`). Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ab.|
| Flutter SDK | Installieren Sie das offizielle [Flutter SDK](https://docs.flutter.dev/get-started/install) und stellen Sie sicher, dass es die [Mindestanforderungen für die unterstützte Version](https://github.com/braze-inc/braze-flutter-sdk#requirements) des Braze Flutter SDK erfüllt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 1. Schritt: Integrieren der Braze-Bibliothek

Fügen Sie das Braze Flutter SDK-Paket über die Befehlszeile hinzu. Dadurch wird die entsprechende Zeile zu Ihrer `pubspec.yaml` hinzugefügt.

```bash
flutter pub add braze_plugin
```

### 2. Schritt: Vollständige native SDK-Einrichtung

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

#### 2.1 Android einrichten

##### Zugangsdaten zur Kompilierzeit bereitstellen

Erstellen Sie eine `braze.xml`-Datei im Ordner `android/res/values` Ihres Projekts. Der API-Schlüssel und der Endpunkt werden zur Laufzeit über Dart bereitgestellt und sind daher in dieser Datei nicht erforderlich. Um die verzögerte Initialisierung zu aktivieren, fügen Sie `com_braze_enable_delayed_initialization` zur Datei hinzu:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
  <!-- API key and endpoint are not required here. They are set at runtime via Dart. -->
</resources>
```

##### Zugangsdaten zur Laufzeit bereitstellen

Alternativ können Sie die verzögerte Initialisierung programmatisch in Ihrer `MainActivity.kt` aktivieren:

```kotlin
import com.braze.Braze

class MainActivity : FlutterActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    Braze.enableDelayedInitialization(context = this)
  }
}
```

Fügen Sie die erforderlichen Berechtigungen zu Ihrer Datei `AndroidManifest.xml` hinzu:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 iOS einrichten

Fügen Sie innerhalb Ihrer bestehenden `application(_:didFinishLaunchingWithOptions:)`-Methode einen Aufruf von `BrazePlugin.configure(_:postInitialization:)` hinzu, um Ihre Konfiguration zu speichern. Die Braze-Instanz wird erst erstellt, wenn `initialize()` aus Dart aufgerufen wird. Der API-Schlüssel und der Endpunkt werden hier nicht festgelegt.

{% subtabs %}
{% subtab SWIFT %}

Fügen Sie den folgenden Code zu Ihrer `AppDelegate.swift` hinzu:

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

Fügen Sie den folgenden Code zu Ihrer `AppDelegate.m` hinzu:

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
`BrazePlugin.configure()` speichert lediglich Ihre Konfiguration. Es existiert keine Braze-Instanz, bis `initialize()` aus Dart aufgerufen wird. Rufen Sie daher nach `configure()` keine Braze SDK-Methoden im AppDelegate auf.
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

#### 2.1 Android einrichten

Um eine Verbindung zu Braze-Servern herzustellen, erstellen Sie eine `braze.xml`-Datei im Ordner `android/res/values` Ihres Projekts. Fügen Sie den folgenden Code ein und ersetzen Sie den API-Bezeichner-Schlüssel und den Endpunkt durch Ihre Werte:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Fügen Sie die erforderlichen Berechtigungen zu Ihrer Datei `AndroidManifest.xml` hinzu:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 iOS einrichten

{% subtabs %}
{% subtab SWIFT %}
Fügen Sie die Braze SDK-Importe am Anfang der Datei `AppDelegate.swift` ein:
```swift
import BrazeKit
import braze_plugin
```

Erstellen Sie in derselben Datei das Braze-Konfigurationsobjekt in der `application(_:didFinishLaunchingWithOptions:)`-Methode und ersetzen Sie den API-Schlüssel und den Endpunkt durch die Werte Ihrer App. Erstellen Sie dann die Braze-Instanz mit Hilfe der Konfiguration und legen Sie eine statische Eigenschaft auf `AppDelegate` an, um den Zugriff zu erleichtern:

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
Importieren Sie das Braze SDK am Anfang der Datei `AppDelegate.m`:
```objc
@import BrazeKit;
@import braze_plugin;
```

Erstellen Sie in derselben Datei das Braze-Konfigurationsobjekt in der `application:didFinishLaunchingWithOptions:`-Methode und ersetzen Sie den API-Schlüssel und den Endpunkt durch die Werte Ihrer App. Erstellen Sie dann die Braze-Instanz mit Hilfe der Konfiguration und legen Sie eine statische Eigenschaft auf `AppDelegate` an, um den Zugriff zu erleichtern:

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

### 3. Schritt: Plugin einrichten

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Importieren Sie das Plugin und erstellen Sie eine einzelne Instanz von `BrazePlugin`:

```dart
import 'package:braze_plugin/braze_plugin.dart';

final BrazePlugin braze = BrazePlugin();
```

Rufen Sie dann `initialize()` mit Ihrem App-Bezeichner-API-Schlüssel und SDK-Endpunkt auf, um die Braze-Instanz zu erstellen. Nachfolgend finden Sie die Optionen, wo Sie diese Methode in Ihrer App aufrufen können.

#### Standard-Initialisierung

Um das SDK beim Start Ihrer App zu initialisieren, rufen Sie `initialize()` in `initState()` auf:

```dart
@override
void initState() {
  super.initState();
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### Verzögerte Initialisierung

Um die SDK-Initialisierung auf einen späteren Zeitpunkt in der Sitzung zu verschieben – z. B. nachdem die Nutzer:innen ihre Einwilligung erteilt oder die Anmeldung abgeschlossen haben – rufen Sie `initialize()` auf, wenn Sie bereit sind:

```dart
// ...
void onUserConsent() {
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

{% alert warning %}
Push-Benachrichtigungen und Deeplinks, die vor dem Aufruf von `initialize()` empfangen werden, werden unter iOS nicht verarbeitet. Unter Android werden Deeplinks aus Push-Benachrichtigungen nicht aufgelöst, solange das SDK auf die Initialisierung wartet. Wenn Ihre App auf Push-Benachrichtigungen oder Deeplinks beim Start angewiesen ist, verwenden Sie stattdessen die [Standard-Initialisierung](#standard-initialization).
{% endalert %}

#### Plattformspezifische API-Schlüssel

Da Ihre Android- und iOS-Apps unterschiedliche API-Schlüssel verwenden, nutzen Sie die Plattformerkennung:

```dart
import 'dart:io' show Platform;

if (Platform.isAndroid) {
  braze.initialize("<ANDROID_API_KEY>", "<BRAZE_ENDPOINT>");
} else if (Platform.isIOS) {
  braze.initialize("<IOS_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### Erneute Initialisierung

Sie können `initialize()` mehrfach aufrufen, um das SDK während einer Sitzung mit einem anderen API-Schlüssel und Endpunkt neu zu initialisieren. Jeder Aufruf entfernt die vorherige Braze-Instanz und erstellt eine neue.

{% alert important %}
Um undefiniertes Verhalten zu vermeiden, weisen Sie in Ihrem Dart-Code nur eine einzige Instanz von `BrazePlugin` zu und verwenden Sie auch nur diese. Alle SDK-Methodenaufrufe, die vor `initialize()` erfolgen, werden unter iOS ignoriert. Rufen Sie daher `initialize()` auf, bevor Sie andere Braze-Methoden verwenden.
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Um das Plugin in Ihren Dart-Code zu importieren, verwenden Sie Folgendes:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Initialisieren Sie dann eine Instanz des Braze-Plugins, indem Sie `new BrazePlugin()` aufrufen, wie in [unserer Beispiel-App](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) gezeigt.

{% alert important %}
Um undefiniertes Verhalten zu vermeiden, weisen Sie in Ihrem Dart-Code nur eine einzige Instanz von `BrazePlugin` zu und verwenden Sie auch nur diese.
{% endalert %}

{% endtab %}
{% endtabs %}

## Testen der Integration
Sie können überprüfen, ob das SDK integriert ist, indem Sie die Sitzungsstatistiken im Dashboard prüfen. Wenn Sie Ihre Anwendung auf einer der beiden Plattformen ausführen, sollten Sie im Dashboard (im Abschnitt **Übersicht**) eine neue Sitzung sehen.

Öffnen Sie eine Sitzung für eine:n bestimmte:n Nutzer:in, indem Sie den folgenden Code in Ihrer App aufrufen.

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

Suchen Sie die Nutzer:in mit `{some-user-id}` im Dashboard unter **Zielgruppe** > **Nutzer:innen suchen**. Dort können Sie überprüfen, ob Sitzungs- und Gerätedaten protokolliert wurden.