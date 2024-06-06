---
nav_title: ニュースフィードカテゴリの定義
article_title: Web 用のニュースフィードカテゴリの定義
platform: Web
page_order: 3
page_type: reference
description: "この記事では、Web アプリケーションのニュースフィードカテゴリを定義する方法について説明します。"
channel: news feed

---

# ニュースフィードカテゴリの定義

> この記事では、Braze Web SDK のニュースフィードカテゴリを定義する方法について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

Braze ニュースフィードのインスタンスは、特定の「カテゴリ」からのカードのみを受信するように構成できます。これにより、1 つのアプリケーション内で複数のニュースフィードストリームを効果的に統合することができます。

ニュースフィードのカテゴリは、次の 3 `allowedCategories` 番目のパラメータを指定することで定義できます`toggleFeed`。

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

次の例のように、フィードにカテゴリを組み合わせて入力することもできます。

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```
