---
page_order: 3
nav_title: Content Cards
platform: 
  - Android
  - FireOS
description: "Learn about Content Cards for the Braze Android SDK, including the different data models and card-specific properties available for your Swift application."
channel:
  - content cards
search_rank: 1
---

# Content Cards

> Learn about Content Cards for the Braze Android SDK, including the different data models and card-specific properties available for your Swift application.

{% alert tip %}
When you're ready to start customizing and using Content Cards, see[Content Card customization]({{site.baseurl}}/developer_guide/customization_guides/content_cards).
{% endalert %}

## Prerequisites

Before you can use Braze Content Cards, you'll need to integrate the [Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration/) into your app. However, no additional setup is required.

## Google fragments

In Android, the Content Cards feed is implemented as a [fragment](https://developer.android.com/guide/components/fragments.html) available in the Braze Android UI project. The [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) class will automatically refresh and display the contents of the Content Cards and log usage analytics. The cards that can appear in a user's `ContentCards` are created on the Braze dashboard.

To learn how to add a fragment to an activity, see [Google's fragments documentation](https://developer.android.com/guide/fragments#Adding "Android Documentation: Fragments").

## Card types and properties

The Content Cards data model is available in the Android SDK and offers the following unique Content Card types. Each type shares a base model, which allows them to inherit common properties from the base model, in addition to having their own unique properties. For full reference documentation, see [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Base card model {#base-card-for-android}

The [base card](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) model provides foundational behavior for all cards.  

|Property | Description |
|---|---|
|`getId()` | Returns the card's ID set by Braze.|
|`getViewed()` | Returns a boolean reflects if the card is read or unread by the user.|
|`getExtras()` | Returns a map of key-value extras for this card.|
|`getCreated()`  | Returns the unix timestamp of the card's creation time from Braze.|
|`getIsPinned` | Returns a boolean that reflects whether the card is pinned.|
|`getOpenUriInWebView()`  | Returns a boolean that reflects whether Uris for this card should be opened <br> in the Braze WebView or not.|
|`getExpiredAt()` | Gets the expiration date of the card.|
|`getIsRemoved()` | Returns a boolean that reflects whether the end user has dismissed this card.|
|`getIsDismissible()`  | Returns a boolean that reflects whether the card is pinned.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image only {#banner-image-card-for-android}

[Image only cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) are clickable full-sized images.

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card's image.|
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a HTTP(s) URL or a protocol URL.|
|`getDomain()` | Returns link text for the property URL.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captioned image {#captioned-image-card-for-android}

[Captioned image cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) are clickable, full-sized images with accompanying descriptive text.

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card's image.|
|`getTitle()` | Returns the title text for the card.|
|`getDescription()` | Returns the body text for the card.|
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a HTTP(s) URL or a protocol URL.|
|`getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Classic {#text-Announcement-card-for-android}

A classic card without an image included will result in a [text announcement card](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). If an image is included, you will receive a [short news card](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Property | Description |
|---|---|
|`getTitle()` | Returns the title text for the card. |
|`getDescription()` | Returns the body text for the card. |
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a HTTP(s) URL or a protocol URL. | 
|`getDomain()` | Returns the link text for the property URL. |
|`getImageUrl()` | Returns the URL of the card's image, applies only to the classic Short News Card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Card methods

All [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) data model objects offer the following analytics methods for logging user events to Braze servers.

|Method | Description |
|---|---|
|`logImpression()` | Manually log an impression to Braze for a particular card. |
|`logClick()` | Manually log a click to Braze for a particular card. |
|`setIsDismissed()` | Manually log a dismissal to Braze for a particular card. If a card is already marked as dismissed, it cannot be marked as dismissed again. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Next steps

When you're ready to start customizing and using Content Cards, see[Content Card customization]({{site.baseurl}}/developer_guide/customization_guides/content_cards).
