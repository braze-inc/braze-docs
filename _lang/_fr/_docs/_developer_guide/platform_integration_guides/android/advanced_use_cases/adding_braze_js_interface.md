---
nav_title: Interface JavaScript Braze
article_title: Ajout de l'interface Braze JavaScript aux Webviews pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 9
description: "Cet article montre comment ajouter l'interface JavaScript Braze à WebViews."
---

# Ajout de l'interface JavaScript Braze aux Webviews

L'utilisation de la fonctionnalité Braze d'un WebView dans votre application peut être faite en ajoutant l'interface JavaScript Braze à votre WebView comme indiqué ci-dessous. Une fois que l'interface a été ajoutée, la même API disponible pour [HTML In-App Messages][1] sera disponible dans votre WebView personnalisée.

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

val javascriptInterface = InAppMessageHtmlJavascriptInterface(contexte, inAppMessage)
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge")
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages
