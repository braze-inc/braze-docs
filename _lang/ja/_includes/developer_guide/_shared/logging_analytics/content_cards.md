> コンテンツカード用のカスタムUIを構築する場合、インプレッション、クリック、非表示といった分析データを手動で記録する必要があります。これらはデフォルトのカードモデルでのみ自動的に処理されるためです。これらのイベントの記録は、コンテンツカード統合の標準的な部分であり、正確なキャンペーンレポートと請求に不可欠です。これを行うには、カスタムUIにBrazeのデータモデルからデータを入力し、その後手動でイベントを記録します。分析の記録方法を理解したら、Braze の顧客が[カスタムコンテンツカードを作成する]({{site.baseurl}}/developer_guide/content_cards/creating_cards/)一般的な方法を確認できます。 

## 分析の記録

カスタムコンテンツカードを実装する場合、コンテンツカードオブジェクトを解析して、`title`、`cardDescription`、`imageUrl`などのペイロードデータを抽出できます。その後、生成されたモデルデータを使用してカスタム UI を作成できます。 

コンテンツカードデータモデルを取得するには、コンテンツカードの更新をサブスクライブします。特に注意すべきプロパティが2つあります。

* **`id`**：コンテンツカード ID の文字列を表します。これは、カスタムコンテンツカードの分析を記録するために使用されるユニークな識別子です。
* **`extras`**：Braze ダッシュボードのすべてのキーと値のペアが含まれます。 

カスタムコンテンツカードでは`id`および`extras`以外のすべてのプロパティの解析はオプションです。データモデルの詳細については、[Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android)、[iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift)、[Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web) の各プラットフォームの統合記事を参照してください。


{% tabs %}
{% tab web %}

カードが更新されたときの更新をサブスクライブするコールバック関数を登録します。

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
コンテンツカードは、`openSession()`の前にサブスクライブリクエストが呼び出された場合にのみ、セッション開始時に更新されます。[フィードを手動で更新]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/)することもいつでも可能です。
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### ステップ 1: プライベートサブスクライバー変数を作成する

カード更新をサブスクライブするには、まずカスタムクラスでサブスクライバーを保持するプライベート変数を宣言します。

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### ステップ 2: 更新をサブスクライブする

次に、通常はカスタムコンテンツカードアクティビティの`Activity.onCreate()`内で、以下のコードを追加して、Braze のコンテンツカードの更新をサブスクライブします。

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

### ステップ 3: 購読解除する

また、カスタムアクティビティが表示されなくなったら、購読を解除することをおすすめします。アクティビティの`onDestroy()`ライフサイクルメソッドに次のコードを追加します。

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### ステップ 1: プライベートサブスクライバー変数を作成する

カード更新をサブスクライブするには、まずカスタムクラスでサブスクライバーを保持するプライベート変数を宣言します。

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### ステップ 2: 更新をサブスクライブする

次に、通常はカスタムコンテンツカードアクティビティの`Activity.onCreate()`内で、以下のコードを追加して、Braze のコンテンツカードの更新をサブスクライブします。

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
contentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### ステップ 3: 購読解除する

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

さらに、サブスクリプションを維持して、コンテンツカードの変更を監視することもできます。これには次の2つの方法があります。 
1. キャンセル可能なオブジェクトを維持する。または、 
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

さらに、コンテンツカードのサブスクリプションを維持する場合は、[`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:))を呼び出すことができます。

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}

コンテンツカードのデータを取得するには、`getContentCards`メソッドを使用します。

```javascript
import Braze from "@braze/react-native-sdk";

const cards = await Braze.getContentCards();
```

更新を監視するには、コンテンツカードの更新イベントをサブスクライブします。

```javascript
const subscription = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to log an impression
    } else {
      // Use card.title, card.cardDescription, card.image, etc.
    }
  });
});
```

Braze サーバーからコンテンツカードを手動で更新するには：

```javascript
Braze.requestContentCardsRefresh();
```

ネットワークリクエストなしでキャッシュされたコンテンツカードを取得するには：

```javascript
const cachedCards = await Braze.getCachedContentCards();
```

{% endtab %}
{% endtabs %}

## イベントの記録

インプレッション、クリック、非表示などの重要な指標の記録は、素早く簡単に行えます。これらの分析を手動で処理するようにカスタムクリックリスナーを設定します。

{% tabs %}
{% tab web %}

[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)を使用して、ユーザーがカードを閲覧したときのインプレッションイベントを記録します。

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)を使用して、ユーザーがカードを操作したときのカードクリックイベントを記録します。

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% tab android %}

[`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt)は、コンテンツカードオブジェクトの配列リストなどの Braze SDK 依存関係を参照して、Braze のロギングメソッドを呼び出すための[`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)を取得できます。`ContentCardable`基本クラスを使用すると、`BrazeManager`へのデータの参照や提供が容易になります。 

インプレッションやカードのクリックを記録するには、[`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html)または[`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html)をそれぞれ呼び出します。 

[`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html)を使用して、特定のコンテンツカードを手動で「却下」として記録したり、Braze に設定したりできます。カードがすでに却下済みとしてマークされている場合、そのカードを再度却下済みとしてマークすることはできません。

カスタムクリックリスナーを作成するには、[`IContentCardsActionListener`](#logging-analytics)を実装するクラスを作成し、[`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html)に登録します。ユーザーがコンテンツカードをクリックしたときに呼び出される[`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html)メソッドを実装します。次に、コンテンツカードクリックリスナーを使用するよう Braze に指示します。 

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
カスタム UI でコントロールバリアントコンテンツカードを処理するには、[`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)オブジェクトを渡した後、他のコンテンツカードタイプと同様に`logImpression`メソッドを呼び出します。オブジェクトはコントロールインプレッションを暗黙的に記録して、ユーザーがいつコントロールカードを表示したかを分析に通知します。{% endalert %}

{% endtab %}

{% tab swift %}

[`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate)プロトコルを実装し、デリゲートオブジェクトを`BrazeContentCardUI.ViewController`の`delegate`プロパティとして設定します。このデリゲートは、カスタムオブジェクトのデータを Braze に渡して記録する処理を行います。例については、[Content Cards UI tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/)を参照してください。

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
カスタム UI でコントロールバリアントコンテンツカードを処理するには、[`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:))オブジェクトを渡した後、他のコンテンツカードタイプと同様に`logImpression`メソッドを呼び出します。オブジェクトはコントロールインプレッションを暗黙的に記録して、ユーザーがいつコントロールカードを表示したかを分析に通知します。
{% endalert %}
{% endtab %}

{% tab react native %}

ユーザーがカードを閲覧したときにインプレッションイベントを記録します。

```javascript
Braze.logContentCardImpression(card.id);
```

ユーザーがカードを操作したときにカードクリックイベントを記録します。

```javascript
Braze.logContentCardClicked(card.id);
```

ユーザーがカードを閉じたときに非表示イベントを記録します。

```javascript
Braze.logContentCardDismissed(card.id);
```

{% endtab %}
{% endtabs %}

## クリック時の動作の処理

{% tabs %}
{% tab web %}

カスタムフィードでユーザーがコンテンツカードをクリックした場合、クリック時の動作（URLへの遷移、ディープリンク、カスタムイベントの記録など）は自動的に処理されません。[`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)を使用して、カードのURLを処理し、設定されたクリック時のアクション（Braze アクション（`brazeActions://` URL）を含む）を実行します。

```javascript
import * as braze from "@braze/web-sdk";

// In your card click handler
function onCardClick(card) {
  // Log the click
  braze.logContentCardClick(card);

  // Handle the on-click behavior
  if (card.url) {
    braze.handleBrazeAction(card.url);
  }
}
```

| パラメーター | 説明 |
|---|---|
| `url` | 有効なURL、またはスキーム`brazeActions://`を持つ有効な Braze アクションURL。 |
| `openLinkInNewTab` | （オプション）URLを新しいタブで開くかどうかを指定します。デフォルトは`false`です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
`handleBrazeAction()`を呼び出さない場合、Braze ダッシュボードで設定されたクリック時の動作（「カスタムイベントを記録」や「URLに遷移」など）は、カスタムフィードに表示されるカードに対して実行されません。
{% endalert %}

{% endtab %}
{% tab android %}

クリック時の動作は、デフォルトのコンテンツカード UI によって自動的に処理されます。カスタム実装の場合は、上記の[分析の記録](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html)セクションで説明されている[`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html)インターフェイスを使用してください。

{% endtab %}
{% tab swift %}

クリック時の動作は、デフォルトのコンテンツカード UI によって自動的に処理されます。カスタム実装の場合は、上記の[分析の記録](#logging-analytics)セクションで説明されている[`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate)プロトコルを使用してください。

{% endtab %}
{% endtabs %}