---
nav_title: "Subscription groups"
article_title: WhatsApp Subscription Groups
page_order: 1
description: "This article outlines WhatsApp subscription groups, what subscription states are offered, and how subscription groups are set."
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp
 
---

# Subscription groups

> WhatsApp subscription groups are created upon integrating WhatsApp with your app through the **Technology Partner Portal**.

## WhatsApp subscription states

There are two subscription states for WhatsApp users: `subscribed` and `unsubscribed`.

| State | Definition |
| --- | --- |
| Subscribed | User has explicitly confirmed that they want to receive WhatsApp messages from a specific company. Users can be subscribed by having their subscription state updated through the Braze subscription API or by deploying an opt-in strategy, as per WhatsApp's guidelines. |
| Unsubscribed | User either hasn’t explicitly given consent for opt-in or their opt-in status has been explicitly removed. <br><br> Users unsubscribed from a WhatsApp subscription group will no longer receive any WhatsApp messages from sending phone numbers that belong to the subscription group. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Setting users' WhatsApp subscription groups

- **Rest API:** User profiles can be programmatically set by the [`/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) using the Braze REST API.
- **Web SDK:** Users can be added to an email, SMS, or WhatsApp subscription group using the `addToSubscriptionGroup` method for [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)), or [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **User import**: Users can be added to email or SMS subscription groups via **Import Users**. When updating the subscription group status, you must have these two columns in your CSV: `subscription_group_id` and `subscription_state`. Refer to [User import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) for more information.

### Checking a user's WhatsApp subscription group

- **User Profile:** Individual user profiles can be accessed through the Braze dashboard from **Audience** > **Search Users**. Here, you can look up user profiles by email address, phone number, or external user ID. When you're inside a user profile, under the **Engagement** tab, you can view a user’s WhatsApp subscription group and their status.

- **Rest API:** Individual user profiles subscription group can be viewed by the [List user’s subscription groups endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) or [List user’s subscription group status endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) by using Braze's REST API. 

## WhatsApp opt-in and opt-out process

Currently, users can subscribe and [opt-in and opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) to WhatsApp messaging in various ways, including [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), through a website, a WhatsApp thread, phone, or in person. Note that opt-ins are required.

Opt-in keywords are not currently supported for the WhatsApp channel, so it will be up to you to maintain a user list. WhatsApp has a retrospective approach to opt-ins and rate limits, where if users start reporting or blocking you, your rate limit will be lowered. 

## Updating a user's subscription status to a WhatsApp Canvas {#update-subscription-status}

Regardless of the opt-in and opt-out methods you use, you can update the subscription status of user profiles with one of the following update methods:

- Create a [Braze-to-Braze webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) that updates the subscription status via REST API, such as in the following example:

![Webhook composer with a message using the POST method.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

To avoid race conditions, any follow-up messaging after the webhook should be contained in a second Canvas that is triggered by outcomes from the first Canvas (such as a user has entered a Canvas variation and is in a WhatsApp subscription group).

- Use the advanced JSON editor to update the user profile with the following template: 

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

![User Update step with an Advanced JSON Editor step.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
Updates to a user's subscription status may take up to 60 seconds.
{% endalert %}

