## About .NET MAUI Content Cards

The Braze .NET MAUI (formerly Xamarin) SDK includes a default card feed to get you started with Content Cards. The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user’s Content Cards.

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Card types and properties

The Braze .NET MAUI SDK has three unique Content Cards card types that share a base model: [Banner](#xamarin_banner), [Captioned Image](#xamarin_captioned-image), and [Classic](#xamarin_classic). Each type inherits common properties from a base model and has the following additional properties.

### Base card model

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
|`urlString`        | (Optional) The URL string associated with the card click action.                                                       |
|`openUrlInWebView` | Whether URLs for this card should be opened in the Braze WebView or not.                                                 |
|`isControlCard`    | Whether this card is a control card. Control cards should not be displayed to the user.                                |
|`extras`           | The map of key-value extras for this card.                                                                             |
|`isTest`           | Whether this card is a test card.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the base card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct) documentation.

### Banner

Banner cards are clickable, full-sized images.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the banner card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) documentation (now renamed to image only).

### Captioned image

Captioned image cards are clickable, full-sized images with accompanying descriptive text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the captioned image card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct) documentation.

### Classic

Classic cards have a title, description, and an optional image on the left of the text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | (Optional) The URL of the card's image.                                                                           |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the classic (text announcement) Content Card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct) documentation. For a full reference of the classic image (short news) card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct) documentation.

## Card methods

You can use these additional methods to build a custom Content Cards Feed within your app:

| Method                                   | Description                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Requests the latest Content Cards from the Braze SDK server.                                           |
| `getContentCards()`                      | Retrieves Content Cards from the Braze SDK. This will return the latest list of cards from the server. |
| `logContentCardClicked(cardId)`          | Logs a click for the given Content Card ID. This method is used only for analytics.                    |
| `logContentCardImpression(cardId)`       | Logs an impression for the given Content Card ID.                                                      |
| `logContentCardDismissed(cardId)`        | Logs a dismissal for the given Content Card ID.                                                        |
