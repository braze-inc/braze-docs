---
nav_title: Card Types
page_order: 5
search_rank: 5
platform: Android
---

# Card Types
Braze has five unique News Feed card types which share a base model. Each card type also has additional card-specific properties which are listed below.

## Base Card

The [Base Card][29] model provides foundational behavior for all cards.  

- `getId()` - returns the card’s ID set by Braze
- `getViewed()` - returns a boolean reflects if the card is read or unread by the user
- `getExtras()` - returns a map of key-value extras for this card
- `setViewed(boolean)` - sets a card's viewed field
- `getCreated()` - returns the unix timestamp of the card’s creation time from Braze dashboard
- `getUpdated()` - returns the unix timestamp of the card’s latest update time from Braze dashboard
- `getCategories()` - returns the list of categories assigned to the card, cards without a category will be assigned ABKCardCategoryNoCategory
- `isInCategorySet(EnumSet)` - returns true if the card belongs to the given category set

## Banner Image Card
[Banner Image Cards][30] are clickable full-sized images. In addition to the base card properties:

- `getImageUrl()` - returns the URL of the card’s image
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL
- `getDomain()` - returns link text for the property url.

## Captioned Image Card
[Captioned Image Cards][31] are clickable full-sized images with accompanying descriptive text. In addition to the base card properties:

- `getImageUrl()` - returns the URL of the card’s image
- `getTitle()` - returns the title text for the card
- `getDescription()` - returns the body text for the card
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL
- `getDomain()` - returns the link text for the property url.

## Text Announcement Card (Captioned Image without Image)
[Text Announcement Cards][32] are clickable cards containing descriptive text. In addition to the base card properties:

- `getTitle()` - returns the title text for the card
- `getDescription()` - returns the body text for the card
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL
- `getDomain()` - returns the link text for the property url.

## Short News Card
[Short News Cards][33] are clickable cards with images and accompanying descriptive text.  In addition to the base card properties:

- `getImageUrl()` - returns the URL of the card’s image
- `getTitle()` - returns the title text for the card
- `getDescription()` - returns the body text for the card
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL
- `getDomain()` - returns the link text for the property url.

## Cross Promotion Small Card
[Cross-Promotion Small Cards][34] link to items in the Google Play Store or Kindle Store. In addition to the base card properties:

- `getTitle()` - returns the title text for the card. This will be the promoted item’s name.
- `getSubtitle()` - returns the text of the category of the promoted item
- `getImageUrl()` - returns property is the URL of the card’s image.
- `getPackage()` - reutrns the package name of the promoted item.
- `getRating()` - returns the rating of the promoted app. This property will be 0.0 unless the promoted item is an app, in which case the rating will be in the range of [0.0, 5.0];
- `getPrice()` - returns the price of the promoted app.
- `getReviewCount()` - returns the number of reviews of the promoted app. This property will be 0 unless the promoted item is an app.
- `getCaption()` - returns the text that will be displayed in the tag on the top of the small cross promotion card.
- `getUrl()` - returns the url of the promoted item which leads to the item’s App Store page.


[29]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html
[30]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/BannerImageCard.html
[31]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/CaptionedImageCard.html
[32]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/TextAnnouncementCard.html
[33]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/ShortNewsCard.html
[34]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/CrossPromotionSmallCard.html
