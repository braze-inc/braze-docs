---
nav_title: 인앱 메시지
article_title: Flutter용 인앱 메시지
platform: Flutter
page_order: 4
page_type: reference
description: "이 문서에서는 분석 사용자 지정 및 로깅을 포함하여 Flutter를 사용하는 iOS 및 Android 앱의 인앱 메시지에 대해 설명합니다."
channel: in-app messages

---

# 인앱 메시지 통합

> Flutter를 사용하여 Android 및 iOS용 인앱 메시지를 통합하고 사용자 지정하는 방법을 알아보세요.

## 인앱 메시지 UI 활성화

Flutter의 인앱 메시징을 iOS와 통합하려면 [Braze Swift SDK를 사용하여 인앱 메시징을 활성화하세요]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#enabling-in-app-messages). Android의 경우 추가 단계가 없습니다.

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

인앱 메시지 자동 표시를 비활성화하려면 네이티브 레이어에서 이러한 업데이트를 수행하세요.

{% tabs %}
{% tab Android %}

1. 버전 `2.2.0` 부터 기본적으로 활성화되는 자동 통합 초기화 프로그램을 사용하고 있는지 확인합니다.
2. `braze.xml` 파일에 다음 줄을 추가하여 인앱 메시지 작동 기본값을 `DISCARD` 으로 설정합니다.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

{% endtab %}
{% tab iOS %}

1. [여기 iOS 문서에](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui) 설명된 대로 `BrazeInAppMessageUIDelegate` 델리게이트를 구현하세요.

2. `.discard` 을 반환하도록 `inAppMessage(_:displayChoiceForMessage:)` 델리게이트 메서드를 업데이트합니다.

{% endtab %}
{% endtabs %}

## 인앱 메시지 데이터 수신

Flutter 앱에서 인앱 메시지 데이터를 수신하려면 `BrazePlugin` 에서 [다트 스트림을](https://dart.dev/tutorials/language/streams) 사용하여 인앱 메시지 데이터 전송을 지원합니다.

`BrazeInAppMessage` 개체는 `uri`, `message`, `header`, `buttons`, `extras` 등 기본 모델 개체에서 사용할 수 있는 필드의 하위 집합을 지원합니다.

### 1단계: Dart 레이어에서 인앱 메시지 데이터 듣기

Dart 레이어에서 인앱 메시지 데이터를 수신하려면 아래 코드를 사용하여 `StreamSubscription` 을 생성하고 `braze.subscribeToInAppMessages()` 으로 호출합니다. 스트림 구독이 더 이상 필요하지 않은 경우 `cancel()` 으로 문의하세요.

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

1단계의 다트 레이어에서 데이터를 수신하려면 다음 코드를 추가하여 네이티브 레이어에서 인앱 메시지 데이터를 전달합니다.

{% tabs %}
{% tab Android %}

인앱 메시지 데이터는 안드로이드 계층에서 자동으로 전달됩니다.

{% endtab %}
{% tab iOS %}

### 옵션 1 - 사용 `BrazeInAppMessageUIDelegate`

1. [핵심 인앱 메시지 델리게이트에](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui) 대한 iOS 문서에 설명된 대로 `BrazeInAppMessageUIDelegate` 델리게이트를 구현하세요.

2. [`willPresent` 델리게이트 구현을](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv) 업데이트하여 `BrazePlugin.process(inAppMessage)` 으로 호출합니다.

### 옵션 2 - 사용자 지정 인앱 메시지 프레젠터

1. 인앱 메시지 UI를 활성화했는지 확인하고 `inAppMessagePresenter` 을 사용자 지정 발표자로 설정합니다.
```swift
    let inAppMessageUI = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = inAppMessageUI
```
2. 사용자 지정 발표자 클래스를 만들고 `BrazePlugin.process(inAppMessage)` 내에서 [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra).
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

콜백을 사용할 수 있게 되기 전에 트리거된 인앱 메시지를 저장하고 설정된 후에 재생하려면 `BrazePlugin` 을 초기화할 때 `customConfigs` 맵에 다음 항목을 추가합니다:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## 샘플 인앱 메시지 테스트

샘플 인앱 메시지를 테스트하려면 다음 단계를 따르세요.

1. `braze.changeUser('your-user-id')` 메서드를 호출하여 React 애플리케이션에서 활성 사용자를 설정합니다.
2. 대시보드의 **캠페인** 페이지로 이동하여 [이 가이드에][1] 따라 새 인앱 메시지 캠페인을 만들 수 있습니다.
3. 테스트 인앱 메시징 캠페인을 작성하고 **테스트** 탭으로 이동합니다. 테스트 사용자와 동일한 `user-id` 을 추가하고 **테스트 보내기를** 클릭합니다.
4. 푸시 알림을 탭하면 디바이스에 인앱 메시지가 표시됩니다.

## GIF 지원

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

![자신의 사용자 ID를 테스트 수신자로 추가하여 인앱 메시지를 테스트할 수 있는 Braze 인앱 메시지 캠페인을 보여줍니다.][2]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {% image_buster /assets/img/react-native/iam-test.png %} "인앱 메시징 테스트"
