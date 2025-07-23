{% multi_lang_include developer_guide/prerequisites/swift.md %}

## UI 델리게이트 설정(필수)

인앱 메시지 표시를 사용자 지정하고 다양한 수명 주기 이벤트에 반응하려면 다음을 설정해야 합니다. [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate). 트리거된 인앱 메시지 페이로드 수신 및 처리, 디스플레이 수명 주기 이벤트 수신, 디스플레이 타이밍 제어에 사용되는 델리게이트 프로토콜입니다. `BrazeInAppMessageUIDelegate` 을 사용하려면 다음을 수행해야 합니다:
- 기본 [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) 구현을 `inAppMessagePresenter`. 
- 프로젝트에 `BrazeUI` 라이브러리를 포함하세요.

### 1단계: `BrazeInAppMessageUIDelegate` 프로토콜 구현 

먼저 `BrazeInAppMessageUIDelegate` 프로토콜과 원하는 모든 해당 메서드를 구현하십시오. 다음 예제에서는 애플리케이션의 `AppDelegate` 클래스에서 이 프로토콜을 구현합니다.

{% tabs %}
{% tab swift %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### 2단계: `delegate` 객체 할당 

이 인앱 메시지 UI를 `inAppMessagePresenter` 로 할당하기 전에 `BrazeInAppMessageUI` 인스턴스에 `delegate` 객체를 할당합니다.

{% tabs %}
{% tab swift %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
일부 위임 메서드가 언어 런타임과의 매개변수 비호환성으로 인해 Objective-C에서 사용할 수 없습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
인앱 메시지 UI 대리자의 단계별 구현에 대해서는 이 [튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)을 참조하십시오.
{% endalert %}

## 클릭 시 동작

각 `Braze.InAppMessage` 오브젝트에는 해당 [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction)이 포함되어 있으며, 이는 클릭 시 동작을 정의합니다. 

### 클릭 작업 유형

`Braze.InAppMessage`의 `clickAction` 속성정보에서 기본값은 `.none`이지만 다음 값 중 하나로 설정할 수 있습니다.

| `ClickAction` | 클릭 시 동작 |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | 외부 브라우저에서 지정된 URL을 엽니다. `useWebView` 을 `true` 으로 설정하면 웹 보기로 열립니다. |
| `.newsFeed` | 메시지를 클릭하면 뉴스피드가 표시되고 메시지가 해제됩니다.<br><br>**참고:** 뉴스피드는 더 이상 사용되지 않습니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요. |
| `.none` | 클릭하면 메시지가 삭제됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
버튼이 포함된 인앱 메시지의 경우 버튼 텍스트를 추가하기 전에 클릭 동작이 추가되면 `clickAction` 메시지도 최종 페이로드에 포함됩니다.
{% endalert %}

### 클릭 시 동작 사용자 지정

이 동작을 사용자 지정하려면 다음 샘플을 참조하여 `clickAction` 속성정보를 수정할 수 있습니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, 
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab 목표-C %}

`inAppMessage(_:prepareWith:)` 메서드는 Objective-C에서 사용할 수 없습니다.

{% endtab %}
{% endtabs %}

### 사용자 지정 동작 처리하기

다음 [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) 위임 메서드가 인앱 메시지를 클릭할 때 호출됩니다. 인앱 메시지 버튼 및 HTML 인앱 메시지 버튼(링크)을 클릭한 경우 버튼 ID가 선택적 매개변수로 제공됩니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

이 메서드는 Braze에서 클릭 동작을 계속 실행할지 여부를 나타내는 부울 값을 반환합니다.

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
{% tab OBJECTIVE-C %}
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

## 모달 해지 사용자 지정

외부 탭 해제 기능을 활성화하려면 사용자 지정하려는 인앱 메시지 유형의 `Attributes` 구조에서 `dismissOnBackgroundTap` 속성정보를 수정하면 됩니다. 

예를 들어 Modal 이미지 인앱 메시지에 이 기능을 사용하려면 다음과 같이 구성할 수 있습니다.

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

`Attributes` 을 통한 사용자 지정은 Objective-C에서 사용할 수 없습니다.

{% endtab %}
{% endtabs %}

기본값은 `false` 입니다. 사용자가 인앱 메시지 외부를 클릭할 때 Modal 인앱 메시지의 해제 여부를 결정합니다.

| `DismissModalOnOutsideTap` | 설명 |
|----------|-------------|
| `true`         | Modal 인앱 메시지는 외부를 탭하면 해제됩니다.     |
| `false`        | 기본 Modal 인앱 메시지는 외부를 탭해도 해제되지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

인앱 메시지 사용자 지정에 대한 자세한 내용은 이 [문서](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization)를 참조하세요.

## 메시지 방향 사용자 지정

인앱 메시지의 방향을 사용자 지정할 수 있습니다. 모든 메시지에 대해 새로운 기본 방향을 설정하거나 단일 메시지에 대해 사용자 지정 방향을 설정할 수 있습니다.

{% tabs local %}
{% tab 모든 메시지 %}
모든 인앱 메시지의 기본 방향을 선택하려면 다음과 같이 [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) 메서드를 사용하여 `PresentationContext` 에서 `preferredOrientation` 속성을 설정합니다. 

예를 들어 세로 방향을 기본 방향으로 설정합니다:

{% subtabs %}
{% subtab swift %}
```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 단일 메시지 %}
단일 메시지의 방향을 설정하려면 `Braze.InAppMessage` 의 `orientation` 속성을 수정합니다:

{% subtabs %}
{% subtab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

인앱 메시지가 표시된 후 메시지가 표시되는 동안 디바이스 방향이 변경되면 메시지가 디바이스와 함께 회전합니다(메시지의 `orientation` 구성에서 지원되는 경우).

메시지가 표시되려면 인앱 메시지의 `orientation` 속성에서 디바이스 방향도 지원해야 합니다. 또한 `preferredOrientation` 설정은 Xcode에서 대상 설정의 **배포 정보** 섹션 아래 애플리케이션이 지원하는 인터페이스 방향에 포함된 경우에만 적용됩니다.

![Xcode에서 지원되는 방향.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
방향은 메시지의 프레젠테이션에만 적용됩니다. 기기의 방향이 바뀌면 메시지 보기가 지원하는 방향 중 하나를 채택합니다. 작은 기기(iPhone, iPod Touch)에서는 모달 또는 전체 인앱 메시지에 가로 방향을 설정하면 콘텐츠가 잘릴 수 있습니다.
{% endalert %}

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
{% tab OBJECTIVE-C %}

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

{% alert tip %}
샘플( `InAppMessageUI`)은 [Swift Braze SDK 리포지토리](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) 및 [Objective-C에서](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI) 확인할 수 있습니다.
{% endalert %}

## 상태 표시줄 숨기기

`Full`, `FullImage`, `HTML`의 인앱 메시지에서 SDK는 기본적으로 상태 표시줄을 숨깁니다. 다른 유형의 인앱 메시지에서 상태 표시줄은 그대로 유지됩니다. 이 동작을 구성하려면 `inAppMessage(_:prepareWith:)` [위임 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)를 사용하여 `PresentationContext`에서 `statusBarHideBehavior` 속성정보를 설정합니다. 이 필드는 다음 값 중 하나를 사용합니다:

| 상태 표시줄 숨기기 동작            | 설명                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | 메시지 보기에서 상태 표시줄 숨김 상태를 결정합니다.                                 |
| `.hidden`                           | 항상 상태 표시줄을 숨기십시오.                                                           |
| `.visible`                          | 항상 상태 표시줄을 표시합니다.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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
{% tab OBJECTIVE-C %}

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

## 앱 스토어 리뷰 프롬프트 사용자 지정

캠페인에서 인앱 메시지를 사용하여 사용자에게 앱 스토어 리뷰를 요청할 수 있습니다.

{% alert note %}
이 예제 프롬프트는 Braze의 기본 동작을 재정의하기 때문에 구현된 경우 노출 횟수를 자동으로 추적할 수 없습니다. [자체 분석을 기록해야]({{site.baseurl}}/developer_guide/analytics/) 합니다.
{% endalert %}

### 1단계: 인앱 메시지 위임자를 설정합니다

먼저, 앱에서 [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_setting-up-the-ui-delegate-required)을 설정하세요. 

### 2단계: 기본 App Store 리뷰 메시지 비활성화

다음으로, 기본 App Store 리뷰 메시지를 비활성화하기 위해 `inAppMessage(_:displayChoiceForMessage:)` [위임 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)를 구현합니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

### 3단계: 딥링크를 생성합니다

딥링크 처리 코드에서 `{YOUR-APP-SCHEME}:app-store-review` 딥링크를 처리하기 위해 다음 코드를 추가합니다. `StoreKit`를 가져와서 `SKStoreReviewController`를 사용해야 합니다.

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

### 4단계: 커스텀 클릭 시 동작 설정

다음으로, 다음을 사용하여 인-앱 메시징 캠페인을 만드십시오:

- 키-값 쌍 `"AppStore Review" : "true"`
- 클릭 시 동작이 '앱으로 딥링크'로 설정되며 딥링크 `{YOUR-APP-SCHEME}:app-store-review`를 사용합니다.

{% endraw %}

{% alert tip %}
Apple은 사용자당 연간 최대 세 번으로 App Store 리뷰 요청을 제한하므로 캠페인에서도 사용자당 연간 세 번으로 [한도를 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)해야 합니다.<br><br>사용자는 App Store 리뷰 프롬프트를 끌 수도 있습니다. 결과적으로, 커스텀 리뷰 프롬프트는 기본 App Store 리뷰 프롬프트의 표시를 보장하지 않으며 직접적으로 리뷰를 요청해서는 안 됩니다.
{% endalert %}
