---
nav_title: 피드
article_title: 콘텐츠 카드용 피드 사용자 지정
page_order: 3
description: "이 문서에서는 콘텐츠 카드 피드 사용자 지정 옵션을 다룹니다."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# 콘텐츠 카드용 피드 사용자 지정

> 콘텐츠 카드 피드는 모바일 또는 웹 애플리케이션에 있는 콘텐츠 카드의 시퀀스입니다. 이 문서에서는 피드를 새로 고치는 시기, 카드 순서, 여러 피드 관리, '빈 피드' 오류 메시지 등을 구성하는 방법을 다룹니다. 콘텐츠 카드 유형 전체 목록은 [콘텐츠 카드 정보를]({{site.baseurl}}/developer_guide/content_cards/) 참조하세요. 

## 피드 새로 고침

기본적으로 콘텐츠 카드 피드는 다음과 같은 경우에 자동으로 새로 고쳐집니다: 
1. 새 세션이 시작됩니다.
2. 피드를 열면 마지막 새로고침 이후 60초 이상이 경과한 경우. 이것은 기본 콘텐츠 카드 피드에만 적용되며 피드 열기당 한 번만 발생합니다.

특정 시간에 수동으로 새로 고치도록 SDK를 구성할 수도 있습니다.

{% alert tip %}
수동으로 새로 고치지 않고 최신 콘텐츠 카드를 동적으로 표시하려면 카드 생성 중에 **첫 번째 노출**을 선택합니다. 이러한 카드는 사용 가능한 상태가 되면 새로 고쳐집니다.
{% endalert %}

{% tabs local %}
{% tab Android %}

[`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html)를 호출하여 언제든지 Android SDK에서 Braze 콘텐츠 카드의 수동 새로 고침을 요청합니다. 

{% subtabs local %}
{% subtab Java %}

```java
Braze.getInstance(context).requestContentCardsRefresh();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh()
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

[`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class) 클래스에서 [`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:)) 메서드를 호출하여 언제든지 Swift SDK에서 Braze 콘텐츠 카드의 수동 새로 고침을 요청합니다.

{% subtabs local %}
{% subtab Swift %}

Swift에서 콘텐츠 카드는 선택적 완료 핸들러를 사용하거나 기본 Swift 동시성 API를 사용하여 비동기 반환을 통해 새로 고칠 수 있습니다.

### 완료 핸들러

```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
  // Implement completion handler
}
```

### 비동기/대기

```swift
let contentCards = await AppDelegate.braze?.contentCards.requestRefresh()
```
{% endsubtab %}
{% subtab Objective-C %}

```objc
[AppDelegate.braze.contentCards requestRefreshWithCompletion:^(NSArray<BRZContentCardRaw *> * contentCards, NSError * error) {
  // Implement completion handler
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

[`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)를 호출하여 언제든지 웹 SDK에서 Braze 콘텐츠 카드의 수동 새로 고침을 요청합니다. 

[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)를 호출하여 마지막 콘텐츠 카드 새로 고침에서 현재 사용 가능한 모든 카드를 가져올 수도 있습니다. 

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();    
}
```

{% endtab %}
{% endtabs %}


{% alert important %}
최대 5개의 통화를 연속으로 빠르게 걸 수 있습니다. 그 후에는 180초마다 하나의 새 통화를 사용할 수 있습니다. 시스템은 언제든지 사용할 수 있도록 최대 5개의 통화를 보관합니다.
{% endalert %}

## 표시되는 카드 순서 사용자 지정

콘텐츠 카드가 표시되는 순서를 변경할 수 있습니다. 이를 통해 시간에 민감한 프로모션과 같은 특정 유형의 콘텐츠에 우선순위를 지정하여 사용자 환경을 미세 조정할 수 있습니다.

{% tabs %}
{% tab Android 보기 시스템 %}

[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)는 [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)를 사용하여 콘텐츠 카드가 피드에 표시되기 전에 정렬 또는 수정을 처리합니다. 커스텀 업데이트 핸들러는 `ContentCardsFragment`에서 [`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html)를 통해 설정할 수 있습니다.

다음은 기본 `IContentCardsUpdateHandler`이며 사용자 지정의 시작점으로 사용할 수 있습니다.

{% subtabs local %}
{% subtab Java %}

```java
public class DefaultContentCardsUpdateHandler implements IContentCardsUpdateHandler {

  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  public static final Parcelable.Creator<DefaultContentCardsUpdateHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsUpdateHandler>() {
    public DefaultContentCardsUpdateHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsUpdateHandler();
    }

    public DefaultContentCardsUpdateHandler[] newArray(int size) {
      return new DefaultContentCardsUpdateHandler[size];
    }
  };

  @Override
  public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
    List<Card> sortedCards = event.getAllCards();
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    Collections.sort(sortedCards, new Comparator<Card>() {
      @Override
      public int compare(Card cardA, Card cardB) {
        // A displays above B
        if (cardA.getIsPinned() && !cardB.getIsPinned()) {
          return -1;
        }

        // B displays above A
        if (!cardA.getIsPinned() && cardB.getIsPinned()) {
          return 1;
        }

        // At this point, both A & B are pinned or both A & B are non-pinned
        // A displays above B since A is newer
        if (cardA.getUpdated() > cardB.getUpdated()) {
          return -1;
        }

        // B displays above A since A is newer
        if (cardA.getUpdated() < cardB.getUpdated()) {
          return 1;
        }

        // At this point, every sortable field matches so keep the natural ordering
        return 0;
      }
    });

    return sortedCards;
  }

  // Parcelable interface method
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // No state is kept in this class so the parcel is left unmodified
  }
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
class DefaultContentCardsUpdateHandler : IContentCardsUpdateHandler {
  override fun handleCardUpdate(event: ContentCardsUpdatedEvent): List<Card> {
    val sortedCards = event.allCards
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    sortedCards.sortWith(Comparator sort@{ cardA: Card, cardB: Card ->
      // A displays above B
      if (cardA.isPinned && !cardB.isPinned) {
        return@sort -1
      }

      // B displays above A
      if (!cardA.isPinned && cardB.isPinned) {
        return@sort 1
      }

      // At this point, both A & B are pinned or both A & B are non-pinned
      // A displays above B since A is newer
      if (cardA.updated > cardB.updated) {
        return@sort -1
      }

      // B displays above A since A is newer
      if (cardA.updated < cardB.updated) {
        return@sort 1
      }
      0
    })
    return sortedCards
  }

  // Parcelable interface method
  override fun describeContents(): Int {
    return 0
  }

  // Parcelable interface method
  override fun writeToParcel(dest: Parcel, flags: Int) {
    // No state is kept in this class so the parcel is left unmodified
  }

  companion object {
    // Interface that must be implemented and provided as a public CREATOR
    // field that generates instances of your Parcelable class from a Parcel.
    val CREATOR: Parcelable.Creator<DefaultContentCardsUpdateHandler?> = object : Parcelable.Creator<DefaultContentCardsUpdateHandler?> {
      override fun createFromParcel(`in`: Parcel): DefaultContentCardsUpdateHandler? {
        return DefaultContentCardsUpdateHandler()
      }

      override fun newArray(size: Int): Array<DefaultContentCardsUpdateHandler?> {
        return arrayOfNulls(size)
      }
    }
  }
}
```

{% endsubtab %}
{% endsubtabs %}

`ContentCardsFragment` 소스는 [GitHub에서](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt) 찾을 수 있습니다.

{% endtab %}
{% tab Jetpack Compose %}
Jetpack Compose에서 콘텐츠 카드를 필터링하고 정렬하려면 `cardUpdateHandler` 매개변수를 설정합니다. 예를 들어, 다음과 같습니다.

```kotlin
ContentCardsList(
    cardUpdateHandler = {
        it.sortedWith { cardA, cardB ->
            // A displays above B
            if (cardA.isPinned && !cardB.isPinned) {
                return@sortedWith -1
            }
            // B displays above A
            if (!cardA.isPinned && cardB.isPinned) {
                return@sortedWith 1
            }
            // At this point, both A & B are pinned or both A & B are non-pinned
            // A displays above B since A is newer
            if (cardA.updated > cardB.updated) {
                return@sortedWith -1
            }
            // B displays above A since A is newer
            if (cardA.updated < cardB.updated) {
                return@sortedWith 1
            }
            0
        }
    }
)
```
{% endtab %}
{% tab iOS %}

{% subtabs %}
{% subtab Swift %}

정적 [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) 변수를 직접 수정하여 카드 피드 순서를 사용자 지정합니다.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
    cards.sorted {
        if $0.pinned && !$1.pinned {
            return true
        } else if !$0.pinned && $1.pinned {
            return false
        } else {
            return $0.createdAt > $1.createdAt
        }
    }
}
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

`BrazeContentCardUI.ViewController.Attributes` 을 통한 사용자 지정은 Objective-C에서 사용할 수 없습니다. 

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

`showContentCards():`의 [`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) 매개변수를 사용하여 피드에서 콘텐츠 카드의 표시 순서를 사용자 지정합니다. 예를 들어, 다음과 같습니다.

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% endtabs %}

## "빈 피드" 메시지 사용자 지정하기

사용자가 콘텐츠 카드를 사용할 자격이 없는 경우 SDK는 다음과 같은 '빈 피드' 오류 메시지를 표시합니다. "업데이트가 없습니다. 나중에 다시 확인해 주세요." 이 '빈 피드' 오류 메시지는 다음과 유사하게 사용자 지정할 수 있습니다:

!["이것은 사용자 지정 빈 상태 메시지입니다."라는 빈 피드 오류 메시지]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab Android 보기 시스템 %}

[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)에서 사용자가 콘텐츠 카드를 받을 자격이 없다고 판단하면 빈 피드 오류 메시지를 표시합니다.

특수 어댑터인 [`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt)가 표준 [`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt)를 대체하여 이 오류 메시지를 표시합니다. 커스텀 메시지 자체를 설정하려면 문자열 리소스 `com_braze_feed_empty`를 재정의합니다.

이 메시지를 표시하는 데 사용되는 스타일은 [`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530)에서 찾을 수 있으며 다음 코드 스니펫에 재현되어 있습니다.

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  <item name="android:lineSpacingExtra">1.5dp</item>
  <item name="android:text">@string/com_braze_feed_empty</item>
  <item name="android:textColor">@color/com_braze_content_card_empty_text_color</item>
  <item name="android:textSize">18.0sp</item>
  <item name="android:gravity">center</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent</item>
</style>
```

콘텐츠 카드 스타일 요소 사용자 지정에 대한 자세한 내용은 [스타일 사용자 지정]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)을 참조하세요.
{% endtab %}
{% tab Jetpack Compose %}
Jetpack Compose로 '빈 피드' 오류 메시지를 사용자 지정하려면 `emptyString`을 `ContentCardsList`에 전달하면 됩니다. `emptyTextStyle`을 `ContentCardListStyling`으로 전달하여 이 메시지를 추가로 사용자 지정할 수도 있습니다.

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

대신 표시하고 싶은 Composable이 있는 경우 `emptyComposable`을 `ContentCardsList`에 전달할 수 있습니다. `emptyComposable` 을 지정하면 `emptyString` 이 사용되지 않습니다.

```kotlin
ContentCardsList(
    emptyComposable = {
        Image(
            painter = painterResource(id = R.drawable.noMessages),
            contentDescription = "No messages"
        )
    }
)
```
{% endtab %}
{% tab iOS %}
{% subtabs local %}
{% subtab Swift %}

관련 [`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults)를 설정하여 보기 컨트롤러 빈 상태를 사용자 지정합니다.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

앱의 [`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj) 파일에서 현지화 가능한 콘텐츠 카드 문자열을 재정의하여 빈 콘텐츠 카드 피드에 자동으로 표시되는 언어를 변경합니다.

{% alert note %}
이 메시지를 다른 로캘 언어로 업데이트하려면 [리소스 폴더 구조](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization)에서 `ContentCardsLocalizable.strings` 문자열을 사용하여 해당 언어를 찾습니다.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

웹 SDK는 프로그래밍 방식으로 '빈 피드' 언어를 대체하는 기능을 지원하지 않습니다. 피드가 표시될 때마다 교체하도록 선택할 수 있지만 피드를 새로 고치는 데 다소 시간이 걸리고 빈 피드 텍스트가 즉시 표시되지 않을 수 있으므로 권장하지 않습니다. 

{% endtab %}
{% endtabs %}

## 여러 피드

특정 카드만 표시하도록 앱에서 콘텐츠 카드를 필터링할 수 있으므로 다양한 사용 사례에 맞게 여러 콘텐츠 카드 피드를 사용할 수 있습니다. 예를 들어 트랜잭션 피드와 마케팅 피드를 모두 유지할 수 있습니다. 이를 위해 Braze 대시보드에서 키-값 페어를 설정하여 다양한 카테고리의 콘텐츠 카드를 생성합니다. 그런 다음 앱이나 사이트에서 이러한 유형의 콘텐츠 카드를 다르게 처리하는 피드를 만들어 일부 유형은 필터링하고 다른 유형은 표시할 수 있습니다.

### 1단계: 카드에 키-값 쌍 설정

콘텐츠 카드 캠페인을 생성할 때 각 카드에서 [키-값 페어 데이터]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior/)를 설정합니다. 이 키-값 쌍을 사용하여 카드를 분류합니다. 키-값 쌍은 카드의 데이터 모델에 있는 `extras` 속성에 저장됩니다.

이 예제에서는 `feed_type` 키와 함께 키-값 페어를 설정하여 카드를 표시해야 하는 콘텐츠 카드 피드를 지정합니다. 값은 `home_screen` 또는 `marketing`과 같이 커스텀 피드에 따라 달라집니다.

### 2단계: 콘텐츠 카드 필터링

키-값 쌍이 할당되면 표시하려는 카드를 표시하고 다른 유형의 카드를 필터링하는 로직이 포함된 피드를 만듭니다. 이 예제에서는 키-값 페어가 `feed_type: "Transactional"`으로 일치하는 카드만 표시합니다.

{% tabs %}
{% tab Android 보기 시스템 %}

콘텐츠 카드 필터링은 [`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html)를 통해 대시보드에 설정된 키-값 페어를 읽고 커스텀 업데이트 핸들러를 사용하여 필터링하거나 원하는 다른 로직을 수행하면 됩니다.

정교하게 표시하기 위해 콘텐츠 카드 피드는 [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)에 표시됩니다. 기본 `IContentCardsUpdateHandler`는 Braze SDK에서 [`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html)를 사용하여 표시할 카드 목록을 반환하지만, 카드 정렬만 하고 자체적으로 제거나 필터링은 수행하지 않습니다.

`ContentCardsFragment`를 필터링하려면 커스텀 [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)를 생성합니다. 앞서 설정한 `feed_type`의 원하는 값과 일치하지 않는 카드를 목록에서 모두 제거하도록 이 `IContentCardsUpdateHandler`를 수정합니다. 예를 들어, 다음과 같습니다.

{% subtabs local %}
{% subtab Java %}

```java
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
  return new IContentCardsUpdateHandler() {
    @Override
    public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
      // Use the default card update handler for a first
      // pass at sorting the cards. This is not required
      // but is done for convenience.
      final List<Card> cards = new DefaultContentCardsUpdateHandler().handleCardUpdate(event);

      final Iterator<Card> cardIterator = cards.iterator();
      while (cardIterator.hasNext()) {
        final Card card = cardIterator.next();

        // Make sure the card has our custom KVP
        // from the dashboard with the key "feed_type"
        if (card.getExtras().containsKey("feed_type")) {
          final String feedType = card.getExtras().get("feed_type");
          if (!desiredFeedType.equals(feedType)) {
            // The card has a feed type, but it doesn't match
            // our desired feed type, remove it.
            cardIterator.remove();
          }
        } else {
          // The card doesn't have a feed
          // type at all, remove it
          cardIterator.remove();
        }
      }

      // At this point, all of the cards in this list have
      // a feed type that explicitly matches the value we put
      // in the dashboard.
      return cards;
    }
  };
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
  return IContentCardsUpdateHandler { event ->
    // Use the default card update handler for a first
    // pass at sorting the cards. This is not required
    // but is done for convenience.
    val cards = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

    val cardIterator = cards.iterator()
    while (cardIterator.hasNext()) {
      val card = cardIterator.next()

      // Make sure the card has our custom KVP
      // from the dashboard with the key "feed_type"
      if (card.extras.containsKey("feed_type")) {
        val feedType = card.extras["feed_type"]
        if (desiredFeedType != feedType) {
          // The card has a feed type, but it doesn't match
          // our desired feed type, remove it.
          cardIterator.remove()
        }
      } else {
        // The card doesn't have a feed
        // type at all, remove it
        cardIterator.remove()
      }
    }

    // At this point, all of the cards in this list have
    // a feed type that explicitly matches the value we put
    // in the dashboard.
    cards
  }
}
```

{% endsubtab %}
{% endsubtabs %}

`IContentCardsUpdateHandler` 를 만든 후에는 이를 사용하는 `ContentCardsFragment` 을 만듭니다. 이 커스ㅁ 피드는 다른 `ContentCardsFragment`와 마찬가지로 사용할 수 있습니다. 앱의 다른 부분에서 대시보드에 제공된 키에 따라 다른 콘텐츠 카드 피드를 표시합니다. 각 `ContentCardsFragment` 피드에는 각 조각의 커스텀 `IContentCardsUpdateHandler` 덕분에 고유한 카드 집합이 표시됩니다. 

예를 들어, 다음과 같습니다.

{% subtabs local %}
{% subtab Java %}

```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Jetpack Compose %}
이 피드에 표시되는 콘텐츠 카드를 필터링하려면 `cardUpdateHandler`를 사용합니다. 예를 들어, 다음과 같습니다.

```kotlin
ContentCardsList(
     cardUpdateHandler = {
         it.filter { card ->
             card.extras["feed_type"] == "Transactional"
         }
     }
 )
 ```
{% endtab %}
{% tab iOS %}

다음 예제에서는 `Transactional` 유형 카드에 대한 콘텐츠 카드 피드를 보여줍니다.

{% subtabs %}
{% subtab Swift %}

```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

더 나아가, `Attributes` 구조에서 `transform` 속성정보를 설정하여 보기 컨트롤러에 표시되는 카드를 필터링하여 기준에 따라 필터링된 카드만 표시할 수 있습니다.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
    [transactionalCards addObject:card];
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

다음 예제에서는 `Transactional` 유형 카드에 대한 콘텐츠 카드 피드를 보여줍니다.

```javascript

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
  braze.showContentCards(null, function(cards) {
    return cards.filter((card) => card.extras["feed_type"] === feed_type);
  });
}
```

그런 다음 사용자 지정 피드에 대한 토글을 설정할 수 있습니다:

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional"); 
};
```

자세한 내용은 [SDK 메서드 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)를 참조하세요.

{% endtab %}
{% endtabs %}


