---
nav_title: 사용자 지정 스타일
article_title: 인앱 메시지 커스텀 스타일 for Web
platform: Web
channel: in-app messages
page_order: 1
page_type: reference
description: "이 기사는 웹 애플리케이션을 위한 인-앱 메시징 커스텀 스타일을 다룹니다."

---

# 커스텀 스타일

> Braze UI 요소는 자연스러운 인앱 메시지 경험을 조성하는 기본 모양과 느낌을 사용하며, 다른 Braze 모바일 플랫폼과의 일관성을 목표로 합니다. Braze의 기본 스타일은 Braze SDK 내 CSS에서 정의됩니다. 

애플리케이션에서 선택한 스타일을 재정의하여 자체 배경 이미지, 글꼴 패밀리, 스타일, 크기, 애니메이션 등으로 표준 인앱 메시지 유형을 사용자 지정할 수 있습니다. 

예를 들어, 다음은 인앱 메시지의 헤더가 이탤릭체로 표시되도록 하는 예제 오버라이드입니다:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

자세한 내용은 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)를 참조하세요.

## 인앱 메시지 기본값 z-index

기본적으로 인앱 메시지는 `z-index: 9001`을 사용하여 표시됩니다. 웹사이트가 이보다 높은 값으로 요소를 스타일링하는 시나리오에서 `inAppMessageZIndex ` [초기화 옵션](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)을 사용하여 구성할 수 있습니다.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
이 옵션은 웹 SDK v3.3.0에 도입되었습니다. 이 옵션을 사용하려면 이전 SDK를 업그레이드해야 합니다.
{% endalert %}

