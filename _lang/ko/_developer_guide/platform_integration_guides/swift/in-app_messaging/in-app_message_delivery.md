---
nav_title: 인앱 메시지 전달
article_title: iOS용 인앱 메시지 전달
platform: Swift
page_order: 2
description: "이 문서에서는 Swift SDK에 대한 iOS 인앱 메시지 전달, 다양한 트리거 유형 표시, 전달 의미 체계 및 이벤트 트리거 단계를 다룹니다."
channel:
  - in-app messages

---

# 인앱 메시지 전달

> 이 참조 문서에서는 iOS 인앱 메시지 전달, 다양한 트리거 유형 표시, 전달 의미 체계 및 이벤트 트리거 단계의 개요를 제공합니다.

## 트리거 유형

인앱 메시지는 SDK에 의해 기록된 이벤트에 의해 트리거됩니다. `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click` 이벤트 유형에서 인앱 메시지를 트리거할 수 있습니다. 게다가 `Specific Purchase` 및 `Custom Event` 트리거에는 강력한 속성정보 필터가 포함되어 있습니다.

{% alert note %}
트리거된 인앱 메시지는 Braze SDK를 통해 기록된 커스텀 이벤트에서만 작동합니다. 인앱 메시지는 API 또는 API 이벤트(예: 구매 이벤트)를 통해 트리거할 수 없습니다. iOS를 사용하는 경우 자세한 내용은 [커스텀 이벤트 추적]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) 문서를 참조하세요.
{% endalert %}

## 인앱 메시지 활성화

Braze가 인앱 메시지를 표시할 수 있도록 하려면 `BrazeInAppMessagePresenter` 프로토콜의 구현을 생성하고 이를 Braze 인스턴스의 선택적 `inAppMessagePresenter`에 할당합니다. `BrazeInAppMessageUI` 오브젝트를 인스턴스화하여 기본 Braze UI 프리젠터를 사용할 수도 있습니다.

`BrazeInAppMessageUI` 클래스에 액세스하려면 `BrazeUI` 라이브러리를 가져와야 합니다.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab 목표-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

## 전달 의미 체계

사용자가 받을 수 있는 모든 인앱 메시지는 세션 시작 시 사용자의 기기로 전달됩니다. 제공되면 SDK가 트리거 시점에 즉시 사용할 수 있도록 자산을 미리 가져와 표시 지연 시간을 최소화합니다.

트리거 이벤트에 적격한 인앱 메시지가 두 개 이상 연결된 경우 우선순위가 가장 높은 인앱 메시지만 전달됩니다.

전달 시 즉시 표시되는 인앱 메시지(세션 시작, 푸시 클릭)의 경우 자산이 미리 로드되지 않아 지연이 발생할 수 있습니다. SDK의 세션 시작 의미 체계에 대한 자세한 내용은 [세션 생애주기]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle)를 참조하세요.

## 트리거 사이의 최소 시간 간격

기본적으로, 원활한 사용자 경험을 보장하기 위해 인앱 메시지를 30초에 한 번으로 제한합니다.

Braze 설정에서 `triggerMinimumTimeInterval` 속성정보를 설정하여 이 값을 재정의할 수 있습니다. Braze 인스턴스를 초기화하기 전에 이 값을 반드시 구성하십시오. `triggerMinimumTimeInterval`을 인앱 메시지 간 최소 시간(초)에 대해 원하는 정수 값으로 설정합니다.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration) 
AppDelegate.braze = braze
```
{% endtab %}
{% tab 목표-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## 일치하는 트리거를 찾을 수 없음

Braze가 특정 이벤트에 대해 일치하는 트리거를 찾지 못하면 [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/)를 호출합니다. 이 시나리오를 처리하기 위해 `BrazeDelegate`를 채택하여 클래스에서 이 메서드를 구현합니다. 

## 인앱 메시지 스택

### 스택에 인앱 메시지 추가

사용자는 다음 상황에서 인앱 메시지를 받을 자격이 있습니다:

- 인앱 메시지 트리거 이벤트가 발생합니다
- 세션이 시작되었습니다
- 앱은 푸시 알림에서 열립니다

인앱 메시지의 트리거 이벤트가 실행되면 '스택'에 배치됩니다. 여러 개의 인앱 메시지가 스택에 있고 표시 대기 중인 경우, Braze는 최근에 수신한 인앱 메시지를 먼저 표시합니다(후입후출).

사용자에게 인앱 메시지를 수신할 수 있는 자격이 있으면 `BrazeInAppMessagePresenter`는 인앱 메시지 스택에서 최신 인앱 메시지를 요청합니다. 스택은 메모리에 저장된 인앱 메시지만 유지하며 일시 중단 모드에서 앱을 실행할 때마다 지워집니다.

### 스택으로 인앱 메시지 반환

트리거된 인앱 메시지는 다음 상황에서 스택으로 반환될 수 있습니다:

- 인앱 메시지는 앱이 백그라운드에 있을 때 트리거됩니다.
- 다른 인앱 메시지가 현재 표시되고 있습니다.
- `inAppMessage(_:displayChoiceForMessage:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)이(가) `.reenqueue`을(를) 반환했습니다.

트리거된 인앱 메시지는 사용자가 인앱 메시지를 받을 자격이 있을 때 나중에 표시할 수 있도록 스택 맨 위에 배치됩니다.

### 인앱 메시지 삭제

다음 상황에서는 트리거된 인앱 메시지가 폐기됩니다:

- `inAppMessage(_:displayChoiceForMessage:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)이(가) `.discard`을(를) 반환했습니다.
- 인앱 메시지의 자산(이미지 또는 ZIP 파일)을 다운로드하지 못했습니다.
- 인앱 메시지가 표시할 준비가 되었지만 시간 초과 기간이 지났습니다.
- 기기 방향이 트리거된 인앱 메시지의 방향과 일치하지 않습니다.

인앱 메시지는 스택에서 제거될 것입니다. 삭제된 후, 인앱 메시지는 트리거 이벤트의 다른 인스턴스에 의해 나중에 트리거될 수 있습니다.

## 실시간 인앱 메시지 생성 및 표시

앱 내에서 다른 시간에 인앱 메시지를 표시하려면 [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) 메서드를 `inAppMessagePresenter`에서 수동으로 호출할 수 있습니다. 인앱 메시지는 앱 내에서 로컬로 생성되어 Braze를 통해 표시될 수 있습니다. 이 기능은 앱 내에서 트리거하려는 메시지를 실시간으로 표시할 때 특히 유용합니다.

자체 인앱 메시지를 생성하면 분석 추적을 선택 해제하고 `message.context`을(를) 사용하여 클릭 및 노출 횟수 로깅을 수동으로 처리해야 합니다.

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab 목표-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

## 키-값 쌍 추가 정보

`Braze.InAppMessage` 오브젝트는 키-값 페어를 `extras`로 전달할 수 있습니다. 캠페인 생성 시 대시보드에서 지정할 수 있습니다. 키-값 페어를 사용하여 앱에서 추가 처리를 위해 인앱 메시지와 함께 데이터를 전송할 수 있습니다.

예를 들어, 추가 항목 콘텐츠에 따라 인앱 메시지의 프레젠테이션을 사용자 지정하려는 경우를 고려합니다. `extras` 속성정보에서 키-값 페어에 액세스하고 이를 중심으로 실행하도록 커스텀 로직을 정의할 수 있습니다.

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab 목표-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

전체 구현을 위해 [예제 앱](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)의 인앱 메시지 맞춤 설정 샘플을 참조할 수 있습니다.

