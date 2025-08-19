---
nav_title: Opt-Ins & Opt-Outs
article_title: WhatsApp Opt-Ins and Opt-Outs
description: "This reference article covers different WhatsApp opt-in and opt-out methods."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
alias: /user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/
---

# Opt-in and opt-out

> Handling WhatsApp opt-ins and opt-outs is crucial as WhatsApp monitors your [phone number quality rating](https://www.facebook.com/business/help/896873687365001), and low ratings may result in your message limits being reduced. <br><br>One way to build a high-quality rating is to prevent users from blocking or reporting your business. This can be done by providing [high-quality messaging](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (such as value to your users), controlling message frequency, and allowing customers to opt-out of receiving future communications. <br><br>This page covers how to set up opt-ins and opt-outs, and the differences between the "regex" and "is" modifiers.

Opt-ins can come from external sources or from Braze methods, such as SMS or in-app and in-browser messages. Opt-outs can be dealt with using keywords set in Braze and WhatsApp marketing buttons. Reference the following methods for guidance on setting up opt-ins and opt-outs.

#### Opt-in methods
- [External to Braze opt-in methods](#external-to-braze-opt-in-methods)
  - [Externally built opt-in list](#externally-built-opt-in-list)
  - [Outbound message in customer support WhatsApp channel](#outbound-message-in-customer-support-whatsapp-channel)
  - [Inbound WhatsApp message](#inbound-whatsapp-message)
- [Braze-powered opt-in methods](#braze-powered-opt-in-methods)

#### Opt-out methods
- [General opt-out keywords](#general-opt-out-keywords)
- [Marketing opt-out selection](#marketing-opt-out-selection)

## Set up opt-ins for your Braze WhatsApp channel

For WhatsApp opt-ins, you must comply with [WhatsApp's requirements](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). You will also need to provide Braze with the following information:
- An `external_id`, a [phone number]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/), and an updated subscription status for every user. This can be done by using the [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) or through the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to update the phone number and subscription status.

{% alert note %}
Braze released an improvement to the `/users/track` endpoint that allows updates to the subscription status that you can learn about in [Subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status). However, if you have already created opt-in protocols using the [`/v2/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/), you may continue to do so there.
{% endalert %}

### External to Braze opt-in methods

Your app or website (account registration, checkout page, account settings, credit card terminal) to Braze.

Wherever you already have marketing consent for email or texting, include an additional section for WhatsApp. After a user opts-in, they need an `external_id`, a [phone number]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/), and updated subscription status. To do this, depending on how your install of Braze is set up, either leverage the [`/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) or use the [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Externally built opt-in list

If you have used WhatsApp previously, you may have already built a user list with opt-ins per the WhatsApp requirements. In this case, upload a CSV or use the API with the [following information]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) into Braze.

#### Outbound message in customer support WhatsApp channel

In your customer support channel, follow up on resolved issues with an automatic message asking if they want to opt-in to marketing messaging. The functionality here depends on the feature availability in your customer support tool of choice and where you keep user information.

1. Provide a [message link](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) from your WhatsApp Business phone number.
2. Provide [quick reply actions]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies) where the customer replies "Yes" to indicate opt-in
3. Set up custom keyword trigger.
4. For either of those ideas, you will probably need to finish the path with the following:
	- Call the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to either update or create a user
	- Leverage the [`/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) or use the [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### Inbound WhatsApp message 

Have customers send an inbound message to the WhatsApp number.

This can be set up as a Canvas or a campaign, depending on whether you'd like the user to receive a confirmation message on the new channel.

1. Create a campaign with the action-based delivery trigger of an inbound message.
2. Create a webhook campaign. For an example webhook, see [Subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status).

{% alert tip %}
Note that you can build a URL or QR code to join a WhatsApp channel from within the [WhatsApp manager](https://business.facebook.com/wa/manage/phone-numbers/) under **Phone Number** > **Message Links**.<br>![WhatsApp QR code composer.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Braze-powered opt-in methods 

#### SMS message

In Canvas, set up a campaign that asks customers if they want to opt-in to receiving WhatsApp messages by using one of the following methods:
- Customer segment: subscribed marketing group outside of the US
- Custom keyword trigger setup

Learn about updating the subscription status of user profiles by viewing [Subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

#### In-app or in-browser message

Create an in-app message or in-browser pop-up prompting customers to opt-in to WhatsApp usage.

Use [HTML in-app message](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) with [JavaScript "bridge"]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge) to interface with Braze SDK. Make sure to use the WhatsApp subscription group ID. 

#### Phone number capture form

Use the [phone number capture form]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) template in the drag-and-drop editor for in-app messages to collect user phone numbers and grow your WhatsApp subscription groups.

## Set up opt-outs for your Braze WhatsApp channel

### General opt-out keywords

You can set up a campaign or Canvas that allows users who message in particular words to opt-out of future messaging. Canvases can be especially beneficial as they allow you to include a follow-up message that confirms the successful opt-out. 

#### Step 1: Create a Canvas with a trigger of "Inbound WhatsApp Message"
 
![Action-based Canvas entry step that that enters users who send a WhatsApp inbound message.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

When selecting keyword triggers, include words like "Stop" or "No Message". If you choose this method, ensure your customers know your opt-out words. For example, after receiving the initial opt-in, include a follow-up response like "To opt-out of these messages, message "Stop" at any time." 

![Message step to send a WhatsApp inbound message where the message body is "STOP" or "NO MESSAGE".]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Step 2: Update the user's profile

Update the user's profile by using one of the methods described in [Subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

### Marketing opt-out selection

Within the WhatsApp message template creator, you can include the "marketing opt-out" option. Any time you include this, ensure the template is used in a Canvas with a subsequent step for a subscription group change. 

1. Create a message template with the "marketing opt-out" quick reply.<br>![Message template with a footer option of "Marketing opt-out"]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Section to configure a marketing oopt-out button.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Create a Canvas that uses this message template.<br><br>
3. Follow the steps in the preceding example but with the trigger text "STOP PROMOTIONS".<br><br>
4. Update the user's subscription status by using one of the methods described in [Subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

## Set up opt-in and opt-out workflows

You can configure "START" and "STOP" keyword response workflows for WhatsApp with these two methods:

- [User Update step](#user-update-step)
- [Webhook campaign to trigger a second WhatsApp campaign](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### User Update step

The [User Update step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) can add the user's phone number to the WhatsApp subscription group when the user sends a keyword to the subscription group's phone number.

The User Update step avoids race conditions because the user won't progress to the next step in the Canvas before their phone number is added to the subscription group. It also has fewer steps to set up than the other methods, so Braze generally recommends this method.

1. Create a Canvas with the action-based step **Send a WhatsApp Inbound Message**. Select **Where the message body** and enter "START" for **Is**.

{% alert important %}
For "STOP" messages, invert the message step confirming the opt-out and the User Update step. If you don't, the user will be opted out of the subscription group first, and then will not be eligible to receive the confirmation message.
{% endalert %}

![A WhatsApp message step where the message body is "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. In the Canvas, create a **Set Up User Update** step and for **Action** select **Advanced JSON Editor**. <br><br>![User Update step with an action of "Advanced JSON Editor".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3. Populate the **User Update object** with the following JSON payload, replacing `XXXXXXXXXXX` with your subscription group ID:

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4. Add a subsequent WhatsApp message step. <br><br>![User Update step in a Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Considerations

The update might complete at variable speeds because Braze batches the [User Update step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) requests.

### Webhook campaign to trigger a second WhatsApp campaign

A Webhook campaign can trigger entry into a second campaign after adding the user's phone number to the WhatsApp subscription group when the user sends a keyword to the subscription group's phone number.

{% alert important %}
You do not need to use this method for STOP messages. The confirmation message will be sent before the user is removed from the subscription group, so you can use one of the other two steps.
{% endalert %}

1. Create a campaign or Canvas with an action-based step **Send a WhatsApp Inbound Message**. Select **Where the message body** and enter "START" for **Is**.

![WhatsApp message step where the message body is "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2. In the campaign or Canvas, create a Webhook Message step, and change the **Request Body** to **Raw Text**.

![Message step for a webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3. Enter the customer's [endpoint URL]({{site.baseurl}}/api/basics/) in the **Webhook URL**, followed by the endpoint link `campaigns/trigger/send`. For example, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Webhook URL field under the "Compose Webhook" section.]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4. In the raw text, enter the following JSON payload and replace `XXXXXXXXXXX` with your subscription group ID. You will need to replace the `campaign_id` after creating your second campaign.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5. Create a WhatsApp campaign (your second campaign) and set the trigger to API. Make sure you copy this `campaign_id` into the JSON payload of your first campaign.

#### Considerations

- Attribute updates from within the Canvas API trigger JSON payload is not yet supported, so you can only trigger a WhatsApp campaign for the WhatsApp response message (as in step 2).
- A WhatsApp template must be approved to send it as a response message. This is because a quick response requires the inbound message trigger to be inside the same campaign or Canvas. If you use a [User Update step](#user-update-step), you can send a quick response message without Meta approval.

## Understanding the difference between "regex" and "is" modifiers

In this table, `STOP` is used as an example trigger word to demonstrate how the modifiers work.

| Modifier | Trigger word | Action |
| --- | --- | --- |
| `Is` | `STOP` | Catches any whole word use of "stop" regardless of case. For example, this catches "stop" but not "please stop". |
| `Matches regex` | `STOP` | Catches any use of "STOP" in that exact case. For example, this catches "STOP" and "PLEASE STOP" but not "stop". |
| `Matches regex` | `(?i)STOP(?-i)` | Catches any use of "STOP" in any case. For example, this catches "stop", "please stop", and "never stop sending me messages". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

