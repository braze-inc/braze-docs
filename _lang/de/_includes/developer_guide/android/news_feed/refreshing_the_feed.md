# Aktualisieren eines Newsfeeds

> Dieser Referenzartikel zeigt, wie Sie den News Feed in Ihrer Android- oder FireOS-Anwendung aktualisieren können.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Aktualisieren des Feeds

Sie können jederzeit eine manuelle Aktualisierung des Braze Newsfeeds in die Warteschlange stellen, indem Sie die folgende Methode aufrufen. Die vollständige referenzierte Dokumentation finden Sie unter [`requestFeedRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html).

```java
Braze.requestFeedRefresh()
```
