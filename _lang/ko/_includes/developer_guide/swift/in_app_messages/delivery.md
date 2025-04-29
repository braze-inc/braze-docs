{% multi_lang_include developer_guide/prerequisites/swift.md %}

## 메시지 트리거

### 트리거 유형

인앱 메시지는 SDK가 다음 사용자 지정 이벤트 유형 중 하나를 기록할 때 자동으로 트리거됩니다: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`. `Specific Purchase` 및 `Custom Event` 트리거에는 강력한 속성 필터도 포함되어 있습니다.

{% alert note %}
인앱 메시지는 API 또는 API 이벤트를 통해 트리거할 수 없으며, SDK에서 로깅한 사용자 지정 이벤트만 트리거할 수 있습니다. 로깅에 대해 자세히 알아보려면 [사용자 지정 이벤트 로깅을]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift) 참조하세요.
{% endalert %}

### 전달 의미 체계

모든 적격 인앱 메시지는 세션이 시작될 때 사용자의 디바이스로 전달됩니다. SDK가 제공되면 에셋을 미리 가져와 트리거 시점에 사용할 수 있으므로 디스플레이 지연 시간을 최소화할 수 있습니다. 트리거 이벤트에 적격 인앱 메시지가 두 개 이상 있는 경우 우선순위가 가장 높은 메시지만 전달됩니다.

SDK의 세션 시작 시맨틱에 대한 자세한 내용은 세션[수명 주기를]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift) 참조하세요.

### 기본 요금 한도

기본적으로 30초에 한 번씩 인앱 메시지를 보낼 수 있습니다.

이를 재정의하려면 Braze 인스턴스가 초기화되기 전에 `triggerMinimumTimeInterval` 속성을 Braze 구성에 추가하세요. 임의의 양의 정수로 설정할 수 있으며 최소 시간 간격(초)을 나타냅니다. For example:

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
{% tab OBJECTIVE-C %}

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

## 키-값 쌍

Braze에서 캠페인을 생성할 때 키-값 쌍을 `extras` 으로 설정하면 인앱 메시징 개체가 앱에 데이터를 전송하는 데 사용할 수 있습니다. For example:

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

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

## 자동 트리거 비활성화하기

인앱 메시지가 자동으로 트리거되는 것을 방지합니다:

1. [여기 iOS 문서](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)에서 설명한 대로 `BrazeInAppMessageUIDelegate` 위임을 구현합니다.
2. `.discard` 을 반환하도록 `inAppMessage(_:displayChoiceForMessage:)` 델리게이트 메서드를 업데이트합니다.

## 수동으로 메시지 트리거하기

### 서버 측 이벤트 사용

서버 측 이벤트를 사용하여 인앱 메시지를 트리거하려면 기기에 무음 푸시를 보내 기기가 SDK 기반 이벤트를 기록할 수 있도록 합니다. 이 SDK 이벤트는 이후에 사용자에게 표시되는 인앱 메시지를 트리거할 수 있습니다.

#### 1단계: 무음 푸시 및 키-값 쌍 처리

다음 함수를 구현하고 [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: 메서드](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/): 내에서 호출하십시오

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

푸시가 수신되면 SDK에서 기록한 이벤트 '인앱 메시지 트리거'가 고객 프로필에 기록됩니다. 

{% alert important %}
푸시 메시지는 SDK에서 기록한 커스텀 이벤트에 사용되기 때문에, Braze는 이 솔루션을 활성화하기 위해 각 사용자의 푸시 토큰을 저장해야 합니다. iOS 사용자의 경우, Braze는 사용자가 OS의 푸시 프롬프트를 받은 시점부터 토큰만 저장합니다. 이전에는 푸시를 사용하여 사용자에게 접근할 수 없으며, 이전 솔루션은 불가능합니다.
{% endalert %}

#### 2단계: 무음 푸시 캠페인 생성

서버 전송 이벤트를 통해 트리거되는 [무음 푸시 캠페인]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)을 생성합니다. 

![사용자 프로필에 사용자 지정 이벤트 "server_event"가 있는 사용자에게 전달되는 액션 기반 전달 인앱 메시지 캠페인입니다.]({% image_buster /assets/img_archive/iosServerSentPush.png %})

푸시 캠페인에는 이 푸시 캠페인이 SDK 커스텀 이벤트를 기록하기 위해 전송되었음을 나타내는 키-값 페어 추가 항목이 포함되어야 합니다. 이 이벤트는 인앱 메시지를 트리거하는 데 사용됩니다.

![두 개의 키-값 쌍을 가진 실행 기반 전달 인앱 메시지 캠페인. "CAMPAIGN_NAME"을 "인앱 메시지 이름 예시"로 설정하고 "IS_SERVER_EVENT"를 "true"로 설정합니다.]({% image_buster /assets/img_archive/iOSServerPush.png %})

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메서드 내 코드가 `IS_SERVER_EVENT` 키에 있는지 확인하고, 이 키가 존재하면 SDK 커스텀 이벤트를 기록합니다.

푸시 페이로드의 키-값 페어 추가 항목 내에서 원하는 값을 보내 이벤트 이름이나 이벤트 속성정보를 변경할 수 있습니다. 사용자 지정 이벤트를 로깅할 때 이러한 추가 정보는 이벤트 이름의 매개변수 또는 이벤트 속성으로 사용할 수 있습니다.

#### 3단계: 인앱 메시지 캠페인 만들기

Braze 대시보드에서 사용자가 볼 수 있는 인앱 메시지 캠페인을 생성하세요. 이 캠페인은 실행 기반 전달을 지원해야 하며 `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메서드 내에서 기록된 커스텀 이벤트에서 트리거되어야 합니다.

다음 예제에서는 초기 무음 푸시의 일부로 이벤트 속성정보를 전송하여 트리거할 특정 인앱 메시지를 구성합니다.

![사용자 지정 이벤트 "인앱 메시지 트리거"를 수행하는 사용자에게 전달되는 액션 기반 전달 인앱 메시지 캠페인으로, "캠페인_이름"이 "IAM 캠페인 이름 예시"와 같습니다.]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
이 인앱 메시지는 애플리케이션이 포그라운드에 있을 때 무음 푸시를 수신해야만 트리거됩니다.
{% endalert %}

### 사전 정의된

미리 정의된 인앱 메시지를 수동으로 표시하려면 다음 방법을 사용하세요:

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### 실시간 메시지 표시

또한 수동으로 로컬 인앱 메시지를 실시간으로 표시하려면 [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:))`inAppMessagePresenter` 메소드를 호출하여 실시간으로 표시할 수도 있습니다. For example:

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIVE-C %}

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

{% alert note %}
인앱 메시지를 직접 작성하면 모든 분석 추적을 옵트아웃하고 `message.context` 을 사용하여 클릭 및 노출 로깅을 수동으로 처리해야 합니다.
{% endalert %}

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
