{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## カードフィード

Braze SDK にはデフォルトのカードフィードが含まれています。デフォルトのカードフィードを表示するには、`launchContentCards()` メソッドを使用します。このメソッドは、ユーザーのコンテンツカードの分析トラッキング、却下、レンダリングをすべて行います。

## コンテンツカード

以下の追加メソッドを使用して、アプリ内にカスタムコンテンツカードフィードを構築できます。

|方法 | 説明 |
|---|---|
|`requestContentCardsRefresh()`|Braze SDKサーバーから最新のコンテンツカードを要求するためのバックグラウンドリクエストを送信する。|
|`getContentCardsFromServer(successCallback, errorCallback)`|Braze SDKからコンテンツカードを取得する。これにより、サーバーから最新のコンテンツカードが要求され、完了時にカードのリストが返されます。||
|`getContentCardsFromCache(successCallback, errorCallback)`|Braze SDKからコンテンツカードを取得する。これは、前回の更新時に更新されたローカルキャッシュから最新のカードリストを返す。|
|`logContentCardClicked(cardId)`|指定されたコンテンツカードIDのクリックを記録する。|
|`logContentCardImpression(cardId)`|与えられたコンテンツカードIDのインプレッションを記録する。|
|`logContentCardDismissed(cardId)`|指定されたコンテンツカード ID が閉じられたことを記録します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
