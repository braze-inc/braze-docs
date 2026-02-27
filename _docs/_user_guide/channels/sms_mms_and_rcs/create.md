---
nav_title: Create a message
article_title: Create an SMS, MMS, or RCS message
page_order: 4
description: "This article covers how to create and send an SMS, MMS, or RCS message in Braze."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# Create an SMS, MMS, or RCS message

> SMS, MMS, and RCS campaigns are great for directly reaching and programmatically conversing with your customers. You can use Liquid and other dynamic content to create a personal experience with your users and create an environment that fosters and enhances an unobtrusive user experience with your brand.

## Step 1: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, targeted messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **SMS/MMS/RCS**, or, for campaigns targeting multiple channels, select **Multichannel**.
3. Name your campaign something clear and meaningful.
4. Add [teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
   * Braze allows you to include both SMS and RCS variants within a single campaign, so you can compare the performance of each.

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas composer.
2. After you've set up your Canvas, add an **SMS/MMS/RCS** Message step in the Canvas builder.
3. Name your step something clear and meaningful.
4. Choose a [step schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed.
5. Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
6. Choose your [advancement behavior]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
7. Choose any other messaging channels which you would like to pair with your message.

{% endtab %}
{% endtabs %}

## Step 2: Select a subscription group

Select a [subscription group]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/subscription_groups/) to ensure you're sending your message to the proper users. When selecting a subscription group, Braze will automatically add a segmenting filter, ensuring that only subscribed users will receive the campaign.

The subscription group you select determines which message types are available in the composer:

| Subscription group type | Available message types |
| --- | --- |
| SMS-only | SMS |
| SMS with MMS-enabled numbers | SMS and MMS |
| RCS-enabled (with RCS-verified sender) | SMS, MMS (if enabled), and RCS |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Braze strongly recommends that every subscription group containing an RCS sender also includes at least one SMS code for fallback. This ensures that if an RCS message fails to deliver (for example, due to device incompatibility or incomplete carrier coverage), the message still reaches your user through SMS.
{% endalert %}

After selecting your subscription group, choose the message type you'd like to compose. If your subscription group supports multiple types, you'll see options to select between them.

![Options to select from an RCS or SMS/MMS message type.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

## Step 3: Compose your message

The compose experience changes depending on which message type you selected. Select the tab for your message type.

{% tabs local %}
{% tab SMS %}

Write your message using languages and personalization (Liquid, Connected Content, and emojis) as needed. Be sure to adhere to our message copy limits to reduce your chances of overage charges.

{% alert important %}
Before proceeding, read the guidelines for [SMS message segments and copy limits]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/segments/). SMS message segments are the character batches that phone carriers use to measure text messages. Messages are charged per message segment, so it's a good idea to understand the nuances of how messages will be split.
{% endalert %}

![SMS composer in Braze with the message "Hi first_name, we appreciate your support! Why not stop by one of our stores and show them this SMS for an exclusive discount? Reply STOP to stop receiving messages from us."]({% image_buster /assets/img/sms_campaign_compose.png %})

### Adding a contact card

You can add a contact card to your SMS message so customers can add your business and contact information to their device contacts. You can assign properties such as company name, phone number, address, email, and a small photo. Refer to [Contact cards]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/mms/contact_card/) for details.

{% endtab %}
{% tab MMS %}

To send an MMS message, your subscription group must have at least one MMS-enabled phone number. This is indicated by an **MMS** tag next to the subscription group in the composer.

Enter your message body, then upload a PNG, JPEG, or GIF image from the [media library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) or specify an image URL. Only one image is supported per message.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

![The compose tab for writing an MMS message.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Image specifications

| Property | Recommendation |
| --- | --- |
| Size | Up to 600&nbsp;KB |
| File types | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Contact cards

You can also include a [contact card]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/mms/contact_card/) (vCard) instead of an image.

### Carrier behavior

MMS messages are billed at a different rate than text-only SMS. Not all carriers can accept MMS. In these cases, the MMS is automatically converted to an image link the user can select.

{% endtab %}
{% tab RCS %}

Choose between a **Text** or **Media** message type.

![Options to select from a Text or Media message type.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% subtabs %}
{% subtab Text %}

RCS text messages focus on text as a medium. Messages up to 160 characters are billed as a basic RCS message. Messages exceeding 160 characters or using a rich element are billed as a rich (single) RCS message, with a character limit of 3,072.

**Features:**

- All SMS features are included, with advanced tracking available for URL click tracking.
- **Suggested replies**: Buttons containing suggested responses that users can select to pre-populate in their text input.
- **Suggested actions**: Buttons that initiate an action on the user's device. Braze currently supports OpenURL suggested actions, which redirect users to a webpage or other URL-identified location.

![Three suggested actions for an RCS message promoting trending fashion styles.]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

**Considerations:**

- You can add up to five buttons per message. These can be either suggested actions or suggested replies.
- In some cases, it can be more cost-effective to send longer text-only messages through RCS than with SMS, because longer SMS messages are broken into multiple billable segments, whereas RCS messages are billed per message.

{% endsubtab %}
{% subtab Media %}

RCS media messages allow you to use engaging media formats that aren't possible with SMS, including image, video, and document files.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

**Features:**

- Supports everything available in text message types, including text, suggested replies, and suggested actions.
- Image files (JPEG, PNG) uploaded from the [media library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/).
- Video files (MP4, MPEG, MV4) added by URL in the message composer.
- Document files (PDF) added by URL in the message composer.

![RCS composer with an option to upload a media file.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

**File specifications:**

| File type | Specifications |
| --- | --- |
| All | File size limited to 100 MB. File URL can have up to 2,048 characters. |
| Image | Supported formats: JPG, JPEG, GIF |
| Video | Supported formats: H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Document | Supported format: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Considerations:**

The user experience of receiving RCS messages may vary based on carrier coverage, mobile device hardware, and operating system. RCS integrates more naturally with Android devices, and different devices may render the experience at different speeds and qualities.

{% endsubtab %}
{% endsubtabs %}

Write your message using languages and personalization ([Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), and emojis) as needed. Be sure to adhere to message copy limits to reduce your chances of overage charges.

{% alert important %}
Before proceeding, read the [RCS message type guidelines](#step-3-compose-your-message) above. RCS messages are [charged per message]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/billing_calculator/), so it's a good idea to understand what can be included in each type.
{% endalert %}

{% endtab %}
{% endtabs %}

### Tips

#### Using Liquid

{% raw %}
If you plan to use Liquid, be sure to include a default value for your chosen personalization so, in the event your user's profile is incomplete, they will not receive a blank placeholder `Hi, !` instead of their name or a coherent sentence.
{% endraw %}

#### Generating AI copy

Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Input a product name or description, and the AI will generate human-like marketing copy for use in your messaging.

![Launch AI Copywriter button, located in the Message field of the SMS composer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Creating right-to-left messages

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Step 4: Preview and test your message

Braze always recommends previewing and testing your message before sending. Switch to the **Test** tab to send a test SMS, MMS, or RCS message to [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) or individual users, or preview the message as a user directly in Braze.

![Previewing SMS copy from the Test tab of the composer. In the profile section, the First Name field is set to "James". In the preview section, the SMS now reads "Hi James, we appreciate your support!"]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
If you'd like to test how many segments your SMS may be split into, test your copy length with the [SMS segment calculator]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator).
{% endalert %}

{% alert note %}
For MMS, the ordering of assets (image and message body) cannot be customized. The ordering is dependent on the phone receiving the message.
{% endalert %}

{% alert note %}
Because RCS rendering is controlled by the user's operating system, device manufacturer, carrier, and messaging app (for example, Google Messages vs. Apple Messages), message appearance can vary. The preview shown in Braze may not exactly match what an end user receives. Validate the final rendering on real devices whenever possible.
{% endalert %}

## Step 5: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Next, build the remainder of your campaign. Refer to the following sections for further details on how to best use our tools to build your message.

#### Choose delivery schedule or trigger

Messages can be delivered based on a scheduled time, an action, or an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

For action-based delivery, you can also set the campaign's duration and [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

This step is also where you can specify delivery controls, such as allowing users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) to receive the campaign, or enabling [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules.

#### Choose users to target

Next, [target users]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) by choosing segments or filters to narrow down your audience. You should have already chosen the subscription group, which narrows users by the level or category of communication they wish to have with you.

{% multi_lang_include target_audiences.md %}

Select the larger audience from your segments, and narrow that segment further with optional filters. You automatically receive a preview of what that approximate segment population looks like. Keep in mind that exact segment membership is always calculated before the message is sent.

{% alert tip %}
Interested in retargeting? Refer to [User retargeting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) to learn more.
{% endalert %}

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

Conversion events help you measure the success of your campaign. For example:

- If you are using geotargeting to trigger a message that has an end goal of the user making a purchase, set the conversion event to a `Purchase`.
- If you are attempting to drive the user to your app, set the conversion event to `Starts Session`.

You can also set custom conversion events based on your specific use case.

{% endtab %}
{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas component. For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.

{% endtab %}
{% endtabs %}

## Step 6: Review and deploy

After you've finished building the last of your campaign or Canvas, review its details, test it, then send it!

Next, check out [SMS, MMS, and RCS reporting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting/) to learn how you can access the results of your campaigns.
