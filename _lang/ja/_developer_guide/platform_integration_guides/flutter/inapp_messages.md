---
nav_title: アプリ内メッセージ
article_title: Flutter のアプリ内メッセージ
platform: Flutter
page_order: 4
page_type: reference
description: "この記事では、分析のカスタマイズやログ記録など、Flutter を使用した iOS および Android アプリのアプリ内メッセージについて説明します。"
channel: in-app messages

---

# アプリ内メッセージの統合

> Flutter を使用して Android と iOS のアプリ内メッセージを統合およびカスタマイズする方法を学びます。

## アプリ内メッセージの UI を有効にする

Flutter のアプリ内メッセージングを iOS と統合するには、[Braze Swift SDK を使用してアプリ内メッセージングを有効にします]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#enabling-in-app-messages)。Android の場合、これ以外の手順はありません。

## 分析のロギング

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

## 自動表示を無効にする

アプリ内メッセージの自動表示を無効にするには、ネイティブレイヤーでこれらの更新を行います。

{% tabs %}
{% tab Android %}

1. 自動統合初期化機能を使用していることを確認してください。この機能は、バージョン `2.2.0` 以降でデフォルトで有効になっています。
2. 次の行を `braze.xml` ファイルに追加することで、アプリ内メッセージ操作のデフォルトを `DISCARD` に設定します。

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

{% endtab %}
{% tab iOS %}

1. [こちらの iOS の記事](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)で説明されているように、`BrazeInAppMessageUIDelegate` デリゲートを実装します。

2. `.discard` を返すように `inAppMessage(_:displayChoiceForMessage:)` デリゲートメソッドを更新します。

{% endtab %}
{% endtabs %}

## アプリ内メッセージデータの受信

Flutter アプリでアプリ内メッセージデータを受信できるよう、`BrazePlugin` は、[Dart ストリーム](https://dart.dev/tutorials/language/streams)を使用したアプリ内メッセージデータの送信をサポートしています。

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

### オプション 1 - `BrazeInAppMessageUIDelegate` の使用

1. [コアアプリ内メッセージデリゲート](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)に関する iOS 記事で説明されているように、`BrazeInAppMessageUIDelegate` デリゲートを実装します。

2. [`willPresent` デリゲート実装](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv)を更新して `BrazePlugin.process(inAppMessage)` を呼び出します。

### オプション 2 - カスタムのアプリ内メッセージプレゼンター

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

{% endtab %}
{% endtabs %}

#### アプリ内メッセージのコールバックを再生する

コールバックが利用可能になる前にトリガーされたアプリ内メッセージを保存し、設定後に再生するには、`BrazePlugin` の初期化時に次のエントリを `customConfigs` マップに追加します。
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## サンプルのアプリ内メッセージをテストする

次のステップに従って、サンプルのアプリ内メッセージをテストします。

1. `braze.changeUser('your-user-id')` メソッドを呼び出して、React アプリケーションにアクティブユーザーを設定します。
2. ダッシュボードの [**キャンペーン**] ページに移動し、[このガイド]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/)に従って新しいアプリ内メッセージキャンペーンを作成します。
3. テスト用のアプリ内メッセージングキャンペーンを作成し、[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。
4. プッシュ通知をタップすると、デバイスにアプリ内メッセージが表示されます。

## GIFサポート

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

![アプリ内メッセージをテストするため、テスト受信者として自分のユーザー ID を追加できることを示す Braze アプリ内メッセージキャンペーン。]({% image_buster /assets/img/react-native/iam-test.png %}「アプリ内メッセージングテスト」)

