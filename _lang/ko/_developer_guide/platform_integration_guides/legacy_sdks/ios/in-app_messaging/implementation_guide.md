---
nav_title: 고급 구현 (선택 사항)
article_title: iOS용 인앱 메시지 구현 가이드(선택 사항)
platform: iOS
page_order: 6
description: "이 고급 구현 가이드에서는 iOS 인앱 메시지 코드 고려사항, 저희 팀이 구축한 세 가지 사용 사례 및 관련 코드 스니펫을 다룹니다."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
기본 인앱 메시지 개발자 통합 가이드를 찾고 계신가요? 여기에서 확인하세요[참조: ]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/).
{% endalert %}

# 인앱 메시징 구현 가이드

> 이 고급 구현 가이드(선택 사항)에서는 인앱 메시지 코드 고려사항, 저희 팀이 구축한 세 가지 커스텀 사용 사례 및 관련 코드 스니펫을 다룹니다. Braze Demo 저장소 [여기](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)를 방문하세요! 이 구현 가이드는 Swift 구현을 중심으로 하지만 관심 있는 사람을 위해 Objective-C 스니펫도 제공됩니다. HTML 구현을 찾고 계신가요? [HTML 템플릿 리포지토리를](https://github.com/braze-inc/in-app-message-templates) 살펴보세요!

## 코드 고려 사항

다음 가이드에서는 기본 인앱 메시지 외에 사용할 수 있는 선택적 커스텀 개발자 통합도 제공합니다. 커스텀 보기 컨트롤러는 각 사용 사례에 포함되어 기능을 확장하고 인앱 메시지의 모양과 느낌을 기본적으로 사용자 지정하는 예제를 제공합니다.

### ABKInAppMessage 하위 클래스

다음 코드 스니펫은 인앱 메시지를 채우려는 서브클래스 보기를 결정하는 Braze SDK의 UI 위임 메서드입니다. 이 가이드에서는 기본 구현을 다루고 전체, 슬라이드업 및 Modal 서브클래스를 매력적인 방식으로 구현하는 방법을 보여줍니다. 커스텀 보기 컨트롤러를 설정하려면 모든 다른 인앱 메시지 서브클래스를 설정해야 합니다. 서브클래싱의 개념에 대해 확실히 이해한 후, [사용 사례](#sample-use-cases)를 확인하여 인앱 메시징 서브클래스를 구현하기 시작합니다.

{% tabs %}
{% tab Swift %}
**ABKInAppMessage 하위 클래스**<br>

```swift
extension AppboyManager: ABKInAppMessageUIDelegate {
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return slideupViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageModal: 
      return modalViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageFull:
      return fullViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
    }
  }
}
```
{% endtab %}
{% tab Objective-C %}
**ABKInAppMessage 하위 클래스**<br> 

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [self slideupViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [self modalViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [self fullViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

## 사용 사례

우리는 아래에 세 가지 사용 사례를 제공했습니다. 각 사용 사례는 자세한 설명, 관련 코드 스니펫 및 Braze 대시보드에서 인앱 메시지의 모양과 느낌에 대한 인상을 제공합니다.
- [커스텀 슬라이드업 인앱 메시지](#custom-slide-up-in-app-message)
- [커스텀 모달 인앱 메시지](#custom-modal-in-app-message)
- [커스텀 전체 인앱 메시지](#custom-full-in-app-message)

### 커스텀 슬라이드업 인앱 메시지

![나란히 놓인 두 개의 iPhone. 첫 번째 iPhone은 전화기 화면 하단을 터치하여 슬라이드업 메시지를 표시합니다. 두 번째 iPhone은 슬라이드업 메시지가 화면 위쪽에 위치하여 표시된 앱 탐색 버튼을 볼 수 있습니다.]({% image_buster /assets/img/iam_implementation/slideup.png %}){: style="float:right;max-width:45%;margin-left:15px;border:0;"}

슬라이드업 인앱 메시지를 작성하는 동안 기본 방법을 사용하여 메시지의 위치를 수정할 수 없다는 점을 알아차렸습니다. 메시지 위치를 수정하려면 `ABKInAppMessageSlideupViewController`를 서브클래스로 만들고 `offset` 변수를 자체 커스텀 변수로 재정의해야 합니다. 오른쪽의 이미지는 슬라이드업 인앱 메시지를 조정하는 방법의 예를 보여줍니다. 

[`SlideFromBottomViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift)에 방문하여 시작하십시오.

#### 기본 UI에 추가 동작 추가<br><br>

{% tabs %}
{% tab Swift %}
**`offset` 변수 업데이트**<br>
`offset` 변수를 업데이트하고 자체 오프셋을 필요에 맞게 설정합니다.
```swift
func setSlideConstraint() {
  offset = 0
}
```

```swift
override var offset: CGFloat {
  get {
    return super.offset
  }
  set {
    super.offset = newValue + adjustedOffset
  }
}
```

{% details 버전 3.34.0 또는 이전  %}
**`slideConstraint` 변수 업데이트**<br>
`slideConstraint` 공용 변수는 슈퍼클래스 `ABKInAppMessageSlideupViewController`에서 나옵니다. 

```swift
func setSlideConstraint() {
    slideConstraint?.constant = bottomSpacing
}
```

```swift
private var bottomSpacing: CGFloat {
    return AppboyManager.shared.activeApplicationViewController.topMostViewController().view.safeAreaInsets.bottom
}
``` 
Braze 데모 저장소를 방문하여 [`topMostViewController()`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/Utils/UIViewController_Util.swift#L17) 기능을 확인하세요.
{% enddetails %}
{% endtab %}
{% tab Objective-C %}
**`offset` 변수 업데이트**<br>
`offset` 변수를 업데이트하고 자체 오프셋을 필요에 맞게 설정합니다.
```objc
- (void)setOffset {
  self.offset = 0;
}
```

```objc
- (CGFloat)offset {
  return [super offset];
}
 
- (void)setOffset:(CGFloat)offset {
  [super setOffset:offset + [self adjustedOffset]];
}
```
{% details 버전 3.34.0 또는 이전  %}
**`slideConstraint` 변수 업데이트**<br>
`slideConstraint` 공용 변수는 슈퍼클래스 `ABKInAppMessageSlideupViewController`에서 나옵니다. 

```objc
- (void)self.setSlideConstraint:(NSLayoutConstraint *)slideConstraint {
  slideConstraint.constant = bottomSpacing;
}
```

```objc
- (CGFloat)bottomSpacing {
  return [AppboyManager shared].activeApplicationViewController.topMostViewController.view.safeAreaInsets.bottom;
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**재정의 및 커스텀 제약 조건 설정**<br>
`beforeMoveInAppMessageViewOnScreen()`을 재정의하고 필요에 맞게 커스텀 제약 조건 값을 설정합니다. 원래 값은 슈퍼클래스에 설정됩니다.

```swift
override func beforeMoveInAppMessageViewOnScreen() {
  super.beforeMoveInAppMessageViewOnScreen()
  setOffset()
}
```

{% details 버전 3.34.0 또는 이전 %}
```swift
override func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% enddetails %}

{% endtab %}
{% tab Objective-C %}
**재정의 및 커스텀 제약 조건 설정**<br> 
`beforeMoveInAppMessageViewOnScreen()`을 재정의하고 필요에 맞게 커스텀 제약 조건 값을 설정합니다. 원래 값은 슈퍼클래스에 설정됩니다.

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [super beforeMoveInAppMessageViewOnScreen];
  [self setOffset];
}
```

{% details 버전 3.34.0 또는 이전  %}
```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self setSlideConstraint:self.slideConstraint];
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

**기기 방향에 대한 제약 조건 조정**<br>
`viewWillTransition()`에서 각각의 값을 조정합니다. 서브클래스는 레이아웃 변경 중 제약 조건을 동기화해야 한다고 가정하기 때문입니다.

### 커스텀 모달 인앱 메시지

![Modal 인앱 메시지를 표시하는 iPhone으로, 여기서 스포츠 팀 목록을 살펴보고 좋아하는 팀을 선택할 수 있습니다. 이 인앱 메시지 하단에 큰 파란색 제출 버튼이 있습니다.]({% image_buster /assets/img/iam_implementation/modal.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

소중한 사용자 속성을 수집하는 매력적인 방법을 제공하기 위해 `ABKInAppMessageModalViewController`는 `UIPickerView`를 활용하여 서브클래스로 만들 수 있습니다. 커스텀 Modal 인앱 메시지를 사용하면 연결된 콘텐츠 또는 사용 가능한 목록을 통해 항목의 동적 목록에서 속성을 표시하고 캡처할 수 있습니다. 

자체 보기를 서브클래스로 만든 인앱 메시지에 삽입할 수 있습니다. 이 예제에서는 `UIPickerView`를 사용하여 `ABKModalInAppMessageViewController`의 기능을 확장하는 방법을 보여줍니다.

[ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift)에 방문하여 시작하십시오.

#### 대시보드 구성

대시보드에서 모달 인앱 메시지를 설정하려면 쉼표로 구분된 문자열로 형식화된 항목 목록을 제공해야 합니다. 이 예제에는, 연결된 콘텐츠를 사용하여 팀 이름의 JSON 목록을 가져오고 적절하게 형식을 지정합니다.

![인앱 메시지 작성기는 인앱 메시지의 모양에 대한 미리보기를 보여주지만 대신 Braze에 제공한 항목 목록을 표시합니다. Braze UI는 휴대폰으로 전송하지 않는 한 사용자 지정 인앱 메시지 UI를 표시하지 않으므로 미리보기에서는 메시지가 어떻게 표시될지 알 수 없으므로 보내기 전에 테스트해 보는 것이 좋습니다.]({% image_buster /assets/img/iam_implementation/dashboard1.png %})

키-값 페어에서 `attribute_key`를 제공합니다. 이 키는 사용자가 선택한 값과 함께 고객 프로필에 커스텀 속성으로 저장됩니다. 귀하의 커스텀 보기 로직은 Braze로 전송된 사용자 속성을 처리해야 합니다.

`ABKInAppMessage` 오브젝트의 `extras` 사전을 통해 올바른 보기를 표시하도록 알리는 `view_type` 키(있는 경우)를 쿼리할 수 있습니다. 인앱 메시지는 메시지별로 구성되므로 커스텀 및 기본값 Modal 보기가 조화를 이룰 수 있습니다.

![메시지 작성기에 두 개의 키-값 페어가 있습니다. 첫 번째 키-값 쌍은 "attribute_key"가 "즐겨찾는 팀"으로 설정되어 있고 두 번째 키-값 쌍은 "view_type"이 "picker"로 설정되어 있습니다.]({% image_buster /assets/img/iam_implementation/dashboard2.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Swift %}
**UI 표시 동작에 `view_type` 사용**<br>
원하는 서브클래스 보기 컨트롤러를 로드하도록 `view_type`에 대해 `extras` 사전을 쿼리합니다.

```swift
func modalViewController(inAppMessage: ABKInAppMessage) -> ABKInAppMessageModalViewController {
  switch inAppMessage.extras?[InAppMessageKey.viewType.rawValue] as? String {
  case InAppMessageViewType.picker.rawValue:
    return ModalPickerViewController(inAppMessage: inAppMessage)
  default:
    return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**UI 표시 동작에 `view_type` 사용**<br>
원하는 서브클래스 보기 컨트롤러를 로드하도록 `view_type`에 대해 `extras` 사전을 쿼리합니다.

```objc
- (ABKInAppMessageModalViewController *)modalViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyViewType];
  NSString *viewType = [inAppMessageData rawValueForInAppMessageViewType:InAppMessageViewTypePicker];
   
  if ([inAppMessage.extras objectForKey:key] && [inAppMessage.extras[key] isEqualToString:viewType]) {
    return [[ModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**오버라이드하고 커스텀 뷰를 제공**<br>
`loadView()`를 재정의하고 필요에 맞게 커스텀 제약 조건 값을 설정합니다.
```swift
override var nibname: String{
  return "ModalPickerViewController"
}

override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% tab Objective-C %}
**오버라이드하고 커스텀 뷰를 제공**<br>
`loadView()`를 재정의하고 필요에 맞게 커스텀 제약 조건 값을 설정합니다.
```objc
- (void)loadView {
  NSString *nibName = @"ModalPickerViewController";
  [[NSBundle mainBundle] loadNibNamed:nibName owner:self options:nil];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**동적 목록을 위한 변수 형식**<br>
`UIPickerView` 구성 요소를 다시 로드하기 전에 `inAppMessage` 메시지 변수가 _문자열_로 출력됩니다. 이 메시지는 올바르게 표시되도록 항목 배열로 형식화되어야 합니다. 예를 들어, 이것은 [`components(separatedBy: ", ")`](https://developer.apple.com/documentation/foundation/nsstring/1413214-components)을 사용하여 달성할 수 있습니다.
```swift
override func viewDidLoad() {
  super.viewDidLoad()
 
  items = inAppMessage.message.separatedByCommaSpaceValue
  pickerView.reloadAllComponents()
}
```
{% endtab %}
{% tab Objective-C %}
**PickerView에 대한 변수 형식 지정**<br>
`UIPickerView` 구성 요소를 다시 로드하기 전에 `inAppMessage` 메시지 변수가 _문자열_로 출력됩니다. 이 메시지는 올바르게 표시되도록 항목 배열로 형식화되어야 합니다. 예를 들어, 이것은 [`componentsSeparatedByString`](https://developer.apple.com/documentation/foundation/nsstring/1413214-componentsseparatedbystring?language=objc)을 사용하여 달성할 수 있습니다.
```objc
- (void)viewDidLoad {
  [super viewDidLoad];
   
  self.items = [[NSArray alloc] initWithArray:[self.inAppMessage.message componentsSeparatedByString:@", "]];
  [self.pickerView reloadAllComponents];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**커스텀 속성 할당**<br>
서브클래스를 사용하여 사용자가 제출을 누른 후 속성과 이에 대응하는 선택된 값을 Braze에 전달합니다.
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective-C %}
**커스텀 속성 할당**<br>
서브클래스를 사용하여 사용자가 제출을 누른 후 속성과 이에 대응하는 선택된 값을 Braze에 전달합니다.
```objc
- (IBAction)primaryButtonTapped:(id)sender {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyAttributeKey];
   
  if (self.selectedItem.length > 0 && [self.inAppMessage.extras objectForKey:key]) {
    [[AppboyManager shared] setCustomAttributeWithKey:self.inAppMessage.extras[key] andStringValue:self.selectedItem];
  }
}
```
{% endtab %}
{% endtabs %}

{% alert tip %}
FaceTime을 통해 비디오를 공유하기 위해 커스텀 Modal 인앱 메시지를 활용하는 데 관심이 있으신가요? SharePlay 인앱 메시지 [구현 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/shareplay/)를 확인하세요.
{% endalert%}

### 커스텀 전체 인앱 메시지

![구성 옵션 목록을 표시하고 각 옵션 옆에 토글이 있는 인앱 메시지. 메시지 하단에 큰 파란색 제출 버튼이 있습니다.]({% image_buster /assets/img/iam_implementation/fullscreen.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

커스텀 전체 인앱 메시지를 사용하여 상호작용하고 사용자 친화적인 프롬프트를 만들어 귀중한 고객 데이터를 수집하세요. 오른쪽 예제는 알림 환경설정을 포함한 대화형 푸시 프라이머로 재구성된 커스텀 전체 인앱 메시지의 구현을 보여줍니다. 

[`FullListViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift)에 방문하여 시작하십시오.

#### 대시보드 구성

대시보드에서 커스텀 전체 인앱 메시지를 설정하려면 쉼표로 구분된 문자열로 형식화된 태그 목록을 제공해야 합니다. 

키-값 페어에서 `attribute_key`를 제공합니다. 이 키는 사용자가 선택한 값과 함께 고객 프로필에 커스텀 속성으로 저장됩니다. 귀하의 커스텀 보기 로직은 Braze로 전송된 사용자 속성을 처리해야 합니다.

![메시지 작성기에 세 개의 키-값 페어가 있습니다. 첫 번째 키-값 쌍 "attribute_key"는 "푸시 태그"로 설정하고, 두 번째 "subtitle_text"는 "알림을 활성화하면..."로 설정하며, 세 번째 "view_type"은 "table_list"로 설정합니다.]({% image_buster /assets/img/iam_implementation/dashboard3.png %}){: style="max-width:65%;"}

#### 인앱 메시지 터치 가로채기
![설정 및 토글 행을 표시하는 Apple 기기. 사용자 지정 보기가 버튼을 처리하며, 버튼 컨트롤 이외의 모든 터치는 앱 내 메시지에 의해 처리되어 해제됩니다.]({% image_buster /assets/img/iam_implementation_guide.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
인앱 메시지 터치를 가로채는 작업은 커스텀 전체 인앱 메시지 버튼이 올바르게 작동하도록 하는 데 매우 중요합니다. 기본적으로, `ABKInAppMessageImmersive`에서는 메시지에 탭 제스처 인식기를 추가하여 사용자가 버튼 없이 메시지를 해제할 수 있습니다. `UISwitch` 또는 버튼을 `UITableViewCell` 보기 계층 구조에 추가하면 이제 터치는 이제 커스텀 보기에 의해 처리됩니다. iOS 6부터 버튼 및 기타 컨트롤이 제스처 인식기보다 우선하므로, 커스텀 전체 인앱 메시지가 정상적으로 작동합니다. 

