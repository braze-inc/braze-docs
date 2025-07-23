---
nav_title: Definieren einer Newsfeed-Kategorie
article_title: Definieren einer Newsfeed-Kategorie für iOS
platform: iOS
page_order: 4
description: "Dieser Referenzartikel beschreibt, wie Sie eine Newsfeed-Kategorie in Ihrer iOS-Anwendung definieren."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Definieren einer Newsfeed-Kategorie

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Instanzen des Braze Newsfeed können so konfiguriert werden, dass sie nur Karten aus einer bestimmten Kategorie empfangen. Dies ermöglicht die effektive Integration mehrerer Newsfeed-Streams in einer einzigen Anwendung. Weitere Informationen zu diesem Feature finden Sie in unseren [Best Practices für]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) Newsfeeds.

Newsfeed-Kategorien können durch den Aufruf einer der folgenden Methoden definiert werden, wenn Sie den Newsfeed laden:

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
{% tab schnell %}

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


Sie können einen Feed auch wie im folgenden Beispiel mit einer Kombination von Kategorien füllen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[newsFeed setCategories:ABKCardCategoryAnnouncements|ABKCardCategoryAdvertising];
```

{% endtab %}
{% tab schnell %}

```swift
newsFeed.categories = ABKCardCategory([.announcements, .advertising])
```

{% endtab %}
{% endtabs %}

