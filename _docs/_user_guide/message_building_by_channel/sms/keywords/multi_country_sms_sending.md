---
nav_title: "Multi-Country SMS Sending"
page_order: 3
description: "This reference article covers multi-country sending best practices."
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

## Multi-Country SMS Sending

In order to send an SMS message to a phone number in a particular country, it is best practice to use a long code or short code that is from the same country. In fact, __short codes can only send SMS to phone numbers from the same country the short code was created in__. 

To overcome this limitation, Subscription Groups can hold long and short codes from multiple different countries and will automatically use the appropriate short code or long code when targeting a user for SMS. Check out our [SMS Subscription Group][1] docs for more information.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/