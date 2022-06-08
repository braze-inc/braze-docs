---
nav_title: "MMS Short and Long Codes"
article_title: MMS Short and Long Codes
page_order: 1
description: "This reference article covers the differences between SMS and MMS short codes and long codes."
page_type: reference
channel:
  - MMS
  
---

# MMS short and long codes

MMS and SMS are both tied to the Braze SMS channel. To access MMS on your account requires the purchase of SMS for those who have not yet purchased access. Existing SMS customers can access MMS once they purchase it. 

MMS is currently supported for US and Canada short codes (5-6 digit numbers) and long codes (10-digit numbers), as well as US and Canada customer numbers. Sending numbers to numbers outside of the US/Canada is possible, but MMS messages will be converted into an SMS message with a link to the media asset. To read more, refer to [Short and long codes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/).

## MMS short codes

All new short code applications will include MMS by default. Typically, short codes must be explicitly requested during the short code application, but now are included by default. Some users may not implement or use this functionality but will be available if needed at a later date.

For those users who got their short codes before Braze supported MMS, all existing US and Canada customers with US and Canada short codes are eligible to instantly enable MMS. Reach out to your customer success manager if this situation applies to you and you would like MMS enabled. 

### MMS short code best practices

- At Braze, we strongly recommend keeping transaction and promotional messaging separate, each with different short codes. Because MMS is tied to the SMS channel, and the SMS channel is highly regulated, customers may be required to pay a monetary penalty for misusing the channel and get their short code suspended (which is irreversible). Keep transaction and promotional messaging tied to different short codes safeguards their transactional messaging. 

- If customers already have a short code dedicated to promotional messaging, and it is MMS enabled, they do not need a separate short code for MMS.

## MMS long codes

Customers may send MMS with long codes. To do this, you must ensure your long codes are MMS-enabled. This can be done initially during set up, or later on from within your account. 

Note that our MMS messages cannot be sent with an alphanumeric sender ID. To learn more about alphanumeric IDs, check out [Alphanumeric sender ID]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id).
