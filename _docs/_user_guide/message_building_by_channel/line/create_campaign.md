---
nav_title: Create a LINE Campaign
article_title: Create a LINE Campaign
description: "This article covers how to create a LINE campaign."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - LINE
---

# Create a LINE campaign

> LINE campaigns can directly reach and programmatically chat with your customers. You can use Liquid and other dynamic content to create a personal experience with your users, and create an environment that fosters and enhances an unobtrusive user experience with your brand.

## Prerequisites

Before creating a LINE message, do the following:

1. Read the LINE overview
2. Acknolwedge policies, limits, and content rules
3. [Set up your LINE connection]({{site.basesurl}}/user_guide/message_building_by_channel/line/line_setup/)

## Step 1: Choose where to build your message

If you're unsure whether to send your message through a campaign or Canvas, a campaign sends a single message while a Canvas can send multiple messages in a multi-step user journey.

### Campaign

1. Create a campaign and select **LINE**, or, for a campaign that targets multiple channels, select **Multichannel campaign**.
2. Give your campaign a unique and meaningful name, and add any teams and tags.
3. Add any necessary variants. You can select different platforms, message types, and layouts for each added variant. For more information on variants, check out [Multivariante and A/B testing]().
4. Seelct a subscription group to confirm you're sending your message to the correct users. Braze will automatically add a segmenting filter to make sure that only subscribed users will receive the campaign.

{% alert tip %}
If your messages are similar or have the same content across all variants, compose your message before adding additional variants. YOu can then select **Copy for Variant** from the **Add Variant** dropdown.
{% endalert %}

### Canvas

1. Create and set up a Canvas.
2. Add a Canvas step and give it a unique and meaningful name.
3. Select a step schedule and specify a delay if needed.
4. Filter your audience for his step as appropriate. YOu can refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time the messages are sent.
5. Select your advancement behavior.
6. Select other messaging channels you want to pair with your message.

## Step 2: Compose your LINE message

Write your message using langauges and personalization (such as Liquid or Connected Content) as needed. LINE allows up to five message bubbles in each message, which can be text or image messages.

![LINE composer with a message displayed in the preview.][1]{: style="max-width:70%;"}

{% alert tip %}
If you plan to use Liquid, be sure to include a default value for your personalization. This will prevent recipients with incomplete user profiles from receiving a blank placeholder. For example, instead of a user receiving the message "Hi, !", they might receive the message "Hi, new subscriber!".
{% endalert %}

## Step 3: Preview and test your message

Switch to the **Test** tab to send a test LINE message to content test groups or individual users, or preview the message as a user directly in Braze.

![The "Tests" tab displaying a preview of a test message.][2]

## Step 4: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Build the remainder of your campaign. Check out the following sections for further details on how to best use Braze to build LINE messages.

{% endtab %}
{% tab Canvas %}

If you haven’t already, complete the remaining sections of your Canvas. For further details on how to build the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to [Creating a Canvas](/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

{% endtab %}
{% endtabs %}

[1]: {% image_buster assets/img/line/line_composer.png %}
[2]: {% image_buster assets/img/line/test_preview.png %}