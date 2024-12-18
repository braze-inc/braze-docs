---
nav_title: 인앱 메시지 UI 위임
article_title: 인앱 메시지 UI Delegate for iOS
platform: Swift
page_order: 2
description: "이 참조 문서에서는 Swift SDK에 대한 iOS 인앱 메시징 위임 설정을 다룹니다."
channel:
  - in-app messages

---

# 인앱 메시지 UI delegate

> 선택적 [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate)을(를) 사용하여 앱 내 메시지의 프레젠테이션을 사용자 정의하고 다양한 라이프사이클 이벤트에 반응하십시오. 이 위임 프로토콜은 추가 처리를 위해 트리거된 인앱 메시지 페이로드를 수신하고 표시 생애주기 이벤트를 수신하며 표시 타이밍을 제어하는 데 사용할 수 있습니다. 

## 전제 조건

`BrazeInAppMessageUIDelegate`를 사용하려면 다음을 수행합니다.
* 기본값 [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) 구현을 `inAppMessagePresenter`으로 사용해야 합니다. 
* 프로젝트에 `BrazeUI` 라이브러리를 포함해야 합니다.

## 인앱 메시지 대리자 설정

샘플 코드를 따라 Braze 인스턴스에 [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) 위임 개체를 설정하십시오:

{% tabs %}
{% tab swift %}

먼저 `BrazeInAppMessageUIDelegate` 프로토콜과 원하는 모든 해당 메서드를 구현하십시오. 다음 예제에서는 애플리케이션의 `AppDelegate` 클래스에서 이 프로토콜을 구현합니다.

```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```

그런 다음, 이 인앱 메시지 UI를 `inAppMessagePresenter`로 할당하기 전에 `BrazeInAppMessageUI` 인스턴스에서 `delegate` 오브젝트를 할당합니다.

```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```

{% endtab %}
{% tab 목표-C %}

먼저 `BrazeInAppMessageUIDelegate` 프로토콜과 원하는 모든 해당 메서드를 구현하십시오. 다음 예제에서는 애플리케이션의 `AppDelegate` 클래스에서 이 프로토콜을 구현합니다.

```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```

그런 다음, 이 인앱 메시지 UI를 `inAppMessagePresenter`로 할당하기 전에 `BrazeInAppMessageUI` 인스턴스에서 `delegate` 오브젝트를 할당합니다.

```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

일부 위임 메서드가 언어 런타임과의 매개변수 비호환성으로 인해 Objective-C에서 사용할 수 없습니다.

{% endtab %}
{% endtabs %}

### 단계별 가이드

인앱 메시지 UI 대리자의 단계별 구현에 대해서는 이 [튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)을 참조하십시오.

## iOS용 인앱 메시지 방향 사용자 지정

### 선호하는 방향 설정

모든 인앱 메시지를 기기 방향에 관계없이 특정 방향으로 표시되도록 구성할 수 있습니다. 선호하는 방향을 설정하려면 `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)를 사용하여 `PresentationContext`의 `preferredOrientation` 속성을 설정하십시오. 

{% tabs %}
{% tab swift %}

예를 들어, 세로 방향을 기본 방향으로 만들려면 다음을 수행합니다.

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endtab %}
{% tab 목표-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endtab %}
{% endtabs %}

인앱 메시지가 표시된 후 메시지가 계속 표시되는 동안 기기 방향이 변경되면 메시지의 `orientation` 구성에서 지원되는 경우 메시지가 기기와 함께 회전합니다.

기기의 방향이 인앱 메시지의 `orientation` 속성정보에서도 지원해야 메시지가 표시됩니다. 또한 `preferredOrientation` 설정은 Xcode에서 대상 설정의 **배포 정보** 섹션 아래 애플리케이션이 지원하는 인터페이스 방향에 포함된 경우에만 적용됩니다.

![Xcode에서 지원되는 방향.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
방향은 메시지의 프레젠테이션에만 적용됩니다. 기기의 방향이 바뀌면 메시지 보기가 지원하는 방향 중 하나를 채택합니다. 작은 기기(iPhone, iPod Touch)에서는 모달 또는 전체 인앱 메시지에 가로 방향을 설정하면 콘텐츠가 잘릴 수 있습니다.
{% endalert %}

### 메시지 방향 수정

메시지별로 방향을 설정할 수도 있습니다. 이 속성은 해당 메시지에 사용할 수 있는 모든 방향 유형을 정의합니다. 이 작업을 수행하려면 주어진 `Braze.InAppMessage`에서 `orientation` 속성정보를 설정합니다.

{% tabs %}
{% tab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endtab %}
{% tab 목표-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endtab %}
{% endtabs %}

## 다크 모드 비활성화

사용자 기기에 다크 모드가 켜져 있는 경우 인앱 메시지에 다크 모드 스타일이 적용되지 않도록 하려면 `inAppMessage(_:prepareWith:)` [위임 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)를 구현합니다. 메서드에 전달된 `PresentationContext`에는 표시할 `InAppMessage` 오브젝트에 대한 참조가 포함되어 있습니다. 각 `InAppMessage`에는 `dark` 및 `light` 모드 테마를 포함하는 `themes` 속성정보가 있습니다. `themes.dark` 속성정보를 `nil`로 설정하면 Braze가 인앱 메시지를 라이트 테마로 자동 표시합니다.

버튼이 있는 인앱 메시지 유형에는 `buttons` 속성정보에 추가 `themes` 오브젝트가 있습니다. 버튼이 다크 모드 스타일을 채택하지 않도록 하려면 [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d)을 사용하여 `light` 테마가 적용되고 `dark` 테마가 적용되지 않은 새 버튼 배열을 생성할 수 있습니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup
    
    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal
    
    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage
    
    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full
    
    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage
    
    default:
      break
  }
}
```

{% endtab %}
{% tab 목표-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## 버튼 클릭 사용자 지정

인앱 메시지 버튼 정보에 액세스하거나 클릭 동작을 재정의하려면 [`BrazeInAppMessageUIDelegate.inAppMessage(_:shouldProcess:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:shouldprocess:buttonid:message:view:)-122yi)를 구현합니다. `true`를 반환하여 Braze가 클릭 동작을 처리하도록 하거나, `false`를 반환하여 동작을 재정의합니다.
{% tabs %}
{% tab swift %}

```swift
  func inAppMessage(
    _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
    buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
  ) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }
    
    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab 목표-C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}


## 디스플레이 중 상태 표시줄 숨기기

`Full`, `FullImage`, `HTML`의 인앱 메시지에서 SDK는 기본적으로 상태 표시줄을 숨깁니다. 다른 유형의 인앱 메시지에서 상태 표시줄은 그대로 유지됩니다. 이 동작을 구성하려면 `inAppMessage(_:prepareWith:)` [위임 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)를 사용하여 `PresentationContext`에서 `statusBarHideBehavior` 속성정보를 설정합니다. 이 필드는 다음 값 중 하나를 사용합니다:

| 상태 표시줄 숨기기 동작            | 설명                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | 메시지 보기에서 상태 표시줄 숨김 상태를 결정합니다.                                 |
| `.hidden`                           | 항상 상태 표시줄을 숨기십시오.                                                           |
| `.visible`                          | 항상 상태 표시줄을 표시합니다.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 디스플레이 타이밍 사용자 지정 

사용자 경험의 특정 시점에 사용 가능한 인앱 메시지 표시 여부를 제어할 수 있습니다. 전체 화면으로 게임을 하거나 로딩 화면에서 인앱 메시지가 나타나지 않도록 하고 싶다면 보류 중인 인앱 메시지를 지연시키거나 삭제할 수 있습니다. 인앱 메시지의 타이밍을 제어하려면 `inAppMessage(_:displayChoiceForMessage:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)를 사용하여 `BrazeInAppMessageUI.DisplayChoice` 속성을 설정하십시오. 

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab 목표-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

다음 값 중 하나를 반환하도록 `BrazeInAppMessageUI.DisplayChoice`을(를) 구성하십시오:

| 디스플레이 선택                      | 동작                                                                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | 메시지는 즉시 표시됩니다. 이것은 기본값입니다.                                                       |
| `.reenqueue`                        | 메시지는 표시되지 않고 스택의 맨 위로 다시 배치됩니다.                                       |
| `.later`                            | 메시지는 표시되지 않고 스택의 맨 위로 다시 배치됩니다. (사용되지 않음, `.reenqueue`을(를) 사용하십시오) |
| `.discard`                          | 메시지는 폐기되며 표시되지 않습니다.                                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 구현 샘플

우리 예제 폴더에서 `InAppMessageUI`을(를) 참조하여 [Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) 및 [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)의 샘플을 확인하세요.

