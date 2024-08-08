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

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュースフィードツールを利用しているお客様に、コンテンツカードのメッセージングチャネルへの移行をお勧めしています。移行により、柔軟性、カスタマイズ性、信頼性が向上します。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

## 未読のニュースフィードカードカウントのリクエスト

未読カードの数は、以下を呼び出していつでもリクエストできます。

```java
getUnreadCardCount()
```

詳細については、[KDoc][17] を参照してください。

[17]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-feed-updated-event/get-unread-card-count.html
