---
nav_title: "User Phone Numbers"
article_title: SMS User Phone Numbers
page_order: 1
description: "This reference article covers phone number formatting, how to importing phone numbers, as well as how to add users to SMS subscription groups."
page_type: reference
channel: 
  - SMS
  
---

# User phone numbers

> This article will discuss different topics around your users' or customers' phone numbers. If you're looking for information about your own numbers, go to our article on [short and long codes]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/#short--long-codes).

Phone numbers are shown in the user profile in local formats, but will not be in the format you use to import the number (`(724) 123 4567`).

## Importing phone numbers

You can import phone numbers by uploading a [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) or via [API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) to create a user.

### Formatting

As a best practice, the best way to import a phone number is in [`E.164`](https://en.wikipedia.org/wiki/e.164) format. However, braze will attempt to interpret or convert any u.s. number to the best of our ability.

All U.S. numbers must be valid, 10-digit phone numbers with a valid area code. They can be input without the `+` and country code, as Braze will assume and map all valid, 10-digit phone numbers as U.S. numbers.

All international numbers should start with a `+`, followed by their country code and then the phone number. (e.g `+442071838750`)

![][picture]{: style="max-width:50%;border: 0;"}

However, to ensure accuracy in the event that you are sending to multiple regions with different country or area codes, it is recommended to use the `E.164` format, even for U.S.-based phone numbers.

You can see the differences between local number formatting as well as universal, `E.164` formatting in the following table:

| Country | Local | Country Code | `E.164` |
|---|---|---|---|
| USA | `4155552671` | 1 | `+14155552671` |
| UK | `2071838750` | 44 | `+442071838750` |
| Brazil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### Adding users to SMS subscription groups

For a customer to receive an SMS message, they must have a valid phone number and be opted-in to a subscription group. Subscription groups are tied to the SMS program you are running (make sure you follow the [legal laws for SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) and have recorded consent for each customer). For more information, refer to [SMS subscription groups][1]. 

### Handling invalid phone numbers

When a phone number is deemed unreachable or invalid, Braze will mark the user's phone number as invalid and will not attempt to send further communications to that phone number. An invalid phone number is marked in the **Engagement Tab** of a user profile.

A phone number is considered invalid in the following cases:

- The phone number supplied is not a valid phone number.
- The phone number is incorrectly formatted.

These invalid phone numbers can be managed using [SMS endpoints]({{site.baseurl}}/api/endpoints/sms/). 

{% alert note %}
If multiple user profiles have the same phone number and that phone number is marked invalid, then all User Profiles will display as invalid.
{% endalert %}

You can also include or exclude any users with invalid phone numbers when [creating a segment][2]. 

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment
[picture]: {% image_buster /assets/img/sms/e164.png %}

