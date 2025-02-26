---
nav_title: 자바스크립트 인터페이스 추가
article_title: Swift용 WebView에 Braze JavaScript 인터페이스 추가하기
platform: Swift
page_order: 5
description: "이 참조 문서에서는 WebViews에 Braze JavaScript 인터페이스를 추가하는 방법을 보여줍니다."

---

# 웹뷰에 Braze JavaScript 인터페이스 추가하기

> 사용자 지정 웹뷰에서 Braze를 활용할 수 있도록 iOS 앱에 Braze 자바스크립트 인터페이스를 추가하는 방법을 알아보세요. 인터페이스를 추가하면 사용자 지정 웹뷰에서 [HTML 인앱 메시지용]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) API를 사용할 수 있습니다.

## 인터페이스 정보

더 브레이즈 [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) 가 담당합니다:

1. [HTML 인앱 메시지에]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) 설명된 대로 Braze 자바스크립트 브릿지를 웹뷰에 삽입합니다.
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

## 예시: 사용자 지정 이벤트 로깅하기

다음 예제에서는 `BrazeBridge` 을 사용하여 기존 웹 콘텐츠의 사용자 지정 이벤트를 Braze Swift SDK에 기록합니다.

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
