---
nav_title: Creating a LINE message
article_title: Creating a LINE Message
page_order: 1
description: "This article covers how to create a LINE message campaign or Canvas."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# Creating a LINE message

> LINE campaigns can directly reach and programmatically chat with your customers. You can use Liquid and other dynamic content to create a personal experience with your users and create an environment that fosters and enhances an unobtrusive user experience with your brand.

## Prerequisites

Before creating a LINE message, do the following:

1. Read the LINE overview.
2. Acknowledge policies, limits, and content rules.
3. [Set up your LINE connection]({{site.basesurl}}/user_guide/message_building_by_channel/line/line_setup/).

Sending LINE messages from Braze will draw from your account's Message Credits.

## Step 1: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}

**Steps:**

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **LINE**, or, for campaigns targeting multiple channels, select **Multichannel Campaign**.
3. Name your campaign something clear and meaningful.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Steps:**

1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas composer.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed.
4. Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
5. Choose your [advancement behavior]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choose any other messaging channels which you would like to pair with your message.

{% endtab %}
{% endtabs %}

## Step 2: Compose your LINE message

Write your message using personalization (such as Liquid or Connected Content) as needed. LINE allows up to five message bubbles in each message, which can be any of the available messages layouts: text, image, rich, or card-based.

![LINE composer with a message displayed in the preview.]({% image_buster /assets/img/line/line_composer.png %})

### Tips

#### Using Liquid

If you plan to use Liquid, be sure to include a default value for your personalization. This will prevent recipients with incomplete user profiles from receiving a blank placeholder. For example, instead of a user receiving the message "Hi, !", they might receive the message "Hi, new subscriber!".

#### Creating right-to-left messages

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Step 3: Preview and test your message

Switch to the **Test** tab to send a test LINE message to content test groups or individual users, or preview the message as a user directly in Braze.

![The "Tests" tab displaying a preview of a test message.]({% image_buster /assets/img/line/test_preview.png %})

## Step 4: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Build the remainder of your campaign. See the following sections for further details on how to best use our tools to build LINE messages.

### Choose delivery schedule or trigger

LINE messages can be delivered based on a scheduled time, an action, or an API trigger. For more about scheduling and trigger options, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

You can specify delivery controls, such as allowing users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) to receive the campaign, or turning on [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules. For action-based delivery, you can also set the campaign's duration and [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

### Choose users to target

[Target users]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) by choosing segments or filters to narrow down your audience. You should have already chosen the subscription group, which narrows users by the level or category of communication they wish to have with you. 

Select the larger audience from your segments, and optionally narrow that segment further with our [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). You'll automatically be given a snapshot of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

Conversion events help you measure the success of your campaign. For example:

- If you are using geotargeting to trigger a LINE message that has an end goal of the user making a purchase, set the conversion event to a `Purchase`.
- If you're trying to drive the user to your app, set the conversion event to `Starts Session`.

You can also set custom conversion events based on your specific use case. Get creative and think about how you want to measure this campaign's success.

{% endtab %}
{% tab Canvas %}

If you haven’t already, complete the remaining sections of your Canvas. For further details on how to build the rest of your Canvas, use multivariate testing and Intelligent Selection, and more, refer to [Creating a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

{% endtab %}
{% endtabs %}

## Step 5: Review and deploy

After you’ve finished building the last of your campaign or Canvas, review its details, test it, then send it!

Next, check out [LINE reporting]({{site.baseurl}}/line/reporting/) to learn how you can access the results of your LINE campaigns.


