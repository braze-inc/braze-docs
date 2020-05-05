---
nav_title: Braze Javascript Interface
platform: Android
page_order: 9

---
## Adding The Braze Javascript Interface to Webviews

Using Braze functionality within a custom WebView in your app can be done by adding the Braze javascript interface. Then, the same API used with [HTML In-App Messages][1] can be used within your custom WebView.

{% tabs %}
{% tab JAVA %}

```java
String javascriptString = AppboyFileUtils.getAssetFileStringContents(context.getAssets(), "appboy-html-in-app-message-javascript-component.js");
myWebView.loadUrl("javascript:" + javascriptString);

final AppboyInAppMessageHtmlJavascriptInterface javascriptInterface = new AppboyInAppMessageHtmlJavascriptInterface(context, inAppMessage);
myWebView.addJavascriptInterface(javascriptInterface, "appboyInternalBridge");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val javascriptString = AppboyFileUtils.getAssetFileStringContents(context.getAssets(), "appboy-html-in-app-message-javascript-component.js")
myWebView.loadUrl("javascript:" + javascriptString!!)

val javascriptInterface = AppboyInAppMessageHtmlJavascriptInterface(context, inAppMessage)
myWebView.addJavascriptInterface(javascriptInterface, "appboyInternalBridge")
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages