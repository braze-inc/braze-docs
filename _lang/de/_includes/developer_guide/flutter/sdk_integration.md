## Über das Flutter Braze SDK

Nachdem Sie das Braze Flutter SDK auf Android und iOS integriert haben, können Sie die Braze API in Ihren in Dart geschriebenen [Flutter Apps](https://flutter.dev/) verwenden. Dieses Plugin bietet grundlegende Analytics-Funktionen und ermöglicht Ihnen die Integration von In-App-Nachrichten und Content-Cards sowohl für iOS als auch für Android mit einer einzigen Codebasis.

## Integration des Flutter SDK

### Voraussetzungen

Bevor Sie das Braze Flutter SDK integrieren, müssen Sie die folgenden Schritte durchführen:

| Voraussetzung | Beschreibung |
| --- | --- |
| Braze API App Bezeichner | Um den Bezeichner Ihrer App zu finden, gehen Sie zu **Einstellungen** > **APIs und Bezeichner** > App-Bezeichner. Weitere Informationen finden Sie unter, [API Bezeichner-Typen]({{site.baseurl}}/api/identifier_types/#app-identifier).|
| Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ab.|
| Flutter SDK | Installieren Sie das offizielle [Flutter SDK](https://docs.flutter.dev/get-started/install) und stellen Sie sicher, dass es der vom Braze Flutter SDK [unterstützten Mindestversion](https://github.com/braze-inc/braze-flutter-sdk#requirements) entspricht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 1: Integrieren der Braze-Bibliothek

Fügen Sie das Braze Flutter SDK-Paket über die Befehlszeile hinzu. Dadurch wird die entsprechende Zeile zu Ihrer `pubspec.yaml` hinzugefügt.

```bash
flutter pub add braze_plugin
```

### Schritt 2: Vollständige Einrichtung des nativen SDK

{% tabs %}
{% tab Android %}

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

{% endtab %}
{% tab iOS %}
{% subtabs global %}
{% subtab SWIFT %}
Fügen Sie den Braze SDK-Import am Anfang der Datei `AppDelegate.swift` ein:
```swift
import BrazeKit
import braze_plugin
```

Erstellen Sie in derselben Datei das Konfigurationsobjekt von Braze in der Methode `application(_:didFinishLaunchingWithOptions:)` und ersetzen Sie den API-Schlüssel und den Endpunkt durch die Werte Ihrer App. Erstellen Sie dann die Braze-Instanz mit Hilfe der Konfiguration und legen Sie eine statische Eigenschaft auf `AppDelegate` an, um den Zugriff zu erleichtern:

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
Importieren Sie `BrazeKit` am Anfang der Datei `AppDelegate.m`:
```objc
@import BrazeKit;
```

Erstellen Sie in derselben Datei das Konfigurationsobjekt von Braze in der Methode `application:didFinishLaunchingWithOptions:` und ersetzen Sie den API-Schlüssel und den Endpunkt durch die Werte Ihrer App. Erstellen Sie dann die Braze-Instanz mit Hilfe der Konfiguration und legen Sie eine statische Eigenschaft auf `AppDelegate` an, um den Zugriff zu erleichtern:

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

### Schritt 3: Das Plugin einrichten

Um das Plugin in Ihren Dart Code zu importieren, gehen Sie wie folgt vor:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Dann initialisieren Sie eine Instanz des Braze-Plugins, indem Sie `new BrazePlugin()` aufrufen, wie in [unserer Beispiel-App](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) gezeigt.

{% alert important %}
Um undefiniertes Verhalten zu vermeiden, sollten Sie in Ihrem Dart Code nur eine einzige Instanz von `BrazePlugin` zuweisen und verwenden.
{% endalert %}

## Testen der Integration

Sie können überprüfen, ob das SDK integriert ist, indem Sie die Sitzungsstatistiken im Dashboard überprüfen. Wenn Sie Ihre Anwendung auf einer der beiden Plattformen ausführen, sollten Sie im Dashboard (im Bereich **Übersicht** ) eine neue Sitzung sehen.

Öffnen Sie eine Sitzung für einen bestimmten Nutzer:innen, indem Sie den folgenden Code in Ihrer App aufrufen.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

Suchen Sie im Dashboard unter **Zielgruppe** > Nutzer:innen suchen nach dem Nutzer:innen mit `{some-user-id}`. Dort können Sie überprüfen, ob Sitzungs- und Gerätedaten protokolliert worden sind.

