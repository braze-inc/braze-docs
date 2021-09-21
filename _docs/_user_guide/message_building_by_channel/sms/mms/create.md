---
nav_title: Creating an MMS Campaign
article_title: Creating an MMS Campaign
page_order: 2
description: "This reference article covers the steps involved in creating, sending, and previewing an MMS message."
page_type: reference
tool:
  - Campaigns
channel:
  - MMS
  
---

# MMS Message Sending

> This page only contains information specific to MMS composition, which is part of the SMS composer. For more detailed information about the SMS/MMS composer, check the [SMS Composer][1].

## MMS Sending Basics

Sending MMS with Braze:
- __Select your subscription group__
  - You must designate a subscription group with MMS enabled phone numbers to target (can be short or long codes).<br><br>
- __Input message body__
  - Input PNG, JPG, GIF, and VCF image types from the media library or specify a URL.
  - Only 1 image supported<br><br>
- __Understand MMS Sending__
  - MMS are billed at a different rate vs. text-only SMS.
  - Not all carriers can accept MMS. In these cases, Twilio will automatically convert the MMS to an image link the user can click.

### Contact Cards

Contact Cards (sometimes known as vCard or Virtual Contact Files (vcf)) are a standardized file format for sending business and contact information that can be easily imported into address books or contact books. These cards can be created [programmatically](https://www.twilio.com/blog/send-vcard-twilio-sms) and uploaded to the Braze Media Library or created through our built-in [Contact Card Generator]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/).

## Creating an MMS message

Creating an MMS message requires your Subscription Group to be configured for MMS sending. This is indicated by seeing the MMS tag when selecting a Subscription Group. Upon selecting an MMS-enabled Subscription Group, you will have the ability to upload an image, reference an image URL, or include a Contact Card.

![picture][2]

### Image Specifications

**Image Specifications** | **Recommended Properties**
--- | ---
Size | 5MB maximum
File Types | PNG, JPG, GIF
{: .reset-td-br-1 .reset-td-br-2}

## Previewing an MMS message

Braze provides a preview of the image you have uploaded. 

{% alert note %}
The ordering of SMS/MMS assets cannot be customized. The ordering is dependent on the phone receiving this message.
{% endalert %}

![picture][3]


[1]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/create/
[2]: {% image_buster /assets/img/sms/mms_composer.png %}
[3]: {% image_buster /assets/img/sms/mms_preview.png %}
[4]: {% image_buster /assets/img/sms/contact_card1.png %}
[5]: {% image_buster /assets/img/sms/contact_card2.png %}
