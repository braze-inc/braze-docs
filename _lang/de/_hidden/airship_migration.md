---
nav_title: SDK-Migration von Airship zu Braze
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# Migrieren von SDKs von Airship zu Braze (iOS)

> Wir bei Braze wissen, dass der Wechsel zu einer völlig neuen Plattform und einem neuen SDK entmutigend sein kann. Aber mit dem folgenden Migrationsleitfaden, den einfachen Beispielen auf Code-Ebene und dem beeindruckenden Funktionsumfang der Braze-Plattform wird Ihnen das sicher nichts ausmachen. In diesem Artikel haben wir das Braze-Äquivalent zu vielen wichtigen Airship-Funktionen sowie "Rip-and-Replace"-SDK-Code-Schnipsel aufgenommen, um Ihre Migration schnell, einfach und schmerzlos zu gestalten.

## Jenseits des Codes
### Token-Verwaltung
Braze verwendet das Gerätetoken von Apple für iOS.

| **Braze Perspective:**<br>Wir stellen sicher, dass Kunden bei der Migration von Airship zu Braze kontinuierlich mit ihren Benutzern kommunizieren können (z. B. durch Push-Benachrichtigungen). Dabei spielt es keine Rolle, ob es sich um einen harten Umstieg auf 100% Braze oder einen granularen Übergang wie 50% Airship 50% Braze usw. handelt. |
{: .reset-td-br-1 role="presentation" }

#### Push-Token-Migration

Sie ist erforderlich, um [Push-Tokens über die API zu migrieren]({{site.baseurl}}/help/help_articles/push/push_token_migration/#migration-via-api). Die verlinkte Dokumentation enthält spezifische Schritte sowie eine Beispiel-Nutzlast, aber der Gesamtprozess ist wie folgt:

1. Importieren Sie die Token über den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Für die Einfuhr großer Mengen haben wir Ressourcen zur Verfügung, um den Prozess zu beschleunigen. Wenden Sie sich an Ihren COM oder SA für weitere Details!
2. Wenn das Token bereits in Braze existiert, wird es ignoriert, andernfalls wird ein anonymes Profil erstellt.
3. Führen Sie die Qualitätssicherung für die Push-Integration durch. Stellen Sie sicher, dass die Schritte zur [Konfiguration von Push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) abgeschlossen sind.

Wenn Ihre Benutzerprofile und Push-Token an verschiedenen Orten gespeichert sind, empfehlen wir, die Push-Token anonym zu importieren und anschließend Ihre bestehenden Benutzerprofile zu migrieren. Es ist nicht notwendig, sie zusammen zu mappen, da das Braze iOS SDK die Token-Auflösung bei erfolgreicher Integration übernimmt.

- Wir empfehlen, Benutzer über die API zu migrieren, aber wenn Sie eine statische Liste von Benutzern importieren müssen, können Sie dies über CSV tun. Beachten Sie, dass **Push-Token nicht über CSV importiert werden können**, da das Objekt "push_token" in der CSV nicht angegeben werden kann. Um eine Importvorlage anzusehen und mehr über den Import von Daten in das Dashboard zu erfahren, lesen Sie unsere [CSV-Dokumentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% alert note %}
Push-Tokens werden im Braze-Dashboard möglicherweise als `subscribed` angezeigt, ändern sich aber in `opted-in`, nachdem Benutzer eine Sitzung mit dem Braze SDK gestartet haben.
{% endalert %}

#### Mehrere Push-Merkmale

Mit Braze kann ein Benutzer mehrere Push-Token haben (einen für jedes Gerät). Indem Sie alle gültigen Push-Token ansprechen, können Sie Benachrichtigungen an mehrere Benutzergeräte senden. Es ist auch möglich, Kampagnen so zu konfigurieren, dass sie nur an das letzte Gerät eines Benutzers gesendet werden.

## Kampagnen-Konfiguration
Braze ist ein wirklich einzigartiges Tool im Bereich der Kundenbindung. Aufgrund unserer umfangreichen Anpassungsmöglichkeiten und des wachsenden Funktionsumfangs profitieren Kampagnen, die nach Braze migriert werden, oft von einer Neuplanung, um die Vorteile dieser Tools zu nutzen. Unser Kampagnenplanungs-Framework (wenden Sie sich an Ihren COM oder SA, um weitere Einzelheiten zu erfahren) ist genau für diesen Zweck entwickelt worden.

### Zusammensetzung
#### Push-Benachrichtigungen
Braze benötigt separate Kanäle für Push (einen für iOS, einen für Android).

| **Braze Perspective:**<br>Wir ermöglichen es unseren Kunden, das Beste aus beiden Welten zu bekommen, anstatt Zugeständnisse machen zu müssen. Die Möglichkeit, den einzelnen Kanal voll auszuschöpfen, bietet dem Vermarkter mehr Flexibilität und ein besseres Nutzererlebnis. Dies ermöglicht es uns, die neuesten Funktionen des jeweiligen Betriebssystems zu übernehmen. So unterstützte Android beispielsweise Rich Notifications vor iOS. |
{: .reset-td-br-1 role="presentation" }

Braze ist in der Lage, Push-Benachrichtigungen an Benutzer zu senden, die ihre Anwendung nicht mit dem installierten Braze SDK aktualisieren. Wenn Braze über ein gültiges Push-Token verfügt, kann Braze die Push-Benachrichtigung ohne das Braze SDK senden, da die APNs den Rest übernehmen. Es ist wichtig zu wissen, dass **die Analyse von** Push-Nachrichten **für Builds ohne das Braze SDK nicht verfügbar ist**.

##### Token teilen

Bei lebenszyklusspezifischen Kampagnen, die während Ihres Migrationsprozesses zum Braze SDK fortgesetzt werden müssen, können Benutzer möglicherweise sowohl von Braze als auch von Airship Benachrichtigungen erhalten, vorausgesetzt, Braze hat ein gültiges Push-Token erhalten.

#### Nachrichtenzentrale
Um die Kampagnenfunktion der Mitteilungszentrale von Airship zu ersetzen, empfehlen wir, eine Multichannel-Kampagne zu erstellen, die aus einer Push-Benachrichtigung und einer [Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/) besteht. Wenn Sie mehr darüber erfahren möchten, wie Sie Content Cards im Format einer Mitteilungszentrale verwenden können, lesen Sie unsere [Anleitung zur Implementierung von iOS Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/implementation_guide/#content-cards-in-a-message-center).

### Segmentierung
Braze bietet mehrere [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/), um Ihren Kunden ein reichhaltiges Benutzererlebnis zu bieten.

| **Braze Perspective**:<br> Segmente in Braze sind vollständig dynamisch, so dass Benutzer das Segment betreten und verlassen, wenn sich die definierten Bedingungen ändern. |
{: .reset-td-br-1 role="presentation" }

#### Migration von Benutzersegmenten

Um ein statisches Luftschiffsegment in Braze direkt zu erstellen, gibt es zwei Möglichkeiten:
- **Importieren über API - Zuweisen eines benutzerdefinierten Attributs** (empfohlen)<br>
Wir empfehlen, Benutzer über den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) zu importieren und dabei diesen importierten Benutzern ein benutzerdefiniertes Attribut zuzuweisen. Sie könnten zum Beispiel ein Segment von Benutzern erstellen, die alle ein benutzerdefiniertes Attribut `Segment_Group_1` haben, das auf `true` gesetzt ist. Um diese Benutzer später zu segmentieren, würden Sie [ein Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) aller Benutzer [erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), bei denen `Segment_Group_1` `true` ist.<br><br>
- **Filter basierend auf CSV-Benutzerimport**<br>
In Braze gibt es eine Option, mit der Sie gezielt nach Benutzern filtern können, die in einem bestimmten CSV-Import enthalten sind. Diese Filteroption finden Sie im Schritt Zielbenutzer unserer Engagement-Tools unter "Benutzer nach `Updated/Imported via CSV` filtern".
![CSV-Import-Filter][1]{: style="max-width:90%;border:0;"}
Beachten Sie, dass für CSV-Importe eine externe ID für jeden importierten Benutzer erforderlich ist und dass **Segmente mit anonymen oder nur aliasbasierten Benutzern nicht importiert werden können**. Um eine Importvorlage anzusehen und mehr über den Import von Daten in das Dashboard zu erfahren, lesen Sie unsere [CSV-Dokumentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

## SDK-Codefragmente reißen und ersetzen
Um die Migration zu vereinfachen, haben wir die folgenden Airship-SDK-Snippets, die in Ihrem Code vorhanden sind, hervorgehoben und die entsprechenden Braze-SDK-Snippets bereitgestellt, die Sie ersetzen müssen. Besuchen Sie die folgenden Themen, um loszulegen:
- [Installation](#installation)
- [Benutzer-ID abrufen und einstellen](#userid)
- [Umgang mit Push-Benachrichtigungen](#pushnotifications)
- [Analytik](#analytics)
- [Umgang mit In-App-Nachrichten](#iammessages)
- [Inhaltskarten und Mitteilungszentrale](#messagecenter)

### Installation {#installation}
{% tabs %}
{% tab Schnell %}
**Luftschiff**
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {

    UAirship.takeOff(UAConfig.default())

    UALocation.shared()?.isLocationUpdatesEnabled = true
    UALocation.shared().isBackgroundLocationUpdatesAllowed = true

    UAirship.push()?.notificationOptions = [.alert, .badge, .sound]
    UAirship.push()?.userPushNotificationsEnabled = true
    UAirship.push()?.pushNotificationDelegate = self

    UAInAppAutomation.shared()?.inAppMessageManager.delegate = self
    UAInAppAutomation.shared()?.inAppMessageManager.displayInterval = 30
}
```
**Löten**
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {

    Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

    locationManager.requestAlwaysAuthorization() // locationManager is a CLLocationManager property variable

    // Push Notifications
    let options: UNAuthorizationOptions = [.alert, .sound, .badge]
    UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
      Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
    }
    UIApplication.shared.registerForRemoteNotifications()

    // In-App Messages
    Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endtab %}
{% tab Objective-C %}
**Luftschiff**
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  [UAirship takeOff:[UAConfig defaultConfig]];

  [[UALocation shared] setLocationUpdatesEnabled:YES];
  [[UALocation shared] setBackgroundLocationUpdatesAllowed:YES];

  [UAirship push].notificationOptions = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UAirship push] setUserPushNotificationsEnabled:YES];
  [[UAirship push] setPushNotificationDelegate:self];

  [UAInAppAutomation shared].inAppMessageManager.delegate = self;
  [UAInAppAutomation shared].inAppMessageManager.displayInterval = 30;

  return YES;
}
```
**Löten**
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  [Appboy startWithApiKey:self.apiKey inApplication:application withLaunchOptions:launchOptions withAppboyOptions:self.appboyOptions];

  [self.locationManager requestAlwaysAuthorization]; // locationManager is a CLLocationManager property variable

  // Push Notifications
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options
                          completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];

  // In-App Messages
  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];

  return YES;
}
```

{% endtab %}
{% endtabs %}

### Benutzer-ID abrufen und einstellen {#userid}
{% tabs %}
{% tab Schnell %}
**Luftschiff**
```swift
extension AirshipManager {
  var userId: String? {
    return UAirship.namedUser()?.identifier
   }

  func setUser(_ userId: String) {
    UAirship.namedUser()?.identifier = userId
  }
}
```
**Löten**
```swift
extension AppboyManager {
  var userId: String? {
     return Appboy.sharedInstance()?.user.userID
  }

  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Luftschiff**
```objc

- (NSString *)userId {
  return [UAirship namedUser].identifier
}

- (void)setUser:(NSString *)userId {
  [[UAirship namedUser] setIdentifier:userId];
}
```
**Löten**
```objc
- (NSString *)userId {
  return [Appboy sharedInstance].user.userID;
}

- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser: userId];
}
```
{% endtab %}
{% endtabs %}

### Umgang mit Push-Benachrichtigungen {#pushnotifications}
{% tabs %}
{% tab Schnell %}
**Luftschiff**
```swift
extension AirshipManager: UAPushNotificationDelegate {
  func receivedBackgroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    completionHandler(.noData)
  }

  func receivedForegroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping () -> Void) {
    completionHandler()
  }

  func receivedNotificationResponse(_ notificationResponse: UANotificationResponse, completionHandler: @escaping () -> Void) {
    completionHandler()
  }
}
```
**Löten**
```swift
extension AppboyManager {
  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
  }

  func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    Appboy.sharedInstance()?.register(application, didReceiveRemoteNotification: userInfo, fetchCompletionHandler: completionHandler)
  }

  func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    Appboy.sharedInstance()?.userNotificationCenter(center, didReceive: response, withCompletionHandler: completionHandler)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Luftschiff**
```objc
- (void)receivedBackgroundNotification:(UANotificationContent *)notificationContent completionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  completionHandler(UIBackgroundFetchResultNoData);
}

- (void)receivedForegroundNotification:(UANotificationContent *)notificationContent completionHandler:(void (^)(void))completionHandler {
  completionHandler();
}

- (void)receivedNotificationResponse:(UANotificationResponse *)notificationResponse completionHandler:(void (^)(void))completionHandler {
  completionHandler();
}
```
**Löten**
```objc
- (void)application:(UIApplication *)application didRegisterForRemoteNotifications
  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
  }

- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}

- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
}

- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center didReceiveNotificationResponse:response withCompletionHandler:completionHandler];
}
```
{% endtab %}
{% endtabs %}

### Analytik {#analytics}
{% tabs %}
{% tab Schnell %}
**Luftschiff**
```swift
extension AirshipManager {
  func trackEvent(with name: String, value: NSDecimalNumber? = nil, eventProperties: [String: Any]? = nil) {
    let event = UACustomEvent(name: name, value: value)

    if let eventProperties = eventProperties {
      event.properties = eventProperties
    }

    event.track()
  }

  func applyMutationsWithValue(_ value: String, forAttribute attribute: String) {
    let mutations = UAAttributeMutations()
    mutations.setString(value, forAttribute: attribute)
    UAirship.namedUser().apply(mutations)
  }
}
```
**Löten**
```swift
extension AppboyManager {
  func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
    Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
  }

  func setCustomAttributeWithKey(_ key: String, andStringValue value: String) {
    Appboy.sharedInstance()?.user.setCustomAttributeWithKey(key, andStringValue: value)
  }

  func logPurchase(productIdentifier: String, inCurrency currency: String, atPrice price: String, withQuanitity quanity: Int) {
    Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quanity))
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Luftschiff**
```objc
- (void)trackEventWith:(NSString *)name value:(NSDecimalNumber *)value eventProperties:(NSDictionary *)eventProperties {
  UACustomEvent *event = [[UACustomEvent alloc] init];
  event.eventName = name;
  event.eventValue = value;
  event.properties = eventProperties;

  [event track];
}

- (void)applyMutationWith:(NSString *)value forAttribute:(NSString *)attribute {
  UAAttributeMutations* mutations = [[UAAttributeMutations alloc] init];
  [mutations setString:value forAttribute:attribute];
  [[UAirship namedUser] applyAttributeMutations:mutations];
}
```
**Löten**
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties: properties];
}

- (void)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value {
  [[Appboy sharedInstance].user setCustomAttributeWithKey:key andStringValue:value];
}

- (void)logPurchase:(NSString *)productIdentifier inCurrency:(NSString *)currency atPrice:(NSString *)price withQuantity:(NSInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currency atPrice:[[NSDecimalNumber alloc] initWithString:price] withQuantity:quantity];
}
```
{% endtab %}
{% endtabs %}

### Umgang mit In-App-Nachrichten {#iammessages}
{% tabs %}
{% tab Schnell %}
**Luftschiff**
```swift

extension AirshipManager: UAInAppMessagingDelegate {
  func extend(_ message: UAInAppMessage) -> UAInAppMessage {
      return message
  }

  func messageWillBeDisplayed(_ message: UAInAppMessage, scheduleID: String) {
  }

  func messageFinishedDisplaying(_ message: UAInAppMessage, scheduleID: String, resolution: UAInAppMessageResolution) {
  }
}
```
**Löten**
```swift
extension AppboyManager: ABKInAppMessageControllerDelegate {
  func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // This delegate method defines whether the in-app message will be displayed now, displayed later, or discarded.
    return .displayInAppMessageNow
  }

  func beforeControlMessageImpressionLogged(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // This delegate method defines the timing of when the control in-app message impression event should be logged: now, later, or discarded.
    return .displayInAppMessageNow
  }
}

extension AppboyManager: ABKInAppMessageUIDelegate {
  func on(inAppMessageDismissed inAppMessage: ABKInAppMessage) {
    // Use this method to perform any custom logic that should execute after the in-app message has been dismissed
  }

  func on(inAppMessageClicked inAppMessage: ABKInAppMessage) -> Bool {
    // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
    return true
  }

  func on(inAppMessageButtonClicked inAppMessage: ABKInAppMessageImmersive, button: ABKInAppMessageButton) -> Bool {
    // This delegate method is fired whenever the user clicks a button on the in-app message.
    return true
  }

  func on(inAppMessageHTMLButtonClicked inAppMessage: ABKInAppMessageHTMLBase, clickedURL: URL?, buttonID buttonId: String) -> Bool {
    // This delegate method is fired whenever the user clicks a link on the HTML in-app message.
    return true
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Luftschiff**
```objc
- (UAInAppMessage *)extendMessage:(UAInAppMessage *)message {

  return message;
}

- (void)messageWillBeDisplayed:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID {

}

- (void)messageFinishedDisplaying:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID resolution:(UAInAppMessageResolution *)resolution {

}
```
**Löten**
```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  return ABKDisplayInAppMessageNow;
}

- (ABKInAppMessageDisplayChoice) beforeControlMessageImpressionLogged:(ABKInAppMessage *)inAppMessage {
  return ABKDisplayInAppMessageNow;
}

- (void)onInAppMessageDismissed:(ABKInAppMessage *)inAppMessage {
  // Use this method to perform any custom logic that should execute after the in-app message has been dismissed
}

- (BOOL)onInAppMessageClicked: (ABKInAppMessage *)inAppMessage {
  // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
  return YES;
}

- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button {
  return YES;
}

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID {
  return YES;
}
```
{% endtab %}
{% endtabs %}

### Inhaltskarten und Mitteilungszentrale {#messagecenter}
{% tabs %}
{% tab Schnell %}
**Luftschiff**
```swift
extension AirshipManager {
  func displayMessageCenter() {
    UAMessageCenter.shared()?.defaultUI.title = "My Message Center"

    let style = UAMessageCenterStyle()
    style.navigationBarColor = .black
    style.titleColor = .white
    style.tintColor = .white

    UAMessageCenter.shared()?.defaultUI.messageCenterStyle = style
    UAMessageCenter.shared()?.display()
  }
}
```
**Löten**
```swift
extension AppboyManager {
  func displayContentCards(navigationController: UINavigationController?) {
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "My Message Center"
    contentCardsVc.disableUnreadIndicator = true
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Luftschiff**
```objc
- (void)displayMessageCenter {
  [UAMessageCenter shared].defaultUI.title = @"My Message Center";
  [[UAMessageCenter shared] display];
}
```
**Löten**
```objc
- (void)displayContentCards:(UINavigationController *)navigationController {
  ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
  contentCards.title = @"My Message Center";
  [self.navigationController pushViewController:contentCards animated:YES];
}
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/csv_filter.png %}
