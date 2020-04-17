---
nav_title: Creating a MMS Campaign
page_order: 2
description: "This reference article covers the steps involved in creating and sending a MMS message."
page_type: reference
tool:
  - Dashboard
  - Docs
  - Campaigns

platform:
  - iOS
  - Android

channel:
  - MMS
---

> This page only contains information specific for MMS composition, which is part of the SMS composer.  For more detailed information about the SMS/MMS composer, check the [SMS Composer][1].

# Creating a MMS message

Creating a MMS message requires your Subscription Group to be configured for MMS sending.  This is indicated by seeing the MMS tag when selecting a Subscription Group.  Upon selecting a MMS enabled Subscription Group, you will have the ability to either upload an image or reference an image URL.

![picture][2]

# Previewing a MMS message

Braze provides a preview of the image you have uploaded.  Please note: The ordering of SMS/MMS assets cannot be customized.  The ordering is dependent on the phone receiving this message.

![picture][3]



[1]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/create/
[2]: {% image_buster /assets/img/sms/mms_composer.png %}
[3]: {% image_buster /assets/img/sms/mms_preview.png %}
