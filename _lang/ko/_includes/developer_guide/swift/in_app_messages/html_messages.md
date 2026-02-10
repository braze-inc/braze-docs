{% multi_lang_include developer_guide/prerequisites/swift.md %}

## HTML 메시지 정보

Braze JavaScript 인터페이스를 사용하면 앱 내 커스텀 웹뷰 내에서 Braze를 활용할 수 있습니다. 인터페이스의 [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) 가 담당합니다:

1. [사용자 가이드에 설명된 대로 WebView에 Braze JavaScript 브릿지를 삽입합니다: HTML 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. 웹뷰에서 받은 브리지 메서드를 [Braze Swift SDK에](https://github.com/braze-inc/braze-swift-sdk) 전달합니다.

## 웹뷰에 인터페이스 추가하기

먼저 앱에 [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler)`WebViewBridge` 를 앱에 추가합니다.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(braze: braze)
```

초기화된 `scriptMessageHandler` 을 WkWebView의 `userContentController` 에 추가합니다.

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

그런 다음 구성을 사용하여 WebView를 만듭니다.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

완료되면 코드가 다음과 비슷해집니다:

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

## 예시: Logging a custom event

다음 예시에서 `BrazeBridge` 는 기존 웹 콘텐츠의 커스텀 이벤트를 Braze Swift SDK에 로깅합니다.

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
