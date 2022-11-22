---
nav_title: "Subscription Groups"
article_title: WhatsApp Subscription Groups
page_order: 2
description: "This article outlines WhatsApp subscription groups, what subscription states are offered, and how subscription groups are set."
page_type: reference
channel:
  - WhatsApp
hidden: true  
---

# WhatsApp subscription groups

WhatsApp subscription groups are created upon integrating WhatsApp with your app through the **Technology Partner Portal**.

{% alert important %}
Support for the WhatsApp channel is currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## WhatsApp subscription states

There are two subscription states for WhatsApp users: `subscribed` and `unsubscribed`. A user's subscription state is not shared across Subscription Groups, meaning a user can be subscribed to a transactional Subscription Group but unsubscribed to a promotional one. For brands, this separation of states ensures they can continue sending relevant WhatsApp messages to their users.

| State | Definition |
| --- | --- |
| Subscribed | User has explicitly confirmed that they want to receive SMS from a specific Subscription Group. Users can be subscribed by having their subscription state updated through the Braze subscription API or by texting an opt-in keyword response. A user must be subscribed to a WhatsApp Subscription Group to receive WhatsApp messaging. |
| Unsubscribed | User has explicitly opted out of messaging from your WhatsApp Subscription group. They can unsubscribe by texting an opt-out keyword response, or a brand can unsubscribe users through the Braze subscription API. Users unsubscribed from a WhatsApp subscription Group will no longer receive messaging. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### How users' WhatsApp subscription groups get set 

- **Rest API:** User profiles can be programmatically set by the [/subscription/status/set][4] endpoint using Braze's REST API.
- **Web SDK:** Users can be added to an email, SMS, or WhatsApp subscription group using the `addToSubscriptionGroup` method for [Android](https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287), or [Web][11].
- **User import**: Users can be added to email or SMS subscription groups via user import. When updating the subscription group status, you must have these two columns in your CSV: `subscription_group_id` and `subscription_state`. Refer to [User import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) for more information.

### How to check a user's WhatsApp subscription group

- **User Profile:** Individual user profiles can be accessed through the Braze dashboard by selecting User Search from the sidebar. Here, you can look up user profiles by email address, phone number, or external user ID. Once in a user profile, under the Engagement tab, you can view a user's SMS subscription groups. 
- **Rest API:** Individual user profiles subscription group can be viewed by the [Get Subscription Group][9] endpoint or [Subscription Group Status][8] endpoint by using Braze's REST API. 

## WhatsApp opt-in process

Currently, users can subscribe and opt-in to WhatsApp messaging in various ways, including [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), through a website, a WhatsApp thread, phone, or in person. Opt-in keywords are not currently supported for the WhatsApp channel, so it will be up to you to maintain a user list. WhatsApp has a retrospective approach to opt-ins and rate limits, where if users start reporting or blocking you, your rate limit will be lowered. 


[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
