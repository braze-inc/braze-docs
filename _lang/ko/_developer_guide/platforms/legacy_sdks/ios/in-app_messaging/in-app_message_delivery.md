---
nav_title: 인앱 메시지 전달
article_title: iOS용 인앱 메시지 전달
platform: iOS
page_order: 3
description: "이 참조 문서에서는 iOS 인앱 메시지 전달, 다양한 트리거 유형 표시, 전달 의미 체계 및 이벤트 트리거 단계를 다룹니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 인앱 메시지 전달

## 트리거 유형

인앱 메시지 제품을 사용하면 여러 가지 이벤트 유형(`Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`)의 결과로 인앱 메시지 표시를 트리거할 수 있습니다. 게다가, `Specific Purchase` 및 `Custom Event` 트리거에는 강력한 속성정보 필터가 포함되어 있습니다.

{% alert note %}
트리거된 인앱 메시지는 Braze SDK를 통해 기록된 커스텀 이벤트에서만 작동합니다. 인앱 메시지는 API 또는 API 이벤트(예: 구매 이벤트)를 통해 트리거할 수 없습니다. iOS를 사용하는 경우 자세한 내용은 [커스텀 이벤트 추적]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift) 문서를 참조하세요.
{% endalert %}

## 전달 의미 체계

사용자가 받을 수 있는 모든 인앱 메시지는 세션 시작 시 사용자의 기기로 전달됩니다. 하나의 이벤트에 의해 두 개의 인앱 메시지가 트리거되는 경우 우선순위가 더 높은 인앱 메시지가 표시됩니다. SDK의 세션 시작 의미 체계에 대한 자세한 내용은 [세션 생애주기]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle)를 참조하세요. 제공되면 SDK가 트리거 시점에 즉시 사용할 수 있도록 자산을 미리 가져와 표시 지연 시간을 최소화합니다.

트리거 이벤트에 적격한 인앱 메시지가 두 개 이상 연결된 경우 우선순위가 가장 높은 인앱 메시지만 전달됩니다.

전달 즉시 표시되는 인앱 메시지(세션 시작, 푸시 클릭)의 경우 자산을 미리 가져오지 않아 약간의 지연 시간이 발생할 수 있습니다.

## 트리거 사이의 최소 시간 간격

기본적으로 양질의 사용자 경험을 제공하기 위해 인앱 메시지 전송을 30초에 한 번으로 제한합니다.

`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`에 전달된 `appboyOptions` 매개변수 내 `ABKMinimumTriggerTimeIntervalKey`를 통해 이 값을 재정의할 수 있습니다. `ABKMinimumTriggerTimeIntervalKey`를 인앱 메시지 간 최소 시간(초)에 대해 원하는 정수 값으로 설정합니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## 일치하는 트리거를 찾지 못함

특정 이벤트에 대해 일치하는 트리거를 찾지 못하면 Braze는 [`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html)의 [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) 메서드를 호출합니다. 이 시나리오를 처리하기 위해 델리게이트 프로토콜을 채택한 클래스에서 이 메서드를 구현하세요. 

## 로컬 인앱 메시지 전달

### 인앱 메시지 스택

#### 인앱 메시지 표시

사용자에게 인앱 메시지를 수신할 수 있는 자격이 있으면 인앱 메시지 스택에서 최신 인앱 메시지를 `ABKInAppMessageController`에 전송합니다. 스택은 메모리에 저장된 인앱 메시지만 유지하며 일시 중단 모드에서 앱을 실행할 때마다 지워집니다.

{% alert important %}
이 상황에서는 렌더링이 정의되지 않으므로 키보드가 화면에 표시될 때 인앱 메시지를 표시하지 않습니다.
{% endalert %}

#### 스택에 인앱 메시지 추가하기

사용자는 다음 상황에서 인앱 메시지를 받을 자격이 있습니다:

- 인앱 메시지 트리거 이벤트가 발생합니다.
- 세션 시작 이벤트
- 푸시 알림에서 앱이 열립니다.

트리거된 인앱 메시지는 트리거 이벤트가 실행될 때 스택에 배치됩니다. 여러 개의 인앱 메시지가 스택에 있고 표시 대기 중인 경우, Braze는 최근에 수신한 인앱 메시지를 먼저 표시합니다(후입후출).

#### 인앱 메시지를 스택으로 반환하기

트리거된 인앱 메시지는 다음 상황에서 스택으로 반환될 수 있습니다:

- 인앱 메시지는 앱이 백그라운드에 있을 때 트리거됩니다.
- 현재 다른 인앱 메시지가 표시되고 있습니다.
- 더 이상 사용되지 않는 `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI 델리게이트 메서드는]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate) 구현되지 않았으며 현재 키보드가 표시되고 있습니다.
- `beforeInAppMessageDisplayed:` [위임 메서드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate) 또는 더 이상 사용되지 않는 `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI 위임 메서드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate)에서 `ABKDisplayInAppMessageLater`를 반환합니다.

#### 인앱 메시지 삭제하기

다음과 같은 상황에서는 트리거된 인앱 메시지가 삭제됩니다:

- `beforeInAppMessageDisplayed:` [위임 메서드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#core-in-app-message-delegate) 또는 더 이상 사용되지 않는 `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI 위임 메서드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/#in-app-message-delegate)에서 `ABKDiscardInAppMessage`를 반환합니다.
- 인앱 메시지의 에셋(이미지 또는 ZIP 파일)을 다운로드하지 못했습니다.
- 인앱 메시지가 표시될 준비가 되었지만 제한 시간이 초과되었습니다.
- 디바이스 방향이 트리거된 인앱 메시지의 방향과 일치하지 않습니다.
- 인앱 메시지는 전체 인앱 메시지이지만 이미지가 없습니다.
- 인앱 메시지는 이미지가 없는 이미지 전용 Modal 인앱 메시지입니다.

#### 수동으로 인앱 메시지 표시를 대기열에 추가

앱 내에서 다른 시간에 인앱 메시지를 표시하려면 다음 메서드를 호출하여 스택에서 맨 위에 있는 인앱 메시지를 수동으로 표시할 수 있습니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### 실시간 인앱 메시지 생성 및 표시

인앱 메시지는 앱 내에서 로컬로 생성하여 Braze를 통해 표시할 수도 있습니다. 이 기능은 앱 내에서 트리거하려는 메시지를 실시간으로 표시할 때 특히 유용합니다. Braze는 로컬에서 생성된 인앱 메시지에 대한 분석을 지원하지 않습니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}

