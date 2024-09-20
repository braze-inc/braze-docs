---
nav_title: バッジ
article_title: ウェブ用ニュースフィードバッジ
platform: Web
page_order: 3
page_type: reference
description: "この記事では、ニュースフィードの未読カード数を要求し、その情報をウェブアプリケーションのバッジに使用する方法について説明する。"
channel: news feed

---

# バッジ

> この記事では、ニュースフィードの未読カード数を要求し、その情報をウェブアプリケーションのバッジに使用する方法について説明する。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

## 未読のニュースフィードカードカウントのリクエスト

未読カードの数は、以下を呼び出していつでもリクエストできます。

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

これは、ニュースフィードの未読カードの数を示すバッジによく使われる。詳細は[JSDocsを][17]参照のこと。Brazeは、フィードを表示するか、次の関数を呼び出すまで、新しいページのロード時にニュースフィードカードを更新しない（そのため、この関数は0を返す）ことに注意。 `braze.requestFeedRefresh();`

[17]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html
