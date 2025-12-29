{% multi_lang_include developer_guide/prerequisites/android.md %}

## À propos des messages HTML

Grâce à l'interface JavaScript de Braze, vous pouvez exploiter Braze à l'intérieur des WebViews personnalisées de votre application. Le [`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html) est responsable de :

1. Injecter le pont JavaScript de Braze dans votre WebView, comme indiqué dans le guide d'utilisation de [: Messages HTML in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Transmission des méthodes de pont reçues de votre WebView au [SDK Android de Braze](https://github.com/braze-inc/braze-android-sdk).

## Ajouter l'interface à une WebView

L’utilisation de la fonctionnalité de Braze à partir d’une WebView dans votre application peut être effectuée en ajoutant l’interface JavaScript de Braze à votre WebView. Après l'ajout de l'interface, la même API est disponible pour [User Guide : Les messages in-app HTML]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) seront disponibles dans votre WebView personnalisé.

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

## Intégrer du contenu YouTube

YouTube et d’autres contenus HTML5 peuvent être joués dans des messages in-app HTML. Cela nécessite que l’accélération matérielle soit activée dans l’activité où le message in-app est affiché. Consultez le [guide du développeur Android](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling) pour plus de détails. L’accélération matérielle est uniquement disponible sur les versions 11 et ultérieures des API Android.

Voici un exemple de vidéo YouTube intégrée dans un extrait de code HTML :

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
