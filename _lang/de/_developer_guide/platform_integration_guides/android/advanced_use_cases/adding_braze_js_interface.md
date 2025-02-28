---
nav_title: Braze JavaScript Schnittstelle
article_title: Hinzufügen der Braze JavaScript-Schnittstelle zu WebViews für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 9
description: "Dieser Referenzartikel beschreibt, wie Sie die Braze JavaScript-Schnittstelle zu WebViews hinzufügen."

---

# Braze JavaScript Schnittstelle

> Dieser Referenzartikel beschreibt, wie Sie die Braze JavaScript-Schnittstelle zu WebViews hinzufügen.

Sie können die Braze-Funktionen von einer WebView aus in Ihrer App verwenden, indem Sie die JavaScript-Schnittstelle von Braze zu Ihrer WebView hinzufügen. Nachdem die Schnittstelle hinzugefügt wurde, steht Ihnen innerhalb Ihres angepassten WebViews dieselbe API zur Verfügung, die auch für [In-App-Nachrichten im HTML-Format]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) verfügbar ist.

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

