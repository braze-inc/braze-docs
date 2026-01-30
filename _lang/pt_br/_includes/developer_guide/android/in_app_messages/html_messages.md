{% multi_lang_include developer_guide/prerequisites/android.md %}

## Sobre mensagens HTML

Com a interface JavaScript do Braze, você pode aproveitar o Braze dentro das WebViews personalizadas do seu app. O [`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html) é responsável por:

1. Injetar a ponte JavaScript do Braze na sua WebView, conforme descrito em [Guia do Usuário: Mensagens HTML no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Passar os métodos da ponte recebidos da sua WebView para o [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk).

## Adição da interface a um WebView

O uso da funcionalidade da Braze a partir de um WebView em seu app pode ser feito adicionando a interface Braze JavaScript ao seu WebView. Depois que a interface foi adicionada, a mesma API disponível para [Guia do Usuário: Mensagens HTML no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) estarão disponíveis dentro da sua WebView personalizada.

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

## Incorporando conteúdo do YouTube

O YouTube e outros conteúdos em HTML5 podem ser reproduzidos em mensagens no app em HTML. Isso requer que a aceleração de hardware seja ativada na atividade em que a mensagem no app está sendo exibida; consulte o [guia do desenvolvedor do Android](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling) para obter mais detalhes. A aceleração de hardware está disponível apenas nas versões 11 e posteriores da API do Android.

A seguir, um exemplo de um vídeo do YouTube incorporado em um trecho de HTML:

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

## Usando deep links

Ao usar deep links ou links externos em mensagens HTML no app Android, **não** chame `brazeBridge.closeMessage()` no seu JavaScript. A lógica interna do SDK fecha automaticamente a mensagem no app quando redireciona para um link. Chamar `brazeBridge.closeMessage()` interfere nesse processo e pode fazer com que a mensagem fique sem resposta quando os usuários retornarem ao seu app. 

O seguinte é um exemplo de um deep link em um trecho de código:

{% raw %}
```javascript
<script>
document.querySelectorAll('[data-button-id]').forEach(function (node)
Unknown macro: { node.addEventListener('click', function () { brazeBridge.logClick(node.dataset.buttonId); brazeBridge.closeMessage(); }); }
);
</script>
```
{% endraw %}