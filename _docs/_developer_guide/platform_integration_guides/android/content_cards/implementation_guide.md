---
nav_title: Advanced Implementation (Optional)
platform: Android
page_order: 7
description: "This advanced implementation guide covers Android Content Card code considerations, three use cases built by our team, accompanying code snippets, and guidance on logging impressions, clicks, and dismissals."
channel:
  - content cards

---

{% alert important %}
Looking for the out-of-the-box Content Card developer integration guide? Find it [here]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_model/).
{% endalert %}

# Content Card Implementation Guide

> This optional and advanced implementation guide covers Content Card code considerations, three custom use cases built by our team, accompanying code snippets, and guidance on logging impressions, clicks, and dismissals. Visit our Braze Demo Repository [here](FIXME)! Please note that this implementation guide is centered around a Kotlin implementation, but Java snippets are provided for those interested.

## Code Considerations

### Import Statements and Helper Files

When building out Content Cards, you should expose the Braze SDK via a single manager singleton. This pattern shields your applicaiton code from the Braze implementation details behind a shared abstraction that makes sense for your use case. It also makes it easier to track, debug, and alter code. An example manager implementation can be found [here](FIXME).

### Content Cards as Custom Objects

Your own custom objects already in use in your application can be extended to carry Content Card data, thereby abstracting the source of the data into a format that is already understood by your application code. Data source abstractions such as this provide flexibility to work with different data backends interchangeably and in concert. In this example, we've defined the `ContentCardable` abstract base class to represent both our existing data (fed, in this example, from a local JSON file) and the new data, fed from the Braze SDK. The base class also exposes the raw Content Card data for consumers that need to access the original `Card` impementation.

When initializing `ContentCardable` instances from the Braze SDK, we utilize the `class_type` extra to map the Content Card to a concrete subclass. We then use the additional key/value pairs set within the Braze Dashboard to populate the necessary fields.

Once you have a solid understanding of these code considerations, check out our [use cases](#sample-use-cases) below to get started implementing your own custom objects.

{% tabs local %}
{% tab No Card Dependencies %}
{% subtabs global %}
{% subtab Kotlin %}
__No `Card` Dependencies__<br>
`ContentCardData` represents the parsed out, common values of an `Card`.

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
__No `Card` Dependencies__<br>
`ContentCardData` represents the parsed out, common values of an `Card`.

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
{% tab Custom Objects %}
{% subtabs global %}
{% subtab Kotlin %}
__Custom Object Initializer__<br>
MetaData from a `Card` is used to populate your concrete subclass's variables. Depending on the subclass, you may need to extract different values during initialization. The key value pairs set up in the Braze Dashboard are represented in the “extras” dictionary.

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
__Custom Object Initializer__<br>
MetaData from a `Card` is used to populate your concrete subclass's variables. Depending on the subclass, you may need to extract different values during initialization. The key value pairs set up in the Braze Dashboard are represented in the “extras” dictionary.

```java
TODO
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Identifying Types %}
{% subtabs global %}
{% subtab Kotlin %}
__Identifying Types__<br>
The `ContentCardClass` enum represents the `class_type` value in the Braze Dashboard and provides a method to initialize the enum from the Strings supplied by the SDK.

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
__Identifying Types__<br>
The `ContentCardClass` enum represents the `class_type` value in the Braze Dashboard and provides a method to initialize the enum from the Strings supplied by the SDK.

```java
TODO
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Sample Use Cases

There are three sample customer use cases provided. Each sample has video walkthroughs, code snippets, and a look into how Content Card variables may look and be used in the Braze dashboard:
- [Content Cards As Supplemental Content](#content-cards-as-supplemental-content)
- [Content Cards in a Message Center](#content-cards-in-a-message-center)
- [Interactive Content Cards](#interactive-content-cards)

### Content Cards as Supplemental Content

You can seamlessly blend Content Cards into an existing feed, allowing data from multiple feeds to load simultaneously. This creates a cohesive, harmonious experience with Braze Content Cards and existing feed content.

#### __Load Content Cards Alongside Existing Content__<br><br>
{% tabs %}
{% tab Kotlin %}
__Load the data into a merged adapter__<br>
In this example, we are loading primary data from a JSON resource file stored in the app, but in practice, you could load this data from anywhere.

```kotlin
class CardableTileDataProvider(private var ctx: Context) : BaseAdapter(),
    ContentCardableObserver {

    private var localTiles: List<Tile> = mutableListOf()
    private var currentTiles: List<Tile> = listOf()

    init {
        BrazeManager.getInstance().registerContentCardableObserver(this)   //register for ContentCard updates
        localTiles = Gson().fromJson(
            InputStreamReader(ctx.resources.openRawResource(R.raw.tiles)),
            TileList::class.java
        ).tiles                                                            //load the local resource file
        currentTiles = localTiles
    }

    override fun getCount(): Int {
      return currentTiles.size
    }

    override fun getItem(position: Int): Any {
        return currentTiles[position]
    }

    override fun getItemId(position: Int): Long {
        return currentTiles[position].id.toLong()
    }

```
{% endtab %}
{% tab Java %}
__Load the data into a merged adapter__<br>
In this example, we are loading primary data from a JSON resource file stored in the app, but in practice, you could load this data from anywhere.

```java
TODO
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
__Receive Content Card updates from the Braze SDK__<br>
A custom observer is used to notify any interested parties about Content Card updates. 

```kotlin
interface ContentCardableObserver {
    fun onContentCardsChanged(cards: List<ContentCardable>)
}

class CardableTileDataProvider(private var ctx: Context) : BaseAdapter(),
    ContentCardableObserver {
      //...
    override fun onContentCardsChanged(cards: List<ContentCardable>) {
        MainScope().launch { updateCards(cards) }
    }
```
{% endtab %}
{% tab Java %}
__Receive Content Card updates from the Braze SDK__<br>
A custom observer is used to notify any interested parties about Content Card updates. 

```java
TODO
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
__Merge the data__<br>
The corresponding `[Tile]` array will be seamlessly blended with an array of Content Cards. Because there are multiple content card subclasses that we could be seeing, we also filter out _only_ the instances of `Tile`

```kotlin
class CardableTileDataProvider(private var ctx: Context) : BaseAdapter(),
    ContentCardableObserver {
      //...
    private fun updateCards(cards: List<ContentCardable>) {
        currentTiles = cards.filterIsInstance<Tile>() + localTiles
        notifyDataSetChanged()
    }
```
{% endtab %}
{% tab Java %}
__Merge the data__<br>
The corresponding `[Tile]` array will be seamlessly blended with an array of Content Cards. Because there are multiple content card subclasses that we could be seeing, we also filter out _only_ the instances of `Tile`

```java
TODO
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Kotlin %}
__Present a unified stream of data__<br>
Because the adapter uses the merged list to supply data model information to the `ListView`, both the Content Card-based data and the API(or JSON)-based data will be displayed in unison to the user.

```kotlin
    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val binding: CardCellLayoutBinding = if (convertView != null) {
            convertView.tag as CardCellLayoutBinding
        } else {
            CardCellLayoutBinding.inflate(LayoutInflater.from(ctx), parent, false)

        }

        val tile = currentTiles[position]
        binding.cellImage.setImageURI(tile.image)
        binding.cellTitle.text = tile.title
        binding.cellDescription.text = tile.detail
        binding.root.tag = binding
        return binding.root
    }
```
{% endtab %}
{% tab Java %}
__Present a unified stream of data__<br>
Because the adapter uses the merged list to supply data model information to the `ListView`, both the Content Card-based data and the API(or JSON)-based data will be displayed in unison to the user.

```java
TODO
```
{% endtab %}
{% endtabs %}

### Content Cards in a Message Center
Content Cards can be used in a message center format where each message is its own card. Each card contains additional key value pairs that power on-click UI/UX.<br>

{% tabs %}
{% tab Kotlin %}
__Using `class_type` for On Click Behavior__<br>
When we inflate the Content Card data into our custom classes, we use the `class_type` property of the data to determine which concrete subclass should be used to
store the data.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.MESSAGE_FULL_PAGE -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```
{% endtab %}
{% tab Java %}
__Using `class_type` for On Click Behavior__<br>
When we inflate the Content Card data into our custom classes, we use the `class_type` property of the data to determine which concrete subclass should be used to
store the data.

```java
TODO
```
{% endtab %}
{% endtabs %}

Then, when handling the user interaction with the message list, we can use the message's type to determine which view to display to the user.

{% tabs %}
{% tab Kotlin %}
```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = MessageListBinding.inflate(layoutInflater)
        setContentView(binding.root)
        dataProvider = CardableMessageDataProvider(this)
        val listView = binding.listView
        listView.adapter = dataProvider
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
```java
TODO
```
{% endtab %}
{% endtabs %}


### Interactive Content Cards
Content Cards can be leveraged to create interactive experiences for your users. In our demo application, we have a Content Card pop-up appear at checkout providing users last-minute promotions. Well-placed cards like this are a great way to give users a "nudge" toward specific user actions. 

#### Interactable View<br><br>
{% tabs %}
{% tab Kotlin %}
__Requesting Content Cards__<br>
When we created our custom BrazeManager, we also defined a custom `ContentCardableObserver` interface to be called when Content Cards are updated. As long as the listener is still retained in memory, a notification callback from the Braze SDK can be expected. 
```kotlin
fun registerContentCardableObserver(observer: ContentCardableObserver){
        registerForContentCardUpdates()
        contentCardableObservers.add(observer)
        requestContentCardUpdate()
        if (cardList.isNotEmpty()){
            observer.onContentCardsChanged(mapCardsToCardables(cardList))
        }
    }
```
{% endtab %}
{% tab Java %}
__Requesting Content Cards__<br>
When we created our custom BrazeManager, we also defined a custom `ContentCardableObserver` interface to be called when Content Cards are updated. As long as the listener is still retained in memory, a notification callback from the Braze SDK can be expected. 
```java
todo
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
__Getting Type-Specific Content Cards__<br>
Similar to our other exampes, we can filter the cards to only retrieve the ones we're interested in for the shopping cart. In this case `Coupon` types.

```kotlin
 override fun onContentCardsChanged(cards: List<ContentCardable>) {
        coupons = cards.filterIsInstance<Coupon>()
    }
```
{% endtab %}
{% tab Java %}
__Getting Type-Specific Content Cards__<br>
Similar to our other exampes, we can filter the cards to only retrieve the ones we're interested in for the shopping cart. In this case `Coupon` types.

```java
@Override
public void onContentCardsChanged(List<ContentCardable> cards) {
        coupons = cards.stream().filter(c -> c instanceof Coupon).collect(Collectors.toList());
}
```
{% endtab %}
{% endtabs %}

## Logging Impressions, Clicks, and Dismissals

After extending your own custom objects to function as Content Cards, logging valuable metrics like impressions, clicks, and dismissals is quick and simple. This can be done through the use of a `ContentCardable` base class that references and provides data to the BrazeManager.

#### __Implementation Components__<br><br>

{% tabs %}
{% tab Kotlin %}
__Custom Objects Call the Logging Methods__<br>
Within your `ContentCardable` base class, you can call the BrazeManager directly, if appropriate. Remember, in this example, the `cardData` property will be nonnull if the object came from a content card. 

```swift
override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val tile = currentTiles[position]
        tile.logContentCardImpression()
        ...
    }
```

__Retrieve the Content Card from the ContentCardId__<br>
The `ContentCardable` base class handles the heavy lifting of calling the `BrazeManager` and passing the unique identifier from the Content Card associated with the custom object.

```kotlin
    fun logContentCardImpression() {
        cardData?.let { BrazeManager.getInstance().logContentCardImpression(it.contentCardId) }
    }
```

__Call `Card` Functions__<br>
The [BrazeManager](insert) can reference Braze SDK dependencies such as the list of Content Card objects array to get the `Card` to call our logging methods.

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
__Custom Objects Call the Logging Methods__<br>
Within your `ContentCardable` base class, you can call the BrazeManager directly, if appropriate. Remember, in this example, the `cardData` property will be nonnull if the object came from a content card. 
```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
        Tile tile = currentTiles.get(position);
        tile.logContentCardImpression();
        ...
    }
```

__Retrieve the Content Card from the `ContentCardId`__<br>
The `ContentCardable` base class handles the heavy lifting of calling the `BrazeManager` and passing the unique identifier from the Content Card associated with the custom object.

```java
    public void logContentCardImpression() {
        if (cardData != null){
            BrazeManager.getInstance().logContentCardImpression(cardData.getContentCardId());
        }
    }
```

__Call `Card` Functions__<br>
The [BrazeManager](insert) can reference Braze SDK dependencies such as the list of Content Card objects array to get the `Card` to call our logging methods.

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
For a control variant Content Card, a custom object should still be instantiated and UI logic should set the object's corresponding view as hidden. The object can then log an impression to inform our analytics of when a user would have seen the control card.
{% endalert %}
