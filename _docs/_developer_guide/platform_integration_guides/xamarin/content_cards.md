---
nav_title: Content Cards
article_title: Content Cards for Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
channel: content cards
page_order: 3
description: "This reference article covers Content Card implementation guidelines for the Xamarin platform."

---

# Content Card integration

> Learn how to set up iOS, Android, and FireOS Content Cards for the Xamarin platform.

The Braze SDK includes a default card feed to get you started with Content Cards. The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user’s Content Cards.

For information on how to integrate the Content Cards into your Xamarin app, see our [Android integration guide][1] and [iOS integration guide][2].

## Prerequisites

To use this feature, you'll need to [integrate Braze SDK for the Xamarin platform]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/).

## Content Card methods

You can use these additional methods to build a custom Content Cards Feed within your app:

| Method                                   | Description                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Requests the latest Content Cards from the Braze SDK server.                                           |
| `getContentCards()`                      | Retrieves Content Cards from the Braze SDK. This will return the latest list of cards from the server. |
| `logContentCardClicked(cardId)`          | Logs a click for the given Content Card ID. This method is used only for analytics.                    |
| `logContentCardImpression(cardId)`       | Logs an impression for the given Content Card ID.                                                      |
| `logContentCardDismissed(cardId)`        | Logs a dismissal for the given Content Card ID.                                                        |

## Content Card data model

The Braze Xamarin SDK has three unique Content Cards card types that share a base model: **banner**, **captioned image**, and **classic**. Each type inherits common properties from a base model and has the following additional properties.

### Base Content Card model properties

|Property           | Description                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
|`idString`         | The card's ID set by Braze.                                                                                            |
|`created`          | The UNIX timestamp of the card's creation time from Braze.                                                             |
|`expiresAt`        | The UNIX timestamp of the card's expiration time. When the value is less than 0, it means the card never expires.      |
|`viewed`           | Whether the card is read or unread by the user. This does not log analytics.                                           |
|`clicked`          | Whether the card has been clicked by the user.                                                                         |
|`pinned`           | Whether the card is pinned.                                                                                            |
|`dismissed`        | Whether the user has dismissed this card. Marking a card as dismissed that has already been dismissed will be a no-op. |
|`dismissible`      | Whether the card is dismissible by the user.                                                                           |
|`urlString`        | (Optional) The url string associated with the card click action.                                                       |
|`openUrlInWebView` | Whether URLs for this card should be opened in Braze's WebView or not.                                                 |
|`isControlCard`    | Whether this card is a control card. Control cards should not be displayed to the user.                                |
|`extras`           | The map of key-value extras for this card.                                                                             |
|`isTest`           | Whether this card is a test card.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2}

For a full reference of the base card, see the [Android][3] and [iOS][4] documentation.

### Banner Content Card model properties

Banner cards are clickable, full-sized images.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
{: .reset-td-br-1 .reset-td-br-2}

For a full reference of the banner card, see the [Android][5] and [iOS][6] documentation (now renamed to image only).

### Captioned image Content Card model properties

Captioned image cards are clickable, full-sized images with accompanying descriptive text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2}

For a full reference of the captioned image card, see the [Android][7] and [iOS][8] documentation.

### Classic Content Card model properties

Classic cards have a title, description, and an optional image on the left of the text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | (Optional) The URL of the card's image.                                                                           |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2}

For a full reference of the classic (text announcement) Content Card, see the [Android][9] and [iOS][10] documentation. For a full reference of the classic image (short news) card, see the [Android][11] and [iOS][12] documentation.

## GIF Support

{% multi_lang_include wrappers/gif_support/content_cards.md %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/
[3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html
[4]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct
[5]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html
[6]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct
[7]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html
[8]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct
[9]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html
[10]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct
[11]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html
[12]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct