---
nav_title: Carousel View
article_title: Content Card Carousel View
page_order: 3
description: "This article covers how to implement a Content Card carousel view."
channel:
  - content cards
---

# Content Card carousel view 

![Sample news app showing carousel of Content Cards in an article.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

This section covers how to implement a multi-card carousel feed where a user can swipe horizontally to view additional featured cards. The logic and implementation of the carousel view is not a default type of Content Card in Braze, and therefore the logic for achieving the use case must be supplied and supported by your development team. To integrate a carousel view, you'll need to use a fully customized Content Card implementation&mdash;the "run" phase of the [crawl, walk, run approach][1].

With this approach, you will not use the default views and logic but instead display the Content Cards in a completely custom manner by using your own views populated with data from the Braze models.

To implement a carousel view, you will:
1. Build your own view controller
2. Subscribe to your custom view controller
3. Manually log analytics
4. Introduce additional client-side logic to dictate how many and which cards to show in the carousel

## Step 1: Create a custom view controller

{% tabs %}
{% tab Android %}

First, create your own custom view controller component. Note that you won't be able to use Braze's default [`ContentCardFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html), as it's only able to handle our default Content Card types.

INSERT SAMPLE ANDROID CODE HERE

{% endtab %}
{% tab iOS %}

First, create your own custom view controller component. Note that you won't be able to extend or subclass [`UICollectionViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller), as it's only able to handle our default Content Card types.

INSERT SAMPLE SWIFT CODE HERE

{% endtab %}
{% tab Web %}

Web Content

INSERT SAMPLE WEB CODE HERE

{% endtab %}
{% endtabs %}


## Step 2: Subscribe to data updates

Then, [subscribe to data updates]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates) from your custom view controller. 

## Step 3: Implement analytics

When creating a custom view controller, Content Card impressions, clicks, and dismissals are not automatically logged. You must [implement each respective method]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events) to ensure impressions, dismissal events, and clicks get properly logged back to Braze's dashboard analytics.

{% alert note %}
Braze offers several different Content Card subclasses, each of which inherit different properties from the generic Content Card model class. Understanding these inherited properties will be useful during customization. Refer to the `ContentCard` class documentation ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard), [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)) for full details. 
{% endalert %}

{% tabs %}
{% tab Android %}

INSERT SAMPLE ANDROID CODE HERE

{% endtab %}
{% tab iOS %}

INSERT SAMPLE SWIFT CODE HERE

{% endtab %}
{% tab Web %}

INSERT SAMPLE WEB CODE HERE

{% endtab %}
{% endtabs %}

## Step 4: Create a Content Card observer

Implement logic that observes for [changes in your Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed), handles Content Card arrival, and displays a specific number of cards in the carousel at any one time. By default, Content Cards are sorted by created date (newest first), and a user sees all cards they are eligible for. 

With that said, you could order and apply additional display logic in a variety of ways. For example, you could select the first five Content Card objects from the array or introduce key-value pairs (the `extras` property in the data model) to build conditional logic around.

If you're implementing a carousel as a secondary Content Cards feed, refer to [Customizing the default Content Card feed]({{site.baseurl}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) to ensure you sort cards into the correct feed based on key-value pairs.

{% alert important %}
It's important to ensure your marketing and developer teams coordinate on which key-value pairs will be used (e.g., `feed_type = brand_homepage`), as any key-value pairs marketers input into the Braze dashboard must exactly match the key-value pairs that developers build into the app logic.
{% endalert %}

{% tabs %}
{% tab Android %}

INSERT SAMPLE ANDROID CODE HERE

{% endtab %}
{% tab iOS %}

INSERT SAMPLE SWIFT CODE HERE

{% endtab %}
{% tab Web %}

INSERT SAMPLE WEB CODE HERE

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/customization_guides/customization_overview