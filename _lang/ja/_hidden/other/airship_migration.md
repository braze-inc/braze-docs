---
nav_title: AirshipからBrazeへのSDK移行
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# AirshipからBraze（iOS）へSDKを移行する

> Brazeでは、全く新しいプラットフォームやSDKに移行するのは大変なことだと理解しているが、以下の移行ガイド、わかりやすいコードレベルの例、Brazeプラットフォームがもたらす印象的な機能セットがあれば、気にすることはないだろう。この記事では、Airshipの主要機能の多くに相当するBrazeと、移行を迅速、簡単、簡単にする "リッピング＆リプレース "SDKコードスニペットを紹介する。

## コードを超えて
### トークン管理
BrazeはアップルのiOS用デバイストークンを使用している。

**| ブレイズの視点**<br>AirshipからBrazeへの移行プロセス（100%Brazeへのハードカットオーバーであろうと、50%Airship 50%Brazeといったきめ細かな移行であろうと）において、顧客がユーザーと継続的にコミュニケーション（プッシュ通知など）できるようにする。|
{: .reset-td-br-1}

#### プッシュトークンの移行

[API経由でプッシュトークンを移行する]({{site.baseurl}}/help/help_articles/push/push_token_migration/#migration-via-api)必要がある。リンク先のドキュメントには、具体的な手順とペイロードの例が記載されているが、全体的な流れは以下の通りである：

1. [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)経由でトークンをインポートする。大規模なバッチ輸入については、プロセスを迅速化するためのリソースを用意している。詳細はCOMまたはSAに問い合わせること！
2. トークンがすでにBrazeに存在する場合は無視され、そうでない場合は匿名プロファイルが生成される。
3. プッシュ統合の品質保証を行う。[プッシュを設定する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)手順が完了していることを確認する。

ユーザープロファイルとプッシュトークンが別々の場所に保存されている場合は、プッシュトークンを匿名でインポートし、その後で既存のユーザープロファイルを移行することを推奨する。Braze iOS SDKが統合成功時にトークンの解決を処理するため、これらを一緒にマッピングする必要はない。

- API経由でユーザーを移行することを推奨するが、静的なユーザーリストをインポートする必要がある場合は、CSV経由で行うことができる。push_token」オブジェクトはCSVで指定できないため、**プッシュトークンをCSV経由でインポートすることはできない**。インポート・テンプレートや、ダッシュボードへのデータ・インポートの詳細については、[CSVドキュメントを]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)参照されたい。

{% alert note %}
プッシュトークンは、Brazeのダッシュボードでは`subscribed` と表示されるかもしれないが、ユーザーがBraze SDKでセッションを開始すると、`opted-in` に変更される。
{% endalert %}

#### 複数のプッシュ・トークン

Brazeでは、ユーザーは複数のプッシュトークン（各デバイスに1つずつ）を持つことができ、有効なプッシュトークンすべてをターゲットにすることで、複数のユーザーデバイスに通知を送ることができる。また、ユーザーの最新のデバイスにのみ送信するようにキャンペーンを設定することも可能である。

## キャンペーンの構成
高いレベルで言えば、Brazeはカスタマー・エンゲージメントの分野では実にユニークなツールである。Brazeに移行したキャンペーンは、豊富なカスタマイズオプションと増え続ける機能セットにより、これらのツールの利点を活用するために再計画が必要になることがよくある。

### 構成
#### プッシュ通知
Brazeはプッシュのために別々のチャンネルを必要とする（iOS用とAndroid用）。

**| ブレイズの視点**<br>我々は、顧客が譲歩する代わりに、両方の世界のベストを得ることを可能にする。個々のチャネルをフルに活用できることで、マーケティング担当者はより柔軟になり、ユーザー・エクスペリエンスも向上する。これにより、各OSの最新機能を採用することができる。例えば、アンドロイドはiOSより先にリッチ通知をサポートしていた。|
{: .reset-td-br-1}

Brazeは、Braze SDKがインストールされたアプリケーションをアップデートしていないユーザーにプッシュ通知を送信することができる。Brazeが有効なプッシュトークンを持っている場合、BrazeはBraze SDKなしでプッシュ通知を送信できる。プッシュメッセージ**分析は、Braze SDKを使用しないビルドでは利用できない**ことに注意することが重要である。

##### トークンを共有する

Braze SDKへの移行プロセス中も継続する必要があるライフサイクル固有のキャンペーンの場合、Brazeが有効なプッシュトークンを受け取っていれば、ユーザーはBrazeとAirshipの両方から通知を受け取ることができる。

#### メッセージセンター
Airshipのメッセージセンター・キャンペーン機能を置き換えるには、プッシュ通知と[コンテンツ・カードで]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/)構成されるマルチチャンネル・キャンペーンを作成することをお勧めする。コンテンツ・カードをメッセージ・センター形式で使用する方法については、[iOSコンテンツ・カード導入ガイドを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/implementation_guide/#content-cards-in-a-message-center)参照されたい。

### セグメンテーション
Brazeは、顧客に豊かなユーザー体験を提供するために、複数の[セグメンテーション]({{site.baseurl}}/user_guide/engagement_tools/segments/)フィルターを提供している。

**| ブレイズの視点**<br> Brazeのセグメントは完全に動的であるため、ユーザーは定義された条件の変化に応じてセグメントに入ったり出たりする。|
{: .reset-td-br-1}

#### ユーザーセグメントの移行

静的な飛行船セグメントをBrazeで直接再現するには、2つの選択肢がある：
- **API経由でインポートする - カスタム属性を割り当てる**（推奨）<br>
[`/users/track` 、エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)経由でユーザーをインポートし、インポートしたユーザーにカスタム属性を割り当てることを推奨する。例えば、`true` に設定されたカスタム属性`Segment_Group_1` を持つユーザーのセグメントを作成することができる。これらのユーザーを後でセグメント化するには、`Segment_Group_1` が`true` である全ユーザーの[セグメントを作成する。]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)<br><br>
- **CSVユーザーインポートに基づくフィルタリング**<br>
Brazeには、特定のCSVインポートに含まれるユーザーをフィルタリングするオプションがある。このフィルタリングオプションは、エンゲージメントツールのターゲットユーザーのステップで、"filter users by`Updated/Imported via CSV`" の下にある。
![CSVインポートフィルター][1]{: style="max-width:90%;border:0;"}
CSVインポートでは、インポートされる各ユーザーに外部IDが必要であり、**匿名またはエイリアスのみのユーザーを持つセグメントはインポートできないことに**注意すること。インポート・テンプレートや、ダッシュボードへのデータ・インポートの詳細については、[CSVドキュメントを]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)参照されたい。

## SDKのコード・スニペットをリッピングして置き換える
移行を簡略化するため、コード内に存在する以下のAirship SDKスニペットを強調表示し、それらを置き換えるために必要な対応するBraze SDKスニペットを提供する。まずは以下のトピックをご覧いただきたい：
- [インストール](#installation)
- [ユーザーIDの取得と設定](#userid)
- [プッシュ通知を扱う](#pushnotifications)
- [分析](#analytics)
- [アプリ内メッセージを処理する](#iammessages)
- [コンテンツ・カードとメッセージ・センター](#messagecenter)

### インストール {#installation}
{% tabs %}
{% tab スウィフト %}
**飛行船**
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
**飛行船**
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

### ユーザーIDの取得と設定 {#userid}
{% tabs %}
{% tab スウィフト %}
**飛行船**
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
**飛行船**
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

### プッシュ通知を扱う {#pushnotifications}
{% tabs %}
{% tab スウィフト %}
**飛行船**
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
**飛行船**
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

### 分析 {#analytics}
{% tabs %}
{% tab スウィフト %}
**飛行船**
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
**飛行船**
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

### アプリ内メッセージを処理する {#iammessages}
{% tabs %}
{% tab スウィフト %}
**飛行船**
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
**飛行船**
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

### コンテンツ・カードとメッセージ・センター {#messagecenter}
{% tabs %}
{% tab スウィフト %}
**飛行船**
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
**飛行船**
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

[1]: {% image_buster /assets/img/csv_filter.png %}
