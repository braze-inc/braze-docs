---
nav_title: 인앱 메시지 전달
article_title: 웹의 인앱 메시지 전달
platform: Web
channel: in-app messages
page_order: 4
page_type: reference
description: "이 문서에서는 인앱 메시지를 수동으로 표시하거나 로컬 인앱 및 종료 의도 메시지를 보내는 방법 등 Braze SDK를 통한 인앱 메시지 전달을 설명합니다."

---

# 인앱 메시지 전달

> 이 문서에서는 인앱 메시지를 수동으로 표시하거나 로컬 인앱 및 종료 의도 메시지를 보내는 방법 등 Braze SDK를 통한 인앱 메시지 전달을 설명합니다.

## 트리거 유형

당사의 인앱 메시지 제품을 사용하면 여러 가지 이벤트 유형(`Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`)의 결과로 인앱 메시지 표시를 트리거할 수 있습니다. 게다가, `Specific Purchase` 및 `Custom Event` 트리거에는 강력한 속성정보 필터가 포함되어 있습니다.

{% alert note %}
트리거된 인앱 메시지는 Braze SDK를 통해 기록된 커스텀 이벤트에서만 작동합니다. 인앱 메시지는 API 또는 API 이벤트(예: 구매 이벤트)를 통해 트리거될 수 없습니다. 웹 앱을 사용 중이라면, [커스텀 이벤트]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/#tracking-custom-events)를 기록하는 방법을 확인하세요.
{% endalert %}

## 전달 의미 체계

사용자가 받을 수 있는 모든 인앱 메시지는 세션 시작 이벤트 시 자동으로 사용자의 기기 또는 브라우저에 다운로드되며, 메시지의 전달 규칙에 따라 트리거됩니다. SDK의 세션 시작 의미 체계에 대한 자세한 내용은 [세션 생애주기 설명서]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#session-lifecycle)를 참조하세요.

## 트리거 사이의 최소 시간 간격

기본적으로, 원활한 사용자 경험을 보장하기 위해 인앱 메시지를 30초에 한 번으로 제한합니다. 이 값을 재정의하려면 `minimumIntervalBetweenTriggerActionsInSeconds` 구성 옵션을 [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 함수로 전달할 수 있습니다.

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## 수동 인앱 메시지 표시

사이트에서 인앱 메시지가 트리거될 때 인앱 메시지를 바로 표시하지 않으려는 경우 자동 표시를 비활성화하고 자체 표시 가입자를 등록할 수 있습니다. 

먼저, 로드 스니펫 내에서 `braze.automaticallyShowInAppMessages()` 호출을 찾아 제거합니다. 그런 다음, 트리거된 인앱 메시지를 표시하거나 표시하지 않도록 커스텀 처리하는 로직을 생성합니다. 

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use Braze's built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
`braze.automaticallyShowInAppMessages()`를 웹사이트에서 제거하지 않고 `braze.showInAppMessage`를 호출하면 메시지가 두 번 표시될 수 있습니다.
{% endalert %}

`inAppMessage` 매개변수는 [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) 서브클래스 또는 [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html) 오브젝트가 되며, 각각 다양한 생애주기 이벤트 가입 메서드를 포함합니다. 전체 설명서는 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)를 참조하십시오.

한 번에 하나의 [`Modal`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages) 또는 [`Full`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages) 인앱 메시지만 표시할 수 있습니다. 하나가 이미 표시되고 있는 동안 두 번째 Modal 또는 전체 메시지를 표시하려고 하면, `braze.showInAppMessage`에서 false를 반환하고 두 번째 메시지가 표시되지 않습니다.

## 로컬 인-앱 메시지

인앱 메시지는 사이트 내에서 생성되어 실시간으로 로컬에 표시될 수 있습니다. 대시보드에서 사용할 수 있는 모든 사용자 정의 옵션은 로컬에서도 사용할 수 있습니다. 특히 실시간으로 앱 내에서 트리거하려는 메시지를 표시하는 데 유용합니다. 그러나 이러한 로컬에서 생성된 메시지에 대한 분석은 Braze 대시보드 내에서 사용할 수 없습니다.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## 종료 의도 메시지

사이트에서 나가려고 할 때 방문자에게 표시되는 종료 의도의 인앱 메시지입니다. 이 기능은 사이트의 이용 경험을 방해하지 않으면서 중요한 정보를 사용자에게 전달할 수 있는 또 다른 기회를 제공합니다. 

이 메시지를 보내려면 먼저 이 [오픈 소스 라이브러리](https://github.com/carlsednaoui/ouibounce)와 같은 종료 의도 라이브러리를 웹사이트에 추가하세요. 그런 다음, 다음 코드 스니펫을 사용하여 'exit intent'를 커스텀 이벤트로 기록합니다. 인앱 메시지 캠페인은 'exit intent'를 트리거 커스텀 이벤트로 사용하여 대시보드에서 생성할 수 있습니다.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```


