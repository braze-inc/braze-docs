# Creating a custom News Feed

> Learn how to create a custom News Feed for the Braze Android SDK.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Creating a custom feed

You can create and display a custom feed by populating your own views with data from Braze News Feed models.

### Step 1: Subscribe to feed updates

Declare a private variable in your custom feed class to hold your subscriber.

```java
// subscriber variable
private IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

In your custom feed activity's `Activity.onCreate()`, add the following code so you can subscribe to feed updates from Braze.

```java
// Remove the old subscription first
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
mFeedUpdatedSubscriber = new IEventSubscriber<FeedUpdatedEvent>() {
  @Override
  public void trigger(final FeedUpdatedEvent event) {
    // This list of Card objects included in the FeedUpdatedEvent should be used to populate your News Feed views.
    List<Card> cards = event.getFeedCards();
    // your logic here
  }
};
Braze.getInstance(context).subscribeToFeedUpdates(mFeedUpdatedSubscriber);

// Request a refresh of feed data
Braze.getInstance(context).requestFeedRefresh();
```

We recommend that you unsubscribe when your custom feed activity moves out of view, by adding the following code to your activity's `onDestroy()` lifecycle method.

```java
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

### Step 2: Log analytics

When you use a custom view, you'll need to log analytics manually since automatic handling is only available through a Braze view.

| Action                          | Method                                                                                                                                   |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Log a display of the feed       | [`Braze.logFeedDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-feed-displayed.html) |
| Log an impression               | [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html)       |
| Log a click on a Card           | [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) |
