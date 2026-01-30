{% multi_lang_include developer_guide/prerequisites/web.md %}

## 커스텀 스타일

Braze UI 요소는 자연스러운 인앱 메시지 경험을 조성하는 기본 모양과 느낌을 사용하며, 다른 Braze 모바일 플랫폼과의 일관성을 목표로 합니다. 기본값 Braze 스타일은 소프트웨어 개발 키트 내 CSS에 정의되어 있습니다. 

### 기본값 스타일 설정하기

애플리케이션에서 선택한 스타일을 재정의하여 자체 배경 이미지, 글꼴 패밀리, 스타일, 크기, 애니메이션 등으로 표준 인앱 메시지 유형을 사용자 지정할 수 있습니다. 

예를 들어, 다음은 인앱 메시지의 헤더가 이탤릭체로 표시되도록 하는 예제 오버라이드입니다:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

자세한 내용은 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)를 참조하세요.

### Z-인덱스 커스텀하기

기본적으로 인앱 메시지는 `z-index: 9001`을 사용하여 표시됩니다. 웹사이트가 이보다 높은 값으로 요소를 스타일링하는 시나리오에서 `inAppMessageZIndex ` [초기화 옵션](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)을 사용하여 구성할 수 있습니다.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
이 기능은 Web Braze 소프트웨어 개발 키트 v3.3.0 이상에서만 사용할 수 있습니다.
{% endalert %}

## 메시지 해제 커스텀하기

By default, when an in-app message is showing, pressing the escape button or a click on the grayed-out background of the page will dismiss the message. `requireExplicitInAppMessageDismissal` [초기화 옵션](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)을 `true`로 구성하여 이 동작을 방지하고 메시지를 해제하려면 명시적으로 버튼을 클릭해야 합니다. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## 새 탭에서 링크 열기

인앱 메시지 링크를 새 탭에서 열도록 설정하려면 `openInAppMessagesInNewTab` 옵션을 `true`로 설정하여 인앱 메시지 클릭 시 모든 링크가 새 탭 또는 새 창에서 열리도록 합니다.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
