---
nav_title: Content Cards
article_title: Content Cards
page_order: 1
layout: dev_guide
guide_top_header: "Content Cards"
guide_top_text: "With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers within the apps they love without interrupting their experience. <br><br>Content Cards are embedded directly into your app or website, letting you create message inboxes and custom interfaces that extend the reach of other channels such as email or push notifications. Additionally, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, Connected Content, custom card expiration times, card analytics, and easy coordination with push notifications. <br><br>**Content Cards availability depends on your Braze package. Contact your account manager or customer success manager to get started.**"
description: "This landing page is home to Braze Content Cards. Here, you can find articles on how to create a Content Card, how to customize your Content Cards, testing, reporting, and more."
channel:
  - content cards
search_rank: 5
guide_featured_title: "Section articles"
guide_featured_list:
- name: Create a Content Card
  link: /docs/user_guide/message_building_by_channel/content_cards/create/
  image: /assets/img/braze_icons/columns-01.svg
- name: Card Creation
  link: /docs/user_guide/message_building_by_channel/content_cards/create/card_creation
  image: /assets/img/braze_icons/message-check-circle.svg
- name: Creative Details
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/
  image: /assets/img/braze_icons/brush-02.svg
- name: Testing
  link: /docs/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Reporting
  link: /docs/user_guide/message_building_by_channel/content_cards/reporting/
  image: /assets/img/braze_icons/pie-chart-01.svg
- name: Best Practices
  link: /docs/user_guide/message_building_by_channel/content_cards/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} Benefits of using Content Cards

Here are just a few benefits of using Content Cards versus having your developers build content into your app:

- **Easier segmentation and personalization:** Your user data lives in Braze, making it easy to define your audience and personalize your messages with Content Cards.
- **Centralized reporting:** Content Card analytics are tracked in Braze, so you have insight into all of your campaigns in one location.
- **Cohesive customer journeys:** You can combine Content Cards with other channels in Braze to create consistent customer experiences. A popular use case is sending a push notification, then saving that notification as a Content Card in your app for anyone who didn’t engage with the push. If the content is built directly into your app by your developers, then it’s isolated from the rest of your messaging.
- **No required opt-in:** Similar to in-app messages, Content Cards don't require opt-in or permissions from your users. But while in-app messages are permissionless and short-lived, Content Cards are permissionless and permanent. This means messaging strategies that pair together in-app messages and Content Cards strike a great balance.
- **More control over the messaging experience:** While you’ll still need your developers to help with the initial setup of Content Cards, afterward, you can control the message, recipients, timing, and more directly from your Braze dashboard.

### Content Cards by the numbers

Because you, the marketer, are building Content Cards yourself in Braze, you can make messaging updates and receive a return on investment without having to completely overhaul your app or website. Here are some helpful statistics on the ROI of Content Cards:

- Content Cards are **38X** more effective than emails at boosting sales over a 72-hour window.[^1]
- Using Content Cards in loyalty enrollment campaigns boosts conversions by **5X**.[^1]
- Sending users outreach through push notifications, in-app messages, and Content Cards results in **6.9X** more sessions, compared to users engaged through push alone.[^2]
- Sending users outreach through email, in-app messages, and Content Cards results in **3.6X** longer average user lifetime, compared to users engaged through email alone.[^2]

## How it works

Braze provides different Content Card types to display the Content Card: Classic, Captioned Image, or Image. At their core, Content Cards are actually a payload of data, not what the data looks like. 

Now let’s get a little technical. Behind the scenes, there are three main parts of a Content Card:

- **Model:** What kind of data lives in the card
- **View:** What the card looks like
- **Controller:** How the user interacts with the card

For a default implementation, you add the card content—the model—either from the dashboard or through APIs, and the view and controller are handled by what is called a view controller. A view controller is the "glue" between the overall application and the screen.

## Use cases

Refer to this section for some common use cases for Content Cards.

{% alert tip %}
For more inspiration, we highly recommend that you check out our [Content Cards Inspiration Guide](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), which includes over 20 customizable campaigns, including referral programs, new product launches, and subscription renewals.
{% endalert %}

{% tabs %}
{% tab Onboarding and next steps %}

As new users explore your app and website, walk them through the values and benefits of what you offer with strategically placed Content Cards. Encourage users to opt into other communication channels with a Content Card on your homepage, and save outstanding onboarding tasks in a dedicated onboarding tab powered by Content Cards. Don’t forget to remove a card after a user completes the desired task!

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

Showcase Content Cards at the top of a user’s homepage to encourage event attendance, using location targeting to reach potential users where they are. Inviting users to relevant physical events makes them feel special, especially with personalized messaging that leverages their previous activity with your brand.

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

Outside of these main use cases, our customers use Content Cards in so many different ways. The power of Content Cards is their flexibility. If the use case you want is not shown here, you can set up [key-value pairs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) and send the payloads to your app or website.

## Content Cards in your app

This section covers the most common ways to place Content Cards within your app or website:

- [Message inbox](#message-inbox)
- [Carousel](#carousel)

The logic and implementation of these placements are not a default in Braze, so your engineering team must supply and support the work for achieving these use cases. For an overview on how to implement these placements, refer to [Creating custom Content Card]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

![3 example content cards, showing the different placement options: message inbox, carousel, and banner.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Message inbox

![An example content card using the "message inbox" placement.]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

A message inbox (also called a notification center or feed) is a persistent place in your app or website where you can display Content Cards in whatever format you prefer. Each message in the inbox is its own Content Card. 

The message inbox is a default implementation with minimal development needed. Braze provides a [view controller](#how-it-works) for a message inbox on iOS, Android, and web to make the creation process easy.

#### Benefits

- Users can receive many cards in one place
- Efficient way to resurface information missed or dismissed on other channels (especially push notifications)
- No opt-in required

#### Behavior

When a user is eligible for a card, it will automatically appear in their inbox. Content Cards are built to be viewed in bulk, so users can view all cards that they’re eligible for at once.

With the default implementation, Content Cards in the inbox can appear as classic (containing a title, text, and an optional image), image only, or captioned image cards. You choose where the message inbox will be located in your app.

Content Cards come with a default style, but you can choose a custom implementation to display the cards and the feed according to the look and feel of your app.

### Carousel

![An example content card using the "carousel" placement.]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Carousels display multiple pieces of content in a single space that your customers can swipe into view. They can be a slideshow of images, text, video, or a combination of them. This is a custom implementation and requires a bit of work from your developers.

#### Benefits

- Users can receive many cards in one place
- Engaging way to surface recommendations

#### Behavior

When a user is eligible for a card, it will appear in a carousel on whichever page of your app the carousel is added to. Users can swipe horizontally to view additional featured cards.

Because this is a custom implementation, you’ll need to work with your developers to build your own views to display the Content Cards. The default classic, image only, and captioned image cards aren't supported with this implementation.

## Integrating Content Cards

Your developers will integrate Content Cards when they integrate the Braze SDK. For more details on how to integrate with Content Cards, refer to the developer guide articles for your platform:

- [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web)

## Sources

<span></span>

[^1]: [8 Tips for Making the Most of Your Customer Retention Campaigns](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Report: The Cross-Channel Marketing Difference](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)
