{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## メッセージデータを記録する

`BrazeInAppMessage` を使用して分析をログに記録するには、インスタンスを目的の分析関数に渡します。

- `logInAppMessageClicked`
- `logInAppMessageImpression`
- - `logInAppMessageButtonClicked` (ボタンインデックスと共に)

以下に例を示します。

```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## メッセージデータにアクセスする

Flutterアプリでアプリ内メッセージデータにアクセスするために、`BrazePlugin` 、[Dart Streamsを](https://dart.dev/tutorials/language/streams)使ったアプリ内メッセージデータの送信をサポートしている。

`BrazeInAppMessage` オブジェクトは、`uri`、`message`、`header`、`buttons`、`extras` などを含む、ネイティブモデルオブジェクトで使用可能なフィールドのサブセットをサポートします。

### ステップ 1:Dart レイヤーでアプリ内メッセージデータをリッスンする

Dart レイヤーでアプリ内メッセージデータを受信するには、以下のコードを使用して `StreamSubscription` を作成し、`braze.subscribeToInAppMessages()` を呼び出します。不要になったストリームサブスクリプションを忘れずに `cancel()` してください。

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

例としては [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart)を参照のこと。

### ステップ2:アプリ内メッセージデータをネイティブレイヤーから転送する

ステップ 1 の Dart レイヤーでデータを受信するには、次のコードを追加して、ネイティブレイヤーからアプリ内メッセージデータを転送します。

{% tabs %}
{% tab Android %}

アプリ内メッセージデータは Android レイヤーから自動的に転送されます。

{% endtab %}
{% tab iOS %}
{% subtabs %}

アプリ内メッセージデータを転送するには、2つの方法がある：

{% subtab UI Delegate %}

1. [コアアプリ内メッセージデリゲート](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)に関する iOS 記事で説明されているように、`BrazeInAppMessageUIDelegate` デリゲートを実装します。

2. [`willPresent` デリゲート実装](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv)を更新して `BrazePlugin.process(inAppMessage)` を呼び出します。
{% endsubtab %}

{% subtab custom presenter %}
1. アプリ内メッセージ UI が有効になっていることを確認して、`inAppMessagePresenter` をカスタムプレゼンターに設定します。
```swift
    let inAppMessageUI = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = inAppMessageUI
```
2. カスタムプレゼンタークラスを作成して、[`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra) 内で `BrazePlugin.process(inAppMessage)` を呼び出します。
```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    // Pass in-app message data to the Dart layer.
    BrazePlugin.processInAppMessage(message)

    // If you want the default UI to display the in-app message.
    super.present(message: message)
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ 3:アプリ内メッセージのコールバックを再生する（オプション）

コールバックが利用可能になる前にトリガーされたアプリ内メッセージを保存し、設定後に再生するには、`BrazePlugin` の初期化時に次のエントリを `customConfigs` マップに追加します。
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
