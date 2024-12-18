---
nav_title: "Ajout de l'interface JavaScript"
article_title: "Ajouter l'interface JavaScript de Braze aux WebViews pour Swift"
platform: Swift
page_order: 5
description: "Cet article de référence montre comment ajouter l’interface JavaScript de Braze à WebViews."

---

# Ajouter l'interface JavaScript de Braze aux WebViews

> Découvrez comment ajouter l'interface JavaScript de Braze à votre application iOS, afin de pouvoir exploiter Braze dans des WebViews personnalisées. Après avoir ajouté l'interface, vous pourrez utiliser l'API pour les [messages HTML in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) dans vos WebViews personnalisées.

## À propos de l'interface

Le Braze [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) est responsable de :

1. Injecter le pont Javascript de Braze dans votre WebView, comme indiqué dans les [messages in-app HTML.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages)
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

Dans l'exemple suivant, `BrazeBridge` est utilisé pour enregistrer un événement personnalisé à partir d'un contenu Web existant vers le SDK Braze Swift.

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
