---
nav_title: Adição da interface JavaScript
article_title: Adição da interface JavaScript do Braze a WebViews para Swift
platform: Swift
page_order: 5
description: "Este artigo de referência mostra como adicionar a interface JavaScript da Braze a WebViews."

---

# Adição da interface JavaScript do Braze às WebViews

> Saiba como adicionar a interface JavaScript do Braze ao seu app iOS, para que você possa aproveitar o Braze em WebViews personalizadas. Depois de adicionar a interface, você poderá usar a API para [mensagens HTML no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) em suas WebViews personalizadas.

## Sobre a interface

O Braze [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) é responsável por:

1. Injetar a ponte Javascript do Braze em seu WebView, conforme descrito nas [mensagens HTML no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
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

No exemplo a seguir, `BrazeBridge` é usado para registrar um evento personalizado do conteúdo da Web existente para o Braze Swift SDK.

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
