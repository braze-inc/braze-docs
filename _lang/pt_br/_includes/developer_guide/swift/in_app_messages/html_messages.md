{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Sobre o envio de mensagens HTML

Com a interface JavaScript do Braze, você pode aproveitar o Braze dentro das WebViews personalizadas em seu app. A interface [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) da interface é responsável por:

1. Injetar a ponte Braze JavaScript em seu WebView, conforme descrito no Guia do Usuário [: Mensagens no app em HTML]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Passar os métodos bridge recebidos de seu WebView para o [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk).

## Adição da interface a um WebView

Primeiro, adicione o [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) de `WebViewBridge` ao seu app.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(braze: braze)
```

Adicione o site `scriptMessageHandler` inicializado ao site `userContentController` de um WkWebView.

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

Em seguida, crie o WebView usando sua configuração.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

Quando terminar, seu código deverá ser semelhante ao seguinte:

```swift
// Create the script message handler using your initialized Braze instance.
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(braze: braze)

// Create a web view configuration and setup the script message handler.
let configuration = WKWebViewConfiguration()
configuration.userContentController.addUserScript(
  Braze.WebViewBridge.ScriptMessageHandler.script
)
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)

// Create the webview using the configuration
let webView = WKWebView(frame: .zero, configuration: configuration)
```

## Exemplo: Registro de um evento personalizado

No exemplo a seguir, o site `BrazeBridge` registra um evento personalizado do conteúdo da Web existente para o Braze Swift SDK.

```javascript
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Logging data via BrazeBridge Example</title>
    <script>
      function logData(data) {
        window.brazeBridge.logCustomEvent(data);
      }
    </script>
  </head>

  <body>
    <input
      type="button"
      value="Click to log a custom Event 'completed_level'"
      onclick="logData('completed_level')"
    />
  </body>
</html>
```
