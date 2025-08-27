{% multi_lang_include developer_guide/prerequisites/android.md %}

## About HTML messages

With the Braze JavaScript interface, you can leverage Braze inside the custom WebViews within your app. The [`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html) is responsible for:

1. Injecting the Braze JavaScript bridge into your WebView, as outlined in [User Guide: HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Passing the bridge methods received from your WebView to the [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk).

## Adding the interface to a WebView

Using Braze functionality from a WebView in your app can be done by adding the Braze JavaScript interface to your WebView. After the interface has been added, the same API available for [User Guide: HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) will be available within your custom WebView.

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

## Embedding YouTube content

YouTube and other HTML5 content can play in HTML in-app messages. This requires hardware acceleration to be enabled in the activity where the in-app message is being displayed; see the [Android developer guide](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling) for more details. Hardware acceleration is only available on Android API versions 11 and later.

The following is an example of an embedded YouTube video in an HTML snippet:

```html
<body>
    <div class="box">
        <div class="relativeTopRight">
            <a href="appboy://close">X</a>
        </div>
        <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI">
        </iframe>
    </div>
</body>
```
