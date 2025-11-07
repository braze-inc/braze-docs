---
nav_title: Creating an SMS message
article_title: Creating an SMS message
page_order: 5
description: "This reference article covers the steps involved in building out and creating an SMS message."
page_type: reference
alias: /create_sms_message/
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# Creating an SMS message

> SMS campaigns are great for directly reaching and programmatically conversing with your customers. You can use Liquid and other dynamic content to create a personal experience with your users and create an environment that fosters and enhances an unobtrusive user experience with your brand. 

## Step 1: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, targeted messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}

**Steps:**

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **SMS**, or, for campaigns targeting multiple channels, select **Multichannel**.
3. Name your campaign something clear and meaningful.
4. Add [teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Select a [subscription group]({{site.baseurl}}/sms_rcs_subscription_groups/) to ensure you're sending your message to the proper users. When selecting a subscription group, Braze will automatically add a segmenting filter, ensuring that only users subscribed will receive the campaign. Only long codes and short codes that belong to that subscription group will be used to send SMS to target users.

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

## Step 2: Compose your SMS message

Write your message using languages and personalization (Liquid, Connected Content, and emojis) as needed. Be sure to adhere to our message copy limits to reduce your chances of overage charges.

{% alert important %}
Before proceeding, read our guidelines for [SMS message segments and copy limits]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/). SMS message segments are the character batches that phone carriers use to measure text messages. Messages are charged per message segment, so it's a good idea to understand the nuances of how messages will be split.
{% endalert %}

![SMS composer in Braze with the message "Hi first_name, we appreciate your support! Why not stop by one of our stores and show them this SMS for an exclusive discount? Reply STOP to stop receiving messages from us."]({% image_buster /assets/img/sms_campaign_compose.png %})

### Adding a contact card

You can add a contact card to your SMS message so customers can add your business and contact information to their device contacts. You can assign properties such as company name, phone number, address, email, and a small photo. Refer to [Contact cards]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) for details.

### Tips

#### Using Liquid

{% raw %}
If you plan to use Liquid, be sure to include a default value for your chosen personalization so, in the event your user profile of the recipient is incomplete, they will not receive a blank placeholder `Hi, !`, instead of their name or a coherent sentence.
{% endraw %}

#### Generating AI copy

Need help creating awesome copy? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Input a product name or description and the AI will generate human-like marketing copy for use in your messaging.

![Launch AI Copywriter button, located in the Message field of the SMS composer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Creating right-to-left messages

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Step 3: Preview and test your message

Braze always recommends previewing and testing your message before sending. Switch to the **Test** tab to send a test SMS to [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) or individual users, or preview the message as a user directly in Braze.

![Previewing SMS copy from the Test tab of the composer. In the profile section, the First Name field is set to "James". In the preview section, the SMS now reads "Hi James, we appreciate your support!"]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
If you'd like to test how many segments your SMS may be split into, test your copy length with our [SMS segment calculator]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).
{% endalert %}

## Step 4: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Next, build the remainder of your campaign. See the following sections for further details on how to best use our tools to build SMS messages.

#### Choose delivery schedule or trigger

SMS messages can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

For action-based delivery, you can also set the campaign's duration and [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

This step is also where you can specify delivery controls, such as allowing users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) to receive the campaign, or enabling [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules.

#### Choose users to target

Next, you need to [target users]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) by choosing segments or filters to narrow down your audience. You should have already chosen the subscription group, which narrows users by the level or category of communication they wish to have with you. 

{% multi_lang_include target_audiences.md %}

In this step, you will select the larger audience from your segments, and narrow that segment further with our filters, if you choose. You'll automatically be given a preview of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

{% alert tip %}
Interesting in SMS retargeting? Visit our SMS [retargeting article]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) to learn more. 
{% endalert %}

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

Conversion events help you measure the success of your campaign. For example:

- If you are using geotargeting to trigger an SMS message that has an end goal of the user making a purchase, set the conversion event to a `Purchase`.
- If you are attempting to drive the user to your app, set the conversion event to `Starts Session`.

You can also set custom conversion events based on your specific use case. Get creative and think about how you truly want to measure this campaign's success.

{% endtab %}

{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas component. For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.

{% endtab %}
{% endtabs %}

## Step 5: Review and deploy

After you've finished building the last of your campaign or Canvas, review its details, test it, then send it!

Next, check out [SMS reporting]({{site.baseurl}}/sms_mms_rcs_reporting/) to learn how you can access the results of your SMS campaigns.
