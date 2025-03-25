---
nav_title: 피드 새로 고침
article_title: Android 및 FireOS용 뉴스피드 새로 고침하기
page_order: 7
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 뉴스피드를 새로 고치는 방법을 보여줍니다."
channel:
  - news feed

---

# 피드 새로 고침

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 뉴스피드를 새로 고치는 방법을 보여줍니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

언제든지 다음을 호출하여 Braze 뉴스피드의 수동 새로 고침을 대기줄에 추가할 수 있습니다.

```java
Braze.requestFeedRefresh()
```

자세한 내용은 [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html)를 참조하세요.


