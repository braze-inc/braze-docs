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

## Creating an MMS message

Creating an MMS message requires your Subscription Group to be configured for MMS sending. This is indicated by seeing the MMS tag when selecting a Subscription Group. Upon selecting an MMS-enabled Subscription Group, you will have the ability to upload an image, reference an image URL, or include a Contact Card.

![picture][2]

## MMS Customization

### Image Specifications

**Image Specifications** | **Recommended Properties**
--- | ---
Size | 5MB maximum
File Types | PNG, JPG, GIF
{: .reset-td-br-1 .reset-td-br-2}

### vCard Contact Cards 

vCards, also known as Virtual Contact Files (.VCF), are a standardized file format for sending business/contact information that can be easily imported into address/contact books. vCards can be created [programmatically(https://www.twilio.com/blog/send-vcard-twilio-sms) and uploaded to the Braze [Media Library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) or created through our built-in Contact Card Generator. Some common properties that can be assigned to these cards are name, image, phone number, address, and email.

#### Contact Card Generator

{% tabs %}
{% tab Step 1: Assign Name %}

__Assign Name__

Contact Cards can be created from the SMS and MMS composer. Select the __Contact Card Generator__ tab to get started.

Next, you will be prompted to input your company name or nickname. This is the name that your users will see when they save the card. A 20 character limit is enforced to ensure the user can see your whole company name/alias in their contacts and messaging app. 

![Contact Card Composer]({% image_buster /assets/img/sms/contact_card1.png %})

{% endtab %}
{% tab Step 2: Assign Phone Number %}

__Assign Phone Number__

Select the subscription group and desired phone number from the available drop-down options. This number will be listed in your Contact Card and available on their phone to text to once saved.

Note that alphanumeric codes are not compatible with two-way messaging and are not supported for Contact Cards.

{% endtab %}
{% tab Step 3: Optional Fields %}
![Contact Card Options]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

__Optional Fields__

__Contact Card Contact Photo__
You can upload an optional thumbnail contact photo for your Contact Card. We recommend a 240x240 jpeg or png image. Any high-resolution images uploaded will be resized to 240x240 to ensure the deliverability of your message, as MMS messages larger than 5MB may fail.

__Other Information__
Other fields allow you to insert your name, subheader, address, and other contact information that your user may want to have handy. 
<br><br><br><br><br><br><br>
{% endtab %}
{% tab Saving your Contact Card %}

__Saving your Contact Card__

Once you've input all the necessary fields, click __Generate Contact Card__, and it will be automatically attached to your campaign or Canvas. From here, you can test your Contact Card or launch your campaign or Canvas.

The Contact card will also be saved in the [Media Library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) to easily reuse in future campaigns and Canvases.

{% endtab %}
{% endtabs %}

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
