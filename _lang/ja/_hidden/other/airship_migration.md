---
nav_title: Airship から Braze への SDK 移行
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# Airship から Braze (iOS) への SDK の移行

> Braze では、まったく新しいプラットフォームと SDK への移行は大変な作業であることを理解していますが、次の移行ガイド、わかりやすいコードレベルの例、および Braze プラットフォームが提供する優れた機能セットにより、それほど気にならないと思います。この記事では、移行を迅速かつシンプルかつスムーズに行うために、Airship の多くの主要な機能に相当する Braze と、「置き換え可能な」SDK コード スニペットを紹介しています。

## コードを超えて
### トークン管理
Braze は iOS 用の Apple のデバイス トークンを使用します。

| **ブレイズの視点:**<br>Airship から Braze への移行プロセス中 (100% Braze へのハード カットオーバーでも、50% Airship 50% Braze などのきめ細かい移行でも)、お客様がユーザーと継続的にコミュニケーション (プッシュ通知など) できるようにします。 |
{: .reset-td-br-1}

#### プッシュトークンの移行

[API 経由でプッシュ トークンを移行する]({{site.baseurl}}/help/help_articles/push/push_token_migration/#migration-via-api)必要があります。リンクされたドキュメントには具体的な手順とペイロードの例が記載されていますが、全体的なプロセスは次のとおりです。

1. トークンをインポートするには、 [`/users/track` 終点]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)。大量のバッチインポートの場合、プロセスを迅速化するためのリソースが用意されています。詳細については、COM または SA にお問い合わせください。
2. トークンが Braze にすでに存在する場合は無視され、そうでない場合は匿名プロファイルが生成されます。
3. プッシュ統合の QA を実行します。[プッシュを構成する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) 手順が完了していることを確認します。

ユーザー プロファイルとプッシュ トークンが別の場所に保存されている場合は、プッシュ トークンを匿名でインポートしてから、既存のユーザー プロファイルを移行することをお勧めします。統合が成功すると Braze iOS SDK がトークンの解決を処理するため、それらを一緒にマッピングする必要はありません。

- API 経由でユーザーを移行することをお勧めしますが、静的なユーザー リストをインポートする必要がある場合は、CSV 経由で実行できます。CSV では「push\_token」オブジェクトを指定できないため、 **プッシュ トークンを CSV 経由でインポートすることはできない** ことに注意してください。インポート テンプレートを表示し、ダッシュボードへのデータのインポートについて詳しくは、[CSV ドキュメント]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)をご覧ください。

{% alert note %}
プッシュトークンは次のように表示されます `subscribed` Brazeダッシュボードでは、 `opted-in` ユーザーが Braze SDK でセッションを開始した後。
{% endalert %}

#### 複数のプッシュトークン

Braze を使用すると、ユーザーは複数のプッシュ トークン (デバイスごとに 1 つ) を持つことができ、すべての有効なプッシュ トークンをターゲットにすることで、複数のユーザー デバイスに通知を送信できます。ユーザーの最新のデバイスにのみキャンペーンを送信するように設定することもできます。

## キャンペーン設定
大まかに言えば、Braze は顧客エンゲージメントの分野において真にユニークなツールです。豊富なカスタマイズ オプションと機能セットの拡大に​​より、Braze に移行されたキャンペーンは、これらのツールの利点を活用するために再計画することでメリットを得られることが多く、当社のキャンペーン計画フレームワーク (詳細については COM または SA にお問い合わせください) はまさにそのために特別に構築されています。

### 構成
#### プッシュ通知
Braze では、プッシュ用に別々のチャネル (iOS 用と Android 用) が必要です。

| **ブレイズの視点:**<br>当社では、お客様が妥協することなく、両方のメリットを享受できるようにしています。個々のチャネルを最大限に活用できるようになると、マーケティング担当者の柔軟性が向上し、ユーザー エクスペリエンスが向上します。これにより、各 OS の最新機能を採用できます。たとえば、Android は iOS よりも前にリッチ通知をサポートしていました。 |
{: .reset-td-br-1}

Braze は、Braze SDK がインストールされた状態でアプリケーションを更新していないユーザーにプッシュ通知を送信できます。Braze に有効なプッシュ トークンがある場合、APNs が残りの処理を処理するため、Braze は Braze SDK なしでプッシュ通知を送信できます。**Braze SDK のないビルドではプッシュ メッセージ分析は利用できない**ことに注意することが重要です。

##### トークンの共有

Braze SDK への移行プロセス中に継続する必要があるライフサイクル固有のキャンペーンの場合、Braze が有効なプッシュ トークンを受信して​​いれば、ユーザーは Braze と Airship の両方から通知を受信できる場合があります。

#### メッセージセンター
Airship のメッセージ センター キャンペーン機能を置き換えるには、プッシュ通知と [コンテンツ カード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/)で構成されるマルチチャネル キャンペーンを作成することをお勧めします。メッセージ センター形式でコンテンツ カードを使用する方法の詳細については、[iOS コンテンツ カード実装ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/implementation_guide/#content-cards-in-a-message-center)をご覧ください。

### セグメンテーション
Braze は、顧客に豊かなユーザー エクスペリエンスを提供するために、複数の [セグメンテーション]({{site.baseurl}}/user_guide/engagement_tools/segments/) フィルターを提供します。

| **ブレイズの視点**:<br> Braze のセグメントは完全に動的であるため、定義された条件が変化すると、ユーザーはセグメントに出入りします。 |
{: .reset-td-br-1}

#### ユーザーセグメントの移行

Braze で静的な Airship セグメントを直接再作成するには、次の 2 つのオプションがあります。
-**API経由でインポート - カスタム属性を割り当てる** （推奨）<br>
ユーザーのインポートは、 [`/users/track` エンドポイントを作成]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) し、その際にインポートされたユーザーにカスタム属性を割り当てます。たとえば、カスタム属性を持つユーザーのセグメントを作成するとします。 `Segment_Group_1` 設定されている `true`。これらのユーザーを後でセグメント化するには、すべてのユーザーの [セグメントを作成し]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) ます。 `Segment_Group_1` は `true`。<br><br>
-**CSV ユーザーのインポートに基づくフィルター**<br>
Braze には、特定の CSV インポートに含まれるユーザーを具体的にフィルタリングするオプションがあります。このフィルタリングオプションは、エンゲージメントツールのターゲットユーザーステップの「ユーザーをフィルタリング」にあります。 `Updated/Imported via CSV`「」。
![CSVインポートフィルター][1]{: style="max-width:90%;border:0;"}
CSV インポートの場合、インポートされたユーザーごとに外部 ID が必要であり、 **匿名またはエイリアスのみのユーザーを含むセグメントはインポートできないこと**に注意してください。インポート テンプレートを表示し、ダッシュボードへのデータのインポートについて詳しくは、[CSV ドキュメント]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)をご覧ください。

## SDKコードスニペットをコピーして置き換える
移行を簡素化するために、コード内に存在する次の Airship SDK スニペットを強調表示し、それらを置き換えるために必要な対応する Braze SDK スニペットを提供しました。開始するには、次のトピックをご覧ください。
- [インストール](#installation)
- [ユーザーIDの取得と設定](#userid)
- [プッシュ通知の処理](#pushnotifications)
- [分析](#analytics)
- [アプリ内メッセージの処理](#iammessages)
- [コンテンツカードとメッセージセンター](#messagecenter)

### インストール {#installation}
{% tabs %}
{% tab Swift %}
**飛行船**
「速い」
関数application(_ application:UIApplication、didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey:任意

    UAirship.takeOff(UAConfig.default())

    UALocation.shared()?.isLocationUpdatesEnabled = true
    UALocation.shared().isBackgroundLocationUpdatesAllowed = true

    UAirship.push()?.notificationOptions = [.alert, .badge, .sound]
    UAirship.push()?.userPushNotificationsEnabled = true
    UAirship.push()?.pushNotificationDelegate = self

    UAInAppAutomation.shared()?.inAppMessageManager.delegate = self
    UAInAppAutomation.shared()?.inAppMessageManager.displayInterval = 30

```
**Braze**
```迅速
関数application(_ application:UIApplication、didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey:任意

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

```
{% endtab %}
{% tab Objective-C %}
**Airship**
```オブジェクト
\- (BOOL)アプリケーション:(UIApplication \*)アプリケーションdidFinishLaunchingWithOptions:(NSDictionary \*)launchOptions {

  [UAirship の離陸:[UAConfig のデフォルト構成]];

  [[UALocation 共有] setLocationUpdatesEnabled:YES];
  [[UALocation 共有] setBackgroundLocationUpdatesAllowed:YES];

  [UAirship プッシュ].notificationOptions = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UAirship プッシュ] setUserPushNotificationsEnabled:YES];
  [[UAirship プッシュ] setPushNotificationDelegate:self];

  [UAInAppAutomation 共有].inAppMessageManager.delegate = self;
  [UAInAppAutomation 共有].inAppMessageManager.displayInterval = 30;

  YESを返します。

```
**Braze**
```オブジェクト
\- (BOOL)アプリケーション:(UIApplication \*)アプリケーションdidFinishLaunchingWithOptions:(NSDictionary \*)launchOptions {

  [Appboy startWithApiKey:self.apiKey inApplication:application withLaunchOptions:launchOptions withAppboyOptions:self.appboyOptions];

  [self.locationManager requestAlwaysAuthorization]; // locationManager は CLLocationManager プロパティ変数です

  // プッシュ通知
  UNAuthorizationOptions オプション = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:オプション
                          完了ハンドラー:^(BOOL が許可されました、NSError * \_Nullable エラー) {
[[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
}];
    [[UIApplication sharedApplication] リモート通知を登録します];

  アプリ内メッセージ数
  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];

  YESを返します。

「」

{% endtab %}
{% endtabs %}

### ユーザーIDの取得と設定 {#userid}
{% tabs %}
{% tab Swift %}
**飛行船**
「速い」
拡張機能 AirshipManager {
var userId: String? {
return UAirship.namedUser()?.identifier
}

  関数setUser(\_userId:文字列
    UAirship.namedUser()?.identifier = ユーザーID
  

```
**Braze**
```迅速
拡張機能 AppboyManager {
var userId: String? {
return Appboy.sharedInstance()?.user.userID
}

  関数 changeUser(_ userId:文字列
    Appboy.sharedInstance()?.changeUser(ユーザーID)
  

```
{% endtab %}
{% tab Objective-C %}
**Airship**
```オブジェクト

- (NSString \*)ユーザーID {
  [UAirship namedUser].identifier を返す


- (void)setUser:(NSString \*)userId {
[[UAirship namedUser] setIdentifier:userId];
}
  ```
**Braze**
```オブジェクト
- (NSString \*)ユーザーID {
  [Appboy sharedInstance].user.userID を返します。


- (void)changeUser:(NSString \*)userId {
[[Appboy sharedInstance] changeUser: userId];
}
  「」
{% endtab %}
{% endtabs %}

### プッシュ通知の処理 {#pushnotifications}
{% tabs %}
{% tab Swift %}
**飛行船**
「速い」
拡張機能 AirshipManager:UAPushNotificationデリゲート {
func receivedBackgroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
completionHandler(.noData)
}

  関数 receivedForegroundNotification(_ notificationContent:UANotificationContent、完了ハンドラー: @escaping () -> Void) {
    完了ハンドラ()
  

  関数 receivedNotificationResponse(_ notificationResponse:UANotificationResponse、完了ハンドラー: @escaping () -> Void) {
    完了ハンドラ()
  

```
**Braze**
```迅速
拡張機能 AppboyManager {
func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
}

  関数application(_ application:UIApplication、didReceiveRemoteNotification ユーザー情報: [AnyHashable:任意]、fetchCompletionHandler 完了ハンドラー: @escaping (UIBackgroundFetchResult) -> Void) {
Appboy.sharedInstance()?.register(application, didReceiveRemoteNotification: userInfo, fetchCompletionHandler: completionHandler)
}

  関数userNotificationCenter(_ center:UNUserNotificationCenter、didReceive 応答:UNNotificationResponse、CompletionHandler の完了ハンドラー: @escaping () -> Void) {
Appboy.sharedInstance()?.userNotificationCenter(center, didReceive: response, withCompletionHandler: completionHandler)
}
    
  ```
{% endtab %}
{% tab Objective-C %}
**Airship**
```オブジェクト
\- (void)receivedBackgroundNotification:(UANotificationContent \*)notificationContent 完了ハンドラー:(void (^)(UIBackgroundFetchResult))完了ハンドラー {
完了ハンドラー(UIBackgroundFetchResultNoData);


- (void)receivedForegroundNotification:(UANotificationContent \*)notificationContent 完了ハンドラー:(void (^)(void))完了ハンドラー {
  完了ハンドラ();


- (void)receivedNotificationResponse:(UANotificationResponse \*)notificationResponse 完了ハンドラー:(void (^)(void))完了ハンドラー {
  完了ハンドラ();

```
**Braze**
```オブジェクト
- (void)アプリケーション:(UIApplication \*)アプリケーションはRegisterForRemoteNotificationsを実行しました
  関数application(_ application:UIApplication、didRegisterForRemoteNotificationsWithDeviceToken デバイストークン:data
    Appboy.sharedInstance()?.registerDeviceToken(デバイストークン)
  

- (void)アプリケーション:(UIApplication \*)アプリケーションはRegisterForRemoteNotificationsWithDeviceTokenを登録しました:(NSData \*)deviceToken {
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
}

- (void)アプリケーション:(UIApplication \*)アプリケーション didReceiveRemoteNotification:(NSDictionary \*)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
[[Appboy sharedInstance] registerApplication:application
didReceiveRemoteNotification:userInfo
fetchCompletionHandler:completionHandler];
}

- (void)userNotificationCenter:(UNUserNotificationCenter \*)center
didReceiveNotificationResponse:(UNNotificationResponse \*)応答
         補完ハンドラ付き:(void (^)(void))補完ハンドラ {
[[Appboy sharedInstance] userNotificationCenter:center didReceiveNotificationResponse:response withCompletionHandler:completionHandler];
}
  「」
{% endtab %}
{% endtabs %}

### 分析 {#analytics}
{% tabs %}
{% tab Swift %}
**飛行船**
「速い」
拡張機能 AirshipManager {
  関数trackEvent( name: 文字列、値:NSDecimalNumber? = nil、イベントプロパティ: [文字列:どれか]? = nil) {
    イベントをUACustomEvent(name: 名前、値: 値)

    if let eventProperties = eventProperties {
      event.properties = eventProperties
    }

    event.track()
  

  関数applyMutationsWithValue(_ 値:文字列、forAttribute 属性:文字列{
let mutations = UAAttributeMutations()
mutations.setString(value, forAttribute: attribute)
UAirship.namedUser().apply(mutations)
}
    
    ```
**Braze**
```迅速
    拡張機能 AppboyManager {
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}

  func setCustomAttributeWithKey(_ キー:文字列、およびStringValue値:文字列 {
Appboy.sharedInstance()?.user.setCustomAttributeWithKey(key, andStringValue: value)
}

  関数 logPurchase(productIdentifier:文字列、inCurrency 通貨:文字列、atPrice 価格:文字列、数量:中級 {
Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quanity))
}
    
  ```
{% endtab %}
{% tab Objective-C %}
**Airship**
```オブジェクト
\- (void)trackEventWith:(NSString \*)name value:(NSDecimalNumber \*)value eventProperties:(NSDictionary \*)eventProperties {
UACustomEvent \*イベント = [[UACustomEvent alloc] init];
イベント.イベント名 = 名前;
  イベント.イベント値 = 値;
  イベントプロパティ = イベントプロパティ;

  [イベントトラック];


- (void)applyMutationWith:(NSString \*)属性の値:(NSString *）属性 {
  UA属性ミューテーション* 変異 = [[UAAttributeMutations alloc] init];
  [mutations setString:value forAttribute:attribute];
  [[UAirship namedUser] applyAttributeMutations:mutations];

```
**Braze**
```オブジェクト
- (void)logCustomEvent:(NSString \*)eventName withProperties:(NSDictionary \*)properties {
[[Appboy sharedInstance] logCustomEvent:eventName withProperties: properties];
}

- (void)setCustomAttributeWithKey:(NSString \*)key およびStringValue:(NSString \*)value {
[[Appboy sharedInstance].user setCustomAttributeWithKey:key andStringValue:value];
}

- (void)logPurchase:(NSString \*)productIdentifier inCurrency:(NSString \*)currency atPrice:(NSString \*)price withQuantity:(NSInteger)quantity {
[[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currency atPrice:[[NSDecimalNumber alloc] initWithString:price] withQuantity:quantity];
}
  「」
{% endtab %}
{% endtabs %}

### アプリ内メッセージの処理 {#iammessages}
{% tabs %}
{% tab Swift %}
**飛行船**
「速い」

拡張機能 AirshipManager:UAInAppMessagingDelegate {
func extend(_ message: UAInAppMessage) -> UAInAppMessage {
return message
}

  関数 messageWillBeDisplayed(_ メッセージ:UAInAppMessage、スケジュールID:文字列
  

  function messageFinishedDisplaying(_ メッセージ:UAInAppMessage、スケジュールID:文字列、解像度:UAInAppMessageResolution) {
  

```
**Braze**
```迅速
拡張機能 AppboyManager:ABKInAppMessageControllerデリゲート {
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
// This delegate method defines whether the in-app message will be displayed now, displayed later, or discarded.
return .displayInAppMessageNow
}

  func beforeControlMessageImpressionLogged(_ inAppMessage:ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
// This delegate method defines the timing of when the control in-app message impression event should be logged: now, later, or discarded.
return .displayInAppMessageNow
}
    

拡張機能 AppboyManager:ABKInAppMessageUIデリゲート {
func on(inAppMessageDismissed inAppMessage: ABKInAppMessage) {
// Use this method to perform any custom logic that should execute after the in-app message has been dismissed
}

  func on(inAppMessageClicked inAppMessage:ABKInAppMessage) -> ブール値 {
    // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
    真を返す
  

  func on(inAppMessageButtonClicked inAppMessage:ABKInAppMessageImmersive、ボタン:ABKInAppMessageButton) -> ブール値 {
    // このデリゲート メソッドは、ユーザーがアプリ内メッセージのボタンをクリックするたびに実行されます。
    真を返す
  

  func on(inAppMessageHTMLButtonClicked inAppMessage:ABKInAppMessageHTMLBase、クリックされたURL:URL?、ボタンID ボタンID:文字列) -> ブール値 {
    // このデリゲート メソッドは、ユーザーが HTML アプリ内メッセージ上のリンクをクリックするたびに実行されます。
    真を返す
  

```
{% endtab %}
{% tab Objective-C %}
**Airship**
```オブジェクト
\- (UAInAppMessage \*)extendMessage:(UAInAppMessage \*)メッセージ {

  返信メッセージ;


- (void)messageWillBeDisplayed:(UAInAppMessage \*)messageスケジュールID:(NSString \*)scheduleID {



- (void)messageFinishedDisplaying:(UAInAppMessage \*)message scheduleID:(NSString \*)scheduleID resolution:(UAInAppMessageResolution \*)resolution {


```
**Braze**
```オブジェクト
\- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage \*)inAppMessage {
  ABKDisplayInAppMessageNow を返します。


- (ABKInAppMessageDisplayChoice) beforeControlMessageImpressionLogged:(ABKInAppMessage \*)inAppMessage {
  ABKDisplayInAppMessageNow を返します。


- (void)onInAppMessageDismissed:(ABKInAppMessage \*)inAppMessage {
  // このメソッドを使用して、アプリ内メッセージが閉じられた後に実行する必要があるカスタム ロジックを実行します。


- (BOOL)onInAppMessageがクリックされたとき:(ABKInAppMessage \*)inAppMessage {
  // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
  YESを返します。


- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive \*)inAppMessage
                             ボタン:(ABKInAppMessageButton \*)ボタン{
  YESを返します。


- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML \*)inAppMessage
                             クリックされたURL:(nullable NSURL \*)クリックされたURL
                               ボタンID:(NSString \*)ボタンID {
  YESを返します。

「」
{% endtab %}
{% endtabs %}

### コンテンツカードとメッセージセンター {#messagecenter}
{% tabs %}
{% tab Swift %}
**飛行船**
「速い」
拡張機能 AirshipManager {
  関数displayMessageCenter() {
    UAMessageCenter.shared()?.defaultUI.title = "私のメッセージセンター"

    let style = UAMessageCenterStyle()
    style.navigationBarColor = .black
    style.titleColor = .white
    style.tintColor = .white

    UAMessageCenter.shared()?.defaultUI.messageCenterStyle = style
    UAMessageCenter.shared()?.display()
  

```
**Braze**
```迅速
拡張機能 AppboyManager {
func displayContentCards(navigationController: UINavigationController?) {
let contentCardsVc = ABKContentCardsTableViewController()
contentCardsVc.title = "My Message Center"
contentCardsVc.disableUnreadIndicator = true
navigationController?.pushViewController(contentCardsVc, animated: true)
}
  
    ```
{% endtab %}
{% tab Objective-C %}
**Airship**
```オブジェクト
    \- (void)ディスプレイメッセージセンター{
    [UAMessageCenter 共有].defaultUI.title = @"マイメッセージセンター";
    [[UAMessageCenter 共有] 表示];
  
```
**Braze**
```オブジェクト
\- (void)displayContentCards:(UINavigationController \*)navigationController {
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"My Message Center";
[self.navigationController pushViewController:contentCards animated:YES];
}
「」
  {% endtab %}
  {% endtabs %}

[1]: {% image_buster /assets/img/csv_filter.png %}
