---
nav_title: Braze JavaScript インターフェイス
article_title: Android と FireOS の WebView に Braze JavaScript インターフェースを追加する
platform: 
  - Android
  - FireOS
page_order: 9
description: "このリファレンス記事では、WebView に Braze JavaScript インターフェイスを追加する方法を説明します。"

---

# Braze JavaScript インターフェイス

> このリファレンス記事では、WebView に Braze JavaScript インターフェイスを追加する方法を説明します。

アプリの WebView から Braze 機能を使用するには、WebView に Braze JavaScript インターフェイスを追加します。インターフェイスを追加すると、[HTML アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages)に使用できるのと同じ API がカスタム WebView でも使用できるようになります。

{% tabs %}
{% tab JAVA %}

```java
String javascriptString = BrazeFileUtils.getAssetFileStringContents(context.getAssets(), "braze-html-bridge.js");
myWebView.loadUrl("javascript:" + javascriptString);

final InAppMessageJavascriptInterface javascriptInterface = new InAppMessageJavascriptInterface(context, inAppMessage);
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val javascriptString = context.assets.getAssetFileStringContents("braze-html-bridge.js")
myWebView.loadUrl("javascript:" + javascriptString!!)

val javascriptInterface = InAppMessageJavascriptInterface(context, inAppMessage)
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge")
```

{% endtab %}
{% endtabs %}

