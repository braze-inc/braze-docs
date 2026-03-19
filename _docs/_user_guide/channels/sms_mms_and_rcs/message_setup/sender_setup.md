---
nav_title: Sender setup
article_title: SMS, MMS, and RCS senders
page_order: 2
description: "This article provides an overview of the codes and senders available for sending SMS, MMS, and RCS messages."
page_type: reference
alias: /sending_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

{% multi_lang_include short_and_long_codes.md %}

## MMS-specific requirements

### MMS sender requirements

> MMS and SMS are both tied to the Braze SMS channel. To access MMS on your account requires the purchase of SMS for those who have not yet purchased access. Existing SMS customers can access MMS after they purchase it.

MMS is currently supported for US short codes (5-6 digit numbers), US and CA long codes (10-digit numbers), and US and Canada customer numbers. MMS is supported for toll-free numbers by certain service providers.

Sending MMS to numbers outside of the US and Canada is possible, but MMS messages will be converted into an SMS message with a link to the media asset.

### MMS short codes

Some users may not implement or use MMS short codes, but they will be available if needed at a later date.

For users who got their short codes before Braze supported MMS, all existing customers with US short codes are eligible to instantly enable MMS. Contact your customer success manager if this situation applies to you and you would like MMS enabled.

{% alert important %}
When enabling MMS for short codes that previously didn't have MMS enabled, the short codes might need to be re-approved in an approval process that could take weeks. It's important to account for this timing when deciding to enable MMS.
{% endalert %}

#### MMS short code best practices

- At Braze, we strongly recommend keeping transaction and promotional messaging separate, each with different short codes. Because MMS is tied to the SMS channel, and the SMS channel is highly regulated, customers may be required to pay a monetary penalty for misusing the channel and get their short code suspended (which is irreversible). Keeping transaction and promotional messaging tied to different short codes safeguards their transactional messaging.
- If customers already have a short code dedicated to promotional messaging, and it is MMS enabled, they do not need a separate short code for MMS.

### MMS long codes

Customers may send MMS with long codes. To do this, you must ensure your long codes are MMS-enabled. This can be done initially during setup, or later on from within your account.

MMS messages cannot be sent with an alphanumeric sender ID.

### MMS message limits and throughput

MMS throughput is one segment per second through a long code.

Carriers impose their own file size limits, which determine the success of MMS sends. These limits can vary by geography and carrier, so Braze recommends not exceeding 600&nbsp;KB for your multimedia asset while also including a message body. We also recommend testing to confirm that your media can be delivered across your users' carriers.

#### Carrier file size limits

| File&nbsp;size | Carrier handling |
| --- | --- |
| 300&nbsp;KB | All carriers should reliably handle MMS messages of this size. |
| 600&nbsp;KB | This is considered the standard maximum file size for MMS across most carriers. |
| 1&nbsp;MB |  Most US and Canadian carriers can handle MMS messages of this size, although this may vary by carrier. Some carriers may allow for larger file sizes than this. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Accepted file types

Braze accepts JPEG, GIF, PNG, and VCF files and allows you to attach a single multimedia asset to your MMS message.
