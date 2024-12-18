---
nav_title: Integration
article_title: News Feed Integration for Android and FireOS
page_order: 1.2
platform: 
  - Android
  - FireOS
description: "This reference article covers different News Feed card types, the different card-specific properties available, and a custom integration example for your Android or FireOS application."
channel:
  - news feed
  
---

# News Feed integration

> This reference article covers different News Feed card types, the different card-specific properties available, and a custom integration example for your Android or FireOS application.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

In Android, the News Feed is implemented as a [fragment](http://developer.android.com/guide/components/fragments.html) available in the Braze Android UI project. Refer to [Google's documentation on fragments](https://developer.android.com/guide/fragments#Adding "Android Documentation: Fragments") for information on adding a fragment to an activity.

The `BrazeFeedFragment` class will automatically refresh and display the contents of the News Feed and log usage analytics. The cards that can appear in a user's News Feed are set on the Braze dashboard.

## Card types

Braze has five unique card types: banner image, captioned image, text announcement, and short news. Each type inherits common properties from a base model and has the following additional properties.

### Base card model properties

The [base card](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) model provides foundational behavior for all cards.  

|Property|Description|
|---|---|
| `getId()` | Returns the card's ID set by Braze. |
| `getViewed()` | Returns a boolean that reflects if the card is read or unread by the user. |
| `getExtras()` | Returns a map of key-value extras for this card. |
| `setViewed(boolean)` | Sets a card's viewed field. |
| `getCreated()` | Returns the unix timestamp of the card's creation time from Braze dashboard. |
| `getUpdated()` | Returns the unix timestamp of the card's latest update time from Braze dashboard. |
| `getCategories()` | Returns the list of categories assigned to the card, cards without a category will be assigned `ABKCardCategoryNoCategory`. |
| `isInCategorySet(EnumSet)` | Returns true if the card belongs to the given category set. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Banner image card properties

[Banner image cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-banner-image-card/index.html) are clickable full-sized images.

|Property|Description|
|---|---|
| `getImageUrl()` | Returns the URL of the card's image. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on. It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captioned image card properties

[Captioned image cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) are clickable full-sized images with accompanying descriptive text.

|Property|Description|
|---|---|
| `getImageUrl()` | Returns the URL of the card's image. |
| `getTitle()` | Returns the title text for the card. |
| `getDescription()` | Returns the body text for the card. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on.  It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Text announcement card (captioned image without image) properties

[Text announcement cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) are clickable cards containing descriptive text.

|Property|Description|
|---|---|
| `getTitle()` | Returns the title text for the card. |
| `getDescription()` | Returns the body text for the card. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on. It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Short news card properties

[Short news cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) are clickable cards with images and accompanying descriptive text.

|Property|Description|
|---|---|
| `getImageUrl()` | Returns the URL of the card's image. |
| `getTitle()` | Returns the title text for the card. |
| `getDescription()` | Returns the body text for the card. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on. It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Session analytics

The Android UI fragments do not automatically track session analytics. To ensure that sessions are [tracked correctly]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/), call `IBraze.openSession()` when your app is opened.

## Linking

Linking to the News Feed from an in-app message must be enabled by registering the `BrazeFeedActivity` within your `AndroidManifest.xml`.

## Custom feed integration

If you want to display the feed in a completely custom manner, it is possible to do so by using your own views populated with data from our models. To obtain News Feed models, you will need to subscribe for News Feed updates and use the resulting model data to populate your views. You will also need to log analytics on the model objects as users interact with your views.

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

To log a display of the feed, call [`Braze.logFeedDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-feed-displayed.html).

To log an impression or click on a Card, call [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) and [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) respectively.

