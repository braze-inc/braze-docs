---
nav_title: Opt-ins and opt-outs
article_title: WhatsApp opt-ins and opt-outs
description: "This reference article covers different WhatsApp opt-in and opt-out methods."
page_type: partner
search_tag: Partner
page_order: 5

---

# Opt-in and opt-out

## Overview

Handling WhatsApp opt-ins and opt-outs is crucial as WhatsApp monitors your [phone number quality rating](https://www.facebook.com/business/help/896873687365001), and low ratings may result in your message limits being reduced. One way to ensure a high-quality rating is to prevent users from blocking or reporting your business. This can be done by providing [high-quality messaging](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (i.e., value to your users), controlling message frequency, and allowing customers to opt-out of receiving future communications. 

Opt-ins can come from external sources or from Braze methods such as SMS or in-app and in-browser messages. Opt-outs can be dealt with using keywords set in Braze and WhatsApp marketing buttons. Reference the following methods for guidance on setting up opt-ins and opt-outs. 

#### Opt-in methods
- [External to Braze opt-in methods](#external-to-braze-opt-in-methods)
  - [Externally built opt-in list](#externally-built-opt-in-list)
  - [Outbound message in customer support WhatsApp channel](#outbound-message-in-customer-support-whatsapp-channel)
  - [Inbound WhatsApp message](#inbound-whatsapp-message)
- [Braze-powered opt-in methods](#braze-powered-opt-in-methods)

#### Opt-out methods
- [General opt-out keywords](#general-opt-out-keywords)
- [Marketing opt-out selection](#marketing-opt-out-selection)
<br><br>
{% alert important %}
Support for the WhatsApp channel is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Set up opt-ins for your Braze WhatsApp channel

For WhatsApp opt-ins, you must comply with [WhatsApp's requirements](https://business.facebook.com/business/help/718961699259789#). You will also need to provide Braze with the following information:
- A `external_id`, a phone number, and an updated subscription status for every user. This can be done by using the [SDK](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287) or through the [`/users/track`](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) endpoint to update the phone number and subscription status. 

{% alert note %}
Note that Braze has recently released an improvement to the `/users/track` endpoint that allows updates to the subscription status updates. However, if you have already created opt-in protocols using the [`/subscription/status/set endpoint`](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/), you may continue to do so there.
{% endalert %}

### External to Braze opt-in methods

Your app or website (account registration, checkout page, account settings, credit card terminal) to Braze.

Wherever you already have marketing consent for email or texting, include an additional section for WhatsApp. Once a user opts-in, they need an `external_id`, a phone number, and updated subscription status. To do this, depending on how your install of Braze is set up, either leverage the [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) endpoint or use the [SDK](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287).

#### Externally built opt-in list

If you have used WhatsApp previously, you may have already built a user list with opt-ins per the WhatsApp requirements. In this case, upload a CSV or use the API with the [following information]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) into Braze.

#### Outbound message in customer support WhatsApp channel

In your customer support channel, follow up on resolved issues with an automatic message asking if they want to opt-in to marketing messaging. The functionality here depends on the feature availability in your customer support tool of choice and where you keep user information.

1. Provide a [message link] from your WhatsApp Business phone number.
2. Provide [quick reply actions]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/quick_replies/) where the customer replies "Yes" to indicate opt-in
3. Set up custom keyword trigger.
4. For either of those ideas, you will probably need to finish the path with the following:
	- Call the [/users/track](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) endpoint to either update or create a user 
	- Leverage the [/subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) endpoint or use the [SDK](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287) 

#### Inbound WhatsApp message 

Have customers send an inbound message to the WhatsApp number.

This can be set up as a Canvas or a campaign, depending on whether you'd like the user to receive a confirmation message on the new channel.

1. Create a webhook campaign<br>**Example [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) method:**<br>![][2]<br><br>![][3]<br><br>
2. Create a campaign with the action-based delivery trigger of an inbound message<br>![][1]

{% alert tip %}
Note that you can build a URL or QR code to join a WhatsApp channel from within the [WhatsApp manager](https://business.facebook.com/wa/manage/phone-numbers/) under **Phone Number** > **Message Links**.<br>![]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Braze-powered opt-in methods 

#### SMS message

In Canvas, set up a campaign that asks customers if they want to opt-in to receiving WhatsApp messages. For example:
- Customer segment: subscribed marketing group outside of the US
- Custom keyword trigger setup
- Update method:
	- [Braze-to-Braze webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) that updates the subscription status via Rest API
	- Update user profile via advanced JSON editor with the following template: 

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

#### In-app or in-browser message

Create an in-app message or in-browser pop-up prompting customers to opt-in to WhatsApp usage.

Use [HTML in-app message](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) with [JavaScript "bridge"]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages/#javascript-bridge) to interface with Braze SDK. Make sure to use the WhatsApp subscription group ID. 

## Set up opt-outs for your Braze WhatsApp channel

### General opt-out keywords

You can set up a campaign or Canvas that allows users who message in particular words to opt-out of future messaging. Canvases can be especially beneficial as they allow you to include a follow-up message that confirms the successful opt-out. 

#### Step 1: Create a Canvas with a trigger of "Inbound WhatsApp Message"
 
![][6]{: style="max-width:85%;"}

When selecting keyword triggers, include words like "Stop" or "No Message". If you choose this method, ensure your customers know your opt-out words. For example, after receiving the initial opt-in, include a follow-up response like "To opt-out of these messages, message "Stop" at any time." 

![][7]

#### Step 2: Update the user's profile

Update the user's profile by using the advanced JSON editor or creating a [Braze-to-Braze webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks#things-to-know). 

1. Using the "Update user profile" Canvas action advanced JSON editor, use the following template:

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

2. Creating a [Braze-to-Braze webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks#things-to-know) that updates the user's subscription status to "unsubscribed". A similar example can be seen below:<br><br>![][8]<br><br>![][9]<br><br>Optionally, you can include a follow-up message that lets the user know that they've been unsubscribed from the channel. Make sure this occurs before the unsubscribe step occurs, as you will no longer be able to message the user. 

### Marketing opt-out selection

Within the WhatsApp message template creator, you can include the "marketing opt-out" option. Any time you include this, ensure the template is used in a Canvas with a subsequent step for a subscription group change. 

1. Create a message template with the "marketing opt-out" quick reply.<br>![][11]<br><br>![][12]<br><br>
2. Create a Canvas that uses this message template.<br><br>
3. Follow the steps in the preceding example but with the trigger text "STOP PROMOTIONS".<br><br>
4. Update the user's subscription status.
  - Create a [Braze-to-Braze webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks#things-to-know) that updates the user's subscription status to "unsubscribed"
  - Use the "update user profile" Canvas advanced JSON editor and use the following template:

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```
Note that Braze has plans to automatically process these marketing opt-outs within the next year but requires a manual process to set it up. 
 
[1]: {% image_buster /assets/img/whatsapp/whatsapp111.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp112.png %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp113.png %} 
[4]: {% image_buster /assets/img/whatsapp/whatsapp114.png %} 
[5]: {% image_buster /assets/img/whatsapp/whatsapp115.png %} 
[6]: {% image_buster /assets/img/whatsapp/whatsapp116.png %} 
[7]: {% image_buster /assets/img/whatsapp/whatsapp117.png %} 
[8]: {% image_buster /assets/img/whatsapp/whatsapp118.png %} 
[9]: {% image_buster /assets/img/whatsapp/whatsapp119.png %} 
[10]: {% image_buster /assets/img/whatsapp/whatsapp120.png %} 
[11]: {% image_buster /assets/img/whatsapp/whatsapp121.png %} 
[12]: {% image_buster /assets/img/whatsapp/whatsapp122.png %} 