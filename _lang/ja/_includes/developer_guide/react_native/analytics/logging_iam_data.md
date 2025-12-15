{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## ロギングの方法

これらのメソッドを使用するには、`BrazeInAppMessage` インスタンスを渡して分析をログに記録し、アクションを実行します。

| 方法                                                    | 説明                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | 提供されたアプリ内メッセージデータのクリックを記録する。                                    |
| `logInAppMessageImpression(inAppMessage)`                 | 提供されたアプリ内メッセージデータのインプレッションを記録する。                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | 提供されたアプリ内メッセージデータとボタンIDのボタンクリックを記録する。               |
| `hideCurrentInAppMessage()`                               | 現在表示されているアプリ内メッセージを解除する。                                     |
| `performInAppMessageAction(inAppMessage)`                 | アプリ内メッセージのアクションを実行する。                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | アプリ内メッセージボタンのアクションを実行する。                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## メッセージデータを扱う

ほとんどの場合、`Braze.addListener` メソッドを使用して、アプリ内メッセージからのデータを処理するイベントリスナーを登録できます。| 

さらに、`Braze.subscribeToInAppMessage` メソッドを呼び出して、アプリ内メッセージがトリガーされたときに SDK に `inAppMessageReceived` イベントを発行させることで、JavaScript レイヤーのアプリ内メッセージデータにアクセスできます。|アプリ内メッセージがトリガーされてリスナーによって受信されたときに独自のコードを実行するには、このメソッドにコールバックを渡します。

メッセージデータの扱い方をカスタマイズするには、以下の実装例を参照のこと：

{% tabs local %}
{% tab basic %}
デフォルトの行動を強化するため、またはiOSやAndroidのネイティブコードをカスタマイズするアクセス権がない場合は、デフォルトのUIを無効にしながら、アプリ内メッセージイベントをBrazeから受信することをお勧めします。デフォルトの UI を無効にするには、`false` を `Braze.subscribeToInAppMessage` メソッドに渡し、アプリ内メッセージデータを使用して JavaScript で独自のメッセージを作成します。デフォルトのUIを無効にする場合は、メッセージングの分析を手動で行う必要がある。

```javascript
import Braze from "@braze/react-native-sdk";

// Option 1: Listen for the event directly via `Braze.addListener`.
//
// You may use this method to accomplish the same thing if you don't
// wish to make any changes to the default Braze UI.
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  console.log(event.inAppMessage);
});

// Option 2: Call `subscribeToInAppMessage`.
//
// Pass in `false` to disable the automatic display of in-app messages.
Braze.subscribeToInAppMessage(false, (event) => {
  console.log(event.inAppMessage);
  // Use `event.inAppMessage` to construct your own custom message UI.
});
```
{% endtab %}

{% tab advanced %}
組み込み UI を使用してアプリ内メッセージを表示するかどうかを決定するためのより高度なロジックを組み込むには、ネイティブレイヤーを介してアプリ内メッセージを実装します。

{% alert warning %}
これは高度なカスタマイズオプションであるため、デフォルトの Braze 実装をオーバーライドすると、アプリ内メッセージイベントを JavaScript リスナーに送信するロジックも無効になることに注意してください。[アプリ内メッセージデータへのアクセス](#accessing-in-app-message-data)の説明に従って `Braze.subscribeToInAppMessage` または `Braze.addListener` を引き続き使用する場合は、イベントの公開を自分で処理する必要があります。
{% endalert %}

{% subtabs %}
{% subtab Android %}
[カスタムマネージャーリスナー]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)に関する Android の記事で説明されているように、`IInAppMessageManagerListener` を実装します。`beforeInAppMessageDisplayed` 実装では、`inAppMessage` データにアクセスして JavaScript レイヤーに送信し、戻り値に基づいてネイティブメッセージを表示するかどうかを決定できます。

これらの値の詳細については、[Android のドキュメントを]({{site.baseurl}}/developer_guide/in_app_messages/)参照してください。

```java
// In-app messaging
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
    WritableMap parameters = new WritableNativeMap();
    parameters.putString("inAppMessage", inAppMessage.forJsonPut().toString());
    getReactNativeHost()
        .getReactInstanceManager()
        .getCurrentReactContext()
        .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
        .emit("inAppMessageReceived", parameters);
    // Note: return InAppMessageOperation.DISCARD if you would like
    // to prevent the Braze SDK from displaying the message natively.
    return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endsubtab %}
{% subtab iOS %}
### デフォルトの UI デリゲートをオーバーライドする

既定では、`braze` インスタンスを初期化すると、[`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) が作成されて割り当てられます。`BrazeInAppMessageUI` は [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) プロトコルの実装であり、受信したアプリ内メッセージの処理をカスタマイズするために使用できる `delegate` プロパティが付属しています。

1. [こちらの iOS の記事](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)で説明されているように、`BrazeInAppMessageUIDelegate` デリゲートを実装します。

2. `inAppMessage(_:displayChoiceForMessage:)` デリゲートメソッドでは、`inAppMessage` データにアクセスして JavaScript レイヤーに送信し、戻り値に基づいてネイティブメッセージを表示するかどうかを決定できます。

これらの値の詳細については、[iOS のドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/)を参照してください。

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  // Convert the message to a JavaScript representation.
  NSData *inAppMessageData = [message json];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };

  // Send to JavaScript.
  [self sendEventWithName:@"inAppMessageReceived" body:arguments];

  // Note: Return `BRZInAppMessageUIDisplayChoiceDiscard` if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return BRZInAppMessageUIDisplayChoiceNow;
}
```

このデリゲートを使用するには、`braze` インスタンスを初期化した後に `brazeInAppMessagePresenter.delegate` に割り当てます。 

{% alert note %}
`BrazeUI` は Objective-C または Swift でのみインポートできます。Objective-C++ を使用している場合は、これを別のファイルで処理する必要があります。
{% endalert %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```

### デフォルトのネイティブ UI をオーバーライドする

ネイティブ iOS レイヤーでアプリ内メッセージの表示を完全にカスタマイズしたい場合は、[`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) プロトコルに従い、以下のサンプルに従ってカスタムプレゼンターを割り当てます。

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
Braze *braze = [BrazeReactBridge initBraze:configuration];
braze.inAppMessagePresenter = [[MyCustomPresenter alloc] init];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
