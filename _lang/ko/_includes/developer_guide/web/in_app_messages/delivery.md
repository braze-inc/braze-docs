{% multi_lang_include developer_guide/prerequisites/web.md %}

## 메시지 트리거

## 트리거 유형

인앱 메시지는 SDK가 다음 사용자 지정 이벤트 유형 중 하나를 기록할 때 자동으로 트리거됩니다: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`. `Specific Purchase` 및 `Custom Event` 트리거에는 강력한 속성 필터도 포함되어 있습니다.

{% alert note %}
인앱 메시지는 API 또는 API 이벤트를 통해 트리거할 수 없으며, SDK에서 로깅한 사용자 지정 이벤트만 트리거할 수 있습니다. 로깅에 대해 자세히 알아보려면 [사용자 지정 이벤트 로깅을]({{site.baseurl}}/developer_guide/analytics/logging_events/) 참조하세요.
{% endalert %}

### 전달 의미 체계

모든 적격 인앱 메시지는 세션이 시작될 때 사용자의 디바이스로 전달됩니다. SDK가 제공되면 에셋을 미리 가져와 트리거 시점에 사용할 수 있으므로 디스플레이 지연 시간을 최소화할 수 있습니다. 트리거 이벤트에 적격 인앱 메시지가 두 개 이상 있는 경우 우선순위가 가장 높은 메시지만 전달됩니다.

SDK의 세션 시작 시맨틱에 대한 자세한 내용은 세션[수명 주기를]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/) 참조하세요.

### 요금 제한

기본적으로 30초에 한 번씩 인앱 메시지를 보낼 수 있습니다.

이를 재정의하려면 Braze 인스턴스가 초기화되기 전에 다음 속성을 Braze 구성에 추가하세요. 최소 시간 간격(초)을 나타내는 양의 정수로 설정할 수 있습니다. For example:

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## 키-값 쌍

Braze에서 캠페인을 생성할 때 키-값 쌍을 `extras` 으로 설정하면 인앱 메시징 개체가 앱에 데이터를 전송하는 데 사용할 수 있습니다. For example:

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```

## 자동 트리거 비활성화하기

인앱 메시지가 자동으로 트리거되는 것을 방지합니다:

로딩 스니펫 내에서 `braze.automaticallyShowInAppMessages()` 호출을 제거한 다음 인앱 메시지 표시 또는 표시 안 함을 처리하는 사용자 지정 로직을 만듭니다.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
웹사이트에서 `braze.automaticallyShowInAppMessages()` 을 제거하지 않으면 `braze.showInAppMessage` 으로 전화하면 메시지가 여러 번 표시될 수 있습니다.
{% endalert %}

`inAppMessage` 매개변수는 [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) 서브클래스 또는 [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html) 오브젝트가 되며, 각각 다양한 생애주기 이벤트 가입 메서드를 포함합니다. 전체 설명서는 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)를 참조하십시오.

한 번에 하나의 [`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web) 또는 [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web) 인앱 메시지만 표시할 수 있습니다. 하나가 이미 표시되고 있는 동안 두 번째 Modal 또는 전체 메시지를 표시하려고 하면, `braze.showInAppMessage`에서 false를 반환하고 두 번째 메시지가 표시되지 않습니다.

## 수동으로 메시지 트리거하기

### 실시간 메시지 표시

인앱 메시지는 사이트 내에서 생성되어 실시간으로 로컬에 표시될 수 있습니다. 대시보드에서 사용할 수 있는 모든 사용자 정의 옵션은 로컬에서도 사용할 수 있습니다. 특히 실시간으로 앱 내에서 트리거하려는 메시지를 표시하는 데 유용합니다. 그러나 이러한 로컬에서 생성된 메시지에 대한 분석은 Braze 대시보드 내에서 사용할 수 없습니다.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## 종료 의도 메시지 트리거하기

이탈 의도 메시지는 방문자가 사이트를 떠나기 전에 중요한 정보를 전달하는 데 사용되는 방해가 되지 않는 인앱 메시지입니다.

이러한 메시지 유형에 대한 트리거를 설정하려면 웹사이트에 종료 의도 라이브러리(예: [ouibounce의 오픈 소스 라이브러리](https://github.com/carlsednaoui/ouibounce))를 구현한 다음 다음 코드를 사용하여 `'exit intent'` 을 Braze의 사용자 지정 이벤트로 로깅하세요. 이제 향후 인앱 메시지 캠페인에서 이 메시지 유형을 사용자 지정 이벤트 트리거로 사용할 수 있습니다.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
