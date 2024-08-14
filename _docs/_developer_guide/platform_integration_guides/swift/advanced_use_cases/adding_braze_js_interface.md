---
nav_title: Braze JavaScript Interface
article_title: Adding the Braze JavaScript Interface to WebViews for Swift
platform: Swift
page_order: 5
description: "This reference article shows how to add the Braze JavaScript Interface to WebViews."

---

# Braze JavaScript interface

> This reference article shows how to add the Braze JavaScript Interface to iOS WebViews.

Using Braze functionality from a WebView in your app can be done by adding the Braze JavaScript interface to your WebView. After the interface has been added, the same API available for [HTML in-app messages][1] will be available within your custom WebView.

We'll start by adding the code required to use a WebView in our app
and add the Braze `ScriptMessageHandler` that is part of the Braze `WebViewBridge`. By adding the `ScriptMessageHandler`
to a WkWebView's `userContentController` we can make use of the Braze Javascript bridge from webpages presented in the WkWebView.

{% tabs %}
{% tab SWIFT %}
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
{% endtab %}
{% endtabs %}

The initializer accepts closures parameters specific to the handling of in-app messages.
If you do not need to handle those actions, you may use
``Braze.WebViewBridge.ScriptMessageHandler(braze: braze)`` directly.

{% tabs %}
{% tab SWIFT %}
```swift
func webViewScriptMessageHandler() -> Braze.WebViewBridge.ScriptMessageHandler
{
let braze = AppDelegate.braze! as Braze
        return .init(
            braze: braze
        )
    }
```
{% endtab %}
{% endtabs %}

The Braze ScriptMessageHandler is responsible for:
1. Injecting the Braze Javascript bridge into your WebView (i.e. as outlined here [HTML in-app messages][1])
2. Passing the  bridge methods received from your WebView to the native Braze SDK

Here’s an example of how to log a custom event from your web content to the Braze Swift SDK using the BrazeBridge:

{% tabs local %}
{% tab HTML %}
```javascript

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logging data via BrazeBridge Example</title>
    <script>

        function logData(data) {
            window.brazeBridge.logCustomEvent(data);
        }
    </script>
</head>
<body>
    <center>
        <br><br>
            <input type="button" value="Click to log a custom Event 'completed_level'" onclick="logData('completed_level')"><br>
    </center>
</body>
</html>
```
{% endtab %}
{% endtabs %}
