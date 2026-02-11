{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Acerca de los mensajes HTML

Con la interfaz JavaScript de Braze, puedes aprovechar Braze dentro de las WebViews personalizadas de tu aplicación. La interfaz [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) es responsable de:

1. Inyectando el puente JavaScript Braze en tu WebView, como se indica en la Guía del usuario [: Mensajes HTML dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Pasar los métodos puente recibidos de tu WebView al [SDK de Braze Swift](https://github.com/braze-inc/braze-swift-sdk).

## Añadir la interfaz a una WebView

En primer lugar, añade el archivo [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) de `WebViewBridge` a tu aplicación.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(braze: braze)
```

Añade el `scriptMessageHandler` inicializado al `userContentController` de un WkWebView .

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

A continuación, crea la Vista Web utilizando tu configuración.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

Cuando hayas terminado, tu código debe ser similar al siguiente:

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

## Ejemplo: Registro de un evento personalizado

En el siguiente ejemplo, `BrazeBridge` registra un evento personalizado del contenido Web existente en el SDK de Swift de Braze.

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
