---
nav_title: "In-app messages"
article_title: In-app messages
page_order: 5
page_type: landing
alias: /in-app_messages/
description: "Engage users with customized in-app messages that enhance the user experience using a variety of layouts and personalization tools in Braze."
channel:
  - in-app messages
search_rank: 5
---

# In-app messages

> In-app messages help you get content to your users without interrupting their day with a push notification. Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before.

## Prerequisites

Before you can send in-app messages, you need to integrate the [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) into your app or website. No additional setup is required.

For minimum SDK versions and feature-specific requirements, refer to:
- [Drag-and-drop editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
- [Message types]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/)

## Use cases

With the rich level of content offered by in-app messages, you can leverage this channel for a variety of use cases:

| Use case | Explanation |
| --- | --- |
| Push priming | Run a [push priming]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/) campaign using a rich in-app message to show your customers the benefit of opting into push for your app or site, and present them with a prompt to grant push permission.
| Sales and promotions | Use modal in-app messages to greet customers with visually appealing media containing static promotion codes or offers. Incentivize them to make purchases or conversions when they otherwise wouldn't have. |
| Encouraging feature adoption | Encourage customers to use other parts of your app or take advantage of a service. |
| Highly personalized campaigns | Place in-app messages as the first thing your customers see when they enter your app or site. Add in some Braze personalization features, such as [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), to compel users to take action and therefore make your outreach more effective.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Other use cases to consider include the following:

- New app features
- App management
- Reviews
- App upgrades or updates
- Giveaways and sweepstakes

## Standard message types

The following tabs show what it looks like for your users to open one of our standard in-app message types—slide-up, modal, and fullscreen in-app messages.

{% tabs %}
{% tab Slideup %}

Slide-up messages typically appear at the top and bottom of the app screen (you can set this when you create your message). These are great for alerting your users about new terms of service, cookies, and other snippets of information.

![Slideup in-app message appearing from the bottom of the app screen. The slide-up includes an icon image and a brief message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Modals appear in the center of the device's screen with a screen overlay that helps it stand out from your app in the background. These are perfect for not-so-subtly suggesting that your user take advantage of a sale or giveaway.

![Modal in-app message appearing in the center of an app and website as a dialog. The modal includes an image, header, message body, and two buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fullscreen %}

Fullscreen messages are exactly what you'd expect—they take up the whole screen of the device! This message type is great when you really need your user's attention, like for mandatory app updates.

![Fullscreen in-app message taking over an app screen. The fullscreen message includes a large image, header, message body, and two buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

In addition to these default message templates, you can also further customize your messaging using custom HTML in-app messages, web modals with CSS, or web email capture forms. For more information, refer to [Customization]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/).

## Next steps

- [Create an in-app message with the drag-and-drop editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
- [Create an in-app message with the traditional editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}
