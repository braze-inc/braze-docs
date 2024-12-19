# HTML in-app messages

> Learn how to add the Braze JavaScript interface to your Android and FireOS apps, so you can use the Braze API to create [HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) in your custom WebViews.

## How it works

With the Braze JavaScript interface, you can leverage Braze inside the custom WebViews within your app. The interface's [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) is responsible for:

1. Injecting the Braze Javascript bridge into your WebView, as outlined in [HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Passing the bridge methods received from your WebView to the [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk).

## Adding the interface to a WebView

Using Braze functionality from a WebView in your app can be done by adding the Braze JavaScript interface to your WebView. After the interface has been added, the same API available for [HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) will be available within your custom WebView.

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
