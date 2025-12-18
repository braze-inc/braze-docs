> 콘텐츠 카드에 대한 커스텀 UI를 구축할 때는 기본값 카드 모델에 대해서만 자동으로 처리되므로 노출 횟수, 클릭 수, 카드 방출과 같은 분석을 수동으로 기록해야 합니다. 이러한 이벤트 로깅은 콘텐츠 카드 통합의 표준 부분이며 정확한 캠페인 보고 및 청구를 위해 필수적입니다. 이렇게 하려면 고객 데이터 모델의 데이터로 커스텀 UI를 채운 다음 이벤트를 수동으로 로깅하세요. 분석을 기록하는 방법을 이해하면 Braze 고객이 [커스텀 콘텐츠 카드를 생성]({{site.baseurl}}/developer_guide/content_cards/creating_cards/)하는 일반적인 방법을 이해할 수 있습니다. 

## 카드 업데이트를 기다리는 중

커스텀 콘텐츠 카드를 구현할 때 콘텐츠 카드 오브젝트를 구문 분석하고 `title`, `cardDescription`, `imageUrl`와 같은 페이로드 데이터를 추출할 수 있습니다. 그런 다음, 결과 모델 데이터를 사용하여 커스텀 UI를 채울 수 있습니다. 

콘텐츠 카드 데이터 모델을 얻으려면 콘텐츠 카드 업데이트에 가입합니다. 특히 주의해야 할 두 가지 속성이 있습니다:

* **`id`**: 콘텐츠 카드 ID 문자열을 나타냅니다. 이것은 커스텀 콘텐츠 카드에서 분석을 기록하는 데 사용되는 고유 식별자입니다.
* **`extras`**: Braze 대시보드의 모든 키-값 쌍을 포함합니다. 

커스텀 콘텐츠 카드에 대한 구문 분석에서 `id` 및 `extras` 외의 모든 속성정보는 선택 사항입니다. 자세한 데이터 모델 정보는 각 플랫폼의 통합 기사를 참조하십시오: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [웹]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### 1단계: 비공개 가입자 변수를 생성합니다

카드 업데이트에 가입하려면 먼저 가입자를 보유할 수 있도록 커스텀 클래스에 개인 변수를 선언합니다.

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### 2단계: 업데이트 가입

다음으로, Braze의 콘텐츠 카드 업데이트에 가입하려면 다음 코드를 추가합니다. 일반적으로 커스텀 콘텐츠 카드 활동의 `Activity.onCreate()` 내부에 있습니다.

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

### 3단계: 구독취소

커스텀 활동이 보기 밖으로 이동하면 가입을 취소하는 것이 좋습니다. 활동의 `onDestroy()` 생명 주기 메서드에 다음 코드를 추가하십시오:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### 1단계: 비공개 가입자 변수를 생성합니다

카드 업데이트에 가입하려면 먼저 가입자를 보유할 수 있도록 커스텀 클래스에 개인 변수를 선언합니다.

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### 2단계: 업데이트 가입

다음으로, Braze의 콘텐츠 카드 업데이트에 가입하려면 다음 코드를 추가합니다. 일반적으로 커스텀 콘텐츠 카드 활동의 `Activity.onCreate()` 내부에 있습니다.

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh()
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### 3단계: 구독취소

커스텀 활동이 보기 밖으로 이동하면 가입을 취소하는 것이 좋습니다. 활동의 `onDestroy()` 생명 주기 메서드에 다음 코드를 추가하십시오:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

콘텐츠 카드 데이터 모델에 액세스하려면 `braze` 인스턴스에서 [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards)를 호출합니다

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

또한 콘텐츠 카드의 변경 사항을 관찰하기 위해 가입을 유지할 수도 있습니다. 두 가지 방법 중 하나로 할 수 있습니다: 
1. 취소 가능 유지 또는 
2. `AsyncStream` 유지.

### 취소 가능 

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

또한 콘텐츠 카드 가입을 유지하려면 [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:))를 호출할 수 있습니다.

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

콜백 함수를 등록하여 카드를 새로 고칠 때 업데이트에 가입합니다.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
콘텐츠 카드는 `openSession()` 전에 가입 요청을 호출한 경우에만 세션을 시작할 때 새로 고쳐집니다. 항상 [피드를 수동으로 새로고침]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/)할 수도 있습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

## 로그 이벤트

가치 있는 측정기준(예: 노출 수, 클릭 수, 해제 수)을 기록하는 것은 빠르고 간단합니다. 이러한 분석을 수동으로 처리하도록 커스텀 클릭 리스너를 설정합니다.

{% tabs %}
{% tab android %}

는 [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) 는 콘텐츠 카드 오브젝트 배열 목록과 같은 Braze 소프트웨어 개발 키트 종속성을 참조하여 [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) 를 사용하여 Braze 로깅 메서드를 호출할 수 있습니다. `ContentCardable` 기본 클래스를 사용하여 데이터를 쉽게 참조하고 `BrazeManager`에 해당 데이터를 제공합니다. 

카드에 대한 노출 횟수 또는 클릭을 기록하려면 각각 [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) 또는 [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html)을 호출하세요. 

특정 카드에 대해 [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html)를 사용하여 Braze에 콘텐츠 카드를 '해제됨'으로 설정하거나 수동으로 기록할 수 있습니다. 카드가 이미 해제됨 상태로 표시된 경우 다시 해제됨 상태로 표시할 수 없습니다.

커스텀 클릭 리스너를 만들려면, 클릭 리스너를 구현하는 클래스를 만들고 [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) 를 구현하는 클래스를 생성하고 [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). 사용자가 콘텐츠 카드를 클릭할 때 호출되는 [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html) 메서드를 구현합니다. 그런 다음, Braze에 콘텐츠 카드 클릭 리스너를 사용하도록 지시합니다. 

{% subtabs local %}
{% subtab Java %}

예를 들어, 다음과 같습니다.

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

예를 들어, 다음과 같습니다.

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
커스텀 UI에서 제어 배리언트 콘텐츠 카드를 처리하려면 [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) 오브젝트를 전달한 다음, 다른 콘텐츠 카드 유형에서와 마찬가지로 `logImpression` 메서드를 호출합니다. 오브젝트는 사용자가 제어 카드를 보았을 때를 분석 팀에 알릴 제어 노출 횟수를 암시적으로 기록합니다.{% endalert %}

{% endtab %}
{% tab swift %}

[`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) 프로토콜을 구현하고 위임 객체를 `BrazeContentCardUI.ViewController`의 `delegate` 속성으로 설정하십시오. 이 위임은 기록할 커스텀 오브젝트의 데이터를 Braze로 다시 전달하여 처리합니다. 예를 들어, [콘텐츠 카드 UI 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/)을 참조하세요.

{% subtabs local %}
{% subtab Swift %}

```swift
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
커스텀 UI에서 제어 배리언트 콘텐츠 카드를 처리하려면 [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) 오브젝트를 전달한 다음, 다른 콘텐츠 카드 유형에서와 마찬가지로 `logImpression` 메서드를 호출합니다. 오브젝트는 사용자가 제어 카드를 보았을 때를 분석 팀에 알릴 제어 노출 횟수를 암시적으로 기록합니다.
{% endalert %}
{% endtab %}

{% tab 웹 %}

사용자가 [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)를 사용하여 카드를 볼 때 노출 횟수 이벤트를 기록합니다.

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

사용자가 [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)을 사용하여 카드와 상호 작용할 때 카드 클릭 이벤트를 기록합니다.

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% endtabs %}
