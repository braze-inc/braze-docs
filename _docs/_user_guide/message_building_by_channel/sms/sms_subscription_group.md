---
nav_title: "SMS Subscription Groups"
article_title: SMS Subscription Groups
page_order: 4
description: "This reference article covers SMS subscription groups, subscription states, and the subscription group setup process."
page_type: reference
channel:
  - SMS
  
---

# SMS subscription groups

> Subscription groups are the foundation for sending SMS and MMS through Braze. A subscription group is a collection of [sending phone numbers][2] (such as short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. For example, if a brand has plans to send both transactional and promotional SMS messaging, two subscription groups with separate pools of sending phone numbers will need to be set up within your Braze dashboard.

## SMS subscription states

There are two subscription states for SMS users: `subscribed` and `unsubscribed`. A user's subscription state is not shared across subscription groups, meaning a user can be `subscribed` to a transactional subscription group but `unsubscribed` to a promotional one. For brands, this separation of states ensures that they can continue to send relevant SMS messages to their users.

| State | Definition |
| --------- | ---------- |
| Subscribed | User has explicitly confirmed that they want to receive SMS from a specific subscription group. A user can be subscribed either by having their subscription state updated through the Braze subscription API or by texting an opt-in keyword response. A user must be subscribed to an SMS subscription group in order to receive an SMS. |
| Unsubscribed | User has explicitly opt-ed out of messaging from your SMS subscription group and the sending-phone numbers inside the subscription group. They can unsubscribe by texting an opt-out keyword response or a brand can unsubscribed users through the [Braze subscription API][4]. Users unsubscribed from an SMS subscription Group will no longer receive any SMS from sending phone numbers that belong to the subscription group.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### How users' SMS subscription groups get set 

- **Rest API:** User profiles can be programmatically set by the [`/subscription/status/set` endpoint][4] by using the Braze REST API.
- **SDK Integration** Users can be added to an email or SMS subscription group using the `addToSubscriptionGroup` method for [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)), or [Web][11].
- **Automatically handled upon user opt-in/opt-out:** By users texting a default opt-in or opt-out [keyword][7], Braze automatically sets and updates users' subscription state.
- **User import**: Users can be added into email or SMS subscription groups via **Import Users**. When updating subscription group status, you must have these two columns in your CSV: `subscription_group_id` and `subscription_state`. Refer to [User import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) for more information.

When a phone number is updated on a user profile, the new phone number inherits the subscription group status of the user. If the phone number is updated to a number that already exists in Braze, the subscription status of that existing phone number is inherited.

For example, if User A has a phone number that is subscribed to several subscription groups and that phone number then gets added to User B, User B will be subscribed to the same subscription groups. To prevent a user from inheriting the existing subscriptions, you can reset the subscription groups of the old number via REST API whenever a user changes their number. If multiple users share this phone number, they will all be unsubscribed.

### How to check a user's SMS subscription group

- **User Profile:** Individual user profiles can be accessed through the Braze dashboard by selecting User Search from the sidebar. Here, you can look up user profiles by email address, phone number, or external user ID. When inside a user profile, under the Engagement tab, you can view a user's SMS subscription groups. 
- **Rest API:** Individual user profiles subscription group can be viewed by the [List user’s subscription groups endpoint][9] or [List user’s subscription group status endpoint][8] by using the Braze REST API. 

## Sending with a subscription group

To launch an SMS campaign through Braze, a subscription group must be selected in the dropdown, as shown in the following image. After it's selected, an audience filter will be added to your campaign or Canvas automatically, ensuring that only users `subscribed` to the selected subscription group are in the target audience. To adhere to international [telecommunication compliance and guidelines][3], Braze will never send SMS to users that have not subscribed to the selected subscription group.  

![SMS composer with the subscription group dropdown open and "Messaging Service A for SMS" highlighted by the user.][6]

## Setup process

During your SMS onboarding process, a Braze onboarding manager will set up subscription groups for your dashboard account. They will work with you to determine how many subscription groups you need and add the appropriate sending phone numbers to your subscription groups. Timelines for setting up a subscription group will depend on the type of phone numbers you're adding. For example, short code applications can take anywhere between 8-12 weeks, while long codes can be set up within a day. If you have questions about your Braze dashboard setup, reach out to your Braze representative for support.  

## Subscription group MMS enablement

In order to send an MMS message, at least one number within your subscription group has to be enabled to send MMS. This is indicated by a tag located next to the subscription group. 

![Subscription Group dropdown with "Messaging Service A for SMS" highlighted. The entry is prefixed with the tag "MMS".][10]{: style="max-width:40%"}


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
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
