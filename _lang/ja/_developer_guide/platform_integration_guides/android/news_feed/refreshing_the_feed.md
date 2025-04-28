---
nav_title: フィードの更新
article_title: Android と FireOS のニュースフィードの更新
page_order: 7
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android または FireOS アプリケーションでニュースフィードを更新する方法について説明します。"
channel:
  - news feed

---

# フィードの更新

> このリファレンス記事では、Android または FireOS アプリケーションでニュースフィードを更新する方法について説明します。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

以下を呼び出すことで、Braze ニュースフィードの手動更新をいつでもキューに入れることができます。

```java
Braze.requestFeedRefresh()
```

詳細については、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html) を参照してください。


