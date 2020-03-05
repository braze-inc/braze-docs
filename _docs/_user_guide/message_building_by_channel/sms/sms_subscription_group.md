---
nav_title: "SMS Subscription Groups"
page_order: 1
description: "This is the Google Search description. Characters past 160 get truncated, keep it brief."
page_type: reference
tool:
  - Dashboard
  - Docs
  - Campaigns

platform:
  - iOS
  - Android

channel:
  - SMS
---

# SMS Subscription Groups
SMS Subscription Groups are the foundation for sending SMS through Braze. A Subscription Group is a collection of [sending phone numbers][2] (i.e. short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. For example, if a brand has plans to send both transactional and promotional SMS messaging, two Subscription Groups with separate pools of sending phone numbers will need to be set up within your Braze dashboard.

## SMS Subscription States
There are two subscription states for SMS users: `subscribed` and `unsubscribed`. A user's subscription state is not shared across Subscription Groups, meaning a user can be `subscribed` to a transactional Subscription Group but `unsubscribed` to a promotional one. For brands, this separation of states ensures that they can continue to send relevant SMS messages to their users.

| State | Definition |
| --------- | ---------- |
| Subscribed | User has explicitly confirmed that they want to receive SMS from a specific Subscription Group. A user can be subscribed either by having their subscription state updated through the Braze subscription API or by texting an opt-in keyword response. A user must be subscribed to an SMS Subscription Group in order to receive an SMS|
| Unsubscribed | User has explicitly opt-ed out of messaging from your SMS Subscription group and the sending-phone numbers inside the Subscription Group. They can unsubscribe by texting an opt-out keyword response or a brand can unsubscribed users through the Braze subscription API. Users unsubscribed from an SMS subscription Group will no longer receive any SMS from sending phone numbers that belong to the Subscription Group.|
{: .reset-td-br-1 .reset-td-br-2}

- Use the [Subscription Group REST APIs][4] to programmatically manage users' subscription states.
- For more details on opt-in and opt-key keyword handling, please refer to this [doc][7].

## Sending with a Subscription Group
To launch an SMS campaign through Braze, a Subscription Group must be selected in the dropdown (see below). Once selected, an audience filter will be added to your campaign or canvas automatically, ensuring that only users `subscribed` to the selected Subscription Group are in the target audience. To adhere to international [telecommunication compliance and guidelines][3], Braze will never send SMS to users that have not subscribed to the selected Subscription Group.  

![picture][6]

### Multi-Country Sending
Some brands may wish to send to a group of users that have phone numbers from various different countries. It's recommended and sometimes required to use a sending phone number that is from the same country as the target user's number. During the Subscription Group [setup process][5], sending phone numbers from different countries can be added to the group. Once completed, sending phone numbers with the same country code as the target user's phone number will automatically be used when launching a campaign. You will not have to create separate campaigns for users with phone numbers with different country codes, allowing you to launch one campaign or use one canvas step to target relevant users.

![picture][1]

## Setup Process
During your SMS onboarding process, a Braze onboarding manager will setup Subscription Groups for your dashboard account. They will work with you to determine how many Subscription Groups you need and add the appropriate sending phone numbers to your Subscription Groups. Timelines for setting up a Subscription Group will depend on the type of phone numbers you're adding. For example, short code applications can take anywhere between 8-12 weeks, while long codes can be set up within a day. If you have questions on your Braze dashboard setup, please reach out to your Braze representative or support.  


[1]: {% image_buster /assets/img/multi_country_subgroups.png %}
[2]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/
[3]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/about_sms/
[4]: {{ site.baseurll}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[5]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[6]: {% image_buster /assets/img/sms_subgroup_select.png %}
[7]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/keywords/
