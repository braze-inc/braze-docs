---
nav_title: バッジ
article_title: Android および FireOS 用のニュースフィードバッジ
page_order: 3.2
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android または FireOS アプリケーションにニュースフィードバッジを追加し、未読のニュースフィードカード数を要求する方法について説明します。"
channel:
  - news feed
  
---

# バッジ

> このリファレンス記事では、Android または FireOS アプリケーションにニュースフィードバッジを追加し、未読のニュースフィードカード数を要求する方法について説明します。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## 未読のニュースフィードカードカウントのリクエスト

未読カードの数は、以下を呼び出していつでもリクエストできます。

```java
getUnreadCardCount()
```

詳細については、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-feed-updated-event/get-unread-card-count.html) を参照してください。

