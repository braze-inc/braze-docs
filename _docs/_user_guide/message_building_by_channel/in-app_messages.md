---
nav_title: "In-app messages"
article_title: In-App Messages
page_order: 2
alias: /in-app_messages/
layout: dev_guide
guide_top_header: "In-App Messages"
guide_top_text: "In-app messages help you get content to your user without interrupting their day with a push notification, as these messages don't deliver outside of the user's app and won't intrude on their home screen. <br><br>Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before. They come with context, have lower urgency, and are delivered when the user is active within your app. For examples of in-app messages, check out our <a href='https://www.braze.com/customers'>customer stories</a>."
description: "This landing page is home to all things in-app message. Here, you can find articles on how to create in-app messages, the drag-and-drop editor, how to customize your messages, reporting, and more."
channel:
  - in-app messages
search_rank: 5
guide_featured_title: "Popular articles"
guide_featured_list:
- name: "Drag-And-Drop Editor"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Traditional Editor"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Creative Details"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/
  image: /assets/img/braze_icons/brush-02.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: "Testing"
  link: /docs/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/
  image: /assets/img/braze_icons/beaker-02.svg
- name: "Reporting"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: "Dark Mode"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/dark-mode/
  image: /assets/img/braze_icons/phone-02.svg
- name: "App Store Rating Prompt"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/ios_app_rating_prompt/
  image: /assets/img/braze_icons/star-01.svg
- name: "Simple survey"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey/
  image: /assets/img/braze_icons/bar-chart-07.svg
- name: "Locales in Messages"
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: "Best Practices"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "FAQ"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} Potential use cases

With the rich level of content offered by in-app messages, you can leverage this channel for a variety of use cases:

| Use case | Explanation |
| --- | --- |
| Push priming | Run a [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) campaign using a rich in-app message to show your customers the benefit of opting into push for your app or site, and present them with a prompt to grant push permission.
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

<br>

{% endtab %}
{% tab Modal %}

Modals appear in the center of the device's screen with a screen overlay that helps it stand out from your app in the background. These are perfect for not-so-subtly suggesting that your user take advantage of a sale or giveaway.

![Modal in-app message appearing in the center of an app and website as a dialog. The modal includes an image, header, message body, and two buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Fullscreen %}

Fullscreen messages are exactly what you'd expect—they take up the whole screen of the device! This message type is great when you really need your user's attention, like for mandatory app updates.

![Fullscreen in-app message taking over an app screen. The fullscreen message includes a large image, header, message body, and two buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

In addition to these default message templates, you can also further customize your messaging using custom HTML in-app messages, web modals with CSS, or web email capture forms. For more information, refer to [Customization]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## More resources

Before you get started with creating your own in-app message campaigns—or using in-app messages in a multi-channel campaign—we highly recommend that you check out our [In-app message prep guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). This guide covers targeting, content, and conversion questions you should consider when building in-app messages.
