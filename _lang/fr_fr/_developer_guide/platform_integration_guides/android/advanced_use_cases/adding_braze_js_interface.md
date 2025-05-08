---
nav_title: Interface JavaScript de Braze
article_title: Ajout de l’interface JavaScript de Braze à WebViews pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 9
description: "Cet article de référence montre comment ajouter l’interface JavaScript de Braze à WebViews."

---

# Interface JavaScript de Braze

> Cet article de référence montre comment ajouter l’interface JavaScript de Braze à WebViews.

L’utilisation de la fonctionnalité de Braze à partir d’une WebView dans votre application peut être effectuée en ajoutant l’interface JavaScript de Braze à votre WebView. Après l'ajout de l'interface, la même API disponible pour les [messages intégrés HTML]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) sera disponible dans votre WebView personnalisée.

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

