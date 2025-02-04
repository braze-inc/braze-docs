---
nav_title: Custom Content Cards
article_title: Creating Custom Content Cards
page_order: 5
description: "This article covers components of creating a custom Content Card UI"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Custom Content Cards

> This article discusses the basic approach you'll use when implementing custom Content Cards, as well as three common use cases: banner images, a message inbox, and a carousel of images. It assumes you've already read the other articles in the Content Card customization guide to understand what can be done by default and what requires custom code. It is especially to understand how to [log analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) for your custom Content Cards. 

## About Content Cards

Braze provides different [Content Card types]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details): `imageOnly`, `captionedImage`, `classic`, `classicImage`, and `control`. These can be used as a starting place for your implementations, tweaking their look and feel. 

You can also display Content Cards in a completely custom manner by creating your own presentation UI populated with data from the Braze models. Parse the Content Card objects and extract their payload data. Then, use the resulting model data to populate your custom UI&mdash;the "run" phase of the [crawl, walk, run approach]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

{% alert note %}
Each default Content Card type is a subclass which inherits different properties from the generic Content Card model class. Understanding these inherited properties will be useful during customization. Refer to the Card class documentation for full details ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard), [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)). 
{% endalert %}

## Creating a custom card

### Step 1: Create a custom UI 

{% tabs local %}
{% tab Android %}

First, create your own custom fragment. The default [`ContentCardFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) is only designed to handle our default Content Card types, but is a good starting point.

{% endtab %}
{% tab iOS %}

First, create your own custom view controller component. The default [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) is only designed to handle our default Content Card types, but is a good starting point.

{% endtab %}
{% tab Web %}

First, create your custom HTML component that will be used to render the cards. 

{% endtab %}
{% endtabs %}

### Step 2: Subscribe to card updates

Then, register a callback function to [subscribe for data updates]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates) when cards are refreshed. 

### Step 3: Implement analytics

Content Card impressions, clicks, and dismissals are not automatically logged in your custom view. You must [implement each respective method]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events) to properly log all metrics back to Braze dashboard analytics.

## Content Card placements

Content Cards can be used in many different ways. Three common implementations are to use them as a message center, a banner ad, or an image carousel. For each of these placements, you will assign [key-value pairs]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (the `extras` property in the data model) to your Content Cards, and based on the values, dynamically adjust the card's behavior, appearance, or functionality during runtime. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Message inbox

Content Cards can be used to simulate a message center. In this format, each message is its own card that contains [key-value pairs]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) that power on-click events. These key-value pairs are the key identifiers that the application looks at when deciding where to go when the user clicks on an inbox message. The values of the key-value pairs are arbitrary. 

#### Example

For example, you may want to create two message cards: a call-to-action for users enable to reading recommendations and a coupon code given to your new subscriber segment.

Keys like `body`, `title`, and `buttonText` might have simple string values your marketers can set. Keys like `terms` might have values that provide a small collection of phrases approved by your Legal department. You would decide how to render `style` and `class_type` on your app or site. 

{% tabs local %}
{% tab Reading recommendations %}
Key-value pairs for the reading recommendation card:

| Key         | Value                                                                |
|------------|----------------------------------------------------------------------|
| `body`       | Add your interests to your Politer Weekly profile for personal reading recommendations. |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab New subscriber coupon %}
Key-value pairs for a new subscriber coupon:

| Key         | Value                                                            |
|------------|------------------------------------------------------------------|
| `title`      | Subscribe for unlimited games                                    |
| `body`       | End of Summer Special - Enjoy 10% off Politer games              |
| `buttonText` | Subscribe Now                                                    |
| `style`      | promo                                                            |
| `class_type` | notification_center                                              |
| `card_priority` | 2                                                              |
| `terms`      | new_subscribers_only                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

{% details Additional information for Android %}

In the Android and FireOS SDK, the message center logic is driven by the `class_type` value that is provided by the key-value pairs from Braze. Using the [`createContentCardable`]({{site.baseurl}}/developer_guide/platforms/android/content_cards/examples/) method, you can filter and identify these class types.

{% tabs local %}
{% tab Kotlin %}
**Using `class_type` for on-click behavior**<br>
When we inflate the Content Card data into our custom classes, we use the `ContentCardClass` property of the data to determine which concrete subclass should be used to store the data.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
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
**Using `class_type` for on-click behavior**<br>
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
        case ContentCardClass.NOTIFICATION_CENTER:{
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
{% enddetails %}

### Carousel

You can set Content Cards your fully-custom carousel feed, allowing users to swipe and view additional featured cards. By default, Content Cards are sorted by created date (newest first), and your users will see all the cards they're eligible for.

To implement a Content Card carousel:

1. Create custom logic that observes for [changes in your Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) and handles Content Card arrival.
2. Create custom client-side logic to display a specific number of cards in the carousel any one time. For example, you could select the first five Content Card objects from the array or introduce key-value pairs to build conditional logic around.

{% alert tip %}
If you're implementing a carousel as a secondary Content Cards feed, be sure to [sort cards into the correct feed using key-value pairs]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
{% endalert %}

### Banner

Content Cards don't have to look like "cards." For example, Content Cards can appear as a dynamic banner that persistently displays on your home page or at the top of designated pages.

To achieve this, your marketers will create a campaign or Canvas step with a **Image Only** type of Content Card. Then, set key-value pairs that are appropriate for using [Content Cards as supplemental content]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content).
