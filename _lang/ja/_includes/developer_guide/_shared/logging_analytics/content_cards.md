> コンテンツカードのカスタムUIを構築する場合、インプレッション、クリック、棄却などの分析を手動で記録する必要がある。これらのイベントのログは、コンテンツカード統合の標準的な部分であり、正確なキャンペーンレポートと課金に不可欠である。これを行うには、カスタムUIにBrazeデータモデルからのデータを入力し、手動でイベントを記録する。分析の記録方法を理解したら、Braze の顧客が[カスタムコンテンツカードを作成する]({{site.baseurl}}/developer_guide/content_cards/creating_cards/)一般的な方法がわかります。 

## カード更新のリスニング

カスタムコンテンツカードを実装する場合、コンテンツカードオブジェクトを解析して、`title`、`cardDescription`、`imageUrl`などのペイロードデータを抽出できます。その後、生成されたモデルデータを使用してカスタム UI を作成できます。 

コンテンツカードデータモデルを入手するには、コンテンツカードの更新を購読します。特に注意すべきプロパティが2つあります。

* **`id`**:コンテンツカード ID の文字列を表します。これは、カスタムコンテンツカードの分析を記録するために使用される一意の識別子です。
* **`extras`**:Braze ダッシュボードのすべてのキーと値のペアが含まれます。 

カスタムコンテンツカードでは`id`および`extras`以外のすべてのプロパティの解析は任意です。データモデルの詳細については、[Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android)、[iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift)、[Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web) の各プラットフォームの統合記事を参照してください。


{% tabs %}
{% tab web %}

カードが更新されたときに更新を購読するコールバック関数を登録します。

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
コンテンツカードは、`openSession()`の前にサブスクライブリクエストが呼び出された場合にのみ、セッション開始時に更新されます。[フィードを手動で更新]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/)することもいつでも選択できます。
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### ステップ1:プライベートサブスクライバー変数を作成する

カード更新を購読するには、まずカスタムクラスでサブスクライバーを保持するプライベート変数を宣言します。

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### ステップ2:更新を購読する

次に、通常はカスタムコンテンツカードアクティビティの`Activity.onCreate()`内で、以下のコードを追加して、Braze のコンテンツカードの更新を購読します。

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

### ステップ3:購読解除

また、カスタムアクティビティが表示されなくなったら、購読を解除することをおすすめします。アクティビティの`onDestroy()`ライフサイクルメソッドに次のコードを追加します。

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### ステップ1:プライベートサブスクライバー変数を作成する

カード更新を購読するには、まずカスタムクラスでサブスクライバーを保持するプライベート変数を宣言します。

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### ステップ2:更新を購読する

次に、通常はカスタムコンテンツカードアクティビティの`Activity.onCreate()`内で、以下のコードを追加して、Braze のコンテンツカードの更新を購読します。

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

### ステップ3:購読解除

また、カスタムアクティビティが表示されなくなったら、購読を解除することをおすすめします。アクティビティの`onDestroy()`ライフサイクルメソッドに次のコードを追加します。

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

コンテンツカードデータモデルにアクセスするには、`braze`インスタンスの[`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards)を呼び出します。

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

さらに、購読を維持して、コンテンツカードの変更を観察することもできます。これには次の2つの方法があります。 
1. キャンセル可能な状態を維持する。または、 
2. `AsyncStream`を維持する。

### キャンセル可能 

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

さらに、コンテンツカードの購読を維持する場合は、[`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:))を呼び出すことができます。

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## イベントのロギング

インプレッション、クリック、離脱などの貴重な指標を素早く簡単に記録できます。これらの分析を手動で処理するようにカスタムクリックリスナーを設定します。

{% tabs %}
{% tab web %}

[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)以下を使用して、ユーザーがカードを閲覧したときのインプレッションイベントをログに記録します。

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)を使用して、ユーザーがカードを操作したときのカードクリックイベントをログに記録します。

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% tab android %}

を参照できる。 [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt)は、コンテンツカードオブジェクト配列リストのようなBraze SDKの依存関係を参照して、Brazeロギングメソッドを呼び出すことができる。 [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)Brazeロギングメソッドを呼び出す。`ContentCardable`基本クラスを使用すると、`BrazeManager`へのデータの参照や提供が容易になります。 

インプレッションやカードのクリックを記録するには、[`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html)または[`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html)をそれぞれ呼び出します。 

[`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html)を使用して、Braze の特定のコンテンツカードを手動で「却下」として記録したり設定したりできます。カードがすでに却下済みとしてマークされている場合、そのカードを再度却下済みとしてマークすることはできません。

カスタム・クリック・リスナーを作成するには、以下を実装したクラスを作成する。 [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html)を実装したクラスを作り、それを [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html).ユーザーがコンテンツカードをクリックしたときに呼び出される[`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html)メソッドを実装します。次に、コンテンツカードクリックリスナーを使用するよう Braze に指示します。 

{% subtabs local %}
{% subtab Java %}

以下に例を示します。

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

以下に例を示します。

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
カスタム UI でコントロールバリアントコンテンツカードを処理するには、[`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) を渡した後、他のコンテンツカードタイプと同様に `logImpression` メソッドを呼び出します。オブジェクトはコントロールインプレッションを暗黙的にログに記録して、ユーザーがいつコントロールカードを表示したかを分析に通知します。{% endalert %}

{% endtab %}

{% tab swift %}

[`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate)プロトコルを実装し、デリゲートオブジェクトを`BrazeContentCardUI.ViewController`の`delegate`プロパティとして設定します。このデリゲートは、カスタムオブジェクトのデータを Braze に渡してログに記録するように処理します。例については、[コンテンツカードUIチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/)を参照してください。

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
カスタム UI でコントロールバリアントコンテンツカードを処理するには、[`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) を渡した後、他のコンテンツカードタイプと同様に `logImpression` メソッドを呼び出します。オブジェクトはコントロールインプレッションを暗黙的にログに記録して、ユーザーがいつコントロールカードを表示したかを分析に通知します。
{% endalert %}
{% endtab %}
{% endtabs %}
