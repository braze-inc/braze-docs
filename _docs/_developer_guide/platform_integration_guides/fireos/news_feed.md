---
nav_title: News Feed
platform: FireOS
page_order: 3

---
# News Feed

The News Feed is a fully customizable in-app content feed for your users. Our targeting and segmentation allows you to create a stream of content that is individually catered to the interests of each user. Depending on their position in the user life cycle and the nature of your app, this could be an on-boarding content server, an advertisement center, an achievement center, or a generic news center.

## Example News Feed

![Sample News Feed][23]

## News Feed Integration Overview

In Android, the News Feed is implemented as a [Fragment][2] that is available in the Braze Android UI project. View [Google's documentation on Fragments][3] for information on how to add a Fragment to an Activity.

>  The Android UI Fragments do not automatically track session analytics. To ensure that sessions are tracked correctly, you should call `IAppboy.openSession()` when your app is opened (learn more about [tracking user sessions][4]).

The `AppboyFeedFragment` class will automatically refresh and display the contents of the News Feed and log usage analytics. The cards that can appear in a user's News Feed are set on the Braze dashboard.

Linking to the News Feed from an in-app message must be enabled by registering the `AppboyFeedActivity` within your [AndroidManifest.xml][28] file.

**Implementation Example**

See [`DroidBoyActivity.java`][5] in the Droidboy sample app.

## News Feed Customization

### Default Styling

Braze UI elements come with a default look and feel that matches the Android standard UI guidelines and provides a seamless experience. You can see these default styles in the `res/values/style.xml` file in the Braze SDK distribution.

```xml
  <style name="Appboy"/>
  <!-- Feed -->
  <style name="Appboy.Feed"/>
  <style name="Appboy.Feed.List">
    <item name="android:background">@android:color/transparent</item>
    <item name="android:divider">@android:color/transparent</item>
    <item name="android:dividerHeight">16.0dp</item>
    <item name="android:paddingLeft">12.5dp</item>
    <item name="android:paddingRight">5.0dp</item>
    <item name="android:scrollbarStyle">outsideInset</item>
  </style>
  ...
  </style>
```

### Overriding Styles

If you would prefer, you can override these styles to create a look and feel that better suits your app. To override a style, copy it in its entirety to the `styles.xml` file in your own project and make modifications. The whole style must be copied over to your local `styles.xml` file in order for all of the attributes to be correctly set.

#### Correct Style Override

```xml
<style name="Appboy.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```

#### Incorrect Style Override

```xml
<style name="Appboy.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```

### Feed Style Elements

Below is a description of the themable Braze UI elements and their names for styling purposes:

![Android Feed][18]
![Android Cards][19]
![Android Empty][20]
![Android Network Error][21]

### Setting A Custom Font

Braze allows for setting a custom font using the [font family guide][40]. To use it, override a style for cards and use the `fontFamily` attribute to instruct Braze to use your custom font family.

For example, to update the font on all titles for Short News Cards, override the `Appboy.Cards.ShortNews.Title` style and reference your custom font family. The attribute value should point to a font family in your `res/font` directory.

Here is a truncated example with a custom font family, `my_custom_font_family`, referenced on the last line:

```
<style name="Appboy.Cards.ShortNews.Title">
  <item name="android:layout_height">wrap_content</item>
  ...
  <item name="android:fontFamily">@font/my_custom_font_family</item>
  <item name="fontFamily">@font/my_custom_font_family</item>
</style>
```

### Setting a Custom News Feed Click Listener

You can handle News Feed clicks manually by setting a custom News Feed click listener. This enables use cases such as selectively using the native web browser to open web links.

#### Step 1: Implement a News Feed Click Listener

Create a class that implements [IFeedClickActionListener][37]. Implement the `onFeedCardClicked()` method, which will be called when the user clicks a News Feed card.

See [CustomFeedClickActionListener.java][38] in our Droidboy sample application for an example implementation.

#### Step 2: Instruct Braze to Use Your News Feed Click Listener

Once your `IFeedClickActionListener` is created, call `AppboyFeedManager.getInstance().setFeedCardClickActionListener()` to instruct `AppboyFeedManager` to use your custom `IFeedClickActionListener`.

See [PreferencesActivity.java][39] in our Droidboy sample application for an example implementation.

### Fully Custom Feed Display

If you would like to display the feed in a completely custom manner, it is possible to do so by using your own views populated with data from our [models][9]. To obtain Braze's News Feed models, you will need to subscribe to News Feed updates and use the resulting model data to populate your views. You will also need to log analytics on the model objects as users interact with your views.

#### Part 1: Subscribing to Feed Updates

First, declare a private variable in your custom feed class to hold your subscriber:

```java
// subscriber variable
private IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

Next, add the following code to subscribe to feed updates from Braze, typically inside of your custom feed activity's `Activity.onCreate()`:

```java
// Remove the old subscription first
Appboy.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
mFeedUpdatedSubscriber = new IEventSubscriber<FeedUpdatedEvent>() {
  @Override
  public void trigger(final FeedUpdatedEvent event) {
    // This list of Card objects included in the FeedUpdatedEvent should be used to populate your News Feed views.
    List<Card> cards = event.getFeedCards();
    // your logic here
  }
};
Appboy.getInstance(context).subscribeToFeedUpdates(mFeedUpdatedSubscriber);

// Request a refresh of feed data
Appboy.getInstance(context).requestFeedRefresh();
```

We also recommend unsubscribing when your custom feed activity moves out of view. Add the following code to your activity's `onDestroy()` lifecycle method:

```
Appboy.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

#### Part 2: Logging Analytics

When using custom views, you will need to log analytics manually as well, since analytics are only handled automatically when using Braze views.

To log a display of the feed, call [`Appboy.logFeedDisplayed()`][6].

To log an impression or click on a Card, call [`Card.logClick()`][7] and [`Card.logImpression()`][8] respectively.

## Categories

### Defining a News Feed Category

Instances of the Braze News Feed can be configured to only receive cards from a certain “category”. This allows for effective integration of multiple News Feed streams within a single application. For more information on this feature read our pages on [News Feed best practices][14]

News Feed Categories can be defined by calling the following methods as you load the News Feed:

```xml
newsFeed.setCategories(CardCategory.ALL_CATEGORIES);
newsFeed.setCategories(CardCategory.ADVERTISING);
newsFeed.setCategories(CardCategory.ANNOUNCEMENTS);
newsFeed.setCategories(CardCategory.NEWS);
newsFeed.setCategories(CardCategory.SOCIAL);
newsFeed.setCategories(CardCategory.NO_CATEGORY);
```

You can also populate a feed with a combination of categories as in the following example:

```xml
newsFeed.setCategories:EnumSet.of(CardCategory.ANNOUNCEMENTS, CardCategory.NEWS);
```

## Read/Unread Indicators

Braze allows you to optionally toggle on an Unread/Read indicator on News Feed cards as pictured below:

![UnreadvsRead][25]

### Enabling the Indicators

In order to enable this functionality add the following line to your `appboy.xml` file:

```xml
<bool name="com_appboy_newsfeed_unread_visual_indicator_on">true</bool>
```

### Customizing the Indicators
These indicators can be customized by altering the values in [android-sdk-ui/src/main/res/drawable-hdpi/icon_unread.png][26] and [android-sdk-ui/src/main/res/drawable-hdpi/icon_read.png][27].

## Card Types
Braze has 5 unique News Feed card types that share a base model. Each card type also has additional card-specific properties which are listed below.

#### Base Card

The [Base Card][29] model provides foundational behavior for all cards.  

- `getId()` - returns the card’s ID set by Braze
- `getViewed()` - returns a boolean reflects if the card is read or unread by the user
- `getExtras()` - returns a map of key-value extras for this card
- `setViewed(boolean)` - sets a card's viewed field
- `getCreated()` - returns the unix timestamp of the card’s creation time from Braze dashboard
- `getUpdated()` - returns the unix timestamp of the card’s latest update time from Braze dashboard
- `getCategories()` - returns the list of categories assigned to the card, cards without a category will be assigned ABKCardCategoryNoCategory
- `isInCategorySet(EnumSet)` - returns true if the card belongs to the given category set

#### Banner Image Card
[Banner Image Cards][30] are clickable full-sized images. In addition to the base card properties:

- `getImageUrl()` - returns the URL of the card’s image
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL
- `getDomain()` - returns link text for the property url.

#### Captioned Image Card
[Captioned Image Cards][31] are clickable full-sized images with accompanying descriptive text. In addition to the base card properties:

- `getImageUrl()` - returns the URL of the card’s image
- `getTitle()` - returns the title text for the card
- `getDescription()` - returns the body text for the card
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL
- `getDomain()` - returns the link text for the property url.

#### Text Announcement Card (Captioned Image without Image)
[Text Announcement Cards][32] are clickable cards containing descriptive text. In addition to the base card properties:

- `getTitle()` - returns the title text for the card
- `getDescription()` - returns the body text for the card
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL
- `getDomain()` - returns the link text for the property url.

#### Short News Card
[Short News Cards][33] are clickable cards with images and accompanying descriptive text.  In addition to the base card properties:

- `getImageUrl()` - returns the URL of the card’s image
- `getTitle()` - returns the title text for the card
- `getDescription()` - returns the body text for the card
- `getUrl()` - returns the URL that will be opened after the card is clicked on. It can be a http(s) URL or a protocol URL
- `getDomain()` - returns the link text for the property url.

## Adding a Badge

You can request the number of unread cards at any time by calling:

```java
getUnreadCardCount()
```

See the [Javadoc][17] for more information.

## Refreshing the Feed

You can queue a manual refresh of the Braze News Feed at any time by calling:

```java
Appboy.requestFeedRefresh()
```

See the [Javadoc][16] for more information.

## Key Value Pairs
`Card` objects may optionally carry key value pairs as `extras`. These can be used to send data down along with a `Card` for further handling by the application.

Call the following on a `Card` object to retrieve its extras:

```java
Map<String, String> getExtras()
```

See the [Javadoc][36] for more information.

## GIFs {#gifs-news-feed}

{% include archive/android/gifs.md channel="the News Feed" %}

[1]: {% image_buster /assets/img_archive/UONewsFeed.png %}
[2]: http://developer.android.com/guide/components/fragments.html
[3]: http://developer.android.com/guide/components/fragments.html#Adding "Android Documentation: Fragments"
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[5]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/DroidBoyActivity.java
[6]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#logFeedDisplayed--
[7]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#logClick--
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#logImpression--
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/fireos/news_feed/card_types/#card-types
[14]: {{site.baseurl}}/help/best_practices/news_feed/
[16]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#requestFeedRefresh()
[17]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/events/FeedUpdatedEvent.html#getUnreadCardCount()
[18]: {% image_buster /assets/img_archive/Image27Theming.png %} "Android Feed"
[19]: {% image_buster /assets/img_archive/Image28Theming.png %} "Android Cards"
[20]: {% image_buster /assets/img_archive/Image29Theming.png %} "Android Empty"
[21]: {% image_buster /assets/img_archive/Image30Theming.png %} "Android Network Error"
[23]: {% image_buster /assets/img_archive/android_news_feed.png %}
[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
[26]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/drawable-hdpi/icon_unread.png
[27]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/res/drawable-hdpi/icon_read.png
[28]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/AndroidManifest.xml "AndroidManifest.xml"
[29]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html
[30]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/BannerImageCard.html
[31]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/CaptionedImageCard.html
[32]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/TextAnnouncementCard.html
[33]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/ShortNewsCard.html
[36]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#getExtras()
[37]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/feed/listeners/IFeedClickActionListener.java
[38]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomFeedClickActionListener.java
[39]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/PreferencesActivity.java#L183
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
