---
nav_title: Braze JavaScript Interface
article_title: Adding the Braze JavaScript Interface to Webviews for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 9
description: "This article shows how to add the Braze JavaScript Interface to WebViews."

---

# Adding the Braze JavaScript interface to Webviews

Using Braze functionality from a WebView in your app can be done by adding the Braze JavaScript interface to your WebView. Once the interface has been added, the same API available for [HTML in-app messages][1] will be available within your custom WebView.

{% tabs %}
{% tab JAVA %}

```java
String javascriptString = BrazeFileUtils.getAssetFileStringContents(context.getAssets(), "appboy-html-in-app-message-javascript-component.js");
myWebView.loadUrl("javascript:" + javascriptString);

final InAppMessageHtmlJavascriptInterface javascriptInterface = new InAppMessageHtmlJavascriptInterface(context, inAppMessage);
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val javascriptString = BrazeFileUtils.getAssetFileStringContents(context.getAssets(), "appboy-html-in-app-message-javascript-component.js")
myWebView.loadUrl("javascript:" + javascriptString!!)

val javascriptInterface = InAppMessageHtmlJavascriptInterface(context, inAppMessage)
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge")
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages
