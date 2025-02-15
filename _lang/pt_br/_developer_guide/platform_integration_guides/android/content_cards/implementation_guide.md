---
nav_title: Guia de implementação avançada (opcional)
article_title: Guia de implementação do cartão de conteúdo para Android (opcional) 
platform: Android
page_order: 7
description: "Este guia de implementação avançada aborda considerações sobre o código do cartão de conteúdo do Android, três casos de uso criados por nossa equipe, acompanhando trechos de código e orientações sobre o registro de impressões, cliques e descartes de cartão."
channel:
  - content cards

---
# Guia de implementação avançada (opcional)

> Este guia de implementação opcional e avançado aborda considerações sobre o código do Content Card, três casos de uso personalizados criados por nossa equipe, acompanhando trechos de código e orientações sobre o registro de impressões, cliques e descartes de cartão. Visite nosso Repositório de Demonstrações Braze [aqui](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Note que este guia de implementação está centrado em uma implementação Kotlin, mas são fornecidos trechos em Java para os interessados.

{% alert important %}
Está procurando o guia básico de integração do desenvolvedor do cartão de conteúdo? Encontre-o [aqui]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/).<br><br>Mais informações sobre a personalização dos cartões de conteúdo podem ser encontradas no [Guia de personalização.]({{site.baseurl}}/developer_guide/customization_guides/content_cards)
{% endalert %}

## Considerações sobre o código

### Importar instruções e arquivos auxiliares

Ao criar cartões de conteúdo, você deve expor o SDK da Braze por meio de um único singleton do gerenciador. Esse padrão protege o código do seu aplicativo dos detalhes de implementação do Braze por meio de uma abstração compartilhada que faz sentido para o seu caso de uso. Isso também facilita o rastreamento, a depuração e a alteração do código. Um exemplo de implementação de gerenciador pode ser encontrado [aqui](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt).

### Cartões de conteúdo como objetos personalizados

Seus próprios objetos personalizados já em uso em seu aplicativo podem ser estendidos para transportar dados do cartão de conteúdo, abstraindo assim a fonte dos dados em um formato já compreendido pelo código do aplicativo. As abstrações de fontes de dados oferecem flexibilidade para trabalhar com diferentes backends de dados de forma intercambiável e em conjunto. Neste exemplo, definimos a classe base abstrata `ContentCardable` para representar nossos dados existentes (alimentados, neste exemplo, por um arquivo JSON local) e os novos dados alimentados pelo SDK da Braze. A classe base também expõe os dados brutos do cartão de conteúdo para os consumidores que precisam acessar a implementação original do `Card`.

Ao inicializar instâncias `ContentCardable` do SDK da Braze, usamos o `class_type` extra para mapear o cartão de conteúdo para uma subclasse concreta. Em seguida, usamos os outros pares de chave/valor definidos no dashboard da Braze para preencher os campos necessários.

Depois de entender bem essas considerações de código, confira nossos [casos de uso](#sample-use-cases) para começar a implementar seus próprios objetos personalizados.

{% tabs localização %}
{% tab Sem dependências de cartão %}
{% subtabs global %}
{% subtab Kotlin %}
**Não há dependências de `Card`**<br>
`ContentCardData` representa os valores comuns analisados de um `Card`.

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
**Não há dependências de `Card`**<br>
`ContentCardData` representa os valores comuns analisados de um `Card`.

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
**Inicializador de objeto personalizado**<br>
Os metadados de um `Card` são usados para preencher as variáveis de sua subclasse concreta. Dependendo da subclasse, talvez você precise extrair valores diferentes durante a inicialização. Os pares de valores-chave configurados no dashboard do Braze são representados no dicionário "extras".

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
**Inicializador de objeto personalizado**<br>
Os metadados de um `Card` são usados para preencher as variáveis de sua subclasse concreta. Dependendo da subclasse, talvez você precise extrair valores diferentes durante a inicialização. Os pares de valores-chave configurados no dashboard do Braze são representados no dicionário "extras".

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
{% tab Identificação de tipos %}
{% subtabs global %}
{% subtab Kotlin %}
**Identificação de tipos**<br>
O enum `ContentCardClass` representa o valor `class_type` no dashboard da Braze e fornece um método para inicializar o enum a partir das strings fornecidas pelo SDK.

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
**Identificação de tipos**<br>
O enum `ContentCardClass` representa o valor `class_type` no dashboard da Braze e fornece um método para inicializar o enum a partir das strings fornecidas pelo SDK.

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

## Renderização de cartões personalizados {#customizing-card-rendering-for-android}

{% tabs localização %}
{% tab Sistema de visualização Android %}

A seguir, listamos informações sobre como alterar a forma como qualquer cartão é renderizado no site `recyclerView`. A interface `IContentCardsViewBindingHandler` define como todos os cartões de conteúdo são renderizados. Você pode personalizar isso para alterar o que quiser:

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

Esse código também pode ser encontrado aqui [`DefaultContentCardsViewBindingHandler`](https://github.com/braze-inc/braze-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsViewBindingHandler.java).

E aqui está como usar essa classe:

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

Outros recursos relevantes sobre esse tópico estão disponíveis neste artigo sobre [Vinculação de dados do Android](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4).

{% endtab %}
{% tab Jetpack Compose %}
Para personalizar cartões no Jetpack Compose, crie uma função Composable personalizada da seguinte forma:

1. Renderize a Composable e retorne `true`.
2. Não renderiza nada e retorna `false`.  Quando `false` for retornado, a Braze renderizará o cartão.

No exemplo a seguir, a função Composable renderiza os cartões `TEXT_ANNOUNCEMENT`, enquanto a Braze renderiza automaticamente o restante:

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

## Descarte de cartão

A desativação da funcionalidade de passar o dedo para recusar é feita por cartão por meio do método [`card.isDismissibleByUser()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissible-by-user.html) método. Os cartões podem ser interceptados antes da exibição usando o método [`ContentCardsFragment.setContentCardUpdateHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) método.

## Personalização do tema escuro

Por padrão, as exibições do cartão de conteúdo responderão automaticamente às alterações do tema escuro no dispositivo com um conjunto de cores temáticas e alterações de layout. 

Para substituir esse comportamento, substitua os valores de `values-night` em `android-sdk-ui/src/main/res/values-night/colors.xml` e `android-sdk-ui/src/main/res/values-night/dimens.xml`.

## Registro de impressões, cliques e demissões

Depois de estender seus objetos personalizados para funcionar como cartões de conteúdo, o registro de métricas valiosas, como impressões, cliques e descartes de cartões, pode ser feito usando uma classe base `ContentCardable` que faz referência e fornece dados para o `BrazeManager`.

#### **Componentes de implementação**<br><br>

{% tabs %}
{% tab Kotlin %}
**Os objetos personalizados chamam os métodos de registro**<br>
Em sua classe base `ContentCardable`, você pode chamar o `BrazeManager` diretamente, se for o caso. Nesse exemplo, a propriedade `cardData` será não nula se o objeto tiver vindo de um cartão de conteúdo. 

```kotlin
override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val tile = currentTiles[position]
        tile.logContentCardImpression()
        ...
    }
```

**Recupere o cartão de conteúdo do `ContentCardId`**<br>
A classe de base `ContentCardable` faz o trabalho pesado de chamar o `BrazeManager` e passar o identificador exclusivo do cartão de conteúdo associado ao objeto personalizado.

```kotlin
    fun logContentCardImpression() {
        cardData?.let { BrazeManager.getInstance().logContentCardImpression(it.contentCardId) }
    }
```

**Chame as funções `Card` **<br>
O [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) pode fazer referência às dependências do SDK da Braze, como a lista de vetores de objetos do cartão de conteúdo, para obter o `Card` e chamar os métodos de registro da Braze.

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
**Os objetos personalizados chamam os métodos de registro**<br>
Em sua classe base `ContentCardable`, você pode chamar o `BrazeManager` diretamente, se for o caso. Lembre-se: nesse exemplo, a propriedade `cardData` será não nula se o objeto tiver vindo de um cartão de conteúdo. 
```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
        Tile tile = currentTiles.get(position);
        tile.logContentCardImpression();
        ...
    }
```

**Recupere o cartão de conteúdo do `ContentCardId`**<br>
A classe de base `ContentCardable` faz o trabalho pesado de chamar o `BrazeManager` e passar o identificador exclusivo do cartão de conteúdo associado ao objeto personalizado.

```java
    public void logContentCardImpression() {
        if (cardData != null){
            BrazeManager.getInstance().logContentCardImpression(cardData.getContentCardId());
        }
    }
```

**Chame as funções `Card` **<br>
O [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) pode fazer referência às dependências do SDK da Braze, como a lista de vetores de objetos do cartão de conteúdo, para obter o `Card` e chamar os métodos de registro da Braze.

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
Para uma variante de controle Content Card, um objeto personalizado ainda deve ser instanciado, e a lógica da interface do usuário deve definir a exibição correspondente do objeto como oculta. O objeto pode então registrar uma impressão para informar nossa análise de dados sobre quando um usuário teria visto o cartão de controle.
{% endalert %}

## Arquivos auxiliares

{% details Arquivo auxiliar do ContentCardKey %}
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

