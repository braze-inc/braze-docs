---
nav_title: 統合
article_title: iOS 向けのプッシュ統合
platform: Swift
page_order: 0
description: "このリファレンス記事では、Braze Swift SDK の iOS プッシュ通知を設定する方法について説明します。"
channel:
  - push
  
---

# プッシュ通知の統合

> このリファレンス記事では、Braze Swift SDK の iOS プッシュ通知を設定する方法について説明します。

[プッシュ通知を使用する][1] と、重要なイベントが発生したときにアプリから通知を送信できます。新しいインスタントメッセージを配信したり、ニュース速報を送信したり、ユーザーのお気に入りのテレビ番組の最新エピソードがダウンロードしてオフライン視聴する準備ができたときに、プッシュ通知を送信することがあります。プッシュ通知は [サイレント][2]にすることもでき、アプリのインターフェースを更新したり、バックグラウンド作業をトリガーしたりするためにのみ使用されます。 

プッシュ通知は、バックグラウンドでの取得間の遅延が許容できないような、散発的だが即時に必要なコンテンツに適しています。プッシュ通知は、アプリケーションが必要な場合にのみ起動するため、バックグラウンドでの取得よりもはるかに効率的です。 

プッシュ通知にはレート制限があるため、アプリケーションで必要な数だけ送信しても問題ありません。iOS と Apple Push Notification サービス (APNs) サーバーが通知の配信頻度を制御するため、送信しすぎても問題が発生することはありません。プッシュ通知がスロットリングされている場合、デバイスが次にキープアライブパケットを送信するか、別の通知を受信するまで遅延する可能性があります。

## 前提条件

### プッシュ通知証明書

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

### プッシュ機能を有効にする

Xcode で、**[署名と機能]** ペインを使用して、プッシュ通知機能をメイン アプリ ターゲットに追加します。

![][24]

## 自動プッシュ統合

Swift SDK は、Braze から受信したリモート通知の処理を自動化するための構成のみのアプローチを提供します。このアプローチはプッシュ通知を統合する最も簡単な方法であり、ほとんどのお客様に推奨されます。

自動プッシュ統合を有効にするには、 `automation` の財産 `push` 構成 `true`:

{% tabs %}
{% tab swift %}
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

これにより、SDK に次の指示が与えられます。
\- システムにプッシュ通知用のアプリケーションを登録します。
\- 初期化時にプッシュ通知の承認/許可を要求します。
\- プッシュ通知関連のシステムデリゲートメソッドの実装を動的に提供します。

{% alert note %}
SDK によって実行される自動化手順は、コードベース内の既存のプッシュ通知処理統合と互換性があります。SDK は、Braze から受信したリモート通知の処理のみを自動化します。独自のまたはサードパーティのSDKリモート通知を処理するために実装されたシステムハンドラは、 `automation` 有効になっています。
{% endalert %}

{% alert warning %}
プッシュ通知の自動化を有効にするには、SDK をメイン スレッドで初期化する必要があります。SDKの初期化は、アプリケーションの起動が完了する前、またはAppDelegate内で実行する必要があります。 [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 実装。
{% endalert %}

### 個々の設定を上書きする

よりきめ細かな制御を行うために、各自動化ステップを個別に有効または無効にすることができます。

{% tabs %}
{% tab swift %}

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

見る [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) 利用可能なすべてのオプションと [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) 自動化の動作の詳細については、こちらをご覧ください。

自動プッシュ統合を使用している場合は、次のセクションをスキップして [ディープリンク](#deep-linking) に進むことができます。

## 手動プッシュ統合

プッシュ通知は手動で統合することもできます。このセクションでは、この統合に必要な手順について説明します。 

{% alert note %}
アプリ固有の追加動作にプッシュ通知を利用する場合は、手動プッシュ通知統合の代わりに自動プッシュ統合を使用できる場合があります。の [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) このメソッドは、Braze によって処理されたリモート通知を通知する方法を提供します。
{% endalert %}

### ステップ 1:APNsでプッシュ通知を登録する

アプリ内に適切なコードサンプルを含めてください [`application:didFinishLaunchingWithOptions:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) ユーザーのデバイスが APNs に登録できるように、デリゲート メソッドを使用します。アプリケーションのメインスレッドですべてのプッシュ統合コードを呼び出すようにしてください。

Braze には、プッシュアクションボタンをサポートするデフォルトのプッシュカテゴリーも用意されており、プッシュ登録コードに手動で追加する必要があります。その他の統合手順については [プッシュアクションボタン][35] を参照してください。

次のコードを `application:didFinishLaunchingWithOptions:` アプリデリゲートのメソッド。 

{% alert note %}
次のコードサンプルには、仮のプッシュ許可の統合が含まれています。(5行目と6行目)。アプリで仮許可を使用する予定がない場合は、`requestAuthorization` オプションに `UNAuthorizationOptionProvisional` を追加するコード行を削除できます。<br>プッシュ仮許可の詳細については、[iOS 通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)をご覧ください。
{% endalert %}

{% tabs %}
{% tab swift %}

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

### ステップ 2: Braze にプッシュトークンを登録する

APNs登録が完了したら、結果を渡します `deviceToken` Braze にプッシュ通知を有効にしてユーザーに送信します。  

{% tabs %}
{% tab swift %}

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

### ステップ 3: プッシュ処理を有効にする

次に、受信したプッシュ通知を Braze に渡します。この手順は、プッシュ分析とリンク処理をログに記録するために必要です。アプリケーションのメインスレッドですべてのプッシュ統合コードを呼び出すようにしてください。

{% tabs %}
{% tab swift %}

アプリの `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッドに次のコードを追加します。

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

次に、アプリの `userNotificationCenter(_:didReceive:withCompletionHandler:)` メソッドに次のコードを追加します。

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```

**フォアグラウンドでのプッシュ通知処理**

アプリがフォアグラウンドにある間にプッシュ通知を表示するには、`userNotificationCenter(_:willPresent:withCompletionHandler:)` を実装します。

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                            willPresent notification: UNNotification,
                            withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```

フォアグラウンド通知がクリックされると、iOS 10のプッシュデリゲート `userNotificationCenter(_:didReceive:withCompletionHandler:)` が呼び出され、Braze はプッシュクリックイベントをログに記録します。

{% endtab %}
{% tab OBJECTIVE-C %}

アプリケーションの `application:didReceiveRemoteNotification:fetchCompletionHandler:` メソッドに次のコードを追加します。

\`\`\`objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
  if (processedByBraze) {
return
()

completionHandler(UIBackgroundFetchResultNoData);
\`\`\`

次に、アプリの `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` メソッドに次のコードを追加します。

\`\`\`objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
  if (processedByBraze) {
return
()

completionHandler();
\`\`\`

**フォアグラウンドでのプッシュ通知処理**

アプリがフォアグラウンドにある間にプッシュ通知を表示するには、`userNotificationCenter:willPresentNotification:withCompletionHandler:` を実装します。

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

フォアグラウンド通知がクリックされると、iOS 10のプッシュデリゲート `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` が呼び出され、Braze はプッシュクリックイベントをログに記録します。

{% endtab %}
{% endtabs %}

## ディープリンク

プッシュからアプリへのディープリンクは、標準のプッシュ統合ドキュメントを介して自動的に処理されます。アプリ内の特定の場所にディープリンクを追加する方法について詳しくは、[高度なユースケース][10]を参照してください。

## プッシュ通知の更新を購読する

Brazeによって処理されたプッシュ通知ペイロードにアクセスするには、 [`Braze.Notifications.subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)/) 方法。

{% tabs %}
{% tab swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithInternalNotifications:NO update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% endtab %}
{% endtabs %}

{% alert note %}
自動プッシュ統合を使用する場合、 `subscribeToUpdates(_:)`Braze によって処理されたリモート通知を受け取る唯一の方法です。の `UIAppDelegate` そして `UNUserNotificationCenterDelegate` 通知が Braze によって自動的に処理される場合、システム メソッドは呼び出されません。
{% endalert %}

## {#push-testing} のテスト

コマンドラインからアプリ内通知とプッシュ通知をテストする場合は、CURL と [メッセージング API][29] を介してターミナルから単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` - [**設定**] > [**API キー**] で利用できます。
- `YOUR_EXTERNAL_USER_ID` - [**ユーザーの検索**] ページで使用できます。詳細については、[ユーザーIDの割り当て][32]を参照してください。
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これらのページは別の場所にあります。<br>\- [**API キー**] は [**開発者コンソール**] > [**API 設定**] にあります。<br>\- [**ユーザー検索**]は、[**ユーザー**] > [**ユーザー検索**] にあります。
{% endalert %}

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
上記の例は、 `US-01` 実例。このインスタンスにいない場合は、[API ドキュメント][66]を参照して、どのエンドポイントにリクエストを送信するかを確認してください。

## プッシュプライマー {#push-primers}

プッシュプライマーキャンペーンでは、アプリのデバイスでプッシュ通知を有効にするようにユーザーに促します。これは、[ノーコードプッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)を使用して、SDK のカスタマイズなしで行うことができます。

[1]:  {{site.baseurl}}/user_guide/message_building_by_channel/push/about/
[2]:  {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-implementation
[24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %}
[29]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id
[34]: {% image_buster /assets/img_archive/xcode8_auto_signing.png %}
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/
[66]: {{site.baseurl}}/api/basics/
