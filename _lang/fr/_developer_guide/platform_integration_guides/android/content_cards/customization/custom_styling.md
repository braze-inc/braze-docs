---
nav_title: Style personnalisé
article_title: Style de carte de contenu personnalisé pour Android et FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Cet article couvre les options de personnalisation pour vos cartes de contenu dans votre application Android ou FireOS."
channel:
  - cartes de contenu

---

# Style personnalisé {#content-cards-style-elements-for-android}

Les messages in-app et les cartes de contenu de Braze sont dotés d’un aspect et d’une convivialité par défaut qui correspondent aux directives de l’IU standard d’Android et offrent une expérience transparente. Vous pouvez voir ces styles par défaut dans le fichier [`res/values/styles.xml`][42] dans la distribution du SDK Braze :

```xml
  <!-- Content Cards Example -->
  <style name="Braze.ContentCards.CaptionedImage.Description">
    <item name="android:textColor">@color/com_braze_description</item>
    <item name="android:textSize">15.0sp</item>
    <item name="android:includeFontPadding">false</item>
    <item name="android:paddingBottom">8.0dp</item>
    <item name="android:layout_marginLeft">10.0dp</item>
    <item name="android:layout_marginRight">10.0dp</item>
    <item name="android:layout_marginTop">8.0dp</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:layout_below">@id/com_braze_content_cards_captioned_image_card_title_container</item>
  </style>
```

Si vous préférez, vous pouvez écraser ces styles pour créer un aspect et une convivialité qui conviennent mieux à votre application. Pour remplacer un style, copiez-le dans son intégralité dans le fichier `styles.xml` dans votre projet et apportez des modifications. Le style entier doit être copié sur votre fichier `styles.xml` local pour que tous les attributs soient correctement définis.

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

## Police personnalisée {#setting-a-custom-font-for-android}

Braze permet de définir une police personnalisée à l’aide du [guide de la famille de polices][40]. Pour l’utiliser, remplacez un style pour les cartes et utilisez l’attribut `fontFamily` pour indiquer à Braze d’utiliser votre famille de polices personnalisée.

Par exemple, pour mettre à jour la police sur tous les titres des cartes image sous-titrées, remplacez le style `Braze.ContentCards.CaptionedImage.Title` et référencez votre famille de polices personnalisée. La valeur d’attribut doit pointer vers une famille de polices dans votre répertoire `res/font`.

Voici un exemple tronqué avec une famille de polices personnalisée, `my_custom_font_family`, référencé sur la dernière ligne :

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

## Icône épinglée personnalisée{#setting-a-custom-pinned-icon-for-android}

Pour définir une icône épinglée personnalisée, remplacez le style `Braze.ContentCards.PinnedIcon`. Votre actif d’image personnalisé doit être déclaré dans l’élément `android:src`.

## Rendu carte personnalisée{#customizing-card-rendering-for-android}

Les informations suivantes indiquent comment modifier la manière dont une carte est affichée dans le `recyclerView`. L’interface `IContentCardsViewBindingHandler` définit la façon dont toutes les cartes de contenu sont affichées. Vous pouvez personnaliser cela pour modifier tout ce que vous voulez :

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
  public ContentCardViewHolder onCreateViewHolder(Context context, List<? extends Card> cards, ViewGroup viewGroup, int viewType) {
    CardType cardType = CardType.fromValue(viewType);
    return getContentCardsViewFromCache(context, cardType).createViewHolder(viewGroup);
  }

  @Override
  public void onBindViewHolder(Context context, List<? extends Card> cards, ContentCardViewHolder viewHolder, int adapterPosition) {
    Card cardAtPosition = cards.get(adapterPosition);
    BaseContentCardView contentCardView = getContentCardsViewFromCache(context, cardAtPosition.getCardType());
    contentCardView.bindViewHolder(viewHolder, cardAtPosition);
  }

  @Override
  public int getItemViewType(Context context, List<? extends Card> cards, int adapterPosition) {
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

Ce code est également disponible ici [`DefaultContentCardsViewBindingHandler`][56].

Voici comment utiliser cette classe :

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

Des ressources pertinentes supplémentaires sur cette rubrique sont disponibles dans cet article sur la [Liaison des données Android](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4).

## Personnalisation du thème sombre

Par défaut, les vues des cartes de contenu répondent automatiquement aux modifications vers le thème sombre sur l’appareil avec un ensemble de thème de couleurs et de modifications de disposition. 

Pour écraser ce comportement, remplacez les valeurs `values-night` dans `android-sdk-ui/src/main/res/values-night/colors.xml` et `android-sdk-ui/src/main/res/values-night/dimens.xml`.

[36]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/get-extras.html
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[42]: https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml
[44]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html
[45]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html
[46]: https://github.com/braze-inc/braze-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsUpdateHandler.java
[49]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
[56]: https://github.com/braze-inc/braze-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsViewBindingHandler.java
