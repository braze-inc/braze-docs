# ニュースフィードの更新

> このリファレンス記事では、Android または FireOS アプリケーションでニュースフィードを更新する方法について説明します。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## フィードの更新

次のメソッドを呼び出すことで、いつでもブレーズニュースフィードの手動更新をキューに入れることができます。完全なリファレンスドキュメントについては、[`requestFeedRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html) を参照してください。

```java
Braze.requestFeedRefresh()
```
