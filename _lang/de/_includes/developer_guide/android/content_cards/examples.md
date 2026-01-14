# Beispiele für die Umsetzung

> Dieser Leitfaden für die optionale und fortgeschrittene Implementierung enthält Code-Überlegungen zu Content-Cards, drei von unserem Team entwickelte Anwendungsfälle, begleitende Code-Snippets sowie Hinweise zur Protokollierung von Impressionen, Klicks und Ausblendungen. Besuchen Sie unser Braze Demo Repository [hier](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Beachten Sie, dass sich dieser Implementierungsleitfaden auf eine Kotlin-Implementierung konzentriert. Für Interessierte werden jedoch Java-Snippets bereitgestellt.

{% alert important %}
Suchen Sie nach dem grundlegenden Leitfaden zur Integration von Content Card Entwicklern? Sie finden ihn [hier]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android).<br><br>Weitere Informationen zum Anpassen von Content-Cards finden Sie im [Anpassungsleitfaden]({{site.baseurl}}/developer_guide/content_cards/).
{% endalert %}

## Code-Überlegungen

### Importanweisungen und Hilfedateien

Wenn Sie Content-Cards erstellen, sollten Sie das Braze SDK über ein einzelnes Manager-Singleton bereitstellen. Dieses Muster schirmt Ihren Anwendungscode von den Braze-Implementierungsdetails hinter einer gemeinsamen Abstraktion ab, die für Ihren Anwendungsfall sinnvoll ist. Außerdem vereinfacht es das Verfolgen, Debuggen und Ändern von Code. Ein Beispiel für die Implementierung eines Managers finden Sie in [`BrazeManager.kt`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) in unserer Demo App auf GitHub.

### Inhaltskarten als benutzerdefinierte Objekte

Sie können die angepassten Objekte, die sich bereits in Ihrer App befinden, erweitern, um Content-Card-Daten zu speichern. So können Sie Ihre Datenquelle in ein Format abstrahieren, das bereits mit Ihrem Code kompatibel ist. Das lässt Ihnen die Flexibilität, mit verschiedenen Daten Backends austauschbar und gemeinsam zu arbeiten.

Im folgenden Beispiel haben wir die abstrakte Basisklasse `ContentCardable` definiert, um sowohl unsere vorhandenen Daten (die aus einer lokalen JSON-Datei stammen) als auch die neuen Daten (die aus dem Braze SDK stammen) darzustellen. Die Basisklasse stellt auch die Content-Card-Rohdaten für Verbraucher bereit, die auf die ursprüngliche Implementierung von `Card` zugreifen müssen.

Bei der Initialisierung von `ContentCardable`-Instanzen aus dem Braze SDK verwenden wir das Extra `class_type`, um die Content-Card einer konkrete Unterklasse zuzuordnen. Wir verwenden dann die zusätzlichen Schlüssel-Wert-Paare, die im Braze-Dashboard festgelegt wurden, um die erforderlichen Felder zu füllen.

Nachdem Sie diese Hinweise zur Code-Anpassung kennengelernt haben, sollten Sie sich unsere [Anwendungsfälle](#sample-use-cases) ansehen, damit Sie mit der Implementierung Ihrer eigenen angepassten Objekte beginnen können.

{% tabs local %}
{% tab Keine Karten-Abhängigkeiten %}
{% subtabs global %}
{% subtab Kotlin %}
**Keine `Card` Abhängigkeiten**<br>
`ContentCardData` stellt die ausgewerteten, gemeinsamen Werte einer `Card` dar.

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
**Keine `Card` Abhängigkeiten**<br>
`ContentCardData` stellt die ausgewerteten, gemeinsamen Werte einer `Card` dar.

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
{% tab Benutzerdefinierte Objekte %}
{% subtabs global %}
{% subtab Kotlin %}
**Benutzerdefinierter Objekt-Initialisierer**<br>
Metadaten aus einer `Card` werden verwendet, um die Variablen der Unterklasse zu füllen. Je nach Unterklasse müssen Sie bei der Initialisierung möglicherweise andere Werte extrahieren. Die im Braze-Dashboard eingerichteten Schlüssel-Wert-Paare sind im Wörterbuch "extras" dargestellt.

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
**Benutzerdefinierter Objekt-Initialisierer**<br>
Metadaten aus einer `Card` werden verwendet, um die Variablen der Unterklasse zu füllen. Je nach Unterklasse müssen Sie bei der Initialisierung möglicherweise andere Werte extrahieren. Die im Braze-Dashboard eingerichteten Schlüssel-Wert-Paare sind im Wörterbuch "extras" dargestellt.

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
{% tab Identifizieren von Typen %}
{% subtabs global %}
{% subtab Kotlin %}
**Identifizieren von Typen**<br>
Der Enum `ContentCardClass` stellt den Wert `class_type` im Braze-Dashboard dar und bietet eine Methode, um den Enum aus den vom SDK bereitgestellten Strings zu initialisieren.

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
**Identifizieren von Typen**<br>
Der Enum `ContentCardClass` stellt den Wert `class_type` im Braze-Dashboard dar und bietet eine Methode, um den Enum aus den vom SDK bereitgestellten Strings zu initialisieren.

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

## Benutzerdefinierte Kartendarstellung {#customizing-card-rendering-for-android}

{% tabs local %}
{% tab Android View System %}

Im Folgenden finden Sie Informationen darüber, wie Sie die Darstellung einer Karte in `recyclerView` ändern können. Die Schnittstelle `IContentCardsViewBindingHandler` definiert, wie alle Content-Cards gerendert werden. Sie können dies nach Belieben ändern:

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

Dieser Code ist auch hier zu finden: [`DefaultContentCardsViewBindingHandler`](https://github.com/braze-inc/braze-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsViewBindingHandler.java).

Und hier sehen Sie, wie Sie diese Klasse verwenden können:

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

Weitere relevante Ressourcen zu diesem Thema finden Sie in diesem Artikel über [Android Data Binding](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4).

{% endtab %}
{% tab Jetpack Compose %}
Um die Karten in Jetpack Compose vollständig anzupassen, erstellen Sie eine angepasste Composable-Funktion, die Folgendes tut:

1. Rendern Sie das Composable und geben Sie `true` zurück.
2. Rendert nichts und gibt `false` zurück.  Wenn `false` zurückgegeben wird, wird Braze die Karte rendern.

Im folgenden Beispiel rendert die Composable-Funktion `TEXT_ANNOUNCEMENT` Karten, während der Rest automatisch von Braze gerendert wird:

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

## Kartenausblendungen

Die Deaktivierung der Funktion, Karten durch eine Wischbewegung auszublenden, erfolgt auf Kartenbasis über die Methode [`card.isDismissibleByUser()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissible-by-user.html). Mit der Methode [`ContentCardsFragment.setContentCardUpdateHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) können Karten vor der Anzeige abgefangen werden.

## Anpassung des Dark Mode-Designs

Standardmäßig reagieren die Inhaltskartenansichten automatisch auf Änderungen des dunklen Themas auf dem Gerät mit einer Reihe von thematischen Farben und Layoutänderungen. 

Um dieses Verhalten außer Kraft zu setzen, überschreiben Sie die Werte `values-night` in `android-sdk-ui/src/main/res/values-night/colors.xml` und `android-sdk-ui/src/main/res/values-night/dimens.xml`.

## Protokollieren von Impressionen, Klicks und Ausblendungen

Nachdem Sie Ihre angepassten Objekte so erweitert haben, dass sie als Content-Cards fungieren, können Sie wertvolle Metriken wie Impressionen, Klicks und Ausblendungen protokollieren, indem Sie eine Basisklasse des Typs `ContentCardable` verwenden, die auf `BrazeManager` verweist und Daten bereitstellt.

#### **Komponenten der Implementierung**<br><br>

{% tabs %}
{% tab Kotlin %}
**Benutzerdefinierte Objekte rufen die Protokollierungsmethoden auf**<br>
Innerhalb der Basisklasse `ContentCardable` können Sie `BrazeManager` bei Bedarf direkt aufrufen. In diesem Beispiel ist die Eigenschaft `cardData` nicht null, wenn das Objekt von einer Content-Card stammte. 

```kotlin
override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val tile = currentTiles[position]
        tile.logContentCardImpression()
        ...
    }
```

**Abrufen von Content-Cards über die `ContentCardId`**<br>
Die Basisklasse `ContentCardable` verarbeitet den Aufruf von `BrazeManager` und die Übergabe des eindeutigen Bezeichners von der Content-Card, die mit dem angepassten Objekt verbunden ist.

```kotlin
    fun logContentCardImpression() {
        cardData?.let { BrazeManager.getInstance().logContentCardImpression(it.contentCardId) }
    }
```

**Aufrufen von `Card`-Funktionen **<br>
[`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) kann auf Abhängigkeiten des Braze SDK verweisen, wie z. B. die Array-Liste von Objekten des Typs "Content-Card", um die `Card` zum Aufrufen unserer Protokollierungsmethoden abzurufen.

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
**Benutzerdefinierte Objekte rufen die Protokollierungsmethoden auf**<br>
Innerhalb der Basisklasse `ContentCardable` können Sie `BrazeManager` bei Bedarf direkt aufrufen. Denken Sie daran, dass die Eigenschaft `cardData` in diesem Beispiel nicht null ist, wenn das Objekt von einer Content-Card stammte. 
```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
        Tile tile = currentTiles.get(position);
        tile.logContentCardImpression();
        ...
    }
```

**Abrufen von Content-Cards über die `ContentCardId`**<br>
Die Basisklasse `ContentCardable` verarbeitet den Aufruf von `BrazeManager` und die Übergabe des eindeutigen Bezeichners von der Content-Card, die mit dem angepassten Objekt verbunden ist.

```java
    public void logContentCardImpression() {
        if (cardData != null){
            BrazeManager.getInstance().logContentCardImpression(cardData.getContentCardId());
        }
    }
```

**Aufrufen von `Card`-Funktionen **<br>
[`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) kann auf Abhängigkeiten des Braze SDK verweisen, wie z. B. die Array-Liste von Objekten des Typs "Content-Card", um die `Card` zum Aufrufen unserer Protokollierungsmethoden abzurufen.

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
Für eine Steuerelementvariante Content Card sollte dennoch ein benutzerdefiniertes Objekt instanziiert werden, und die UI-Logik sollte die entsprechende Ansicht des Objekts als ausgeblendet festlegen. Das Objekt kann dann eine Impression protokollieren, um unsere Analytics darüber zu informieren, wann ein Nutzer die Kontrollkarte gesehen hat.
{% endalert %}

## Hilfsdateien

{% details ContentCardKey Hilfedatei %}
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

