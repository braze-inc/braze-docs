---
nav_title: "Subscription Groups"
article_title: WhatsApp Subscription Groups
page_order: 2
description: "Subscription Groups are the foundation for sending SMS & MMS through Braze. A Subscription Group is a collection of sending phone numbers (i.e., short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose."
page_type: reference
channel:
  - WhatsApp
  
---

# WhatsApp subscription groups

WhatsApp subscription groups are created upon integrating WhatsApp with your app through the **Technology Partner Portal**.

## WhatsApp subscription states

There are two subscription states for WhatsApp users: `subscribed` and `unsubscribed`. A user’s subscription state is not shared across Subscription Groups, meaning a user can be subscribed to a transactional Subscription Group but unsubscribed to a promotional one. For brands, this separation of states ensures that they can continue to send relevant WhatsApp messages to their users.

| State | Definition |
| --- | --- |
| Subscribed | User has explicitly confirmed that they want to receive SMS from a specific Subscription Group. A user can be subscribed either by having their subscription state updated through the Braze subscription API or by texting an opt-in keyword response. A user must be subscribed to an WhatsApp Subscription Group in order to receive WhatsApp messaging. |
| Unsubscribed | User has explicitly opt-ed out of messaging from your WhatsApp Subscription group. They can unsubscribe by texting an opt-out keyword response or a brand can unsubscribed users through the Braze subscription API. Users unsubscribed from an WhatsApp subscription Group will no longer receive messaging. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### How users' WhatsApp subscription groups get set 

- **Rest API:** User profiles can be programmatically set by the [/subscription/status/set][4] endpoint by using Braze's REST API.
- **Web SDK:** Users can be added to an email, SMS, or WhatsApp subscription group using the `addToSubscriptionGroup` method for [Android](https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287), or [Web][11].
- **User import**: Users can be added into email or SMS subscription groups via user import. When updating subscription group status, you must have these two columns in your CSV: `subscription_group_id` and `subscription_state`. Refer to [User import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) for more information.

### How to check a user's WhatsApp subscription group

- **User Profile:** Individual user profiles can be accessed through the Braze dashboard by selecting User Search from the sidebar. Here, you can look up user profiles by email address, phone number, or external user ID. Once in a user profile, under the Engagement tab, you can view a user's SMS subscription groups. 
- **Rest API:** Individual user profiles subscription group can be viewed by the [Get Subscription Group][9] endpoint or [Subscription Group Status][8] endpoint by using Braze’s REST API. 

## WhatsApp opt-in process

Currently, users can subscribe and opt-in to WhatsApp messaging in a variety of ways including SMS, through a website, a WhatsApp thread, by phone, or in person. there are no opt-in keywords for the WhatsApp channel, though opt-ins can be generated in a variety of ways and it's up to you to maintain a user list. WhatsApp has a retrospective approach to opt-ins and rate limis, where if users start reporting or blocking you, your rate limit will be lowered. 

### How to upload user lists

User import  (if customer has this audience) 
Download from Meta 
Upload as per Braze instructions 

### User lists

Maintaining your user list (opt in/opt out) 
Subscription status endpoints to manage WhatsApp subscriptions 
Generating opt ins 
HTML phone number capture
Canvas trigger to update user profile subscription state 