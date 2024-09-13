---
nav_title: 고급 구현 (선택 사항)
article_title: 인앱 메시지 구현 가이드 (선택 사항)
platform: iOS
page_order: 6
description: "이 고급 구현 가이드는 iOS 인앱 메시지 코드 고려 사항, 우리 팀이 구축한 세 가지 사용 사례 및 관련 코드 스니펫을 다룹니다."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include 사용 중단/목적-c.md %}

<br>
{% alert important %}
기본 인앱 메시지 개발자 통합 가이드를 찾고 계십니까? 여기에서 찾으세요]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/).
{% endalert %}

# 인-앱 메시징 구현 가이드

> 이 선택적이고 고급 구현 가이드는 인앱 메시지 코드 고려 사항, 저희 팀이 만든 세 가지 커스텀 사용 사례 및 관련 코드 스니펫을 다룹니다. Braze Demo 저장소 [여기](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)를 방문하세요! 이 구현 가이드는 Swift 구현을 중심으로 하지만 관심 있는 사람들을 위해 Objective-C 코드 조각도 제공됩니다. HTML 구현을 찾고 계신가요? 우리의 [HTML 템플릿 저장소](https://github.com/braze-inc/in-app-message-templates)를 확인해보세요!

## 코드 고려사항

다음 가이드는 기본 인앱 메시지 외에 사용할 수 있는 선택적 커스텀 개발자 통합을 제공합니다. 커스텀 뷰 컨트롤러는 각 사용 사례에 포함되어 있어 기능을 확장하고 앱 내 메시지의 모양과 느낌을 네이티브로 커스터마이즈하는 예제를 제공합니다.

### ABKInAppMessage 하위 클래스

다음 코드 스니펫은 인앱 메시지를 채우려는 하위 클래스 보기를 결정하는 Braze 소프트웨어 개발 키트의 UI 대리자 메서드입니다. 이 가이드에서는 기본 구현을 다루고 전체, 슬라이드 업 및 모달 하위 클래스를 매력적인 방식으로 구현하는 방법을 보여줍니다. 사용자 정의 뷰 컨트롤러를 설정하려면 모든 다른 인앱 메시지 하위 클래스를 설정해야 합니다. 서브클래싱의 개념에 대해 확실히 이해한 후, [사용 사례](#sample-use-cases)를 확인하여 앱 내 메시징 서브클래스를 구현하기 시작하십시오.

{% tabs %}
{% tab 스위프트 %}
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
{% tab 오브젝티브-C %}
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

우리는 아래에 세 가지 사용 사례를 제공했습니다. 각 사용 사례는 자세한 설명, 관련 코드 스니펫 및 Braze 대시보드에서 앱 내 메시지가 어떻게 보이고 사용될 수 있는지에 대한 통찰을 제공합니다:
- [커스텀 슬라이드업 인앱 메시지](#custom-slide-up-in-app-message)
- [커스텀 모달 인앱 메시지](#custom-modal-in-app-message)
- [커스텀 full 인앱 메시지](#custom-full-in-app-message)

### 커스텀 슬라이드업 인앱 메시지

![나란히 놓인 두 개의 아이폰. 최초의 아이폰은 전화기 화면 하단을 터치하여 슬라이드 업 메시지를 표시합니다. 두 번째 아이폰은 화면에서 더 높이 위치한 슬라이드업 메시지를 가지고 있어 표시된 앱 탐색 버튼을 볼 수 있습니다.][2]{: style="float:right;max-width:45%;margin-left:15px;border:0;"}

슬라이드업 인앱 메시지를 작성하는 동안 기본 방법을 사용하여 메시지의 위치를 수정할 수 없다는 것을 알 수 있습니다. 이와 같은 수정은 `ABKInAppMessageSlideupViewController`을(를) 서브클래싱하고 `offset` 변수를 사용자 커스텀 변수로 재정의하여 가능합니다. 오른쪽의 이미지는 슬라이드 업 인-앱 메시지를 조정하는 방법의 예를 보여줍니다. 

[`SlideFromBottomViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift)에 방문하여 시작하십시오.

#### 기본 UI에 추가 동작 추가<br><br>

{% tabs %}
{% tab 스위프트 %}
**변수 `offset` 업데이트**<br>
변수를 업데이트하고 자신의 오프셋을 필요에 맞게 설정하십시오.
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
**변수 `slideConstraint` 업데이트**<br>
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
{% tab 오브젝티브-C %}
**변수 `offset` 업데이트**<br>
변수를 업데이트하고 자신의 오프셋을 필요에 맞게 설정하십시오.
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
**변수 `slideConstraint` 업데이트**<br>
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
{% tab 스위프트 %}
**무시하고 커스텀 제약 조건 설정**<br>
`beforeMoveInAppMessageViewOnScreen()`을(를) 재정의하고 필요에 맞게 커스텀 제약 조건 값을 설정하십시오. 원래 값은 슈퍼클래스에 설정됩니다.

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
{% tab 오브젝티브-C %}
**무시하고 커스텀 제약 조건 설정**<br> 
`beforeMoveInAppMessageViewOnScreen()`을(를) 재정의하고 필요에 맞게 커스텀 제약 조건 값을 설정하십시오. 원래 값은 슈퍼클래스에 설정됩니다.

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
해당 값을 `viewWillTransition()`에서 조정하십시오. 하위 클래스는 레이아웃 변경 중 제약 조건을 동기화하는 책임을 집니다.

### 커스텀 모달 인앱 메시지

![모달 인앱 메시지를 표시하는 iPhone으로, 스포츠 팀 목록을 순환하고 좋아하는 팀을 선택할 수 있습니다. 이 인앱 메시지의 하단에는 큰 파란색 제출 버튼이 있습니다.][3]{: style="float:right;max-width:23%;margin-left:15px;border:0;"}

`ABKInAppMessageModalViewController`은(는) `UIPickerView`을(를) 활용하여 귀중한 사용자 속성을 수집하는 매력적인 방법을 제공하기 위해 서브클래스화될 수 있습니다. 커스텀 모달 인앱 메시지를 사용하면 연결된 콘텐츠 또는 사용 가능한 목록을 사용하여 항목의 동적 목록에서 속성을 표시하고 캡처할 수 있습니다. 

자신의 견해를 서브클래스된 인-앱 메시지에 삽입할 수 있습니다. 이 예시는 `UIPickerView`을(를) 사용하여 `ABKModalInAppMessageViewController`의 기능을 확장하는 방법을 보여줍니다.

[ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift)에 방문하여 시작하십시오.

#### 대시보드 구성

대시보드에서 모달 인앱 메시지를 설정하려면 쉼표로 구분된 문자열로 형식화된 항목 목록을 제공해야 합니다. 우리의 예에서, 우리는 연결된 콘텐츠를 사용하여 팀 이름의 JSON 목록을 가져오고 적절하게 형식을 지정합니다.

![인앱 메시지 작성기는 인앱 메시지가 어떻게 보일지 미리보기를 보여주지만 대신 Braze에 제공한 항목 목록을 표시합니다. Braze UI는 커스텀 인앱 메시지 UI를 휴대폰으로 전송하지 않으면 표시하지 않으므로 미리보기는 메시지의 실제 모양을 나타내지 않습니다. 따라서 전송하기 전에 테스트하는 것을 권장합니다.][4]

키-값 쌍에서 `attribute_key`을(를) 제공하십시오. 이 키는 사용자가 선택한 값과 함께 고객 프로필에 커스텀 속성으로 저장됩니다. 귀하의 커스텀 보기 로직은 Braze로 전송된 사용자 속성을 처리해야 합니다.

`extras` 사전은 `ABKInAppMessage` 객체에서 (있는 경우) 올바른 보기를 표시하도록 신호하는 `view_type` 키를 쿼리할 수 있게 해줍니다. 인앱 메시지는 메시지별로 구성되므로 커스텀 및 기본값 모달 뷰가 조화를 이룰 수 있다는 점을 유의하는 것이 중요합니다.

![메시지 작성기에서 두 개의 키-값 쌍을 찾았습니다. 첫 번째 키-값 페어는 "attribute_key"가 "Favorite Team"으로 설정되어 있고, 두 번째는 "view_type"이 "picker"로 설정되어 있습니다.][5]{: style="max-width:65%;"}

{% tabs %}
{% tab 스위프트 %}
**UI 디스플레이 동작에 `view_type` 사용**<br>
귀하의 `view_type`가 원하는 하위 클래스 뷰 컨트롤러를 로드하도록 `extras` 사전을 쿼리하십시오.

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
{% tab 오브젝티브-C %}
**UI 디스플레이 동작에 `view_type` 사용**<br>
귀하의 `view_type`가 원하는 하위 클래스 뷰 컨트롤러를 로드하도록 `extras` 사전을 쿼리하십시오.

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
{% tab 스위프트 %}
**오버라이드하고 커스텀 뷰를 제공**<br>
`loadView()`을(를) 재정의하고 자신의 커스텀 뷰를 설정하여 필요에 맞게 조정하십시오.
```swift
override var nibname: String{
  return "ModalPickerViewController"
}

override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% tab 오브젝티브-C %}
**오버라이드하고 커스텀 뷰를 제공**<br>
`loadView()`을(를) 재정의하고 자신의 커스텀 뷰를 설정하여 필요에 맞게 조정하십시오.
```objc
- (void)loadView {
  NSString *nibName = @"ModalPickerViewController";
  [[NSBundle mainBundle] loadNibNamed:nibName owner:self options:nil];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab 스위프트 %}
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
{% tab 오브젝티브-C %}
**피커뷰의 형식 변수**<br>
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
{% tab 스위프트 %}
**커스텀 속성 할당**<br>
서브클래스를 사용하여 사용자가 제출을 누른 후 속성과 해당 선택된 값을 Braze에 전달합니다.
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab 오브젝티브-C %}
**커스텀 속성 할당**<br>
서브클래스를 사용하여 사용자가 제출을 누른 후 속성과 해당 선택된 값을 Braze에 전달합니다.
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
FaceTime을 통해 동영상을 공유하기 위해 우리의 커스텀 모달 인앱 메시지를 활용하는 데 관심이 있습니까? SharePlay 인앱 메시지 [구현 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/shareplay/)를 확인하세요.
{% endalert%}

### 커스텀 전체 인앱 메시지

![구성 옵션 목록을 표시하고 각 옵션 옆에 토글이 있는 인앱 메시지. 메시지 하단에 큰 파란색 제출 버튼이 있습니다.][6]{: style="float:right;max-width:23%;margin-left:15px;border:0;"}

커스텀 전체 인앱 메시지를 사용하여 상호작용하고 사용자 친화적인 프롬프트를 만들어 귀중한 고객 데이터를 수집하세요. 오른쪽 예시는 알림 환경설정을 포함한 인터랙티브 푸시 프라이머로 재구상된 커스텀 전체 인앱 메시지의 구현을 보여줍니다. 

[`FullListViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift)에 방문하여 시작하십시오.

#### 대시보드 구성

대시보드에서 커스텀 전체 인앱 메시지를 설정하려면 쉼표로 구분된 문자열로 형식화된 태그 목록을 제공해야 합니다. 

키-값 쌍에서 `attribute_key`을(를) 제공하십시오. 이 키는 사용자가 선택한 값과 함께 고객 프로필에 커스텀 속성으로 저장됩니다. 귀하의 커스텀 보기 로직은 Braze로 전송된 사용자 속성을 처리해야 합니다.

![메시지 작성기에서 세 개의 키-값 쌍을 찾았습니다. 첫 번째 키-값 페어 "attribute_key"는 "푸시 태그"로 설정되고, 두 번째 "subtitle_text"는 "알림을 활성화하면 또한..."로 설정되며, 세 번째 "view_type"은 "테이블 목록"으로 설정됩니다.][7]{: style="max-width:65%;"}

#### 인앱 메시지 터치를 가로채기
![설정 및 토글 행을 표시하는 Apple 기기. 커스텀 뷰는 버튼을 처리하며, 버튼 컨트롤 외부의 모든 터치는 인앱 메시지에 의해 처리되고 이를 닫습니다.][1]{: style="float:right;max-width:30%;margin-left:10px;border:0"}
인앱 메시지 터치를 가로채는 것은 커스텀 전체 인앱 메시지 버튼이 올바르게 작동하도록 하는 데 매우 중요합니다. 기본적으로, `ABKInAppMessageImmersive` 메시지에 탭 제스처 인식기를 추가하여 사용자가 버튼 없이 메시지를 닫을 수 있습니다. `UISwitch` 또는 버튼을 `UITableViewCell` 뷰 계층 구조에 추가하면 터치가 이제 커스텀 뷰에 의해 처리됩니다. iOS 6부터 버튼 및 기타 컨트롤이 제스처 인식기보다 우선하여 작동하므로, 우리의 커스텀 전체 인앱 메시지가 정상적으로 작동합니다. 

[1]: {% image_buster /assets/img/iam_implementation_guide.png %}
[2]: {% image_buster /assets/img/iam_implementation/slideup.png %}
[3]: {% image_buster /assets/img/iam_implementation/modal.png %}
[4]: {% image_buster /assets/img/iam_implementation/dashboard1.png %}
[5]: {% image_buster /assets/img/iam_implementation/dashboard2.png %}
[6]: {% image_buster /assets/img/iam_implementation/fullscreen.png %}
[7]: {% image_buster /assets/img/iam_implementation/dashboard3.png %}
[8]: {% image_buster /assets/img/iam_implementation/dashboard4.png %}
