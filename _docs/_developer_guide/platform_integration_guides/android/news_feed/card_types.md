---
nav_title: Card Types
article_title: News Feed Card Types for Android and FireOS
page_order: 1.2
platform: 
  - Android
  - FireOS
description: "This article covers different News Feed card types and the different card-specific properties available."
channel:
  - news feed
  
---

# Card types

Braze has five unique News Feed card types that share a base model. Each card type also has additional card-specific properties which are listed below.

## Base card

The [base card][29] model provides foundational behavior for all cards.  

- `getId()` - returns the card’s ID set by Braze.
- `getViewed()` - returns a boolean that reflects if the card is read or unread by the user.
- `getExtras()` - returns a map of key-value extras for this card.
- `setViewed(boolean)` - sets a card's viewed field.
- `getCreated()` - returns the unix timestamp of the card’s creation time from Braze dashboard.
- `getUpdated()` - returns the unix timestamp of the card’s latest update time from Braze dashboard.
- `getCategories()` - returns the list of categories assigned to the card, cards without a category will be assigned `ABKCardCategoryNoCategory`.
- `isInCategorySet(EnumSet)` - returns true if the card belongs to the given category set.

## Banner image card
[Banner image cards][30] are clickable full-sized images. In addition to the base card properties:

- `getImageUrl()` - returns the URL of the card’s image.
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL.
- `getDomain()` - returns link text for the property URL.

## Captioned image card

[Captioned image cards][31] are clickable full-sized images with accompanying descriptive text. In addition to the base card properties:

- `getImageUrl()` - returns the URL of the card’s image.
- `getTitle()` - returns the title text for the card.
- `getDescription()` - returns the body text for the card.
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL.
- `getDomain()` - returns the link text for the property url.

## Text announcement card (captioned image without image)

[Text announcement cards][32] are clickable cards containing descriptive text. In addition to the base card properties:

- `getTitle()` - returns the title text for the card.
- `getDescription()` - returns the body text for the card.
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL.
- `getDomain()` - returns the link text for the property URL.

## Short news card

[Short news cards][33] are clickable cards with images and accompanying descriptive text. In addition to the base card properties:

- `getImageUrl()` - returns the URL of the card’s image.
- `getTitle()` - returns the title text for the card.
- `getDescription()` - returns the body text for the card.
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL.
- `getDomain()` - returns the link text for the property URL.

[29]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/index.html
[30]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-banner-image-card/index.html
[31]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-captioned-image-card/index.html
[32]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-text-announcement-card/index.html
[33]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-short-news-card/index.html
