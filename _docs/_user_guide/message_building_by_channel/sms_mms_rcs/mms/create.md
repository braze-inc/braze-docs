---
nav_title: Creating an MMS campaign
article_title: Creating an MMS Campaign
page_order: 2
description: "This reference article covers the steps involved in creating, sending, and previewing an MMS message."
page_type: reference
alias: /create_mms_message/
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# Creating an MMS campaign

> This article contains information specific to MMS composition, which is part of the SMS composer. For more detailed information about the SMS/MMS composer, refer to the [SMS composer]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/).

## MMS sending basics

### Select your subscription group

You must designate a subscription group with MMS enabled phone numbers to target (can be short or long codes).

### Input message body

Input PNG, JPEG, GIF, and VCF image types from the media library or specify a URL. Only one image is supported.

### Understand MMS sending

MMS are billed at a different rate versus text-only SMS, and not all carriers can accept MMS. In these cases, Twilio will automatically convert the MMS to an image link the user can click.

### Use contact cards

Contact cards (sometimes known as vCard or Virtual Contact Files (vcf)) are a standardized file format for sending business and contact information that can be easily imported into address books or contact books. These cards can be created [programmatically](https://www.twilio.com/blog/send-vcard-twilio-sms) and uploaded to the Braze media library or created through our built-in [contact card generator]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/).

## Creating an MMS message

Creating an MMS message requires your subscription group to be configured for MMS sending. This is indicated by seeing the MMS tag when selecting a subscription group. Upon selecting an MMS-enabled subscription group, you will have the ability to upload an image, reference an image URL, or include a contact card.

![The "Compose" tab to write your message.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Image specifications

| **Image Specifications** | **Recommended Properties** |
|--------------------------|----------------------------|
| Size                     | Up to 600&nbsp;KB        |
| File Types               | PNG, JPEG, GIF             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Previewing an MMS message

Braze provides a preview of the image you have uploaded in the **Preview** panel of the message composer. 

{% alert note %}
The ordering of SMS/MMS assets cannot be customized. The ordering is dependent on the phone receiving this message.
{% endalert %}

![An example of a message "Ready to hit the gym...at home?". The preview shows the message and image sent as texts.]({% image_buster /assets/img/sms/mms_preview.png %})
