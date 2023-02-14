---
nav_title: About Content Cards
article_title: About Content Cards
page_order: 0
description: "This reference article provides an overview of the Braze Content Card channel and common use cases."
channel:
  - content cards
search_rank: 4
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/messaging-channels-content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} About Content Cards

> This reference article provides an overview of the Braze Content Card channel and common use cases.

{% multi_lang_include video.html id="4FUPxkIq2xc" align="right" %}

With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love without interrupting their experience. In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, custom card expiration times, card analytics, and easy coordination with push notifications.

Content Cards are available as an add-on feature. To get started with Content Cards, reach out to your Braze customer success manager or our support team for more information.

{% alert note %}
If you're using our News Feed tool, we recommend that you move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. News Feed is being deprecated. See our [Migration Guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) or contact your Braze account manager for more information.
{% endalert %}

## When to use Content Cards 

Content Cards typically sit in a feed of sorts (but not necessarily), and help you take advantage of the visual space by incorporating images and graphics that stand out. You can personalize the cards based on user actions, onboard your customers with a checklist, and much more!

### Advantages of using Content Cards

Wondering about the benefits of using Content Cards versus having your tech team build content into your app? Here are some advantages of using Content Cards:

- **Easier segmentation and personalization:** Your user data lives in Braze, making it easy to define your audience and personalize your messages with Content Cards.
- **Centralized reporting:** Content Card analytics are tracked in Braze, so you have insight into all of your campaigns in one centralized location.
- **Cohesive customer journeys:** You can combine Content Cards with other channels in Braze to create consistent customer experiences. A popular use case is sending a push notification, then saving that notification as a Content Card in your app for anyone who didn't engage with the push. If the content is built directly into your app by your tech team, then it's siloed from the rest of your messaging.
- **More control over the messaging experience:** While you'll still need your tech team to help with the initial setup of Content Cards, after that, you'll be able to control the message, recipients, timing, and more straight from your Braze dashboard.

### Use cases

Here are some common use cases for Content Cards:

- Showcase new content.
- Coordinate with push messages to illustrate a persistent record of promotions.
- Give customers who don't have push enabled access to promotions.
- Trigger order confirmations or other personalized communication with your customer.
- Develop and deliver an onboarding schedule.

## Content Cards and feed

This is what it looks like for your users to open a standard Content Card feed. As you can see, three standard types of cards can sit in the feed—a Banner Card, a Captioned Content Card, and a Classic Content Card.

![Contents Card feed that shows the three standard types of cards.]({% image_buster /assets/img/cc_feed_new.png %}){: style="max-width:60%;border:none"}

{% alert note %}
Content Cards have a maximum size limit of 2 KB for content you enter in the Braze dashboard. This includes message text, image URLs, links, and key-value pairs. Exceeding that amount will prevent the card from sending.
{% endalert %}
