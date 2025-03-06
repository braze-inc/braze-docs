---
nav_title: 배지
article_title: 뉴스피드 배지 Android 및 FireOS용
page_order: 3.2
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 뉴스피드 배지를 추가하고 미열람 뉴스피드 카드 수를 요청하는 방법을 다룹니다."
channel:
  - news feed
  
---

# 배지

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 뉴스피드 배지를 추가하고 미열람 뉴스피드 카드 수를 요청하는 방법을 다룹니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## 미열람 뉴스피드 카드 수 요청

언제든지 다음 번호로 전화하여 읽지 않은 카드의 수를 요청할 수 있습니다:

```java
getUnreadCardCount()
```

자세한 내용은 [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-feed-updated-event/get-unread-card-count.html)을 참조하십시오.

