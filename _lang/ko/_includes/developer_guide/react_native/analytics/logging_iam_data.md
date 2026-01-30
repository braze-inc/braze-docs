{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 로깅 방법

이러한 방법은 `BrazeInAppMessage` 인스턴스를 전달하여 분석을 기록하고 작업을 수행하는 데 사용할 수 있습니다.

| 방법                                                    | 설명                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | 제공된 인앱 메시지 데이터에 대한 클릭을 기록합니다.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | 제공된 인앱 메시지 데이터에 대한 노출을 기록합니다.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | 제공된 인앱 메시지 데이터 및 버튼 ID에 대한 버튼 클릭을 기록합니다.               |
| `hideCurrentInAppMessage()`                               | 현재 표시된 인앱 메시지를 해제합니다.                                     |
| `performInAppMessageAction(inAppMessage)`                 | 인앱 메시지에 대한 작업을 수행합니다.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | 인앱 메시지 버튼에 대한 작업을 수행합니다.                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 메시지 데이터 처리하기

대부분의 경우 `Braze.addListener` 메서드를 사용하여 이벤트 리스너를 등록해 인앱 메시지에서 오는 데이터를 처리할 수 있습니다. 

또한 인앱 메시지가 트리거될 때 SDK가 `inAppMessageReceived` 이벤트를 게시하도록 `Braze.subscribeToInAppMessage` 메서드를 호출하여 JavaScript 레이어에서 인앱 메시지 데이터에 액세스할 수 있습니다. 이 메서드에 콜백을 전달하여 인앱 메시지가 트리거되고 리스너에서 수신될 때 자체 코드를 실행합니다.

메시지 데이터 처리 방법을 커스텀하려면 다음 구현 예시를 참조하세요:

{% tabs local %}
{% tab basic %}
기본값 동작을 개선하거나 기본 iOS 또는 Android 코드를 사용자 지정할 수 없는 경우 기본 UI를 비활성화하면서 Braze에서 인앱 메시지 이벤트를 계속 수신하는 것이 좋습니다. 기본 UI를 비활성화하려면 `Braze.subscribeToInAppMessage` 메서드에 `false`를 전달하고 인앱 메시지 데이터를 사용하여 JavaScript로 메시지를 작성합니다. 기본값 UI를 사용하지 않도록 선택하면 메시징에 대한 분석을 수동으로 기록해야 한다는 점에 유의하세요.

```javascript
import Braze from "@braze/react-native-sdk";

// Option 1: Listen for the event directly via `Braze.addListener`.
//
// You may use this method to accomplish the same thing if you don't
// wish to make any changes to the default Braze UI.
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  console.log(event.inAppMessage);
});

// Option 2: Call `subscribeToInAppMessage`.
//
// Pass in `false` to disable the automatic display of in-app messages.
Braze.subscribeToInAppMessage(false, (event) => {
  console.log(event.inAppMessage);
  // Use `event.inAppMessage` to construct your own custom message UI.
});
```
{% endtab %}

{% tab advanced %}
기본 제공 UI를 사용하여 인앱 메시지를 표시할지 여부를 결정하는 고급 로직을 포함하려면 기본 레이어를 통해 인앱 메시지를 구현합니다.

{% alert warning %}
이 옵션은 고급 사용자 지정 옵션이므로 기본 Braze 구현을 재정의하면 JavaScript 리스너에 인앱 메시지 이벤트를 전송하는 로직도 무효화됩니다. [인앱 메시지 데이터에 액세스](#accessing-in-app-message-data)에서 설명한 대로 `Braze.subscribeToInAppMessage` 또는 `Braze.addListener`를 계속 사용하려면 이벤트 게시를 직접 처리해야 합니다.
{% endalert %}

{% subtabs %}
{% subtab Android %}
[커스텀 매니저 리스너]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)에 대한 Android 문서에서 설명한 대로 `IInAppMessageManagerListener`를 구현합니다. `beforeInAppMessageDisplayed` 구현에서 `inAppMessage` 데이터에 액세스하여 JavaScript 레이어로 전송하고 반환 값에 따라 기본 메시지의 표시 여부를 결정할 수 있습니다.

이러한 값에 대한 자세한 내용은 [Android 설명서를]({{site.baseurl}}/developer_guide/in_app_messages/) 참조하세요.

```java
// In-app messaging
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
    WritableMap parameters = new WritableNativeMap();
    parameters.putString("inAppMessage", inAppMessage.forJsonPut().toString());
    getReactNativeHost()
        .getReactInstanceManager()
        .getCurrentReactContext()
        .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
        .emit("inAppMessageReceived", parameters);
    // Note: return InAppMessageOperation.DISCARD if you would like
    // to prevent the Braze SDK from displaying the message natively.
    return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endsubtab %}
{% subtab iOS %}
### 기본 UI 위임 재정의

기본적으로 [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/)는 `braze` 인스턴스를 초기화할 때 생성 및 할당됩니다. `BrazeInAppMessageUI`는 [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) 프로토콜의 구현이며 수신된 인앱 메시지 처리를 사용자 지정하는 데 사용할 수 있는 `delegate` 속성정보가 함께 제공됩니다.

1. [여기 iOS 문서](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)에서 설명한 대로 `BrazeInAppMessageUIDelegate` 위임을 구현합니다.

2. `inAppMessage(_:displayChoiceForMessage:)` 델리게이트 메서드에서 `inAppMessage` 데이터에 액세스하여 자바스크립트 계층으로 전송하고 반환값에 따라 네이티브 메시지를 표시할지 표시하지 않을지 결정할 수 있습니다.

이러한 값에 대한 자세한 내용은 [iOS 설명서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/)를 참조하세요.

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  // Convert the message to a JavaScript representation.
  NSData *inAppMessageData = [message json];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };

  // Send to JavaScript.
  [self sendEventWithName:@"inAppMessageReceived" body:arguments];

  // Note: Return `BRZInAppMessageUIDisplayChoiceDiscard` if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return BRZInAppMessageUIDisplayChoiceNow;
}
```

이 위임을 사용하려면 `braze` 인스턴스를 초기화한 후 `brazeInAppMessagePresenter.delegate`에 할당합니다. 

{% alert note %}
`BrazeUI`는 Objective-C 또는 Swift에서만 가져올 수 있습니다. Objective-C++를 사용하는 경우 별도의 파일에서 처리해야 합니다.
{% endalert %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```

### 기본 제공 UI 재정의

기본 iOS 레이어에서 인앱 메시지 프레젠테이션을 완전히 사용자 지정하려면, 아래 샘플에 따라 [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) 프로토콜을 준수하고 커스텀 프레젠터를 지정합니다.

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
Braze *braze = [BrazeReactBridge initBraze:configuration];
braze.inAppMessagePresenter = [[MyCustomPresenter alloc] init];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
