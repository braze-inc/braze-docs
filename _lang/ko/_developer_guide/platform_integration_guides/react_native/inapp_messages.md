---
nav_title: 인앱 메시지
article_title: React Native용 인앱 메시지
platform: React Native
page_order: 4
page_type: reference
description: "이 문서에서는 분석 사용자 지정 및 로깅을 포함하여 React Native를 사용하는 iOS 및 Android 앱의 인앱 메시지를 다룹니다."
channel: in-app messages

---

# 인앱 메시지 통합

> React Native를 사용할 때 기본 인앱 메시지는 Android와 iOS에서 자동으로 표시됩니다. 이 문서에서는 React Native를 사용하는 앱의 인앱 메시지에 대한 분석 사용자 지정 및 로깅을 다룹니다.

## 인앱 메시지 데이터 액세스

대부분의 경우 `Braze.addListener` 메서드를 사용하여 이벤트 리스너를 등록해 인앱 메시지에서 오는 데이터를 처리할 수 있습니다. 

또한 인앱 메시지가 트리거될 때 SDK가 `inAppMessageReceived` 이벤트를 게시하도록 `Braze.subscribeToInAppMessage` 메서드를 호출하여 JavaScript 레이어에서 인앱 메시지 데이터에 액세스할 수 있습니다. 이 메서드에 콜백을 전달하여 인앱 메시지가 트리거되고 리스너에서 수신될 때 자체 코드를 실행합니다.

기본 동작을 추가로 사용자 지정하거나 기본 iOS 또는 Android 코드를 사용자 지정할 수 없는 경우, 기본 UI를 비활성화하는 동시에 Braze에서 인앱 메시지 이벤트를 수신하는 것이 좋습니다. 기본 UI를 비활성화하려면 `Braze.subscribeToInAppMessage` 메서드에 `false`를 전달하고 인앱 메시지 데이터를 사용하여 JavaScript로 메시지를 작성합니다. 기본 UI를 비활성화하려는 경우 메시지에서 [분석을 수동으로 기록](#analytics)해야 합니다.

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

## 고급 사용자 지정

기본 제공 UI를 사용하여 인앱 메시지를 표시할지 여부를 결정하는 고급 로직을 포함하려면 기본 레이어를 통해 인앱 메시지를 구현합니다.

{% alert warning %}
이 옵션은 고급 사용자 지정 옵션이므로 기본 Braze 구현을 재정의하면 JavaScript 리스너에 인앱 메시지 이벤트를 전송하는 로직도 무효화됩니다. [인앱 메시지 데이터에 액세스](#accessing-in-app-message-data)에서 설명한 대로 `Braze.subscribeToInAppMessage` 또는 `Braze.addListener`를 계속 사용하려면 이벤트 게시를 직접 처리해야 합니다.
{% endalert %}

{% tabs %}
{% tab Android %}

[커스텀 매니저 리스너]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-manager-listener)에 대한 Android 문서에서 설명한 대로 `IInAppMessageManagerListener`를 구현합니다. `beforeInAppMessageDisplayed` 구현에서 `inAppMessage` 데이터에 액세스하여 JavaScript 레이어로 전송하고 반환 값에 따라 기본 메시지의 표시 여부를 결정할 수 있습니다.

이러한 값에 대한 자세한 내용은 [Android 설명서를]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/) 참조하세요.

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
{% endtab %}
{% tab iOS %}
### 기본 UI 위임 재정의

기본적으로 [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/)는 `braze` 인스턴스를 초기화할 때 생성 및 할당됩니다. `BrazeInAppMessageUI`는 [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) 프로토콜의 구현이며 수신된 인앱 메시지 처리를 사용자 지정하는 데 사용할 수 있는 `delegate` 속성정보가 함께 제공됩니다.

1. [여기 iOS 문서](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)에서 설명한 대로 `BrazeInAppMessageUIDelegate` 위임을 구현합니다.

2. `inAppMessage(_:displayChoiceForMessage:)` 델리게이트 메서드에서 `inAppMessage` 데이터에 액세스하여 자바스크립트 계층으로 전송하고 반환값에 따라 네이티브 메시지를 표시할지 표시하지 않을지 결정할 수 있습니다.

이러한 값에 대한 자세한 내용은 [iOS 설명서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/)를 참조하세요.

{% subtabs %}
{% subtab OBJECTIVE-C %}
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
{% endsubtab %}
{% endsubtabs %}

이 위임을 사용하려면 `braze` 인스턴스를 초기화한 후 `brazeInAppMessagePresenter.delegate`에 할당합니다. 

{% alert note %}
`BrazeUI`는 Objective-C 또는 Swift에서만 가져올 수 있습니다. Objective-C++를 사용하는 경우 별도의 파일에서 처리해야 합니다.
{% endalert %}

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

### 기본 제공 UI 재정의

기본 iOS 레이어에서 인앱 메시지 프레젠테이션을 완전히 사용자 지정하려면, 아래 샘플에 따라 [`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter) 프로토콜을 준수하고 커스텀 프레젠터를 지정합니다.

{% subtabs %}
{% subtab OBJECTIVE-C %}
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

## 분석 및 조치 방법

이러한 방법은 `BrazeInAppMessage` 인스턴스를 전달하여 분석을 기록하고 작업을 수행하는 데 사용할 수 있습니다.

| 방법                                                    | 설명                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | 제공된 인앱 메시지 데이터에 대한 클릭을 기록합니다.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | 제공된 인앱 메시지 데이터에 대한 노출을 기록합니다.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | 제공된 인앱 메시지 데이터 및 버튼 ID에 대한 버튼 클릭을 기록합니다.               |
| `hideCurrentInAppMessage()`                               | 현재 표시된 인앱 메시지를 해제합니다.                                     |
| `performInAppMessageAction(inAppMessage)`                 | 인앱 메시지에 대한 작업을 수행합니다.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | 인앱 메시지 버튼에 대한 작업을 수행합니다.                                     |

## 샘플 인앱 메시지 표시 테스트

샘플 인앱 메시지를 테스트하려면 다음 단계를 따르세요.

1. `Braze.changeUserId('your-user-id')` 메서드를 호출하여 React 애플리케이션에서 활성 사용자를 설정합니다.
2. **캠페인**으로 이동하여 [이 가이드]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/)에 따라 새 인앱 메시지 캠페인을 생성합니다.
3. 테스트 인앱 메시징 캠페인을 작성하고 **테스트** 탭으로 이동합니다. 동일한 `user-id`을 테스트 사용자로 추가하고 **테스트 보내기**를 클릭하십시오. 곧 기기에서 인앱 메시지를 실행할 수 있습니다.

![브레이즈 인앱 메시지 캠페인으로, 테스트 수신자로 자신의 사용자 ID를 추가할 수 있음을 보여줍니다.]({% image_buster /assets/img/react-native/iam-test.png %} "인앱 메시징 테스트")

샘플 구현은 [React Native SDK](https://github.com/braze-inc/braze-react-native-sdk) 내의 BrazeProject에서 찾을 수 있습니다. 추가적인 [Android](https://github.com/braze-inc/braze-android-sdk) 및 [iOS](https://github.com/braze-inc/braze-swift-sdk) SDK 구현 샘플을 찾을 수 있습니다.

## 인앱 메시지 데이터 모델

인앱 메시지 모델은 React Native SDK에서 사용할 수 있습니다. Braze에는 동일한 데이터 모델을 공유하는 네 가지 인앱 메시지 유형( **슬라이드업**, **모달**, **전체** 및 **HTML 전체**)이 있습니다.

### 인앱 메시지 모델 속성

인앱 메시지 모델은 모든 인앱 메시지의 기본을 제공합니다.

|등록정보          | 설명                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | 메시지 JSON 표현입니다.                                                                                |
|`message`         | 메시지 텍스트입니다.                                                                                                      |
|`header`          | 메시지 헤더입니다.                                                                                                    |
|`uri`             | 버튼 클릭 액션과 연결된 URI입니다.                                                                       |
|`imageUrl`        | 메시지 이미지 URL입니다.                                                                                                 |
|`zippedAssetsUrl` | HTML 콘텐츠를 표시하도록 준비된 압축된 에셋입니다.                                                                    |
|`useWebView`      | 버튼 클릭 동작이 웹 보기를 사용하여 리디렉션할지 여부를 나타냅니다.                                            |
|`duration`        | 메시지 표시 기간입니다.                                                                                          |
|`clickAction`     | 버튼 클릭 액션 유형입니다. 세 가지 유형(`NEWS_FEED`, `URI`, `NONE`)이 있습니다.                                     |
|`dismissType`     | 메시지 닫기 유형. 두 가지 유형(`SWIPE` 및 `AUTO_DISMISS`)이 있습니다.                                                 |
|`messageType`     | SDK에서 지원하는 인앱 메시지 유형입니다. 네 가지 유형(`SLIDEUP`, `MODAL`, `FULL`, `HTML_FULL`)이 있습니다.          |
|`extras`          | 메시지 추가 항목 사전. 기본값: `[:]`.                                                                   |
|`buttons`         | 인앱 메시지의 버튼 목록입니다.                                                                             |
|`toString()`      | 문자열 표현으로서의 메시지입니다.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

인앱 메시지 모델에 대한 전체 참조는 [안드로이드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage) 설명서를 참조하십시오.

### 인앱 메시지 버튼 모델 속성

인앱 메시지에 버튼을 추가하여 작업 및 로그 분석을 수행할 수 있습니다. 버튼 모델은 모든 인앱 메시지 버튼의 기본을 제공합니다.

|등록정보          | 설명                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | 버튼의 텍스트입니다.                                                                                                     |
|`uri`             | 버튼 클릭 액션과 연결된 URI입니다.                                                                            |
|`useWebView`      | 버튼 클릭 동작이 웹 보기를 사용하여 리디렉션할지 여부를 나타냅니다.                                                 |
|`clickAction`     | 사용자가 버튼을 클릭할 때 처리되는 클릭 동작 유형입니다. 세 가지 유형(`NEWS_FEED`, `URI`, `NONE`)이 있습니다. |
|`id`              | 메시지의 버튼 ID.                                                                                               |
|`toString()`      | 문자열 표현으로서의 버튼입니다.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

버튼 모델에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button) 설명서를 참조하십시오.

## GIF 지원

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

