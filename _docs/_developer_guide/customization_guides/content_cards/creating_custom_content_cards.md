---
nav_title: Creating Custom Content Cards
article_title: Creating Custom Content Cards
page_order: 5
description: "This article covers components of creating a custom Content Card UI"
channel:
  - content cards
---

# Creating custom Content Cards

> This article discusses the basic approach you'll use when implementing custom Content Cards, as well as three common use cases: banner images, a message inbox, and a carousel of images.

Braze provides four [Content Card types][1]: `banner`, `captionedImage`, `classic`, and `classicImage`. These can be used as a starting place for your implementations, tweaking their look and feel. You can also display Content Cards in a completely custom manner by using your own presentation UI populated with data from the Braze models; parse the Content Card objects and extract payload data such as `title`, `cardDescription`, and `imageUrl`. Then, you can use the resulting model data to populate your custom UI&mdash;the "run" phase of the [crawl, walk, run approach][2].

{% alert note %}
Each default Content Card type is a subclass which inherits different properties from the generic Content Card model class. Understanding these inherited properties will be useful during customization. Refer to the `ContentCard` class documentation ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard), [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)) for full details. 
{% endalert %}


## Customization overview

Depending on your use case, the exact implementation of your custom Content Card will vary a bit, but you will want to follow this basic formula:

1. Build your own UI
2. Listen to data updates
3. Manually log analytics

### Step 1: Create a custom UI 

{% tabs %}
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

Then, register a callback function to [subscribe for data updates][6] when cards are refreshed. 

### Step 3: Implement analytics

Content Card impressions, clicks, and dismissals are not automatically logged in your custom view. You must [implement each respective method][3] to ensure all metrics get properly logged back to Braze's dashboard analytics.

## Content Card placements

This section provides an overview of the three most common ways to place Content Cards within your app or site. For each of these placements, you will assign [key-value pairs][7] (the `extras` property in the data model) to your Content Cards, and based on the values, dynamically adjust the card's behavior, appearance, or functionality during runtime. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Message inbox

Content Cards can be used to simulate a message center. In this format, each message is its own card that contains [key-value pairs][5] that power on-click events. These key-value pairs are the key identifiers that the application looks at when deciding where to go when the user clicks on an inbox message. The values of the key-value pairs are arbitrary but should be distinguishable between class types. 

Here is an example dashboard configuration you might use to create two message cards: one message is a call to action for a user to add their preferences to receive targeted reading recommendations, and one provides a coupon code to a segment of new subscribers. 

![]({% image_buster /assets/img/content_cards/content-card-message-inbox-with-kvps %}){: style="max-width:50%;"}

Example key-value pairs for the reading recommendation card could be:

- body: Add your interests to your Politer Weekly profile for personal reading recommendations.
- style: info
- placement: notification_center
- card_priority: 1

Example key-value pairs for a new subscriber coupon could be:

- title: Subscribe for unlimited games
- body: End of Summer Special - Enjoy 10% off Politer games
- buttonText: Subscribe Now
- style: promo
- placement: notification_center
- card_priority: 2
- terms: new_subscribers_only

Your marketers could make this Content Card available only for a segment of new users. 

You would handle each of the values. Keys like `body`, `title`, and `buttonText` might have simple string values your marketers can set. Keys like `terms` might have values that provide a small collection of phrases approved by your Legal department. You would decide how to render `style` and `placement` on your app or site. 

### Carousel

Content Cards can be set in a carousel feed where a user can swipe horizontally to view additional featured cards. 

To create a Content Card carousel, implement logic that observes for [changes in your Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) and handles Content Card arrival. By default, Content Cards are sorted by created date (newest first), and a user sees all cards they are eligible for. Implement client-side logic to display a specific number of cards in the carousel at any one time.

With that said, you could order and apply additional display logic in a variety of ways. For example, you could select the first five Content Card objects from the array or introduce key-value pairs to build conditional logic around.

If you're implementing a carousel as a secondary Content Cards feed, refer to [Customizing the default Content Card feed]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) to ensure you sort cards into the correct feed based on key-value pairs.

### Banner

Content Cards don't have to look like "cards." For example, Content Cards can appear as a dynamic banner that persistently displays on your home page or at the top of other designated pages.

To achieve this, your marketers will create a campaign or Canvas step with a **Banner** type of Content Card. Then, set key-value pairs that are appropriate for using [Content Cards as supplemental content][4].


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details
[2]: {{site.baseurl}}/developer_guide/customization_guides/customization_overview
[3]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events
[4]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content
[5]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs
[6]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates
[7]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs
