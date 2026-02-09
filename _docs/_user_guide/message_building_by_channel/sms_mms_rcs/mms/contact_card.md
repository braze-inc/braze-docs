---
nav_title: Contact cards
article_title: Contact Cards
page_order: 3
description: "This reference article covers how to create a contact card to include in your MMS and SMS messages."
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS
  
---

# Contact cards 

> Contact cards (sometimes known as vCard or Virtual Contact Files (VCF)) are a standardized file format for sending business and contact information that can be easily imported into address books or contact books. Note: Sending a Contact Card will be charged as an MMS so make sure to understand your volumes and consumption rates when creating Contact Cards.

Contact cards can be created [programmatically](https://www.twilio.com/blog/send-vcard-twilio-sms) and uploaded to the Braze [media library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) or created through our built-in contact card generator. These cards can be assigned common properties such as your company's name, phone number, address, email, and a small photo. To start making contact cards, first make sure you're set up to use MMS in Braze.

## Contact card generator

### Step 1: Assign name

Contact cards can be created from the SMS and MMS composer. Select the **Contact Card Generator** tab to get started.

Next, you will be prompted to input your company name or nickname. This is the name that your users will see when they save the card. A 20-character limit is enforced to ensure the user can see your whole company name or alias in their contacts and messaging app. 

![The Contact Card generator tab.]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### Step 2: Assign phone number

Select the subscription group and desired phone number from the available dropdown options. This number will be listed in your contact card and available on their phone to text to after it's saved.

Note that alphanumeric codes are not compatible with two-way messaging and are not supported for contact cards.

### Step 3: Optional fields

![Optional fields for the contact card generator.]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### Upload contact card contact photo

You can upload an optional thumbnail contact photo for your contact card. We recommend a 240 x 240&nbsp;px JPEG or PNG image. Any high-resolution images uploaded will be resized to 240 x 240&nbsp;px to ensure the deliverability of your message, as MMS messages larger than 5&nbsp;MB may fail.

#### Add more information

Other fields allow you to insert your name, subheader, address, and other contact information that your user may want to have available. 

### Step 4: Saving your contact card

Once you've input all the necessary fields, click **Generate Contact Card**, and it will be automatically attached to your campaign or Canvas. From here, you can add a message, test your contact card, and launch your campaign or Canvas.

The contact card will also be saved in the [media library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) to easily reuse in future campaigns and Canvases.

## Adding an existing contact card

To add an existing contact card, create a campaign or Canvas and select your desired subscription group. Next, an **Add Media** option will appear in the message composer window. Here, you can upload an existing contact card file or locate one through the media library.
