---
nav_title: コンテンツカード
article_title: コンテンツカードの統合
page_order: 2
---

# コンテンツカードの統合

> Cordova Braze SDK のコンテンツ カードを統合する方法を学びます。

{% multi_lang_include cordova/prerequisites.md %}

## カードフィード

Braze SDK にはデフォルトのカードフィードが含まれています。デフォルトのカードフィードを表示するには、`launchContentCards()` メソッドを使用します。このメソッドは、ユーザーのコンテンツカードの分析トラッキング、却下、レンダリングをすべて行います。

## コンテンツカード

以下の追加メソッドを使用して、アプリ内にカスタムコンテンツカードフィードを構築できます。

|メソッド | 説明 |
|---|---|
|`requestContentCardsRefresh()`|Braze SDK サーバーから最新のコンテンツカードを要求するバックグラウンドリクエストを送信します。|
|`getContentCardsFromServer(successCallback, errorCallback)`|Braze SDK からコンテンツカードを取得します。これにより、サーバーから最新のコンテンツカードが要求され、完了時にカードのリストが返されます。|
|`getContentCardsFromCache(successCallback, errorCallback)`|Braze SDK からコンテンツカードを取得します。これにより、前回の更新時に更新された最新のカードリストがローカルキャッシュから返されます。|
|`logContentCardClicked(cardId)`|指定されたコンテンツカード ID のクリックを記録します。|
|`logContentCardImpression(cardId)`|指定されたコンテンツカード ID のインプレッションを記録します。|
|`logContentCardDismissed(cardId)`|指定されたコンテンツカード ID が閉じられたことを記録します。|
{: .reset-td-br-1 .reset-td-br-2}
