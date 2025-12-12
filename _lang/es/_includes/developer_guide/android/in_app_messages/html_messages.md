{% multi_lang_include developer_guide/prerequisites/android.md %}

## Acerca de los mensajes HTML

Con la interfaz JavaScript de Braze, puedes aprovechar Braze dentro de las WebViews personalizadas de tu aplicación. El [`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html) es responsable de:

1. Inyectando el puente JavaScript Braze en tu WebView, como se indica en la Guía del usuario [: Mensajes HTML dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Pasar los métodos puente recibidos de tu WebView al [SDK de Android Braze](https://github.com/braze-inc/braze-android-sdk).

## Añadir la interfaz a una WebView

Puedes utilizar la funcionalidad Braze desde una WebView en tu aplicación añadiendo la interfaz JavaScript Braze a tu WebView. Una vez añadida la interfaz, la misma API disponible para [Guía del usuario: Los mensajes HTML dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) estarán disponibles dentro de tu WebView personalizada.

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

## Incrustar contenido de YouTube

YouTube y otros contenidos HTML5 pueden reproducirse en mensajes HTML dentro de la aplicación. Esto requiere habilitar la aceleración por hardware en la actividad en la que se está mostrando el mensaje dentro de la aplicación; consulta la [guía del desarrollador de Android](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling) para más detalles. La aceleración por hardware solo está disponible en las versiones 11 y posteriores de la API de Android.

A continuación se muestra un ejemplo de un video de YouTube incrustado en un fragmento de código HTML:

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
