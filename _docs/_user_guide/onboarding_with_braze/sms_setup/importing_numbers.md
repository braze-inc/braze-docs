---
nav_title: Importing Phone Numbers
page_order: 2
---
# Importing Phone Numbers

You can import phone numbers by uploading a [CSV]({{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) or via [API]({{ site.baseurl }}/api/endpoints/user_data/#user-track-endpoint) to create a user. The user's number will then appear in their user profile.

## Formatting

As a best practice, the best way to import a phone number is in [`E.164`](https://en.wikipedia.org/wiki/E.164) format. However, Braze will attempt to interpret or convert any U.S. number to the best of our ability.

All U.S. numbers must be valid, 10-digit phone numbers with a valid area code. They can be inputted without the `+` and country code, as Braze will assume and map all valid, 10-digit phone numbers as U.S. numbers.

All international numbers should start with a `+`, followed by their country code and then the phone number:

| Correct | Incorrect |
|---|---|
| `+4402012341234` | `4402012341234` <br> `+4 402 0123 412 34` <br> `402012341234` <br> `01234 1234` |

However, to ensure accuracy in the event that you are sending to multiple regions with different country or area codes, it is recommended to use the `[E.164](https://en.wikipedia.org/wiki/E.164)` format, even for U.S.-based phone numbers.

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

## Adding Users to SMS Subscription Groups

For a customer to receive an SMS message, they __must have a valid phone number and be opted-in to a Subscription Group__. Subscription Groups are tied to the SMS program you are running ([make sure you follow the legal laws for SMS and have recorded consent for each customer]({{ site.basurl }}/user_guide/message_building_by_channel/sms/compliance/)).
