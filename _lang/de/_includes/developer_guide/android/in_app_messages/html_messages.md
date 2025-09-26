{% multi_lang_include developer_guide/prerequisites/android.md %}

## Über HTML Nachrichten

Mit der Braze JavaScript-Schnittstelle können Sie Braze innerhalb der angepassten WebViews Ihrer App nutzen. Die Schnittstelle [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) ist verantwortlich für:

1. Einspeisen der Braze JavaScript-Bridge in Ihre WebView, wie beschrieben in [Nutzerhandbuch: In-App-Nachrichten im HTML-Format]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Übergabe der von Ihrer WebView empfangenen Bridge-Methoden an das [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk).

## Hinzufügen der Schnittstelle zu einer WebView

Sie können die Braze-Funktionen von einer WebView aus in Ihrer App verwenden, indem Sie die JavaScript-Schnittstelle von Braze zu Ihrer WebView hinzufügen. Nachdem die Schnittstelle hinzugefügt wurde, steht dieselbe API auch für [User Guide zur Verfügung: In-App-Nachrichten im HTML-Format]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) werden in Ihrem angepassten WebView verfügbar sein.

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

## YouTube-Inhalte einbetten

YouTube und andere HTML5-Inhalte können in HTML-In-App-Nachrichten abgespielt werden. Dazu muss die Hardware-Beschleunigung in der Aktivität, in der die In-App-Nachricht angezeigt wird, aktiviert sein. Weitere Informationen finden Sie im [Android-Entwicklerhandbuch](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling). Die Hardware-Beschleunigung ist nur für Android-APIs ab Version 11 verfügbar.

Im Folgenden sehen Sie ein Beispiel für ein eingebettetes YouTube-Video in einem HTML-Snippet:

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
