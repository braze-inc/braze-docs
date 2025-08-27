---
nav_title: Carousel view
article_title: Content Card Carousel View for iOS
platform: iOS
page_order: 5
description: "This article covers how to implement a Content Card carousel view use case for iOS applications."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Use case: Carousel view

![Sample news app showing carousel of Content Cards in an article.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

This section covers how to implement a multi-card carousel feed where a user can swipe horizontally to view additional featured cards. To integrate a carousel view, you'll need to use a fully customized Content Card implementation—the "run" phase of the [crawl, walk, run approach]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches).

With this approach, you will not use Braze views and default logic but instead, display the Content Cards in a completely custom manner by using your own views populated with data from the Braze models.

In terms of the level of development effort, the key differences between the basic implementation and the carousel implementation include:

- Building your own views
- Logging Content Card analytics
- Introducing additional client-side logic to dictate how many and which cards to show in the carousel

## Implementation

### Step 1: Create a custom view controller

To create the Content Cards carousel, create your own custom view controller (such as `UICollectionViewController`) and [subscribe for data updates]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#getting-the-data). Note that you won't be able to extend or subclass our default `ABKContentCardTableViewController`, as it's only able to handle our default Content Card types.

### Step 2: Implement analytics

When creating a fully custom view controller, Content Card impressions, clicks, and dismissals are not automatically logged. You must implement the respective analytics methods to ensure impressions, dismissal events, and clicks get properly logged back to the Braze dashboard analytics.

For information on the analytics methods, refer to [Card methods]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#card-methods). 

{% alert note %}
The same page also details the different properties inherited from our generic Content Card model class, which you may find useful during your view implementation.
{% endalert %}

### Step 3: Create a Content Card observer

Create a [Content Card observer]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/#step-2-set-up-a-content-card-listener) that is responsible for handling the arrival of Content Cards, and implement conditional logic to display a specific number of cards in the carousel at any one time. By default, Content Cards are sorted by created date (newest first), and a user sees all cards they are eligible for.

That said, you could order and apply additional display logic in a variety of ways. For example, you could select the first five Content Card objects from the array or introduce key-value pairs (the `extras` property in the data model) to build conditional logic around.

If you're implementing a carousel as a secondary Content Cards feed, refer to [Using multiple Content Card feeds]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds/) to ensure you sort cards into the correct feed based on key-value pairs.

{% alert important %}
It's important to ensure your marketing and developer teams coordinate on which key-value pairs will be used (for example, `feed_type = brand_homepage`), as any key-value pairs marketers input into the Braze dashboard must exactly match the key-value pairs that the developers build into the app logic.
{% endalert %}

For iOS-specific developer documentation on the Content Cards class, methods, and attributes, refer to the iOS [`ABKContentCard` class reference](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Considerations

- By using completely custom views, you will not be able to extend or subclass the methods used in `ABKContentCardsController`. Instead, you'll need to integrate the data model methods and properties yourself.
- The logic and implementation of the carousel view is not a default type of Content Card in Braze, and therefore the logic for achieving the use case must be supplied and supported by your development team.
- You will need to implement client-side logic to display a specific number of cards in the carousel at any one time.

