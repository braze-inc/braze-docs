---
nav_title: SMS Double Opt-In
article_title: SMS Double Opt-In
permalink: /sms_double_opt_in/
description: "This reference article covers the SMS double opt-in feature, and explains how to enable the feature, select opt-in keywords and reply messages, and enter users into the SMS double opt-in workflow through subscription updates that occur in REST API, SDK, and preference center updates."
Tool:
  - SMS
hidden: true
---

# SMS double opt-in

> The SMS double opt-in feature allows you to require users to explicitly confirm their opt-in intent before they can receive SMS messages. This helps you tailor your focus to users who are likely to be engaged or are engaged with SMS.

When SMS double opt-in is turned on, users are sent an SMS message that asks for their explicit consent before they can be messageable by your campaigns or Canvases. 

While not an explicit requirement of the Telephone Consumer Protection Act of 1991 (TCPA), Braze recommends that you configure SMS double opt-in to ensure users are aware and consenting to be a part of your SMS program. For more information about SMS Compliance, view [SMS laws, regulations, and abuse prevention]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/).

{% alert important %}
SMS double opt-in is currently in early access. Contact your Braze customer success manager if you're interested in participating in the early access.
{% endalert %}

## SMS double opt-in workflows

Users can provide their explicit consent through outbound or inbound SMS messages.

### Outbound SMS double opt-in

When a user provides their phone number, they are sent an SMS message that asks for their consent.

![Screenshot of inbound SMS message where a user sends "JOIN" and receives the response "Reply Y to confirm you want to JOIN our SMS program. 3msg/week, text STOP at any time to STOP, then texts back "Y".][1]{:style="max-width:40%;"}

### Inbound SMS double opt-in

When a user sends an SMS message that contains an opt-in keyword, they are sent an SMS message that asks for their consent.

![Screenshot of outbound SMS message with the brand texting, "Welcome to BRAND text updates! 1 msg a week for the latest offers. Reply Y to opt-in.", the users replying with "Y", and the brand responding with "Thanks! You're now opted-in to BRAND alerts. Here is a promo code SMS10 for 10% off your first purchase!"][2]{:style="max-width:40%;"}

## Enabling SMS double opt-in

To turn on SMS double opt-in, navigate to the **SMS Global Keywords** table in the applicable Subscription Group, and click **Edit** in the **Opt-In Keyword Category**. Next, select your opt-in method (**Opt-In** or **Double Opt-In**). Selecting **Double Opt-In** will expand the page to show additional [configurable fields](#configurable-fields).

![The Opt-In Method section has two opt-in methods to choose from: Opt-In and Double Opt-In.][3]{:style="max-width:50%;"}

### Configurable fields {#configurable-fields}

| Category   |    Fields    | Description   
| ----------- |----------- |---------------- 
| Opt-In Prompt | Keywords | These are the keywords that a user can text to indicate opt-in intent. `START` is a required keyword. This opt-in prompt will also be sent to the user when their subscription status is updated by sources listed in the [Subscription sources](#subscription-sources) section.
| | Reply Message | This is the initial response that a user will receive after texting an opt-in keyword (e.g., “Reply Y to confirm you want to receive messages from this number. Msg&Data Rates may apply.” )
| Double Opt-In Confirmation | Keywords | These are the keywords a user can reply with to confirm their opt-in intent. At least one keyword is required. These keywords should be specified in the **Opt-In Prompt Reply Message** field.
| | Reply Message | This is the confirmation response that a user will receive after they have explicitly confirmed their opt-in and are now messageable via SMS. The user’s Subscription Group status will be set to `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

![The configurable fields have two sections, Opt-In Prompt and Double Opt-In Confirmation, each with the fields Keywords and Reply Message.][4]

## Subscription Group status

Only after the user completes the SMS double opt-in workflow does their [Subscription Group status]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) update to `Subscribed`. If the user begins the workflow but doesn’t complete it, they remain `Unsubscribed` and cannot be sent SMS messages from that Subscription Group.

Users can also be entered into the SMS double opt-in workflow if they are [subscribed from other sources]({{site.baseurl}}//user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (e.g., REST API, SDK).

## Subscription sources {#subscription-sources}

Users can also enter the SMS double opt-in workflow through subscription updates that occur outside of inbound SMS messages. These sources include updates from the REST API, SDK, and preference center. When a user enters the SMS double opt-in workflow via these sources, they will receive the **Opt-In Prompt Reply Message**.

Each subscription source has a different enrollment behavior, as described in the following table.

Source    | Double Opt-In Enrollment Behavior   
----------- | -----------
SDK | Users are automatically enrolled when subscribed via the Braze SDK.
REST API | By default, users won’t be enrolled when their subscription status is set by `/users/track` or any of the `subscription/status/set` endpoints. Users can be enrolled by passing an optional parameter `send_double_opt_in_response` as `true` (e.g., [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "send_double_opt_in_response: true}]). 
Shopify | Users won’t be enrolled when their subscription status is set by our Shopify integration.
User Import | Users won’t be enrolled when their subscription status is set by User Import.
{: .reset-td-br-1 .reset-td-br-2}

[1]: {% image_buster /assets/img/double_opt_in_inbound.png %}
[2]: {% image_buster /assets/img/double_opt_in_outbound.png %}
[3]: {% image_buster /assets/img/double_opt_in_method.png %}
[4]: {% image_buster /assets/img/double_opt_in_fields.png %}
