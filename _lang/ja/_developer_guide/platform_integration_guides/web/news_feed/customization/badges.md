---
nav_title: バッジ
article_title: ウェブ用ニュースフィードバッジ
platform: Web
page_order: 3
page_type: reference
description: "この記事では、未読のニュースフィードカード数をリクエストし、その情報を使用して Web アプリケーションのバッジを強化する方法について説明します。"
channel: news feed

---

# バッジ

> この記事では、未読のニュースフィードカード数をリクエストし、その情報を使用して Web アプリケーションのバッジを強化する方法について説明します。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## 未読のニュースフィードカードカウントのリクエスト

未読カードの数は、以下を呼び出していつでもリクエストできます。

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

これは、未読のニュースフィードカードの数を示すバッジを強化するためによく使用されます。詳細については[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html)を参照してください。Brazeは、フィードを表示するか、次の関数を呼び出すまで、新しいページのロード時にニュースフィードカードを更新しない（そのため、この関数は0を返す）ことに注意。 `braze.requestFeedRefresh();`

