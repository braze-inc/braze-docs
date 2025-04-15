---
nav_title: Interfaz JavaScript Braze
article_title: Añadir la interfaz JavaScript Braze a WebViews para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 9
description: "Este artículo de referencia muestra cómo añadir la interfaz JavaScript de Braze a las WebViews."

---

# Interfaz JavaScript Braze

> Este artículo de referencia muestra cómo añadir la interfaz JavaScript de Braze a las WebViews.

Puedes utilizar la funcionalidad Braze desde una WebView en tu aplicación añadiendo la interfaz JavaScript Braze a tu WebView. Una vez añadida la interfaz, la misma API disponible para [los mensajes HTML dentro de la]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) aplicación estará disponible dentro de tu WebView personalizada.

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

