{% multi_lang_include developer_guide/prerequisites/android.md %}

## À propos des messages HTML

Grâce à l'interface JavaScript Braze, vous pouvez utiliser Braze dans les WebViews personnalisées de votre application. Le/la[`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html)est responsable de :

1. Intégration du pont JavaScript Braze dans votre WebView, comme indiqué dans le guide[ de l'utilisateur : Messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) HTML.
2. Transmission des méthodes de pontage reçues de votre WebView au [SDK Android Braze](https://github.com/braze-inc/braze-android-sdk).

## Ajouter l'interface à une WebView

L’utilisation de la fonctionnalité de Braze à partir d’une WebView dans votre application peut être effectuée en ajoutant l’interface JavaScript de Braze à votre WebView. Une fois l'interface ajoutée, la même API est disponible pour le guide[ de l'utilisateur : Les messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) HTML seront accessibles dans votre WebView personnalisé.

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

## Intégration de contenu YouTube

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

## Utilisation des liens profonds

Lorsque vous utilisez des liens profonds ou des liens externes dans des messages in-app Android, **veuillez ne pas** appeler`brazeBridge.closeMessage()`  dans votre JavaScript. La logique interne du SDK ferme automatiquement le message in-app lorsqu'il redirige vers un lien. Les appels`brazeBridge.closeMessage()`interfèrent avec ce processus et peuvent entraîner un blocage du message lorsque les utilisateurs reviennent à votre application. 

Voici un exemple de lien profond dans un extrait de code :

{% raw %}
```javascript
<script>
document.querySelectorAll('[data-button-id]').forEach(function (node)
Unknown macro: { node.addEventListener('click', function () { brazeBridge.logClick(node.dataset.buttonId); brazeBridge.closeMessage(); }); }
);
</script>
```
{% endraw %}