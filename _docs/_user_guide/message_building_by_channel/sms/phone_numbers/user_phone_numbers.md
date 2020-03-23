---
nav_title: "User Phone Numbers"
page_order: 1
description: "This reference article covers phone number formatting, how to importing phone numbers, as well as how to add users to SMS subscription groups."
page_type: reference
channel: SMS
---

# User Phone Numbers

> This article will discuss different topics around your users' or customers' phone numbers - if you're looking for information about your own numbers, please go to our article on [Short & Long Codes]({{ site.baseurl }}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/#short--long-codes).

Phone numbers are shown in the User Profile in local formats, but will not be in the format you use to import the number (`(724) 123 4567`).

## Importing Phone Numbers

You can import phone numbers by uploading a [CSV]({{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) or via [API]({{ site.baseurl }}/api/endpoints/user_data/#user-track-endpoint) to create a user.

### Formatting

As a best practice, the best way to import a phone number is in [`E.164`](https://en.wikipedia.org/wiki/E.164) format. However, Braze will attempt to interpret or convert any U.S. number to the best of our ability.

All U.S. numbers must be valid, 10-digit phone numbers with a valid area code. They can be inputted without the `+` and country code, as Braze will assume and map all valid, 10-digit phone numbers as U.S. numbers.

All international numbers should start with a `+`, followed by their country code and then the phone number. (e.g `+4402012341234`)

However, to ensure accuracy in the event that you are sending to multiple regions with different country or area codes, it is recommended to use the `E.164` format, even for U.S.-based phone numbers.

You can see the differences between local number formatting as well as universal, `E.164` formatting in the table below:

Country | Local |  `E.164`
---|---|---
USA | `415 123 1234` | `+14151231234`
UK | `020 1234 1234` | `+442012341234`
Lithuania | `8 601 12345` | `+37060112345`

As you can see, the country codes for each listing are:
- USA: `+1`
- UK: `+4`
- Lithuania: `+3`

### Adding Users to SMS Subscription Groups

For a customer to receive an SMS message, they __must have a valid phone number and be opted-in to a Subscription Group__. Subscription Groups are tied to the SMS program you are running ([make sure you follow the legal laws for SMS and have recorded consent for each customer]({{ site.baseurl }}/user_guide/message_building_by_channel/sms/about_sms/#sms-laws-regulations--abuse-prevention)). For more information on SMS Subscription Groups, check out [our documentation][1]. 

[1]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/sms_subscription_group/


