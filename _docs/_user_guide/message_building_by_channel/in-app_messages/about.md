---
nav_title: "About In-App Messages"
article_title: About In-App Messages
page_order: 0
page_type: reference
description: "This reference article gives a brief overview of in-app messages."
channel:
  - in-app messages

---

# About in-app messages

> This article covers ___. In addition to the content covered here, we also recommend checking out our [In-App and In-Browser Messages](https://lab.braze.com/messaging-channels-in-app-in-browser) LAB course.

In-app messages are good for a lot of things. They're content rich and have a lower sense of urgency, as these messages don't deliver outside of the user's app and won't intrude on their home screen. In-app messages exist within your app (hence the name), come with context, and are almost never unwelcome! They're always delivered when the user is active within your app.

To see examples of in-app messages, check out our [Case Studies][1].

## Potential use cases

With the rich level of content offered by in-app messages, you can leverage this channel for a variety of use cases:

| Use case | Explanation |
| --- | --- |
| Push priming | Run a [push priming][2] campaign using a rich in-app message to show your customers the benefit of opting into push for your app or site, and present them with a prompt to grant push permission.
| Sales and promotions | Use modal in-app messages to greet customers with visually appealing media containing promo codes or offers. Incentivize them to make purchases or conversions when they otherwise wouldn't have. |
| Encouraging feature adoption | Encourage customers to use other parts of your app or take advantage of a service. |
| Highly personalized campaigns | Place IAMs as the first thing your customers see when they enter your app/site. Add in some Braze personalization features, such as [Connected Content][3], to compel users to take action and therefore make your outreach more effective.
{: .reset-td-br-1 .reset-td-br-2}

Other use cases include the following:

- New app features
- App management
- Reviews
- App upgrades or updates
- Giveaways and sweepstakes

## Expected behaviors by message types

These are what it looks like for your users to open one of our out-of-the-box in-app message types.

{% tabs %}
{% tab Slideup %}

Slideups typically appear at the top and bottom of the app screen (you can set this when you create your message). These are great for alerting your users about new terms of service, cookies, and other snippets of information.

![Slideup Behavior]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

Modals appear in the center of the device's screen with a screen overlay that helps it stand out from your app in the background. These are great call-to-action These are perfect for not-so-subtly suggesting that your user take advantage of a sale or giveaway.

![Modal Behavior]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Full-Screen %}

Full-screen messages are exactly what you'd expect—they take up the whole screen of the device! This message type is great when you really need your user's attention, like for mandatory app updates.

![Full-Screen Behavior]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

[1]: https://www.braze.com/customers
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
