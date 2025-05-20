# 뉴스피드 새로 고침하기

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 뉴스피드를 새로 고치는 방법을 보여줍니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## 피드 새로 고침

다음 방법을 호출하여 언제든지 Braze 뉴스피드의 수동 새로고침을 대기열에 추가할 수 있습니다. 전체 참조 문서는 [`requestFeedRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html).

```java
Braze.requestFeedRefresh()
```
