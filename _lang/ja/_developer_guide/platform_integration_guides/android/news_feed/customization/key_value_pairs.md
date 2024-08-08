---
nav_title: キーと値のペア
article_title: Android およびFireOS のニュースフィードのキーと値のペア
page_order: 3
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android またはFireOS アプリケーションでニュースフィードのキーと値のペアを使用する方法について説明します。"
channel:
  - news feed

---

# キーと値のペア

> このリファレンス記事では、Android またはFireOS アプリケーションでニュースフィードのキーと値のペアを使用する方法について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュースフィードツールを利用しているお客様に、コンテンツカードのメッセージングチャネルへの移行をお勧めしています。移行により、柔軟性、カスタマイズ性、信頼性が向上します。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

オプションで、`Card` オブジェクトはキーと値のペアを `extras` として保持できます。これらは、`Card` とともにデータを送信し、アプリケーションでさらに処理するために使用します。

`Card` オブジェクトで以下を呼び出して、そのエクストラを取得します。

{% tabs %}
{% tab JAVA %}

```java
Map<String, String> getExtras()
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
extras: Map<String, String>
```

{% endtab %}
{% endtabs %}
