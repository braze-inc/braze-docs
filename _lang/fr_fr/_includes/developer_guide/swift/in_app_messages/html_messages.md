{% multi_lang_include developer_guide/prerequisites/swift.md %}

## À propos des messages HTML

Grâce à l'interface JavaScript de Braze, vous pouvez exploiter Braze à l'intérieur des WebViews personnalisées de votre application. L'élément [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) est responsable de :

1. Injecter le pont JavaScript de Braze dans votre WebView, comme indiqué dans le guide d'utilisation de [: Messages HTML in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Transmission des méthodes de pont reçues de votre WebView au [SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk).

## Ajouter l'interface à une WebView

Tout d'abord, ajoutez le fichier [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) from `WebViewBridge` à votre application.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(braze: braze)
```

Ajoutez l'adresse `scriptMessageHandler` initialisée à l'adresse `userContentController` d'un WkWebView.

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

Créez ensuite la WebView en utilisant votre configuration.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

Lorsque vous aurez terminé, votre code devrait ressembler à ce qui suit :

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

## Exemple : Enregistrement d'un événement personnalisé

Dans l'exemple suivant, `BrazeBridge` enregistre un événement personnalisé à partir d'un contenu Web existant vers le SDK Braze Swift.

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
