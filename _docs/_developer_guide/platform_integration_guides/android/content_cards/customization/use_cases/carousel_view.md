---
nav_title: Carousel View
article_title: Content Card Carousel View for Android and FireOS
page_order: 10
platform: 
  - Android
  - FireOS
description: "This article covers how to implement a Content Card carousel view use case for Android and FireOS applications."
channel:
  - content cards

---

# Carousel view

![Sample news app showing carousel of Content Cards in an article]({% image_buster/assets/img_archive/cc_politer_carousel_android.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;"}

This section covers implementing a multi-card carousel feed where a user can swipe horizontally to view additional featured cards. To integrate a carousel view, you'll need to use a fully customized Content Card implementation—the "run" phase of the [crawl, walk, run approach][1].

With this approach, you will not use Braze’s views and default logic but will instead display the Content Cards in a completely custom manner by using your own views populated with data from the Braze models.

In terms of the level of development effort, the key differences between the out-of-the-box implementation and the carousel implementation include:

- Building your own views
- Logging Content Card analytics
- Introducing additional client-side logic to dictate how many and which cards to show in the carousel

## Implementation

### Step 1: Create a custom view controller

To create the Content Cards carousel, create your own custom views and [subscribe for data updates]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/#fully-custom-content-card-display-for-android). Note that you won't be able to use Braze's default `ContentCardFragment`, as it's only able to handle our default Content Card types.

### Step 2: Implement analytics

When creating a fully custom view controller, Content Card impressions, clicks, and dismissals are not automatically logged. You must implement the respective analytics methods to ensure impressions, dismissal events, and clicks get properly logged back to Braze's dashboard analytics.

For information on the analytics methods, refer to [Card analytics methods]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/#card-methods).

{% alert note %}
The same page also details the different properties inherited from our generic Content Card model class, which you may find useful during your view implementation.
{% endalert %}

### Step 3: Create a Content Card update handler

Follow the steps for [Using multiple Content Card feeds]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/multiple_feeds/) to set key-value pairs on cards and create a Content Card update handler.

{% alert important %}
It's important to ensure your marketing and developer teams coordinate on which key-value pairs will be used (e.g., `feed_type = brand_homepage`), as any key-value pairs used must match the key-value pairs that the developers build into the app logic.
{% endalert %}

For Android-specific developer documentation on the Content Cards class, methods, and attributes in Kotlin, refer to the Android [com.braze.ui.contentcards.view](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/index.html) documentation.

## Considerations

- By using completely custom views, you will not be able to extend or subclass the methods used in `ABKContentCardsController`. Instead, you'll need to integrate the data model methods and properties yourself.
- The logic and implementation of the carousel view is not a default type of Content Card in Braze, and therefore the logic for achieving the use case must be supplied and supported by your development team.
- You will need to implement client-side logic to display a specific number of cards in the carousel at any one time.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches
