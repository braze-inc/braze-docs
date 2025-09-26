{% multi_lang_include developer_guide/prerequisites/swift.md %}

## メッセージトリガー

### トリガーの種類

アプリ内メッセージは、SDKが以下のカスタムイベントタイプのいずれかを記録すると自動的にトリガーされる：`Any Purchase` `Specific Purchase` 、`Session Start` 、`Custom Event` 、`Push Click` 。`Specific Purchase` 、`Custom Event` のトリガーには、ロバストなプロパティフィルターも含まれている。

{% alert note %}
アプリ内メッセージは、APIやAPIイベントによってトリガーされることはなく、SDKによって記録されるカスタムイベントによってのみトリガーされる。ロギングの詳細については、[カスタムイベントの学習を]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)参照のこと。
{% endalert %}

### 配信セマンティクス

対象となるアプリ内メッセージはすべて、セッション開始時にユーザーの端末に配信される。SDKは配信時にアセットをプリフェッチするため、トリガー時にアセットを利用でき、表示レイテンシを最小限に抑えることができる。トリガーイベントに複数のアプリ内メッセージがある場合、最も優先度の高いメッセージのみが配信される。

SDKのセッション開始セマンティクスの詳細については、セッション[ライフサイクルを]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift)参照のこと。

### デフォルトレート制限

デフォルトでは、アプリ内メッセージは30秒に1回送信できる。

これをオーバーライドするには、Brazeインスタンスが初期化される前に、Braze設定に`triggerMinimumTimeInterval` プロパティを追加する。これは任意の正の整数に設定でき、最小の時間間隔を秒単位で表す。以下に例を示します。

{% tabs %}
{% tab SWIFT %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration) 
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## キーと値のペア

Brazeでキャンペーンを作成する際、キーと値のペアを`extras` 、アプリ内メッセージングオブジェクトがアプリにデータを送信する際に使用できるように設定できる。以下に例を示します。

{% tabs %}
{% tab SWIFT %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

完全な実装については、 [サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)でアプリ内メッセージのカスタマイズサンプルを参照してください。

## 自動トリガーを無効にする

アプリ内メッセージが自動的にトリガーされないようにする：

1. [こちらの iOS の記事](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)で説明されているように、`BrazeInAppMessageUIDelegate` デリゲートを実装します。
2. `.discard` を返すように `inAppMessage(_:displayChoiceForMessage:)` デリゲートメソッドを更新します。

## 手動でメッセージをトリガーする

### サーバー側イベントを使う

サーバーサイドイベントを使用してアプリ内メッセージをトリガーするには、デバイスにサイレントプッシュを送信して、デバイスで SDK ベースのイベントを記録できるようにします。この SDK イベントは、その後、ユーザー向けのアプリ内メッセージをトリガーできます。

#### ステップ1:サイレントプッシュとキーと値のペアを扱う

次の関数を実装し、[`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: メソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/)内で呼び出します。

{% tabs %}
{% tab SWIFT %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

サイレントプッシュを受信すると、ユーザープロファイルに対して SDK が記録したイベント「アプリ内メッセージトリガー」がログに記録されます。 

{% alert important %}
SDK のログに記録されたカスタムイベントの記録にプッシュメッセージが使用されているため、Braze はこのソリューションを有効にするには、ユーザーごとにプッシュトークンを格納する必要があります。iOS ユーザーの場合、Braze ではユーザーが OS のプッシュプロンプトを受け取った時点からのトークンのみが保存されます。これ以前では、ユーザーはプッシュを使用して到達できず、先行ソリューションも実行できません。
{% endalert %}

#### ステップ 2:サイレントプッシュキャンペーンの作成

サーバー送信イベントを介してトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)を作成します。 

![カスタムイベント「server_event」を持つユーザープロファイルのユーザーに配信されるアクションベースの配信アプリ内メッセージキャンペーンです。]({% image_buster /assets/img_archive/iosServerSentPush.png %})

プッシュキャンペーンにはキーと値のペアエクストラを含める必要があります。これは、このプッシュキャンペーンが SDK カスタムイベントを記録するために送信されることを示します。このイベントは次のアプリ内メッセージをトリガーするために使用されます。

![アクションベースの配信アプリ内メッセージキャンペーンで、2つのキーと値のペアがあります。「キャンペーン_NAME」を「アプリ内メッセージ名の例」に設定し、「IS_SERVER_EVENT」を「true」に設定します。]({% image_buster /assets/img_archive/iOSServerPush.png %})

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内のコードはキー `IS_SERVER_EVENT` をチェックし、SDK カスタムイベントがあればログに記録します。

プッシュペイロードのキーと値のペアエクストラ内で目的の値を送信することで、イベント名またはイベントプロパティのいずれかを変更できます。カスタムイベントを記録する場合、これらのエクストラはイベント名のパラメータまたはイベントプロパティとして使用できます。

#### ステップ3: アプリ内メッセージキャンペーンを作成する

Braze ダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信があり、`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内から記録されたカスタムイベントからトリガーされる必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![カスタムイベント「アプリ内メッセージトリガー」を実行したユーザーに配信されるアクションベースの配信アプリ内メッセージキャンペーンで、「campaign_name」が「IAM Campaign Name Example」と等しい場合に配信されます。]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
なお、これらのアプリ内メッセージは、アプリケーションがフォアグラウンドにある間にサイレントプッシュが受信された場合にのみトリガーされます。
{% endalert %}

### あらかじめ定義されたものを表示する

事前に定義したアプリ内メッセージを手動で表示するには、以下の方法を使用する：

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### リアルタイムでメッセージを表示する

を手動で呼び出すことで、アプリ内メッセージをリアルタイムで表示することもできる。 [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:))`inAppMessagePresenter` 。以下に例を示します。

{% tabs %}
{% tab SWIFT %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

{% alert note %}
独自のアプリ内メッセージを作成する場合、分析トラッキングをオプトアウトし、`message.context` を使用してクリックとインプレッションのロギングを手動で処理する必要がある。
{% endalert %}

## アプリ内メッセージスタック

### アプリ内メッセージのスタックへの追加

ユーザーは、次の状況でアプリ内メッセージを受信できます。

- アプリ内メッセージトリガーイベントが発生する
- セッションが開始される
- プッシュ通知からアプリを開く

アプリ内メッセージのトリガーイベントが発生すると、そのイベントは「スタック」に配置されます。複数のアプリ内メッセージがスタック内にあり、表示を待機している場合、Braze は最後に受信したアプリ内メッセージを最初に表示します (後入れ先出し)。

ユーザーにアプリ内メッセージを受信する資格がある場合、`BrazeInAppMessagePresenter` により、アプリ内メッセージスタックから最新のアプリ内メッセージがリクエストされます。スタックはメモリに保存されたアプリ内メッセージのみを保持し、一時停止モードからアプリを起動するまでの間にクリアされます。

### アプリ内メッセージをスタックに返す

トリガーされたアプリ内メッセージは、次の状況でスタックに返されることがあります。

- アプリがバックグラウンドにあるときに、アプリ内メッセージがトリガーされた。
- 別のアプリ内メッセージが現在表示されている。
- `inAppMessage(_:displayChoiceForMessage:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)が `.reenqueue` を返した。

トリガーされたアプリ内メッセージは、ユーザーがアプリ内メッセージを受信する資格がある場合に後で表示されるよう、スタックの最上位に配置されます。

### アプリ内メッセージの破棄

トリガーされたアプリ内メッセージは、次の状況では破棄されます。

- `inAppMessage(_:displayChoiceForMessage:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)が `.discard` を返しました。
- アプリ内メッセージのアセット (画像または ZIP ファイル) のダウンロードに失敗しました。
- アプリ内メッセージを表示する準備ができていますが、タイムアウト時間が経過しました。
- デバイスの向きが、トリガーされたアプリ内メッセージの向きと一致しません。

アプリ内メッセージはスタックから削除されます。アプリ内メッセージは破棄された後、トリガーイベントの別のインスタンスによって後でトリガーできます。
