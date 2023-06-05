---
nav_title: Logging Analytics  
article_title: Logging Analytics 
page_order: 4
description: "This article covers how to manually log clicks, events, and analytics for your customized Content Cards."
toc_headers: "h2"

---

# Logging analytics manually

> If you would like to display the Content Cards in a completely custom manner, you can implement your own Content Cards presentation UI. However, data such as impressions, clicks, and dismissals are only handled automatically when using Braze's default card models. When implementing completely custom UI, you will need to handle this data manually. To do this, populate your custom UI with data from Braze's data models and manually log analytics like impressions and clicks. 

## Listening for card updates

When implementing your custom Content Cards, you can parse Braze's Content Card objects and extract their payload data such as `title`, `cardDescription`, and `imageUrl`. Then, you can use the resulting model data to populate your custom UI. 

To obtain Braze's Content Card data model, subscribe to Content Card updates. There are two properties to pay particular attention to:

* **`idString`**: Represents the Content Card ID. This is the unique identifier used to log analytics from custom Content Cards.
* **`extras`**: Encompasses all the key-value pairs from the Braze dashboard.

All properties outside of `idString` and `extras` are optional to parse for custom Content Cards. For more information on the data model, see each platform's integration article: [Android][1], [iOS][2], [Web][3].

<!--This alert was taken from the Web guide. Is it applicable for Android and Swift as well? -->

{% alert important %}
Content Cards will only refresh on session start if a subscribe request is called before `openSession()`. You can always choose to [manually refresh the feed]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed) as well.
{% endalert %}

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

### Create a private subscriber variable

To subscribe to card updates, first declare a private variable in your custom class to hold your subscriber:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### Subscribe to updates

Next, add the following code to subscribe to Content Card updates from Braze, typically inside of your custom Content Cards activity's `Activity.onCreate()`:

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
Braze.getInstance(context).requestContentCardsRefresh(true);
```

### Unsubscribe

We also recommend unsubscribing when your custom activity moves out of view. Add the following code to your activity's `onDestroy()` lifecycle method:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### Create a private subscriber variable

To subscribe to card updates, first declare a private variable in your custom class to hold your subscriber:

```kotlin
private var mContentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### Subscribe to updates

Next, add the following code to subscribe to Content Card updates from Braze, typically inside of your custom Content Cards activity's `Activity.onCreate()`:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
mContentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### Unsubscribe

We also recommend unsubscribing when your custom activity moves out of view. Add the following code to your activity's `onDestroy()` lifecycle method:

```kotlin
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

To access the Content Cards data model, call `contentCards.cards` on your `braze` instance.

{% subtabs %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Additionally, you can also maintain a subscription to observe for changes in your Content Cards. You can do so in one of two ways: 
1. Maintaining a cancellable; or 
2. Maintaining an `AsyncStream`.

### Cancellable 

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

Additionally, if you wish to maintain a subscription to your content cards, you can call `subscribeToUpdates`:

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Register a callback function to subscribe for updates when cards are refreshed.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates(function(updates){
  const cards = updates.cards;
  // do something with the latest instance of `cards`
});

braze.openSession();
```

{% endtab %}
{% endtabs %}



## Logging events

After extending your custom objects to function as Content Cards, logging valuable metrics like impressions, clicks, and dismissals is quick and simple. Set a custom click listener to manually handle these analytics.

<!-- JOSH TO DO: Reminder: When you remove the information from the Android guide that is duplicative with this article, move the Helper file information from Advanced Integration Guide into the Integration section --->

{% tabs %}
{% tab Android %}

<!-- Android Question: What is the difference between this prescribed method and the advice given in: https://www.braze.com/docs/developer_guide/platform_integration_guides/android/content_cards/customization/handling_clicks_manually. Would that article's content be better to use? --->

The [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) can reference Braze SDK dependencies such as the Content Card objects array list to get the `Card` to call the Braze logging methods. Use the `ContentCardable` base class to easily reference and provide data to the `BrazeManager`. 

To log an impression or click on a card, call [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) or [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) respectively. 

You can manually log or set a Content Card as "dismissed" to Braze for a particular card with [`setIsDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html). If a card is already marked as dismissed, it cannot be marked as dismissed again.

{% subtabs %}
{% subtab Java %}

### Custom objects call the logging methods

Within your `ContentCardable` base class, call the `BrazeManager` directly, if appropriate. In this example, the `cardData` property will be nonnull if the object came from a Content Card. 
```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
        Tile tile = currentTiles.get(position);
        tile.logContentCardImpression();
        ...
    }
```

### Retrieve the Content Card from the `ContentCardId`

The `ContentCardable` base class handles the heavy lifting of calling the `BrazeManager` and passing the unique identifier from the Content Card associated with the custom object.

```java
    public void logContentCardImpression() {
        if (cardData != null){
            BrazeManager.getInstance().logContentCardImpression(cardData.getContentCardId());
        }
    }
```

### Call `Card` functions

Then, the `BrazeManager` calls our logging methods.

```java
    public void logContentCardClicked(String idString) {
        getContentCard(idString).ifPresent(Card::logClick);
    }

    public void logContentCardImpression(String idString) {
        getContentCard(idString).ifPresent(Card::logImpression);
    }

    private Optional<Card> getContentCard(String idString) {
        return cardList.filter(c -> c.id.equals(idString)).findAny();
    }
```

{% endsubtab %}
{% subtab Kotlin %}

### Custom objects call the logging methods

Within your `ContentCardable` base class, call the `BrazeManager` directly, if appropriate. In this example, the `cardData` property will be nonnull if the object came from a Content Card. 

```kotlin
override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val tile = currentTiles[position]
        tile.logContentCardImpression()
        ...
    }
```

### Retrieve the Content Card from the `ContentCardId`

The `ContentCardable` base class handles the heavy lifting of calling the `BrazeManager` and passing the unique identifier from the Content Card associated with the custom object.

```kotlin
    fun logContentCardImpression() {
        cardData?.let { BrazeManager.getInstance().logContentCardImpression(it.contentCardId) }
    }
```

### Call `Card` functions

Then, the `BrazeManager` calls our logging methods.

```kotlin
    fun logContentCardClicked(idString: String?) {
        getContentCard(idString)?.logClick()
    }

    fun logContentCardImpression(idString: String?) {
        getContentCard(idString)?.logImpression()
    }

    private fun getContentCard(idString: String?): Card? {
        return cardList.find { it.id == idString }.takeIf { it != null }
    }
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

Implement the [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) protocol and set your delegate object as the `delegate` property of your `BrazeContentCardUI.ViewController`. This delegate will handle passing the data of your custom object back to Braze to be logged.

{% subtabs %}
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

Refer to the [Content Cards UI tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) for an example. 

{% endtab %}
{% tab Web %}

Log impression events when cards are viewed by users:

```javascript
import * as braze from "@braze/web-sdk";

braze.logCardImpressions([card1, card2, card3], true);
```

Log card click events when users interact with a card:

```javascript
import * as braze from "@braze/web-sdk";

braze.logCardClick(card, true);
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/