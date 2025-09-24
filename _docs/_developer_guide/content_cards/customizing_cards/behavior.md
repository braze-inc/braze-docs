---
nav_title: Behavior
article_title: Customizing the behavior of Content Cards
page_order: 2
description: "This implementation guide discusses changing the behavior of Content Cards, adding extras such as key-value pairs to your payload, and recipes for common customizations."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Customizing the behavior of Content Cards

> This implementation guide discusses changing the behavior of Content Cards, adding extras such as key-value pairs to your payload, and recipes for common customizations. For the full list of content card types, see [About Content Cards]({{site.baseurl}}/developer_guide/content_cards/). 

## Key-value pairs

Braze enables you to send extra data payloads via Content Cards to user devices using key-value pairs. These can help you track internal metrics, update app content, and customize properties. [Add key-value pairs using the dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create#step-4-configure-additional-settings-optional). 
 
{% alert note %}
We do not recommend sending nested JSON values as key-value pairs. Instead, flatten the JSON before sending it. 
{% endalert %}

{% tabs %}
{% tab web %}

Key-value pairs are stored on <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> objects as `extras`. These can be used to send data down along with a card for further handling by the application. Call `card.extras` to access these values.

{% endtab %}
{% tab android %}

Key-value pairs are stored on <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> objects as `extras`. These can be used to send data down along with a card for further handling by the application. Call <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> to access these values.

{% endtab %}
{% tab swift %}

Key-value pairs are stored on <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> objects as `extras`. These can be used to send data down along with a card for further handling by the application. Call <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> to access these values.

{% endtab %}
{% endtabs %}

{% alert tip %}
It's important that your marketing and developer teams coordinate on which key-value pairs will be used (for example, `feed_type = brand_homepage`), as any key-value pairs marketers input into the Braze dashboard must exactly match the key-value pairs that developers build into the app logic.
{% endalert %}

## Content Cards as supplemental content

![]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

You can seamlessly blend Content Cards into an existing feed, allowing data from multiple feeds to load simultaneously. This creates a cohesive, harmonious experience with Braze Content Cards and existing feed content.

The example to the right shows a feed with a hybrid list of items that are populated via local data and Content Cards powered by Braze. With this, Content Cards can be indistinguishable alongside existing content.

### API-triggered key-value pairs

[API-triggered campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) are a good strategy to employ when a card's values depend on external factors to determine what content to display to the user. For example, to display supplemental content, set key-value pairs using Liquid. Note that `class_type` should be known at set-up time.

![The key-value pairs for the supplemental Content Cards use case. In this example, different aspects of the card such as "tile_id", "tile_deeplink", and "tile_title" are set using Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Content Cards as interactive content
![An interactive Content Card showing a 50 percent promotion appear in the bottom left corner of the screen. After it's clicked, a promotion will be applied to the cart.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

Content Cards can be leveraged to create dynamic and interactive experiences for your users. In the example to the right, we have a Content Card pop-up appear at checkout providing users last-minute promotions. Well-placed cards like this are a great way to give users a "nudge" toward specific user actions. 

The key-value pairs for this use case include a `discount_percentage` set as the desired discount amount and `class_type` set as `coupon_code`. These key-value pairs allow you to filter and display type-specific Content Cards on the checkout screen. For more information on using key-value pairs to manage multiple feeds, see [Customizing the default Content Card feed]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds). 
<br>
<br>

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"} 

## Content Card badges

![An iPhone home screen showing a Braze sample app named Swifty with a red badge displaying the number 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Badges are small icons that are ideal for getting a user's attention. Using badges to alert the user about new Content Card content can attract users back to your app and increase sessions.

### Displaying the number of unread Content Cards as a badge

You can display the number of unread Content Cards your user has as a badge on your app's icon. 

{% tabs %}
{% tab web %}

You can request the number of unread cards at any time by calling:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

You can then use this information to display a badge signifying how many unread Content Cards there are. See the <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">SDK reference docs</a> for more information.

{% endtab %}
{% tab android %}

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

You can then use this information to display a badge signifying how many unread Content Cards there are. See the <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">SDK reference docs</a> for more information.


{% endtab %}
{% tab swift %}

The following sample uses `braze.contentCards` to request and display the number of unread Content Cards. After the app is closed and the user's session ends, this code requests a card count, filtering the number of cards based on the `viewed` property.

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
{% endtabs %}


