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

__No `Card` Dependencies__<br>
`ContentCardData` represents the parsed out, common values of an `Card`.
{% tabs %}
{% tab Kotlin %}


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
{% endtab %}
{% tab Java %}


```java
TODO
```
{% endtab %}
{% endtabs %}
__Custom Object Initializer__<br>
MetaData from a `Card` is used to populate your concrete subclass's variables. Depending on the subclass, you may need to extract different values during initialization. The key value pairs set up in the Braze Dashboard are represented in the “extras” dictionary.
{% tabs %}
{% tab Kotlin %}
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
{% endtab %}
{% tab Java %}
```java
TODO
```
{% endtab %}
{% endtabs %}
__Identifying Types__<br>
The `ContentCardClass` enum represents the `class_type` value in the Braze Dashboard and provides a method to initialize the enum from the Strings supplied by the SDK.
{% tabs %}
{% tab Kotlin %}
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
{% endtab %}
{% tab Java %}
```java
TODO
```
{% endtab %}
{% endtabs %}

