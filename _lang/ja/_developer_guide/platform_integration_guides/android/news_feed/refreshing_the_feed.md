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

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュースフィードツールを利用しているお客様に、コンテンツカードのメッセージングチャネルへの移行をお勧めしています。移行により、柔軟性、カスタマイズ性、信頼性が向上します。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

以下を呼び出すことで、Braze ニュースフィードの手動更新をいつでもキューに入れることができます。

```java
Braze.requestFeedRefresh()
```

詳細については、[KDoc][16] を参照してください。


[16]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html
