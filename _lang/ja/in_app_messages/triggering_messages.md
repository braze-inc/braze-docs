---
nav_title: メッセージのトリガー
article_title: Braze SDKを使ったアプリ内メッセージのトリガー
page_order: 0.2
description: "Braze SDKを通してアプリ内メッセージをトリガーする方法を学習。"
platform: 
  - Android
  - FireOS
  - Swift
  - Web
---

# アプリ内メッセージのトリガー

> Braze SDKを通してアプリ内メッセージをトリガーする方法を学習。

## メッセージのトリガーと配信

アプリ内メッセージは、SDK が以下のカスタムイベントタイプのいずれかをログに記録したときにトリガーされます: `Session Start`、`Push Click`、`Any Purchase`、`Specific Purchase`、`Custom Event` (最後の 2 つは堅牢なプロパティフィルターを含む)。

ユーザーのセッション開始時に、Braze は対象となるすべてのアプリ内メッセージをユーザーのデバイスに配信し、同時にアセットをプリフェッチして表示レイテンシーを最小化します。トリガーイベントに複数の適格なアプリ内メッセージがある場合、最も優先度の高いメッセージのみが配信されます。詳しくは[セッションライフサイクル]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/#about-the-session-lifecycle)を参照してください。

{% alert note %}
アプリ内メッセージは、API または API イベントによってトリガーすることはできません。SDK によってログに記録されるカスタムイベントによってのみトリガーされます。ロギングの詳細については、[カスタムイベントのログ記録]({{site.baseurl}}/developer_guide/analytics/logging_events/)を参照してください。
{% endalert %}

## キーと値のペア

Braze でキャンペーンを作成する場合は、キーと値のペアを `extras` として設定できます。これは、アプリ内メッセージングオブジェクトがアプリにデータを送信するために使用できます。

{% tabs %}
{% tab web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
詳細については、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721) を参照してください。
{% endalert %}
{% endtab %}

{% tab swift %}
次の例では、カスタムロジックを使用して、`extras` のキーと値のペアに基づいてアプリ内メッセージの表示を設定します。完全なカスタマイズ例については、[サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)を参照してください。

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 自動トリガーを無効にする

デフォルトでは、アプリ内メッセージは自動的にトリガーされます。これを無効にする方法:

{% tabs %}

{% tab web %}
読み込みスニペット内の`braze.automaticallyShowInAppMessages()` への呼び出しを削除し、アプリ内メッセージの表示/非表示を処理するカスタムロジックを作成する。

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
`braze.automaticallyShowInAppMessages()` を削除せずに`braze.showInAppMessage` を呼び出すと、メッセージが 2 回表示される場合があります。
{% endalert %}

トリガーメッセージの遅延や復元など、メッセージのタイミングに関するより高度なコントロールについては、[チュートリアルを参照のこと：トリガーメッセージの延期と復元
{% endtab %}

{% tab android %}
1. を実装する。 [`IInAppMessageManagerListener`](https://www.braze.com/docs/developer_guide/in_app_messages/customization/?sdktab=android&tab=global%20listener#android_step-1-implement-the-custom-manager-listener)を実装してカスタムリスナーを設定する。
2. メソッドを更新する。 [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html)メソッドを更新する。 [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html).

メッセージを後で表示したり、再キューイングするなど、メッセージのタイミングに関するより高度なコントロールについては、[メッセージのカスタマイズの](https://www.braze.com/docs/developer_guide/in_app_messages/customization/?tab=global%20listener&subtab=kotlin#android_step-2-instruct-braze-to-use-the-custom-manager-listener)ページを参照されたい。
{% endtab %}

{% tab swift %}
1. `BrazeInAppMessageUIDelegate` デリゲートをアプリに実装する。完全なチュートリアルについては、[チュートリアルを参照のこと：アプリ内メッセージ UI ](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. `.discard` を返すように `inAppMessage(_:displayChoiceForMessage:)` デリゲートメソッドを更新します。

トリガーメッセージの遅延や復元など、メッセージのタイミングに関するより高度なコントロールについては、[チュートリアルを参照のこと：トリガーメッセージの延期と復元
{% endtab %}

{% tab flutter %}
1. 自動統合初期化機能を使用していることを確認してください。この機能は、バージョン `2.2.0` 以降でデフォルトで有効になっています。
2. 次の行を `braze.xml` ファイルに追加することで、アプリ内メッセージ操作のデフォルトを `DISCARD` に設定します。
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab unity %}
{% subtabs %}
{% subtab Android %}
Android の場合、Braze 設定エディターで、[**アプリ内メッセージを自動的に表示する**] の選択を解除します。または、Unity プロジェクトの `braze.xml` で `com_braze_inapp_show_inapp_messages_automatically` を `false` に設定できます。

アプリ内メッセージの初期表示動作は、Braze 設定の「アプリ内メッセージマネージャー初期表示動作」で設定できます。
{% endsubtab %}

{% subtab iOS %}
iOS の場合、Braze 設定エディターでゲームオブジェクトリスナーを設定し、[**Braze でアプリ内メッセージを表示する**] が選択されていないことを確認します。

アプリ内メッセージの初期表示動作は、Braze 設定の「アプリ内メッセージマネージャー初期表示動作」で設定できます。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## デフォルトのレート制限を上書きする

デフォルトでは、アプリ内メッセージは 30 秒に 1 回送信できます。これをオーバーライドするには、Brazeインスタンスが初期化される前に、以下のプロパティを設定ファイルに追加する。この値は、新しいレート制限 (秒単位) として使用されます。

{% tabs %}
{% tab web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}

{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 手動でメッセージをトリガーする

デフォルトでは、アプリ内メッセージは SDK がカスタムイベントを記録したときに自動的にトリガーます。しかし、これに加えて、以下の方法を使って、手動でメッセージをトリガーできます。

### サーバー側のイベントを使用する

{% tabs %}
{% tab web %}
現時点では、Web Braze SDKは、サーバーサイドのイベントを使用して手動でメッセージをトリガーすることをサポートしていない。
{% endtab %}

{% tab android %}
サーバー送信イベントを使用してアプリ内メッセージをトリガーするには、サイレントプッシュ通知をデバイスに送信し、カスタムプッシュコールバックがSDKベースのイベントをログに記録できるようにする。このイベントは、その後、ユーザー向けのアプリ内メッセージをトリガーします。

#### ステップ1:サイレントプッシュを受信するプッシュコールバックを作成する

特定のサイレントプッシュ通知をリッスンするには、カスタムプッシュコールバックを登録します。詳しくは、[プッシュ通知の]({{site.baseurl}}/developer_guide/push_notifications#android_setting-up-push-notifications)設定を参照のこと。

配信されるアプリ内メッセージに関して 2 つのイベントが記録されます。1 つはサーバーによって記録され、もう 1 つはカスタムプッシュコールバック内から記録されます。同じイベントが重複しないようにするには、プッシュコールバック内からログに記録されるイベントは、サーバー送信イベントと同じ名前ではなく、「アプリ内メッセージトリガーイベント」などの一般的な命名規則に従う必要があります。そうしないと、単一のユーザーアクションについてログに記録される重複イベントによって、セグメンテーションとユーザーデータが影響を受ける可能性があります。

{% subtabs %}
{% subtab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endsubtab %}
{% endsubtabs %}

#### ステップ 2:プッシュキャンペーンを作成する

サーバー送信イベントを介してトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)を作成します。

![]({% image_buster /assets/img_archive/serverSentPush.png %})

プッシュキャンペーンにはキーと値のペアエクストラを含める必要があります。これは、このプッシュキャンペーンが SDK カスタムイベントを記録するために送信されることを示します。このイベントは次のアプリ内メッセージをトリガーするために使用されます。

![2組のキーと値のペア：IS_SERVER_EVENT は "true "に設定され、CAMPAIGN_NAME は "example campaign name "に設定されている。]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

前出のプッシュコールバックサンプルコードは、キーと値のペアを認識して、適切な SDK カスタムイベントをログに記録します。

「アプリ内メッセージトリガー」イベントに添付するイベントプロパティを含めるには、プッシュペイロードのキーと値のペアでプロパティを渡します。この例では、後続のアプリ内メッセージのキャンペーン名が含められています。カスタムプッシュコールバックは、カスタムイベントをログに記録するときに、イベントプロパティのパラメーターとして値を渡すことができます。

#### ステップ3: アプリ内メッセージキャンペーンを作成する

Braze ダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信が必要であり、カスタムプッシュコールバック内から記録されたカスタムイベントからトリガーされる必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

!["campaign_name" "IAMキャンペーン名の例 "と等しい場合にアプリ内メッセージがトリガーされるアクションベースの配信キャンペーン。]({% image_buster /assets/img_archive/iam_event_trigger.png %})

アプリがフォアグラウンドにないときにサーバー送信イベントがログに記録されると、イベントはログに記録されますが、アプリ内メッセージは表示されません。アプリケーションがフォアグラウンドになるまでイベントを遅延させたい場合は、カスタムプッシュレシーバーにチェックを含めて、アプリがフォアグラウンドになるまでイベントを無視または遅延させる必要があります。
{% endtab %}

{% tab swift %}
#### ステップ 1: サイレントプッシュとキーと値のペアを扱う

次の関数を実装し、[`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: メソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/)内で呼び出します。

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

サイレントプッシュを受信すると、ユーザープロファイルに対して SDK が記録したイベント「アプリ内メッセージトリガー」がログに記録されます。 

{% alert important %}
SDK のログに記録されたカスタムイベントの記録にプッシュメッセージが使用されているため、Braze はこのソリューションを有効にするには、ユーザーごとにプッシュトークンを格納する必要があります。iOS ユーザーの場合、Braze ではユーザーが OS のプッシュプロンプトを受け取った時点からのトークンのみが保存されます。これ以前では、ユーザーはプッシュを使用して到達できず、先行ソリューションも実行できません。
{% endalert %}

#### ステップ 2:サイレントプッシュキャンペーンの作成

サーバー送信イベントを介してトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)を作成します。 

![ユーザープロファイルにカスタムイベント"server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %}が設定されているユーザーに配信されるアクションベースのアプリ内メッセージキャンペーン)

プッシュキャンペーンにはキーと値のペアエクストラを含める必要があります。これは、このプッシュキャンペーンが SDK カスタムイベントを記録するために送信されることを示します。このイベントは次のアプリ内メッセージをトリガーするために使用されます。

!["CAMPAIGN_NAME" 。"アプリ内メッセージ名の例 "として設定され、"IS_SERVER_EVENT" 。"true "に設定されている。2つのキーと値のペアを持つアクションベースの配信アプリ内メッセージキャンペーン。]({% image_buster /assets/img_archive/iOSServerPush.png %})

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内のコードはキー `IS_SERVER_EVENT` をチェックし、SDK カスタムイベントがあればログに記録します。

プッシュペイロードのキーと値のペアエクストラ内で目的の値を送信することで、イベント名またはイベントプロパティのいずれかを変更できます。カスタムイベントを記録する場合、これらのエクストラはイベント名のパラメータまたはイベントプロパティとして使用できます。

#### ステップ3: アプリ内メッセージキャンペーンを作成する

Braze ダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信があり、`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内から記録されたカスタムイベントからトリガーされる必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

!["campaign_name" が "IAM Campaign Name Example "に等しいカスタムイベント "アプリ内メッセージトリガー "を実行したユーザーに配信されるアクションベースの配信アプリ内メッセージキャンペーン。]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
なお、これらのアプリ内メッセージは、アプリケーションがフォアグラウンドにある間にサイレントプッシュが受信された場合にのみトリガーされます。
{% endalert %}
{% endtab %}
{% endtabs %}

### 事前定義されたメッセージを表示する

事前定義したアプリ内メッセージを手動で表示するには、以下の方法を使用します。

{% tabs %}
{% tab web %}
```javascript
braze.requestInAppMessageDisplay();
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}
{% endtabs %}

### リアルタイムでメッセージを表示する 

また、ダッシュボードで利用できるのと同じカスタマイズオプションを使って、アプリ内メッセージをリアルタイムで作成・表示することもできる。そのために必要なこと:

{% tabs %}
{% tab web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
ソフトキーボードが画面に表示されているときは、レンダリングが定義されていないため、アプリ内メッセージを表示しないでください。
{% endalert %}
{% endtab %}

{% tab swift %}
`inAppMessagePresenter` で [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) メソッドを手動で呼び出します。以下に例を示します。

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
独自のアプリ内メッセージを作成する場合、分析トラッキングをオプトアウトし、`message.context` を使用してクリックとインプレッションのロギングを手動で処理する必要がある。
{% endalert %}
{% endtab %}

{% tab unity %}
スタックの次のメッセージを表示するには、`DisplayNextInAppMessage()` メソッドを使う。`DISPLAY_LATER` または `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` がアプリ内メッセージ表示アクションとして選択されている場合、メッセージはこのスタックに保存されます。

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Web 用 Exit-intent メッセージ

Exit-intent メッセージは、訪問者が Web サイトを離れる前に訪問者に重要な情報を伝えるために使用される、中断のないアプリ内メッセージです。

Web SDKでこれらのメッセージタイプのトリガーを設定するには、Webサイトに([ouibounceのオープンソースライブラリなど](https://github.com/carlsednaoui/ouibounce))exit-intentライブラリを実装し、次のコードを使ってBrazeのカスタムイベントとして`'exit intent'` 。これで、今後のアプリ内メッセージキャンペーンでは、このメッセージタイプをカスタムイベントトリガーとして使うことができる。

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
