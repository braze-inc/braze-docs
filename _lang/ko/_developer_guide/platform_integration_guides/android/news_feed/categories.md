---
nav_title: 뉴스피드 카테고리 정의하기
article_title: Android 및 FireOS용 뉴스피드 카테고리 정의하기
page_order: 3
platform: 
  - Android
  - FireOS
description: "이 참고 문서에서는 Android 또는 FireOS 애플리케이션에서 뉴스피드 카테고리를 정의하는 방법을 보여줍니다."
channel:
  - news feed
  
---

# 뉴스피드 카테고리 정의하기

이 참고 문서에서는 Android 또는 FireOS 애플리케이션에서 뉴스피드 카테고리를 정의하는 방법을 보여줍니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze 뉴스피드의 인스턴스는 특정 '카테고리'의 카드만 수신하도록 구성할 수 있습니다. 이를 통해 단일 애플리케이션 내에서 여러 개의 뉴스피드 스트림을 효과적으로 통합할 수 있습니다. 이 기능에 대한 자세한 내용은 뉴스피드 [모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/)를 참조하세요.

뉴스피드를 로드할 때 다음 메서드를 호출하여 뉴스피드 카테고리를 정의할 수 있습니다.

```xml
newsFeed.setCategories(CardCategory.ALL_CATEGORIES);
newsFeed.setCategories(CardCategory.ADVERTISING);
newsFeed.setCategories(CardCategory.ANNOUNCEMENTS);
newsFeed.setCategories(CardCategory.NEWS);
newsFeed.setCategories(CardCategory.SOCIAL);
newsFeed.setCategories(CardCategory.NO_CATEGORY);
```

다음 예시와 같이 여러 카테고리의 조합으로 피드를 채울 수도 있습니다:

```xml
newsFeed.setCategories:EnumSet.of(CardCategory.ANNOUNCEMENTS, CardCategory.NEWS);
```


