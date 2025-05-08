---
nav_title: アプリ内メッセージ
article_title: React Native のアプリ内メッセージ
platform: React Native
page_order: 4
page_type: reference
description: "この記事では、分析のカスタマイズやログ記録など、React Native を使用した iOS および Android アプリのアプリ内メッセージについて説明します。"
channel: in-app messages

---

# アプリ内メッセージの統合

> React Native を使用すると、ネイティブのアプリ内メッセージが Android および iOS に自動的に表示されます。この記事では、React Native を使用したアプリのアプリ内メッセージの分析のカスタマイズとログ記録について説明します。

## アプリ内メッセージデータへのアクセス

ほとんどの場合、`Braze.addListener` メソッドを使用して、アプリ内メッセージからのデータを処理するイベントリスナーを登録できます。| 

さらに、`Braze.subscribeToInAppMessage` メソッドを呼び出して、アプリ内メッセージがトリガーされたときに SDK に `inAppMessageReceived` イベントを発行させることで、JavaScript レイヤーのアプリ内メッセージデータにアクセスできます。|アプリ内メッセージがトリガーされてリスナーによって受信されたときに独自のコードを実行するには、このメソッドにコールバックを渡します。

デフォルトの動作をさらにカスタマイズする場合、またはネイティブ iOS または Android コードをカスタマイズするアクセス権がない場合は、Braze からアプリ内メッセージ イベントを受信しながらデフォルト UI を無効にすることをお勧めします。デフォルトの UI を無効にするには、`false` を `Braze.subscribeToInAppMessage` メソッドに渡し、アプリ内メッセージデータを使用して JavaScript で独自のメッセージを作成します。デフォルトの UI を無効にすることを選択した場合は、メッセージ[の分析を手動でログに記録する](#analytics)必要があることに注意してください。

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

## 高度なカスタマイズ

組み込み UI を使用してアプリ内メッセージを表示するかどうかを決定するためのより高度なロジックを組み込むには、ネイティブレイヤーを介してアプリ内メッセージを実装します。

{% alert warning %}
これは高度なカスタマイズオプションであるため、デフォルトの Braze 実装をオーバーライドすると、アプリ内メッセージイベントを JavaScript リスナーに送信するロジックも無効になることに注意してください。[アプリ内メッセージデータへのアクセス](#accessing-in-app-message-data)の説明に従って `Braze.subscribeToInAppMessage` または `Braze.addListener` を引き続き使用する場合は、イベントの公開を自分で処理する必要があります。
{% endalert %}

{% tabs %}
{% tab Android %}

[カスタムマネージャーリスナー]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener)に関する Android の記事で説明されているように、`IInAppMessageManagerListener` を実装します。`beforeInAppMessageDisplayed` 実装では、`inAppMessage` データにアクセスして JavaScript レイヤーに送信し、戻り値に基づいてネイティブメッセージを表示するかどうかを決定できます。

これらの値の詳細については、[Android のドキュメントを]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/)参照してください。

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
{% endtab %}
{% tab iOS %}
### デフォルトの UI デリゲートをオーバーライドする

既定では、`braze` インスタンスを初期化すると、[`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/) が作成されて割り当てられます。`BrazeInAppMessageUI` は [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) プロトコルの実装であり、受信したアプリ内メッセージの処理をカスタマイズするために使用できる `delegate` プロパティが付属しています。

1. [こちらの iOS の記事](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)で説明されているように、`BrazeInAppMessageUIDelegate` デリゲートを実装します。

2. `inAppMessage(_:displayChoiceForMessage:)` デリゲートメソッドでは、`inAppMessage` データにアクセスして JavaScript レイヤーに送信し、戻り値に基づいてネイティブメッセージを表示するかどうかを決定できます。

これらの値の詳細については、[iOS のドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/)を参照してください。

{% subtabs %}
{% subtab OBJECTIVE-C %}
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
{% endsubtab %}
{% endsubtabs %}

このデリゲートを使用するには、`braze` インスタンスを初期化した後に `brazeInAppMessagePresenter.delegate` に割り当てます。 

{% alert note %}
`BrazeUI` は Objective-C または Swift でのみインポートできます。Objective-C++ を使用している場合は、これを別のファイルで処理する必要があります。
{% endalert %}

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

### デフォルトのネイティブ UI をオーバーライドする

ネイティブ iOS レイヤーでアプリ内メッセージの表示を完全にカスタマイズしたい場合は、[`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) プロトコルに従い、以下のサンプルに従ってカスタムプレゼンターを割り当てます。

{% subtabs %}
{% subtab OBJECTIVE-C %}
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

## 分析とアクション方法

これらのメソッドを使用するには、`BrazeInAppMessage` インスタンスを渡して分析をログに記録し、アクションを実行します。

| 方法                                                    | 説明                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | 提供されたアプリ内メッセージデータのクリックを記録する。                                    |
| `logInAppMessageImpression(inAppMessage)`                 | 提供されたアプリ内メッセージデータのインプレッションを記録する。                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | 提供されたアプリ内メッセージデータとボタンIDのボタンクリックを記録する。               |
| `hideCurrentInAppMessage()`                               | 現在表示されているアプリ内メッセージを解除する。                                     |
| `performInAppMessageAction(inAppMessage)`                 | アプリ内メッセージのアクションを実行する。                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | アプリ内メッセージボタンのアクションを実行する。                                     |

## サンプルのアプリ内メッセージの表示をテストする

次のステップに従って、サンプルのアプリ内メッセージをテストします。

1. `Braze.changeUserId('your-user-id')` メソッドを呼び出して、React アプリケーションにアクティブユーザーを設定します。
2. [**キャンペーン**] に移動し、[このガイド]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/)に従って新しいアプリ内メッセージキャンペーンを作成します。
3. テスト用のアプリ内メッセージングキャンペーンを作成し、[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。すぐにデバイスでアプリ内メッセージを起動できるようになるはずです。

![自分のユーザーIDをテスト受信者として追加し、アプリ内メッセージをテストできることを示すBrazeアプリ内メッセージキャンペーン。]({% image_buster /assets/img/react-native/iam-test.png %} "In-App Messaging Test")

サンプル実装は、[React Native SDK](https://github.com/braze-inc/braze-react-native-sdk)内のBrazeProjectにある。その他のAndroidとiOSの実装サンプルは、[Androidと](https://github.com/braze-inc/braze-android-sdk) [iOS](https://github.com/braze-inc/braze-swift-sdk)SDKにある。

## アプリ内メッセージのデータモデル

アプリ内メッセージのモデルは、React Native SDK で利用できます。Braze には、同じデータ モデルを共有する4つのアプリ内メッセージタイプ (**スライドアップ**、**モーダル**、**フル**、**HTML フル**) があります。

### アプリ内メッセージモデルのプロパティ

アプリ内メッセージモデルは、すべてのアプリ内メッセージのベースを提供します。

|プロパティ          | 説明                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | メッセージのJSON表現。                                                                                |
|`message`         | メッセージテキスト。                                                                                                      |
|`header`          | メッセージのヘッダーである。                                                                                                    |
|`uri`             | ボタンをクリックするアクションに関連するURI。                                                                       |
|`imageUrl`        | メッセージ画像のURL。                                                                                                 |
|`zippedAssetsUrl` | HTMLコンテンツを表示するために準備されたzip圧縮された資産。                                                                    |
|`useWebView`      | ボタンをクリックしたアクションがウェブビューを使ってリダイレクトされるかどうかを示す。                                            |
|`duration`        | メッセージの表示時間。                                                                                          |
|`clickAction`     | ボタンのクリックアクションのタイプ。3つのタイプは次のとおりです。`NEWS_FEED`、`URI`、そして `NONE`。                                     |
|`dismissType`     | メッセージのクローズタイプ。2つのタイプは次のとおりです。`SWIPE` および`AUTO_DISMISS`。                                                 |
|`messageType`     | SDKがサポートするアプリ内メッセージタイプ。4つのタイプは次のとおりです。`SLIDEUP`、`MODAL`、`FULL` および `HTML_FULL`。          |
|`extras`          | メッセージエクストラ辞書。デフォルト値：`[:]`.                                                                   |
|`buttons`         | アプリ内メッセージのボタン一覧。                                                                             |
|`toString()`      | String表現としてのメッセージ。                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

アプリ内メッセージモデルの完全なリファレンスについては、[[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html)] および [[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage)] のドキュメントを参照してください。

### アプリ内メッセージボタンモデルのプロパティ

アプリ内メッセージにボタンを追加して、アクションを実行したり、分析をログに記録したりできます。ボタンモデルは、すべてのアプリ内メッセージボタンのベースを提供します。

|プロパティ          | 説明                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | ボタンのテキスト。                                                                                                     |
|`uri`             | ボタンをクリックするアクションに関連するURI。                                                                            |
|`useWebView`      | ボタンをクリックしたアクションがウェブビューを使ってリダイレクトされるかどうかを示す。                                                 |
|`clickAction`     | ユーザーがボタンをクリックしたときに処理されるクリックアクションのタイプ。3つのタイプは次のとおりです。`NEWS_FEED`、`URI`、そして `NONE`。 |
|`id`              | メッセージのボタンID。                                                                                               |
|`toString()`      | String表現としてのボタン。                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ボタンモデルの完全なリファレンスについては、[[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html)] および [[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button)] のドキュメントを参照してください。

## GIFサポート

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

