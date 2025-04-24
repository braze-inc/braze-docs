---
nav_title: フィードのカスタマイズ
article_title: デフォルトのコンテンツカードフィードのカスタマイズ
page_order: 3
description: "この記事では、コンテンツカードフィードのカスタマイズオプションについて説明します。"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# デフォルトのコンテンツカードフィードのカスタマイズ

> コンテンツカードフィードは、モバイルまたは Web アプリケーションの一連のコンテンツカードです。この記事では、フィードの更新時の設定、カードの順序、複数フィードの管理、「空のフィード」エラーメッセージについて説明します。コンテンツカードで使用するカスタマイズオプションのタイプの基本的な概要については、[カスタマイズの概要]({{site.baseurl}}/developer_guide/customization_guides/customization_overview)を参照してください。 

## フィードの更新

デフォルトでは、コンテンツカードフィードは次の場合に自動的に更新されます。 
1. 新しいセッションが開始される場合
2. フィードが開かれ、最後の更新から 60  秒以上経過した場合

SDK は、特定の時間に手動で更新するように設定することもできます。

{% alert tip %}
手動で更新せずに最新のコンテンツカードを動的に表示するには、カード作成時に **[最初のインプレッション発生時]** を選択します。これらのカードは、使用可能になると更新されます。
{% endalert %}

{% tabs local %}
{% tab Android %}

Android SDK から[`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html)を呼び出すことで、いつでも手動で Braze コンテンツカードの更新を要求します。 

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

[`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class)クラスで[`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:))メソッドを呼び出すことで、いつでも Swift SDK から Braze コンテンツカードの手動更新を要求します。

{% subtabs local %}
{% subtab Swift %}

Swift では、オプションの補完ハンドラまたはネイティブの Swift concurrency API を使用した非同期リターンを使用して、コンテンツカードを更新できます。

### 完了ハンドラ

```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
  // Implement completion handler
}
```

### 非同期/待機

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
{% tab Web %}

Web SDK から[`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)を呼び出して、いつでも手動で Braze コンテンツカードのリフレッシュを要求します。 

また、[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)を呼び出して、最新のコンテンツカード更新から現在利用可能なすべてのカードを取得することもできます。 

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();    
}
```

{% endtab %}
{% endtabs %}


{% alert important %}
最大5回まで連続して呼び出しを行うことができます。その後は、180秒ごとに1つの新しい呼び出しが可能になります。システムは、いつでも使用できるように最大5つの呼び出しを保持します。
{% endalert %}

## 表示されるカードの順序をカスタマイズする

コンテンツカードの表示順序を変更できます。これにより、時間的制約のあるプロモーションなど、特定のタイプのコンテンツに優先順位を付けることで、ユーザーエクスペリエンスを微調整できます。

{% tabs %}
{% tab Android View System %}

[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)は、[`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)に依存して、フィードに表示される前にコンテンツカードのソートまたは変更を処理します。カスタム更新ハンドラは、`ContentCardsFragment`の[`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html)で設定できます。

以下はデフォルトの`IContentCardsUpdateHandler`であり、カスタマイズの開始点として使用できます。

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

`ContentCardsFragment`ソースは [GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt) にあります。

{% endtab %}
{% tab Jetpack Compose %}
Jetpack Compose でコンテンツカードをフィルタリングおよびソートするには、`cardUpdateHandler`パラメータを設定します。以下に例を示します。

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

静的な[`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults)変数を直接変更して、カードフィードの順序をカスタマイズします。

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

`BrazeContentCardUI.ViewController.Attributes` によるカスタマイズは Objective-C では使用できません。 

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

`showContentCards():`の[`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)パラメーターを使用して、フィードのコンテンツカードの表示順序をカスタマイズします。以下に例を示します。

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% endtabs %}

## 「空のフィード」メッセージのカスタマイズ

ユーザーがコンテンツカードに適格でない場合、SDK は次のような「空のフィード」エラーメッセージを表示します。「更新はありません。後で再度確認してください。」この「空のフィード」エラーメッセージは、次のようにカスタマイズできます。

![これはカスタムの空状態メッセージです」と表示される空フィードのエラーメッセージ]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab Android View System %}

[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)によって、ユーザがコンテンツカードに対応していないと判断された場合は、空のフィードエラーメッセージが表示されます。

特殊なアダプタ[`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt)は、標準の[`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt)を置き換えてこのエラーメッセージを表示します。カスタムメッセージ自体を設定するには、文字列リソース`com_braze_feed_empty`を上書きします。

このメッセージを表示するために使用されるスタイルは、[`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530)で見つけることができ、次のコードスニペットで再現されます。

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

コンテンツカードスタイル要素のカスタマイズの詳細については、[スタイルのカスタマイズ]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles)を参照してください。
{% endtab %}
{% tab Jetpack Compose %}
Jetpack Compose で「空のフィード」エラーメッセージをカスタマイズするには、`emptyString`を`ContentCardsList`に渡します。`emptyTextStyle`を`ContentCardListStyling`に渡して、このメッセージをさらにカスタマイズすることもできます。

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

代わりに表示するコンポーザブルがある場合は、`emptyComposable`を`ContentCardsList`に渡します。`emptyComposable`を指定した場合、`emptyString`は使用されません。

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

関連する[`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults)を設定して、ビューコントローラーの空の状態をカスタマイズします。

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

空のコンテンツカードフィードに自動的に表示される言語を変更するには、アプリの[`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj)ファイルでローカライズ可能なコンテンツカード文字列を再定義します。

{% alert note %}
別のロケール言語でこのメッセージを更新する場合は、[リソースフォルダ構造](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization)で対応する言語を文字列`ContentCardsLocalizable.strings`で検索します。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Web SDK では、「空のフィード」の言語をプログラムで置き換えることはできません。フィードが表示されるたびに置き換えることを選択できますが、フィードが更新され、空のフィードテキストがすぐに表示されないため、これはお勧めしません。 

{% endtab %}
{% endtabs %}

## 複数のフィード

コンテンツカードは、特定のカードのみが表示されるようにアプリでフィルタリングできます。これにより、さまざまなユースケースで複数のコンテンツカードフィードを使用できます。たとえば、トランザクションフィードとマーケティングフィードの両方を維持できます。これを行うには、Braze ダッシュボードでキーと値のペアを設定して、コンテンツカードのさまざまなカテゴリーを作成します。次に、これらのタイプのコンテンツカードを異なる方法で処理し、一部のタイプをフィルタリングして他のタイプを表示するフィードをアプリまたはサイトに作成します。

### ステップ1:カードにキーと値のペアを設定する

コンテンツカードキャンペーンを作成する場合は、各カードで[キーと値のペアデータ]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/)を設定します。このキーと値のペアを使用して、カードを分類します。キーと値のペアは、カードのデータモデルの`extras`プロパティに保存されます。

この例では、カードが表示されるコンテンツカードフィードを指定するキー`feed_type`を使用してキーと値のペアを設定します。この値は、`home_screen`や`marketing`など、カスタムフィードの値になります。

### ステップ 2:コンテンツカードのフィルタリング

キーと値のペアが割り当てられたら、他のタイプのカードを表示およびフィルタリングするカードを表示するロジックを含むフィードを作成します。この例では、`feed_type: "Transactional"`のキーと値のペアが一致するカードのみを表示します。

{% tabs %}
{% tab Android View System %}

コンテンツカードのフィルタリングは、[`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html)を介してダッシュボードに設定されたキーと値のペアを読み取り、カスタム更新ハンドラを使用してフィルタリング (または他の必要なロジックを実行) することで実現できます。

詳細に説明すると、コンテンツカードフィードが[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)に表示されます。デフォルトの`IContentCardsUpdateHandler`は、Braze SDK から[`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html)を受け取り、表示するカードのリストを返しますが、カードの並べ替えのみを行い、それ自体は削除やフィルタリングを実行しません。

`ContentCardsFragment`でフィルタリングできるようにするには、カスタムの[`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)を作成します。この`IContentCardsUpdateHandler`を変更して、前に設定した`feed_type`の目的の値と一致しないカードをリストから削除します。以下に例を示します。

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

`IContentCardsUpdateHandler`を作成したら、それを使用する`ContentCardsFragment`を作成します。このカスタムフィードは、他の`ContentCardsFragment`と同様に使用できます。アプリのさまざまな部分で、ダッシュボードに用意されているキーに基づいて、さまざまなコンテンツカードフィードを表示します。各`ContentCardsFragment`フィードには、各フラグメントのカスタム`IContentCardsUpdateHandler`のおかげで一意のカードセットが表示されます。 

以下に例を示します。

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
このフィードに表示されるコンテンツカードをフィルタリングするには、`cardUpdateHandler`を使用します。以下に例を示します。

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

次の例では、`Transactional`タイプカードのコンテンツカードフィードを示します。

{% subtabs %}
{% subtab Swift %}

```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

さらに一歩進むために、ビューコントローラーに表示されるカードは、`transform`プロパティを`Attributes`構造体に設定して、条件でフィルタリングされたカードのみを表示することでフィルタリングできます。

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
{% tab Web %}

次の例では、`Transactional`タイプカードのコンテンツカードフィードを示します。

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

次に、カスタムフィードのトグルを設定できます。

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional"); 
};
```

詳細については、[SDK メソッドドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)を参照してください。

{% endtab %}
{% endtabs %}


