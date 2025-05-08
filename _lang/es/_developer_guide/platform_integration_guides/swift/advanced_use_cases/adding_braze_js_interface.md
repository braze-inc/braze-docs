---
nav_title: Añadir la interfaz JavaScript
article_title: Añadir la interfaz JavaScript Braze a WebViews para Swift
platform: Swift
page_order: 5
description: "Este artículo de referencia muestra cómo añadir la interfaz JavaScript de Braze a las WebViews."

---

# Añadir la interfaz JavaScript Braze a WebViews

> Aprende a añadir la interfaz JavaScript Braze a tu aplicación iOS, para que puedas aprovechar Braze en WebViews personalizadas. Después de añadir la interfaz, podrás utilizar la API para [mensajes HTML dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) en tus WebViews personalizadas.

## Acerca de la interfaz

El Braze [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) es responsable de:

1. Inyectar el puente Javascript Braze en tu WebView, como se indica en [los mensajes HTML dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
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

En el siguiente ejemplo, se utiliza `BrazeBridge` para registrar un evento personalizado desde el contenido Web existente al SDK de Braze Swift.

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
