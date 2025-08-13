---
nav_title: Fertigstellung der Integration
article_title: Fertigstellung der Swift SDK-Integration
platform: Swift
description: "Dieser Referenzartikel zeigt, wie Sie die Integration des Braze Swift SDK abschließen, nachdem Sie es über eine der Integrationsoptionen installiert haben."
page_order: 2

---

# Fertigstellung der Integration

> Bevor Sie diese Schritte ausführen, stellen Sie sicher, dass Sie das Swift SDK für iOS entweder mit dem [Swift-Paketmanager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) oder mit [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/) integriert haben.

## Aktualisieren Sie Ihren App-Delegierten

{% tabs %}
{% tab schnell %}

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

{% endtab %}
{% tab OBJECTIVE-C %}

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

{% endtab %}
{% endtabs %}


## SDK-Integration abgeschlossen

An diesem Punkt sollte Ihre grundlegende Integration abgeschlossen sein. Braze sollte nun Daten von Ihrer Anwendung sammeln. Folgen Sie den anderen Artikeln in diesem Integrationsleitfaden, um die gesamte Palette der Features und Messaging-Kanäle von Braze zu implementieren und anzupassen.

## Zusätzliche Ressourcen

Unsere [SDK referenzierende Dokumentation der](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/ "iOS-Klassen") bietet zusätzliche Informationen und Anleitungen zu jedem SDK-Symbol.

