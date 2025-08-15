---
nav_title: Double opt-in
article_title: Double Opt-In
description: "This reference article covers the double opt-in feature, and explains how to enable the feature, select opt-in keywords and reply messages, and enter users into the double opt-in workflow through subscription updates that occur in REST API, SDK, and preference center updates."
page_type: reference
page_order: 2
channel:
  - SMS
  - MMS
  - RCS
---

# Double opt-in

> The double opt-in feature allows you to require users to explicitly confirm their opt-in intent before they can receive SMS, MMS, or RCS messages. This helps you tailor your focus to users who are likely to be engaged or are engaged with the channel, and follow compliance best practices.

When double opt-in is turned on, users are sent a message that asks for their explicit consent before they can be messaged by your campaigns or Canvases. 

While not an explicit requirement of the Telephone Consumer Protection Act of 1991 (TCPA), Braze recommends that you configure double opt-in to confirm users are aware and consenting to be a part of your SMS, MMS, or RCS program. For more information about compliance, view [Laws, regulations, and abuse prevention for SMS, MMS, and RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

## Double opt-in workflows

Double opt-in empowers you to obtain explict consent through inbound and outbound opt-in campaigns.

### Outbound

When a user provides their phone number, they are sent a message that asks for their consent.

![Screenshot of outbound SMS message with the brand texting, "Welcome to BRAND text updates! 1 msg a week for the latest offers. Reply Y to opt-in.", the users replying with "Y", and the brand responding with "Thanks! You're now opted-in to BRAND alerts. Here is a promo code SMS10 for 10% off your first purchase!"]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Inbound

When a user sends a message that contains an opt-in keyword, they are sent a message that asks for their consent.

![Screenshot of inbound SMS message where a user sends "JOIN" and receives the response "Reply Y to confirm you want to JOIN our SMS program. 3msg/week, text STOP at any time to STOP, then texts back "Y".]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Enabling double opt-in

To turn on double opt-in, go to the **Global Keywords** table in the applicable subscription group, and click **Edit** in the **Opt-In Keyword Category**. Next, select your opt-in method (**Opt-In** or **Double Opt-In**). Selecting **Double Opt-In** will expand the page to show additional [configurable fields](#configurable-fields).

![The Opt-In Method section has two opt-in methods to choose from: Opt-In and Double Opt-In.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Configurable fields {#configurable-fields}

| Category   |    Fields    | Description   
| ----------- |----------- |---------------- 
| Opt-In Prompt | Keywords | These are the keywords that a user can text to indicate opt-in intent. `START` is a required keyword. This opt-in prompt will also be sent to the user when their subscription status is updated by sources listed in the [Subscription sources](#subscription-sources) section.
| | Reply Message | This is the initial response that a user will receive after texting an opt-in keyword (for example, “Reply Y to confirm you want to receive messages from this number. Msg&Data Rates may apply.” )
| Double Opt-In Confirmation | Keywords | These are the keywords a user can reply with to confirm their opt-in intent. At least one keyword is required. These keywords should be specified in the **Opt-In Prompt Reply Message** field.
| | Reply Message | This is the confirmation response that a user will receive after they have explicitly confirmed their opt-in and are now messageable. The user’s subscription group status will be set to `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

When a user receives an opt-in prompt, they have 30 days to confirm their opt-in intent. If a user wants to subscribe after the 30-day window, they need to text an opt-in keyword to start the double opt-in workflow again.

![The configurable fields have two sections, Opt-In Prompt and Double Opt-In Confirmation, each with the fields Keywords and Reply Message.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Subscription group status

Only after the user completes the double opt-in workflow does their [subscription group status]({{site.baseurl}}/sms_rcs_subscription_groups/) update to `Subscribed`. If the user begins the workflow but doesn’t complete it, they remain `Unsubscribed` and cannot be sent messages from that subscription group.

Users can also be entered into the double opt-in workflow if they are [subscribed from other sources]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (for example, REST API, SDK).

## Subscription sources {#subscription-sources}

Users can also enter the double opt-in workflow through subscription updates that occur outside of inbound messages. These sources include updates from the REST API, SDK, and preference center. When a user enters the double opt-in workflow through these sources, they will receive the **Opt-In Prompt Reply Message**.

Each subscription source has a different enrollment behavior, as described in the following table.

Source    | Double Opt-In Enrollment Behavior   
----------- | -----------
SDK | Users will automatically enter the double opt-in workflow when subscribed through the Braze SDK.
REST API | Users can be entered into the workflow when the subscription status is set through `/subscription/status/set`, `/v2/subscription/status/set` or `/users/track` and the optional parameter `use_double_opt_in_logic` is passed as `true` (for example, [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). If this parameter is omitted, users will not be entered into the double opt-in workflow.
Shopify | Users will not be entered into the  double opt-in workflow when their subscription status is set by our Shopify integration.
User Import | Users will not be entered into the double opt-in workflow when their subscription status is set by User Import.
[Preference Center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Users will automatically enter into the double opt-in workflow when subscribed through a preference center.
User Update Step | Users can be entered into the  double opt-in workflow when their subscription status is set through the User Update step and the optional parameter `use_double_opt_in_logic` is passed as `true`. If this parameter is omitted, users will not be entered into the double opt-in workflow.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Multi-language support
For inbound messages, double opt-in is supported for all languages defined in the subscription group. This means you can define your auto-responses in different languages and Braze will send the auto-response associated with a specific language when a matching keyword is received.

Users who enter the double opt-in workflow through subscription updates that occur outside of inbound messages (for example, SDK, REST API, Shopify) will only be sent the English keywords.

