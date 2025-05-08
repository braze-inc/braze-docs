---
nav_title: 인앱 메시지
article_title: Flutter용 인앱 메시지
platform: Flutter
page_order: 4
page_type: reference
description: "이 문서에서는 분석 사용자 지정 및 로깅을 포함하여 Flutter를 사용하는 iOS 및 Android 앱의 인앱 메시지를 다룹니다."
channel: in-app messages

---

# 인앱 메시지 통합

> Flutter를 사용하여 Android 및 iOS용 인앱 메시지를 통합하고 사용자 지정하는 방법을 알아봅니다.

## 인앱 메시지 UI 활성화

Flutter의 인앱 메시징을 iOS와 통합하려면 [Braze Swift SDK를 사용하여 인앱 메시징을 활성화]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#enabling-in-app-messages)합니다. Android의 경우 추가 단계가 없습니다.

## 로깅 분석

`BrazeInAppMessage` 를 사용하여 분석을 기록하려면 원하는 분석 기능에 인스턴스를 전달합니다:
- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (버튼 인덱스와 함께)

예를 들어, 다음과 같습니다.
```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## 자동 표시 비활성화하기

인앱 메시지 자동 표시를 비활성화하려면 기본 레이어에서 이 업데이트를 수행합니다.

{% tabs %}
{% tab Android %}

1. 버전 `2.2.0`부터 기본적으로 활성화되는 자동 통합 초기화 프로그램을 사용하고 있는지 확인합니다.
2. `braze.xml` 파일에 다음 줄을 추가하여 인앱 메시지 작업의 기본값을 `DISCARD`로 설정합니다.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

{% endtab %}
{% tab iOS %}

1. [여기 iOS 문서](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)에서 설명한 대로 `BrazeInAppMessageUIDelegate` 위임을 구현합니다.

2. `.discard` 을 반환하도록 `inAppMessage(_:displayChoiceForMessage:)` 델리게이트 메서드를 업데이트합니다.

{% endtab %}
{% endtabs %}

## 인앱 메시지 데이터 수신

Flutter 앱에서 인앱 메시지 데이터를 수신하기 위해 `BrazePlugin`에서 [Dart 스트림](https://dart.dev/tutorials/language/streams)을 사용하여 인앱 메시지 데이터 전송을 지원합니다.

`BrazeInAppMessage` 개체는 `uri`, `message`, `header`, `buttons`, `extras` 등 기본 모델 오브젝트에서 사용할 수 있는 필드의 하위 집합을 지원합니다.

### 1단계: Dart 레이어에서 인앱 메시지 데이터 듣기

Dart 레이어에서 인앱 메시지 데이터를 수신하려면 아래 코드를 사용하여 `StreamSubscription`을 생성하고 `braze.subscribeToInAppMessages()`를 호출합니다. 스트림 가입이 더 이상 필요하지 않은 경우 `cancel()`을 수행합니다.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

예제는 샘플 앱의 [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) 를 참조하세요.

### 2단계: 네이티브 레이어에서 인앱 메시지 데이터 전달

1단계의 Dart 레이어에서 데이터를 수신하려면 다음 코드를 추가하여 기본 레이어에서 인앱 메시지 데이터를 전달합니다.

{% tabs %}
{% tab Android %}

인앱 메시지 데이터는 안드로이드 계층에서 자동으로 전달됩니다.

{% endtab %}
{% tab iOS %}

### 옵션 1 - `BrazeInAppMessageUIDelegate` 사용

1. [핵심 인앱 메시지 위임](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)에 대한 iOS 문서에 설명된 대로 `BrazeInAppMessageUIDelegate` 위임을 구현합니다.

2. `BrazePlugin.process(inAppMessage)`를 호출하도록 [`willPresent` 위임 구현](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv)을 업데이트합니다.

### 옵션 2 - 사용자 지정 인앱 메시지 프레젠터

1. 인앱 메시지 UI를 활성화했는지 확인하고 `inAppMessagePresenter`를 커스텀 프레젠터로 설정합니다.
```swift
    let inAppMessageUI = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = inAppMessageUI
```
2. 커스텀 프레젠터 클래스를 만들고 [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra)에서 `BrazePlugin.process(inAppMessage)`를 호출하니다.
```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    // Pass in-app message data to the Dart layer.
    BrazePlugin.processInAppMessage(message)

    // If you want the default UI to display the in-app message.
    super.present(message: message)
  }
}
```

{% endtab %}
{% endtabs %}

#### 인앱 메시지 콜백 재생하기

콜백을 사용하기 위해 먼저 트리거된 인앱 메시지를 저장하고 설정된 후에 재생하려면 `BrazePlugin`을 초기화할 때 `customConfigs` 맵에 다음 항목을 추가합니다.
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## 샘플 인앱 메시지 테스트

샘플 인앱 메시지를 테스트하려면 다음 단계를 따르세요.

1. `braze.changeUser('your-user-id')` 메서드를 호출하여 React 애플리케이션에서 활성 사용자를 설정합니다.
2. 대시보드의 **캠페인** 페이지로 이동하여 [이 가이드에]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) 따라 새 인앱 메시지 캠페인을 만들 수 있습니다.
3. 테스트 인앱 메시징 캠페인을 작성하고 **테스트** 탭으로 이동합니다. 테스트 사용자와 동일한 `user-id`를 추가하고 **테스트 보내기**를 클릭합니다.
4. 푸시 알림을 탭하면 기기에 인앱 메시지가 표시됩니다.

## GIF 지원

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

![자신의 사용자 ID를 테스트 수신자로 추가하여 인앱 메시지를 테스트할 수 있는 Braze 인앱 메시지 캠페인]({% image_buster /assets/img/react-native/iam-test.png %} "인앱 메시징 테스트")

