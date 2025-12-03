## Integration des Swift SDK

Sie können das Braze Swift SDK mithilfe des Swift-Paketmanagers (SPM), CocoaPods oder manueller Integrationsmethoden integrieren und anpassen. Weitere Informationen über die verschiedenen SDK-Symbole finden Sie in der [referenzierten Dokumentation zu Braze Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/).

### Voraussetzungen

Bevor Sie beginnen, überprüfen Sie, ob Ihre Umgebung von der [neuesten Braze Swift SDK-Version](https://github.com/braze-inc/braze-swift-sdk#version-information) unterstützt wird.

### Schritt 1: Installieren Sie das Braze Swift SDK

Wir empfehlen die Verwendung des [Swift-Paketmanagers (SwiftPM)](https://swift.org/package-manager/) oder [CocoaPods](http://cocoapods.org/) zur Installation des Braze Swift SDK. Alternativ können Sie das SDK auch manuell installieren.

{% tabs local %}
{% tab Swift Package Manager %}
#### Schritt 1.1: SDK-Version importieren

Öffnen Sie Ihr Projekt und navigieren Sie zu den Einstellungen Ihres Projekts. Wählen Sie die Registerkarte **Swift-Pakete** und klicken Sie auf die Schaltfläche <i class="fas fa-plus"></i> hinzufügen unterhalb der Paketliste.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
Ab Version 7.4.0 verfügt das Braze Swift SDK über zusätzliche Verteilungskanäle als [statische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) und [dynamische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Wenn Sie stattdessen eines dieser Formate verwenden möchten, folgen Sie den Installationsanweisungen vom jeweiligen Repository.
{% endalert %}

Geben Sie die URL unseres iOS Swift SDK-Repository `https://github.com/braze-inc/braze-swift-sdk` in das Textfeld ein. Wählen Sie unter dem Abschnitt **Abhängigkeitsregel** die SDK-Version aus. Klicken Sie schließlich auf **Paket hinzufügen**.

![]({% image_buster /assets/img/importsdk_example.png %})

#### Schritt 1.2: Wählen Sie Ihre Pakete aus

Das Braze Swift SDK teilt Features in eigenständige Bibliotheken auf, um Entwicklern mehr Kontrolle darüber zu geben, welche Features sie in ihre Projekte importieren möchten.

| Paket         | Details                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | Haupt-SDK-Bibliothek mit Unterstützung für Analysen und Push-Benachrichtigungen.                                                                                        |
| `BrazeLocation` | Standortbibliothek mit Unterstützung für Standortanalysen und Geofence-Überwachung.                                                                              |
| `BrazeUI`       | Die von Braze bereitgestellte Benutzeroberfläche Bibliothek für In-App-Nachrichten, Content-Cards und Banner. Importieren Sie diese Bibliothek, wenn Sie die Standard UI Komponenten verwenden möchten. |

{: .ws-td-nw-1}

##### Über die Bibliotheken der Extension

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) und [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) sind Erweiterungsmodule, die zusätzliche Funktionen bieten und nicht direkt zu Ihrem Hauptanwendungsziel hinzugefügt werden sollten. Folgen Sie stattdessen den verlinkten Anleitungen, um sie separat in ihre jeweiligen Zielerweiterungen zu integrieren.
{% endalert %}

| Paket                    | Details                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | Erweiterungsbibliothek für Benachrichtigungsdienste mit Unterstützung für umfangreiche Push-Benachrichtigungen. |
| `BrazePushStory`           | Erweiterungsbibliothek für Benachrichtigungsinhalte mit Unterstützung für Push Stories.            |

{: .ws-td-nw-1}

Wählen Sie das Paket, das Ihren Anforderungen am besten entspricht, und klicken Sie auf **Paket hinzufügen**. Stellen Sie sicher, dass Sie mindestens `BrazeKit` auswählen.

![]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### Schritt 1.1: CocoaPods installieren

Eine vollständige Anleitung finden Sie im [CocoaPods-Handbuch Erste Schritte](https://guides.cocoapods.org/using/getting-started.html). Ansonsten können Sie den folgenden Befehl ausführen, um schnell loszulegen:

```bash
$ sudo gem install cocoapods
```

Wenn Sie nicht weiterkommen, lesen Sie die [CocoaPods-Anleitung zur Fehlerbehebung](http://guides.cocoapods.org/using/troubleshooting.html).

#### Schritt 1.2: Erstellen der Poddatei

Als nächstes erstellen Sie in Ihrem Xcode-Projektverzeichnis eine Datei namens `Podfile`.

{% alert note %}
Ab Version 7.4.0 verfügt das Braze Swift SDK über zusätzliche Verteilungskanäle als [statische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) und [dynamische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Wenn Sie stattdessen eines dieser Formate verwenden möchten, folgen Sie den Installationsanweisungen vom jeweiligen Repository.
{% endalert %}

Fügen Sie die folgende Zeile in Ihr Podfile ein:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` enthält die wichtigste SDK-Bibliothek mit Unterstützung für Analytics und Push-Benachrichtigungen.

Wir empfehlen Ihnen, Braze so zu versionieren, dass Pod-Updates automatisch alles erfassen, was kleiner als eine kleine Versionsaktualisierung ist. Dies sieht folgendermaßen aus: `pod 'BrazeKit' ~> Major.Minor.Build`. Wenn Sie die neueste Version des Braze SDK auch bei größeren Änderungen automatisch integrieren möchten, können Sie `pod 'BrazeKit'` in Ihrem Podfile verwenden.

##### Über zusätzliche Bibliotheken

Das Braze Swift SDK teilt Features in eigenständige Bibliotheken auf, um Entwicklern mehr Kontrolle darüber zu geben, welche Features sie in ihre Projekte importieren möchten. Zusätzlich zu `BrazeKit` können Sie die folgenden Bibliotheken zu Ihrem Podfile hinzufügen:

| Bibliothek               | Details                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | Standortbibliothek mit Unterstützung für Standortanalysen und Geofence-Überwachung.                                                                              |
| `pod 'BrazeUI'`       | Die von Braze bereitgestellte Benutzeroberfläche Bibliothek für In-App-Nachrichten, Content-Cards und Banner. Importieren Sie diese Bibliothek, wenn Sie die Standard UI Komponenten verwenden möchten. |

{: .ws-td-nw-1}

###### Erweiterungsbibliotheken

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) und [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) sind Erweiterungsmodule, die zusätzliche Funktionen bieten und nicht direkt zu Ihrem Hauptanwendungsziel hinzugefügt werden sollten. Stattdessen müssen Sie für jedes dieser Module eigene Erweiterungs-Targets erstellen und die Braze-Module in ihre entsprechenden Targets importieren.

| Bibliothek                          | Details                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | Erweiterungsbibliothek für Benachrichtigungsdienste mit Unterstützung für umfangreiche Push-Benachrichtigungen. |
| `pod 'BrazePushStory'`           | Erweiterungsbibliothek für Benachrichtigungsinhalte mit Unterstützung für Push Stories.            |

{: .ws-td-nw-1}

#### Schritt 1.3: Installieren Sie das SDK

Um die Braze SDK CocoaPod zu installieren, navigieren Sie in Ihrem Terminal zum Verzeichnis Ihres Xcode-App-Projekts und führen den folgenden Befehl aus:
```
pod install
```

Jetzt sollten Sie den von CocoaPods erstellten neuen Xcode-Projektarbeitsbereich öffnen können. Stellen Sie sicher, dass Sie diesen Xcode-Workspace anstelle Ihres Xcode-Projekts verwenden.

![Ein Braze-Beispielordner, der erweitert wurde, um die neue `BrazeExample.workspace` zu zeigen.]({% image_buster /assets/img/braze_example_workspace.png %})

#### Update des SDK mit CocoaPods

Um einen CocoaPod zu aktualisieren, führen Sie einfach den folgenden Befehl in Ihrem Projektverzeichnis aus:

```
pod update
```
{% endtab %}

{% tab Manual %}
#### Schritt 1.1: Laden Sie das Braze SDK herunter

Rufen Sie die [Braze SDK Release-Seite auf GitHub](https://github.com/braze-inc/braze-swift-sdk/releases) auf und laden Sie `braze-swift-sdk-prebuilt.zip` herunter.

!["Die Braze SDK Release-Seite auf GitHub."]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### Schritt 1.2: Wählen Sie Ihre Frameworks aus

Das Braze Swift SDK enthält eine Vielzahl von eigenständigen XCFrameworks, die Ihnen die Freiheit geben, nur die gewünschten Features zu integrieren. Verwenden Sie folgende Tabelle, um Ihre XCFrameworks auszuwählen:

| Paket                    | Erforderlich? | Beschreibung                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Ja       | Die SDK-Hauptbibliothek, die Unterstützung für Analytics und Push-Benachrichtigungen bietet                                                                                                                                                                                                                                                         |
| `BrazeLocation`            | Kein:e        | Bibliothek für Standorte mit Unterstützung für Analytics und Geofence-Überwachung.                                                                                                                                                                                                                                               |
| `BrazeUI`                  | Kein:e        | Die von Braze bereitgestellte Benutzeroberfläche Bibliothek für In-App-Nachrichten, Content-Cards und Banner. Importieren Sie diese Bibliothek, wenn Sie die Standard UI Komponenten verwenden möchten.                                                                                                                                                                      |
| `BrazeNotificationService` | Kein:e        | Bibliothek zur Erweiterung des Benachrichtigungsdienstes mit Unterstützung für Rich-Push-Benachrichtigungen. Fügen Sie diese Bibliothek nicht direkt zum Hauptanwendungsziel hinzu, sondern [fügen Sie `BrazeNotificationService` separat hinzu](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).                 |
| `BrazePushStory`           | Kein:e        | Bibliothek zur Erweiterung von Benachrichtigungsinhalten, die Push-Storys unterstützt. Fügen Sie diese Bibliothek nicht direkt zum Hauptanwendungsziel hinzu, sondern [fügen Sie `BrazePushStory` separat hinzu](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                                 |
| `BrazeKitCompat`           | Kein:e        | Kompatibilitätsbibliothek mit allen `Appboy`- und `ABK*`-Klassen und -Methoden, die in der `Appboy-iOS-SDK` Version 4X.X. verfügbar waren. Einzelheiten zur Verwendung finden Sie im minimalen Migrationsszenario im [Migrationshandbuch](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/).            |
| `BrazeUICompat`            | Kein:e        | Kompatibilitätsbibliothek mit allen `ABK*`-Klassen und -Methoden, die in der Bibliothek `AppboyUI` in `Appboy-iOS-SDK` Version 4X.X. verfügbar waren. Einzelheiten zur Verwendung finden Sie im minimalen Migrationsszenario im [Migrationshandbuch](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | Kein:e        | Die Abhängigkeit wird nur von `BrazeUICompat` im minimalen Migrationsszenario verwendet.                                                                                                                                                                                                                                                           |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Schritt 1.3: Bereiten Sie Ihre Dateien vor

Entscheiden Sie, ob Sie **statische** oder **dynamische** XCFrameworks verwenden möchten, und bereiten Sie dann Ihre Dateien vor:

1. Erstellen Sie ein temporäres Verzeichnis für Ihre XCFrameworks.
2. Öffnen Sie in `braze-swift-sdk-prebuilt` das Verzeichnis `dynamic` und verschieben Sie `BrazeKit.xcframework` in Ihr Verzeichnis. Ihr Verzeichnis sollte in etwa so aussehen wie das folgende:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Verschieben Sie jedes der von Ihnen [gewählten XCFrameworks](#swift_step-2-choose-your-frameworks) in Ihr temporäres Verzeichnis. Ihr Verzeichnis sollte in etwa so aussehen wie das folgende:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### Schritt 1.4: Integrieren Sie Ihre Frameworks

Als Nächstes integrieren Sie die **dynamischen** oder **statischen** XCFrameworks, die Sie [zuvor vorbereitet haben](#swift_step-3-prepare-your-files):

Wählen Sie in Ihrem Xcode-Projekt Ihr Build-Target und dann **Allgemein**. Ziehen Sie die [Dateien, die Sie zuvor vorbereitet haben](#swift_step-3-prepare-your-files), per Drag-and-Drop unter **Frameworks, Bibliotheken und eingebettete Inhalte**.

!["Ein Xcode-Beispielprojekt, bei dem jede Bibliothek von Braze auf 'Einbetten & Signieren' eingestellt ist."]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
Ab dem Swift SDK 12.0.0 sollten Sie für die Braze XCFrameworks sowohl für die statische als auch für die dynamische Variante immer **Embed & Sign** auswählen. Dadurch wird sichergestellt, dass die Ressourcen des Frameworks ordnungsgemäß in Ihr App-Bundle eingebettet werden.
{% endalert %}

{% alert tip %}
Um die GIF-Unterstützung zu aktivieren, fügen Sie `SDWebImage.xcframework` hinzu, das sich entweder in `braze-swift-sdk-prebuilt/static` oder `braze-swift-sdk-prebuilt/dynamic` befindet.
{% endalert %}

#### Häufige Fehler bei Objective-C Projekten

Wenn Ihr Xcode-Projekt nur Objective-C-Dateien enthält, erhalten Sie möglicherweise die Fehlermeldung "Fehlendes Symbol", wenn Sie versuchen, Ihr Projekt zu erstellen. Um diese Fehler zu beheben, öffnen Sie Ihr Projekt und fügen Sie eine leere Swift-Datei zu Ihrem Dateibaum hinzu. Dadurch wird Ihre Build-Toolchain gezwungen, [Swift Runtime](https://support.apple.com/kb/dl1998) einzubetten und während der Build-Zeit eine Verbindung zu den entsprechenden Frameworks herzustellen.

```bash
FILE_NAME.swift
```

Ersetzen Sie `FILE_NAME` durch einen beliebigen String ohne Leerzeichen. Ihre Datei sollte etwa so aussehen wie die folgende:

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### Schritt 2: Verzögerte Initialisierung einrichten (optional)

Sie können die Initialisierung des Braze Swift SDK verzögern. Das ist nützlich, wenn Ihre App die Konfiguration laden oder auf die Zustimmung des Nutzers:innen warten muss, bevor Sie das SDK starten. Die verzögerte Initialisierung stellt sicher, dass Push-Benachrichtigungen von Braze in die Warteschlange gestellt werden, bis das SDK bereit ist.

Um dies zu ermöglichen, rufen Sie `Braze.prepareForDelayedInitialization()` so früh wie möglich auf - idealerweise innerhalb oder vor Ihrem `application(_:didFinishLaunchingWithOptions:)`.

{% alert note %}
Dies gilt nur für Push-Benachrichtigungen von Braze. Andere Push-Benachrichtigungen werden normalerweise von Systemdelegierten bearbeitet.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
[`Braze.prepareForDelayedInitialization(pushAutomation:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) akzeptiert einen optionalen Parameter `pushAutomation`. Bei der Einstellung `nil` sind alle Features der Push-Automatisierung aktiviert, mit Ausnahme der Anfrage zur Push-Autorisierung beim Start.
{% endalert %}

### Schritt 3: Aktualisieren Sie Ihren App-Delegierten

{% alert important %}
Im Folgenden wird davon ausgegangen, dass Sie Ihrem Projekt bereits eine `AppDelegate` hinzugefügt haben (die nicht standardmäßig erstellt wird). Wenn Sie dies nicht vorhaben, sollten Sie das Braze SDK so früh wie möglich initialisieren, z.B. beim Start der App.
{% endalert %}

{% subtabs local %}
{% subtab swift %}
Fügen Sie die folgende Code-Zeile in Ihre `AppDelegate.swift`-Datei ein, um die im Braze Swift SDK enthaltenen Features zu importieren:

```swift
import BrazeKit
```

Als Nächstes fügen Sie der Klasse `AppDelegate` eine statische Eigenschaft hinzu, um während der gesamten Lifetime Ihrer Anwendung auf die Braze-Instanz zu referenzieren:

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

Fügen Sie schließlich in `AppDelegate.swift` das folgende Snippet zu Ihrer Methode `application:didFinishLaunchingWithOptions:` hinzu:

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

Aktualisieren Sie `YOUR-APP-IDENTIFIER-API-KEY` und `YOUR-BRAZE-ENDPOINT` mit dem korrekten Wert auf Ihrer **App-Einstellungsseite**. Sehen Sie sich unsere [API-Bezeichner-Typen]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) an, um mehr darüber zu erfahren, wo Sie Ihren App-Bezeichner-API-Schlüssel finden.

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Fügen Sie die folgende Codezeile in Ihre Datei `AppDelegate.m` ein:

```objc
@import BrazeKit;
```

Als Nächstes fügen Sie eine statische Variable in Ihre `AppDelegate.m`-Datei ein, um während der gesamten Lifetime Ihrer Anwendung eine Referenz auf die Braze-Instanz zu behalten:

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

Schließlich fügen Sie in Ihrer `AppDelegate.m`-Datei das folgende Snippet zur Methode `application:didFinishLaunchingWithOptions:` hinzu:

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

Aktualisieren Sie `YOUR-APP-IDENTIFIER-API-KEY` und `YOUR-BRAZE-ENDPOINT` mit dem richtigen Wert von Ihrer Seite **Einstellungen verwalten**. In unserer [API-Dokumentation]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) finden Sie weitere Informationen darüber, wo Sie den API-Schlüssel für Ihre App-Kennung finden.

{% endsubtab %}
{% endsubtabs local %}

## Optionale Konfigurationen

### Protokollieren

#### Protokollstufen

Die Standard-Protokollebene für das Braze Swift SDK ist `.error`- dies ist auch die minimal unterstützte Ebene, wenn die Protokolle aktiviert sind. Dies ist die vollständige Liste der Protokollebenen:

| Schnell       | Objective-C              | Beschreibung                                                  |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | Debugging-Informationen protokollieren + `.info` + `.error`.              |
| `.info`     | `BRZLoggerLevelInfo`     | Allgemeine SDK-Informationen protokollieren (Nutzer:innen-Änderungen, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Fehler protokollieren.                                                  |
| `.disabled` | `BRZLoggerLevelDisabled` | Es erfolgt keine Protokollierung.                                           |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Einstellen der Protokollstufe

Sie können die Protokollstufe zur Laufzeit in Ihrem `Braze.Configuration` Objekt zuweisen. Ausführliche Informationen zur Verwendung finden Sie unter [`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

{% tabs %}
{% tab schnell %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}
