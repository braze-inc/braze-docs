---
nav_title: コンテンツカード
article_title: Flutter のコンテンツカード
platform: Flutter
page_order: 3
page_type: reference
description: "この記事では、Flutter アプリ用のコンテンツカードの使用を開始する方法について説明します。"
channel: content cards

---

# コンテンツカードの統合

> この記事では、Flutter アプリ用のコンテンツカードを設定する方法について説明します。

Braze SDK には、コンテンツカードを使い始めるためのデフォルトのカードフィードが含まれています。カードフィードを表示するには、`braze.launchContentCards()` メソッドを使用できます。Braze SDK に含まれるデフォルトのカードフィードは、ユーザーのコンテンツカードの分析トラッキング、却下、レンダリングをすべて処理します。

## カスタマイズ

これらの追加メソッドを使用すると、[プラグインパブリックインターフェイス][7] で利用可能な次のメソッドを使用して、アプリ内にカスタムコンテンツカードフィードを構築できます。

| 方法                                         | 説明                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Braze SDK サーバーに最新のコンテンツカードを要求します。                                           |
| `braze.logContentCardClicked(contentCard)`    | 指定されたコンテンツカードオブジェクトのクリックを記録します。                                                            |
| `braze.logContentCardImpression(contentCard)` | 指定されたコンテンツカードオブジェクトのインプレッションを記録します。                                                      |
| `braze.logContentCardDismissed(contentCard)`  | 指定されたコンテンツカードオブジェクトが却下されたことを記録します。                                                        |
{: .reset-td-br-1 .reset-td-br-2}

## コンテンツカードデータの受信

Flutter アプリでコンテンツカードデータを受信するために、`BrazePlugin` は [Dart ストリーム](https://dart.dev/tutorials/language/streams)を使用したコンテンツカードデータの送信をサポートしています。

`BrazeContentCard` [オブジェクト](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html)は、`description`、`title`、`image`、`url`、`extras` などを含む、ネイティブモデルオブジェクトで使用可能なフィールドのサブセットをサポートします。

### ステップ 1Dart レイヤーでコンテンツカードデータをリッスンする

Dart レイヤーでコンテンツカードデータを受信するには、以下のコードを使用して `StreamSubscription` を作成し、`braze.subscribeToContentCards()` を呼び出します。不要になったストリームサブスクリプションを忘れずに `cancel()` してください。

\`\`\`dart
// ストリームサブスクリプションを作成
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // コンテンツカードを処理
}

// ストリームのサブスクリプションをキャンセル
contentCardsStreamSubscription.cancel();
\`\`\`

例については、サンプルアプリの [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) を参照してください。

### ステップ 2:ネイティブレイヤーからコンテンツカードデータを転送する

ステップ 1 の Dart レイヤーでデータを受信するには、次のコードを追加して、ネイティブレイヤーからコンテンツカードデータを転送します。

{% tabs %}
{% tab Android %}

コンテンツカードデータは Android レイヤーから自動的に転送されます。

{% endtab %}
{% tab iOS %}

1. [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) のドキュメントの説明に従って、コンテンツカードの最新情報を購読登録するように `contentCards.subscribeToUpdates` を実装します。

2. `contentCards.subscribeToUpdates` コールバックの実装では `BrazePlugin.processContentCards(contentCards)` を呼び出す必要があります。

例については、サンプルアプリの [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) を参照してください。

{% endtab %}
{% endtabs %}

#### コンテンツカードのコールバックを再生する

コールバックが利用可能になる前にトリガーされたコンテンツカードを保存し、設定後に再生するには、`BrazePlugin` の初期化時に次のエントリを `customConfigs` マップに追加します。
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## コンテンツカードのサンプル表示のテスト

コンテンツカードのサンプルをテストする手順は、次のとおりです。

1. `braze.changeUserId('your-user-id')` メソッドを呼び出して、React アプリケーションにアクティブユーザーを設定します。
2. [**キャンペーン**] に移動し、[このガイド][3]に従って新しいコンテンツカードキャンペーンを作成します。
3. コンテンツカードのテストキャンペーンを作成し、[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。
4. プッシュ通知をタップすると、デバイスでコンテンツカードが起動します。フィードを表示するには、フィードを更新する必要が生じる場合があります。

![コンテンツカードをテストするために、テスト受信者として自分のユーザー ID を追加できることを示す Braze コンテンツカードキャンペーン。][4]

各プラットフォームの詳細については、[Android の統合] [5] または [iOS インテグレーション] [6] ガイドを参照してください。


[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create
[4]: {% image_buster /assets/img/react-native/content-card-test.png %} 「コンテンツカードキャンペーンテスト」
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[6]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui
[7]: https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart
