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

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

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
