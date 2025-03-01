---
nav_title: SDK-Ersteinrichtung
article_title: SDK-Ersteinrichtung für Flutter
platform: Flutter
page_order: 1
description: "Diese Referenz stellt das Flutter SDK vor und erklärt, wie Sie es nativ auf Android und iOS integrieren können."
search_rank: 1
---

# SDK-Ersteinrichtung

> Dieser Referenzartikel beschreibt, wie Sie das Braze SDK für Flutter installieren. Folgen Sie diesen Anweisungen, um das [Braze Flutter SDK](https://pub.dev/packages/braze_plugin) zu installieren, das ein Paket enthält, das es Integratoren erlaubt, Braze APIs in [Flutter Apps](https://flutter.dev/) zu verwenden, die in Dart geschrieben wurden.

Dieses Plugin bietet grundlegende Analytics-Funktionen und ermöglicht Ihnen die Integration von In-App-Nachrichten und Content-Cards sowohl für iOS als auch für Android mit einer einzigen Codebasis.

{% alert note %}
Sie müssen die Installationsschritte auf beiden Plattformen separat durchführen.
{% endalert %}

## Voraussetzungen

Um die Installation abzuschließen, benötigen Sie den [API-Schlüssel für den App-Bezeichner]({{site.baseurl}}/api/identifier_types/) sowie den [SDK-Endpunkt]({{site.baseurl}}/api/basics/#endpoints). Beide befinden sich unter **Einstellungen verwalten** auf dem Dashboard.

Bevor Sie diese Schritte ausführen, installieren Sie das [Flutter SDK](https://docs.flutter.dev/get-started/install) und richten es ein. Stellen Sie sicher, dass auf Ihrem Rechner und in Ihrem Projekt die [hier angegebenen](https://github.com/braze-inc/braze-flutter-sdk#readme) Mindestversionen von Flutter und Dart installiert sind.

## Schritt 1: Integrieren der Braze-Bibliothek

Fügen Sie das Braze Flutter SDK-Paket über die Befehlszeile hinzu.

```bash
flutter pub add braze_plugin
```

Dadurch wird die entsprechende Zeile zu Ihrer `pubspec.yaml` hinzugefügt.

## Schritt 2: Vollständige native Einrichtung

{% tabs %}
{% tab Android %}

Um eine Verbindung zu Braze-Servern herzustellen, erstellen Sie eine `braze.xml`-Datei im Ordner `android/res/values` Ihres Projekts. Fügen Sie den folgenden Code ein und ersetzen Sie den API-Bezeichner-Schlüssel und den Endpunkt durch Ihre Werte:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
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

## Schritt 3: Nutzung

Um das Plugin in Ihren Dart Code zu importieren, gehen Sie wie folgt vor:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Dann initialisieren Sie eine Instanz des Braze-Plugins, indem Sie `new BrazePlugin()` aufrufen, wie in [unserer Beispiel-App](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) gezeigt.

## Testen Sie Ihre grundlegende Integration

An diesem Punkt können Sie überprüfen, ob das SDK integriert ist, indem Sie die Sitzungsstatistiken im Dashboard überprüfen. Wenn Sie Ihre Anwendung auf einer der beiden Plattformen ausführen, sollten Sie im Dashboard (im Bereich **Übersicht** ) eine neue Sitzung sehen.

Sie können eine Sitzung für einen bestimmten Nutzer öffnen, indem Sie den folgenden Code in Ihrer App aufrufen.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

Suchen Sie dann im Dashboard unter **Zielgruppe** > Nutzer:innen suchen nach dem Nutzer:in mit `{some-user-id}`. Dort können Sie überprüfen, ob Sitzungs- und Gerätedaten protokolliert worden sind.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie unter **Nutzer**:innen > Nutzersuche nach Nutzern suchen.
{% endalert %}

