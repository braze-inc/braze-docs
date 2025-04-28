---
nav_title: JavaScript インタフェースの追加
article_title: Swift の WebView に Braze JavaScript インターフェイスを追加する
platform: Swift
page_order: 5
description: "このリファレンス記事では、WebView に Braze JavaScript インターフェイスを追加する方法を説明します。"

---

# WebView へのBraze JavaScript インタフェースの追加

> Braze JavaScript インターフェイスをiOS アプリに追加する方法について説明します。これにより、カスタムWebViews でBraze を活用できます。インターフェイスを追加すると、カスタムWebView で[HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) のAPI を使用できるようになります。

## インターフェースについて

Braze [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) は以下のことを行います。

1. [HTML in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) に概説されているように、Braze Javascript ブリッジをWebView にインジェクトします。
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

次の例では、`BrazeBridge` を使用して、既存のWeb コンテンツから Braze Swift SDK にカスタムイベントを記録します。

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
