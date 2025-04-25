# News Feed

> Learn about News Feed for the Braze Android SDK, including card types, card properties, and optional configurations.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Prerequisites

Before you can use News Feed, you'll need to [integrate the Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android). However, no additional setup is required.

## Google fragments

In Android, the Content Cards feed is implemented as a [fragment](https://developer.android.com/guide/components/fragments.html) available in the Braze Android UI project. The [`BrazeFeedFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-feed-fragment/index.html) class will automatically refresh and display the contents of the News Feed and log usage analytics. The cards that can appear in a user's News Feed are set on the Braze dashboard.

To learn how to add a fragment to an activity, see [Google's fragments documentation](https://developer.android.com/guide/fragments#Adding).

## Card types and properties

Braze has five unique card types: banner image, captioned image, text announcement, and short news. Each type inherits common properties from a base model and has the following additional properties.

### Base card model

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

### Banner image

[Banner image cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-banner-image-card/index.html) are clickable full-sized images.

|Property|Description|
|---|---|
| `getImageUrl()` | Returns the URL of the card's image. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on. It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captioned image

[Captioned image cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) are clickable full-sized images with accompanying descriptive text.

|Property|Description|
|---|---|
| `getImageUrl()` | Returns the URL of the card's image. |
| `getTitle()` | Returns the title text for the card. |
| `getDescription()` | Returns the body text for the card. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on.  It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Text announcement

[Text announcement cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) are clickable cards containing descriptive text and no image.

|Property|Description|
|---|---|
| `getTitle()` | Returns the title text for the card. |
| `getDescription()` | Returns the body text for the card. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on. It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Short news

[Short news cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) are clickable cards with images and accompanying descriptive text.

|Property|Description|
|---|---|
| `getImageUrl()` | Returns the URL of the card's image. |
| `getTitle()` | Returns the title text for the card. |
| `getDescription()` | Returns the body text for the card. |
| `getUrl()` | Returns the URL that will be opened after the card is clicked on. It can be a HTTP or HTTPS URL or a protocol URL. |
| `getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Optional configurations

### Tracking session analytics

The Android UI fragments do not automatically track session analytics. To ensure that sessions are [tracked correctly]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), call `IBraze.openSession()` when your app is opened.

### Linking from in-app messages

Linking to the News Feed from an in-app message must be enabled by registering the `BrazeFeedActivity` within your `AndroidManifest.xml`.

## Next steps

If you're ready to create your own News Feed, see [Creating a custom News Feed]({{site.baseurl}}/developer_guide/news_feed/).
