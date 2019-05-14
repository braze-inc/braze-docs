---
nav_title: Customization
page_order: 1
search_rank: 5
platform: Android
---

### Default Styling {#default-styling-for-android}

Braze In App Messages and Content Cards come with a default look and feel that matches the Android standard UI guidelines and provide a seamless experience. You can see these default styles in the [`res/values/styles.xml`][42] file in the Braze SDK distribution.

```xml
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

There are additional relevant resources on this topic available [here](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4).

### Setting a Custom Content Cards Click Listener

You can handle Content Cards clicks manually by setting a custom click listener. This enables use cases such as selectively using the native web browser to open web links.

#### Step 1: Implement a Content Cards Click Listener

Create a class that implements [IContentCardsActionListener][43] and register it with `AppboyContentCardsManager`. Implement the `onContentCardClicked()` method, which will be called when the user clicks a content card.

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

To log a display of the Content Cards, call [`Appboy.logContentCardsDisplayed()`][41].

To log an impression or click on a Card, call [`Card.logClick()`][7] or [`Card.logImpression()`][8] respectively.

## Key-Value Pair.
`Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data down along with a `Card` for further handling by the application.

See the [Javadoc][36] for more information.

## GIFs {#gifs-news-content-cards}

{% include archive/android/gifs.md channel="Content Cards" %}

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
[36]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#getExtras--
[37]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/ui/feed/listeners/IFeedClickActionListener.java
[38]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomFeedClickActionListener.java
[39]: https://github.com/Appboy/appboy-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/PreferencesActivity.java#L183
[40]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[41]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#logContentCardsDisplayed--
[42]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml
[43]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/contentcards/listeners/IContentCardsActionListener.html
