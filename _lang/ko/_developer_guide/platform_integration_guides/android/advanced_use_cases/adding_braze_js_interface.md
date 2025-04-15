---
nav_title: Braze JavaScript 인터페이스
article_title: Android 및 FireOS용 WebView에 Braze 자바스크립트 인터페이스 추가하기
platform: 
  - Android
  - FireOS
page_order: 9
description: "이 참조 문서에서는 WebViews에 Braze JavaScript 인터페이스를 추가하는 방법을 보여줍니다."

---

# Braze JavaScript 인터페이스

> 이 참조 문서에서는 WebViews에 Braze JavaScript 인터페이스를 추가하는 방법을 보여줍니다.

앱의 WebView에서 Braze 기능을 사용하려면 WebView에 Braze JavaScript 인터페이스를 추가하면 됩니다. 인터페이스가 추가되면 [HTML 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages)에 사용할 수 있는 동일한 API를 커스텀 WebView 내에서 사용할 수 있습니다.

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

