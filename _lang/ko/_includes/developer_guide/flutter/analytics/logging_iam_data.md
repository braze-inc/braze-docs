{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## 로깅 메시지 데이터

`BrazeInAppMessage`를 사용하여 분석을 기록하려면 원하는 분석 함수에 인스턴스를 전달하세요:

- `logInAppMessageClicked`
- `logInAppMessageImpression`
- `logInAppMessageButtonClicked` (버튼 인덱스와 함께)

예를 들어:

```dart
// Log a click
braze.logInAppMessageClicked(inAppMessage);
// Log an impression
braze.logInAppMessageImpression(inAppMessage);
// Log button index `0` being clicked
braze.logInAppMessageButtonClicked(inAppMessage, 0);
```

## 메시지 데이터에 접근하기

Flutter 앱에서 인앱 메시지 데이터에 접근하기 위해 `BrazePlugin`은 [Dart Streams](https://dart.dev/tutorials/language/streams)를 사용하여 인앱 메시지 데이터 전송을 지원합니다.

`BrazeInAppMessage` 오브젝트는 `uri`, `message`, `header`, `buttons`, `extras` 등 네이티브 모델 오브젝트에서 사용할 수 있는 필드의 하위 집합을 지원합니다.

### Dart 레이어에서 인앱 메시지 데이터 수신하기

Dart 레이어에서 인앱 메시지 데이터를 수신하려면 아래 코드를 사용하여 `StreamSubscription`을 생성하고 `braze.subscribeToInAppMessages()`를 호출하세요. 스트림 구독이 더 이상 필요하지 않으면 `cancel()`을 호출하세요.

```dart
// Create stream subscription
StreamSubscription inAppMessageStreamSubscription;

inAppMessageStreamSubscription = braze.subscribeToInAppMessages((BrazeInAppMessage inAppMessage) {
  // Handle in-app messages
}

// Cancel stream subscription
inAppMessageStreamSubscription.cancel();
```

예제는 Braze Flutter SDK 샘플 애플리케이션의 [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart)를 참조하세요.

### 네이티브 레이어에서 인앱 메시지 데이터 전달하기

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

인앱 메시지 데이터는 Android 및 iOS 네이티브 레이어 모두에서 자동으로 전달됩니다. 추가 설정은 필요하지 않습니다.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Flutter SDK 17.1.0 이하를 사용하는 경우, iOS 네이티브 레이어에서 인앱 메시지 데이터를 전달하려면 수동 설정이 필요합니다. 애플리케이션에 다음 중 하나가 포함되어 있을 수 있습니다. Flutter SDK 18.0.0으로 마이그레이션하려면 `BrazePlugin.processInAppMessage(_:)` 호출을 제거하세요. 데이터 전달은 이제 자동으로 처리됩니다.

{% subtabs %}
{% subtab UI Delegate %}

[`willPresent` 델리게이트 구현](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:willpresent:view:)-4pzvv)에서 `BrazePlugin.processInAppMessage(_:)` 호출을 제거하세요.

{% endsubtab %}

{% subtab Custom presenter %}

커스텀 프레젠터의 [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/present(message:)-f2ra) 구현에서 `BrazePlugin.processInAppMessage(message)` 호출을 제거하세요:

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

### 인앱 메시지 콜백 재생하기(선택 사항)

콜백을 사용할 수 있기 전에 트리거된 인앱 메시지를 저장하고, 콜백이 설정된 후에 재생하려면 `BrazePlugin`을 초기화할 때 `customConfigs` 맵에 다음 항목을 추가하세요:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
