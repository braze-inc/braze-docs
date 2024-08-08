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

\`\`\`javascript
import Braze from "@braze/react-native-sdk";

// オプション 1: `Braze.addListener` を介して直接イベントをリッスンします。
//
// You may use this method to accomplish the same thing if you don't
// デフォルトの Braze UI に変更を加えたい。
Braze.addListener(Braze.Events.IN\_APP\_MESSAGE\_RECEIVED, (event) => {
console.log(event.inAppMessage);
  });

// オプション2: `subscribeToInAppMessage` を呼び出します。
`false` を //
// Pass in  してアプリ内メッセージの自動表示を無効にします。
Braze.subscribeToInAppMessage(false, (event) => {
console.log(event.inAppMessage);
  // `event.inAppMessage` を使用して、独自のカスタムメッセージ UI を作成します。
  });
\`\`\`

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
\`\`\`objc
\- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI \*)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw \*)message {
// Convert the message to a JavaScript representation.
NSData *inAppMessageData = [message json];
NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
NSDictionary *arguments = @{
@"inAppMessage" : inAppMessageString
};

  // JavaScript に送信します。
  [self sendEventWithName:@"inAppMessageReceived" body:arguments];

  // 注: もし以下のようにしたい場合、`BRZInAppMessageUIDisplayChoiceDiscard` を返してください。
  // Braze SDK がメッセージをネイティブに表示したい。
  BRZInAppMessageUIDisplayChoiceNow を返す。
}
\`\`\`
{% endsubtab %}
{% endsubtabs %}

このデリゲートを使用するには、`braze` インスタンスを初期化した後に `brazeInAppMessagePresenter.delegate` に割り当てます。 

{% alert note %}
`BrazeUI` は Objective-C または Swift でのみインポートできます。Objective-C++ を使用している場合は、これを別のファイルで処理する必要があります。
{% endalert %}

{% subtabs %}
{% subtab OBJECTIVE-C %}
\`\`\`objc
@import BrazeUI;

- (BOOL)application:(UIApplication \*)application didFinishLaunchingWithOptions:(NSDictionary \*)launchOptions {
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
Braze *braze = [BrazeReactBridge initBraze:configuration];
((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
AppDelegate.braze = braze;
}
  \`\`\`
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

| 方法 | 説明 |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | 提供されたアプリ内メッセージ データのクリックをログに記録します。                                    |
| `logInAppMessageImpression(inAppMessage)`                 | 提供されたアプリ内メッセージデータのインプレッションをログに記録します。                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | 提供されたアプリ内メッセージデータとボタン ID のボタンクリックをログに記録します。               |
| `hideCurrentInAppMessage()`| 現在表示されているアプリ内メッセージを閉じます。 |
| `performInAppMessageAction(inAppMessage)`| アプリ内メッセージのアクションを実行します。 |
| `performInAppMessageButtonAction(inAppMessage, buttonId)`| アプリ内メッセージボタンのアクションを実行します。 |

## サンプルのアプリ内メッセージの表示をテストする

次のステップに従って、サンプルのアプリ内メッセージをテストします。

1. `Braze.changeUserId('your-user-id')` メソッドを呼び出して、React アプリケーションにアクティブユーザーを設定します。
2. [**キャンペーン**] に移動し、[このガイド][5]に従って新しいアプリ内メッセージキャンペーンを作成します。
3. テスト用のアプリ内メッセージングキャンペーンを作成し、[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。すぐにデバイスでアプリ内メッセージを起動できるようになるはずです。

![アプリ内メッセージをテストするため、テスト受信者として自分のユーザー ID を追加できることを示す Braze アプリ内メッセージキャンペーン。][6]

サンプル実装は、[React Native SDK][7] 内の BrazeProject にあります。追加の Android および iOS 実装サンプルは、[Android][8] および [iOS][9] SDK にあります。

## アプリ内メッセージのデータモデル

アプリ内メッセージのモデルは、React Native SDK で利用できます。Braze には、同じデータ モデルを共有する4つのアプリ内メッセージタイプ (**スライドアップ**、**モーダル**、**フル**、**HTML フル**) があります。

### アプリ内メッセージモデルのプロパティ

アプリ内メッセージモデルは、すべてのアプリ内メッセージのベースを提供します。

|プロパティ| 説明 |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString`|メ ッセージの JSON 表現。 |
|`message`| メッセージテキスト。 |
|`header`| メッセージヘッダー。 |
|`uri`| ボタンのクリックアクションに関連付けられた URI。 |
|`imageUrl`| メッセージ画像の URL。 |
|`zippedAssetsUrl`| HTML コンテンツを表示するために準備された圧縮アセット。 |
|`useWebView`| ボタンのクリックアクションを Web ビューを使用してリダイレクトするかどうかを示します。 |
|`duration`| メッセージの表示期間。 |
|`clickAction`| ボタンのクリックアクションのタイプ。3つのタイプは次のとおりです。`NEWS_FEED`、 `URI`、`NONE`。 |
|`dismissType`| メッセージのクローズタイプ。2つのタイプは次のとおりです。`SWIPE` および`AUTO_DISMISS`。 |
|`messageType`| SDKでサポートされているアプリ内メッセージのタイプ。4つのタイプは次のとおりです。`SLIDEUP`、`MODAL`、`FULL` および `HTML_FULL`。 |
|`extras`| メッセージエクストラ辞書。デフォルト値: `[:]`.                                                                   |
|`buttons`| アプリ内メッセージのボタンのリスト。 |
|`toString()`| 文字列表現としてのメッセージ。 |
{: .reset-td-br-1 .reset-td-br-2}

アプリ内メッセージモデルの完全なリファレンスについては、[Android][10] および [iOS][11] のドキュメントを参照してください。

### アプリ内メッセージボタンモデルのプロパティ

アプリ内メッセージにボタンを追加して、アクションを実行したり、分析をログに記録したりできます。ボタンモデルは、すべてのアプリ内メッセージボタンのベースを提供します。

|プロパティ| 説明 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`| ボタン上のテキスト。 |
|`uri`| ボタンのクリックアクションに関連付けられた URI。 |
|`useWebView`| ボタンのクリックアクションを Web ビューを使用してリダイレクトするかどうかを示します。 |
|`clickAction`| ユーザーがボタンをクリックしたときに処理されるクリック アクションのタイプ。3つのタイプは次のとおりです。`NEWS_FEED`、`URI`、そして `NONE`。 |
|`id`| メッセージのボタン ID。 |
|`toString()`| 文字列表現としてのボタン。 |
{: .reset-td-br-1 .reset-td-br-2}

ボタンモデルの完全なリファレンスについては、[Android][12] および [iOS][13] のドキュメントを参照してください。

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#step-1-implement-an-in-app-message-manager-listener
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[6]: {% image_buster /assets/img/react-native/iam-test.png %} 「アプリ内メッセージングテスト」
[7]: https://github.com/braze-inc/braze-react-native-sdk
[8]: https://github.com/braze-inc/braze-android-sdk
[9]: https://github.com/braze-inc/braze-swift-sdk
[10]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html
[11]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage
[12]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html
[13]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button
