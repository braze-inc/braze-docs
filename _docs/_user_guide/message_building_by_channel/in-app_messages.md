---
nav_title: "In-app messages"
article_title: In-App Messages
page_order: 2
alias: /in-app_messages/
description: "This landing page is home to all things in-app message. Here, you can find articles on how to create in-app messages, the drag-and-drop editor, how to customize your messages, reporting, and more."
channel:
  - in-app messages
search_rank: 5
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} In-app messages

> In-app messages help you get content to your user without interrupting their day with a push notification, as these messages don't deliver outside of the user's app and won't intrude on their home screen. 

Customized and tailored in-app messages enhance the user experience and help your audience get the most value out of your app. With a variety of layouts and customization tools to choose from, in-app messages engage your users more than ever before. They come with context, have lower urgency, and are delivered when the user is active within your app. For examples of in-app messages, check out our [customer stories](https://www.braze.com/customers/).

## Potential use cases

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

In addition to these default message templates, you can also further customize your messaging using custom HTML in-app messages, web modals with CSS, or web email capture forms. For more information, refer to [Customization]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Templated in-app messages

In-app messages will be delivered as templated in-app messages when **Re-evaluate campaign eligibility before displaying** is selected or if any of the following Liquid tags exist in the message:

- `canvas_entry_properties`
- `connected_content`
- SMS variables such as {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

This means during session start, the device will receive the trigger of that in-app message instead of the entire message. When the user triggers the in-app message, the user's device will make a network request to fetch the actual message.

{% alert note %}
The message will not deliver if the device doesn't have access to the internet. The message might not deliver if the Liquid logic takes too long to resolve.
{% endalert %}

## Abort behavior

At Braze, an abort occurs when a user takes an action that makes them eligible to receive a message, but they don't receive the message because its Liquid logic marks them as ineligible. For example:

1. Sam performs an action which should trigger an email campaign.
2. The email’s body contains Liquid logic that says if a custom attribute score is less than 50, do not send this email.
3. Sam's custom attribute score is 20.
4. Braze recognizes that Sam shouldn’t receive this email, and the email is aborted.
5. An abort event is logged.

However, because in-app messages are a pull channel, aborts work a little differently for them.

### In-app message abort behavior

In-app messages are pulled in by the device at session start and cached on the device, so regardless of Internet connection quality, the message can be delivered instantly to the user. For example, if a user receives five in-app messages within their session, they will receive all five on session start. The messages will be cached locally and appear when their defined trigger events occur (session start, user clicks a button which logs a custom event, or other).

In other words, the logic that determines if we should abort an in-app message occurs **before** the trigger has occurred. To demonstrate this, let's say Sam from the email example is subscribed to push notifications.

1. Sam starts a session by launching a Braze-powered app on their phone.
2. Based on the audience criteria of the active campaigns in the workspace, Sam could be eligible for five different campaigns. All five are pulled into their phone and cached.
3. Sam **has not** performed any actions that would trigger these messages, but they could receive those messages in the session.
4. The Liquid in two of the in-app messages has rules that exclude Sam from receiving the message (such as their score custom attribute not being high enough).
5. Sam is not sent the two in-app messages that exclude them, but they are sent the other three messages.
6. No abort events are logged.

Braze doesn't log any abort events in Sam's case because this doesn't fulfill our definition of an abort; Sam **did not** perform any actions that would trigger the messages. In other words, when it comes to in-app messages, users never actually perform the trigger before Braze determines they shouldn’t see the message.

#### Templated in-app message abort behavior

[Templated in-app messages](#templated-in-app-messages) force the SDK to reevaluate if a message should display when the trigger event occurs. This has a different abort behavior. To demonstrate, let's consider this example:

1. Sam starts a Braze session by launching a Braze-powered app on their phone.
2. The audience criteria of the active campaigns say Sam could be eligible for a templated in-app message, so the trigger information is sent to their device without the message payload.
3. Sam selects a button that logs a custom event, triggering the templated in-app message.
4. Sam's device makes a network request to fetch the in-app message.
5. The message's Liquid logic leads to an abort, so Braze logs this as an abort; Sam performed the trigger action prior to this evaluation.

##### Comparing in-app message abort behavior

This table compares the in-app message flows that Sam experienced:

| In-app message | Abort behavior |
| --- | --- |
| Standard | An abort event was not logged because Sam didn't perform any actions that would trigger a message.<br><br>Standard in-app messages don’t log aborts because the definition of an abort is “didn’t see the message despite performing the trigger action.” Because in-app messages are delivered to the device before the trigger actions occur, it doesn’t make sense to consider in-app messages omitted because of Liquid logic. |
| Templated | An abort event was logged because Sam performed the trigger action to trigger the templated in-app message but received an abort in the Liquid templating. <br><br>Templated in-app messages log aborts because the Liquid evaluation occurs after the trigger action has been performed. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## More resources

Before you get started with creating your own in-app message campaigns—or using in-app messages in a multi-channel campaign—we highly recommend that you check out our [In-app message prep guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). This guide covers targeting, content, and conversion questions you should consider when building in-app messages.
