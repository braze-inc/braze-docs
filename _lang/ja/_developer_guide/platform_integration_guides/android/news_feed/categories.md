---
nav_title: ニュースフィードカテゴリの定義
article_title: Android と FireOS のニュースフィードカテゴリの定義
page_order: 3
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android または FireOS アプリケーションでニュースフィードカテゴリを定義する方法を示します。"
channel:
  - news feed
  
---

# ニュースフィードカテゴリの定義

このリファレンス記事では、Android または FireOS アプリケーションでニュースフィードカテゴリを定義する方法を示します。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze ニュースフィードのインスタンスは、特定の「カテゴリ」からのカードのみを受信するように構成できます。これにより、1 つのアプリケーション内で複数のニュースフィードストリームを効果的に統合することができます。この機能について詳しくは、ニュースフィードの[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/)をご覧ください。

ニュースフィードのカテゴリは、ニュースフィードを読み込むときに以下のメソッドを呼び出すことで定義できます。

```xml
newsFeed.setCategories(CardCategory.ALL_CATEGORIES);
newsFeed.setCategories(CardCategory.ADVERTISING);
newsFeed.setCategories(CardCategory.ANNOUNCEMENTS);
newsFeed.setCategories(CardCategory.NEWS);
newsFeed.setCategories(CardCategory.SOCIAL);
newsFeed.setCategories(CardCategory.NO_CATEGORY);
```

次の例のように、カテゴリの組み合わせをフィードに取り込むこともできます。

```xml
newsFeed.setCategories:EnumSet.of(CardCategory.ANNOUNCEMENTS, CardCategory.NEWS);
```


