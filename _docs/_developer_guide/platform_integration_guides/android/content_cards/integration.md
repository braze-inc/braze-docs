---
nav_title: Integration
article_title: Content Card Integration for Android and FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "This article covers the Content Card integration and the different data models and card-specific properties available for your Android or FireOS application."
channel:
  - content cards

---

# Content Cards integration

In Android, the Content Cards feed is implemented as a [fragment][2] available in the Braze Android UI project. View [Google's Fragments][3] for information on adding a fragment to an activity.

The [`ContentCardsFragment`][4] class will automatically refresh and display the contents of the Content Cards and log usage analytics. The cards that can appear in a user's `ContentCards` are created on the Braze dashboard.

## Content Cards data model

The Content Cards data model is available in the Android SDK.

## Content Card model {#card-types-for-android}

Braze has three unique Content Cards card types that share a base model: banner, captioned image, and classic. Each type inherits common properties from a base model and has the following additional properties.

### Base Content Card model properties {#base-card-for-android}

The [base card][29] model provides foundational behavior for all cards.  

|Property | Description |
|---|---|
|`getId()` | Returns the card’s ID set by Braze.|
|`getViewed()` | Returns a boolean reflects if the card is read or unread by the user.|
|`getExtras()` | Returns a map of key-value extras for this card.|
|`getCreated()`  | Returns the unix timestamp of the card’s creation time from Braze.|
|`getIsPinned` | Returns a boolean that reflects whether the card is pinned.|
|`getOpenUriInWebView()`  | Returns a boolean that reflects whether Uris for this card should be opened <br> in Braze's WebView or not.|
|`getExpiredAt()` | Gets the expiration date of the card.|
|`getIsRemoved()` | Returns a boolean that reflects whether the end user has dismissed this card.|
|`getIsDismissible()`  | Returns a boolean that reflects whether the card is pinned.|
{: .reset-td-br-1 .reset-td-br-2}

### Banner image card properties {#banner-image-card-for-android}

[Banner image cards][30] are clickable full-sized images.

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card’s image.|
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a http(s) URL or a protocol URL.|
|`getDomain()` | Returns link text for the property URL.|
{: .reset-td-br-1 .reset-td-br-2}

### Captioned image card properties {#captioned-image-card-for-android}

[Captioned image cards][31] are clickable full-sized images with accompanying descriptive text.

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card’s image.|
|`getTitle()` | Returns the title text for the card.|
|`getDescription()` | Returns the body text for the card.|
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a http(s) URL or a protocol URL.|
|`getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2}

### Classic card properties {#text-Announcement-card-for-android}

A classic card without an image included will result in a [text announcement card][32]. If an image is included, you will receive a [short news card][41].

|Property | Description |
|---|---|
|`getTitle()` | Returns the title text for the card. |
|`getDescription()` | Returns the body text for the card. |
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a http(s) URL or a protocol URL. | 
|`getDomain()` | Returns the link text for the property URL. |
|`getImageUrl()` | Returns the URL of the card's image, applies only to the classic Short News Card. |
{: .reset-td-br-1 .reset-td-br-2}

## Card methods

All `Card` data model objects offer the following analytics methods for logging user events to Braze servers.

|Method | Description |
|---|---|
|`logImpression()` | Manually log an impression to Braze for a particular card. |
|`logClick()` | Manually log a click to Braze for a particular card. |
|`setIsDismissed()` | Manually log a dismissal to Braze for a particular card. If a card is already marked as dismissed, it cannot be marked as dismissed again. |
{: .reset-td-br-1 .reset-td-br-2}

## Custom Content Cards {#fully-custom-content-card-display-for-android}

If you would like to display the Content Cards in a completely custom manner, it is possible to do so by using your own views populated with data from our models. To obtain Braze’s Content Cards models, you will need to subscribe to Content Card updates and use the resulting model data to populate your views. You will also need to log analytics on the model objects as users interact with your views.

### Part 1: Subscribing to Content Card updates

First, declare a private variable in your custom class to hold your subscriber:

{% tabs %}
{% tab JAVA %}

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
private var mContentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

{% endtab %}
{% endtabs %}

Next, add the following code to subscribe to Content Card updates from Braze, typically inside of your custom Content Cards activity's `Activity.onCreate()`:

{% tabs %}
{% tab JAVA %}

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

{% endtab %}
{% tab KOTLIN %}

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

{% endtab %}
{% endtabs %}

We also recommend unsubscribing when your custom activity moves out of view. Add the following code to your activity's `onDestroy()` lifecycle method:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endtab %}
{% endtabs %}

### Part 2: Logging analytics

When using custom views, you will need to log analytics manually since analytics are only handled automatically when using Braze views.

To log a display of the Content Cards, call [`Appboy.logContentCardsDisplayed()`][41].

To log an impression or click on a Card, call [`Card.logClick()`][7] or [`Card.logImpression()`][8] respectively.

For campaigns using Control Cards for A/B testing, you can use [`Card.isControl()`][55] to determine if a card will be blank, and used only for tracking purposes.

### Manually dismissing a Content Card

You can manually log or set a Content Card as "dismissed" to Braze for a particular card with [`setIsDismissed`][57].

If a card is already marked as dismissed, it cannot be marked as dismissed again.

[7]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/log-click.html
[8]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/log-impression.html
[55]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/is-control.html
[57]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/index.html#-1644350493%2FProperties%2F-1725759721
[41]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/log-content-cards-displayed.html

[29]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/index.html
[30]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-banner-image-card/index.html
[31]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-captioned-image-card/index.html
[32]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-text-announcement-card/index.html
[41]: https://github.com/Appboy/android-sdk/blob/9a091979b4cbaff7f935c2cae03043a944c3ab53/android-sdk-base/src/main/java/com/appboy/models/cards/ShortNewsCard.java
[2]: http://developer.android.com/guide/components/fragments.html
[3]: http://developer.android.com/guide/components/fragments.html#Adding "Android Documentation: Fragments"
[4]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
