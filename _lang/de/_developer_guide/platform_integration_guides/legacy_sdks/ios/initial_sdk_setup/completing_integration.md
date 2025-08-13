---
nav_title: Fertigstellung der Integration
article_title: Fertigstellung der iOS SDK-Integration
platform: iOS
description: "Dieser Referenzartikel beschreibt, wie Sie die Integration des Braze SDK abschließen, nachdem Sie es über eine der Integrationsoptionen installiert haben."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Fertigstellung der Integration

Bevor Sie diese Schritte ausführen, vergewissern Sie sich bitte, dass das SDK mit [Carthage]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/carthage_integration/), [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/cocoapods/), dem [Swift-Paketmanager]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/) oder einer [manuellen]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/) Integration integriert wurde.

## Schritt 1: Aktualisieren Sie Ihren App-Delegierten

{% tabs %}
{% tab OBJECTIVE-C %}

Wenn Sie das Braze SDK mit CocoaPods, Carthage oder einer [dynamischen manuellen Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/) integrieren, fügen Sie die folgende Codezeile in die Datei `AppDelegate.m` ein:

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Wenn Sie die Integration mit dem Swift-Paketmanager oder einer [statischen manuellen Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/) vornehmen, verwenden Sie stattdessen diese Zeile:

```objc
#import "AppboyKit.h"
```

Fügen Sie als Nächstes in der Datei `AppDelegate.m` das folgende Snippet in die Methode `application:didFinishLaunchingWithOptions:` ein:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

Aktualisieren Sie `YOUR-APP-IDENTIFIER-API-KEY` mit dem richtigen Wert auf Ihrer Seite **Einstellungen verwalten**. In unserer [API-Dokumentation]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) finden Sie weitere Informationen darüber, wo Sie den API-Schlüssel für Ihre App-Kennung finden.

{% endtab %}
{% tab schnell %}

Wenn Sie das Braze SDK mit CocoaPods, Carthage oder einer [dynamischen manuellen Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/) integrieren, fügen Sie die folgende Codezeile in die Datei `AppDelegate.swift` ein:

```swift
import Appboy_iOS_SDK
```

Wenn Sie die Integration mit dem Swift-Paketmanager oder einer [statischen manuellen Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/) vornehmen, verwenden Sie stattdessen diese Zeile:

```swift
import AppboyKit
```
Weitere Informationen zur Verwendung von Objective-C-Code in Swift-Projekten finden Sie in der [Apple-Entwicklerdokumentation](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Fügen Sie als Nächstes in `AppDelegate.swift` das folgende Snippet zu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` hinzu:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Aktualisieren Sie `YOUR-APP-IDENTIFIER-API-KEY` mit dem richtigen Wert auf Ihrer Seite **Einstellungen verwalten**. In unserer [API-Dokumentation]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) finden Sie weitere Informationen darüber, wo Sie den API-Schlüssel für Ihre App-Kennung finden.

{% endtab %}
{% endtabs %}

{% alert note %}
Das Singleton `sharedInstance` ist null, bevor `startWithApiKey:` aufgerufen wird, da dies eine Voraussetzung für die Verwendung jeglicher Braze-Funktionen ist.
{% endalert %}

{% alert warning %}
Stellen Sie sicher, dass Sie Braze im Haupt-Thread Ihrer Anwendung initialisieren. Eine asynchrone Initialisierung kann zu fehlerhaften Funktionen führen.
{% endalert %}


## Schritt 2: Legen Sie Ihren Daten-Cluster fest

{% alert note %}
Beachten Sie, dass seit Dezember 2019 keine angepassten Endpunkte mehr vergeben werden. Bereits vorhandene angepasste Endpunkte können weiterhin verwendet werden. Weitere Einzelheiten finden Sie in unserer <a href="{{site.baseurl}}/api/basics/#endpoints">Liste der verfügbaren Endpunkte</a>.
{% endalert %}

### Endpunktkonfiguration zur Kompilierzeit (empfohlen)

Wenn ein bereits vorhandener benutzerdefinierter Endpunkt angegeben wird:
- Ab Braze iOS SDK v3.0.2 können Sie einen angepassten Endpunkt mithilfe der Datei `Info.plist` festlegen. Fügen Sie das Wörterbuch `Braze` zu Ihrer Datei `Info.plist` hinzu. Fügen Sie im Wörterbuch `Braze` den Zeichenfolgen-Untereintrag `Endpoint` hinzu und legen Sie den Wert auf die Autorität der URL des angepassten Endpunkts fest (z. B. `sdk.iad-01.braze.com`, nicht `https://sdk.iad-01.braze.com`). Beachten Sie, dass vor Braze iOS SDK v4.0.2 der Wörterbuchschlüssel `Appboy` anstelle von `Braze` verwendet werden muss.

Ihr Braze-Vertreter sollte Sie bereits über den [richtigen Endpunkt]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) informiert haben.

### Laufzeit-Endpunkt-Konfiguration

Wenn ein bereits vorhandener benutzerdefinierter Endpunkt angegeben wird:
- Ab Braze iOS SDK v3.17.0+ können Sie Ihren Endpunkt über den `ABKEndpointKey` innerhalb des `appboyOptions` Parameters, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird, überschreiben. Legen Sie den Wert auf die Autorität der URL des angepassten Endpunkts fest (z. B. `sdk.iad-01.braze.com`, nicht `https://sdk.iad-01.braze.com`).

## SDK-Integration abgeschlossen

Braze sollte nun Daten von Ihrer Anwendung erfassen und die grundlegende Integration sollte abgeschlossen sein. Lesen Sie die folgenden Artikel, um die [benutzerdefinierte Ereignisverfolgung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/), [Push-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) und die gesamte Palette der Braze-Funktionen zu aktivieren.

## Anpassen von Braze beim Starten

Wenn Sie Braze beim Start anpassen möchten, können Sie stattdessen die Braze-Initialisierungsmethode `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` verwenden und eine optionale `NSDictionary` von Braze-Starttasten übergeben.
{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie in Ihrer `AppDelegate.m` Datei innerhalb Ihrer `application:didFinishLaunchingWithOptions:` Methode die folgende Braze-Methode hinzu:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

Beachten Sie, dass diese Methode die Initialisierungsmethode `startWithApiKey:inApplication:withLaunchOptions:` ersetzen würde.

{% endtab %}
{% tab schnell %}

Fügen Sie in `AppDelegate.swift` innerhalb der Methode `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` die folgende Braze-Methode hinzu, wobei `appboyOptions` ein `Dictionary` der Startkonfigurationswerte ist:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

Beachten Sie, dass diese Methode die Initialisierungsmethode `startWithApiKey:inApplication:withLaunchOptions:` ersetzen würde.

{% endtab %}
{% endtabs %}

Diese Methode wird mit den folgenden Parametern aufgerufen:

- `YOUR-APP-IDENTIFIER-API-KEY`: Der API-Schlüssel des [App-Bezeichners]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) aus dem Braze-Dashboard.
- `application` - Die aktuelle App.
- `launchOptions`: Die Optionen für `NSDictionary`, die Sie aus `application:didFinishLaunchingWithOptions:` abrufen.
- `appboyOptions`: Ein optionales `NSDictionary` mit Werten für die Startkonfiguration von Braze.

Siehe [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h) für eine Liste der Braze-Starttasten.

## Appboy.sharedInstance() und Swift-Nullbarkeit
Abweichend von der üblichen Praxis ist das Singleton `Appboy.sharedInstance()` optional. Das liegt daran, dass `sharedInstance` `nil` ist, bevor `startWithApiKey:` aufgerufen wird, und es gibt einige nicht standardmäßige, aber nicht ungültige Implementierungen, in denen eine verzögerte Initialisierung verwendet werden kann.

Wenn Sie `startWithApiKey:` in Ihrem `didFinishLaunchingWithOptions:` Delegaten aufrufen, bevor Sie auf `sharedInstance` von Appboy (Standardimplementierung) zugreifen, können Sie eine optionale Verkettung wie `Appboy.sharedInstance()?.changeUser("testUser")` verwenden, um lästige Überprüfungen zu vermeiden. Dies ist vergleichbar mit einer Objective-C-Implementierung, die von einem Nicht-Null-Wert `sharedInstance` ausgeht.

## Zusätzliche Ressourcen

Weitere Informationen zu SDK-Methoden sind der vollständigen [iOS Class Documentation](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html "") zu entnehmen.

