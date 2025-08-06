Durch die Installation des Braze SDK erhalten Sie grundlegende Analytics-Funktionen{% if include.platform == 'iOS' %} sowie funktionierende In-App-Nachrichten, mit der Sie Ihre Benutzer einbinden können{% endif %}.

Das {{include.platform}} Braze SDK sollte mit [CocoaPods](http://cocoapods.org/), einem Abhängigkeitsmanager für Objective-C und Swift-Projekte, installiert oder aktualisiert werden. CocoaPods bietet zusätzliche Einfachheit bei der Integration und Aktualisierung.

## {{include.platform}} SDK CocoaPods Integration

### Schritt 1: CocoaPods installieren

Die Installation des SDK über die {{include.platform}} [CocoaPods](http://cocoapods.org/) automatisiert den Großteil des Installationsprozesses für Sie. Bevor Sie mit diesem Vorgang beginnen, vergewissern Sie sich, dass Sie die [Ruby-Version 2.0.0](https://www.ruby-lang.org/en/installation/) oder höher verwenden. Beachten Sie, dass Kenntnisse der Ruby-Syntax nicht erforderlich sind, um dieses SDK zu installieren.

Führen Sie einfach den folgenden Befehl aus, um loszulegen:

```bash
$ sudo gem install cocoapods
```

**Anmerkung**: Wenn Sie aufgefordert werden, die ausführbare Datei `rake` zu überschreiben, finden Sie weitere Informationen in der [Anleitung „Erste Schritte“ auf CocoaPods.org](http://guides.cocoapods.org/using/getting-started.html).

**Anmerkung**: Wenn Sie Probleme mit CocoaPods haben, lesen Sie bitte die [CocoaPods-Anleitung zur Fehlerbehebung](http://guides.cocoapods.org/using/troubleshooting.html).

### Schritt 2: Erstellen der Poddatei

Nachdem Sie nun den CocoaPods Ruby Gem installiert haben, müssen Sie in Ihrem Xcode-Projektverzeichnis eine Datei namens `Podfile` erstellen.

Fügen Sie die folgende Zeile in Ihre Poddatei ein:

```
target 'YourAppTarget' do
  pod 'Appboy-{{include.platform}}-SDK'
end
```

**Anmerkung**: Wir empfehlen Ihnen, Braze so zu versionieren, dass Pod-Updates automatisch alles erfassen, was kleiner als eine kleine Versionsaktualisierung ist. Das sieht aus wie 'pod 'Appboy-{{include.platform}}-SDK' ~> Major.Minor.Build'. Wenn Sie die neueste Version von Braze SDK auch bei größeren Änderungen automatisch integrieren möchten, können Sie `pod 'Appboy-{{include.platform}}-SDK'` in Ihrem Podfile verwenden.
{% if include.platform == 'iOS' %}
**Anmerkung**: Wenn Sie keine Braze-Standard-UI verwenden und die SDWebImage-Abhängigkeit nicht einführen möchten, verweisen Sie Ihre Braze-Abhängigkeit in Ihrem Podfile auf unseren Core-Subspec, wie `pod 'Appboy-iOS-SDK/Core'` in Ihrem Podfile. {% endif %}.

### Schritt 3: Installieren des Braze SDK

Um die Braze SDK CocoaPods zu installieren, navigieren Sie in Ihrem Terminal zum Verzeichnis Ihres Xcode-App-Projekts und führen den folgenden Befehl aus:
```
pod install
```

Jetzt sollten Sie den neuen, von CocoaPods erstellten Xcode-Projektarbeitsbereich öffnen können. Stellen Sie sicher, dass Sie diesen Xcode-Workspace anstelle Ihres Xcode-Projekts verwenden. 

![Neuer Workspace]({% image_buster /assets/img_archive/podsworkspace.png %})

### Schritt 4: Aktualisieren Ihres App-Delegaten

{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie die folgende Codezeile in Ihre Datei `AppDelegate.m` ein:

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

Fügen Sie in Ihrer `AppDelegate.m`-Datei  das folgende Snippet in Ihre Methode `application:didFinishLaunchingWithOptions` ein:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab schnell %}

Wenn Sie das Braze SDK mit CocoaPods oder Carthage integrieren, fügen Sie die folgende Codezeile in Ihre `AppDelegate.swift`-Datei ein:

```swift
{% if include.platform == 'iOS' %}import Appboy_iOS_SDK{% else %}import AppboyTVOSKit{% endif %}
```

Weitere Informationen zur Verwendung von Objective-C-Code in Swift-Projekten finden Sie in den [Apple Developer Docs](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Fügen Sie in `AppDelegate.swift` folgendes Snippet zu Ihrem `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` hinzu:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

**Anmerkung**: Das Singleton von Braze `sharedInstance` ist null, bevor `startWithApiKey:` aufgerufen wird, da dies eine Voraussetzung für die Nutzung aller Braze-Funktionen ist.

{% endtab %}
{% endtabs %}

{% alert important %}
Stellen Sie sicher, dass Sie `YOUR-API-KEY` auf der Seite „Einstellungen verwalten“ mit dem richtigen Wert aktualisieren.
{% endalert %}

{% alert warning %}
Stellen Sie sicher, dass Sie Braze im Haupt-Thread Ihrer Anwendung initialisieren. Eine asynchrone Initialisierung kann zu fehlerhaften Funktionen führen.
{% endalert %}


### Schritt 5: Geben Sie Ihren benutzerdefinierten Endpunkt oder Daten-Cluster an

{% alert note %}
Beachten Sie, dass ab Dezember 2019 keine benutzerdefinierten Endpunkte mehr vergeben werden. Wenn Sie einen bereits bestehenden benutzerdefinierten Endpunkt haben, können Sie ihn weiterhin verwenden. Weitere Einzelheiten finden Sie in unserer <a href="{{site.baseurl}}/api/basics/#endpoints">Liste der verfügbaren Endpunkte</a>.
{% endalert %}

Ihre Braze-Vertretung sollte Sie bereits über den [richtigen Endpunkt]({{ site.baseurl }}/user_guide/ informiert haben.administrative/access_braze/sdk_endpoints/).

#### Endpunktkonfiguration zur Kompilierzeit (empfohlen)
Wenn ein bereits vorhandener angepasster Endpunkt...
- Ab Braze iOS SDK v3.0.2 können Sie einen angepassten Endpunkt mithilfe der Datei `Info.plist` festlegen. Fügen Sie das Wörterbuch `Appboy` zu Ihrer Datei Info.plist hinzu. Fügen Sie im Wörterbuch `Appboy` den Untereintrag `Endpoint` string hinzu und setzen Sie den Wert auf die Autorität Ihrer benutzerdefinierten Endpunkt-URL (zum Beispiel `sdk.iad-01.braze.com`, nicht `https://sdk.iad-01.braze.com`).

#### Laufzeit-Endpunkt-Konfiguration

Wenn ein bereits vorhandener angepasster Endpunkt...
- Ab Braze iOS SDK v3.17.0+ können Sie Ihren Endpunkt über den `ABKEndpointKey` innerhalb des `appboyOptions` Parameters, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird, überschreiben. Setzen Sie den Wert auf die Autorität Ihrer angepassten Endpunkt-URL (z. B. `sdk.iad-01.braze.com`, nicht `https://sdk.iad-01.braze.com`).

{% alert note %}
Die Unterstützung für das Setzen von Endpunkten zur Laufzeit mit `ABKAppboyEndpointDelegate` wurde in Braze iOS SDK v3.17.0 entfernt. Wenn Sie bereits `ABKAppboyEndpointDelegate` verwenden, beachten Sie, dass in den Braze iOS SDK Versionen v3.14.1 bis v3.16.0 jeder Verweis auf `dev.appboy.com` in Ihrer `getApiEndpoint()` Methode durch einen Verweis auf `sdk.iad-01.braze.com` ersetzt werden muss.
{% endalert %}

{% alert important %}
Um Ihren spezifischen Cluster herauszufinden, fragen Sie bitte Ihren Customer-Success-Manager oder wenden Sie sich an unser Support-Team.
{% endalert %}

### SDK-Integration abgeschlossen

Braze sollte nun Daten von Ihrer Anwendung sammeln und Ihre grundlegende Integration sollte abgeschlossen sein. {% if include.platform == 'iOS' %}Bitte lesen Sie die folgenden Abschnitte, um das Tracking angepasster Events, Push-Nachrichten, den News-Feed und die gesamte Palette der Braze-Features zu aktivieren.{% else %}Bitte beachten Sie, dass Bitcode beim Kompilieren Ihrer tvOS-App und aller anderen Bibliotheken von Drittanbietern aktiviert sein muss.{% endif %}

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

**Anmerkung**: Diese Methode würde die `startWithApiKey:inApplication:withLaunchOptions:` Initialisierungsmethode ersetzen.

Diese Methode wird mit den folgenden Parametern aufgerufen:

- `YOUR-API-KEY` - Der API-Schlüssel Ihrer Anwendung aus dem Braze Dashboard
- `application` - Die aktuelle App
- `launchOptions` - Die Optionen `NSDictionary`, die Sie von `application:didFinishLaunchingWithOptions:` erhalten
- `appboyOptions` - Ein optionales `NSDictionary` mit Startkonfigurationswerten für Braze

Siehe [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) für eine Liste der Braze-Starttasten.

## Appboy.sharedInstance() und Swift-Nullbarkeit
Abweichend von der üblichen Praxis ist das Singleton `Appboy.sharedInstance()` optional. Das liegt daran, dass `sharedInstance` `nil` ist, bevor `startWithApiKey:` aufgerufen wird, und es gibt einige nicht standardmäßige, aber nicht ungültige Implementierungen, in denen eine verzögerte Initialisierung verwendet werden kann.

Wenn Sie `startWithApiKey:` in Ihrem `didFinishLaunchingWithOptions:` Delegaten aufrufen, bevor Sie auf `sharedInstance` von Appboy (Standardimplementierung) zugreifen, können Sie eine optionale Verkettung wie `Appboy.sharedInstance()?.changeUser("testUser")` verwenden, um lästige Überprüfungen zu vermeiden. Dies ist vergleichbar mit einer Objective-C-Implementierung, die von einem Nicht-Null-Wert `sharedInstance` ausgeht.

