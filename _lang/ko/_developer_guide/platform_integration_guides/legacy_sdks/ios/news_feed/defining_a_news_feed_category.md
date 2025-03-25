---
nav_title: 뉴스피드 카테고리 정의하기
article_title: iOS용 뉴스피드 카테고리 정의하기
platform: iOS
page_order: 4
description: "이 참조 문서에서는 iOS 애플리케이션에서 뉴스피드 카테고리를 정의하는 방법을 설명합니다."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 뉴스피드 카테고리 정의하기

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze 뉴스피드의 인스턴스는 특정 카테고리의 카드만 수신하도록 구성할 수 있습니다. 이를 통해 단일 애플리케이션 내에서 여러 개의 뉴스피드 스트림을 효과적으로 통합할 수 있습니다. 이 기능에 대한 자세한 내용은 뉴스피드 [모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/)를 참조하세요.

뉴스피드를 로드할 때 다음 메서드 중 하나를 호출하여 뉴스피드 카테고리를 정의할 수 있습니다:

{% tabs %}
{% tab 목표-C %}

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


다음 예시와 같이 여러 카테고리의 조합으로 피드를 채울 수도 있습니다:

{% tabs %}
{% tab 목표-C %}

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

