{% multi_lang_include developer_guide/prerequisites/swift.md %} 또한 인앱 메시지를 인에이블먼트해야 합니다.

## 메시지 유형

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## 인앱 메시지 활성화

### 1단계: 의 구현을 만듭니다. `BrazeInAppMessagePresenter`

Braze가 인앱 메시지를 표시하도록 하려면 `BrazeInAppMessagePresenter` 프로토콜의 구현을 생성하고 이를 Braze 인스턴스의 선택적 `inAppMessagePresenter` 에 할당하세요. `BrazeInAppMessageUI` 오브젝트를 인스턴스화하여 기본 Braze UI 프리젠터를 사용할 수도 있습니다.

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

### 2단계: 일치하는 트리거 처리 안 함

구현 [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/) 를 관련 `BrazeDelegate` 클래스 내에서 구현합니다. 특정 이벤트에 대해 일치하는 트리거를 찾지 못하면 Braze는 이 메서드를 자동으로 호출합니다.
