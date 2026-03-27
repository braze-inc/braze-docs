{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## メッセージデータの記録

`BrazeInAppMessage` を使用して分析をログに記録するには、インスタンスを目的の分析関数に渡します。

- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (ボタンインデックスと共に)

以下に例を示します。

```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## メッセージデータへのアクセス

Flutter アプリでアプリ内メッセージデータにアクセスするために、`BrazePlugin` は [Dart Streams](https://dart.dev/tutorials/language/streams) を使用したアプリ内メッセージデータの送信をサポートしています。

`BrazeInAppMessage` オブジェクトは、`uri`、`message`、`header`、`buttons`、`extras` などを含む、ネイティブモデルオブジェクトで使用可能なフィールドのサブセットをサポートします。

### Dart レイヤーでアプリ内メッセージデータをリッスンする

Dart レイヤーでアプリ内メッセージデータを受信するには、以下のコードを使用して `StreamSubscription` を作成し、`braze.subscribeToInAppMessages()` を呼び出します。不要になったストリームサブスクリプションは忘れずに `cancel()` してください。

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

例については、Braze Flutter SDK サンプルアプリケーションの [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) を参照してください。

### ネイティブレイヤーからアプリ内メッセージデータを転送する

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

アプリ内メッセージデータは Android と iOS の両方のネイティブレイヤーから自動的に転送されます。追加のセットアップは必要ありません。

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Flutter SDK 17.1.0 以前を使用している場合、iOS ネイティブレイヤーからのアプリ内メッセージデータの転送には手動セットアップが必要です。アプリケーションには以下のいずれかが含まれている可能性があります。Flutter SDK 18.0.0 に移行するには、`BrazePlugin.processInAppMessage(_:)` の呼び出しを削除してください。データの転送は自動的に処理されるようになりました。

{% subtabs %}
{% subtab UI Delegate %}

[`willPresent` デリゲート実装](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv)から `BrazePlugin.processInAppMessage(_:)` の呼び出しを削除してください。

{% endsubtab %}

{% subtab Custom presenter %}

カスタムプレゼンターの [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra) 実装から `BrazePlugin.processInAppMessage(message)` の呼び出しを削除してください。

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

### アプリ内メッセージのコールバックを再実行する（オプション）

コールバックが利用可能になる前にトリガーされたアプリ内メッセージを保存し、設定後に再生するには、`BrazePlugin` の初期化時に次のエントリを `customConfigs` マップに追加します。
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
