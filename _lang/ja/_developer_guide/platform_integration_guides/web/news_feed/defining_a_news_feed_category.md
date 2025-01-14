---
nav_title: ニュースフィードのカテゴリーを定義する
article_title: ウェブのニュースフィードカテゴリーを定義する
platform: Web
page_order: 3
page_type: reference
description: "この記事では、ウェブアプリケーションのニュース・フィード・カテゴリーを定義する方法を説明する。"
channel: news feed

---

# ニュースフィードカテゴリの定義

> この記事では、Braze Web SDKのニュースフィードカテゴリを定義する方法について説明する。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze ニュースフィードのインスタンスは、特定の「カテゴリ」からのカードのみを受信するように構成できます。これにより、1 つのアプリケーション内で複数のニュースフィードストリームを効果的に統合することができます。

ニュースフィードのカテゴリは、3番目の`allowedCategories` パラメータを`toggleFeed` に与えることで定義できる：

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

次の例のように、フィードにカテゴリーを組み合わせて入力することもできる：

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```
