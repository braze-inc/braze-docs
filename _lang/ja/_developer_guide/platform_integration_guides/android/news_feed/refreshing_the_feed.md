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
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

以下を呼び出すことで、Braze ニュースフィードの手動更新をいつでもキューに入れることができます。

```java
Braze.requestFeedRefresh()
```

詳細については、[KDoc][16] を参照してください。


[16]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html
