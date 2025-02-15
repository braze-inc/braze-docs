---
nav_title: Guide d’implémentation avancée (facultatif)
article_title: Guide d’implémentation de la carte de contenu pour Android (facultatif) 
platform: Android
page_order: 7
description: "Ce guide d’implémentation avancé couvre les considérations du code de carte de contenu Android, trois cas d’utilisation créés par notre équipe, les extraits de code l’accompagnant et les directives sur l’enregistrement des impressions, des clics et des rejets."
channel:
  - content cards

---
# Guide d’implémentation avancée (facultatif)

> Ce Guide d’implémentation avancé optionnel couvre les considérations du code de carte de contenu, trois cas d’utilisation personnalisés créés par notre équipe, les extraits de code l’accompagnant et les directives sur la journalisation des impressions, des clics et des rejets. Visitez notre dépôt de démonstrations Braze [ici](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Notez que ce guide d’implémentation est centré autour d’une implémentation Kotlin, mais les extraits de code Java sont fournis aux personnes intéressées.

{% alert important %}
Vous recherchez le guide d’intégration de base du développeur de carte de contenu ? Vous le trouverez [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/).<br><br>Vous trouverez de plus amples informations sur la personnalisation des cartes de contenu dans le [Guide de personnalisation.]({{site.baseurl}}/developer_guide/customization_guides/content_cards)
{% endalert %}

## Considérations du code

### Importer des relevés et des fichiers d’aide

Lors de la création de cartes de contenu, vous devez exposer le SDK Braze via un gestionnaire singleton unique. Ce modèle protège le code de votre application des détails de l’implémentation de Braze derrière une abstraction partagée qui est logique pour votre cas d’utilisation. Il facilite également la traçabilité, le débogage et les changements de code. Vous trouverez [ici](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) un exemple de mise en œuvre par un gestionnaire.

### Les cartes de contenu comme objets personnalisés

Vos propres objets personnalisés déjà utilisés dans votre application peuvent être étendus pour transporter des données de carte de contenu, entraînant ainsi l’abstraction de la source des données vers un format déjà compris par le code de votre application. Les abstractions de sources de données permettent de travailler de manière flexible avec des données secondaires différentes de manière interchangeable et de concert. Dans cet exemple, nous avons défini la classe de base abstraite `ContentCardable` pour qu’elle représente à la fois nos données existantes (alimentées, dans cet exemple, à partir d’un fichier JSON local) et les nouvelles données alimentées par le SDK Braze. La classe de base expose également les données brutes de la carte de contenu pour les consommateurs qui ont besoin d’accéder à l’implémentation originale `Card`.

Lors de l'initialisation des instances `ContentCardable` à partir du SDK Braze, nous utilisons le supplément `class_type` pour mapper la carte de contenu à une sous-classe concrète. Nous utilisons ensuite les paires clé-valeur supplémentaires définies dans le tableau de bord de Braze pour renseigner les champs nécessaires.

Une fois que vous aurez acquis une solide compréhension de ces considérations du code, consultez nos [cas d'utilisation](#sample-use-cases) pour commencer à mettre en œuvre vos propres objets personnalisés.

{% tabs local %}
{% tab Pas de dépendance à l'égard des cartes %}
{% subtabs global %}
{% subtab Kotlin %}
**Pas de dépendances de `Card`**<br>
`ContentCardData` représente les valeurs analysées et communes d’un `Card`.

```kotlin
abstract class ContentCardable (){

    var cardData: ContentCardData? = null

    constructor(data:Map<String, Any>):this(){
        cardData = ContentCardData(data[idString] as String,
            ContentCardClass.valueFrom(data[classType] as String),
            data[created] as Long,
            data[dismissable] as Boolean)
    }

    val isContentCard: Boolean
        get() = cardData != null

    fun logContentCardClicked() {
        BrazeManager.getInstance().logContentCardClicked(cardData?.contentCardId)
    }

    fun logContentCardDismissed() {
        BrazeManager.getInstance().logContentCardDismissed(cardData?.contentCardId)
    }

    fun logContentCardImpression() {
        BrazeManager.getInstance().logContentCardImpression(cardData?.contentCardId)
    }
}

data class ContentCardData (var contentCardId: String,
                            var contentCardClassType: ContentCardClass,
                            var createdAt: Long,
                            var dismissable: Boolean)
```
{% endsubtab %}
{% subtab Java %}
**Pas de dépendances de `Card`**<br>
`ContentCardData` représente les valeurs analysées et communes d’un `Card`.

```java
public abstract class ContentCardable{

  private ContentCardData cardData = null;

  public ContentCardable(Map<String, Object> data){
      cardData = new ContentCardData()
      cardData.contentCardId = (String) data.get(idString);
      cardData.contentCardClassType = contentCardClassType.valueOf((String)data.get(classType));
      cardData.createdAt = Long.parseLong((String)data.get(createdAt));
      cardData.dismissable = Boolean.parseBoolean((String)data.get(dismissable));
  }

  public ContentCardable(){

  }

  public boolean isContentCard(){
    return cardData != null;
  }

  public void logContentCardClicked() {
    if (isContentCard()){
      BrazeManager.getInstance().logContentCardClicked(cardData.contentCardId)
    }
  }

  public void logContentCardDismissed() {
    if(isContentCard()){
      BrazeManager.getInstance().logContentCardDismissed(cardData.contentCardId)
    }
  }

  public void logContentCardImpression() {
    if(isContentCard()){
      BrazeManager.getInstance().logContentCardImpression(cardData.contentCardId)
    }
  }
}

public class ContentCardData{
  public String contentCardId;
  public ContentCardClass contentCardClassType;
  public long createdAt;
  public boolean dismissable;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Objets personnalisés %}
{% subtabs global %}
{% subtab Kotlin %}
**Initialisateur d'objet personnalisé**<br>
Les métadonnées d'une `Card` sont utilisées pour renseigner les variables de votre sous-classe concrète. Selon la sous-classe, vous devrez peut-être extraire différentes valeurs pendant l’initialisation. Les paires clé-valeur définies dans le tableau de bord de Braze sont représentées dans le dictionnaire « compléments ».

```kotlin
class Tile: ContentCardable {
    constructor(metadata:Map<String, Any>):super(metadata){
        val extras = metadata[extras] as? Map<String, Any>
        title = extras?.get(Keys.title) as? String
        image = extras?.get(Keys.image) as? String
        detail = metadata[ContentCardable.detail] as? String
        tags = (metadata[ContentCardable.tags] as? String)?.split(",")
        val priceString = extras?.get(Keys.price) as? String
        if (priceString?.isNotEmpty() == true){
            price = priceString.toDouble()
        }
        id = floor(Math.random()*1000).toInt()
    }
  }
```
{% endsubtab %}
{% subtab Java %}
**Initialisateur d'objet personnalisé**<br>
Les métadonnées d'une `Card` sont utilisées pour renseigner les variables de votre sous-classe concrète. Selon la sous-classe, vous devrez peut-être extraire différentes valeurs pendant l’initialisation. Les paires clé-valeur définies dans le tableau de bord de Braze sont représentées dans le dictionnaire « compléments ».

```java
public class Tile extends ContentCardable {

    public Tile(Map<String, Object> metadata){
        super(metadata);
        this.detail = (String) metadata.get(ContentCardable.detail);
        this.tags = ((String)metadata.get(ContentCardable.tags)).split(",");
        if (metadata.containsKey(Keys.extras)){
            Map<String, Object> extras = metadata.get(Keys.extras);
            this.title = (String)extras.get(Keys.title);
            this.price = Double.parseDouble((String)extras.get(Keys.price));
            this.image = (String)extras.get(Keys.image);

        }
    }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Identification des types %}
{% subtabs global %}
{% subtab Kotlin %}
**Identifier les types**<br>
L’enum `ContentCardClass` représente la valeur `class_type` du tableau de bord de Braze et fournit une méthode d’initialisation de l’enum des chaînes de caractères fournies par le SDK.

```kotlin
enum class ContentCardClass{
    AD,
    COUPON,
    NONE,
    ITEM_TILE,
    ITEM_GROUP,
    MESSAGE_FULL_PAGE,
    MESSAGE_WEB_VIEW;

    companion object {
        // This value must be synced with the `class_type` value that has been set up in your
        // Braze dashboard or its type will be set to `ContentCardClassType.none.`
        fun valueFrom(str: String?): ContentCardClass {
            return when(str?.toLowerCase()){
                "coupon_code" -> COUPON
                "home_tile" -> ITEM_TILE
                "group" -> ITEM_GROUP
                "message_full_page" -> MESSAGE_FULL_PAGE
                "message_webview" -> MESSAGE_WEB_VIEW
                "ad_banner" -> AD
                else -> NONE
            }
        }
    }
}
```
{% endsubtab %}
{% subtab Java %}
**Identifier les types**<br>
L’enum `ContentCardClass` représente la valeur `class_type` du tableau de bord de Braze et fournit une méthode d’initialisation de l’enum des chaînes de caractères fournies par le SDK.

```java
enum ContentCardClass {
    AD,
    COUPON,
    NONE,
    ITEM_TILE,
    ITEM_GROUP,
    MESSAGE_FULL_PAGE,
    MESSAGE_WEB_VIEW

    public static valueFrom(String val){
        switch(val.toLowerCase()){
            case "coupon_code":{
                return COUPON;
            }
            case "home_tile":{
                return ITEM_TILE;
            }
            case "group":{
                return ITEM_GROUP;
            }
            case "message_full_page":{
                return MESSAGE_FULL_PAGE;
            }
            case "message_webview":{
                return MESSAGE_WEB_VIEW;
            }
            case "ad_banner":{
                return AD;
            }
            default:{
                return NONE;
            }
        }
    }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Rendu de carte personnalisée {#customizing-card-rendering-for-android}

{% tabs local %}
{% tab Système d'affichage Android %}

Les informations suivantes indiquent comment modifier la manière dont une carte est affichée dans le `recyclerView`. L’interface `IContentCardsViewBindingHandler` définit la façon dont toutes les cartes de contenu sont affichées. Vous pouvez personnaliser cela pour modifier tout ce que vous voulez :

{% subtabs %}
{% subtab JAVA %}

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

{% endsubtab %}
{% subtab KOTLIN %}

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

{% endsubtab %}
{% endsubtabs %}

Ce code peut également être trouvé ici [`DefaultContentCardsViewBindingHandler`](https://github.com/braze-inc/braze-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsViewBindingHandler.java).

Voici comment utiliser cette classe :

{% subtabs %}
{% subtab JAVA %}

```java
IContentCardsViewBindingHandler viewBindingHandler = new DefaultContentCardsViewBindingHandler();

ContentCardsFragment fragment = getMyCustomFragment();
fragment.setContentCardsViewBindingHandler(viewBindingHandler);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val viewBindingHandler = DefaultContentCardsViewBindingHandler()

val fragment = getMyCustomFragment()
fragment.setContentCardsViewBindingHandler(viewBindingHandler)
```

{% endsubtab %}
{% endsubtabs %}

D'autres ressources pertinentes sur ce sujet sont disponibles dans cet article sur la [liaison de données Android](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4).

{% endtab %}
{% tab Jetpack Compose %}
Pour personnaliser entièrement les cartes dans Jetpack Compose, créez une fonction Composable personnalisée faisant ce qui suit :

1. Rendez le Composable et renvoyez `true`.
2. Ne rien rendre et renvoyer `false`.  Lorsque `false` est renvoyé, Braze présente la carte.

Dans l'exemple suivant, la fonction Composable rend `TEXT_ANNOUNCEMENT` cartes, tandis que Braze rend automatiquement le reste :

```kotlin
val myCustomCardRenderer: @Composable ((Card) -> Boolean) = { card ->
    if (card.cardType == CardType.TEXT_ANNOUNCEMENT) {
        val textCard = card as TextAnnouncementCard
        Box(
            Modifier
                .padding(10.dp)
                .fillMaxWidth()
                .background(color = Color.Red)
        ) {
            Text(
                modifier = Modifier
                    .align(Alignment.Center)
                    .fillMaxWidth()
                    .basicMarquee(iterations = Int.MAX_VALUE),
                fontSize = 35.sp,
                text = textCard.description
            )
        }
        true
    } else {
        false
    }
}

ContentCardsList(
    customCardComposer = myCustomCardRenderer
)
```
{% endtab %}
{% endtabs %}

## Fermeture de carte de contenu

La fermeture de la carte de contenu se fait carte par carte via la méthode [`card.isDismissibleByUser()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissible-by-user.html) méthode. Les cartes peuvent être interceptées avant l'affichage à l'aide de la méthode [`ContentCardsFragment.setContentCardUpdateHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) méthode.

## Personnalisation du thème sombre

Par défaut, les vues des cartes de contenu répondent automatiquement aux modifications vers le thème sombre sur l’appareil avec un ensemble de thèmes de couleurs et de modifications de disposition. 

Pour écraser ce comportement, remplacez les valeurs `values-night` dans `android-sdk-ui/src/main/res/values-night/colors.xml` et `android-sdk-ui/src/main/res/values-night/dimens.xml`.

## Enregistrer les impressions, les clics et les rejets

Après avoir étendu vos objets personnalisés pour qu'ils fonctionnent comme des cartes de contenu, l'enregistrement d'indicateurs précieux tels que les impressions, les clics et les fermetures peut être effectué en utilisant une classe de base `ContentCardable` qui fait référence et fournit des données à `BrazeManager`.

#### **Composants d’implémentation**<br><br>

{% tabs %}
{% tab Kotlin %}
**Les objets personnalisés appellent les méthodes de journalisation**<br>
Dans votre classe de base `ContentCardable`, vous pouvez appeler directement `BrazeManager`, le cas échéant. Dans cet exemple, la propriété `cardData` sera non nulle si l'objet provient d'une carte de contenu. 

```kotlin
override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val tile = currentTiles[position]
        tile.logContentCardImpression()
        ...
    }
```

**Récupérer la carte de contenu à partir de `ContentCardId`**<br>
La classe de base `ContentCardable` gère la partie ardue de l’appel de `BrazeManager` et du transfert de l’identifiant unique à partir de la carte de contenu associée à l’objet personnalisé.

```kotlin
    fun logContentCardImpression() {
        cardData?.let { BrazeManager.getInstance().logContentCardImpression(it.contentCardId) }
    }
```

**Appeler les fonctions de `Card`**<br>
Le [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) peut faire référence aux dépendances du SDK Braze, telles que la liste du tableau d'objets de cartes de contenu, afin que `Card` puisse appeler nos méthodes d’enregistrement.

```kotlin
    fun logContentCardClicked(idString: String?) {
        getContentCard(idString)?.logClick()
    }

    fun logContentCardImpression(idString: String?) {
        getContentCard(idString)?.logImpression()
    }

    private fun getContentCard(idString: String?): Card? {
        return cardList.find { it.id == idString }.takeIf { it != null }
    }
```
{% endtab %}
{% tab Java %}
**Les objets personnalisés appellent les méthodes de journalisation**<br>
Dans votre classe de base `ContentCardable`, vous pouvez appeler directement `BrazeManager`, le cas échéant. N'oubliez pas que dans cet exemple, la propriété `cardData` sera non nulle si l'objet provient d'une carte de contenu. 
```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
        Tile tile = currentTiles.get(position);
        tile.logContentCardImpression();
        ...
    }
```

**Récupérer la carte de contenu à partir de `ContentCardId`**<br>
La classe de base `ContentCardable` gère la partie ardue de l’appel de `BrazeManager` et du transfert de l’identifiant unique à partir de la carte de contenu associée à l’objet personnalisé.

```java
    public void logContentCardImpression() {
        if (cardData != null){
            BrazeManager.getInstance().logContentCardImpression(cardData.getContentCardId());
        }
    }
```

**Appeler les fonctions de `Card`**<br>
Le [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) peut faire référence aux dépendances du SDK Braze, telles que la liste du tableau d'objets de cartes de contenu, afin que `Card` puisse appeler nos méthodes d’enregistrement.

```java
    public void logContentCardClicked(String idString) {
        getContentCard(idString).ifPresent(Card::logClick);
    }

    public void logContentCardImpression(String idString) {
        getContentCard(idString).ifPresent(Card::logImpression);
    }

    private Optional<Card> getContentCard(String idString) {
        return cardList.filter(c -> c.id.equals(idString)).findAny();
    }
```
{% endtab %}
{% endtabs %}

{% alert important %}
Pour une carte de contenu de variante de contrôle, un objet personnalisé doit toujours être instancié et la logique de l’interface graphique doit définir la vue correspondante de l’objet comme masquée. L’objet peut ensuite enregistrer une impression pour informer notre analytique du moment où l’utilisateur devrait avoir vu la carte de contrôle.
{% endalert %}

## Fichiers d’aide

{% details Fichier d'aide ContentCardKey %}
{% tabs %}
{% tab Kotlin %}
```kotlin
companion object Keys{
        const val idString = "idString"
        const val created = "created"
        const val classType = "class_type"
        const val dismissable = "dismissable"
        //...
    }
```
{% endtab %}
{% tab Java %}
```java
public static final String IDSTRING = "idString";
public static final String CREATED = "created";
public static final String CLASSTYPE = "class_type";
public static final String DISMISSABLE = "dismissable";
...
```
{% endtab %}
{% endtabs %}
{% enddetails %}

