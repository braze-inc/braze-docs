---
nav_title: "User Phone Numbers"
article_title: SMS User Phone Numbers
page_order: 1
description: "This reference article covers SMS phone number formatting, how to importing phone numbers, as well as how to add users to SMS subscription groups."
page_type: reference
channel: 
  - SMS
  
---

# User phone numbers

> This article will discuss different topics around your users' or customers' phone numbers. If you're looking for information about your own numbers, go to our article on [sending phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/).

Phone numbers are shown in the user profile as a string of digits. If you import a number that contains any non-digits (such as `,`, `-`, `(`, or others), the non-digits will be removed. For example, importing `+1 (724) 123-4567` will show as `17241234567`.

## Importing phone numbers

You can import phone numbers by uploading a [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) or via [API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) to create a user.

### Formatting

As a best practice, the best way to import a phone number is in the [`E.164`](https://en.wikipedia.org/wiki/e.164) format. Braze will attempt to interpret or convert any U.S. number to the best of our ability. However, to ensure accuracy in the event that you are sending to multiple regions with different country or area codes, we recommend you use the `E.164` format, even for U.S.-based phone numbers.

All U.S. numbers must be valid, 10-digit phone numbers with a valid area code. They can be input without the `+` and country code, as Braze will assume and map all valid, 10-digit phone numbers as U.S. numbers.

All international numbers should start with a `+`, followed by their country code and then the phone number. For example, `+442071838750`. 

![][picture]{: style="max-width:50%;border: 0;"}

You can see the differences between local number formatting as well as universal, `E.164` formatting in the following table:

| Country | Local | Country Code | `E.164` |
|---|---|---|---|
| USA | `4155552671` | 1 | `+14155552671` |
| UK | `2071838750` | 44 | `+442071838750` |
| Brazil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

#### About the `E.164` format

Phone carriers have a specific type of format they expect called `E.164` which is the international telephone numbering plan that ensures that each device has a globally unique number. This is what allows phone calls and text messages to be correctly routed to individual phones in different countries. E.164 numbers are formatted as shown in the following image, and can have a maximum of 15 digits.

### Adding users to SMS subscription groups

For a customer to receive an SMS message, they must have a valid phone number and be opted-in to a subscription group. Subscription groups are tied to the SMS program you are running (make sure you follow the [legal requirements for SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) and have recorded consent for each customer). For more information, refer to [SMS subscription groups][1]. 

### Handling invalid phone numbers

When a phone number is deemed invalid, Braze will mark the user's phone number as invalid and will not attempt to send further communications to that phone number. An invalid phone number is marked in the **Engagement Tab** of a user profile.

![][picture2]{: style="max-width:50%;border: 0;"}

A phone number is considered invalid for the following reasons:
- **Provider Error**: a permanent error was received from the SMS provider. This indicates that the phone number supplied is incorrectly formatted or permanently unable to receive SMS messages.
- **Deactivated**: the phone number has been deactivated due to a mobile subscriber terminating their service and releasing their number from their carrier (and may eventually be recycled and assigned to a new user).

These invalid phone numbers can be managed using [SMS endpoints]({{site.baseurl}}/api/endpoints/sms/). 

{% alert note %}
If multiple user profiles have the same phone number and that phone number is marked invalid, then all existing User Profiles with that number will display as invalid. Newly created user profiles will never initially be marked as invalid.
{% endalert %}

You can also include or exclude any users with invalid phone numbers when [creating a segment][2]. 

### Third-party sourcing and verification

Braze relies on third-party tools to source invalid numbers. Braze is not responsible for any outages or misinformation of these services. Thus, this tool should not be relied upon as your sole method of compliance for verifying invalid numbers.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[picture]: {% image_buster /assets/img/sms/e164.png %}
[picture2]: {% image_buster /assets/img/sms/invalid_banner.png %}
