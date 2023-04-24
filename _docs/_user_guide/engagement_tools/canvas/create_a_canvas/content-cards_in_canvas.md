---
nav_title: Content Cards In Canvas
article_title: Content Cards in Canvas
page_order: 7
page_type: reference
description: "This reference article describes features and nuances specific to using Content Cards as a messaging channel within Canvas."
tool: Canvas
channel: content cards

---

# Content Cards in Canvas

Content Cards can be sent to your customers as part of their Canvas journey. This article describes features and nuances specific to using Content Cards as a messaging channel within Canvas.

As with other Canvas messaging channels, Content Cards will be sent to a user's device when they meet the audience and targeting criteria specified for its step. After the Content Card is sent, it will be available in each eligible user's feed the next time their cards feed is refreshed.

![][1]

Two options that will change how the Content Card step will interact with Canvas are its [Expiration](#content-card-expiration) and [Advancement Behavior](#advancement-behavior-options).

## Content Card expiration {#content-card-expiration}

When composing a new Content Card you have the option to choose when it should expire from the user's feed, based on its send time. The expiration time begins when a user reaches its Canvas component and the card is sent.

If a sent card expires before a user has viewed it in your app, it will be removed from their feed the next time their cards are refreshed.

{% alert important %}
The Content Card will be available until it expires, even if the user has moved to subsequent steps. If you do not want the Content Card to be live when the next steps in the Canvas are delivered, ensure that the expiration is shorter than the delay on subsequent steps.
{% endalert %}

## Advancement Behavior options {#advancement-behavior-options}

{% alert note %}
In Canvas Flow, Message components automatically advance all users who enter the step. There is no requirement to specify message advancement behavior, making configuring the overall step simpler. If you want to implement the **Advance when message sent** option, add a separate [Audience Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) to filter users that didn't receive the previous step.
{% endalert %}

The Advancement Behavior option allows you to control when a user should advance to their next eligible step. Steps that send [only Content Cards](#steps-with-in-content-cards-only) have different advancement options than [steps with multiple message types](#steps-with-multiple-message-channels) (push, email, etc.). For Content Cards in a Canvas Flow workflow, this option is set to always immediately advance the audience.

### Steps with Content Cards only {#steps-with-in-content-cards-only}

If a step contains only Content Cards (and no other messaging channel), you can control the advancement behavior with the following options:

| Option | Description |
|---|---|
| Advance When Message Sent | Users will advance to the next steps of the Canvas when the Content Card has been successfully sent. Use this option when you want users to advance only if the card will be sent and not aborted. |
| Immediately Advance Audience | Users will advance to the next steps of the Canvas when the Content Card sending is attempted. If the card is aborted and not sent, users will still advance to the next step. Use this option when you want users to advance regardless of whether the content card is sent successfully or aborted. |
{: .reset-td-br-1 .reset-td-br-2}

![][2]

### Components with multiple channels {#steps-with-multiple-message-channels}

Canvas components with a Content Card and another messaging channel have the following advancement options:

| Option | Description |
|---|---|
| Advance When Message Sent | Users will advance to the next steps of the Canvas when at least one of the message types in this step have been sent successfully.|
| Immediately Advance Audience | When this option is selected, everyone in the component's audience will advance to the next steps after the delay elapses, whether they have seen the noted message or not.  <br> <br> _Users must match the component's segment and filter criteria to advance to next steps._ |
{: .reset-td-br-1 .reset-td-br-2}

![][3]

## Reporting and analytics

After launching a Content Cards step in Canvas you can begin to analyze several different metrics for this step. These metrics include the number of messages sent, unique recipients, conversion rates, total revenue, and more.

![][4]

For more information on the available metrics and their definitions, see our [Report Metrics Glossary][6].

## Use cases

#### Promotional offers

Add cards to a user's feed as they qualify for specific promotions and advertisements. For example, if a user becomes eligible for a new offer after performing an action or making a purchase, using Canvas you can send them a Content Card, in addition to other messaging channels, so that the next time they open the app the offer is available to them.

#### Push notification inbox

There are times when a user may dismiss a push notification or delete an email, but you want to remind them or promote the offer in case they change their mind.

Using Canvas, you can add a component that sends both a Content Card and push notification to give users a persistent "inbox" of cards that align with promotional messages sent via push. 

#### Multiple feeds based on categories

You can separate your Content Cards into multiple feeds based on categories such as different topics users can browse, or transactional and marketing feeds. For more information on creating multiple feeds using key-value pairs, check out our guides for [Web SDK][7] and [Android SDK][8].


[1]: {% image_buster /assets/img_archive/content-cards-in-canvas.png %}
[2]: {% image_buster /assets/img_archive/content-cards-in-canvas-single-channel.png %}
[3]: {% image_buster /assets/img_archive/content-cards-in-canvas-multiple-channels.png %}
[4]: {% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %}
[6]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/multiple_feeds/
