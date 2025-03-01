---
nav_title: Hinzufügen der JavaScript-Schnittstelle
article_title: Hinzufügen der Braze JavaScript-Schnittstelle zu WebViews für Swift
platform: Swift
page_order: 5
description: "Dieser Referenzartikel beschreibt, wie Sie die Braze JavaScript-Schnittstelle zu WebViews hinzufügen."

---

# Hinzufügen der Braze JavaScript-Schnittstelle zu WebViews

> Erfahren Sie, wie Sie die Braze JavaScript-Schnittstelle zu Ihrer iOS-App hinzufügen, um Braze in angepassten WebViews nutzen zu können. Nachdem Sie die Schnittstelle hinzugefügt haben, können Sie die API für [HTML-In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) in Ihren benutzerdefinierten WebViews verwenden.

## Über die Schnittstelle

Der Braze [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) ist für Folgendes verantwortlich:

1. Einspeisung der Braze Javascript-Bridge in die WebView, wie unter [HTML-In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) beschrieben.
2. Übergabe der von Ihrer WebView empfangenen Bridge-Methoden an das [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk).

## Hinzufügen der Schnittstelle zu einer WebView

Fügen Sie zunächst die [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) von `WebViewBridge` zu Ihrer App hinzu.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(braze: braze)
```

Fügen Sie den initialisierten `scriptMessageHandler` zum `userContentController` eines WkWebViews hinzu.

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

Erstellen Sie dann die WebView mit Ihrer Konfiguration.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

Wenn Sie fertig sind, sollte Ihr Code etwa so aussehen wie der folgende:

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

## Beispiel: Protokollieren eines angepassten Events

Im folgenden Beispiel wird `BrazeBridge` verwendet, um ein angepasstes Event aus bestehenden Webinhalten im Braze Swift-SDK zu protokollieren.

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
