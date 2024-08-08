---
nav_title: バッジ
article_title: Web用ニュースフィードバッジ
platform: Web
page_order: 3
page_type: reference
description: "この記事では、未読のニュースフィードカード数をリクエストし、その情報を使用してウェブアプリケーションのバッジを作成する方法について説明します。"
channel: news feed

---

# バッジ

> この記事では、未読のニュースフィードカード数をリクエストし、その情報を使用してウェブアプリケーションのバッジを作成する方法について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

## 未読のニュースフィードカードカウントのリクエスト

未読カードの数は、以下を呼び出していつでもリクエストできます。

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

これは、未読のニュースフィードカードの数を示すバッジに電力を供給するためによく使用されます。詳細については、 [JSDocs][17] を参照してください。Brazeは、フィードを表示するか、 `braze.requestFeedRefresh();`

[17]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html
