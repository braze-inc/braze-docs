{% multi_lang_include developer_guide/prerequisites/swift.md %}

## HTMLについて

Braze JavaScript インターフェイスを使用すると、Brazeをアプリ内のカスタムWebView 内で活用できます。インターフェイスの[`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) は、次のことを行います。

1. [ ユーザガイドに記載されているように、Braze JavaScript ブリッジをWebView に挿入します。HTML アプリ内メッセージs
2. WebView から受け取ったブリッジメソッドを[Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) に渡します。

## WebView へのインターフェースの追加

まず、`WebViewBridge` の [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) をアプリに追加します。

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(braze: braze)
```

初期化された`scriptMessageHandler` をWkWebView の`userContentController` に追加します。

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

次に、設定を使用してWebView を作成します。

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

完了したら、コードは次のようになります。

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

## 例: カスタムイベントをログに記録する

次の例では、`BrazeBridge` は、既存のウェブコンテンツからBraze Swift SDKにカスタムイベントを記録します。

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
