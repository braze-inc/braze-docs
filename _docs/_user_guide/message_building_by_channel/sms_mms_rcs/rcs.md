---
nav_title: "RCS"
article_title: Rich Communication Services (RCS)
alias: /text_only_rcs/
page_type: reference
page_order: 13
description: "This reference article covers how to set up and create text-only RCS messages in Braze."
hidden: true
---

# Rich Communication Services (RCS)

> Rich Communication Services (RCS) is an advanced messaging protocol that enhances the traditional SMS and MMS experience by enabling richer, more interactive communication with customers.

## About RCS messages

Carrier support for RCS messaging is a continually developing space. Braze currently supports sending RCS messages in the following countries:

- United States
- United Kingdom

For more information about carrier coverage, reach out to your Braze customer success manager.

### Subscription groups

Subscription groups are considered a collection of RCS-verified senders or sending phone numbers that are used for a specific type of messaging purpose. For example, if you plan to send both transactional and promotional RCS messages, you must set up two subscription groups with separate RCS-verified senders in your Braze dashboard.

## Terms to know

| Term | Definition |
|----|----|
| Text-only (basic RCS message) | This category includes simple messages that are limited to text, similar to traditional SMS. These messages can be up to 1,600 characters and provide a basic level of communication without any rich media elements. |
| Single-content (single RCS message) | This category encompasses enhanced messages that include rich elements such as images, carousels, and buttons. |
| RCS-verified sender | The sending entity of an RCS message. You can think of this as what the recipient of the RCS message will see on their device to identify where the message is coming from. Broadly speaking, the RCS-verified sender contains a company name, visual branding, and verified badge. Braze takes care of creating RCS-verified senders during the RCS setup process. |
| Subscription group | A collection of RCS-verified senders or sending phone numbers that are used for a specific type of messaging purpose. For example, if you plan to send both transactional and promotional RCS messages, you must set up two subscription groups with separate RCS-verified senders in your Braze dashboard. |
| SMS fallback | If a message is unable to be delivered with RCS (for example, lack of carrier support in the region), Braze will attempt to deliver the message with SMS when a sending phone number exists within the subscription group. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Prerequisites

| Requirement | Description |
|----|----|
| Message Credits | Contact your Braze customer success manager to confirm that you're set up on a Message Credits contract. Message Credits is a flexible contract type that allows you to purchase and allocate message volume across various channels, such as SMS and WhatsApp. |
| RCS-verified sender | The sending entity of an RCS message that the recipient sees on their device to identify where the message is coming from. An RCS-Verified Sender consists of a company name, visual branding, and a verified badge. <br><br>Braze will help you apply and register for an RCS-verified sender in eligible regions. You’ll need to provide your Braze representative with some basic information. |
| List of users with phone numbers | Before you can start sending messages, you must add users to your account. Additionally, you must know the approximate size of your audience. Users and phone numbers can be added to Braze through several different methods. Phone numbers must be formatted as a 10-digit number, as well as a country area code. Learn more about [user phone numbers](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting). |
| Keywords and responses | All base keywords must have responses attributed to it before you can begin messaging. Braze will process opt-in, opt-out, and help keywords automatically. Customization options and additional keyword-response configurations are available. <br><br>Learn more about [keywords and responses](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/keywords/optin_optout). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Setting up RCS

### RCS verified senders

After you have purchased your RCS SKUs, confirmed your region eligibility, and are up and running on our Message Credits system, you’re ready to set up your RCS-verified senders. These are the sending entities that your customers will see on their mobile devices which represent your business, and that RCS presents robustly to enhance trust. As opposed to SMS, which identifies your business by a simple phone number, an RCS-verified sender consists of a company name, visual branding, and a verified badge. 

To set up an RCS-verified sender, contact your Braze representative. We'll guide you through the RCS sender registration process and handle the creation of any subscription groups.

### SMS fallback

For optimal message delivery, it's recommended for each subscription group to have an RCS and an SMS sender because Braze will attempt to fallback to SMS when RCS is unavailable. The SMS sender should be capable of delivering messages to the target country. For example, if your RCS sender is registered to send in the UK, you would include a UK long code in the subscription group.

A few example scenarios of where RCS may be unavailable include:

- The recipient's mobile device does not support RCS due to older hardware or software versions
- An RCS send attempt to a region where the RCS sender is not registered

## Creating an RCS campaign

### Step 1: Choose where to build your message

{% tabs %}
{% tab Campaign %}

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
{% alert note %}
If you're using the [older navigation](https://www.braze.com/docs/navigation), you can find **Campaigns** under **Engagement**.
{% endalert %}

{: start="2"}
2. Select **SMS/MMS**, or, for campaigns targeting multiple channels, select **Multichannel**.
3. Name your campaign something clear and meaningful.
4. Add [teams](https://www.braze.com/docs/user_guide/administrative/manage_your_braze_users/teams/) and [tags](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_app_group/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder](https://www.braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Create your Canvas](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas composer.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed.
4. Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
5. Choose your [advancement behavior](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choose any other messaging channels which you would like to pair with your message.

{% endtab %}
{% endtabs %}

### Step 2: Select your subscription group

Choose a subscription group from the dropdown with **RCS/SMS** in the label or description. This indicates the subscription group is RCS enabled.

### Step 3: Compose your message

In the editor, there are **Text-only RCS** and **RCS** labels to identify your message. **Text-only RCS** refers to a basic RCS message. **RCS** refers to a single-content or single RCS message.

{% alert important %}
As you compose your message, if you exceed 160 characters, the label will be updated to **RCS**, indicating that message pricing has changed. In addition, the 1,600 character limit of the message will display in the denominator.
{% endalert %}

![The editor for text-only RCS message.]({% image_buster /assets/img/text_only_rcs/text_only_rcs_example.png %})

### Step 4: Preview and test your message

Braze always recommends previewing and testing your message before sending. Switch to the **Test** tab to send a test RCS message to content test groups or individual users, or preview the message as a user directly in Braze.

### Step 5: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Next, build the remainder of your campaign. See the following sections for further details on how to best use our tools to build RCS messages.

#### Choose delivery schedule or trigger

RCS messages can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to [Scheduling your campaign](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

For action-based delivery, you can also set the campaign's duration and [Quiet Hours](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

This step is also where you can specify delivery controls, such as allowing users to become [re-eligible](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) to receive the campaign, or enabling [frequency capping](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules.

#### Choose users to target

Text-only RCS supports the [user retargeting methods](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/campaign/retargeting/#retargeting-options) that are supported by SMS today.

#### Choose conversion events

Conversion events help you measure the success of your campaign. Braze allows you to track how often users perform specific actions, [conversion events](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion will be counted if the user takes the specified action.

{% endtab %}

{% tab Canvas %}

Complete the remaining sections of your Canvas component. 

For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.

{% endtab %}
{% endtabs %}

### Step 6: Review and deploy

After you’ve finished building the last of your campaign or Canvas, review its details, test it, then send it!

## Analytics

| Metric | Definition |
| --- | --- |
| Reads | _Reads_ is the count and percentage of RCS message sends that were marked as read by the recipient. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }