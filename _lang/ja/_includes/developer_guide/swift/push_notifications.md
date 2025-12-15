## レート制限

プッシュ通知にはレート制限があるため、アプリケーションで必要なだけ送信しても構いません。iOS と Apple Push Notification service (APNs) サーバーが配信頻度を制御するため、送信しすぎても問題が発生することはありません。プッシュ通知がスロットリングされている場合、デバイスが次にキープアライブパケットを送信するか、別の通知を受信するまで遅延する可能性があります。

## プッシュ通知の設定

### ステップ 1: APN トークンをアップロードする

{% multi_lang_include developer_guide/swift/apns_token.md %}

### ステップ2:プッシュ機能を有効にする

Xcodeで、メインアプリターゲットの**Signing& Capabilities**セクションに行き、プッシュ通知機能を追加する。

![Xcodeプロジェクトの「Signing& Capabilities」セクション。]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### ステップ 3:プッシュ処理の設定

Swift SDKを使用して、Brazeから受信したリモート通知の処理をオートメーション化できる。これはプッシュ通知を処理する最もシンプルな方法であり、推奨される処理方法である。

{% tabs local %}
{% tab Automatic %}
#### ステップ 3.1:プッシュ・プロパティでオートメーションをイネーブルメントにする

自動プッシュ統合を有効にするには、`push` 設定の`automation` プロパティを`true` に設定する：

{% subtabs %}
{% subtab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endsubtab %}
{% endsubtabs %}

これにより、SDK に次のことが指示されます。
- プッシュ通知用のアプリケーションをシステムに登録する。
- 初期化時にプッシュ通知の認証/許可を要求する。
- プッシュ通知関連のシステム・デリゲート・メソッドの実装を動的に提供する。

{% alert note %}
SDK によって実行されるオートメーションステップは、コードベース内の既存のプッシュ通知処理統合と互換性があります。SDKは、Brazeから受信したリモート通知の処理のみを自動化する。`automation` が有効になっている場合、独自または別のサードパーティの SDK リモート通知を処理するために実装されたシステムハンドラは、引き続き機能します。
{% endalert %}

{% alert warning %}
プッシュ通知の自動化を有効にするには、SDKをメインスレッドで初期化する必要がある。SDK の初期化は、アプリケーションの起動が完了する前、または AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 実装で行う必要があります。
アプリケーションが SDK を初期化する前に追加の設定を必要とする場合は、[遅延初期化]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift)に関するドキュメントのページを参照してください。
{% endalert %}

#### ステップ 3.2:個々の設定を上書きする（オプション）

よりきめ細かいコントロールのために、各オートメーションステップを個別に有効または無効にすることができます

{% subtabs %}
{% subtab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endsubtab %}
{% endsubtabs %}

使用可能なすべてのオプションについては [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) を、オートメーション動作の詳細については [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) を参照してください。
{% endtab %}

{% tab Manual %}
{% alert note %}
アプリに固有の追加の動作をプッシュ通知に依存している場合でも、手動プッシュ通知統合ではなく自動プッシュ統合を使用できる場合があります。この [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:))メソッドは、Brazeが処理したリモート通知を通知する方法を提供する。
{% endalert %}

#### ステップ 3.1:APNでプッシュ通知に登録する

ユーザーのデバイスがAPNに登録できるように、アプリの[`application:didFinishLaunchingWithOptions:` デリゲート・メソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application)内に適切なコード・サンプルを含める。アプリケーションのメインスレッドですべてのプッシュ統合コードを呼び出すようにしてください。

Braze には、プッシュアクションボタンをサポートするデフォルトのプッシュカテゴリーも用意されており、プッシュ登録コードに手動で追加する必要があります。その他の統合ステップについては、[プッシュアクションボタンを]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories)参照のこと。

アプリのデリゲートの`application:didFinishLaunchingWithOptions:` メソッドに以下のコードを追加する。 

{% alert note %}
次のコードサンプルには、仮のプッシュ許可の統合が含まれています。(5行目と6行目)。アプリで仮許可を使用する予定がない場合は、`requestAuthorization` オプションに `UNAuthorizationOptionProvisional` を追加するコード行を削除できます。<br>プッシュ仮許可の詳細については、[iOS 通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)をご覧ください。
{% endalert %}

{% subtabs %}
{% subtab Swift %}

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

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
アプリの起動が完了する前に、`center.delegate = self` を使用してデリゲートオブジェクトを同期的に割り当てる必要があります (可能であれば `application:didFinishLaunchingWithOptions:` で) 。そうしないと、アプリがプッシュ通知を受信できなくなる可能性があります。詳細については、Apple の [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) ドキュメントを参照してください。
{% endalert %}

#### ステップ 3.2:Braze にプッシュトークンを登録する

APNの登録が完了したら、結果の`deviceToken` をBrazeに渡し、ユーザーのプッシュ通知を有効にする。  

{% subtabs %}
{% subtab Swift %}

アプリの `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` メソッドに次のコードを追加します。

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

アプリの `application:didRegisterForRemoteNotificationsWithDeviceToken:` メソッドに次のコードを追加します。

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`application:didRegisterForRemoteNotificationsWithDeviceToken:` デリゲートメソッドは、`application.registerForRemoteNotifications()` の呼び出し後に毎回呼び出されます。<br><br>他のプッシュサービスから Braze に移行する場合、ユーザーのデバイスがすでに APNs に登録されていれば、このメソッドは次にこのメソッドが呼び出されたときに既存の登録からトークンを収集し、ユーザーはプッシュするために再オプトインする必要はありません。
{% endalert %}

#### ステップ3.3：プッシュ処理を有効にする

次に、受信したプッシュ通知をBrazeに渡す。このステップは、プッシュ分析とリンク処理のロギングに必要である。アプリケーションのメインスレッドですべてのプッシュ統合コードを呼び出すようにしてください。

##### デフォルトのプッシュ処理

{% subtabs %}
{% subtab Swift %}
Brazeデフォルトのプッシュ処理を有効にするには、アプリの`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッドに以下のコードを追加する：

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
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Brazeデフォルトのプッシュ処理を有効にするには、アプリケーションの`application:didReceiveRemoteNotification:fetchCompletionHandler:` メソッドに以下のコードを追加する：

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
{% endsubtab %}
{% endsubtabs %}

##### フォアグラウンドでのプッシュ通知処理

{% subtabs %}
{% subtab Swift %}
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
{% endsubtab %}

{% subtab OBJECTIVE-C %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## テスト通知 {#push-testing}

コマンドラインからアプリ内通知とプッシュ通知をテストする場合は、CURL と[メッセージング API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) を介してターミナルから単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` - [**設定**] > [**API キー**] で利用できます。
- `YOUR_EXTERNAL_USER_ID` - [**ユーザーの検索**] ページで使用できます。詳しくは[ユーザーIDの割り当てを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id)参照のこと。
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

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

## プッシュプライマー {#push-primers}

プッシュプライマーキャンペーンでは、アプリのデバイスでプッシュ通知を有効にするようにユーザーに促します。これは、[ノーコードプッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)を使用して、SDK のカスタマイズなしで行うことができます。

## ダイナミックなAPNゲートウェイ管理

ダイナミックなAppleプッシュ通知サービス（APNs）ゲートウェイ管理は、正しいAPNs環境を自動的に検出することで、iOSプッシュ通知の信頼性と効率を高める。以前は、プッシュ通知に使用するAPN環境（開発環境または本番環境）を手動で選択していたため、ゲートウェイの設定が間違っていたり、配信エラーや`BadDeviceToken` 。

ダイナミックなAPNゲートウェイ管理で、あなたは手に入れることができる：

- **信頼性が向上した：**通知は常に正しいAPN環境に配信されるため、配信の失敗を減らすことができる。
- **コンフィギュレーションの簡素化：**APNのゲートウェイ設定を手動で管理する必要がなくなった。
- **エラーに強い：**無効または欠落したゲートウェイ値は優雅に処理され、中断のないサービスを提供する。

### 前提条件

Brazeは、以下のSDKバージョン要件で、iOSのプッシュ通知のダイナミックなAPNゲートウェイ管理をサポートする：

{% sdk_min_versions swift:10.0.0 %}

### 仕組み

iOSアプリがBraze Swift SDKと統合すると、デバイス関連データを送信する。 [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment)をBraze SDK APIに送信する。`apns_gateway` の値は、アプリが開発環境(`dev`)と本番環境(`prod`)のどちらのAPNを使用しているかを示す。

Brazeは、各デバイスのレポートされたゲートウェイ値も保存する。新しい有効なゲートウェイ値を受信すると、Brazeは自動的に保存されている値を更新する。

Brazeがプッシュ通知を送るとき：

- デバイスに有効なゲートウェイ値（devまたはprod）が保存されている場合、Brazeはそれを使用して正しいAPN環境を決定する。
- ゲートウェイ値が保存されていない場合、Brazeは**アプリ設定**ページで設定されたAPN環境をデフォルトとする。

### よくある質問

#### なぜこの機能が導入されたのか？

ダイナミックなAPNゲートウェイ管理により、適切な環境が自動的に選択される。以前は、APNsゲートウェイを手動で設定する必要があり、`BadDeviceToken` エラー、トークンの無効化、APNsレート制限の問題の可能性があった。

#### これがプッシュ配信のパフォーマンスにどのような影響を与えるのか？

この機能は、プッシュトークンを常に正しいAPN環境にルーティングすることで、ゲートウェイの設定ミスによる失敗を回避し、配信率を向上させる。

#### この機能を無効にできるか？

ダイナミックなAPNゲートウェイ管理はデフォルトでオンになっており、信頼性を向上させる。ゲートウェイの手動選択が必要な特定のユースケースがある場合は、[Brazeサポートに]({{site.baseurl}}/user_guide/administrative/access_braze/support/)連絡すること。
