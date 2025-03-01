---
nav_title: SDK-Integrationsleitfaden (optional)
article_title: Braze SDK-Integrationsanleitung für iOS (optional)
alias: "/ios_sdk/"
description: "Dieser Leitfaden zur iOS-Integration führt Sie Schritt für Schritt durch die bewährten Verfahren bei der ersten Integration des iOS SDK und seiner Kernkomponenten in Ihre Anwendung. Diese Anleitung hilft Ihnen, eine BrazeManager.swift-Hilfsdatei zu erstellen."
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Braze iOS SDK-Integration Anleitung

> Dieser Leitfaden zur optionalen iOS-Integration führt Sie Schritt für Schritt durch die bewährten Verfahren bei der ersten Integration des iOS SDK und seiner Kernkomponenten in Ihre Anwendung. Diese Anleitung hilft Ihnen bei der Erstellung einer `BrazeManager.swift`-Hilfsdatei, die alle Abhängigkeiten vom Braze iOS SDK vom Rest Ihres produktiven Codes entkoppelt, was eine gemeinsamen `import AppboyUI` in Ihrer gesamten Anwendung bewirkt. Dieser Ansatz vermeidet Probleme, die durch übermäßige SDK-Importe entstehen, und erleichtert das Tracking, Debugging und Ändern von Code. 

{% alert important %}
Diese Anleitung geht davon aus, dass Sie das [SDK bereits zu Ihrem Xcode-Projekt hinzugefügt]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) haben.
{% endalert %}

## Überblick über die Integration

Die folgenden Schritte helfen Ihnen bei der Erstellung einer `BrazeManager`-Hilfsdatei, die Ihr Produktionscode aufruft. Diese Hilfedatei kümmert sich um alle Braze-bezogenen Abhängigkeiten, indem sie verschiedene Erweiterungen für die nachfolgend aufgeführten Integrationsthemen hinzufügt. Jedes Thema enthält horizontale Tab-Schritte und Code-Snippets sowohl in Swift als auch in Objective-C. Beachten Sie, dass die Schritte Content-Card und In-App-Nachricht für die Integration nicht erforderlich sind, wenn Sie nicht vorhaben, diese Kanäle in Ihrer Anwendung zu verwenden.

- [Erstellen Sie BrazeManager.swift](#create-brazemanagerswift)
- [Initialisieren Sie das SDK](#initialize-the-sdk)
- [Push-Benachrichtigungen](#push-notifications)
- [Zugriff auf Nutzer:in-Variablen und -Methoden](#access-user-variables-and-methods)
- [Log-Analytics](#log-analytics)
- [In-App-Nachrichten (optional)](#in-app-messages)
- [Content-Cards (optional)](#content-cards)
- [Nächste Schritte](#next-steps)

### BrazeManager.swift erstellen

{% tabs local %}
{% tab BrazeManager swift erstellen %}

##### BrazeManager.swift erstellen
Um Ihre `BrazeManager.swift` Datei zu erstellen, erstellen Sie eine neue Swift-Datei mit dem Namen _BrazeManager_, die Sie an dem von Ihnen gewünschten Standort zu Ihrem Projekt hinzufügen. Als Nächstes ersetzen Sie `import Foundation` durch `import AppboyUI` für SPM (`import Appboy_iOS_SDK` für CocoaPods) und erstellen dann eine Klasse `BrazeManager`, die als Host für alle Braze-bezogenen Methoden und Variablen dienen wird. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` ist eine Klasse `NSObject` und keine Struktur, sodass sie mit ABK-Delegaten wie `ABKInAppMessageUIDelegate` konform gehen kann.
- `BrazeManager` ist eine Singleton-Klasse, sodass nur eine Instanz dieser Klasse verwendet wird. Dies geschieht, um einen einheitlichen Zugriffspunkt auf das Objekt zu schaffen.
{% endalert %} 

1. Fügen Sie eine statische Variable namens _shared_ hinzu, die die Klasse `BrazeManager` initialisiert. Dieser Vorgang wird garantiert nur einmal ausgelöst.
2. Als Nächstes fügen Sie eine private konstante Variable namens _apiKey_ hinzu und setzen sie als API-Schlüsselwert aus Ihrem Workspace im Braze-Dashboard ein.
3. Fügen Sie eine private berechnete Variable namens _appboyOptions_ hinzu, die Konfigurationswerte für das SDK speichern wird. Es wird vorerst leer sein.

{% subtabs global %}
{% subtab Swift %}

```swift
class BrazeManager: NSObject {
  // 1
  static let shared = BrazeManager()
  
  // 2
  private let apikey = "YOUR-API-KEY"
  
  // 3
  private var appboyOptions: [String:Any] {
    return [:]
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation BrazeManager
 
// 1
+ (instancetype)shared {
    static BrazeManager *shared = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        shared = [[BrazeManager alloc] init];
        // Do any other initialisation stuff here
    });
    return shared;
}
 
// 2
- (NSString *)apiKey {
  return @"YOUR-API-KEY";
}
 
// 3
- (NSDictionary *)appboyOptions {
  return [NSDictionary dictionary];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Initialisieren Sie das SDK

{% tabs local %}
{% tab Schritt 1: Initialize SDK from BrazeManager swift %}

##### SDK von BrazeManager.swift aus initialisieren
Als nächstes müssen Sie das SDK initialisieren. Diese Anleitung geht davon aus, dass Sie das [SDK bereits zu Ihrem Xcode-Projekt hinzugefügt]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) haben. Sie müssen auch Ihren [Workspace SDK-Endpunkt]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/#step-2-specify-your-data-cluster) und [`LogLevel`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#braze-log-level) in der Datei `Info.plist` oder in `appboyOptions` festgelegt haben.

Fügen Sie die Methode `didFinishLaunchingWithOptions` aus der Datei `AppDelegate.swift` ohne einen Rückgabetyp in Ihre Datei `BrazeManager.swift` ein. Wenn Sie eine ähnliche Methode in der Datei `BrazeManager.swift` erstellen, wird es in Ihrer Datei `AppDelegate.swift` keine Anweisung `import AppboyUI` geben. 

Als Nächstes initialisieren Sie das SDK mit Ihren neu deklarierten Variablen `apiKey` und `appboyOptions`.

{% alert important %}
Die Initialisierung muss im Haupt-Thread durchgeführt werden.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Schritt 2: Handle Appboy Initialization %}

##### Appboy-Initialisierung in AppDelegate.swift behandeln
Gehen Sie nun zurück zur Datei `AppDelegate.swift` und fügen Sie den folgenden Code-Snippet in die Methode `didFinishLaunchingWithOptions` von AppDelegate ein, um die Initialisierung von Appboy aus der Hilfedatei `BrazeManager.swift` zu verarbeiten. Denken Sie daran, dass es nicht notwendig ist, eine Anweisung `import AppboyUI` in `AppDelegate.swift` hinzuzufügen.

{% subtabs global %}
{% subtab Swift %}

```swift
func application(
  _ application: UIApplication, 
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Override point for customization after application launch
 
  [[BrazeManager shared] application:application didFinishLaunchingWithOptions:launchOptions];
   
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Fahren Sie mit der Kompilierung Ihres Codes fort und führen Sie Ihre Anwendung aus.<br><br>Jetzt sollte das SDK betriebsbereit sein. Vergewissern Sie sich in Ihrem Dashboard, dass die Sitzungen protokolliert werden, bevor Sie fortfahren.
{% endalert %}

### Push-Benachrichtigungen

{% tabs local %}
{% tab Schritt 1: Push-Zertifikat hinzufügen %}

##### Push-Zertifikat hinzufügen

Navigieren Sie zu Ihrem bestehenden Workspace im Braze-Dashboard. Laden Sie unter **Einstellungen für Push-Benachrichtigungen** Ihre Push-Zertifikatsdatei auf Ihr Braze-Dashboard hoch und speichern Sie sie. 

![]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Schritt 2: Für Benachrichtigungen registrieren %}

{% alert important %}
Verpassen Sie nicht den speziellen Kontrollpunkt am Ende dieses Schritts!
{% endalert %}

##### Für Push-Benachrichtigungen registrieren

Als nächstes registrieren Sie sich für Push-Benachrichtigungen. Diese Anleitung setzt voraus, dass Sie in Ihrem Apple-Entwicklerportal und Ihrem Xcode-Projekt die [Push-Zugangsdaten korrekt eingerichtet]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) haben. 

Der Code für die Registrierung von Push-Benachrichtigungen wird in der Methode `didFinishLaunching...` in der Datei `BrazeManager.swift` hinzugefügt. Ihr Code zur Initialisierung sollte am Ende wie folgt aussehen:

1. Konfigurieren Sie die Inhalte für die Anfrage zur Autorisierung der Interaktion mit dem Nutzer:innen. Diese Optionen sind als Beispiel aufgeführt.
2. Fordern Sie die Genehmigung zum Senden von Push-Benachrichtigungen an Ihre Nutzer an. Die Antwort Ihres Nutzers (Push-Benachrichtigungen zulassen oder ablehnen) wird in der Variable `granted` getrackt.
3. Leiten Sie die Ergebnisse der Push-Autorisierung an Braze weiter, nachdem der Nutzer mit der Benachrichtigungsaufforderung interagiert hat.
4. Starten Sie den Registrierungsprozess mit APNs; dies muss im Hauptthread geschehen. Wenn die Registrierung erfolgreich ist, ruft die App im Objekt `AppDelegate` die Methode `didRegisterForRemoteNotificationsWithDeviceToken` auf. 

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?) {
  Appboy.start(withAPIKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
  // 1 
  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  // 2 
  UNUserNotificationCenter.current().requestAuthorization(option: options) { (granted, error) in
  // 3 
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  
  // 4 
  UIApplications.shared.registerForRemoteNotificiations()
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
   
  // 1
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
   
  // 2
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
  // 3
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
 
  // 4
  [[UIApplication sharedApplication] registerForRemoteNotifications];
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert checkpoint %}
Fahren Sie mit der Kompilierung Ihres Codes fort und führen Sie Ihre Anwendung aus.
- Bestätigen Sie in Ihrer App, dass Sie zu Push-Benachrichtigungen aufgefordert werden, bevor Sie weitere Fortschritte machen.
- Wenn Sie nicht dazu aufgefordert werden, versuchen Sie, die App zu löschen und neu zu installieren, um sicherzustellen, dass die Aufforderung zur Push-Benachrichtigung zuvor nicht angezeigt wurde.

Beachten Sie, dass Sie aufgefordert werden, Push-Benachrichtigungen anzufordern, bevor Sie fortfahren.
{% endalert %}

{% endtab %}
{% tab Schritt 3: Methoden weiterleiten %}

##### Methoden für Push-Benachrichtigungen weiterleiten

Als Nächstes leiten Sie die Methoden für Push-Benachrichtigungen des Systems von `AppDelegate.swift` an `BrazeManager.swift` weiter, damit sie vom Braze iOS SDK verarbeitet werden können.

###### Schritt 1: Erweiterung für den Code der Push-Benachrichtigung erstellen

Erstellen Sie eine Erweiterung für Ihren Code für Push-Benachrichtigungen in `BrazeManager.swift`, damit Sie besser erkennen können, welchem Zweck die Hilfsdatei dient, etwa so:

1. Nach dem Muster, dass Sie keine Anweisung `import AppboyUI` in Ihre `AppDelegate` einfügen, werden wir die Methoden für Push-Benachrichtigungen also in `BrazeManager.swift` behandeln. Die Token für die Geräte der Nutzer:innen müssen von der Methode `didRegisterForRemote...` an Braze übergeben werden. Diese Methode ist erforderlich, um stille Push-Benachrichtigungen zu implementieren. Als Nächstes fügen Sie die gleiche Methode aus `AppDelegate` in Ihre -`BrazeManager`-Klasse ein.
2. Fügen Sie die folgende Zeile innerhalb der Methode hinzu, um das Token des Geräts in Braze zu registrieren. Dies ist notwendig, damit Braze das Token mit dem aktuellen Gerät verknüpfen kann. 

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK - Push Notifications
extension BrazeManager {
  // 1 
  func application(
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
  ) {
    // 2 
    Appboy.sharedInstance().?registerDeviceToken(deviceToken)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK - Push Notifications
// 1
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  // 2
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}
```
{% endsubtab %}
{% endsubtabs %}

###### Schritt 2: Fernbenachrichtigungen unterstützen
Fügen Sie auf dem Tab **Signieren & Fähigkeiten** die Unterstützung von **Hintergrundmodi** hinzu und wählen Sie **Remote-Benachrichtigungen** aus, um mit der Unterstützung von Push-Benachrichtigungen aus der Ferne zu beginnen, die von Braze stammen.<br><br>![Signing & Capabilities]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### Schritt 3: Handhabung von Fernbenachrichtigungen
Das Braze SDK kann Push-Benachrichtigungen aus der Ferne verarbeiten, die von Braze stammen. Leiten Sie Fernbenachrichtigungen an Braze weiter. Push-Benachrichtigungen, die nicht von Braze stammen, werden vom SDK automatisch ignoriert. Fügen Sie in der Erweiterung für Push-Benachrichtigungen die folgende Methode zu `BrazeManager.swift` hinzu.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication, 
  didReceiveRemoteNotification userInfo: [AnyHashable : Any], 
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  Appboy.sharedInstance()?.register(
    application, 
    didReceiveRemoteNotification: userInfo, 
    fetchCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application didReceiveRemoteNotification:userInfo fetchCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}

###### Schritt 4: Antworten auf Benachrichtigungen weiterleiten

Das Braze SDK kann die Antwort auf Push-Benachrichtigungen verarbeiten, die von Braze stammen. Leiten Sie die Antwort der Push-Benachrichtigungen an Braze weiter. Das SDK ignoriert automatisch Antworten von Push-Benachrichtigungen, die nicht von Braze stammen. Fügen Sie die folgende Methode in Ihre `BrazeManager.swift` Datei ein:

{% subtabs global %}
{% subtab Swift %}

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter, 
  didReceive response: UNNotificationResponse, 
  withCompletionHandler completionHandler: @escaping () -> Void
) {
  Appboy.sharedInstance()?.userNotificationCenter(
    center, 
    didReceive: response, 
    withCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response 
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center 
                   didReceiveNotificationResponse:response 
                            withCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Fahren Sie mit der Kompilierung Ihres Codes fort und führen Sie Ihre Anwendung aus. <br><br>Versuchen Sie, sich selbst eine Push-Benachrichtigung vom Braze-Dashboard aus zu senden, und beobachten Sie, ob die Analytics von den Push-Benachrichtigungen protokolliert werden, bevor Sie weitere Fortschritte machen.
{% endalert %}

### Zugriff auf Nutzer:in-Variablen und -Methoden

{% tabs local %}
{% tab Nutzer:in-Variablen und -Methoden erstellen %}

##### Erstellen Sie Nutzer:in-Variablen und -Methoden

Als Nächstes benötigen Sie einfachen Zugriff auf die Variablen und Methoden von `ABKUser`. Erstellen Sie eine Erweiterung für Ihren Nutzercode in `BrazeManager.swift`, damit Sie besser erkennen können, welchem Zweck die Hilfsdatei dient, etwa so:

1. Ein `ABKUser` Objekt repräsentiert einen bekannten oder anonymen Nutzer:in in Ihrer iOS-Anwendung. Fügen Sie eine berechnete Variable hinzu, um die `ABKUser` abzurufen. Diese Variable wird wiederverwendet, um Variablen über den Nutzer:innen abzurufen.
2. Fragen Sie die Nutzervariable ab, um einfach auf die `userId` zugreifen zu können. Unter den anderen Variablen ist das Objekt `ABKUser` verantwortlich für (`firstName`, `lastName`, `phone`, `homeCity` usw.)
3. Legen Sie den Nutzer fest, indem Sie `changeUser()` mit einem entsprechenden `userId` aufrufen.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK: - User
extension BrazeManager {
  // 1
  var user: ABKUser? {
    return Appboy.sharedInstance()?.user
  }

  // 2 
  var userId: String? {
    return user?.userID
  }

  // 3
  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - User
  // 1
- (ABKUser *)user {
  return [[Appboy sharedInstance] user];
}
   
   // 2 
- (NSString *)userId {
  return [self user].userID;
}
 
  // 3
- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser:userId];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Fahren Sie mit der Kompilierung Ihres Codes fort und führen Sie Ihre Anwendung aus.<br><br>Versuchen Sie, Nutzer:innen anhand einer erfolgreichen Registrierung zu identifizieren. Vergewissern Sie sich, dass Sie genau wissen, was ein geeigneter Nutzer ist und was nicht. <br><br>Achten Sie in Ihrem Dashboard darauf, dass der Bezeichner des Nutzers protokolliert wird, bevor Sie fortfahren.
{% endalert %} 

### Log-Analytics

{% tabs local %}
{% tab Schritt 1: Angepasste Events %}

##### Angepasste Event-Methode für das Protokoll erstellen

Erstellen Sie auf der Grundlage der folgenden `logCustomEvent`- Methode des Braze SDK eine passende Methode. 

**Referenzierte Braze-Methode `logCustomEvent`**<br>
Das ist so gewollt, denn nur die Datei `BrazeManager.swift` kann direkt auf die Methoden des Braze iOS SDK zugreifen. Wenn Sie also eine passende Methode erstellen, ist das Ergebnis dasselbe und Sie brauchen keine direkten Abhängigkeiten vom Braze iOS SDK in Ihrem Produktionscode.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**Matching-Methode**<br>
Protokolliert angepasste Events vom Objekt `Appboy` in Braze. `Properties` ist ein optionaler Parameter mit dem Standardwert Null. Angepasste Events müssen keine Eigenschaften haben, aber einen Namen. 

{% subtabs global %}
{% subtab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(nullable NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:properties];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Schritt 2: Angepasste Attribute %}

##### Methode zur Erstellung angepasster Attribute für das Protokoll 

Das SDK kann zahlreiche Typen als angepasste Attribute protokollieren. Es ist nicht notwendig, Hilfsmethoden für jeden Werttyp zu erstellen, der gesetzt werden kann. Stellen Sie stattdessen nur eine Methode zur Verfügung, mit der Sie auf den entsprechenden Wert filtern können.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

Angepasste Attribute werden über das Objekt `ABKUser` protokolliert. 

Erstellen Sie **eine Methode**, die alle verfügbaren Typen, die für ein Attribut festgelegt werden können, umfasst. Fügen Sie diese Methode in Ihrer `BrazeManager.swift`-Datei in der Analytics Erweiterung hinzu. Dazu filtern Sie die gültigen angepassten Attribut-Typen und rufen die mit dem passenden Typ verbundene Methode auf.

- Der Parameter `value` ist ein generischer Typ, der dem Protokoll `Equatable` entspricht. Dies geschieht explizit. Wenn der Typ nicht dem entspricht, den das Braze iOS SDK erwartet, wird ein Kompilierungsfehler ausgegeben.
- Die Parameter `key` und `value` sind optionale Parameter, die in der Methode bedingungslos ausgepackt werden. Das ist nur eine Möglichkeit, um sicherzustellen, dass keine Nullwerte an das Braze iOS SDK übergeben werden.

{% subtabs global %}
{% subtab Swift %}

```swift
func setCustomAttributeWithKey<T: Equatable>(_ key: String?, andValue value: T?) {
  guard let key = key, let value = value else { return }
  switch value.self {
  case let value as Date:
    user?.setCustomAttributeWithKey(key, andDateValue: value)
  case let value as Bool:
    user?.setCustomAttributeWithKey(key, andBOOLValue: value)
  case let value as String:
    user?.setCustomAttributeWithKey(key, andStringValue: value)
  case let value as Double:
    user?.setCustomAttributeWithKey(key, andDoubleValue: value)
  case let value as Int:
    user?.setCustomAttributeWithKey(key, andIntegerValue: value)
  default:
   return
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)setCustomAttributeWith:(NSString *)key andValue:(id)value {
  if ([value isKindOfClass:[NSDate class]]) {
    [[self user] setCustomAttributeWithKey:key andDateValue:value];
  } else if ([value isKindOfClass:[NSString class]]) {
    [[self user] setCustomAttributeWithKey:key andStringValue:value];
  } else if ([value isKindOfClass:[NSNumber class]]) {
    if (strcmp([value objCType], @encode(double)) == 0) {
      [[self user] setCustomAttributeWithKey:key andDoubleValue:[value doubleValue]];
    } else if (strcmp([value objCType], @encode(int)) == 0) {
      [[self user] setCustomAttributeWithKey:key andIntegerValue:[value integerValue]];
    } else if ([value boolValue]) {
      [[self user] setCustomAttributeWithKey:key andBOOLValue:[value boolValue]];
    }
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Schritt 3: Käufe %}

##### Methode zur Protokollierung von Käufen erstellen

Als Nächstes erstellen Sie auf der Grundlage der Braze-SDK-Methode `logPurchase` eine Matching-Methode. 

**Referenzierte Braze-Methode `logPurchase`**<br>
Das ist so gewollt, denn nur die Datei `BrazeManager.swift` kann direkt auf die Methoden des Braze iOS SDK zugreifen. Wenn Sie also eine passende Methode erstellen, ist das Ergebnis dasselbe und Sie brauchen keine direkten Abhängigkeiten vom Braze iOS SDK in Ihrem Produktionscode. 

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**Matching-Methode**<br>
Protokollieren Sie Einkäufe aus dem `Appboy` Objekt in Braze. Das SDK verfügt über mehrere Methoden zur Protokollierung von Käufen, und dies ist nur ein Beispiel. Diese Methode übernimmt auch die Erstellung der Objekte `NSDecimal` und `UInt`. Wie Sie diesen Teil handhaben wollen, bleibt Ihnen überlassen, dies ist nur ein Beispiel.

{% subtabs global %}
{% subtab Swift %}

```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPurchase:(NSString *)productIdentifier inCurrency:(nonnull NSString *)currencyCode atPrice:(nonnull NSDecimalNumber *)price withQuantity:(NSUInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currencyCode atPrice:price withQuantity:quantity];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Fahren Sie mit der Kompilierung Ihres Codes fort und führen Sie Ihre Anwendung aus. <br><br>Versuchen Sie, angepasste Events zu protokollieren.<br><br>Achten Sie in Ihrem Dashboard darauf, dass die angepassten Events protokolliert werden, bevor Sie fortfahren.
{% endalert %}

### In-App-Nachrichten

{% tabs local %}
{% tab Schritt 1: Mit Delegat  %} konform machen

{% alert important %}
Der folgende Abschnitt In-App-Nachricht ist für die Integration nicht erforderlich, wenn Sie diesen Kanal nicht in Ihrer Anwendung verwenden möchten.
{% endalert %}

##### Konform zu ABKInAppMessageUIDelegate

Als Nächstes aktivieren Sie den Code Ihrer `BrazeManager.swift` Datei, sodass er mit `ABKInAppMessageUIDelegate` konform ist und die zugehörigen Methoden direkt verarbeiten kann. 

Der Code für die Anpassung an den Delegaten wird in den `didFinishLaunching...`-Methoden in der Datei `BrazeManager.swift` hinzugefügt. Ihr Code für die Initialisierung sollte am Ende wie folgt aussehen:

{% subtabs global %}
{% subtab swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()

  Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
   
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
   
  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Schritt 2: Delegierte Methoden hinzufügen %}

##### Delegierte Methoden hinzufügen
Als Nächstes erstellen Sie eine Erweiterung, die dem `ABKInAppMessageUIDelegate` entspricht.

Fügen Sie das folgende Snippet dem Abschnitt Analytics hinzu. Beachten Sie, dass das Objekt `BrazeManager.swift` als Delegat festgelegt ist. Hier wird die Datei `BrazeManager.swift` alle `ABKInAppMessageUIDelegate`-Methoden behandeln. 

{% alert important %}
Der `ABKInAppMessageUIDelegate` enthält keine obligatorischen Methoden, aber im Folgenden finden Sie ein Beispiel für eine.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - ABKInAppMessage UI Delegate
extension AppboyManager: ABKInAppMessageUIDelegate{
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return ABKInAppMessageSlideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return ABKInAppMessageFullViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - ABKInAppMessage UI Delegate
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [[ABKInAppMessageSlideupViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [[ABKInAppMessageFullViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  }
  return nil;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Fahren Sie mit der Kompilierung Ihres Codes fort und führen Sie Ihre Anwendung aus. <br><br>Versuchen Sie, sich selbst eine In-App-Nachricht zu schicken. <br><br>Setzen Sie in der Datei `BrazeManager.swift` einen Haltepunkt am Beginn der `ABKInAppMessageUIDelegate`-Beispielmethode. Senden Sie sich selbst eine In-App-Nachricht und bestätigen Sie, dass der Haltepunkt erreicht ist, bevor Sie fortfahren.
{% endalert %}

### Content-Cards

{% tabs local %}
{% tab Content-Card-Variablen und -Methoden erstellen %}

{% alert important %}
Der folgende Content-Card-Abschnitt ist für die Integration nicht erforderlich, wenn Sie nicht vorhaben, diesen Kanal in Ihrer Anwendung zu verwenden.
{% endalert %}

##### Content-Card-Variablen und -Methoden erstellen

Ermöglichen Sie Ihrem Code, den Content-Cards-View-Controller ohne unnötige `import AppboyUI`-Anweisungen anzuzeigen. 

Erstellen Sie eine Erweiterung für Ihren Content-Cards-Code in `BrazeManager.swift`, damit Sie besser erkennen können, welchem Zweck die Hilfsdatei dient, etwa so:

1. Zeigen Sie den `ABKContentCardsTableViewController` an. Ein optionaler `navigationController` ist der einzige Parameter, der benötigt wird, um den View Controller zu präsentieren oder zu pushen.
2. Initialisieren Sie ein `ABKContentCardsTableViewController`-Objekt und ändern Sie optional den Titel. Sie müssen auch den initialisierten View Controller zum Navigations-Stack hinzufügen.

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - Content Cards
extension BrazeManager {

  // 1 
  func displayContentCards(navigationController: UINavigationController?) {
      
    // 2 
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "Content Cards"
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - Content Cards
  // 1
- (void)displayContentCards:(UINavigationController *)navigationController {
  // 2
  ABKContentCardsTableViewController *contentCardsVc = [[ABKContentCardsTableViewController alloc] init];
  contentCardsVc.title = @"Content Cards";
  [navigationController pushViewController:contentCardsVc animated:YES];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Fahren Sie mit der Kompilierung Ihres Codes fort und führen Sie Ihre Anwendung aus.<br><br>Versuchen Sie, den `ABKContentCardsTableViewController` in Ihrer Anwendung anzuzeigen, bevor Sie fortfahren.
{% endalert %}

## Nächste Schritte

Herzlichen Glückwunsch! Sie haben diesen Leitfaden für die Integration von Best Practices abgeschlossen! Ein Beispiel für die `BrazeManager` Helferdatei finden Sie auf [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift).

Jetzt, wo Sie alle Abhängigkeiten vom Braze iOS SDK vom Rest Ihres Codes entkoppelt haben, sollten Sie sich einige unserer optionalen Anleitungen zur erweiterten Implementierung ansehen:
- [Anleitung zur Implementierung von Push-Benachrichtigungen für Fortgeschrittene]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/)
- [Leitfaden zur Implementierung von In-App-Nachrichten für Fortgeschrittene]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/)
- [Handbuch zur erweiterten Implementierung von Content-Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/)

