# Refreshing a News Feed

> This reference article shows how to refresh the News Feed in your Android or FireOS application.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Refreshing the feed

You can queue a manual refresh of the Braze News Feed at any time by calling the following method. For full reference documentation, see [`requestFeedRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html).

```java
Braze.requestFeedRefresh()
```
