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

#### vCard Contact Cards 

vCards, also known as Virtual Contact Files (.VCF), are a standardized file format for sending business/contact information that can be easily imported into address/contact books. vCards can be created programmatically and assigned properties found [here](https://tools.ietf.org/html/rfc6350#section-6). Some common properties included are name, phone number, birthday, address, and email. For more information on how to create vCards, visit the [Twilio vCard documentation](https://www.twilio.com/blog/send-vcard-twilio-sms).

## Creating an MMS message

Creating an MMS message requires your Subscription Group to be configured for MMS sending. This is indicated by seeing the MMS tag when selecting a Subscription Group. Upon selecting an MMS-enabled Subscription Group, you will have the ability to either upload an image or reference an image URL.

![picture][2]

### Image Specifications

**Image Specifications** | **Recommended Properties**
--- | ---
Size | 5MB maximum
File Types | PNG, JPG, GIF
{: .reset-td-br-1 .reset-td-br-2}

## Contact Card Generator

{% tabs %}
{% tab Step 1 %}

Contact Cards can be created from the SMS and MMS composer. Select the __Contact Card Generator__ tab to get started.

{% endtab %}
{% tab Step 2 %}

Next, you will be prompted to input yout company name or nickname. This is


{% endtab %}
{% tab Step 3 %}


{% endtab %}
{% tab Step 4 %}


{% endtab %}

## Previewing an MMS message

Braze provides a preview of the image you have uploaded. 

{% alert note %}
The ordering of SMS/MMS assets cannot be customized. The ordering is dependent on the phone receiving this message.
{% endalert %}

![picture][3]


[1]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/create/
[2]: {% image_buster /assets/img/sms/mms_composer.png %}
[3]: {% image_buster /assets/img/sms/mms_preview.png %}
