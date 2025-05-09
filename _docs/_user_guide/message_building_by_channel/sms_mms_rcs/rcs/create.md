---
nav_title: "Creating an RCS Message"
article_title: Creating an RCS Message
page_order: 2
alias: /create_rcs_message/
description: "This article covers how to create an RCS Message."
page_type: reference
channel:
  - RCS
---

# Creating an RCS message

> RCS campaigns are great for directly reaching and programmatically conversing with your customers. You can use Liquid and other dynamic content to create a personal experience with your users and create an environment that fosters and enhances an unobtrusive user experience with your brand.

## Step 1: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}
1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **SMS/MMS/RCS**, or, for campaigns targeting multiple channels, select **Multichannel**.
3. Name your campaign something clear and meaningful.
4. Add [teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **SMS and RCS variant testing**: Braze allows you to include both SMS and RCS variants within a single campaign, allowing you to compare the performance of each. You can add SMS and RCS variants during the first step of the message composition.

{: start="6"} 
6. Select an RCS-enabled [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/). When selecting a subscription group, Braze will automatically add a segmenting filter, ensuring that only users subscribed will receive the campaign. Only long codes and short codes that belong to that subscription group will be used to send SMS to target users.
- **SMS fallback**: Braze strongly recommends that every subscription group that contains an RCS sender also includes at least one SMS code for fallback. This is important for deliverability in cases RCS messages fail to deliver. Some reasons for this may include user device incompatibility and incomplete carrier coverage in a given country or region. By enabling SMS fallback, your message will still deliver to your user and that you never miss that opportunity to connect with them.   

{: start="7"}
7. Choose between SMS and RCS. Before composing RCS messages, choose the channel you send with. We generally recommend using RCS wherever possible as there are significant user engagement benefits over SMS; however, we always provide the option of sending with SMS so that you have maximum flexibility and control. 

![Options to select from an RCS or SMS/MMS message type.]({% image_buster /assets/img/rcs/rcs_message_type.png %})

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Steps:**

1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas composer.
2. After you've set up your Canvas, add an **SMS/MMS/RCS** Message step in the Canvas builder. 
3. Name your step something clear and meaningful.

{: start="4"}
4. Select an RCS-enabled [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/). When selecting a subscription group, Braze will automatically add a segmenting filter, ensuring that only users subscribed will receive the campaign. Only long codes and short codes that belong to that subscription group will be used to target users.
- **SMS fallback**: Braze strongly recommends that every subscription group that contains an RCS sender also includes at least one SMS code for fallback. This is important for deliverability in cases RCS messages fail to deliver. Some reasons for this may include user device incompatibility and incomplete carrier coverage in a given country or region. By enabling SMS fallback, your message will still deliver to your user and that you never miss that opportunity to connect with them.

{: start="5"}
5. Choose between SMS and RCS. Before composing RCS messages, choose the channel you send with. We generally recommend using RCS wherever possible as there are significant user engagement benefits over SMS; however, we always provide the option of sending with SMS so that you have maximum flexibility and control. 

![Options to select from an RCS or SMS/MMS message type.]({% image_buster /assets/img/rcs/rcs_message_type.png %})

{% endtab %}
{% endtabs %}

## Step 2: Select your RCS message type

Choose your RCS message type. Currently, the options are **Text** and **Media**.

![Options to select from a Text or Media message type.]({% image_buster /assets/img/rcs/rcs_text_media.png %})

### Text message type 

As implied by the name, RCS text messages are focused on text as a medium. If you type up to 160 characters, the RCS message is billed as a text-only (or "basic") message. If you exceed 160 characters or use a rich element, the message is billed as a rich (or "single") RCS message (and the character limit increases to 3072 characters). 

#### Features

- Text message types include all SMS features. Only Advanced Tracking is possible for URL click tracking to give you user-level reporting granularity. 
- In addition, you now have the option to include engaging **Suggested Replies** and **Suggested Actions** buttons that drive high-engagement user actions, such as visiting a landing page or placing an order. 
    - **Suggested Replies** are buttons containing suggested responses for users to click and pre-populate in their text input, removing the friction of having to think of a response by providing a constrained set of choices for them. 
    - **Suggested Actions** are buttons that initiate an action on the user’s device. They typically consist of one of two descriptive words and a visual icon to help the user understand what the button does. Braze currently supports OpenURL Suggested Actions. This functions similarly to a URL, where users who select the button are redirected to a webpage or other URL-identified location. 

![A GIF of three Suggested Actions for an RCS message promoting trending fashion styles: "Fairytale royalty", "Edgy academia", and "Show me your other styles".]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %})

#### Considerations

- For character limits on text, you may write up to 160 characters for a text-only (basic)RCS message or up to 3072 for a rich (single) RCS message. 
- For button limits, you may add up to five buttons per message. These buttons can be either suggested actions or suggested replies.
- Longer text blocks and too many buttons can frustrate users, so wherever possible we recommend leaning into simplicity. 
- In some cases, it can be more cost effective to send longer text-only messages through RCS than with SMS. This is because longer SMS messages are broken down into multiple segments, each of which are billable, whereas RCS messages are instead billed per message. Contact your Braze account team for more details and guidance. 

### Media message type

RCS media messages allow you to use engaging media formats that are not possible with SMS. These include image, video, and document files. These media options exist to help you engage your audience even more deeply and enable entirely new use cases. At the moment, only image uploading is supported through the [Media Library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). 

#### Features

- Media message types support everything that is available in text message types, which includes text, suggested replies, and suggested actions.
- Supports image files, including JPEG and PNG file formats. Image files are available through upload from the Media Library. 
- Supports video files, including MP4, MPEG, and MV4 file formats. Video files can be added by URL directly in the message composer. 
- Supports document files in the PDF file format. Document files can be added through the URL directly in the message composer. 

![RCS composer with an option to upload a media file.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

#### File specifications

| File type | Specifications |
| --- | --- |
| All | - File size is limited to 100 MB <br><br>- File URL can have up to 2048 characters |
| Image files | Supported file formats include JPG, JPEG, and GIF
| Video files | Supported file formats include H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Document files | Supported file formats: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Considerations

The user experience of receiving RCS messages may vary slightly based on a number of factors, including carrier coverage in the destination country, mobile device hardware, and mobile device operating system. 

Generally speaking, RCS integrates more naturally with Android devices (this method was largely implemented by Google and peer-to-peer RCS messaging is broadly adopted among the Android community). Different devices may render the experience at different speeds and qualities.  

## Step 3: Compose your RCS message

Write your message using languages and personalization (Liquid, Connected Content, and emojis) as needed. Be sure to adhere to our message copy limits to reduce your chances of overage charges.

{% alert important %}
Before proceeding, read our guidelines for RCS message limits. RCS messages are charged per message, so it’s a good idea to understand the nuances of what can be included in each type of RCS message.
{% endalert %}

## Step 4: Preview and test your message

Braze always recommends previewing and testing your message before sending. Go to the **Test** tab to send a test RCS to content test groups or individual users, or preview the message as a user directly in Braze.

## Step 5: Build the remainder of your campaign or Canvas

Next, build the remainder of your campaign or Canvas. Refer to the following sections for further details on how to best use our tools to build RCS messages.

### Step 5.1: Choose delivery schedule or trigger

RCS messages can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

For action-based delivery, you can also set the campaign’s duration and Quiet Hours.

This step is also where you can specify delivery controls, such as allowing users to become re-eligible to receive the campaign, or enabling frequency capping rules.

### Step 5.2: Choose users to target

Target users by choosing segments or filters to narrow down your audience. You should have already chosen the subscription group, which narrows users by the level or category of communication they want to have with you. 

In this step, you will select the larger audience from your segments, and narrow that segment further with optional [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). You’ll automatically be given a snapshot of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

{% alert tip %}
Interesting in RCS retargeting? To learn more, refer to [RCS retargeting]().
{% endalert %}

### Step 5.3: Choose conversion events

Braze allows you to track how often users perform specific actions, conversion events, after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

Conversion events help you measure the success of your campaign. For example:
- If you're using geotargeting to trigger an RCS message that has an end goal of the user making a purchase, set the conversion event to **Purchase**.
- If you're attempting to drive the user to your app, set the conversion event to **Starts Session**.

You can also set custom conversion events based on your specific use case. Get creative with how you truly want to measure your campaign’s success.

## Step 6: Review and deploy

After you’ve finished building your campaign or Canvas, review its details, test it, then send it!

Next, refer to [SMS and RCS reporting]() to learn how you can access the results of your RCS campaigns.

## Tips

### Using Liquid for message personalization

If you plan to use Liquid, be sure to include a default value for your chosen personalization so, in the event your user profile of the recipient is incomplete, they will not receive a blank placeholder Hi, !, instead of their name or a coherent sentence.

### Generating AI copy

Need help creating awesome copy? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/). Input a product name or description and the AI will generate human-like marketing copy for use in your messaging.

![Message composer with an icon to open the AI copywriting assistant.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %})

### Creating right-to-left messages

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Frequently asked questions

### Can I send pre-recorded voicemails with RCS?

Yes, you can use media messages to support audio files.
