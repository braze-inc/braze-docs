---
nav_title: アプリ内メッセージ配信
article_title: iOS 向けアプリ内メッセージ配信
platform: iOS
page_order: 3
description: "この参考記事では、iOS アプリ内メッセージ配信について説明し、さまざまなトリガータイプ、配信セマンティクス、イベントトリガーステップについて説明します。"
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# アプリ内メッセージ配信

## トリガーの種類

アプリ内メッセージ製品を使用すると、次のようなさまざまなイベントタイプの結果としてアプリ内メッセージ表示をトリガーできます: `Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、および `Push Click`。さらに、`Specific Purchase` そして `Custom Event` トリガーには堅牢なプロパティフィルターが含まれています。

{% alert note %}
トリガーされたアプリ内メッセージは、Braze SDK を通じて記録されたカスタムイベントでのみ機能します。アプリ内メッセージは、API または API イベント (購入イベントなど) によってトリガーすることはできません。iOS を使用している場合は、[カスタムイベントの追跡]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)に関する記事を参照して詳細を確認してください。
{% endalert %}

## 配信セマンティクス

ユーザーが対象になるすべてのアプリ内メッセージは、セッション開始時にユーザーのデバイスに配信されます。1つのイベントによって2つのアプリ内メッセージがトリガーされた場合、優先度の高いアプリ内メッセージが表示されます。SDK のセッション開始セマンティクスの詳細については、[セッションライフサイクル]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle)に関する記事をお読みください。配信時に、SDK はアセットをプリフェッチしてトリガー時にすぐに利用できるようにし、表示遅延を最小限に抑えます。

トリガーイベントに複数の適格なアプリ内メッセージが関連付けられている場合、最も優先度の高いアプリ内メッセージのみが配信されます。

アセットがプリフェッチされていないため、配信 (セッション開始、プッシュクリック) 時にすぐに表示されるアプリ内メッセージには多少の遅延が発生する可能性があります。

## トリガー間の最小時間間隔

デフォルトでは、高品質のユーザーエクスペリエンスを促進するため、アプリ内メッセージのレートが 30 秒に 1 回に制限されています。

この値は、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡された `appboyOptions` パラメーター内の `ABKMinimumTriggerTimeIntervalKey` を使用してオーバーライドできます。`ABKMinimumTriggerTimeIntervalKey` を、アプリ内メッセージ間の最小時間 (秒) として使用する整数値に設定します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## 一致するトリガーが見つからない

Braze が特定のイベントに一致するトリガーを検出できない場合、[`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html) の [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) メソッドを呼び出します。このシナリオを処理するには、デリゲートプロトコルを採用するクラスにこのメソッドを実装します。 

## ローカルのアプリ内メッセージ配信

### アプリ内メッセージスタック

#### アプリ内メッセージの表示

ユーザーがアプリ内メッセージを受信する資格がある場合、`ABKInAppMessageController` には、アプリ内メッセージスタックから最新のアプリ内メッセージが提供されます。スタックはメモリに保存されたアプリ内メッセージのみを保持し、一時停止モードからアプリを起動するまでの間にクリアされます。

{% alert important %}
キーボードが画面に表示されているときは、レンダリングが定義されていないため、アプリ内メッセージを表示しないでください。
{% endalert %}

#### アプリ内メッセージをスタックに追加する

ユーザーは、次の状況でアプリ内メッセージを受信できます。

- アプリ内メッセージトリガーイベントが発生する
- セッション開始イベント
- プッシュ通知からアプリを開く

トリガーされたアプリ内メッセージは、トリガーイベントが発生するとスタックに配置されます。複数のアプリ内メッセージがスタック内にあり、表示を待機している場合、Braze は最後に受信したアプリ内メッセージを最初に表示します (後入れ先出し)。

#### アプリ内メッセージをスタックに返す

トリガーされたアプリ内メッセージは、次の状況でスタックに返されることがあります。

- アプリがバックグラウンドにあるときに、アプリ内メッセージがトリガーされた。
- 別のアプリ内メッセージが現在表示されている。
- 非推奨の `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI デリゲートメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate)は実装されておらず、キーボードが現在表示されています。
- `beforeInAppMessageDisplayed:` [デリゲートメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate)または非推奨の `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI デリゲートメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate)が `ABKDisplayInAppMessageLater` を返しました。

#### アプリ内メッセージの破棄

トリガーされたアプリ内メッセージは、次の状況では破棄されます。

- `beforeInAppMessageDisplayed:` [デリゲートメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate)または非推奨の `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI デリゲートメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate)が `ABKDiscardInAppMessage` を返しました。
- アプリ内メッセージのアセット (画像または ZIP ファイル) のダウンロードに失敗しました。
- アプリ内メッセージを表示する準備ができていますが、タイムアウト時間が経過しました。
- デバイスの向きが、トリガーされたアプリ内メッセージの向きと一致しません。
- アプリ内メッセージは完全なアプリ内メッセージですが、画像はありません。
- アプリ内メッセージは画像のみのモーダルアプリ内メッセージですが、画像はありません。

#### アプリ内メッセージ表示を手動でキューに入れる

アプリ内で別の時点でアプリ内メッセージを表示したい場合は、次のメソッドを呼び出してスタックの最上位のアプリ内メッセージを手動で表示できます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### リアルタイムのアプリ内メッセージの作成と表示

アプリ内メッセージはアプリ内でローカルに作成し、Braze 経由で表示することもできます。これは、アプリ内でトリガーしたいメッセージをリアルタイムで表示する場合に特に便利です。Braze は、ローカルで作成されたアプリ内メッセージの分析をサポートしていません。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}

