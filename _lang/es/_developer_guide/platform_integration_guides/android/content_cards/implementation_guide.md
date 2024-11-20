---
nav_title: Guía de Implementación Avanzada (Opcional)
article_title: Guía de implementación de la tarjeta de contenido para Android (Opcional) 
platform: Android
page_order: 7
description: "Esta guía de implementación avanzada abarca consideraciones sobre códigos de tarjetas de contenido de Android, tres casos de uso creados por nuestro equipo, fragmentos de código que los acompañan y orientaciones sobre el registro de impresiones, clics y descartes."
channel:
  - content cards

---
# Guía de aplicación avanzada (opcional)

> Esta guía de implementación opcional y avanzada abarca consideraciones sobre códigos de tarjetas de contenido, tres casos de uso personalizados creados por nuestro equipo, fragmentos de código que los acompañan y orientaciones sobre el registro de impresiones, clics y descartes. ¡Visita nuestro repositorio de demostraciones Braze [aquí](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Ten en cuenta que esta guía de implementación se centra en una implementación de Kotlin, pero se proporcionan fragmentos de código Java para los interesados.

{% alert important %}
¿Buscas la guía básica de integración del desarrollador de la tarjeta de contenido? Encuéntralo [aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/).<br><br>Encontrarás más información sobre cómo personalizar las tarjetas de contenido en la [Guía de personalización.]({{site.baseurl}}/developer_guide/customization_guides/content_cards)
{% endalert %}

## Consideraciones sobre códigos

### Declaraciones de importación y archivos de ayuda

Al crear tarjetas de contenido, debes exponer el SDK de Braze a través de un único administrador singleton. Este patrón protege el código de tu aplicación de los detalles de implementación de Braze tras una abstracción compartida que tiene sentido para tu caso de uso. También facilita el seguimiento, la depuración y la modificación del código. Puedes encontrar un ejemplo de implementación de administrador [aquí](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt).

### Tarjetas de contenido como objetos personalizados

Tus propios objetos personalizados ya en uso en tu aplicación pueden ampliarse para transportar datos de la tarjeta de contenido, abstrayendo así el origen de los datos en un formato ya comprendido por el código de tu aplicación. Las abstracciones de origen de datos proporcionan flexibilidad para trabajar con diferentes backends de datos de forma intercambiable y concertada. En este ejemplo, hemos definido la clase base abstracta `ContentCardable` para representar tanto nuestros datos existentes (alimentados, en este ejemplo, desde un archivo JSON local) como los nuevos datos alimentados desde el SDK de Braze. La clase base también expone los datos brutos de la tarjeta de contenido para los consumidores que necesiten acceder a la implementación original de `Card`.

Al inicializar instancias de `ContentCardable` desde el SDK de Braze, utilizamos el extra `class_type` para mapear la tarjeta de contenido a una subclase concreta. A continuación, utilizamos los pares clave-valor adicionales establecidos en el panel de Braze para rellenar los campos necesarios.

Una vez que tengas una sólida comprensión de estas consideraciones sobre códigos, consulta nuestros [casos de uso](#sample-use-cases) para empezar a implementar tus propios objetos personalizados.

{% tabs local %}
{% tab Sin dependencias de tarjetas %}
{% subtabs global %}
{% subtab Kotlin %}
**No hay dependencias de `Card` **<br>
`ContentCardData` representa los valores comunes analizados de un `Card`.

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
**No hay dependencias de `Card` **<br>
`ContentCardData` representa los valores comunes analizados de un `Card`.

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
{% tab Objetos personalizados %}
{% subtabs global %}
{% subtab Kotlin %}
**Inicializador de objetos personalizado**<br>
Los metadatos de un `Card` se utilizan para rellenar las variables de tu subclase concreta. Dependiendo de la subclase, puede que necesites extraer valores diferentes durante la inicialización. Los pares clave-valor configurados en el panel de Braze se representan en el diccionario "extras".

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
**Inicializador de objetos personalizado**<br>
Los metadatos de un `Card` se utilizan para rellenar las variables de tu subclase concreta. Dependiendo de la subclase, puede que necesites extraer valores diferentes durante la inicialización. Los pares clave-valor configurados en el panel de Braze se representan en el diccionario "extras".

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
{% tab Tipos identificadores %}
{% subtabs global %}
{% subtab Kotlin %}
**Tipos identificadores**<br>
La enumeración `ContentCardClass` representa el valor `class_type` en el panel Braze y proporciona un método para inicializar la enumeración a partir de las cadenas suministradas por el SDK.

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
**Tipos identificadores**<br>
La enumeración `ContentCardClass` representa el valor `class_type` en el panel Braze y proporciona un método para inicializar la enumeración a partir de las cadenas suministradas por el SDK.

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

## Representación personalizada de tarjetas {#customizing-card-rendering-for-android}

{% tabs local %}
{% tab Sistema de visualización de Android %}

A continuación se indica cómo cambiar la representación de cualquier tarjeta en `recyclerView`. La interfaz `IContentCardsViewBindingHandler` define cómo se representan todas las tarjetas de contenido. Puedes personalizarlo para cambiar lo que quieras:

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

Este código también puede encontrarse aquí [`DefaultContentCardsViewBindingHandler`](https://github.com/braze-inc/braze-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsViewBindingHandler.java).

Y a continuación te explicamos cómo utilizar esta clase:

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

Puedes encontrar más recursos relevantes sobre este tema en este artículo sobre [Vinculación de datos en Android](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4).

{% endtab %}
{% tab Jetpack Compose %}
Para personalizar completamente las tarjetas en Jetpack Compose, crea una función Composable personalizada que haga lo siguiente:

1. Renderiza el Composable y devuelve `true`.
2. No renderiza nada y devuelve `false`.  Cuando se devuelva `false`, Braze renderizará la tarjeta.

En el siguiente ejemplo, la función Composable renderiza las tarjetas `TEXT_ANNOUNCEMENT`, mientras que Braze renderiza automáticamente el resto:

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

## Descarte de tarjeta

La desactivación de la función de deslizar para descartar se hace por tarjeta mediante el método [`card.isDismissibleByUser()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissible-by-user.html) método. Las tarjetas pueden interceptarse antes de mostrarse utilizando el método [`ContentCardsFragment.setContentCardUpdateHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) método.

## Personalización del tema oscuro

Por predeterminado, las vistas de la tarjeta de contenido responderán automáticamente a los cambios del Tema Oscuro en el dispositivo con un conjunto de colores temáticos y cambios de diseño. 

Para anular este comportamiento, anula los valores de `values-night` en `android-sdk-ui/src/main/res/values-night/colors.xml` y `android-sdk-ui/src/main/res/values-night/dimens.xml`.

## Registro de impresiones, clics y descartes

Después de ampliar tus objetos personalizados para que funcionen como tarjetas de contenido, el registro de métricas valiosas como impresiones, clics y rechazos puede hacerse utilizando una clase base `ContentCardable` que haga referencia y proporcione datos a `BrazeManager`.

#### **Componentes de aplicación**<br><br>

{% tabs %}
{% tab Kotlin %}
**Los objetos personalizados llaman a los métodos de registro**<br>
Dentro de tu clase base `ContentCardable`, puedes llamar directamente a `BrazeManager`, si procede. En este ejemplo, la propiedad `cardData` será no nula si el objeto procede de una tarjeta de contenido. 

```kotlin
override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val tile = currentTiles[position]
        tile.logContentCardImpression()
        ...
    }
```

**Recuperar la tarjeta de contenido de `ContentCardId`**<br>
La clase base `ContentCardable` se encarga del trabajo pesado de llamar a `BrazeManager` y pasar el identificador único de la tarjeta de contenido asociada al objeto personalizado.

```kotlin
    fun logContentCardImpression() {
        cardData?.let { BrazeManager.getInstance().logContentCardImpression(it.contentCardId) }
    }
```

**Llamar a las funciones de `Card` **<br>
El [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) puede hacer referencia a dependencias del SDK de Braze, como la lista de matrices de objetos de la tarjeta de contenido, para obtener el `Card` para llamar a nuestros métodos de registro.

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
**Los objetos personalizados llaman a los métodos de registro**<br>
Dentro de tu clase base `ContentCardable`, puedes llamar directamente a `BrazeManager`, si procede. Recuerda que, en este ejemplo, la propiedad `cardData` será no nula si el objeto procede de una tarjeta de contenido. 
```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
        Tile tile = currentTiles.get(position);
        tile.logContentCardImpression();
        ...
    }
```

**Recuperar la tarjeta de contenido de `ContentCardId`**<br>
La clase base `ContentCardable` se encarga del trabajo pesado de llamar a `BrazeManager` y pasar el identificador único de la tarjeta de contenido asociada al objeto personalizado.

```java
    public void logContentCardImpression() {
        if (cardData != null){
            BrazeManager.getInstance().logContentCardImpression(cardData.getContentCardId());
        }
    }
```

**Llamar a las funciones de `Card` **<br>
El [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) puede hacer referencia a dependencias del SDK de Braze, como la lista de matrices de objetos de la tarjeta de contenido, para obtener el `Card` para llamar a nuestros métodos de registro.

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
Para una variante de control Tarjeta de contenido, aún debe instanciarse un objeto personalizado, y la lógica de la interfaz de usuario debe establecer la vista correspondiente del objeto como oculta. El objeto puede entonces registrar una impresión para informar a nuestro análisis de cuándo un usuario habría visto la tarjeta de control.
{% endalert %}

## Archivos de ayuda

{% details Archivo de ayuda ContentCardKey %}
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

