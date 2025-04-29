{% multi_lang_include developer_guide/prerequisites/swift.md %} 인앱 메시지를 활성화해야 합니다.

## 메시지 유형

{% tabs %}
{% multi_lang_include developer_guide/_shared/push_notifications/message_types/swift.md %}
{% endtabs %}

## 인앱 메시지 활성화

### 1단계: `BrazeInAppMessagePresenter`의 구현을 만드세요.

Braze가 인앱 메시지를 표시할 수 있도록 하려면, `BrazeInAppMessagePresenter` 프로토콜의 구현을 만들고 이를 Braze 인스턴스의 선택적 `inAppMessagePresenter`에 할당하세요. `BrazeInAppMessageUI` 오브젝트를 인스턴스화하여 기본 Braze UI 프리젠터를 사용할 수도 있습니다.

`BrazeInAppMessageUI` 클래스에 액세스하려면 `BrazeUI` 라이브러리를 가져와야 합니다.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

### 2단계: 일치하는 트리거가 없습니다.

관련 `BrazeDelegate` 클래스 내에서 [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/)을 구현하세요. Braze가 특정 이벤트에 대한 일치하는 트리거를 찾지 못하면, 이 메서드를 자동으로 호출합니다.
