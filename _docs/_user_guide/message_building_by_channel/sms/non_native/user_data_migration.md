---
nav_title: "User Data Migration"
article_title: Non-Native SMS User Data Migration
page_order: 4
description: "This reference article runs through all the considerations a non-native SMS user should keep in mind when migrating user data to Braze."
page_type: reference
channel:
  - SMS
  
---

# User data migration

Let’s run through all the considerations you’ll need to keep in mind when you’re migrating your user data to Braze. 

## Format user phone numbers to carrier standards

Phone carriers have a specific type of format they expect called E.164 which is the international telephone numbering plan which ensures that each device has a globally unique number. This is what allows phone calls and text messages to be correctly routed to individual phones in different countries. E.164 numbers are formatted as shown below and can have a maximum of fifteen (15) digits. [Learn more here.][userphone]<br>
![e164][picture]{: style="max-width:50%;border: 0;"}

## Adding aliases to the user profiles

Aliases are necessary to be able to capture any custom events or [custom keyword responses][customkeyword]. You will want to set the “alias label” to “phone” and the “alias name” to the user’s phone number.

## Update historical information on users subscription states

If you have any historical information about your user’s [subscription states][subscriptionstate] for your various messaging channels, please be sure to update this information in Braze. 

## Example migration steps

Before you begin composing SMS campaigns through Braze, you’ll need to update your user data to ensure that all of this works. 

__Here's a quick summary of the user data you'll need to update in Braze:__

1. __Import users' phone numbers in the correct format__ ([E.164][0]) formatting requires a '+' and a country code, e.g. +12408884782. For more information on how to import user phone numbers, check out our [documentation][userphone].
  - Use the [users/track][1] REST API endpoint to assign the `phone` value.<br><br>

2. __Add a user alias__ to identified user profiles with a user's phone number. The required format for this is alias_label: 'phone' and alias_name: '+12408884782'
  - Use the [users/alias/new][2] REST API endpoint to assign an alias to existing user profiles.
  - There are also SDK methods for Aliasing Users [iOS][3] / [Android][4] / [Web][5].<br><br>

3. __Assign your user's SMS [subscription state][subscriptionstate]__ (e.g. subscribed or unsubscribed) if you have this information.
  - Use the [subscription/status/set][6] REST API endpoint to set users as subscribed or unsubscribed from your SMS Subscription Group(s).
  - Note that once the SMS Subscription Groups have been configured in your dashboard, you'll be able to grab the necessary `subscription_group_id` which you'll need for your API request.


[0]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#aliasing-users
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[picture]: {% image_buster /assets/img/sms/e164.jpg %}
[customkeyword]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
