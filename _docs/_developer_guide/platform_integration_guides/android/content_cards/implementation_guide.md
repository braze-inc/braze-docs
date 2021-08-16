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

When building out Content Cards, you should expose the Braze SDK via a single manager singleton. This pattern shields your application code from the Braze implementation details behind a shared abstraction that makes sense for your use case. It also makes it easier to track, debug, and alter code. An example manager implementation can be found [here](FIXME).

### Content Cards as Custom Objects

Your own custom objects already in use in your application can be extended to carry Content Card data, thereby abstracting the source of the data into a format already understood by your application code. Data source abstractions such as this provide flexibility to work with different data backends interchangeably and in concert. In this example, we've defined the `ContentCardable` abstract base class to represent both our existing data (fed, in this example, from a local JSON file) and the new data, fed from the Braze SDK. The base class also exposes the raw Content Card data for consumers that need to access the original `Card` implementation.

When initializing `ContentCardable` instances from the Braze SDK, we utilize the `class_type` extra to map the Content Card to a concrete subclass. We then use the additional key-value pairs set within the Braze Dashboard to populate the necessary fields.

Once you have a solid understanding of these code considerations, check out our [use cases](#sample-use-cases) below to start implementing your own custom objects.

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
MetaData from a `Card` is used to populate your concrete subclass's variables. Depending on the subclass, you may need to extract different values during initialization. The key-value pairs set up in the Braze dashboard are represented in the “extras” dictionary.

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
MetaData from a `Card` is used to populate your concrete subclass's variables. Depending on the subclass, you may need to extract different values during initialization. The key-value pairs set up in the Braze dashboard are represented in the “extras” dictionary.

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
The `ContentCardClass` enum represents the `class_type` value in the Braze dashboard and provides a method to initialize the enum from the Strings supplied by the SDK.

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
The `ContentCardClass` enum represents the `class_type` value in the Braze dashboard and provides a method to initialize the enum from the Strings supplied by the SDK.

```java
TODO
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Sample Use Cases

There are three sample customer use cases provided. Each use case offers a detailed explanation, relevant code snippets, and a look into how Content Card variables may look and be used in the Braze dashboard:
- [Content Cards As Supplemental Content](#content-cards-as-supplemental-content)
- [Content Cards in a Message Center](#content-cards-in-a-message-center)
- [Interactive Content Cards](#interactive-content-cards)

### Content Cards as Supplemental Content

![Supplementary Content PNG][1]{: style="float:right;max-width:25%;margin-left:15px;border:0;"}

You can seamlessly blend Content Cards into an existing feed, allowing data from multiple feeds to load simultaneously. This creates a cohesive, harmonious experience with Braze Content Cards and existing feed content.

The example to the right shows a `ListView` with a hybrid list of items that are populated via local data and Content Cards powered by Braze. With this, Content Cards can be indistinguishable alongside existing content.

#### Dashboard Configuration

This Content Card is delivered by an API-triggered campaign with API-triggered key-value pairs. This is ideal for campaigns where the card's values depend on external factors to determine what content to display to the user. Note that `class_type` should be known at set-up time.

![Supplementary Content PNG][2]{: style="max-width:60%;"}

##### Ready to log analytics?
Visit the [following section](#logging-impressions-clicks-and-dismissals) to get a better understanding of how the flow of data should look.

### Content Cards in a Message Center
<br>
Content Cards can be used in a message center format where each message is its own card. Each message in the message center is populated via a Content Card payload, and each card contains additional key-value pairs that power on-click UI/UX. In the example below, one message directs you to an arbitrary custom view, while another opens to a webview that displays custom HTML.

![Message Center PNG][3]{: style="border:0;"}{: style="max-width:80%;border:0"}

#### Dashboard Configuration

For the following message types, the key-value pair `class_type` should be added to your dashboard configuration. The values assigned here are arbitrary but should be distinguishable between class types. These key-value pairs are the key identifiers that the application looks at when deciding where to go when the user clicks on an abridged inbox message. 

| Arbitrary Custom View Message (Full Page) | Webview Message (HTML) |
| ---- | ---- |
| <br>The key-value pairs for this use case include:<br><br>- `message_header` set as `Full Page`<br>- `class_type` set as `message_full_page`<br><br><br>![Message Center JPG1][4]{: style="max-width:100%;"} | The key-value pairs for this use case include:<br><br>- `message_header` set as `HTML`<br>- `class_type` set as `message_webview`<br>- `message_title`<br><br>This message also looks for an HTML key-value pair, but if you are working with a web domain, a URL key-value pair is also valid.<br><br>![Message Center JPG2][5] |
{: .reset-td-br-1 .reset-td-br-2}

#### Further Explanation

The message center logic is driven by the `class_type` that is provided by the key-value pairs from Braze. Using the `createContentCardable` method from our example, you can filter and identify these class types.

{% tabs %}
{% tab Kotlin %}
__Using `class_type` for On Click Behavior__<br>
When we inflate the Content Card data into our custom classes, we use the `ContentCardClass` property of the data to determine which concrete subclass should be used to
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

Then, when handling the user interaction with the message list, we can use the message's type to determine which view to display to the user.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
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
__Using `class_type` for On Click Behavior__<br>
When we inflate the Content Card data into our custom classes, we use the `ContentCardClass` property of the data to determine which concrete subclass should be used to store the data.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.MESSAGE_FULL_PAGE:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

Then, when handling the user interaction with the message list, we can use the message's type to determine which view to display to the user.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}

##### Ready to log analytics?
Visit the [following section](#logging-impressions-clicks-and-dismissals) to get a better understanding of how the flow of data should look.

![Interactive Content PNG][6]{: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

### Interactive Content Cards
<br>
Content Cards can be leveraged to create dynamic and interactive experiences for your users. In the example to the right, we have a Content Card pop-up appear at checkout providing users last-minute promotions. 

Well-placed cards like this are a great way to give users a "nudge" toward specific user actions. 
<br><br><br>
#### Dashboard Configuration

The dashboard configuration for interactive Content Cards is quick and straightforward. The key-value pairs for this use case include a `discount_percentage` set as the desired discount amount and `class_type` set as `coupon_code`. These key-value pairs are how type-specific Content Cards get filtered and displayed on the checkout screen.

![Interactive Content JPG][7]{: style="max-width:70%;"} 

##### Ready to log analytics?
Visit the [following section](#logging-impressions-clicks-and-dismissals) to get a better understanding of how the flow of data should look.

## Logging Impressions, Clicks, and Dismissals

After extending your custom objects to function as Content Cards, logging valuable metrics like impressions, clicks, and dismissals is quick and simple. This can be done by using a `ContentCardable` base class that references and provides data to the `BrazeManager`.

#### __Implementation Components__<br><br>

{% tabs %}
{% tab Kotlin %}
__Custom Objects Call the Logging Methods__<br>
Within your `ContentCardable` base class, you can call the `BrazeManager` directly, if appropriate. Remember, in this example, the `cardData` property will be nonnull if the object came from a Content Card. 

```kotlin
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
The [BrazeManager](insert) can reference Braze SDK dependencies such as the Content Card objects array list to get the `Card` to call our logging methods.

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
Within your `ContentCardable` base class, you can call the `BrazeManager` directly, if appropriate. Remember, in this example, the `cardData` property will be nonnull if the object came from a Content Card. 
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
The `[BrazeManager](insert)` can reference Braze SDK dependencies such as the Content Card objects array list to get the `Card` to call our logging methods.

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

## Helper Files

{% details ContentCardKey Helper File %}
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

[1]: {% image_buster /assets/img/cc_implementation/android_supplemental_content.png %}
[2]: {% image_buster /assets/img/cc_implementation/supplementary_content.png %}
[3]: {% image_buster /assets/img/cc_implementation/android_message_center.png %}
[4]: {% image_buster /assets/img/cc_implementation/full_page.png %}
[5]: {% image_buster /assets/img/cc_implementation/html_webview.png %}
[6]: {% image_buster /assets/img/cc_implementation/android_discount2.png %} //todo
[7]: {% image_buster /assets/img/cc_implementation/discount.png %}