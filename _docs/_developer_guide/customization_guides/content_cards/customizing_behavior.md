---
nav_title: Customizing Card Behavior
article_title: Customizing Content Card Behavior
page_order: 2
description: "This implementation guide discusses changing the behavior of Content Cards, adding extras such as key-value pairs to your payload, and recipes for common customizations."
channel:
  - content cards
---

# Customizing Content Card behavior

> This implementation guide discusses changing the behavior of Content Cards, adding extras such as key-value pairs to your payload, and recipes for common customizations.

## Key-value pairs

Braze enables you to send extra data payloads to user devices using key-value pairs. These can help you track internal metrics, update app content, and customize properties.

{% alert note %}
We do not recommend sending nested JSON values as key-value pairs. Instead, flatten the JSON before sending it. 
{% endalert %}

{% tabs %}
{% tab Android %}

You can place key-value pairs on [`card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721) objects as `extras`. These can be used to send data down along with a card for further handling by the application. Call [`card.extras`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html) to access these values.

{% endtab %}
{% tab iOS %}

You can place key-value pairs on [`card`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard) objects as `extras`. These can be used to send data down along with a card for further handling by the application. Call [`card.extras`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras) to access these values.

{% endtab %}
{% tab Web %}

You can place key-value pairs on [`card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) objects as `extras`. These can be used to send data down along with a card for further handling by the application. Call `card.extras` to access these values.

{% endtab %}
{% endtabs %}

You can also add key-value pairs through the [dashboard][6].

<!--Question: This alert specifically calls out a size limit for content "entered in the dashboard." Does that include Content Cards with extras programmatically added? -->

{% alert note %}
Content Cards have a maximum size limit of 2 KB for content you enter in the Braze dashboard. This includes message text, image URLs, links, and key-value pairs. Exceeding that amount will prevent the card from sending.
{% endalert %}


## Content Cards as supplemental content

![][1]{: style="float:right;max-width:25%;margin-left:15px;border:0;"}

You can seamlessly blend Content Cards into an existing feed, allowing data from multiple feeds to load simultaneously. This creates a cohesive, harmonious experience with Braze Content Cards and existing feed content.

<!---In the Android Implementation Guide, the image is said to show a `ListView`. In the Swift context, it was a `UICollectionView`. Is the following a good way to talk about this generically so this content doesn't have to be tabbed? -->

The example to the right shows a feed with a hybrid list of items that are populated via local data and Content Cards powered by Braze. With this, Content Cards can be indistinguishable alongside existing content.

### API-triggered key-value pairs

[API-triggered campaigns][7] are a good strategy to employ when a card's values depend on external factors to determine what content to display to the user. For example, to display supplemental content, set key-value pairs using Liquid. Note that `class_type` should be known at set-up time.

![The key-value pairs for the supplemental Content Cards use case. In this example, different aspects of the card such as "tile_id", "tile_deeplink", and "tile_title" are set using Liquid.][2]{: style="max-width:60%;"}

## Content Cards as interactive content
![An interactive Content Card showing a 50 percent promotion appear in the bottom left corner of the screen. Once clicked, a promotion will be applied to the cart.][4]{: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

Content Cards can be leveraged to create dynamic and interactive experiences for your users. In the example to the right, we have a Content Card pop-up appear at checkout providing users last-minute promotions. Well-placed cards like this are a great way to give users a "nudge" toward specific user actions. 

The key-value pairs for this use case include a `discount_percentage` set as the desired discount amount and `class_type` set as `coupon_code`. These key-value pairs allow you to filter and display type-specific Content Cards on the checkout screen. For more information on using key-value pairs to manage multiple feeds, see [Customizing the default Content Card feed][3]. 
<br>
<br>

![][5]{: style="max-width:70%;"} 

## Content card badges

![An iPhone home screen showing a Braze sample app named Swifty with a red badge displaying the number 7][8]{: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Badges are small icons that are ideal for getting a user's attention. Using badges to alert the user about new Content Card content can attract users back to your app and increase sessions.

### Displaying the number of unread Content Cards as a badge

You can display the number of unread Content Cards your user has as a badge on your app's icon. 

{% tabs %}
{% tab Android %}

You can request the number of unread cards at any time by calling:

{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endsubtab %}
{% endsubtabs %}

You can then use this information to display a badge signifying how many unread Content Cards there are. See the [SDK reference docs](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html) for more information.


{% endtab %}
{% tab iOS %}

The following sample uses `braze.contentCards` to request and display the number of unread Content Cards. Once the app is closed and the user's session ends, this code requests a card count, filtering the number of cards based on the `viewed` property.

{% subtabs %}
{% subtab Swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Within this method, implement the following code, which actively updates the badge count while the user views cards during a given session:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Within this method, implement the following code, which actively updates the badge count while the user views cards during a given session:

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

You can request the number of unread cards at any time by calling:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

You can then use this information to display a badge signifying how many unread Content Cards there are. See the [SDK reference docs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html) for more information.

{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/cc_implementation/supplementary.png %}
[2]: {% image_buster /assets/img/cc_implementation/supplementary_content.png %}
[3]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds
[4]: {% image_buster /assets/img/cc_implementation/discount2.png %}
[5]: {% image_buster /assets/img/cc_implementation/discount.png %}
[6]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/#content-cards
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/
[8]: {% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}