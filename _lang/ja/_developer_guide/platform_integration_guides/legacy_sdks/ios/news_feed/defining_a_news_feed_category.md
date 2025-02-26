---
nav_title: ニュースフィードのカテゴリーを定義する
article_title: iOS のニュースフィードカテゴリーを定義する
platform: iOS
page_order: 4
description: "この参照記事では、iOS アプリケーションでニュースフィードカテゴリーを定義する方法を紹介します。"
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# ニュースフィードカテゴリの定義

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze ニュースフィードのインスタンスは、特定のカテゴリーからのカードのみを受信するように構成できます。これにより、1 つのアプリケーション内で複数のニュースフィードストリームを効果的に統合することができます。この機能の詳細については、ニュースフィードの[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/)をご覧ください。

ニュースフィードのカテゴリーは、ニュースフィードを読み込むときに以下のメソッドのいずれかを呼び出すことで定義できます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[newsFeed setCategories:ABKCardCategoryAll];
[newsFeed setCategories:ABKCardCategoryAnnouncements];
[newsFeed setCategories:ABKCardCategoryAdvertising];
[newsFeed setCategories:ABKCardCategorySocial];
[newsFeed setCategories:ABKCardCategoryNews];
[newsFeed setCategories:ABKCardCategoryNoCategory];
```

{% endtab %}
{% tab swift %}

```swift
newsFeed.categories = ABKCardCategory.all
newsFeed.categories = ABKCardCategory.announcements
newsFeed.categories = ABKCardCategory.advertising
newsFeed.categories = ABKCardCategory.social
newsFeed.categories = ABKCardCategory.news
newsFeed.categories = ABKCardCategory.noCategory
```

{% endtab %}
{% endtabs %}


次の例のように、カテゴリの組み合わせをフィードに取り込むこともできます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[newsFeed setCategories:ABKCardCategoryAnnouncements|ABKCardCategoryAdvertising];
```

{% endtab %}
{% tab swift %}

```swift
newsFeed.categories = ABKCardCategory([.announcements, .advertising])
```

{% endtab %}
{% endtabs %}

