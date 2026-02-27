---
nav_title: Content Cards
article_title: Content Cards
page_order: 2
page_type: landing
description: "Send a dynamic stream of rich content to your users with Content Cards, embedded directly in your app or website."
channel:
  - content cards
search_rank: 5
---

# Content Cards

> With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers within the apps they love without interrupting their experience. Content Cards are embedded directly into your app or website, letting you create message inboxes and custom interfaces that extend the reach of other channels such as email or push notifications.

## Prerequisites

Content Cards availability depends on your Braze package. Contact your account manager or customer success manager to get started.

Before you can use Content Cards, you need to integrate the [Braze SDK]({{site.baseurl}}/developer_guide/content_cards/) into your app or website. No additional setup is required. To build your own UI instead, refer to the [Content Card customization guide]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/).

## Benefits of using Content Cards

Here are some benefits of using Content Cards versus having your developers build content into your app:

- **Easier segmentation and personalization:** Your user data lives in Braze, making it easy to define your audience and personalize your messages with Content Cards.
- **Centralized reporting:** Content Card analytics are tracked in Braze, so you have insight into all of your campaigns in one location.
- **Cohesive customer journeys:** You can combine Content Cards with other channels in Braze to create consistent customer experiences. A popular use case is sending a push notification, then saving that notification as a Content Card in your app for anyone who didn't engage with the push. If the content is built directly into your app by your developers, then it's isolated from the rest of your messaging.
- **No required opt-in:** Similar to in-app messages, Content Cards don't require opt-in or permissions from your users. But while in-app messages are permissionless and short-lived, Content Cards are permissionless and permanent. This means messaging strategies that pair together in-app messages and Content Cards strike a great balance.
- **More control over the messaging experience:** While you'll still need your developers to help with the initial setup of Content Cards, afterward, you can control the message, recipients, timing, and more directly from your Braze dashboard.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Use cases

Refer to this section for some common use cases for Content Cards.

{% alert tip %}
For more inspiration, refer to the [Content Cards Inspiration Guide](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), which includes over 20 customizable campaigns, including referral programs, new product launches, and subscription renewals.
{% endalert %}

{% tabs %}
{% tab Onboarding and next steps %}

As new users explore your app and website, walk them through the values and benefits of what you offer with strategically placed Content Cards. Encourage users to opt into other communication channels with a Content Card on your homepage, and save outstanding onboarding tasks in a dedicated onboarding tab powered by Content Cards. Don't forget to remove a card after a user completes the desired task!

![Content Card onboarding use case example.]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab Event attendance %}

Showcase Content Cards at the top of a user's homepage to encourage event attendance, using location targeting to reach potential users where they are. Inviting users to relevant physical events makes them feel special, especially with personalized messaging that leverages their previous activity with your brand.

![Content Card event attendance use case example.]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab Recommendations %}

Use the data you have on user behaviors and preferences to surface relevant content in real time from homepage or inbox Content Cards and draw them back into your product offering.

![Content Card recommendations use case example.]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab Sales and promotions %}

Take advantage of Content Cards to highlight promotional messages and unclaimed offers directly on your homepage or in a dedicated promotional inbox. Pull in relevant content based on each customer's previous purchases to deliver attention-grabbing personalized promotions.

![Content Card sales and promotions use case example.]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### Other use cases

Outside of these main use cases, customers use Content Cards in many different ways. The power of Content Cards is their flexibility. If the use case you want is not shown here, you can set up [key-value pairs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) and send the payloads to your app or website.

For an overview on how to implement Content Card placements in your app or website, refer to [Creating custom Content Cards]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

## Next steps

- [Create a Content Card]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/)
- [Creative details]({{site.baseurl}}/user_guide/channels/content_cards/creative_details/)
