---
nav_title: Opt-ins and opt-outs
article_title: WhatsApp Opt-ins and opt-outs
description: " "
page_type: partner
search_tag: Partner
page_order: 5
hidden: true  
---

# WhatsApp opt-ins and opt-outs

## Overview

Businesses must comply with [WhatsApp's requirements when obtaining opt-in](https://business.facebook.com/business/help/718961699259789#). 

For WhatApp opt-ins, Braze needs to know the following information:
- Every user needs an `external_id`, a phone number, and an updated subscription status
	- [Use the SDK](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)
	- [User track endpoint](): update phone number (and create a new user if applicable) and update subscription status.
		- Create and update users
		- if `external_id` exists, then we update, else create a new user
	- Optional: subscription status set endpoint
		- Accepts with external ID or phone number

Note that Braze has recently released an improvement to the users/track endpoint that allows updates to the subscription status updates. However, if you have already created opt-in protocols using the subscription status set endpoint, you may continue to do so there.

## External to Braze opt-in methods

Your app or website (Account registration, Checkout Page, Account settings, credit card terminal)

Wherever you already have marketing consent for email or texting, include an additional section for WhatsApp.

Once a user opts-in, they need an `external_id`, a phone number, and updated subscription status. To do this, depending on how your install of braze is set up, either leverage the 	[/subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) endpoint or use the [SDK](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287).

## Outbound message in customer support WhatsApp channel

In your customer support channel, follow up on a resolved issue with an automatic message asking if they want to opt-in to marketing messaging. The functionality here depends on the feature availability in your customer support tool of choice and where you keep user information.

1. Quick reply action
2. keyword process
3. For either of those ideas, you will probably need to finish the path with the following:
	- Call the users/track endpoint to either update or create a user 
	- Leverage the [/subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) endpoint or use the [SDK](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287) 


## Externally built opt-in list 

If you have used WhatsApp previously, you may have already built a user list with opt-ins per the WhatsApp requirements. In this case, upload a [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) or REST API with the following information into Braze.

## Inbound WhatsApp message 

Have customers send an inbound message to the WhatsApp number.

This can be set up as a Canvas or a campaign, depending on whether you'd like the user to receive a confirmation message on the new channel.

1. Create a webhook campaign
2. Create a campaign with the action-based delivery trigger of an inbound message

![][1]

**Example [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) method**

![][2]
![][3]

Note that you can build a URL or QR code to join a WhatsApp channel from within the [WhatsApp manager](https://business.facebook.com/wa/manage/phone-numbers/) under **Phone Number** > **Message Links**.

![][5]

## Braze-powered opt-in methods 

### SMS message

In Canvas, set up a campaign that asks customers if they want to opt-in to receiving WhatsApp messages. 
- Sample segmentation: in subscribed Marketing group, outside of the US
- Custom keyword trigger
- Update method:
	- [Braze-to-Braze webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) that updates the subscription status via Rest API
	- Update user profile via advanced JSON editor with the following template: 

### In-app or in-browser message

Create an in-app message or in-browser pop-up prompting customers to opt-in to WhatsApp usage.

Use [HTML in-app message](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) with [JavaScript "bridge"]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages/#javascript-bridge) to interface with Braze SDK.
It's included in the directions, but make sure to use the WhatsApp subscription group ID. 


## Set up opt-outs for your Braze WhatsApp channel

WhatsApp monitors the quality of a braze's content on the channel. Keeping a high [phone number quality rating]() is important in preventing your message limits from being reduced. One way to ensure a high-quality rating is to prevent users from blocking or reporting your business. This can be done by providing [high-quality messaging](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (i.e., value to your users), controlling message frequency, and allowing customers to opt-out of receiving future communications. 

### General opt-out keywords

You can set up a campaign or Canvas that allows users who message in particular words to opt-out of future messaging. Campaigns can be beneficial as they allow you to include a follow-up message that confirms the successful opt-out. 

### Create a Canvas with a trigger of "Inbound WhatsApp Message"
 
![][6]

Include words like "Stop" or "No Message". If you choose this method, ensure your customers know these opt-out words. For example, after receiving the initial opt-in, include the following in your response: "To opt-out of these messages, message "Stop" at any time. 

![][7]

### Update the user's profile by either:

1. Using the "Update user profile" Canvas action advanced JSON editor, you can use the following template:

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

2. Creating a [Braze-to-Braze webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks#things-to-know) that updates the user's subscription status to "unsubscribed"
  - A similar example can be seen below:<br>![][8]<br><br>![][9]
  - If you wish, include a follow-up message that lets the user know that they've been unsubscribed to the channel, but before the unsubscribe step occurs (as you will no longer be able to message the user). 

### Marketing opt-out selection

Within the WhatsApp message template creator, you can include the "marketing opt-out" option. Any time you include this, ensure the template is used in a Canvas with a subsequent step for a subscription group change. 

1. Create a message template with the "marketing Opt-Out" quick reply.<br>![][10]<br>![][11]<br>![][12]
2. Create a Canvas that uses this message template.
3. Follow steps 2-4 above but with the trigger text "STOP PROMOTIONS"
4. Update the user's subscription status
  - Create a [Braze-to-Braze webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks#things-to-know) that updates the user's subscription status to "unsubscribed"
  - Use the "Update user profile" Canvas Advanced JSON editor and use the following template:

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