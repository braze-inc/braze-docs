---
nav_title: Content Cards for Android
permalink: /content_cards_android/

---

# Content Cards for Android

Content Cards are Braze’s new messaging channel which will allow you to create individual messages that appear in a user’s message inbox. This feature is set to, in the future, replace the legacy feature _News Feed channel_, as it provides superior behavior and functionality.

With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, custom card expiration times, card [analytics]({{ site.baseurl }}/content_cards/#content-cards-analytics), and easy coordination with push notifications.

## Example Content Card {#example-content-card-for-android}

![Content Card Example][1]

## Content Cards Integration Overview {#content-cards-integration-for-android}

In Android, Content Cards and the feedback form are implemented as [Fragments][2] that are available in the Braze Android UI project. View [Google's documentation on Fragments][3] for information on how to add a Fragment to an Activity.

The `AppboyContentCardsFragment` class will automatically refresh and display the contents of the Content Cards and log usage analytics. The cards that can appear in a user's ContentCards are set on the Braze dashboard.

## Content Cards Customization {#content-cards-customization-for-android}

### Default Styling {#default-styling-for-android}

The Braze UI elements (IAMs and Content Cards) come with a default look and feel that matches the Android standard UI guidelines and provides a seamless experience. You can see these default styles in the `res/values/style.xml` file in the Braze SDK distribution.

```xml
  <style name="Appboy"/>

  <!-- Content Cards Example -->
  <style name="Appboy.ContentCards.CaptionedImage.Description">
    <item name="android:textColor">@color/com_appboy_description</item>
    <item name="android:textSize">15.0sp</item>
    <item name="android:includeFontPadding">false</item>
    <item name="android:paddingBottom">8.0dp</item>
    <item name="android:layout_marginLeft">10.0dp</item>
    <item name="android:layout_marginRight">10.0dp</item>
    <item name="android:layout_marginTop">8.0dp</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:layout_below">@id/com_appboy_content_cards_captioned_image_card_title_container</item>
  </style>
```

### Overriding Styles {#overriding-styles-for-android}

If you would prefer, you can override these styles to create a look and feel that better suits your app. To override a style, copy it in its entirety to the `styles.xml` file in your own project and make modifications. The whole style must be copied over to your local `styles.xml` file in order for all of the attributes to be correctly set.

#### Correct Style Override {#correct-style-override-for-android}

```xml
<style name="Appboy.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```

#### Incorrect Style Override {#incorrect-style-override-for-android}

```xml
<style name="Appboy.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```

## Content Cards Style Elements {#content-cards-style-elements-for-android}

### Setting A Custom Font {#setting-a-custom-font-for-android}

Braze allows for setting a custom font using the [font family guide][40]. To use it, override a style for cards and use the `fontFamily` attribute to instruct Braze to use your custom font family.

For example, to update the font on all titles for Captioned Image Cards, override the `Appboy.ContentCards.CaptionedImage.Title` style and reference your custom font family. The attribute value should point to a font family in your `res/font` directory.

Here is a truncated example with a custom font family, `my_custom_font_family`, referenced on the last line:

```xml
  <style name="Appboy.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

### Customizing Displayed Card Order {#customizing-displayed-card-order-for-android}

Here's information on how to change how any card is rendered in the recyclerView. The `IContentCardsViewBindingHandler` interface defines how all Content Cards get rendered. You can customize this to change anything you want.

{% tabs %}
{% tab JAVA %}

```java
public class DefaultContentCardsViewBindingHandler implements IContentCardsViewBindingHandler {
  /**
   * A cache for the views used in binding the items in the {@link android.support.v7.widget.RecyclerView}.
   */
  private final Map<CardType, BaseContentCardView> mContentCardViewCache = new HashMap<CardType, BaseContentCardView>();

  @Override
  public ContentCardViewHolder onCreateViewHolder(Context context, List<Card> cards, ViewGroup viewGroup, int viewType) {
    CardType cardType = CardType.fromValue(viewType);
    return getContentCardsViewFromCache(context, cardType).createViewHolder(viewGroup);
  }

  @Override
  public void onBindViewHolder(Context context, List<Card> cards, ContentCardViewHolder viewHolder, int adapterPosition) {
    Card cardAtPosition = cards.get(adapterPosition);
    BaseContentCardView contentCardView = getContentCardsViewFromCache(context, cardAtPosition.getCardType());
    contentCardView.bindViewHolder(viewHolder, cardAtPosition);
  }

  @Override
  public int getItemViewType(Context context, List<Card> cards, int adapterPosition) {
    Card card = cards.get(adapterPosition);
    return card.getCardType().getValue();
  }

  /**
   * Gets a cached instance of a {@link BaseContentCardView} for view creation/binding for a given {@link CardType}.
   * If the {@link CardType} is not found in the cache, then a view binding implementation for that {@link CardType}
   * is created and added to the cache.
   */
  @VisibleForTesting
  BaseContentCardView getContentCardsViewFromCache(Context context, CardType cardType) {
    if (!mContentCardViewCache.containsKey(cardType)) {
      // Create the view here
      BaseContentCardView contentCardView;
      switch (cardType) {
        case BANNER:
          contentCardView = new BannerImageContentCardView(context);
          break;
        case CAPTIONED_IMAGE:
          contentCardView = new CaptionedImageContentCardView(context);
          break;
        case SHORT_NEWS:
          contentCardView = new ShortNewsContentCardView(context);
          break;
        case TEXT_ANNOUNCEMENT:
          contentCardView = new TextAnnouncementContentCardView(context);
          break;
        default:
          contentCardView = new DefaultContentCardView(context);
          break;
      }
      mContentCardViewCache.put(cardType, contentCardView);
    }
    return mContentCardViewCache.get(cardType);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class DefaultContentCardsViewBindingHandler : IContentCardsViewBindingHandler {
  /**
   * A cache for the views used in binding the items in the [android.support.v7.widget.RecyclerView].
   */
  private val mContentCardViewCache = HashMap<CardType, BaseContentCardView<*>>()

  override fun onCreateViewHolder(context: Context, cards: List<Card>, viewGroup: ViewGroup, viewType: Int): ContentCardViewHolder? {
    val cardType = CardType.fromValue(viewType)
    return getContentCardsViewFromCache(context, cardType)?.createViewHolder(viewGroup)
  }

  override fun onBindViewHolder(context: Context, cards: List<Card>, viewHolder: ContentCardViewHolder, adapterPosition: Int) {
    val cardAtPosition = cards[adapterPosition]
    val contentCardView = getContentCardsViewFromCache(context, cardAtPosition.cardType)
    contentCardView?.bindViewHolder(viewHolder, cardAtPosition)
  }

  override fun getItemViewType(context: Context, cards: List<Card>, adapterPosition: Int): Int {
    val card = cards[adapterPosition]
    return card.cardType.value
  }

  /**
   * Gets a cached instance of a [BaseContentCardView] for view creation/binding for a given [CardType].
   * If the [CardType] is not found in the cache, then a view binding implementation for that [CardType]
   * is created and added to the cache.
   */
  @VisibleForTesting
  @NonNull
  internal fun getContentCardsViewFromCache(context: Context, cardType: CardType): BaseContentCardView<*>? {
    if (!mContentCardViewCache.containsKey(cardType)) {
      // Create the view here
      val contentCardView: BaseContentCardView<*>
      when (cardType) {
        CardType.BANNER -> contentCardView = BannerImageContentCardView(context)
        CardType.CAPTIONED_IMAGE -> contentCardView = CaptionedImageContentCardView(context)
        CardType.SHORT_NEWS -> contentCardView = ShortNewsContentCardView(context)
        CardType.TEXT_ANNOUNCEMENT -> contentCardView = TextAnnouncementContentCardView(context)
        else -> contentCardView = DefaultContentCardView(context)
      }
      mContentCardViewCache[cardType] = contentCardView
    }
    return mContentCardViewCache[cardType]
  }
}
```

{% endtab %}
{% endtabs %}

And here's how to use the above class:

{% tabs %}
{% tab JAVA %}

```java
IContentCardsViewBindingHandler viewBindingHandler = DefaultContentCardsViewBindingHandler();

AppboyContentCardsFragment fragment = getMyCustomFragment();
fragment.setContentCardsViewBindingHandler(viewBindingHandler);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val viewBindingHandler = DefaultContentCardsViewBindingHandler()

val fragment = getMyCustomFragment()
fragment.setContentCardsViewBindingHandler(viewBindingHandler)
```

{% endtab %}
{% endtabs %}

There are additional relevant resources on this topic available here (https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4).

### Setting a Custom Content Cards Click Listener

You can handle Content Cards clicks manually by setting a custom Content Cards click listener. This enables use cases such as selectively using the native web browser to open web links.

#### Step 1: Implement a Content Cards Click Listener

Create a class that implements IContentCardsActionListener and register it with `AppboyContentCardsManager`. Implement the `onContentCardClicked()`` method, which will be called when the user clicks a content card.

#### Step 2: Instruct Braze to Use Your Content Card Click Listener

You can see an example of steps 1 and 2 here:

{% tabs %}
{% tab JAVA %}

```java
AppboyContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
AppboyContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endtab %}
{% endtabs %}

### Fully Custom Content Card Display {#fully-custom-content-card-display-for-android}

If you would like to display the Content Cards in a completely custom manner, it is possible to do so by using your own views populated with data from our models. To obtain Braze’s content cards models, you will need to subscribe for content card updates and use the resulting model data to populate your views. You will also need to log analytics on the model objects as users interact with your views.

#### Part 1: Subscribing to Content Card Updates

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
private val mContentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

{% endtab %}
{% endtabs %}

Next, add the following code to subscribe to Content Card updates from Braze, typically inside of your custom Content Cards activity's `Activity.onCreate()`:

{% tabs %}
{% tab JAVA %}

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Appboy.getInstance(this).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all content cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Appboy.getInstance(this).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Appboy.getInstance(this).requestContentCardsRefresh(true);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Appboy.getInstance(this).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
mContentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all content cards
  val allCards = event.allCards

  // Your logic below
}
Appboy.getInstance(this).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Appboy.getInstance(this).requestContentCardsRefresh(true)
```

{% endtab %}
{% endtabs %}

We also recommend unsubscribing when your custom activity moves out of view. Add the following code to your activity's `onDestroy()` lifecycle method:

{% tabs %}
{% tab JAVA %}

```java
Appboy.getInstance(this).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Appboy.getInstance(this).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endtab %}
{% endtabs %}

#### Part 2: Logging Analytics

When using custom views, you will need to log analytics manually as well, since analytics are only handled automatically when using Braze views.

To log a display of the Content Cards, call Appboy.logContentCardsDisplayed()

To log an impression or click on a Card, call [`Card.logClick()`][7] and [`Card.logImpression()`][8] respectively.

## Read/Unread Indicators {#read-indicators-for-android}

Braze allows you to optionally toggle on an Unread/Read indicator on Content Cards.

Unread content cards pic here

### Customizing the Indicators {#customizing-the-indicators-for-android}
These indicators can be customized by altering the values in the style `Appboy.ContentCards.UnreadBar`.

## Card Types {#card-types-for-android}
Braze has 5 unique Content Cards card types which share a base model. Each card type also has additional card-specific properties which are listed below.

#### Base Card {#base-card-for-android}

The [Base Card][29] model provides foundational behavior for all cards.  

|Property | Description |
|---|---|
|`getId()` | Returns the card’s ID set by Braze.|
|`getViewed()` | Returns a boolean reflects if the card is read or unread by the user.|
|`getExtras()` | Returns a map of key-value extras for this card.|
|`getCreated()`  | Returns the unix timestamp of the card’s creation time from Braze.|
|`getIsPinned` | Returns a boolean that reflects whether the card is pinned.|
|`getOpenUriInWebView()`  | Returns a boolean that reflects whether Uris for this card should be opened in Braze's WebView or not.|
|`getExpiredAt()` | Gets the expiration date of the card.|
|`getIsRemoved()` | Returns a boolean that reflects whether the end user has dismissed this card.|
|`getIsDismissible()`  | Returns a boolean that reflects whether the card is pinned.|

#### Banner Image Card {#banner-image-card-for-android}
[Banner Image Cards][30] are clickable full-sized images. In addition to the base card properties:

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card’s image.|
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a http(s) URL or a protocol URL.|
|`getDomain()` | Returns link text for the property URL.|

#### Captioned Image Card {#captioned-image-card-for-android}
[Captioned Image Cards][31] are clickable full-sized images with accompanying descriptive text. In addition to the base card properties:

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card’s image.|
|`getTitle()` | Returns the title text for the card.
|`getDescription()` | Returns the body text for the card.
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a http(s) URL or a protocol URL.
|`getDomain()` | Returns the link text for the property URL.

#### Text Announcement Card (Captioned Image without Image) {#text-Announcement-card-for-android}
[Text Announcement Cards][32] are clickable cards containing descriptive text. In addition to the base card properties:

|Property | Description |
|---|---|
|`getTitle()` | Returns the title text for the card.
|`getDescription()` | Returns the body text for the card.
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a http(s) URL or a protocol URL.
|`getDomain()` | Returns the link text for the property URL.

#### Short News Card
[Short News Cards][33] are clickable cards with images and accompanying descriptive text.  In addition to the base card properties:

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card’s image.
|`getTitle()` | Returns the title text for the card.
|`getDescription()` | Returns the body text for the card.
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a http(s) URL or a protocol URL.
|`getDomain()` | Returns the link text for the property URL.

#### Cross Promotion Small Card
[Cross-Promotion Small Cards][34] link to items in the Google Play Store or Kindle Store. In addition to the base card properties:

|Property | Description |
|---|---|
|`getTitle()` | Returns the title text for the card. This will be the promoted item’s name.
|`getSubtitle()` | Returns the text of the category of the promoted item.
|`getImageUrl()` | Returns property is the URL of the card’s image.
|`getPackage()` | Returns the package name of the promoted item.
|`getRating()` | Returns the rating of the promoted app. This property will be 0.0 unless the promoted item is an app, in which case the rating will be in the range of [0.0, 5.0];
|`getPrice()` | Returns the price of the promoted app.
|`getReviewCount()` | Returns the number of reviews of the promoted app. This property will be 0 unless the promoted item is an app.
|`getCaption()` | Returns the text that will be displayed in the tag on the top of the small cross promotion card.
|`getUrl()` | Returns the URL of the promoted item which leads to the item’s App Store page.

## Adding a Badge

You can request the number of unread cards at any time by calling:

{% tabs %}
{% tab JAVA %}

```java
Appboy.getInstance(context).getContentCardUnviewedCount()
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Appboy.getInstance(context).contentCardUnviewedCount
```

{% endtab %}
{% endtabs %}

## Refreshing Content Cards

You can queue a manual refresh of the Braze Content Cards at any time by calling:

{% tabs %}
{% tab JAVA %}

```java
Appboy.getInstance(context).requestContentCardsRefresh()
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Appboy.getInstance(context).requestContentCardsRefresh()
```

{% endtab %}
{% endtabs %}

## Key-Value Pairs
`Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data down along with a `Card` for further handling by the application.

See the [Javadoc][36] for more information.

## GIFs {#gifs-news-content-cards}

{% include archive/android/gifs.md channel="Content Cards" %}

[1]:{% image_buster /assets/img_archive/contentcard.png %}
[2]: http://developer.android.com/guide/components/fragments.html
[3]: http://developer.android.com/guide/components/fragments.html#Adding "Android Documentation: Fragments"
[4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[5]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/DroidBoyActivity.java
[6]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#logFeedDisplayed--
[7]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#logClick--
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#logImpression--
[9]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/news_feed/#card-types
[14]: {{ site.baseurl }}/help/best_practices/news_feed/
[16]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#requestFeedRefresh()
[18]: {% image_buster /assets/img_archive/Image27Theming.png %} "Android Feed"
[19]: {% image_buster /assets/img_archive/Image28Theming.png %} "Android Cards"
[20]: {% image_buster /assets/img_archive/Image29Theming.png %} "Android Empty"
[21]: {% image_buster /assets/img_archive/Image30Theming.png %} "Android Network Error"
[22]: {% image_buster /assets/img_archive/sample_news_feed.png %}
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
[34]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/CrossPromotionSmallCard.html
[36]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#getExtras--
[37]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/feed/listeners/IFeedClickActionListener.java
[38]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomFeedClickActionListener.java
[39]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/PreferencesActivity.java#L183
[40]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
