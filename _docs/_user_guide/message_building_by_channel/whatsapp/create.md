---
nav_title: Creating a WhatsApp message
article_title: Creating a WhatsApp message
page_order: 5
description: "This reference article covers the steps involved in building out and creating a WhatsApp message."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
hidden: true
---

# Creating a WhatsApp message

> WhatsApp campaigns are great for directly reaching and programmatically conversing with your customers. You can use Liquid and other dynamic content to create a personal experience with your users and create an environment that fosters and enhances an unobtrusive user experience with your brand. 

{% alert important %}
Support for the WhatsApp channel is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Prerequisites

To create a WhatsApp message and leverage the Whatsapp channel, you must first read through the WhatsApp [overview]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) and do the following:
  - Acknowledge policies, limits, and content rules
  - Set up your WhatsApp connection
  - Build out initial templates in Meta to use in your messages

## Step 1: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}

**Steps:**

1. Go to the **Campaigns** page and click <i class="fas fa-plus"></i> **Create Campaign**.
2. Select **WhatsApp**, or, for campaigns targeting multiple channels, select **Multichannel Campaign**.
3. Name your campaign something clear and meaningful.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Select a [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription) to ensure you’re sending your message to the proper users. When selecting a subscription group, Braze will automatically add a segmenting filter, ensuring that only users subscribed will receive the campaign.

{% alert tip %}
If all of the messages in your campaign are similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Steps:**

1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas wizard.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed.
4. Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
5. Choose your [advancement behavior]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choose any other messaging channels you want to pair with your message.

{% endtab %}
{% endtabs %}

## Step 2: Compose your WhatsApp message

To compose your message, select an [approved WhatsApp template]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates). 

![][1]

If you added variables while creating the WhatsApp template in the Meta Business Manager, those variables will show up as blank spaces in the message composer. Replace these blank spaces with Liquid. If you opted to include images when building your template, upload or add images from the media library. 

![][2]

Note that disabled text fields (highlighted gray) cannot be edited as they are part of the approved WhatsApp template. If you would like to make updates to the disabled text, you must edit your template and get it reapproved. 

{% alert tip %}
{% raw %}
If you plan to use Liquid, be sure to include a default value for your chosen personalization so in the event your user profile of the recipient is incomplete, they will not receive a blank placeholder `Hi, !` instead of their name or a coherent sentence.
{% endraw %}
{% endalert %}

## Step 3: Preview and test your message

Braze always recommends previewing and testing your message before sending it. Switch to the **Test** tab to send a test WhatsApp message to [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) or individual users, or preview the message as a user directly in Braze.

![][3]

## Step 4: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Next, build the remainder of your campaign. See the following sections for further details on how to best utilize our tools to build WhatsApp messages.

#### Choose a delivery schedule or trigger

WhatsApp messages can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

For action-based delivery, you can also set the campaign's duration and [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

This step is also where you can specify delivery controls, such as allowing users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) to receive the campaign, or enabling [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules.

#### Choose users to target

Next, you need to [target users]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) by choosing segments or filters to narrow down your audience. You should have already chosen the Subscription Group, which narrows users by the level or category of communication they wish to have with you. In this step, you will select the larger audience from your segments and narrow that segment further with our filters. You'll automatically be given a snapshot of what that approximate segment population looks like right now. Remember that exact segment membership is always calculated just before the message is sent.

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), after receiving a campaign. You can allow up to a 30-day window during which a conversion will be counted if the user takes the specified action.

You can also set custom conversion events based on your specific use case. Get creative and think about how you truly want to measure this campaign's success.

{% endtab %}

{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas component. For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.

{% endtab %}
{% endtabs %}

## Step 5: Review and deploy

After you've finished building the last of your campaign or Canvas, review its details, test it, then send it!

Next, check out [WhatsApp reporting]() to learn how you can access the results of your WhatsApp campaigns.

[1]: {% image_buster /assets/img/whatsapp/whatsapp6.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp7.png %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp8.png %} 