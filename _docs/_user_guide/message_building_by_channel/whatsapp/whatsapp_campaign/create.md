---
nav_title: Creating a WhatsApp Message
article_title: Creating a WhatsApp Message
page_order: 0
description: "This reference article covers the steps involved in building out and creating a WhatsApp message."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# Creating a WhatsApp message

> WhatsApp campaigns are great for directly reaching and programmatically conversing with your customers. You can use Liquid and other dynamic content to create a personal experience with your users and create an environment that fosters and enhances an unobtrusive user experience with your brand. 

## Prerequisites

Before you can create WhatsApp messages, you need to review and complete the following from the [WhatsApp overview]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/):
  - Acknowledge policies, limits, and content rules
  - Set up your WhatsApp connection
  - Build out initial templates in Meta to use in your messages

## Creating a message

### Step 1: Choose where to build your message

{% alert note %}
WhatsApp creates different [message templates](#template-messages) for each language. Either create a campaign for each language with segmentation to serve the correct template to users, or use Canvas. 
{% endalert %}

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}

**Steps:**

1. Go to the **Campaigns** page and click <i class="fas fa-plus"></i> **Create Campaign**.
2. Select **WhatsApp**, or, for campaigns targeting multiple channels, select **Multichannel Campaign**.
3. Name your campaign something clear and meaningful.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
If all of the messages in your campaign are similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Steps:**

1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas composer.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed.
4. Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
5. Choose your [advancement behavior]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choose any other messaging channels you want to pair with your message.

{% alert tip %}
If an action-based Canvas is triggered by an inbound WhatsApp message, you can reference WhatsApp properties in any Canvas step until the next action path.
{% endalert %}

{% endtab %}
{% endtabs %}

### Step 2: Compose your WhatsApp message

Select if you’d like to create a WhatsApp [template message](#template-messages) or response message, depending on your use case. Any business-initiated conversation must start from an approved template, whereas response messages can be used in responses to inbound messages from users within a 24-hour window.

![The Message Variants section lets you select a subscription group and one of two message types: WhatsApp Template Message and Response Message.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

#### Template messages

You can use [approved WhatsApp template messages]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
) to initiate conversations with your users on WhatsApp. These messages are submitted in advance to WhatsApp for content approval, which can take up to 24 hours to approve. Any edits you make to copy needs to be edited and resubmitted to WhatsApp.

Disabled text fields (highlighted gray) cannot be edited as they are part of the approved WhatsApp template. To make updates to the disabled text, you must edit your template and get it reapproved.

##### Languages

Each template has an assigned language, so you need to create a campaign or Canvas step for each language to correctly set up user matching. For example, if you're building a Canvas that uses templates assigned with Indonesian and English, you need to create a Canvas step for the Indonesian template and a Canvas step for the English template.

![List of templates including previews of their messages, their assigned languages, and their approved status.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

If you're adding copy in a language that is written right-to-left, note that the final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

##### Variables

If you added variables while creating the WhatsApp template in the Meta Business Manager, those variables will show up as blank spaces in the message composer. Replace these blank spaces with Liquid or plain text. To use plain text, use the format "text here" encased by double braces. If you opted to include images when building your template, you can upload or add images from the media library or by referencing an image URL.

Note that disabled text fields (highlighted gray) cannot be edited as they are part of the approved WhatsApp template. If you would like to make updates to the disabled text, you must edit your template and get it reapproved.

{% alert tip %}
{% raw %}
If you plan to use Liquid, be sure to include a default value for your chosen personalization so in the event your user profile of the recipient is incomplete, they will not receive a message. Any messages with missing Liquid variables will not be sent by WhatsApp.
{% endraw %}
{% endalert %}

![The Add Personalization tool with the attribute "first_name" and the default value "you".]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

#### Dynamic links 

Call-to-action URLs may contain variables, though Meta requires them to be at the end of the URL, such as `{% raw %}https://example.com/{{variable}}{% endraw %}`, where the variable can then be replaced in Braze with Liquid. Links can also be included as the body text as part of the template. At this time, neither of these links can be shortened. 

#### Response messages

You can use response messages to reply to inbound messages from your users. These messages are built in-app on Braze during your composition experience and can be edited at any time. You can use Liquid to match the response message language to the appropriate users.

There are five response message layouts you can use:
- Quick Reply
- Text Message
- Media Message
- Call-to-action Button
- List Message

![The response message composer for a Reply Message that welcomes new users with a discount code.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

### Step 3: Preview and test your message

Braze always recommends previewing and testing your message before sending it. Switch to the **Test** tab to send a test WhatsApp message to [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) or individual users, or preview the message as a user directly in Braze.

![A preview message for a custom user named Max.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
A conversation window is required to send response messages, including test messages. To initiate a conversation window, send a WhatsApp message to the phone number associated with the subscription group you’re using for this message. The associated phone number is listed in the alert on the **Test** tab.
{% endalert %}

![An alert that says, "To test, first open a conversation window by sending a WhatsApp message to +1 217-582-9414. Then, send your response message to the test user."]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

### Step 4: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Next, build the remainder of your campaign. See the following sections for further details on how to best use our tools to build WhatsApp messages.

#### Choose a delivery schedule or trigger

WhatsApp messages can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

For action-based delivery, you can also set the campaign's duration and [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

This step is also where you can specify delivery controls, such as allowing users to become [re-eligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) to receive the campaign, or enabling [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules.

#### Choose users to target

Next, you need to [target users]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) by choosing segments or filters to narrow down your audience. You should have already chosen the subscription group, which narrows users by the level or category of communication they wish to have with you. In this step, you will select the larger audience from your segments and narrow that segment further with our filters. You'll automatically be given a snapshot of what that approximate segment population looks like right now. Remember that exact segment membership is always calculated just before the message is sent.

{% multi_lang_include target_audiences.md %}

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), after receiving a campaign. You can allow up to a 30-day window during which a conversion will be counted if the user takes the specified action.

You can also set custom conversion events based on your specific use case. Get creative and think about how you truly want to measure this campaign's success.

{% endtab %}

{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas component. For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) step of our Canvas documentation.

Because conversation windows can only last 24 hours per inbound message, Braze will check to make sure there are no delays exceeding 24 hours between an inbound message and a response message. 

{% endtab %}
{% endtabs %}

### Step 5: Review and deploy

After you've finished building the last of your campaign or Canvas, review its details, test it, then send it!

Next, check out [WhatsApp reporting]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/) to learn how you can access the results of your WhatsApp campaigns.

## Supported WhatsApp features

### Outbound messages

The following features are supported for outbound WhatsApp messages you send through Braze:

| Feature | Details | Max Size | Supported Formats |
| ------- | ------- | ------------- | ---------------------- |
| Header text | Strings and variable parameters are supported. | — | —
| Body text | Strings and variable parameters are supported. | — | — |
| Footer text | Strings and variable parameters are supported. | — | — |
| CTA links | Various call-to-action (CTA) types are supported. For more details, see [Call-to-action types](#ctas). | — | — |
| Images | Images can be embedded within the body text. They must be 8-bit and use either an RGB or RGBA color model. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| Documents | Documents can embedded within body text. Files must be hosted through URL. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Videos | Videos can be embedded within body text. Files must be hosted through URL or in the [Braze media library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library). | < 16 MB | `.3gp`, `.mp4` |
| Audio | Audio is only supported through response messaging. Files must be hosted through URL. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Inbound messages

The following features are supported for inbound WhatsApp messages you receive through Braze:

| Feature | Details | Supported Formats |
| ------- | ------- | ------------------ |
| Body text | Only standard strings are supported. | — |
| Images | Images must be 8-bit and use either an RGB or RGBA color model. Files must be less than 5 MB. | `.jpg`, `.png` |
| Audio | Only Ogg files encoded with the Opus codec are supported. Other Ogg formats are not. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| Documents | Documents are supported through message attachment. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Video | Only H.264 video codec and AAC audio codec are supported. Videos must either have a single audio stream or no audio stream. | `.mp4`, `.3gp` |
| CTA links | Various call-to-action (CTA) types are supported. For more details, see [Call-to-action types](#ctas). | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Call-to-action types {#ctas}

The following call-to-action types are supported for WhatsApp messages you send through Braze:

| CTA type    | Details |
| ----------- |---------------- | 
| Visit website | One button maximum (including variable parameters). |
| Call phone number | Available for message templates only. <br>One button maximum. |
| Custom quick reply buttons | Three buttons maximum. |
| Marketing opt-out button | By default, subscription statuses are not automatically updated. For a full walkthrough, see [Opt-ins & Opt-Outs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection). |
| Coupon code message templates | Available for message templates only. <br>These can be opened and edited like other message templates, and are compatible with Liquid and Braze promotion codes. |
| CTA response messages  | Create a response message that includes a call to action button. |
| [List response messages]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#list-messages) | Create a response message that includes a list of up to 10 options for users to pick from. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

