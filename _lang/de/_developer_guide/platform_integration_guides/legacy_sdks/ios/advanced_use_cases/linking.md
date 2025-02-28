---
nav_title: Deeplinking
article_title: Deeplinking für iOS
platform: iOS
page_order: 0
description: "In diesem Artikel erfahren Sie, wie Sie den universellen Deeplink-Delegaten für Ihre iOS App implementieren und wie Sie Deeplinks zu App-Einstellungen oder einem Newsfeed setzen."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Deeplinks setzen für iOS

Einführende Informationen zu Deeplinks setzen finden Sie in unserem [Artikel im Benutzerhandbuch]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking). Wenn Sie zum ersten Mal Deeplinks in Ihre Braze-App setzen möchten, können Sie mit den folgenden Schritten beginnen.

{% alert note %}
Dieser Artikel enthält Informationen zum News Feed, der nicht mehr verwendet wird. Braze empfiehlt Kunden, die unser News Feed-Tool verwenden, auf unseren Nachrichtenkanal Content Cards umzusteigen - er ist flexibler, anpassbarer und zuverlässiger. Weitere Informationen finden Sie im [Migrationsleitfaden]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Schritt 1: Ein Schema registrieren

Sie müssen ein angepasstes Schema in der Datei `Info.plist` angeben. Die Navigationsstruktur wird durch eine Reihe von Wörterbüchern definiert. Jedes dieser Wörterbücher enthält ein String-Array mit Strings.

Verwenden Sie Xcode, um Ihre `Info.plist`-Datei zu bearbeiten:

1. Fügen Sie einen neuen Schlüssel hinzu, `URL types`. Xcode macht daraus automatisch ein Array, das ein Wörterbuch namens `Item 0` enthält.
2. Fügen Sie innerhalb von `Item 0` einen Schlüssel `URL identifier` hinzu. Stellen Sie den Wert auf Ihr angepasstes Schema ein.
3. Fügen Sie innerhalb von `Item 0` einen Schlüssel `URL Schemes` hinzu. Dies wird automatisch ein Array sein, das einen `Item 0`-String enthält.
4. Stellen Sie `URL Schemes` >> `Item 0` auf Ihr angepasstes Schema ein.

Wenn Sie Ihre `Info.plist`-Datei  direkt bearbeiten möchten, können Sie auch dieser Spezifikation folgen:

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>{YOUR.SCHEME}</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>{YOUR.SCHEME}</string>
        </array>
    </dict>
</array>
```

## Schritt 2: Angepasstes Schema in die Allowlist eintragen (iOS 9+)

Ab iOS 9 müssen Apps eine Liste mit angepassten Schemata haben, die die App öffnen darf. Der Versuch, Schemata außerhalb dieser Liste aufzurufen, führt dazu, dass das System einen Fehler in den Protokollen des Geräts aufzeichnet und der Deeplink nicht geöffnet werden kann. Ein Beispiel für diesen Fehler sieht so aus:

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Wenn zum Beispiel eine In-App-Nachricht beim Antippen die Facebook-App öffnen soll, muss die App das angepasste Schema von Facebook (`fb`) in der Erlaubnisliste haben. Andernfalls wird das System den Deeplink ablehnen. Deeplinks, die auf eine Seite oder Ansicht innerhalb Ihrer eigenen App verweisen, erfordern nach wie vor, dass das angepasste Schema Ihrer App unter `Info.plist` aufgeführt ist.

Sie müssen alle Schemas, auf die die App Deeplinks setzen muss, in einer Alllowlist in der `Info.plist`-Datei Ihrer App mit dem Schlüssel `LSApplicationQueriesSchemes` auflisten. Zum Beispiel:

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>facebook</string>
    <string>twitter</string>
</array>
```

Weitere Informationen finden Sie in der [Dokumentation von Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) über die Taste `LSApplicationQueriesSchemes`.

## Schritt 3: Handler implementieren

Nachdem Sie die App aktiviert haben, ruft iOS die Methode [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc) auf. Das wichtige Argument ist das [NSURL-Objekt](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL).

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Here you should insert code to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% tab schnell %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Here you should insert code to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% endtabs %}

![]({% image_buster /assets/img_archive/deep_link.png %})

# Universelle Links

Um universelle Links zu verwenden, stellen Sie sicher, dass Sie eine registrierte Domain zu den Fähigkeiten Ihrer App hinzugefügt und eine `apple-app-site-association`-Datei hochgeladen haben. Dann implementieren Sie die Methode `application:continueUserActivity:restorationHandler:` in Ihrer `AppDelegate`. Zum Beispiel:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application
continueUserActivity:(NSUserActivity *)userActivity
  restorationHandler:(void (^)(NSArray *restorableObjects))restorationHandler {
  if ([userActivity.activityType isEqualToString:NSUserActivityTypeBrowsingWeb]) {
    NSURL *url = userActivity.webpageURL;
    // Handle url
  }
  return YES;
}
```

{% endtab %}
{% tab schnell %}

```swift
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  if (userActivity.activityType == NSUserActivityTypeBrowsingWeb) {
    let url = userActivity.webpageURL
    // Handle url
  }
  return true
}
```

{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie bei [Apple](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html).

{% alert note %}
Die Standard Universal Link Integration ist nicht mit Push-Benachrichtigungen, In-App-Nachrichten oder Newsfeed von Braze kompatibel. Sehen Sie in der Beschreibung der [Link-Anpassung](#linking-handling-customization) nach, wie Sie universelle Links innerhalb Ihrer Anwendung handhaben. Alternativ empfehlen wir Ihnen, [schema-basierte Deeplinks](#step-1-registering-a-scheme) mit Push-Benachrichtigungen, In-App-Nachrichten und dem Newsfeed zu setzen.
{% endalert%}

## App Transport Security (ATS)
Mit iOS 9 wurde eine wichtige Änderung eingeführt, die sich auf Web-URLs auswirkt, die in In-App-Nachrichten, Newsfeed-Karten und Push-Benachrichtigungen eingebettet sind.

### ATS-Anforderungen
Aus der [Dokumentation von Apple:](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14) "App Transport Security" ist ein Feature, das die Sicherheit der Verbindungen zwischen einer App und Internet Serviceleistungen; Diensten verbessert. Das Feature besteht aus Standard-Verbindungsanforderungen, die den Best Practices für sichere Verbindungen entsprechen. Apps können dieses Standardverhalten außer Kraft setzen und die Transportsicherheit deaktivieren."

ATS wird standardmäßig auf iOS 9+ angewendet. Es erfordert, dass alle Verbindungen HTTPS verwenden und mit TLS 1.2 mit Forward Secrecy verschlüsselt werden. Weitere Informationen finden Sie unter [Voraussetzungen für die Verbindung mit ATS](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35). Alle Bilder, die von Braze an Endgeräte geliefert werden, werden von einem Content Delivery Network ("CDN") verarbeitet, das TLS 1.2 unterstützt und mit ATS kompatibel ist.

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

#### Bestätigen Sie, dass alle Links ATS-konform sind (empfohlen)
Ihre Integration in Braze kann die ATS-Anforderungen erfüllen, indem Sie sicherstellen, dass alle bestehenden Links, zu denen Sie Nutzer:innen führen (durch In-App-Nachrichten und Push-Kampagnen oder Newsfeed-Karten), die ATS-Anforderungen erfüllen. Es gibt zwar Möglichkeiten, die ATS-Beschränkungen zu umgehen, aber wir empfehlen zu überprüfen, ob alle verlinkten URLs ATS-konform sind. Da Apple immer mehr Wert auf die Sicherheit von Anwendungen legt, werden die folgenden Ansätze zur Zulassung von ATS-Ausnahmen von Apple nicht garantiert unterstützt.

Ein SSL-Tool kann Ihnen dabei helfen, Sicherheitsprobleme des Internetservers zu erkennen. Dieser [SSL-Server-Test](https://www.ssllabs.com/ssltest/index.html) von Qualys, Inc. bietet einen Punkt speziell für die Einhaltung von Apple ATS 9 und iOS 9.

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

Weitere Informationen zum Debuggen von ATS-Fehlern finden Sie unter [Versand einer App mit App-Transport-Sicherheit](http://timekl.com/blog/2015/08/21/shipping-an-app-with-app-transport-security/?utm_campaign=iOS+Dev+Weekly&utm_medium=email&utm_source=iOS_Dev_Weekly_Issue_213).

## URL-Kodierung

Ab Braze iOS SDK v2.21.0 kodiert das SDK Links in Prozent, um gültige `NSURL`s zu erstellen. Alle Link-Zeichen, die in einer korrekt geformten URL nicht zulässig sind, wie z. B. Unicode-Zeichen, werden in Prozent umgewandelt.

Um einen verschlüsselten Link zu dekodieren, verwenden Sie die Methode `NSString` [`stringByRemovingPercentEncoding`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/index.html#//apple_ref/occ/instm/NSString/stringByRemovingPercentEncoding). Beachten Sie, dass Sie in `ABKURLDelegate` auch `YES` zurückgeben müssen und dass ein Aufruf zur Aktion erforderlich ist, um die Verarbeitung der URL durch die App zu triggern. Zum Beispiel:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% tab schnell %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% endtabs %}

## Anpassung {#linking-customization}

### Standard WebView-Anpassung

Die anpassbare Klasse `ABKModalWebViewController` zeigt Internet-URLs an, die vom SDK geöffnet wurden, typischerweise wenn "Web-URL in App öffnen" für einen Web-Deeplink ausgewählt wurde.

Sie können eine Kategorie für die Klasse `ABKModalWebViewController` deklarieren oder sie direkt ändern, um die Webansicht anzupassen. Prüfen Sie die [.h-Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKModalWebViewController.h) und die [.m-Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/ABKModalWebViewController.m) der Klasse für weitere Details.

### Anpassung der Link-Handhabung

Mit dem Protokoll `ABKURLDelegate` können Sie die Handhabung von URLs wie Deeplinks, Web-URLs und universellen Links anpassen. Um den Delegaten während der Initialisierung von Braze zu setzen, übergeben Sie ein Delegaten-Objekt an den `ABKURLDelegateKey` in `appboyOptions` von [`startWithApiKey:inApplication:withAppboyOptions:`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). Braze ruft dann die Implementierung von `handleAppboyURL:fromChannel:withExtras:` in Ihrem Delegaten auf, bevor es URIs verarbeitet.

#### Beispiel für die Integration: ABKURLDelegate

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)handleAppboyURL:(NSURL *)url fromChannel:(ABKChannel)channel withExtras:(NSDictionary *)extras {
  if ([[url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return YES;
  }
  // Let Braze handle links otherwise
  return NO;
}
```

{% endtab %}
{% tab schnell %}

```swift
func handleAppboyURL(_ url: URL?, from channel: ABKChannel, withExtras extras: [AnyHashable : Any]?) -> Bool {
  if (url.host == "MY-DOMAIN.com") {
    // Custom handle link here
    return true;
  }
  // Let Braze handle links otherwise
  return false;
}
```

{% endtab %}
{% endtabs %}

Für weitere Informationen siehe [`ABKURLDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKURLDelegate.h).

## Häufig vorkommende Anwendungsfälle

### Deeplinks zu den App-Einstellungen setzen

iOS kann Nutzer:innen von Ihrer App auf deren Seite in der iOS-Einstellungsanwendung führen. Sie können `UIApplicationOpenSettingsURLString` nutzen, um Nutzer über Deeplinks mit Einstellungen aus Push-Benachrichtigungen, In-App-Nachrichten und dem Newsfeed zu verknüpfen.

1. Vergewissern Sie sich zunächst, dass Ihre Anwendung entweder für [schema-basierte Deeplinks](#deep-links) oder für [universelle Links](#universal-links) eingerichtet ist.
2. Legen Sie eine URI für Deeplinks auf die Seite **Einstellungen** fest (z.B. `myapp://settings` oder `https://www.braze.com/settings`).
3. Wenn Sie angepasste schemabasierte Deeplinks verwenden, fügen Sie den folgenden Code zu Ihrer `application:openURL:options:`-Methode hinzu:

{% tabs %}
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
{% tab schnell %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplicationOpenSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
{% endtabs %}

