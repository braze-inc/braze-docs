---
nav_title: アプリ内メッセージ配信
article_title: iOS 向けアプリ内メッセージ配信
platform: Swift
page_order: 2
description: "この記事では、iOS アプリ内メッセージ配信について説明し、Swift SDK のさまざまなトリガータイプ、配信セマンティクス、イベントトリガーステップについて説明します。"
channel:
  - in-app messages

---

# アプリ内メッセージ配信

> このリファレンス記事では、iOS アプリ内メッセージ配信の概要を説明し、さまざまなトリガータイプ、配信セマンティクス、イベントトリガーステップについて説明します。

## トリガーの種類

アプリ内メッセージは SDK によって記録されるイベントによってトリガーされます。イベントタイプ `Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、`Push Click` からアプリ内メッセージをトリガーできます。さらに、`Specific Purchase` および `Custom Event` トリガーには堅牢なプロパティフィルターが含まれています。

{% alert note %}
トリガーされたアプリ内メッセージは、Braze SDK を通じて記録されたカスタムイベントでのみ機能します。アプリ内メッセージは、API または API イベント (購入イベントなど) によってトリガーすることはできません。iOS を使用している場合は、[カスタムイベントの追跡]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)に関する記事を参照して詳細を確認してください。
{% endalert %}

## アプリ内メッセージを有効にする

Braze でアプリ内メッセージを表示できるようにするには、 `BrazeInAppMessagePresenter` プロトコルの実装を作成し、それを Braze インスタンスでオプションの `inAppMessagePresenter` に割り当てます。`BrazeInAppMessageUI` オブジェクトをインスタンス化することで、デフォルトの Braze UI プレゼンターを使用することもできます。

`BrazeInAppMessageUI` クラスにアクセスするには、`BrazeUI` ライブラリーをインポートする必要があることに注意してください。

{% tabs %}
{% tab SWIFT %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

## 配信セマンティクス

ユーザーが対象になるすべてのアプリ内メッセージは、セッション開始時にユーザーのデバイスに配信されます。配信時に、SDK はアセットをプリフェッチしてトリガー時にすぐに利用できるようにし、表示遅延を最小限に抑えます。

トリガーイベントに複数の適格なアプリ内メッセージが関連付けられている場合、最も優先度の高いアプリ内メッセージのみが配信されます。

アセットがプリフェッチされていないため、配信 (セッション開始、プッシュクリック) 時にすぐに表示されるアプリ内メッセージには多少の遅延が発生する可能性があります。SDK のセッション開始セマンティクスの詳細については、[セッションライフサイクル]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle)に関する記事をお読みください。

## トリガー間の最小時間間隔

デフォルトでは、高品質のユーザーエクスペリエンスを促進するため、アプリ内メッセージのレートが30秒に1回に制限されています。

この値は、 Braze 構成の `triggerMinimumTimeInterval` プロパティを設定することで上書きできます。Braze インスタンスを初期化する前に、必ずこの値を設定してください。`triggerMinimumTimeInterval` を、アプリ内メッセージ間の最小時間 (秒) として使用する整数値に設定します。

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

## 一致するトリガーが見つからない

Braze で特定のイベントに一致するトリガーを検出できない場合、[`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/) が呼び出されます。このシナリオを処理するには、`BrazeDelegate` を採用するクラスにこのメソッドを実装します。 

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

## リアルタイムのアプリ内メッセージの作成と表示

アプリ内で別の時点でアプリ内メッセージを表示する必要がある場合は、`inAppMessagePresenter` において [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) を手動で呼び出すことができます。アプリ内メッセージはアプリ内でローカルに作成し、Braze 経由で表示できます。これは、アプリ内でトリガーしたいメッセージをリアルタイムで表示する場合に特に便利です。

独自のアプリ内メッセージを作成すると、分析の追跡をオプトアウトすることになり、`message.context` を使用してクリックとインプレッションのロギングを手動で処理する必要があることに注意してください。

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

## キーと値のペアのエクストラ

`Braze.InAppMessage` オブジェクトはキーと値のペアを `extras` として保持できます。これらは、キャンペーン作成時にダッシュボードで指定します。キーと値のペアを使用して、アプリ内メッセージとともにデータを送信し、アプリでさらに処理することができます。

たとえば、アプリ内メッセージの表示をそのエクストラの内容に基づいてカスタマイズするケースを考えてみましょう。`extras` プロパティでキーと値のペアにアクセスし、実行に使用するカスタムロジックを定義します。

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

