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

|方法 | 説明 |
|---|---|
|`requestContentCardsRefresh()`|Braze SDKサーバーから最新のコンテンツカードを要求するためのバックグラウンドリクエストを送信する。|
|`getContentCardsFromServer(successCallback, errorCallback)`|Braze SDKからコンテンツカードを取得する。これは、最新のコンテンツ・カードをサーバーに要求し、完了するとカードのリストを返す。|
|`getContentCardsFromCache(successCallback, errorCallback)`|Braze SDKからコンテンツカードを取得する。これは、前回の更新時に更新されたローカルキャッシュから最新のカードリストを返す。|
|`logContentCardClicked(cardId)`|指定されたコンテンツカードIDのクリックを記録する。|
|`logContentCardImpression(cardId)`|与えられたコンテンツカードIDのインプレッションを記録する。|
|`logContentCardDismissed(cardId)`|指定されたコンテンツカードIDの退会ログを記録する。|
{: .reset-td-br-1 .reset-td-br-2}

## GIFサポート

{% multi_lang_include wrappers/gif_support/content_cards.md %}
