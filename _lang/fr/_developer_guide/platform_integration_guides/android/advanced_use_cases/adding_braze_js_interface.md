---
nav_title: Interface JavaScript de Braze
article_title: Ajout de l’interface JavaScript de Braze à WebViews pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 9
description: "Cet article de référence montre comment ajouter l’interface JavaScript de Braze à WebViews."

---

# Ajout de l’interface JavaScript de Braze à WebViews

L’utilisation de la fonctionnalité de Braze à partir d’une WebView dans votre application peut être effectuée en ajoutant l’interface JavaScript de Braze à votre WebView. Une fois l’interface ajoutée, la même API disponible pour les [messages in-app HTML][1] sera disponible dans votre WebView personnalisé.

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
