---
nav_title: 메시지 트리거
article_title: Braze SDK를 통해 인앱 메시지 트리거하기
page_order: 0.2
description: "Braze SDK를 통해 인앱 메시지를 트리거하는 방법을 알아보세요."
platform: 
  - Android
  - FireOS
  - Swift
  - Web
---

# 인앱 메시지 트리거

> Braze SDK를 통해 인앱 메시지를 트리거하는 방법을 알아보세요.

## 메시지 트리거 및 전달

인앱 메시지는 SDK가 다음 사용자 지정 이벤트 유형 중 하나를 기록할 때 트리거됩니다: `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase`, `Custom Event` (마지막 두 개는 강력한 속성 필터가 포함되어 있습니다).

사용자 세션이 시작되면 Braze는 모든 적격 인앱 메시지를 디바이스에 전달하는 동시에 에셋을 프리페칭하여 디스플레이 지연 시간을 최소화합니다. 트리거 이벤트에 적격 인앱 메시지가 두 개 이상 있는 경우 우선순위가 가장 높은 메시지만 전달됩니다. 자세한 내용은 [세션 수명 주기를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle) 참조하세요.

{% alert note %}
인앱 메시지는 API 또는 API 이벤트를 통해 트리거할 수 없으며, SDK에서 로깅한 사용자 지정 이벤트만 트리거할 수 있습니다. 로깅에 대해 자세히 알아보려면 [사용자 지정 이벤트 로깅을]({{site.baseurl}}/developer_guide/analytics/logging_events/) 참조하세요.
{% endalert %}

## 키-값 쌍

Braze에서 캠페인을 생성할 때 키-값 쌍을 `extras` 으로 설정하면 인앱 메시징 개체가 앱에 데이터를 전송하는 데 사용할 수 있습니다.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
자세한 내용은 [KDoc을](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721) 참조하세요.
{% endalert %}
{% endtab %}

{% tab swift %}
다음 예제는 사용자 지정 로직을 사용하여 `extras` 에서 키-값 쌍에 따라 인앱 메시지 표시를 설정하는 예제입니다. 전체 사용자 지정 예시를 보려면 [샘플 앱을](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples) 확인하세요.

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 웹 %}
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
{% endtab %}
{% endtabs %}

## 자동 트리거 비활성화하기

기본적으로 인앱 메시지는 자동으로 트리거됩니다. 이 기능을 비활성화하려면:

{% tabs %}
{% tab Android %}
1. `2.2.0` 버전 이상에서 기본적으로 활성화되어 있는 자동 연동 초기화 프로그램을 사용하고 있는지 확인합니다.
2. `braze.xml` 파일에 다음 줄을 추가하여 인앱 메시지 작업의 기본값을 `DISCARD`로 설정합니다.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab swift %}
1. 앱에서 `BrazeInAppMessageUIDelegate` 델리게이트를 구현합니다. 전체 안내는 [튜토리얼을 참조하세요: 인앱 메시지 UI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. `.discard` 을 반환하도록 `inAppMessage(_:displayChoiceForMessage:)` 델리게이트 메서드를 업데이트합니다.
{% endtab %}

{% tab 웹 %}
로딩 스니펫 내에서 `braze.automaticallyShowInAppMessages()` 호출을 제거한 다음 인앱 메시지 표시 여부를 처리하는 사용자 지정 로직을 생성합니다.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
`braze.automaticallyShowInAppMessages()` 을 제거하지 않고 `braze.showInAppMessage` 으로 전화하면 메시지가 두 번 표시될 수 있습니다.
{% endalert %}
{% endtab %}

{% tab 유니티 %}
{% subtabs %}
{% subtab Android %}
Android의 경우, Braze 설정 에디터에서 **인앱 메시지 자동 표시를** 선택 해제합니다. 또는 Unity 프로젝트의 `braze.xml` 에서 `com_braze_inapp_show_inapp_messages_automatically` 을 `false` 으로 설정할 수 있습니다.

초기 인앱 메시지 표시 작업은 Braze 설정에서 "인앱 메시지 관리자 초기 표시 작업"을 사용하여 설정할 수 있습니다.
{% endsubtab %}

{% subtab iOS %}
iOS의 경우, Braze 구성 에디터에서 게임 오브젝트 리스너를 설정하고 **Braze 표시 인앱 메시지가** 선택되어 있지 않은지 확인합니다.

초기 인앱 메시지 표시 작업은 Braze 설정에서 "인앱 메시지 관리자 초기 표시 작업"을 사용하여 설정할 수 있습니다.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 기본 요금 한도 재정의하기

기본적으로 30초에 한 번씩 인앱 메시지를 보낼 수 있습니다. 이를 재정의하려면 Braze 인스턴스가 초기화되기 전에 구성 파일에 다음 프로퍼티를 추가하세요. 이 값은 초 단위의 새로운 속도 제한으로 사용됩니다.

{% tabs %}
{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 웹 %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}
{% endtabs %}

## 수동으로 메시지 트리거하기

기본적으로 인앱 메시지는 SDK가 사용자 지정 이벤트를 기록할 때 자동으로 트리거됩니다. 그러나 이 외에도 다음 방법을 사용하여 수동으로 메시지를 트리거할 수 있습니다.

### 서버 측 이벤트 사용

{% tabs %}
{% tab Android %}
서버에서 전송한 이벤트를 사용하여 인앱 메시지를 트리거하려면 디바이스에 무음 푸시 알림을 보내면 사용자 지정 푸시 콜백이 SDK 기반 이벤트를 기록할 수 있습니다. 그러면 이 이벤트가 사용자에게 표시되는 인앱 메시지를 트리거합니다.

#### 1단계: 무음 푸시 수신을 위한 푸시 콜백 만들기

커스텀 푸시 콜백을 등록하여 특정 무음 푸시 알림을 수신 대기합니다. 자세한 내용은 [표준 Android 푸시 통합을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) 참조하세요.

인앱 메시지를 전달하기 위해 두 개의 이벤트가 기록됩니다. 하나는 서버에서, 다른 하나는 커스텀 푸시 콜백에서 기록됩니다. 동일한 이벤트가 중복되지 않도록 하려면 푸시 콜백 내에서 기록된 이벤트는 일번적인 명명 규칙을 따라야 하고(예: '인앱 메시지 트리거 이벤트'), 서버에서 보낸 이벤트와 같은 이름이 아니어야 합니다. 이를 준수하지 않으면 단일 사용자 작업에 대해 기록된 중복 이벤트가 세분화 및 사용자 데이터에 영향을 미칠 수 있습니다.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endsubtab %}
{% endsubtabs %}

#### 2단계: 푸시 캠페인 만들기

서버 전송 이벤트를 통해 트리거되는 [무음 푸시 캠페인을]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) 만듭니다.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

푸시 캠페인에는 이 푸시 캠페인이 SDK 커스텀 이벤트를 기록하기 위해 전송되었음을 나타내는 키-값 페어 추가 항목이 포함되어야 합니다. 이 이벤트는 인앱 메시지를 트리거하는 데 사용됩니다.

![두 세트의 키-값 페어: IS_SERVER_EVENT를 "true"로 설정하고 CAMPAIGN_NAME을 "예시 캠페인 이름"으로 설정합니다.]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

앞의 푸시 콜백 샘플 코드는 키-값 페어를 인식하고 적절한 SDK 커스텀 이벤트를 기록합니다.

'인앱 메시지 트리거' 이벤트에 첨부할 이벤트 속성정보를 포함하려면 푸시 페이로드의 키-값 페어에서 이벤트 속성정보를 전달하면 됩니다. 이 예시에서는 후속 인앱 메시지의 캠페인 이름이 포함되었습니다. 그러면 커스텀 푸시 콜백은 커스텀 이벤트를 기록할 때 이벤트 속성정보의 매개변수로 값을 전달할 수 있습니다.

#### 3단계: 인앱 메시지 캠페인 만들기

Braze 대시보드에서 사용자가 볼 수 있는 인앱 메시지 캠페인을 생성하세요. 이 캠페인에는 액션 기반 전달이 있어야 하며 사용자 지정 푸시 콜백 내에서 로깅된 사용자 지정 이벤트에서 트리거되어야 합니다.

다음 예제에서는 초기 무음 푸시의 일부로 이벤트 속성정보를 전송하여 트리거할 특정 인앱 메시지를 구성합니다.

!["캠페인_이름"이 "IAM 캠페인 이름 예시"와 같을 때 인앱 메시지가 트리거되는 액션 기반 전달 캠페인입니다.]({% image_buster /assets/img_archive/iam_event_trigger.png %})

앱이 포그라운드에 있지 않은 상태에서 서버에서 전송된 이벤트가 기록되면 이벤트는 기록되지만 인앱 메시지는 표시되지 않습니다. 애플리케이션이 포그라운드에 표시될 때까지 이벤트를 지연시키려면 앱이 포그라운드에 표시될 때까지 이벤트를 해제하거나 지연시키도록 커스텀 푸시 수신기에 확인을 포함해야 합니다.
{% endtab %}

{% tab swift %}
#### 1단계: 무음 푸시 및 키-값 쌍 처리

다음 함수를 구현하고 [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: 메서드](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/): 내에서 호출하십시오

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

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
{% endtab %}

{% tab 웹 %}
현재 웹브레이즈 SDK는 서버 측 이벤트를 사용하여 메시지를 수동으로 트리거하는 기능을 지원하지 않습니다.
{% endtab %}
{% endtabs %}

### 미리 정의된 메시지 표시

미리 정의된 인앱 메시지를 수동으로 표시하려면 다음 방법을 사용하세요:

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}

{% tab 웹 %}
```javascript
braze.requestInAppMessageDisplay();
```
{% endtab %}
{% endtabs %}

### 실시간 메시지 표시 

대시보드에서 사용할 수 있는 동일한 사용자 지정 옵션을 사용하여 로컬 인앱 메시지를 실시간으로 생성하고 표시할 수도 있습니다. 그렇게 하려면

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
이 상황에서는 렌더링이 정의되지 않으므로 소프트 키보드가 화면에 표시될 때 인앱 메시지를 표시하지 않습니다.
{% endalert %}
{% endtab %}

{% tab swift %}
메서드를 수동으로 호출합니다. [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:))`inAppMessagePresenter` 메서드를 직접 호출하세요. For example:

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
인앱 메시지를 직접 작성하면 모든 분석 추적을 옵트아웃하고 `message.context` 을 사용하여 클릭 및 노출 로깅을 수동으로 처리해야 합니다.
{% endalert %}
{% endtab %}

{% tab 웹 %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab 유니티 %}
스택에 다음 메시지를 표시하려면 `DisplayNextInAppMessage()` 메서드를 사용합니다. `DISPLAY_LATER` 또는 `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` 을 인앱 메시지 표시 동작으로 선택하면 메시지가 이 스택에 저장됩니다.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## 웹용 종료 의도 메시지

이탈 의도 메시지는 방문자가 웹사이트를 떠나기 전에 중요한 정보를 전달하는 데 사용되는 방해가 되지 않는 인앱 메시지입니다.

웹 SDK에서 이러한 메시지 유형에 대한 트리거를 설정하려면 웹사이트에 종료 의도 라이브러리(예: [ouibounce의 오픈 소스 라이브러리](https://github.com/carlsednaoui/ouibounce))를 구현한 다음 다음 코드를 사용하여 `'exit intent'` 을 Braze의 사용자 지정 이벤트로 로깅하세요. 이제 향후 인앱 메시지 캠페인에서 이 메시지 유형을 사용자 지정 이벤트 트리거로 사용할 수 있습니다.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
