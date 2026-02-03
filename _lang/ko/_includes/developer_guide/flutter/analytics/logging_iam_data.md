{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## 로그 메시지 데이터

`BrazeInAppMessage` 를 사용하여 분석을 기록하려면 원하는 분석 기능에 인스턴스를 전달합니다:

- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (버튼 인덱스와 함께)

For example:

```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## 메시지 데이터에 접근하기

Flutter 앱에서 인앱 메시지 데이터에 접근하려면, `BrazePlugin`은 [Dart Streams](https://dart.dev/tutorials/language/streams)를 사용하여 인앱 메시지 데이터를 전송하는 것을 지원합니다.

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
{% subtabs %}

인앱 메시지 데이터를 전달하는 방법은 두 가지가 있습니다:

{% subtab UI Delegate %}

1. [핵심 인앱 메시지 위임](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)에 대한 iOS 문서에 설명된 대로 `BrazeInAppMessageUIDelegate` 위임을 구현합니다.

2. `BrazePlugin.process(inAppMessage)`를 호출하도록 [`willPresent` 위임 구현](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv)을 업데이트합니다.
{% endsubtab %}

{% subtab custom presenter %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 3단계: 인앱 메시지에 대한 콜백 재생(선택 사항)

콜백을 사용하기 위해 먼저 트리거된 인앱 메시지를 저장하고 설정된 후에 재생하려면 `BrazePlugin`을 초기화할 때 `customConfigs` 맵에 다음 항목을 추가합니다.
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
