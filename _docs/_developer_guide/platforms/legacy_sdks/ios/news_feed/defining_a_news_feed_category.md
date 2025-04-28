---
nav_title: Defining a News Feed Category
article_title: Defining a News Feed Category for iOS
platform: iOS
page_order: 4
description: "This reference article shows how to define a News Feed category in your iOS application."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Defining a News Feed category

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Instances of the Braze News Feed can be configured to only receive cards from a certain category. This allows for the effective integration of multiple News Feed streams within a single application. For more information on this feature, visit our News Feed [best practices]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/).

News Feed categories can be defined by calling one of the following methods as you load the News Feed:

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


You can also populate a feed with a combination of categories as in the following example:

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

