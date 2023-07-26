---
nav_title: Creating Custom Content Cards
article_title: Creating Custom Content Cards
page_order: 5
description: "This article covers components of creating a custom Content Card UI"
channel:
  - content cards
---

# Creating custom Content Cards

Braze provides [four Content Card templates: banner, captioned image, classic, and classic image][1]. These templates can be used as a starting place for your implementations, tweaking their look and feel, the order in which cards are displayed, and how the feed is shown to your users. You can also display Content Cards in a completely custom manner by using your own presentation UI populated with data from the Braze models&mdash;the "run" phase of the [crawl, walk, run approach][2].

This article discusses the basic approach you'll use when implementing custom Content Cards, as well as three common use cases: banner images, a message inbox, and a carousel of images.

{% alert note %}
Each default Content Card template is a subclass which inherits different properties from the generic Content Card model class. Understanding these inherited properties will be useful during customization. Refer to the `ContentCard` class documentation ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard), [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)) for full details. 
{% endalert %}


## Customization basics

When implementing your custom Content Cards, you can parse the Content Card objects and extract their payload data such as `title`, `cardDescription`, and `imageUrl`. Then, you can use the resulting model data to populate your custom UI.

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

First, create your custom view. <!-- Is there a web equivalent to a view controller?-->

{% endtab %}
{% endtabs %}

### Step 2: Subscribe to card updates

Then, [register a callback function to subscribe for data updates when cards are refreshed][6]. 

<!-- Is the following a true statement for Android and iOS? "Content Cards will only refresh on session start if a subscribe request is called before openSession(). You can always choose to manually refresh the feed as well."-->

### Step 3: Implement analytics

When creating a custom view, Content Card impressions, clicks, and dismissals are not automatically logged. You must [implement each respective method][3] to ensure impressions, dismissals, and clicks get properly logged back to Braze's dashboard analytics.

## Content Card placements

This section provides an overview of the three most common ways to place Content Cards within your app or site. For each of these placements, you will assign [key-value pairs][7] to your Content Cards, and based on the values, dynamically adjust the card's behavior, appearance, or functionality during runtime. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Banner

Content Cards don't have to look like "cards." For example, Content Cards can appear as a dynamic banner that persistently displays on your home page or at the top of other designated pages. 

To achieve this, your marketers will create a campaign or Canvas step with an **Banner** type of Content Card. Then, set key-value pairs that are appropriate for using [Content Cards as supplemental content.][4]

### Message inbox

Content Cards can be used to simulate a message center. In this format, each message is its own card that contains key-value pairs that power on-click UX. In the following example, one message directs you to an arbitrary custom view, while another opens to a webview that displays custom HTML.

Assign [key-value pairs][5] in the dashboard to the cards you intend to use for your message center. The values of the key-value pairs are arbitrary but should be distinguishable between class types. These key-value pairs are the key identifiers that the application looks at when deciding where to go when the user clicks on an inbox message. For example, you could add the key-value pair `class_type` to your dashboard configuration. 

{% tabs local %}
{% tab Arbitrary custom view message (full page) %}

The key-value pairs for this use case include:

- `class_type` set as `message_full_page`
- `message_header` set as `Full Page`

![]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Webview message (HTML) %}

The key-value pairs for this use case include:

- `class_type` set as `message_webview`
- `message_header` set as `HTML`
- `message_title` set as a string with your content.

This message also looks for an HTML key-value pair, but if you are working with a web domain, a URL key-value pair is also valid.

![]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

### Carousel

Content Cards can be set in a carousel feed where a user can swipe horizontally to view additional featured cards. 

To create a Content Card carousel, implement logic that observes for [changes in your Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed), and handles Content Card arrival. By default, Content Cards are sorted by created date (newest first), and a user sees all cards they are eligible for. You will need to implement client-side logic to display a specific number of cards in the carousel at any one time.

With that said, you could order and apply additional display logic in a variety of ways. For example, you could select the first five Content Card objects from the array or introduce key-value pairs (the `extras` property in the data model) to build conditional logic around.

If you're implementing a carousel as a secondary Content Cards feed, refer to [Customizing the default Content Card feed]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) to ensure you sort cards into the correct feed based on key-value pairs.





[1]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details
[2]: {{site.baseurl}}/developer_guide/customization_guides/customization_overview
[3]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events
[4]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content
[5]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs
[6]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates
[7]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs