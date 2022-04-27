---
nav_title: Integration
article_title: News Feed Integration for Android and FireOS
page_order: 1.2
platform: 
  - Android
  - FireOS
description: "This article covers different News Feed card types, the different card-specific properties available, and a custom integration example for your Android or FireOS application."
channel:
  - news feed
  
---

# News Feed integration

In Android, the News Feed is implemented as a [fragment][2] available in the Braze Android UI project. Refer to Google's documentation on [Fragments][3] for information on adding a fragment to an activity.

The `AppboyFeedFragment` class will automatically refresh and display the contents of the News Feed and log usage analytics. The cards that can appear in a user's News Feed are set on the Braze dashboard.

## Card types

Braze has five unique card types: banner image, captioned image, text announcement, and short news. Each type inherits common properties from a base model and has the following additional properties.

### Base card model properties

The [base card][29] model provides foundational behavior for all cards.  

|Property|Description|
|---|---|
| `getId()` | Returns the card’s ID set by Braze. |
| `getViewed()` | Returns a boolean that reflects if the card is read or unread by the user. |
| `getExtras()` | Returns a map of key-value extras for this card. |
| `setViewed(boolean)` | Sets a card's viewed field. |
| `getCreated()` | Returns the unix timestamp of the card’s creation time from Braze dashboard. |
| `getUpdated()` | Returns the unix timestamp of the card’s latest update time from Braze dashboard. |
| `getCategories()` | Returns the list of categories assigned to the card, cards without a category will be assigned `ABKCardCategoryNoCategory`. |
| `isInCategorySet(EnumSet)` | Returns true if the card belongs to the given category set. |
{: .reset-td-br-1 .reset-td-br-2}

### Banner image card properties

[Banner image cards][30] are clickable full-sized images.

|Property|Description|
|---|---|
| `getImageUrl()` | Returns the URL of the card’s image. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on. It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2}

### Captioned image card properties

[Captioned image cards][31] are clickable full-sized images with accompanying descriptive text.

|Property|Description|
|---|---|
| `getImageUrl()` | Returns the URL of the card’s image. |
| `getTitle()` | Returns the title text for the card. |
| `getDescription()` | Returns the body text for the card. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on.  It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2}

### Text announcement card (captioned image without image) properties

[Text announcement cards][32] are clickable cards containing descriptive text.

|Property|Description|
|---|---|
| `getTitle()` | Returns the title text for the card. |
| `getDescription()` | Returns the body text for the card. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on. It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2}

### Short news card properties

[Short news cards][33] are clickable cards with images and accompanying descriptive text.

|Property|Description|
|---|---|
| `getImageUrl()` | Returns the URL of the card’s image. |
| `getTitle()` | Returns the title text for the card. |
| `getDescription()` | Returns the body text for the card. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on. It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2}

## Session analytics

The Android UI fragments do not automatically track session analytics. To ensure that sessions are [tracked correctly][4], call `IAppboy.openSession()` when your app is opened.

## Linking

Linking to the News Feed from an in-app message must be enabled by registering the `AppboyFeedActivity` within your `AndroidManifest.xml`.

## Custom feed integration

If you would like to display the feed in a completely custom manner, it is possible to do so by using your own views populated with data from our models. To obtain Braze's News Feed models, you will need to subscribe for News Feed updates and use the resulting model data to populate your views. You will also need to log analytics on the model objects as users interact with your views.

### Part 1: Subscribing to feed updates

First, declare a private variable in your custom feed class to hold your subscriber:

```java
// subscriber variable
private IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

Next, add the following code to subscribe to feed updates from Braze, typically inside of your custom feed activity's `Activity.onCreate()`:

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

We also recommend unsubscribing when your custom feed activity moves out of view. Add the following code to your activity's `onDestroy()` lifecycle method:

```
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

### Part 2: Logging analytics

When using custom views, you will need to log analytics manually since analytics are only handled automatically when using Braze views.

To log a display of the feed, call [`Appboy.logFeedDisplayed()`][6].

To log an impression or click on a Card, call [`Card.logClick()`][7] and [`Card.logImpression()`][8] respectively.

[36]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/get-extras.html
[2]: http://developer.android.com/guide/components/fragments.html
[3]: http://developer.android.com/guide/components/fragments.html#Adding "Android Documentation: Fragments"
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[6]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/log-feed-displayed.html
[7]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/log-click.html
[8]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/log-impression.html
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/card_types/#card-types
[29]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/index.html
[30]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-banner-image-card/index.html
[31]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-captioned-image-card/index.html
[32]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-text-announcement-card/index.html
[33]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-short-news-card/index.html
