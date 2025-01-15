---
nav_title: Interface JavaScript do Braze
article_title: Adição da interface JavaScript da Braze a WebViews para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 9
description: "Este artigo de referência mostra como adicionar a interface JavaScript da Braze a WebViews."

---

# Interface JavaScript do Braze

> Este artigo de referência mostra como adicionar a interface JavaScript da Braze a WebViews.

O uso da funcionalidade da Braze a partir de um WebView em seu app pode ser feito adicionando a interface Braze JavaScript ao seu WebView. Depois que a interface tiver sido adicionada, a mesma API disponível para [mensagens no app em HTML]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) estará disponível em seu WebView personalizado.

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

