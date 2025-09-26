{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## メッセージの種類

{% tabs %}
{% multi_lang_include developer_guide/_shared/push_notifications/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/push_notifications/message_types/swift.md %}
{% endtabs %}

## データモデル

アプリ内メッセージのモデルは、React Native SDK で利用できます。Braze には、同じデータ モデルを共有する4つのアプリ内メッセージタイプ (**スライドアップ**、**モーダル**、**フル**、**HTML フル**) があります。

### メッセージ

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

### ボタン

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
