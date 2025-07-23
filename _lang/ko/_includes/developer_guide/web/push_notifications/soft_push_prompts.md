{% multi_lang_include developer_guide/prerequisites/web.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) 합니다.

## 소프트 푸시 프롬프트 정보

사이트에서는 푸시 권한을 요청하기 전에 사용자를 '프라임'하고 푸시 알림을 보내야 하는 이유를 설명하는 '소프트' 푸시 프롬프트를 구현하는 것이 좋습니다. 이 기능은 브라우저에서 사용자에게 직접 프롬프트를 표시하는 빈도를 조절하고 사용자가 권한을 거부하면 다시는 요청할 수 없기 때문에 유용합니다.

또는 표준 [웹 푸시 통합에]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration) 설명된 대로 `requestPushPermission()` 으로 직접 전화하는 대신 [트리거된 인앱 메시지를]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) 사용하여 특별한 사용자 지정 처리를 포함할 수 있습니다.

{% alert tip %}
새로운 [노코드 푸시 프라이머]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)를 사용하면 SDK 사용자 지정 없이도 이 작업을 수행할 수 있습니다.
{% endalert %}

## 소프트 푸시 프롬프트 설정

{% multi_lang_include archive/web-v4-rename.md %}

### 1단계: 푸시 프라이머 캠페인 만들기

먼저, Braze 대시보드에서 'Prime for Push' 인앱 메시징 캠페인을 생성해야 합니다.

1. 원하는 텍스트와 스타일로 **모달** 인앱 메시지를 만듭니다. 
2. 다음으로, 클릭 시 동작을 **메시지 닫기**로 설정합니다. 이 동작은 나중에 사용자 지정할 수 있습니다.
3. 키는 `msg-id`이고 값은 `push-primer`인 키-값 페어를 메시지에 추가합니다.
4. 메시지에 커스텀 이벤트 트리거 동작(예: 'prime-for-push')을 할당합니다. 필요한 경우 대시보드에서 수동으로 사용자 지정 이벤트를 만들 수 있습니다.

### 2단계: 호출 제거

Braze SDK 통합의 경우 로딩 스니펫 내에서 `automaticallyShowInAppMessages()`에 대한 호출을 찾아서 제거합니다.

### 3단계: 업데이트 통합

마지막으로 제거된 호출을 다음 스니펫으로 대체합니다:

```javascript
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // check if message is not a control variant
  if (inAppMessage instanceof braze.inAppMessage) {
    // access the key-value pairs, defined as `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // check the value of our key `msg-id` defined in the Braze dashboard
    if (keyValuePairs["msg-id"] === "push-primer") {
      // We don't want to display the soft push prompt to users on browsers
      // that don't support push, or if the user has already granted/blocked permission
      if (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // do not call `showInAppMessage`
        return;
      }

      // user is eligible to receive the native prompt
      // register a click handler on one of the two buttons
      if (inAppMessage.buttons[0]) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // success!
            },
            function() {
              // user declined
            }
          );
        });
      }
    }
  }

  // show the in-app message now
  braze.showInAppMessage(inAppMessage);
});
```

사용자에게 소프트 푸시 프롬프트를 표시하려면 이 인앱 메시지를 트리거하는 이벤트 이름과 함께 `braze.logCustomEvent`를 호출합니다.
