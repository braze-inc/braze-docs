---
nav_title: About Content Cards
article_title: About Content Cards
page_order: 0
description: "This reference article provides an overview of the Braze Content Card channel and common use cases."
channel:
  - content cards
search_rank: 4
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} About Content Cards

> Content Cards are a channel that is embedded directly into the interface of your app or website so that you can engage users in a way that feels like a native, seamless part of the experience. You can do a lot with Content Cards—but the most common implementations are a message inbox, carousel, or banner.

Content Cards are great for extending the reach of other channels, like email or push notifications, and they give you more control over the app or website experience.

{% alert note %}
If you're using our News Feed tool, we recommend that you move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. News Feed is being deprecated. See our [Migration Guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) or contact your Braze account manager for more information.
{% endalert %}

Content Cards are an add-on feature and must be purchased. To get started with Content Cards, reach out to your Braze customer success manager or our support team.

## Advantages of using Content Cards

Wondering about the benefits of using Content Cards versus having your developers build content into your app? Here are some advantages of using Content Cards:

- **Easier segmentation and personalization:** Your user data lives in Braze, making it easy to define your audience and personalize your messages with Content Cards.
- **Centralized reporting:** Content Card analytics are tracked in Braze, so you have insight into all of your campaigns in one centralized location.
- **Cohesive customer journeys:** You can combine Content Cards with other channels in Braze to create consistent customer experiences. A popular use case is sending a push notification, then saving that notification as a Content Card in your app for anyone who didn’t engage with the push. If the content is built directly into your app by your developers, then it’s siloed from the rest of your messaging.
- **Content Cards don't require opt-in:** Similar to in-app messages, Content Cards don't require opt-in or permissions from your users. While in-app messages are permissionless but short-lived, Content Cards are permissionless and permanent. This means messaging strategies that pair in-app messages and Content Cards together strike a great balance.
- **More control over the messaging experience:** While you’ll still need your developers to help with the initial setup of Content Cards, after that, you’ll be able to control the message, recipients, timing, and more straight from your Braze dashboard.

### Content Cards by the numbers

Because you, the marketer, are building Content Cards yourself in Braze, you can make messaging updates and receive a return on investment without having to completely overhaul your app or site. Here are some helpful statistics on the ROI of Content Cards:

- Content Cards are **38X** more effective than emails at boosting sales over a 72-hour window.[^1]
- Using Content Cards in loyalty enrollment campaigns boosts conversions by **5X**.[^1]
- Sending users outreach via push, in-app messages, and Content Cards results in **6.9X** more sessions, compared to users engaged via push alone.[^2]
- Sending users outreach via email, in-app messages, and Content Cards results in **3.6X** longer average user lifetime, compared to users engaged via email alone.[^2]

## Use cases

This section outlines some common use cases for Content Cards.

{% alert tip %}
For more inspiration, we highly recommend that you check out our [Content Cards Inspiration Guide](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), which includes over 20 customizable campaigns, including referral programs, new product launches, and subscription renewal.
{% endalert %}

{% tabs %}
{% tab Onboarding and next steps %}

As new customers explore your app and website, walk them through the values and benefits of what you offer with strategically placed Content Cards. Encourage customers to opt into other communication channels with a Content Card on your homepage, and save outstanding onboarding tasks in a dedicated onboarding tab powered by Content Cards. Don’t forget to remove a card after a customer completes the desired task!

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_onboarding.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Event attendance %}

Showcase Content Cards at the top of a user’s homepage to encourage event attendance, using location targeting to reach potential customers where they are. Inviting users to relevant physical events makes them feel special, especially with personalized messaging that leverages their previous activity with your brand.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Recommendations %}

Use the data you have on user behaviors and preferences to surface relevant content in real time from homepage or inbox Content Cards and draw them back into your product offering.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Sales and promotions %}

Take advantage of Content Cards to highlight promotional messages and unclaimed offers directly on your homepage or in a dedicated promotional inbox. Pull in relevant content based on each customer’s previous purchases to deliver attention-grabbing personalized promotions.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### Other use cases

Outside of these main use cases, our customers use Content Cards in so many different ways. The power of Content Cards is their flexibility. If the use case you want is not shown here, you can set up [key-value pairs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) and get the payloads sent to your app or site.

## Content Card placements

This section provides an overview of the three most common ways to place Content Cards within your app or site:

- [Message inbox](#message-inbox)
- [Carousel](#carousel)
- [Banner](#banner)

The logic and implementation of these placements are not a default in Braze, and therefore the work for achieving these use cases must be supplied and supported by your engineering team. For an overview on how to implement these placements, refer to the [creating custom Content Card article]({{site.baseurl}}/developer_guide/customization_guides/content_cards/creating_custom_content_cards).

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Message inbox

![]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

A message inbox (also called a notification center or feed) is a persistent place in your app or website where you can display Content Cards in whatever format you prefer. Each message in the inbox is its own Content Card. 

The message inbox is a default implementation with minimal development needed—we provide a [view controller](#how-content-cards-work) for a message inbox on iOS, Android, and web that makes it easier to create this feature, powered by Content Cards.

#### Benefits

- Users can receive many cards in one place
- Easy way to resurface information missed or dismissed on other channels (especially push notifications)
- No opt-in required

#### Behavior

When a user is eligible for a card, it will automatically appear in their inbox. Content Cards are inherently built to be viewed in bulk, so users will be able to view all cards that they’re eligible for at once.

With the default implementation, Content Cards in the inbox can appear as classic (containing a title, text, and an optional image), image only, or captioned image cards. You choose where the message inbox will be located in your app.

Content Cards come with a default style, but you can choose a custom implementation to display the cards and the feed according to the look and feel of your app.

### Carousel

![]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Carousels display multiple pieces of content in a single space that your customers can swipe into view. They can be a slideshow of images, text, video, or a combination of all of them. This is a custom implementation and requires a bit of work from your developers.

#### Benefits

- Users can receive many cards in one place
- Engaging way to surface recommendations

#### Behavior

When a user is eligible for a card, it will appear in a carousel on whichever page of your app the carousel is added to. Users can swipe horizontally to view additional featured cards.

Because this is a custom implementation, you’ll need to work with your developers to build your own views to display the Content Cards. The default classic, image only, and captioned image cards are not supported with this implementation.

### Banner

![]({% image_buster /assets/img_archive/cc_placement_banner.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Content Cards can appear as a dynamic banner that persistently displays on your home page or at the top of other designated pages.

#### Benefits

- Persists on the page unlike an in-app message, so you have more time to reach your audience
- Great way to showcase new content in a prominent location on your home page

#### Behavior

Users can view and engage the most relevant content they are eligible for. Because this is a custom implementation, you’ll need to work with your developers to customize the views to display the Content Cards.

## How Content Cards work

At their core, Content Cards are actually a payload of data, not what the data looks like. Braze provides template views (banner, modal, captioned image) to display the Content Card data, which is ultimately what your message looks like.

Now let’s get a little technical. Behind the scenes, there are three main parts of a Content Card:

- **Model:** What kind of data lives in the card
- **View:** What the card looks like
- **Controller:** How the user interacts with the card

For a default implementation, you add the card content—the model—either from the dashboard or via APIs, and the view and controller are handled by what is called a view controller. A view controller is the "glue" between the overall application and the screen.

## Integrating Content Cards

Your developers will integrate Content Cards when they integrate the Braze SDK. For more details on how to integrate with Content Cards, refer to the developer guide articles for your platform:

- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/ "iOS Content Card Integration Guide")
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/ "Android Content Card Integration Guide")
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/ "Web Content Card Integration Guide")

## Sources

<span></span>

[^1]: [8 Tips for Making the Most of Your Customer Retention Campaigns](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Report: The Cross-Channel Marketing Difference](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)
