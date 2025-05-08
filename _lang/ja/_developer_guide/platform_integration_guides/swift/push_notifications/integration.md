---
nav_title: 統合
article_title: iOS 向けのプッシュ統合
platform: Swift
page_order: 0
description: "この参考記事では、Braze Swift SDKのiOSプッシュ通知の設定方法について説明する。"
channel:
  - push
  
---

# プッシュ通知の統合

> この参考記事では、Braze Swift SDKのiOSプッシュ通知の設定方法について説明する。

[プッシュ通知]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)を使用すると、重要なイベントが発生したときにアプリから通知を送ることができます。新しいインスタントメッセージを配信したり、ニュース速報を送信したり、ユーザーのお気に入りのテレビ番組の最新エピソードがダウンロードしてオフライン視聴する準備ができたときに、プッシュ通知を送信することがあります。プッシュ通知は、アプリのインターフェイスの更新やバックグラウンド作業のトリガーにのみ使用される[サイレント通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)にすることもできます。 

プッシュ通知は、バックグラウンドでの取得間の遅延が許容できないような、散発的だが即時に必要なコンテンツに適しています。プッシュ通知は、アプリケーションが必要な場合にのみ起動するため、バックグラウンドでの取得よりもはるかに効率的です。 

プッシュ通知にはレート制限があるため、アプリケーションで必要なだけ送信しても構いません。iOS と Apple Push Notification service (APNs) サーバーが配信頻度を制御するため、送信しすぎても問題が発生することはありません。プッシュ通知がスロットリングされている場合、デバイスが次にキープアライブパケットを送信するか、別の通知を受信するまで遅延する可能性があります。

## 初期設定

### ステップ 1:APN証明書をアップロードする

Braze を使用して iOS のプッシュ通知を送信する前に、Apple が提供する `.p8` のプッシュ通知ファイルを用意する必要があります。Apple の[開発者向けドキュメント](https://developer.apple.com/documentation/usernotifications)に記載されているように、

1. Apple 開発者アカウントで、［[**証明書、識別子 & プロファイル**](https://developer.apple.com/account/ios/certificate)］ を開きます。
2. [**キー**] で [**すべて**] を選択し、右上の追加ボタン (+) をクリックします。
3. [**キーの説明**]で、署名キーの一意の名前を入力します。
4. [**キーサービス**] で [**Apple プッシュ通知サービス (APNs)**] チェックボックスをオンにし、[**続行**] をクリックします。[**確認**] をクリックします。
5. キー ID をメモしておきます。[**ダウンロード**] をクリックして、キーを生成してダウンロードします。ダウンロードしたファイルは、何度もダウンロードできませんので、安全な場所に保存してください。
6. Braze で、[**設定**] > [**アプリ設定**] に移動し、[**Apple プッシュ通知証明書**] で `.p8` ファイルをアップロードします。開発用または実稼働用のプッシュ証明書のいずれかをアップロードできます。アプリが　App Store で公開された後にプッシュ通知をテストするには、アプリの開発バージョン用に別のワークスペースを設定することをお勧めします。
7. プロンプトが表示されたら、アプリの[バンドル ID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier)、[キー ID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/)、[チーム ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id)を入力し、［**保存**］ をクリックします。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**設定の管理**] > [**設定]** から `.p8` ファイルをアップロードできます。
{% endalert %}

### ステップ2:プッシュ機能を有効にする

Xcode で、メインアプリのターゲットの**署名 & 機能**セクションに移動しプッシュ通知機能を追加します。

![Xcode プロジェクトの「署名 & 機能」セクション]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

## 自動プッシュ統合

Swift SDK は、Braze から受信したリモート通知の処理を自動化するための設定のみのアプローチを提供します。この方法は、プッシュ通知を統合する最もシンプルな方法であり、ほとんどの顧客に推奨されます。

自動プッシュ統合を有効にするには、`push` 設定の`automation` プロパティを`true` に設定する：

{% tabs %}
{% tab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endtab %}
{% endtabs %}

これにより、SDK に次のことが指示されます。
- プッシュ通知用のアプリケーションをシステムに登録する。
- 初期化時にプッシュ通知の認証/許可を要求する。
- プッシュ通知関連のシステム・デリゲート・メソッドの実装を動的に提供する。

{% alert note %}
SDK によって実行されるオートメーションステップは、コードベース内の既存のプッシュ通知処理統合と互換性があります。SDKは、Brazeから受信したリモート通知の処理のみを自動化する。`automation` が有効になっている場合、独自または別のサードパーティの SDK リモート通知を処理するために実装されたシステムハンドラは、引き続き機能します。
{% endalert %}

{% alert warning %}
プッシュ通知の自動化を有効にするには、SDKをメインスレッドで初期化する必要がある。SDK の初期化は、アプリケーションの起動が完了する前、または AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 実装で行う必要があります。
アプリケーションが SDK を初期化する前に追加の設定を必要とする場合は、[遅延初期化]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/)に関するドキュメントのページを参照してください。
{% endalert %}

### 個々のコンフィギュレーションを上書きする

よりきめ細かいコントロールのために、各オートメーションステップを個別に有効または無効にすることができます

{% tabs %}
{% tab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endtab %}
{% endtabs %}

使用可能なすべてのオプションについては [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) を、オートメーション動作の詳細については [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) を参照してください。

自動プッシュ統合を使用している場合は、次のセクションをスキップして[ディープリンク](#deep-linking)に進むことができます。

## 手動プッシュ統合

プッシュ通知は手動で統合することもできる。このセクションでは、この統合に必要な手順を説明する。 

{% alert note %}
アプリに固有の追加の動作をプッシュ通知に依存している場合でも、手動プッシュ通知統合ではなく自動プッシュ統合を使用できる場合があります。この [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:))メソッドは、Brazeが処理したリモート通知を通知する方法を提供する。
{% endalert %}

### ステップ 1:APNでプッシュ通知に登録する

ユーザーのデバイスがAPNに登録できるように、アプリの[`application:didFinishLaunchingWithOptions:` デリゲート・メソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application)内に適切なコード・サンプルを含める。アプリケーションのメインスレッドですべてのプッシュ統合コードを呼び出すようにしてください。

Braze には、プッシュアクションボタンをサポートするデフォルトのプッシュカテゴリーも用意されており、プッシュ登録コードに手動で追加する必要があります。その他の統合ステップについては、[プッシュアクションボタンを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/)参照のこと。

アプリのデリゲートの`application:didFinishLaunchingWithOptions:` メソッドに以下のコードを追加する。 

{% alert note %}
次のコードサンプルには、仮のプッシュ許可の統合が含まれています。(5行目と6行目)。アプリで仮許可を使用する予定がない場合は、`requestAuthorization` オプションに `UNAuthorizationOptionProvisional` を追加するコード行を削除できます。<br>プッシュ仮許可の詳細については、[iOS 通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)をご覧ください。
{% endalert %}

{% tabs %}
{% tab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
アプリの起動が完了する前に、`center.delegate = self` を使用してデリゲートオブジェクトを同期的に割り当てる必要があります (可能であれば `application:didFinishLaunchingWithOptions:` で) 。そうしないと、アプリがプッシュ通知を受信できなくなる可能性があります。詳細については、Apple の [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) ドキュメントを参照してください。
{% endalert %}

### ステップ2:Braze にプッシュトークンを登録する

APNの登録が完了したら、結果の`deviceToken` をBrazeに渡し、ユーザーのプッシュ通知を有効にする。  

{% tabs %}
{% tab Swift %}

アプリの `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` メソッドに次のコードを追加します。

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endtab %}
{% tab OBJECTIVE-C %}

アプリの `application:didRegisterForRemoteNotificationsWithDeviceToken:` メソッドに次のコードを追加します。

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endtab %}
{% endtabs %}

{% alert important %}
`application:didRegisterForRemoteNotificationsWithDeviceToken:` デリゲートメソッドは、`application.registerForRemoteNotifications()` の呼び出し後に毎回呼び出されます。<br><br>他のプッシュサービスから Braze に移行する場合、ユーザーのデバイスがすでに APNs に登録されていれば、このメソッドは次にこのメソッドが呼び出されたときに既存の登録からトークンを収集し、ユーザーはプッシュするために再オプトインする必要はありません。
{% endalert %}

### ステップ 3:プッシュ処理を有効にする

次に、受信したプッシュ通知をBrazeに渡す。このステップは、プッシュ分析とリンク処理のロギングに必要である。アプリケーションのメインスレッドですべてのプッシュ統合コードを呼び出すようにしてください。

#### デフォルトのプッシュ処理

{% tabs %}
{% tab Swift %}
Brazeのデフォルトのプッシュ処理を有効にするには、アプリの`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッドに以下のコードを追加する：

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

次に、アプリの `userNotificationCenter(_:didReceive:withCompletionHandler:)` メソッドに以下を追加します。

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endtab %}

{% tab OBJECTIVE-C %}
Brazeのデフォルトのプッシュ処理を有効にするには、アプリケーションの`application:didReceiveRemoteNotification:fetchCompletionHandler:` メソッドに以下のコードを追加する：

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

次に、アプリの `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` メソッドに次のコードを追加します。

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endtab %}
{% endtabs %}

#### フォアグラウンドでのプッシュ通知処理

{% tabs %}
{% tab Swift %}
フォアグラウンドのプッシュ通知を有効にし、受信時に Braze がそれを認識できるようにするには、`UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)` を実装します。ユーザーがフォアグラウンド通知をタップすると、`userNotificationCenter(_:didReceive:withCompletionHandler:)` プッシュデリゲートが呼び出され、Brazeはプッシュクリックイベントを記録する。

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endtab %}

{% tab OBJECTIVE-C %}
フォアグラウンドのプッシュ通知を有効にし、受信時に Braze がそれを認識できるようにするには、`userNotificationCenter:willPresentNotification:withCompletionHandler:` を実装します。ユーザーがフォアグラウンド通知をタップすると、`userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` プッシュデリゲートが呼び出され、Brazeはプッシュクリックイベントを記録する。

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endtab %}
{% endtabs %}

## ディープリンク

プッシュからアプリへのディープリンクは、標準のプッシュ統合ドキュメントを介して自動的に処理されます。アプリ内の特定の場所にディープリンクを追加する方法について詳しくは、[高度なユースケース]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-implementation)を参照してください。

## プッシュ通知更新を購読する

Brazeが処理するプッシュ通知ペイロードにアクセスするには [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/)メソッドを使う。

`payloadTypes` パラメーターを使用して、プッシュ開封イベント、プッシュ受信イベント、またはその両方を含む通知を購読するかどうかを指定できます。

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
プッシュ受信イベントは、フォアグラウンド通知と `content-available` バックグラウンド通知に対してのみトリガーされることに留意してください。終了中に受信した通知や、`content-available` フィールドのないバックグラウンド通知ではトリガーされない。
{% endalert %}

{% endtab %}

{% tab OBJECTIVE-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
プッシュ受信イベントは、フォアグラウンド通知と `content-available` バックグラウンド通知に対してのみトリガーされることに留意してください。終了中に受信した通知や、`content-available` フィールドのないバックグラウンド通知ではトリガーされない。
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
自動プッシュ統合を使用する場合、Braze によって処理されるリモート通知を受信する唯一の方法は `subscribeToUpdates(_:)` です。`UIAppDelegate` と `UNUserNotificationCenterDelegate` システムメソッドは、通知が Braze によって自動的に処理されるときには呼び出されません。
{% endalert %}

{% alert tip %}
`application(_:didFinishLaunchingWithOptions:)` でプッシュ通知サブスクリプションを作成し、アプリが終了状態にある間にエンドユーザーが通知をタップした後にサブスクリプションがトリガーされるようにします。
{% endalert %}

## {#push-testing} のテスト

コマンドラインからアプリ内通知とプッシュ通知をテストする場合は、CURL と[メッセージング API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) を介してターミナルから単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` - [**設定**] > [**API キー**] で利用できます。
- `YOUR_EXTERNAL_USER_ID` - [**ユーザーの検索**] ページで使用できます。詳しくは[ユーザーIDの割り当てを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id)参照のこと。
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これらのページは別の場所にあります。<br>\- [**API キー**] は [**開発者コンソール**] > [**API 設定**] にあります。<br>\- [**ユーザー検索**]は、[**ユーザー**] > [**ユーザー検索**] にあります。
{% endalert %}

以下の例では、`US-01` インスタンスを使用している。このインスタンスを使用していない場合は、[APIドキュメントを]({{site.baseurl}}/api/basics/)参照して、どのエンドポイントにリクエストを行うかを確認すること。

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## プッシュプライマー {#push-primers}

プッシュプライマーキャンペーンでは、アプリのデバイスでプッシュ通知を有効にするようにユーザーに促します。これは、[ノーコードプッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)を使用して、SDK のカスタマイズなしで行うことができます。

