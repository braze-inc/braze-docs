---
nav_title: "User phone numbers"
article_title: SMS User Phone Numbers
page_order: 7
description: "This reference article covers SMS phone number formatting, how to importing phone numbers, as well as how to add users to SMS subscription groups."
page_type: reference
alias: /user_phone_numbers/
channel: 
  - SMS
  - MMS
  - RCS
---

# User phone numbers

> This article will discuss different topics around your users' or customers' phone numbers. If you're looking for information about your own numbers, go to our article on [sending phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## Recommended format

We recommend importing phone numbers in [`E.164`](https://en.wikipedia.org/wiki/e.164) format to ensure accuracy in the event that you are sending to multiple regions with different country or area codes&#8212;even for U.S.-based phone numbers.

- **U.S. numbers:** All U.S. numbers must be valid, 10-digit phone numbers with a valid area code. If any 10-digit phone number is missing a `+` and country code, Braze will map it as U.S. numbers.
- **International numbers:** All international numbers should start with a `+`, followed by their country code and then the phone number. For example, `+442071838750`.

![Example of a valid e164 international phone number.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

Here's a few examples showing the differences between local and `E.164` formatting:

| Country | Local | Country Code | `E.164` |
|---|---|---|---|
| USA | `4155552671` | 1 | `+14155552671` |
| UK | `2071838750` | 44 | `+442071838750` |
| Brazil | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

## Importing phone numbers

When importing phone numbers, it's important that you follow the [recommended format](#recommended-format). To import phone numbers, use one of the following methods:

- [Uploading a CSV to Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)
- [Using the `/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
User phone numbers are displayed in Braze as a string of digits. If you import a number that contains any non-digits (such as `,`, `-`, `(`, or others), the non-digits will be removed when rendered in Braze. For example, importing `+1 (724) 123-4567` will show as `17241234567`.
{% endalert %}

## Handling invalid phone numbers

When a phone number is deemed invalid, Braze will mark the user's phone number as invalid and will not attempt to send further communications to that phone number. An invalid phone number is marked in the **Engagement Tab** of a user profile.

![Example error message for invalid phone numbers in Braze.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

A phone number is considered invalid for the following reasons:

- **Provider Error**: a permanent error was received from the SMS and RCS provider. This indicates that the phone number supplied is incorrectly formatted or permanently unable to receive SMS or RCS messages.
- **Deactivated**: the phone number has been deactivated due to a mobile subscriber terminating their service and releasing their number from their carrier (and may eventually be recycled and assigned to a new user).

These invalid phone numbers can be managed using [SMS and RCS endpoints]({{site.baseurl}}/api/endpoints/sms/). 

{% alert note %}
If multiple user profiles have the same phone number and that phone number is marked invalid, then all existing User Profiles with that number will display as invalid. Newly created user profiles will never initially be marked as invalid.
{% endalert %}

You can also include or exclude any users with invalid phone numbers when [creating a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

## Adding users to SMS and RCS subscription groups

For a user to receive an SMS or RCS message, they must have a valid phone number and be opted-in to a subscription group. Subscription groups are tied to the SMS or RCS program you are running (make sure you follow the [legal requirements for SMS, MMS, and RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) and have recorded consent for each customer). For more information, refer to [SMS and RCS subscription groups]({{site.baseurl}}/sms_rcs_subscription_groups/).

## Third-party sourcing and verification

Braze relies on third-party tools to source invalid numbers. Braze is not responsible for any outages or misinformation of these services. Thus, this tool should not be relied upon as your sole method of compliance for verifying invalid numbers.
