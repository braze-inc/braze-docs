---
nav_title: Airship에서 Braze로의 SDK 마이그레이션
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# Airship에서 Braze로 SDK 마이그레이션(iOS)

> 완전히 새로운 플랫폼과 SDK로 이전하는 것이 어려울 수 있으나 다음 마이그레이션 가이드와 간단한 코드 수준의 예제, 그리고 Braze 플랫폼이 제공하는 인상적인 기능 세트를 활용하면 걱정하지 않아도 됩니다. 이 글에는 마이그레이션을 빠르고 간단하고 쉽게 진행할 수 있도록 여러 주요 Airship 기능에 해당하는 Braze와 "rip-and-replace" SDK 코드 스니펫이 포함되어 있습니다.

## 코드 그 너머
### 토큰 관리
Braze는 iOS용 Apple의 디바이스 토큰을 사용합니다.

| **Braze 퍼스펙티브:**<br>Airship에서 Braze로 마이그레이션하는 과정(100% Braze로의 하드 컷오버 또는 50% Airship 50% Braze와 같은 세분화된 전환 등)에서 푸시 알림 등을 통해 고객이 사용자와 지속적으로 소통할 수 있도록 보장합니다. |
{: .reset-td-br-1 role="presentation" }

#### 푸시 토큰 마이그레이션

[API를 통해 푸시 토큰을 마이그레이션해야]({{site.baseurl}}/help/help_articles/push/push_token_migration/#migration-via-api) 합니다. 링크된 설명서에 구체적인 단계와 페이로드 예시가 포함되어 있지만 전체 프로세스는 다음과 같습니다.

1. [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 통해 토큰을 가져옵니다. 대량 일괄 가져오기의 경우 프로세스를 신속하게 처리하는 데 도움이 되는 리소스를 제공합니다. 자세한 내용은 담당 COM 또는 SA에게 문의하세요!
2. 토큰이 이미 Braze에 존재하는 경우 무시되며, 그렇지 않은 경우 익명 프로필이 생성됩니다.
3. 푸시 통합에 대한 품질 보증을 수행합니다. [푸시 구성]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 단계가 완료되었는지 확인합니다.

사용자 프로필과 푸시 토큰이 서로 다른 위치에 저장되어 있는 경우 푸시 토큰을 익명으로 가져온 다음 기존 사용자 프로필을 마이그레이션하는 것을 권장합니다. 통합이 성공하면 Braze iOS SDK가 토큰 확인을 처리하므로 함께 매핑할 필요는 없습니다.

- API를 통해 사용자를 마이그레이션하는 것이 좋지만 정적 사용자 목록을 가져와야 하는 경우 CSV를 통해 마이그레이션할 수 있습니다. 푸시 토큰은 CSV에 "push_token" 개체를 지정할 수 없으므로 **CSV를 통해 가져올 수 없습니다**. 가져오기 템플릿을 보고 대시보드로 데이터를 가져오는 방법에 대해 자세히 알아보려면 [CSV 설명서]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)를 확인하세요.

{% alert note %}
푸시 토큰은 Braze 대시보드에서 `subscribed`로 표시될 수 있지만, 사용자가 Braze SDK로 세션을 시작하면 `opted-in`으로 변경됩니다.
{% endalert %}

#### 여러 개의 푸시 토큰

Braze를 사용하면 사용자는 여러 개의 푸시 토큰(각 디바이스당 하나씩)을 가질 수 있으며, 유효한 모든 푸시 토큰을 타겟팅하여 여러 사용자 디바이스에 알림을 보낼 수 있습니다. 사용자의 가장 최근 디바이스로만 캠페인을 전송하도록 구성할 수도 있습니다.

## 캠페인 구성
높은 수준에서 보면 Braze는 고객 참여 분야에서 진정으로 독보적인 도구입니다. 광범위한 사용자 지정 옵션과 증가하는 기능 세트로 인해 Braze로 마이그레이션한 캠페인은 이러한 도구의 이점을 활용하기 위해 다시 계획을 세우는 경우가 많으며, 캠페인 계획 프레임워크(자세한 내용은 담당 COM 또는 SA에게 문의)는 이를 위해 특별히 설계되었습니다.

### 구성
#### 푸시 알림
Braze에는 푸시용 채널이 별도로 필요합니다(iOS용, Android용).

| **Braze 퍼스펙티브:**<br>저희는 고객이 양보하지 않고도 두 가지 장점을 모두 누릴 수 있도록 지원합니다. 개별 채널을 최대한 활용할 수 있으면 마케터에게 더 많은 유연성을 제공하고 사용자 경험을 개선할 수 있습니다. 이를 통해 각 OS의 최신 기능을 채택할 수 있습니다. 예를 들어, Android는 iOS보다 먼저 리치 알림을 지원했습니다. |
{: .reset-td-br-1 role="presentation" }

Braze는 Braze SDK를 설치한 상태에서 애플리케이션을 업데이트하지 않은 사용자에게 푸시 알림을 보낼 수 있습니다. Braze에 유효한 푸시 토큰이 있으므로 나머지는 APN이 처리하여 Braze SDK 없이도 푸시 알림을 전송할 수 있습니다. **Braze SDK가 없는 빌드에서는 푸시 메시지 분석을 사용할 수 없다는 점**에 유의해야 합니다.

##### 토큰 공유

Braze SDK로 마이그레이션하는 과정에서 계속 진행해야 하는 생애주기별 캠페인의 경우, Braze가 유효한 푸시 토큰을 받았다면 사용자는 Braze와 Airship 모두로부터 알림을 받을 자격이 있을 수 있습니다.

#### 메시지 센터
Airship의 메시지 센터 캠페인 기능을 대체하려면 푸시 알림과 [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/)로 구성된 멀티채널 캠페인을 만드는 것이 좋습니다. 메시지 센터 형식의 콘텐츠 카드를 사용하는 방법에 대한 자세한 내용은 [iOS 콘텐츠 카드 구현 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/implementation_guide/#content-cards-in-a-message-center)를 참조하세요.

### 세분화
Braze는 고객에게 풍부한 사용자 경험을 제공하기 위해 다양한 [세분화]({{site.baseurl}}/user_guide/engagement_tools/segments/) 필터를 제공합니다.

| **Braze 퍼스펙티브**:<br> Braze의 세그먼트는 완전히 동적이기 때문에 사용자는 정의된 조건이 변경되면 세그먼트에 들어가고 나가게 됩니다. |
{: .reset-td-br-1 role="presentation" }

#### 사용자 세그먼트 마이그레이션

Braze에서 정적 Airship 세그먼트를 직접 재생성하려면 두 가지 옵션을 사용할 수 있습니다.
- **API를 통한 가져오기 - 사용자 지정 속성 할당** (권장)<br>
[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 통해 사용자를 가져오면서 가져온 사용자에 커스텀 속성을 할당하는 것이 좋습니다. 예를 들어 각각 `true`로 설정된 커스텀 속성 `Segment_Group_1`을 가진 사용자 세그먼트를 만들 수 있습니다. 나중에 이러한 사용자를 세분화하려면 `Segment_Group_1`이 `true`인 모든 사용자의 [세그먼트를 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)하면 됩니다.<br><br>
- **CSV 사용자 가져오기를 기반으로 필터링**<br>
Braze에는 특정 CSV 가져오기에 포함된 사용자를 구체적으로 필터링하는 옵션이 있습니다. 이 필터링 옵션은 참여 툴의 타겟 사용자 단계에서 "`Updated/Imported via CSV`로 사용자 필터링"에서 찾을 수 있습니다.
![CSV 가져오기 필터]({% image_buster /assets/img/csv_filter.png %}){: style="max-width:90%;border:0;"}
CSV 가져오기의 경우 가져온 각 사용자에 대해 외부 ID가 필요하며 **익명 또는 별칭 전용 사용자가 있는 세그먼트는 가져올 수 없습니다**. 가져오기 템플릿을 보고 대시보드로 데이터를 가져오는 방법에 대해 자세히 알아보려면 [CSV 설명서]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)를 확인하세요.

## SDK 코드 스니펫 추출 및 바꾸기
마이그레이션을 간소화하기 위해 Braze는 코드에 존재하는 다음 Airship SDK 스니펫을 강조 표시하고 이를 대체하는 데 필요한 해당 Braze SDK 스니펫을 제공했습니다. 시작하려면 다음 주제를 참조하세요:
- [설치](#installation)
- [사용자 ID 가져오기 및 설정](#userid)
- [푸시 알림 처리하기](#pushnotifications)
- [분석](#analytics)
- [인앱 메시지 처리](#iammessages)
- [콘텐츠 카드 및 메시지 센터](#messagecenter)

### 설치 {#installation}
{% tabs %}
{% tab Swift %}
**비행선**
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
**Braze**
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
**비행선**
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
**Braze**
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

### 사용자 ID 가져오기 및 설정 {#userid}
{% tabs %}
{% tab Swift %}
**비행선**
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
**Braze**
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
**비행선**
```objc

- (NSString *)userId {
  return [UAirship namedUser].identifier
}

- (void)setUser:(NSString *)userId {
  [[UAirship namedUser] setIdentifier:userId];
}
```
**Braze**
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

### 푸시 알림 처리하기 {#pushnotifications}
{% tabs %}
{% tab Swift %}
**비행선**
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
**Braze**
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
**비행선**
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
**Braze**
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

### 분석 {#analytics}
{% tabs %}
{% tab Swift %}
**비행선**
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
**Braze**
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
**비행선**
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
**Braze**
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

### 인앱 메시지 처리 {#iammessages}
{% tabs %}
{% tab Swift %}
**비행선**
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
**Braze**
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
**비행선**
```objc
- (UAInAppMessage *)extendMessage:(UAInAppMessage *)message {

  return message;
}

- (void)messageWillBeDisplayed:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID {

}

- (void)messageFinishedDisplaying:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID resolution:(UAInAppMessageResolution *)resolution {

}
```
**Braze**
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

### 콘텐츠 카드 및 메시지 센터 {#messagecenter}
{% tabs %}
{% tab Swift %}
**비행선**
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
**Braze**
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
**비행선**
```objc
- (void)displayMessageCenter {
  [UAMessageCenter shared].defaultUI.title = @"My Message Center";
  [[UAMessageCenter shared] display];
}
```
**Braze**
```objc
- (void)displayContentCards:(UINavigationController *)navigationController {
  ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
  contentCards.title = @"My Message Center";
  [self.navigationController pushViewController:contentCards animated:YES];
}
```
{% endtab %}
{% endtabs %}

