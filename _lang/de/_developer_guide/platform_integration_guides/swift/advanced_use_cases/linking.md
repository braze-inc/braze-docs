---
nav_title: Deeplinking
article_title: Deeplinking für iOS
platform: Swift
page_order: 1
description: "In diesem Artikel erfahren Sie, wie Sie den universellen Deeplink-Delegaten für Ihre iOS-App implementieren und Deeplinks zu App-Einstellungen für das Swift SDK setzen."

---

# Deeplinking

> Deeplinks setzen einen Link, der eine native App startet, bestimmte Inhalte anzeigt oder eine bestimmte Aktion ausführt. Wenn Sie zum ersten Mal Deeplinks in Ihre iOS App setzen möchten, folgen Sie diesen Schritten.

Allgemeine Informationen darüber, was Deeplinks sind, finden Sie in unserem [FAQ-Artikel]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking). 

## Schritt 1: Schema registrieren

Um Deeplinks setzen zu können, muss ein angepasstes Schema in Ihrer `Info.plist`-Datei angegeben sein. Die Navigationsstruktur wird durch eine Reihe von Wörterbüchern definiert. Jedes dieser Wörterbücher enthält ein String-Array mit Strings.

Verwenden Sie Xcode, um Ihre `Info.plist`-Datei zu bearbeiten:

1. Fügen Sie einen neuen Schlüssel hinzu, `URL types`. Xcode macht daraus automatisch ein Array, das ein Wörterbuch namens `Item 0` enthält.
2. Fügen Sie innerhalb von `Item 0` einen Schlüssel `URL identifier` hinzu. Stellen Sie den Wert auf Ihr angepasstes Schema ein.
3. Fügen Sie innerhalb von `Item 0` einen Schlüssel `URL Schemes` hinzu. Dies wird automatisch ein Array sein, das einen `Item 0`-String enthält.
4. Stellen Sie `URL Schemes` >> `Item 0` auf Ihr angepasstes Schema ein.

Wenn Sie Ihre `Info.plist`-Datei direkt bearbeiten möchten, können Sie auch dieser Spezifikation folgen:

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

## Schritt 2: Schemas allowlist hinzufügen

Sie müssen die URL-Schemata, die Sie an `canOpenURL(_:)` übergeben möchten, deklarieren, indem Sie den Schlüssel `LSApplicationQueriesSchemes` in die Datei Info.plist Ihrer App einfügen. Der Versuch, Schemata außerhalb dieser Liste aufzurufen, führt dazu, dass das System einen Fehler in den Protokollen des Geräts aufzeichnet und der Deeplink nicht geöffnet werden kann. Ein Beispiel für diesen Fehler sieht wie folgt aus:

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Wenn zum Beispiel eine In-App-Nachricht beim Antippen die Facebook App öffnen soll, muss die App das angepasste Schema von Facebook (`fb`) in Ihrer Erlaubnisliste haben. Andernfalls wird das System den Deeplink ablehnen. Deeplinks, die auf eine Seite oder Ansicht innerhalb Ihrer eigenen App verweisen, erfordern nach wie vor, dass das angepasste Schema Ihrer App unter `Info.plist` aufgeführt ist.

Ihre Beispiel-Allowlist könnte etwa so aussehen:

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

Weitere Informationen finden Sie in der [Dokumentation von Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) über die Taste `LSApplicationQueriesSchemes`.

## Schritt 3: Handler implementieren

Nachdem Sie die App aktiviert haben, ruft iOS die Methode [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc) auf. Das wichtige Argument ist das [NSURL-Objekt](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL).

{% tabs %}
{% tab schnell %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Insert your code here to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% endtabs %}

## App Transport Security (ATS)

### ATS-Anforderungen
Aus der [Dokumentation von Apple:](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14) "App Transport Security" ist ein Feature, das die Sicherheit der Verbindungen zwischen einer App und Internet Serviceleistungen; Diensten verbessert. Das Feature besteht aus Standard-Verbindungsanforderungen, die den Best Practices für sichere Verbindungen entsprechen. Apps können dieses Standardverhalten außer Kraft setzen und die Transportsicherheit deaktivieren."

ATS wird standardmäßig angewendet. Es erfordert, dass alle Verbindungen HTTPS verwenden und mit TLS 1.2 mit Forward Secrecy verschlüsselt werden. Weitere Informationen finden Sie unter [Voraussetzungen für die Verbindung mit ATS](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35). Alle Bilder, die von Braze an Endgeräte geliefert werden, werden von einem Content Delivery Network ("CDN") verarbeitet, das TLS 1.2 unterstützt und mit ATS kompatibel ist.

Sofern sie nicht als Ausnahmen in Ihrer Anwendung `Info.plist` angegeben sind, schlagen Verbindungen, die diese Anforderungen nicht erfüllen, mit Fehlern fehl, die in etwa so aussehen:

```
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

```
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

Die ATS-Konformität wird für Links durchgesetzt, die innerhalb der mobilen App geöffnet werden (unsere Standardbehandlung von angeklickten Links) und gilt nicht für Websites, die extern über einen Webbrowser geöffnet werden.

### Umgang mit ATS-Anforderungen

Sie können ATS auf eine der folgenden drei Arten handhaben:

#### Stellen Sie sicher, dass alle Links ATS-kompatibel sind (empfohlen).
Ihre Integration in Braze kann die ATS-Anforderungen erfüllen, indem Sie sicherstellen, dass alle bestehenden Links, zu denen Sie Nutzer weiterleiten (z. B. durch In-App-Nachrichten und Push-Kampagnen), die ATS-Anforderungen erfüllen. Es gibt zwar Möglichkeiten, die ATS-Beschränkungen zu umgehen, aber unsere Empfehlung ist sicherzustellen, dass alle verlinkten URLs ATS-konform sind. Da Apple immer mehr Wert auf die Sicherheit von Anwendungen legt, werden die folgenden Ansätze zur Zulassung von ATS-Ausnahmen von Apple nicht garantiert unterstützt.

#### ATS teilweise deaktivieren
Sie können zulassen, dass eine Teilmenge von Links mit bestimmten Domains oder Schemata als Ausnahmen von den ATS-Regeln behandelt werden. Ihre Integration in Braze erfüllt die ATS-Anforderungen, wenn jeder Link, den Sie in einem Messaging-Kanal von Braze verwenden, entweder ATS-konform ist oder mit einer Ausnahme behandelt wird.

Um eine Domain als Ausnahme des ATS hinzuzufügen, fügen Sie Folgendes in die Datei `Info.plist` Ihrer App ein:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

Weitere Informationen finden Sie in Apples Artikel über [Sicherheitsschlüssel für den Transport von Apps](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33).

#### ATS vollständig deaktivieren

Sie können ATS ganz abschalten. Beachten Sie, dass dies aufgrund des verlorenen Sicherheitsschutzes und der zukünftigen iOS-Kompatibilität nicht zu empfehlen ist. Um ATS zu deaktivieren, fügen Sie Folgendes in die Datei `Info.plist` Ihrer App ein:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

## URL-Kodierung

Das SDK kodiert Links in Prozent, um gültige `URL`s zu erstellen. Alle Link-Zeichen, die in einer korrekt geformten URL nicht zulässig sind, wie z. B. Unicode-Zeichen, werden in Prozent umgewandelt.

Um einen verschlüsselten Link zu dekodieren, verwenden Sie die `String`-Eigenschaft [`removingPercentEncoding`](https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding). Sie müssen auch `true` in `BrazeDelegate.braze(_:shouldOpenURL:)` eingeben. Um die Verarbeitung der URL durch Ihre App zu triggern, ist ein Aufruf zur Aktion erforderlich. 

Zum Beispiel:

{% tabs %}
{% tab schnell %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = [url.absoluteString stringByRemovingPercentEncoding];
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% endtabs %}


## Deeplinking zu App-Einstellungen

Sie können `UIApplicationOpenSettingsURLString` nutzen, um Nutzer:innen von Push-Benachrichtigungen, In-App-Nachrichten und dem Newsfeed aus Deeplinks zu den Einstellungen Ihrer App zu setzen.

Um Nutzer aus Ihrer App in die iOS-Einstellungen zu bringen:
1. Vergewissern Sie sich zunächst, dass Ihre Anwendung entweder für [schema-basierte Deeplinks](##step-1-registering-a-scheme) oder für [universelle Links](#universal-links) eingerichtet ist.
2. Legen Sie eine URI für Deeplinks auf die Seite **Einstellungen** fest (z.B. `myapp://settings` oder `https://www.braze.com/settings`).
3. Wenn Sie angepasste schemabasierte Deeplinks verwenden, fügen Sie den folgenden Code zu Ihrer `application:openURL:options:`-Methode hinzu:

{% tabs %}
{% tab schnell %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplication.openSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
  NSString *path  = [url path];
  if ([path isEqualToString:@"settings"]) {
    NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
    [[UIApplication sharedApplication] openURL:settingsURL];
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Anpassung {#linking-customization}

### Standard WebView-Anpassung

Die Klasse `Braze.WebViewController` zeigt vom SDK geöffnete Internet-URLs an, typischerweise wenn für einen Deeplink "Web-URL in der App öffnen" ausgewählt wurde.

Sie können den `Braze.WebViewController` über die Detegatmethode [`BrazeDelegate.braze(_:willPresentModalWithContext:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:willpresentmodalwithcontext:)-12sqy/) anpassen.

### Anpassung der Link-Handhabung

Mit dem Protokoll `BrazeDelegate` können Sie die Handhabung von URLs wie Deeplinks, Web-URLs und universellen Links anpassen. Um den Delegaten während der Initialisierung von Braze zu setzen, setzen Sie ein Delegatobjekt auf die Instanz `Braze`. Braze ruft dann die Implementierung von `shouldOpenURL` in Ihrem Delegaten auf, bevor es URIs verarbeitet.

#### Universelle Links

Braze unterstützt universelle Links in Push-Benachrichtigungen, In-App-Nachrichten und Content-Cards. Um die Unterstützung für universelle Links zu aktivieren, muss [`configuration.forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) auf `true` gesetzt sein.

Wenn diese Funktion aktiviert ist, leitet Braze universelle Links über die `AppDelegate` Methode an Ihre App weiter. [`application:continueUserActivity:restorationHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) Methode. 

Ihre Anwendung muss auch für den Umgang mit universellen Links eingerichtet sein. Lesen Sie die [Dokumentation von Apple](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app), um sicherzustellen, dass Ihre Anwendung korrekt für universelle Links konfiguriert ist.

{% alert warning %}
Die universelle Linkweiterleitung erfordert den Zugriff auf die Anwendungsberechtigungen. Wenn Sie die Anwendung in einem Simulator ausführen, sind diese Berechtigungen nicht direkt verfügbar und universelle Links werden nicht an die System-Handler weitergeleitet.
Um die Unterstützung für Simulator-Builds hinzuzufügen, können Sie die Datei `.entitlements` in der Build-Phase _Copy Bundle Resources_ hinzufügen. Siehe die Dokumentation zu [`forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) für weitere Details.
{% endalert %}

{% alert note %}
Das SDK fragt die `apple-app-site-association`-Datei Ihrer Domain nicht ab. Es unterscheidet zwischen universellen Links und normalen URLs, indem es nur den Domain-Namen betrachtet. Infolgedessen beachtet das SDK keine Ausschlussregel, die in der `apple-app-site-association` pro [unterstützenden zugehörigen Domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains) definiert ist.
{% endalert %}

### Beispiel für die Integration: BrazeDelegate

{% tabs %}
{% tab schnell %}

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if context.url.host == "MY-DOMAIN.com" {
    // Custom handle link here
    return false
  }
  // Let Braze handle links otherwise
  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}
```

{% endtab %}
{% endtabs %}

Für weitere Informationen siehe [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate).


