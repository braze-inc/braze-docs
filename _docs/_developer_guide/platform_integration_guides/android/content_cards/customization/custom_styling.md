---
nav_title: Custom Styling
article_title: Custom Content Card Styling for Android and FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "This article covers customization options for your Content Cards in your Android or FireOS application."
channel:
  - content cards

---

# Custom styling {#content-cards-style-elements-for-android}

Braze in-app messages and Content Cards come with a default look and feel that matches the Android standard UI guidelines and provide a seamless experience. You can see these default styles in the [`res/values/styles.xml`][42] file in the Braze SDK distribution:

```xml
  <!-- Content Cards Example -->
  <style name="Braze.ContentCards.CaptionedImage.Description">
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

If you would prefer, you can override these styles to create a look and feel that better suits your app. To override a style, copy it in its entirety to the `styles.xml` file in your project and make modifications. The whole style must be copied over to your local `styles.xml` file for all attributes to be correctly set.

{% tabs local %}
{% tab Correct style override %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```
{% endtab %}
{% tab Incorrect style override %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```
{% endtab %}
{% endtabs %}

## Custom font {#setting-a-custom-font-for-android}

Braze allows setting a custom font using the [font family guide][40]. To use it, override a style for cards and use the `fontFamily` attribute to instruct Braze to use your custom font family.

For example, to update the font on all titles for captioned image cards, override the `Appboy.ContentCards.CaptionedImage.Title` style and reference your custom font family. The attribute value should point to a font family in your `res/font` directory.

Here is a truncated example with a custom font family, `my_custom_font_family`, referenced on the last line:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

## Custom pinned icon {#setting-a-custom-pinned-icon-for-android}

To set a custom pinned icon, override the `Appboy.ContentCards.PinnedIcon` style. Your custom image asset should be declared in the `android:src` element.

## Custom card rendering {#customizing-card-rendering-for-android}

The following lists information on how to change how any card is rendered in the `recyclerView`. The `IContentCardsViewBindingHandler` interface defines how all Content Cards get rendered. You can customize this to change anything you want:

{% tabs %}
{% tab JAVA %}

```java
public class DefaultContentCardsViewBindingHandler implements IContentCardsViewBindingHandler {
  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  public static final Parcelable.Creator<DefaultContentCardsViewBindingHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsViewBindingHandler>() {
    public DefaultContentCardsViewBindingHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsViewBindingHandler();
    }

    public DefaultContentCardsViewBindingHandler[] newArray(int size) {
      return new DefaultContentCardsViewBindingHandler[size];
    }
  };

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

  // Parcelable interface method
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // Retaining views across a transition could lead to a
    // resource leak so the parcel is left unmodified
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class DefaultContentCardsViewBindingHandler : IContentCardsViewBindingHandler {
  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  val CREATOR: Parcelable.Creator<DefaultContentCardsViewBindingHandler?> = object : Parcelable.Creator<DefaultContentCardsViewBindingHandler?> {
    override fun createFromParcel(`in`: Parcel): DefaultContentCardsViewBindingHandler? {
      return DefaultContentCardsViewBindingHandler()
    }

    override fun newArray(size: Int): Array<DefaultContentCardsViewBindingHandler?> {
      return arrayOfNulls(size)
    }
  }

  /**
    * A cache for the views used in binding the items in the [RecyclerView].
    */
  private val mContentCardViewCache: MutableMap<CardType, BaseContentCardView<*>?> = HashMap()

  override fun onCreateViewHolder(context: Context?, cards: List<Card?>?, viewGroup: ViewGroup?, viewType: Int): ContentCardViewHolder? {
    val cardType = CardType.fromValue(viewType)
    return getContentCardsViewFromCache(context, cardType)!!.createViewHolder(viewGroup)
  }

  override fun onBindViewHolder(context: Context?, cards: List<Card>, viewHolder: ContentCardViewHolder?, adapterPosition: Int) {
    if (adapterPosition < 0 || adapterPosition >= cards.size) {
      return
    }
    val cardAtPosition = cards[adapterPosition]
    val contentCardView = getContentCardsViewFromCache(context, cardAtPosition.cardType)
    if (viewHolder != null) {
      contentCardView!!.bindViewHolder(viewHolder, cardAtPosition)
    }
  }

  override fun getItemViewType(context: Context?, cards: List<Card>, adapterPosition: Int): Int {
    if (adapterPosition < 0 || adapterPosition >= cards.size) {
      return -1
    }
    val card = cards[adapterPosition]
    return card.cardType.value
  }

  /**
    * Gets a cached instance of a [BaseContentCardView] for view creation/binding for a given [CardType].
    * If the [CardType] is not found in the cache, then a view binding implementation for that [CardType]
    * is created and added to the cache.
    */
  @VisibleForTesting
  fun getContentCardsViewFromCache(context: Context?, cardType: CardType): BaseContentCardView<Card>? {
    if (!mContentCardViewCache.containsKey(cardType)) {
      // Create the view here
      val contentCardView: BaseContentCardView<*> = when (cardType) {
        CardType.BANNER -> BannerImageContentCardView(context)
        CardType.CAPTIONED_IMAGE -> CaptionedImageContentCardView(context)
        CardType.SHORT_NEWS -> ShortNewsContentCardView(context)
        CardType.TEXT_ANNOUNCEMENT -> TextAnnouncementContentCardView(context)
        else -> DefaultContentCardView(context)
      }
      mContentCardViewCache[cardType] = contentCardView
    }
    return mContentCardViewCache[cardType] as BaseContentCardView<Card>?
  }

  // Parcelable interface method
  override fun describeContents(): Int {
    return 0
  }

  // Parcelable interface method
  override fun writeToParcel(dest: Parcel?, flags: Int) {
    // Retaining views across a transition could lead to a
    // resource leak so the parcel is left unmodified
  }
}
```

{% endtab %}
{% endtabs %}

This code can also be found here [`DefaultContentCardsViewBindingHandler`][56].

And here's how to use the above class:

{% tabs %}
{% tab JAVA %}

```java
IContentCardsViewBindingHandler viewBindingHandler = new DefaultContentCardsViewBindingHandler();

ContentCardsFragment fragment = getMyCustomFragment();
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

Additional relevant resources on this topic are available in this article on [Android Data Binding](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4).

## Dark theme customization

By default, Content Card views will automatically respond to Dark Theme changes on the device with a set of themed colors and layout changes. 

To override this behavior, override the `values-night` values in `android-sdk-ui/src/main/res/values-night/colors.xml` and `android-sdk-ui/src/main/res/values-night/dimens.xml`.

[36]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/get-extras.html
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[41]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/log-content-cards-displayed.html
[42]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml
[44]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html
[45]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html
[46]: https://github.com/Appboy/appboy-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsUpdateHandler.java
[49]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
[56]: https://github.com/Appboy/appboy-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsViewBindingHandler.java
