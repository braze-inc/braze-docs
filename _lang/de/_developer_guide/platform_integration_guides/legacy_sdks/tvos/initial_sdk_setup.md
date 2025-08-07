---
nav_title: SDK-Ersteinrichtung
article_title: SDK-Ersteinrichtung für tvOS
platform: tvOS
page_order: 0
page_type: reference
description: "Auf dieser Seite werden die Schritte zur Ersteinrichtung des tvOS Braze SDK beschrieben."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SDK-Ersteinrichtung

> Dieser Referenzartikel beschreibt, wie Sie das Braze SDK für tvOS installieren. Durch die Installation des Braze SDK erhalten Sie die grundlegenden Analytics-Funktionen.

{% alert note %}
Unser tvOS SDK unterstützt derzeit Analytics-Funktionen. Um eine tvOS App Ihrem Dashboard hinzuzufügen, öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).
{% endalert %}

Das tvOS Braze SDK sollte mit [CocoaPods](http://cocoapods.org/), einem Abhängigkeitsmanager für Objective-C- und Swift-Projekte, installiert oder aktualisiert werden. CocoaPods bietet zusätzliche Einfachheit bei der Integration und Aktualisierung.

## tvOS SDK CocoaPods Integration

### Schritt 1: CocoaPods installieren

Die Installation des SDK über die tvOS [CocoaPods](http://cocoapods.org/) automatisiert den Großteil des Installationsprozesses für Sie. Bevor Sie mit diesem Vorgang beginnen, stellen Sie sicher, dass Sie [Ruby Version 2.0.0](https://www.ruby-lang.org/en/installation/) oder höher verwenden.

Führen Sie als Erstes folgenden Befehl aus:

```bash
$ sudo gem install cocoapods
```

- Wenn Sie aufgefordert werden, die ausführbare Datei `rake` zu überschreiben, finden Sie weitere Informationen unter [Erste SchritteCocoaPods](http://guides.cocoapods.org/using/getting-started.html "Installationsanleitung") auf CocoaPods.org.
- Wenn Sie Probleme mit CocoaPods haben, lesen Sie bitte die [CocoaPods-FehlerbehebungCocoaPods](http://guides.cocoapods.org/using/troubleshooting.html "Troubleshooting Guide").

### Schritt 2: Erstellen der Poddatei

Nachdem Sie nun den CocoaPods Ruby Gem installiert haben, müssen Sie in Ihrem Xcode-Projektverzeichnis eine Datei namens `Podfile` erstellen.

Fügen Sie die folgende Zeile in Ihr Podfile ein:

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

Wir empfehlen Ihnen, Braze so zu versionieren, dass Pod-Updates automatisch alles erfassen, was kleiner als eine kleine Versionsaktualisierung ist. Also etwa `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`. Wenn Sie die neueste Version des Braze SDK automatisch integrieren möchten, auch bei größeren Änderungen, können Sie `pod 'Appboy-tvOS-SDK'` in Ihrem Podfile verwenden.

### Schritt 3: Installieren des Braze SDK

Um die Braze SDK CocoaPods zu installieren, navigieren Sie in Ihrem Terminal zum Verzeichnis Ihres Xcode-App-Projekts und führen den folgenden Befehl aus:
```
pod install
```

Jetzt sollten Sie den von CocoaPods erstellten neuen Xcode-Projektarbeitsbereich öffnen können. Stellen Sie sicher, dass Sie diesen Xcode-Workspace anstelle Ihres Xcode-Projekts verwenden. 

![]({% image_buster /assets/img_archive/podsworkspace.png %})

### Schritt 4: Aktualisieren Ihres App-Delegaten

{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie die folgende Codezeile in Ihre Datei `AppDelegate.m` ein:

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

Fügen Sie in Ihrer `AppDelegate.m`-Datei  das folgende Snippet in Ihre Methode `application:didFinishLaunchingWithOptions` ein:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Schließlich aktualisieren Sie `YOUR-API-KEY` mit dem korrekten Wert auf Ihrer Seite **Einstellungen verwalten**.

{% endtab %}
{% tab schnell %}

Wenn Sie das Braze SDK mit CocoaPods oder Carthage integrieren, fügen Sie die folgende Codezeile in Ihre `AppDelegate.swift`-Datei ein:

```swift
import AppboyTVOSKit
```

Weitere Informationen zur Verwendung von Objective-C Code in Swift-Projekten finden Sie in den [Apple Developer Docs](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Fügen Sie in `AppDelegate.swift` folgendes Snippet zu Ihrem `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` hinzu:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Als nächstes aktualisieren Sie `YOUR-API-KEY` auf der Seite **Einstellungen verwalten** mit dem richtigen Wert.

Unser `sharedInstance`-Singleton wird null sein, bevor `startWithApiKey:` aufgerufen wird, da dies eine Voraussetzung für die Verwendung jeglicher Braze-Funktionen ist.

{% endtab %}
{% endtabs %}

{% alert warning %}
Stellen Sie sicher, dass Sie Braze im Haupt-Thread Ihrer Anwendung initialisieren. Eine asynchrone Initialisierung kann zu fehlerhaften Funktionen führen.
{% endalert %}

### Schritt 5: Geben Sie Ihren benutzerdefinierten Endpunkt oder Daten-Cluster an

{% alert note %}
Ab Dezember 2019 werden keine benutzerdefinierten Endpunkte mehr vergeben. Wenn Sie einen bereits bestehenden benutzerdefinierten Endpunkt haben, können Sie diesen weiterhin verwenden. Weitere Einzelheiten finden Sie in unserer <a href="{{site.baseurl}}/api/basics/#endpoints">Liste der verfügbaren Endpunkte</a>.
{% endalert %}

Ihre Braze-Vertretung sollte Sie bereits über den [richtigen Endpunkt]({{ site.baseurl }}/user_guide/ informiert haben.administrative/access_braze/sdk_endpoints/).

#### Endpunktkonfiguration zur Kompilierzeit (empfohlen)
Wenn ein bereits vorhandener benutzerdefinierter Endpunkt angegeben wird:
- Ab Braze iOS SDK v3.0.2 können Sie einen angepassten Endpunkt mithilfe der Datei `Info.plist` festlegen. Fügen Sie das Wörterbuch `Appboy` zu Ihrer Datei Info.plist hinzu. Fügen Sie im `Appboy`-Dictionary den String-Untereintrag `Endpoint` hinzu und setzen Sie den Wert auf die Autorität Ihrer angepassten Endpunkt-URLs (z.B. `sdk.iad-01.braze.com`, nicht `https://sdk.iad-01.braze.com`).

#### Laufzeit-Endpunkt-Konfiguration
Wenn ein bereits vorhandener angepasster Endpunkt angegeben wird:
- Ab Braze iOS SDK v3.17.0+ können Sie Ihren Endpunkt über den `ABKEndpointKey` innerhalb des `appboyOptions` Parameters, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird, überschreiben. Setzen Sie den Wert auf Ihre angepasste Endpunkt-URL-Autorität (z. B. `sdk.iad-01.braze.com`, nicht `https://sdk.iad-01.braze.com`).

{% alert note %}
Die Unterstützung für das Setzen von Endpunkten zur Laufzeit mit `ABKAppboyEndpointDelegate` wurde in Braze iOS SDK v3.17.0 entfernt. Wenn Sie bereits `ABKAppboyEndpointDelegate` verwenden, beachten Sie, dass in den Braze iOS SDK Versionen v3.14.1 bis v3.16.0 jeder Verweis auf `dev.appboy.com` in Ihrer `getApiEndpoint()` Methode durch einen Verweis auf `sdk.iad-01.braze.com` ersetzt werden muss.
{% endalert %}

### SDK-Integration abgeschlossen

Braze sollte nun Daten von Ihrer Anwendung erfassen und die grundlegende Integration sollte abgeschlossen sein. Beachten Sie, dass Bitcode bei der Kompilierung Ihrer tvOS App und aller anderen Bibliotheken von Drittanbietern aktiviert sein muss.

### Aktualisieren des Braze SDK über CocoaPods

Um einen Cocoapod zu aktualisieren, führen Sie einfach die folgenden Befehle in Ihrem Projektverzeichnis aus:

```
pod update
```

## Anpassen von Braze beim Starten

Wenn Sie Braze beim Start anpassen möchten, können Sie stattdessen die Braze-Initialisierungsmethode `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` verwenden und eine optionale `NSDictionary` von Braze-Starttasten übergeben.
{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie in Ihrer `AppDelegate.m` Datei innerhalb Ihrer `application:didFinishLaunchingWithOptions` Methode die folgende Braze-Methode hinzu:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab schnell %}

Fügen Sie in `AppDelegate.swift` innerhalb Ihrer Methode `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` die folgende Braze-Methode hinzu:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

wobei `appboyOptions` eine `Dictionary` der Werte der Startkonfiguration ist.

{% endtab %}
{% endtabs %}

Diese Methode würde die Initialisierungsmethode `startWithApiKey:inApplication:withLaunchOptions:` ersetzen und wird mit den folgenden Parametern aufgerufen:

- `YOUR-API-KEY`: Den API-Schlüssel Ihrer Anwendung finden Sie unter **Einstellungen verwalten** auf dem Braze-Dashboard.
- `application`: Die aktuelle App.
- `launchOptions`: Die Optionen `NSDictionary`, die Sie von `application:didFinishLaunchingWithOptions:` erhalten.
- `appboyOptions`: Eine optionale `NSDictionary` mit Werten für die Startkonfiguration von Braze.

Siehe [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) für eine Liste der Braze-Starttasten.

## Appboy.sharedInstance() und Swift-Nullbarkeit
Abweichend von der üblichen Praxis ist das Singleton `Appboy.sharedInstance()` optional. Das liegt daran, dass `sharedInstance` `nil` ist, bevor `startWithApiKey:` aufgerufen wird, und es gibt einige nicht standardmäßige, aber nicht ungültige Implementierungen, in denen eine verzögerte Initialisierung verwendet werden kann.

Wenn Sie `startWithApiKey:` in Ihrem `didFinishLaunchingWithOptions:` Delegaten aufrufen, bevor Sie auf `sharedInstance` von Appboy (Standardimplementierung) zugreifen, können Sie eine optionale Verkettung wie `Appboy.sharedInstance()?.changeUser("testUser")` verwenden, um lästige Überprüfungen zu vermeiden. Dies ist vergleichbar mit einer Objective-C-Implementierung, die von einem Nicht-Null-Wert `sharedInstance` ausgeht.

## Optionen für die manuelle Integration

Sie können unser tvOS SDK auch manuell integrieren - holen Sie sich einfach das Framework aus unserem [Public Repository](https://github.com/appboy/appboy-ios-sdk) und initialisieren Sie Braze wie in den vorangegangenen Abschnitten beschrieben.

## Nutzeridentifizierung und Analytics-Berichte
In unserer [iOS Dokumentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) finden Sie Informationen zum Einstellen von Benutzer-IDs, zum Protokollieren angepasster Events und zum Einstellen von Nutzer:innen-Attributen. Wir empfehlen Ihnen auch, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) vertraut zu machen.

