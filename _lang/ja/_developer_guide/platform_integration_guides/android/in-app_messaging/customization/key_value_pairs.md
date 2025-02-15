---
nav_title: キーと値のペア
article_title: Android と FireOS のアプリ内メッセージのキーと値のペア
platform: 
  - Android
  - FireOS
page_order: 6.9
description: "このリファレンス記事では、Android または FireOS アプリケーションのアプリ内メッセージングのキーと値のペアについて説明します。"
channel:
  - in-app messages

---

# キーと値のペア

> このリファレンス記事では、Android または FireOS アプリケーションのアプリ内メッセージングのキーと値のペアについて説明します。

アプリ内メッセージオブジェクトはキーと値のペアを`extras`として保持できます。これらは、アプリ内メッセージキャンペーンを作成するときに、ダッシュボードの [**設定**] で指定されます。これらは、アプリ内メッセージとともにデータを送信し、アプリケーションでさらに処理するために使用します。

アプリ内メッセージオブジェクトを取得したら、以下を呼び出してエクストラを取得します。

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

詳細については、この [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721) を参照してください。

