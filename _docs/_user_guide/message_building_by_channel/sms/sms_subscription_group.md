---
nav_title: "SMS Subscription Groups"
article_title: SMS Subscription Groups
page_order: 2
description: "Subscription Groups are the foundation for sending SMS & MMS through Braze. A Subscription Group is a collection of sending phone numbers (i.e. short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose."
page_type: reference
channel:
  - SMS
  
---

# SMS Subscription Groups

> Subscription Groups are the foundation for sending SMS & MMS through Braze. A Subscription Group is a collection of [sending phone numbers][2] (i.e. short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. For example, if a brand has plans to send both transactional and promotional SMS messaging, two Subscription Groups with separate pools of sending phone numbers will need to be set up within your Braze dashboard.

## SMS subscription states

There are two subscription states for SMS users: `subscribed` and `unsubscribed`. A user's subscription state is not shared across Subscription Groups, meaning a user can be `subscribed` to a transactional Subscription Group but `unsubscribed` to a promotional one. For brands, this separation of states ensures that they can continue to send relevant SMS messages to their users.

| State | Definition |
| --------- | ---------- |
| Subscribed | User has explicitly confirmed that they want to receive SMS from a specific Subscription Group. A user can be subscribed either by having their subscription state updated through the Braze subscription API or by texting an opt-in keyword response. A user must be subscribed to an SMS Subscription Group in order to receive an SMS |
| Unsubscribed | User has explicitly opt-ed out of messaging from your SMS Subscription group and the sending-phone numbers inside the Subscription Group. They can unsubscribe by texting an opt-out keyword response or a brand can unsubscribed users through the [Braze subscription API][4]. Users unsubscribed from an SMS subscription Group will no longer receive any SMS from sending phone numbers that belong to the Subscription Group.|
{: .reset-td-br-1 .reset-td-br-2}

### How users' SMS subscription groups get set 

- __Rest API:__ User profiles can be programmatically set by the [/subscription/status/set][4] endpoint by using Braze's REST API.
- __Web SDK:__ Users can be added to an email or SMS subscription group using the [addToSubscriptionGroup][11] method.
- __Automatically Handled Upon User Opt-In/Opt-Out:__ By users texting a default opt-in or opt-out [keyword][7], Braze automatically sets and updates users' subscription state.

### How to check a user's SMS subscription group

- __User Profile:__ Individual user profiles can be accessed through the Braze dashboard by selecting User Search from the right sidebar. Here, you can look up user profiles by email address, phone number, or external user ID. Once in a user profile, under the Engagement tab, you can view a user's SMS subscription groups. 
- __Rest API:__ Individual user profiles subscription group can be viewed by the [Get Subscription Group][9] endpoint or [Subscription Group Status][8] endpoint by using Braze’s REST API. 

## Sending with a Subscription Group

To launch an SMS campaign through Braze, a Subscription Group must be selected in the dropdown (see below). Once selected, an audience filter will be added to your campaign or Canvas automatically, ensuring that only users `subscribed` to the selected Subscription Group are in the target audience. To adhere to international [telecommunication compliance and guidelines][3], Braze will never send SMS to users that have not subscribed to the selected Subscription Group.  

![picture][6]

## Setup process

During your SMS onboarding process, a Braze onboarding manager will setup Subscription Groups for your dashboard account. They will work with you to determine how many Subscription Groups you need and add the appropriate sending phone numbers to your Subscription Groups. Timelines for setting up a Subscription Group will depend on the type of phone numbers you're adding. For example, short code applications can take anywhere between 8-12 weeks, while long codes can be set up within a day. If you have questions about your Braze dashboard setup, please reach out to your Braze representative for support.  

## Subscription group MMS enablement

In order to send an MMS message, at least one number within your Subscription Group has to be enabled to send MMS. This is indicated by a tag located next to the Subscription Group. 

![picture][10]{: style="max-width:40%"}


[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.user.html#addtosubscriptiongroup

