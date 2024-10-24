---
nav_title: HTML Messages
article_title: Adding the Braze JavaScript Interface to WebViews for Swift
platform: Swift
page_order: 5
description: "This reference article shows how to add the Braze JavaScript Interface to WebViews."

---

# HTML in-app messages

> Learn how to add the Braze JavaScript interface to your iOS app, so you can use the Braze API to create [HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) in your custom WebViews.

## How it works

With the Braze JavaScript interface, you can leverage Braze inside the custom WebViews within your app. The interface's [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) is responsible for:

1. Injecting the Braze Javascript bridge into your WebView, as outlined in [HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Passing the bridge methods received from your WebView to the [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk).

## Adding the interface to a WebView

First, add the [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) from `WebViewBridge` to your app.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(braze: braze)
```

Add the initialized `scriptMessageHandler` to a WkWebView's `userContentController`.

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

Then create the WebView using your configuration.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

When you're finished, your code should be similar to the following:

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

## Example: Logging a custom event

In the following example, `BrazeBridge` logs a custom event from existing web content to the Braze Swift SDK.

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
