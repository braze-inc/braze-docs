## Flutterのコンテンツカードについて

Braze SDK には、コンテンツカードを使い始めるためのデフォルトのカードフィードが含まれています。カードフィードを表示するには、`braze.launchContentCards()` メソッドを使用できます。Braze SDK に含まれるデフォルトのカードフィードは、ユーザーのコンテンツカードの分析トラッキング、却下、レンダリングをすべて処理します。

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## カードメソッド

[プラグインパブリックインターフェイス](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart)で使用可能な以下のメソッドを使用して、アプリ内にカスタムコンテンツカードフィードを構築できます。

| 方法                                         | 説明                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Braze SDK サーバーから最新のコンテンツカードをリクエストします。                                           |
| `braze.logContentCardClicked(contentCard)`    | 指定されたコンテンツカードオブジェクトのクリックを記録します。                                                            |
| `braze.logContentCardImpression(contentCard)` | 指定されたコンテンツカードオブジェクトのインプレッションを記録します。                                                      |
| `braze.logContentCardDismissed(contentCard)`  | 指定されたコンテンツカードオブジェクトの却下を記録します。                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## コンテンツカードデータの受信

Flutter アプリでコンテンツカードデータを受信するために、`BrazePlugin` は [Dart ストリーム](https://dart.dev/tutorials/language/streams)を使用したコンテンツカードデータの送信をサポートしています。

`BrazeContentCard` [オブジェクト](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html)は、`description`、`title`、`image`、`url`、`extras` などを含む、ネイティブモデルオブジェクトで使用可能なフィールドのサブセットをサポートしています。

### Dart レイヤーでコンテンツカードデータをリッスンする

Dart レイヤーでコンテンツカードデータを受信するには、以下のコードを使用して `StreamSubscription` を作成し、`braze.subscribeToContentCards()` を呼び出します。不要になったストリームサブスクリプションは忘れずに `cancel()` してください。

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

例については、Braze Flutter SDK サンプルアプリケーションの [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) を参照してください。

### ネイティブ iOS レイヤーからコンテンツカードデータを転送する

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

コンテンツカードデータは Android と iOS の両方のネイティブレイヤーから自動的に転送されます。追加のセットアップは必要ありません。

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Flutter SDK 17.1.0 以前を使用している場合、iOS ネイティブレイヤーからのコンテンツカードデータ転送には手動セットアップが必要です。アプリケーションには、`BrazePlugin.processContentCards(contentCards)` を呼び出す `contentCards.subscribeToUpdates` コールバックが含まれている可能性があります。Flutter SDK 18.0.0 に移行するには、`BrazePlugin.processContentCards(_:)` の呼び出しを削除してください。データ転送は自動的に処理されるようになりました。

例については、Braze Flutter SDK サンプルアプリケーションの [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) を参照してください。

{% endtab %}
{% endtabs %}

#### コンテンツカードのコールバックを再生する

コールバックが利用可能になる前にトリガーされたコンテンツカードを保存し、設定後に再生するには、`BrazePlugin` の初期化時に次のエントリを `customConfigs` マップに追加します。
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
