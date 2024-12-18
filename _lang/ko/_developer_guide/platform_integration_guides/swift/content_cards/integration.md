---
nav_title: 통합
article_title: iOS용 콘텐츠 카드 통합
platform: Swift
page_order: 0
description: "이 문서에서는 Swift SDK에서 사용할 수 있는 통합 단계, 데이터 모델 및 카드별 속성정보를 다룹니다."
channel:
  - content cards

---

# 콘텐츠 카드 통합

> 이 참조 문서에서는 Swift 애플리케이션에 사용할 수 있는 콘텐츠 카드 통합, 여러 데이터 모델 및 카드별 속성정보를 다룹니다. 준비가 되면 구현 및 사용자 정의를 시작하려면 [콘텐츠 카드 사용자 정의 가이드]({{site.baseurl}}/developer_guide/customization_guides/content_cards)를 참조하세요.

## 통합 정보

기본값 콘텐츠 카드 UI는 Braze SDK의 `BrazeUI` 라이브러리에서 통합할 수 있습니다. `braze` 인스턴스를 사용하여 콘텐츠 카드 뷰 컨트롤러를 만듭니다. 콘텐츠 카드 UI 수명주기를 가로채고 이에 대응하려면 [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate)를 `BrazeContentCardUI.ViewController`의 위임으로 구현합니다.

{% alert note %}
iOS 뷰 컨트롤러 옵션에 대한 자세한 내용은 [Apple 개발자 설명서](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers)를 참조하십시오.
{% endalert %}

Swift SDK의 `BrazeUI` 라이브러리는 두 가지 기본 보기 컨트롤러 컨텍스트(탐색 및 Modal)를 제공합니다. 즉, 앱 또는 사이트에 몇 줄의 코드를 추가하여 이러한 컨텍스트에서 콘텐츠 카드를 통합할 수 있습니다. 두 가지 보기 모두 [사용자 정의 가이드]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios)에 설명된 대로 사용자 정의 및 스타일링 옵션을 제공합니다. 또한 표준 Braze 대신 커스텀 콘텐츠 카드 보기 컨트롤러를 만들어 더 많은 커스터마이제이션 옵션을 사용할 수 있습니다. 예시는 [콘텐츠 카드 UI 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/)을 참조하십시오.

{% alert important %}
커스텀 UI에서 제어 배리언트 콘텐츠 카드를 처리하려면 [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) 오브젝트를 전달한 다음, 다른 콘텐츠 카드 유형에서와 마찬가지로 `logImpression` 메서드를 호출합니다. 오브젝트는 사용자가 제어 카드를 보았을 때를 분석 팀에 알릴 제어 노출 횟수를 암시적으로 기록합니다.
{% endalert %}

## 탐색 컨텍스트

탐색 컨트롤러는 탐색 인터페이스에서 하나 이상의 하위 보기 컨트롤러를 관리하는 보기 컨트롤러입니다. 다음은 `BrazeContentCardUI.ViewController` 인스턴스를 내비게이션 컨트롤러에 푸시하는 예입니다:

{% tabs %}
{% tab swift %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab 목표-C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

## Modal 컨텍스트

Modal 프레젠테이션을 사용하여 앱의 워크플로에서 중요한 정보를 사용자에게 요청하는 것과 같은 일시적인 중단을 생성합니다. 이 모델 뷰에는 상단에 탐색 표시 줄이 있고 표시 줄 측면에 **완료** 버튼이 있습니다. 다음은 `BrazeContentCard.ViewController` 인스턴스를 모달 컨트롤러에 푸시하는 예입니다:

{% tabs %}
{% tab swift %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab 목표-C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

예를 들어 `BrazeUI` 뷰 컨트롤러의 사용법은 해당 콘텐츠 카드 UI 샘플을 [Examples 앱](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)에서 확인하세요.

## 콘텐츠 카드 데이터 모델

콘텐츠 카드 데이터 모델은 iOS Swift SDK의 `BrazeKit` 모듈에서 사용할 수 있습니다.

Braze는 다섯 가지 콘텐츠 카드 유형(자막 이미지, 클래식, 클래식 이미지, 제어)을 제공합니다. 각 유형은 `Braze.ContentCard` 유형의 구현입니다. `BrazeKit`는 Objective-C 호환성을 위해 대체 [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) 클래스를 제공합니다.

콘텐츠 카드 속성정보의 전체 목록과 콘텐츠 카드 사용에 대한 자세한 내용은 [`ContentCard` 클래스 설명서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard)를 참조하세요.

콘텐츠 카드 데이터 모델에 액세스하려면 `braze` 인스턴스에서 `contentCards.cards`를 호출합니다 카드 데이터 구독에 대한 자세한 내용은 [로그 분석]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics)을 참조하십시오.

## 카드 방법

각 카드는 카드 상태를 관리하기 위한 다양한 메서드를 포함하는 `Context` 객체로 초기화됩니다. 카드 오브젝트의 해당 상태 속성정보를 수정하려는 경우 이러한 메서드를 호출합니다.

| 방법                               | 설명                                                                                                                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()`      | 콘텐츠 카드 노출 횟수 이벤트를 기록합니다.                                                                                                   |
| `card.context?.logClick()`           | 콘텐츠 카드 클릭 이벤트를 기록합니다.                                                                                                        |
| `card.context?.processClickAction()` | 주어진 [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction) 입력을 처리합니다. |
| `card.context?.logDismissed()`       | 콘텐츠 카드 해제 이벤트를 기록합니다.                                                                                                    |
| `card.context?.logError()`           | 콘텐츠 카드와 관련된 오류를 기록하십시오.                                                                                                |
| `card.context?.loadImage()`          | 주어진 콘텐츠 카드 이미지를 URL에서 로드합니다. 이 메서드는 콘텐츠 카드에 이미지가 없을 때 nil일 수 있습니다.                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

자세한 내용은 [`Context` 클래스 설명서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)를 참조하십시오.

{% alert important %}
Swift SDK는 기본적으로 애니메이션 GIF 지원을 제공하지 않습니다. 지원은 `GIFViewProvider`의 인스턴스에서 서드파티 또는 자체 보기를 래핑하여 추가할 수 있습니다.

GIF 지원에 대한 자세한 내용은 이 [튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)을 참조하세요.
{% endalert %}
