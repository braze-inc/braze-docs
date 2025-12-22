---
nav_title: "Creating an RCS message"
article_title: Creating an RCS Message
page_order: 2
alias: /create_rcs_message/
description: "This article covers how to create an RCS message."
page_type: reference
channel:
  - RCS
---

# Creating an RCS message

> RCS campaigns are great for directly reaching and programmatically conversing with your customers. You can use Liquid and other dynamic content to create a personal experience with your users and create an environment that fosters and enhances an unobtrusive user experience with your brand.

## Creating an RCS message

### Step 1: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, targeted messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}
1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **SMS/MMS/RCS**, or, for campaigns targeting multiple channels, select **Multichannel**.
3. Name your campaign something clear and meaningful.
4. Add [teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.

{: start="5"} 
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **SMS and RCS variant testing**: Braze allows you to include both SMS and RCS variants within a single campaign, allowing you to compare the performance of each. You can add SMS and RCS variants during the first step of the message composition.

{: start="6"} 
6. Select an RCS-enabled [subscription group]({{site.baseurl}}/sms_rcs_subscription_groups/). When selecting a subscription group, Braze will automatically add a segmenting filter, ensuring that only users subscribed will receive the campaign. Only long codes and short codes that belong to that subscription group will be used to send SMS to target users.
- **SMS fallback**: Braze strongly recommends that every subscription group that contains an RCS sender also includes at least one SMS code for fallback. This is important for deliverability in cases RCS messages fail to deliver. Some reasons for this may include user device incompatibility and incomplete carrier coverage in a given country or region. By enabling SMS fallback, your message will still deliver to your user and that you never miss that opportunity to connect with them.   

{: start="7"}
7. Choose between SMS and RCS. Before composing RCS messages, choose the channel you send with. We generally recommend using RCS wherever possible as there are significant user engagement benefits over SMS; however, we always provide the option of sending with SMS so that you have maximum flexibility and control. 

![Options to select from an RCS or SMS/MMS message type.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas composer.
2. After you've set up your Canvas, add an **SMS/MMS/RCS** Message step in the Canvas builder. 
3. Name your step something clear and meaningful.
4. Select an RCS-enabled [subscription group]({{site.baseurl}}/sms_rcs_subscription_groups/). When selecting a subscription group, Braze will automatically add a segmenting filter, ensuring that only users subscribed will receive the campaign. Only long codes and short codes that belong to that subscription group will be used to target users.
- **SMS fallback**: Braze strongly recommends that every subscription group that contains an RCS sender also includes at least one SMS code for fallback. This is important for deliverability in cases RCS messages fail to deliver. Some reasons for this may include user device incompatibility and incomplete carrier coverage in a given country or region. By enabling SMS fallback, your message will still deliver to your user and that you never miss that opportunity to connect with them.

{: start="5"}
5. Choose between SMS and RCS. Before composing RCS messages, choose the channel you send with. We generally recommend using RCS wherever possible as there are significant user engagement benefits over SMS; however, we always provide the option of sending with SMS so that you have maximum flexibility and control. 

![Options to select from an RCS or SMS/MMS message type.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Step 2: Select your RCS message type

For your RCS message type, choose between **Text** or **Media**.

![Options to select from a Text or Media message type.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Text %}
As the name implies, RCS text messages focus on text as a medium. If you type up to 160 characters, the RCS message is billed as a text-only (or "basic") message. If you exceed 160 characters or use a rich element, the message is billed as a rich (or "single") RCS message (and the character limit increases to 3072 characters). 

#### Features

- Text message types include all SMS features. Only Advanced Tracking is possible for URL click tracking to give you user-level reporting granularity. 
- In addition, you now have the option to include engaging **Suggested Replies** and **Suggested Actions** buttons that drive high-engagement user actions, such as visiting a landing page or placing an order. 
    - **Suggested Replies** are buttons containing suggested responses for users to click and pre-populate in their text input, removing the friction of having to think of a response by providing a constrained set of choices for them. 
    - **Suggested Actions** are buttons that initiate an action on the user’s device. They typically consist of one of two descriptive words and a visual icon to help the user understand what the button does. Braze currently supports OpenURL Suggested Actions. This functions similarly to a URL, where users who select the button are redirected to a webpage or other URL-identified location. 

![A GIF of three Suggested Actions for an RCS message promoting trending fashion styles: "Fairytale royalty", "Edgy academia", and "Show me your other styles".]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Considerations

- For character limits on text, you may write up to 160 characters for a text-only (basic) RCS message or up to 3072 for a rich (single) RCS message. 
- For button limits, you can add up to five buttons per message. These buttons can be either suggested actions or suggested replies.
- Longer text blocks and too many buttons can frustrate users, so wherever possible, we recommend leaning into simplicity. 
- In some cases, it can be more cost-effective to send longer text-only messages through RCS than with SMS. This is because longer SMS messages are broken down into multiple segments, each of which is billable, whereas RCS messages are instead billed per message. Contact your Braze account manager for more details and guidance. 
{% endtab %}

{% tab Media %}
RCS media messages allow you to use engaging media formats that aren't possible with SMS. These include image, video, and document files. These media options exist to help you engage your audience even more deeply and enable entirely new use cases. At the moment, only image uploading is supported through the [Media Library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). 

#### Features

- Media message types support everything available in text message types, which includes text, suggested replies, and suggested actions.
- Supports image files, including JPEG and PNG file formats. Image files are available through upload from the Media Library. 
- Supports video files, including MP4, MPEG, and MV4 file formats. Video files can be added by URL directly in the message composer. 
- Supports document files in PDF format. Document files can be added through the URL directly in the message composer. 

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

Generally speaking, RCS integrates more naturally with Android devices (this method was largely implemented by Google, and peer-to-peer RCS messaging is broadly adopted among the Android community). Different devices may render the experience at different speeds and qualities.  
{% endtab %}
{% endtabs %}

### Step 3: Compose your RCS message

Write your message using languages and personalization ([Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), and emojis) as needed. Be sure to adhere to our message copy limits to reduce your chances of overage charges.

{% alert important %}
Before proceeding, read our [guidelines for RCS message limits](#step-2-select-your-rcs-message-type). RCS messages are [charged per message]({{site.baseurl}}/sms_rcs_billing_calculators/), so it’s a good idea to understand the nuances of what can be included in each type of RCS message.
{% endalert %}

### Step 4: Preview and test your message

Because RCS rendering is controlled by the user’s operating system, device manufacturer, carrier, and messaging app (for example, Google Messages vs. Apple Messages), message appearance can vary. As a result, the RCS preview shown in Braze may not exactly match what an end user ultimately receives. Differences may include layout, media sizing, buttons, branding elements, or supported features. Braze always recommends previewing and testing your message before sending. Use the **Test** tab to send a test RCS to content test groups or individual users, and preview the message as a user directly within Braze. However, final rendering should always be validated on real devices whenever possible, as Braze cannot guarantee perfect parity across all OS, device, and carrier combinations.


### Step 5: Build the remainder of your campaign or Canvas

Next, build the remainder of your campaign or Canvas. Refer to the following sections for further details on how to best use our tools to build RCS messages.

#### Step 5.1: Choose delivery schedule or trigger

RCS messages can be delivered based on a scheduled time, an action, or an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

For action-based delivery, you can also set the campaign’s duration and Quiet Hours.

Specify your delivery controls, such as allowing users to become re-eligible to receive the campaign or enabling frequency capping rules.

#### Step 5.2: Choose users to target

Target users by choosing segments or filters to narrow down your audience. You should have already selected the subscription group, which narrows users by the level or category of communication they want to have with you.

{% multi_lang_include target_audiences.md %}

Next, you'll select the larger audience from your segments and narrow that segment further with optional [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). You'll automatically be given a preview of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

{% alert tip %}
Interested in using RCS retargeting to target users based on their SMS and RCS interactions? Refer to [Retargeting]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Step 5.3: Choose conversion events

Braze allows you to track how often users perform specific actions, or conversion events, after receiving a campaign. You can allow up to a 30-day window during which a conversion will be counted if the user takes the specified action.

Conversion events help you measure the success of your campaign. For example:
- If you're using geotargeting to trigger an RCS message that has an end goal of the user making a purchase, set the conversion event to **Purchase**.
- If you're attempting to drive the user to your app, set the conversion event to **Starts Session**.

You can also set custom conversion events based on your specific use case. Get creative with how you truly want to measure your campaign’s success.

### Step 6: Review and deploy

After you’ve finished building your campaign or Canvas, review its details, test it, then send it!

Next, refer to [Reporting for SMS, MMS, and RCS]({{site.baseurl}}/sms_mms_rcs_reporting/) to learn how you can access the results of your RCS campaigns.

## Tips

### Using Liquid for message personalization

If you plan to use Liquid, be sure to include a default value for your chosen personalization so, if the recipient's user profile is incomplete, they will not receive a blank placeholder `Hi, !` instead of their name or a coherent sentence.

### Generating AI copy

Need help creating engaging copy? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Input a product name or description, and the AI will generate human-like marketing copy for use in your messaging.

![Message composer with an icon to open the AI copywriting assistant.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Frequently asked questions

### Can I send pre-recorded voicemails with RCS?

Yes, you can use media messages to support audio files.
