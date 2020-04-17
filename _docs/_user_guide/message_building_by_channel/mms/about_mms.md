---
nav_title: "About MMS"
page_order: 0
description: "This reference article covers general use cases of the MMS channel."
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

# What is a MMS Messages?
MMS, also known as Multimedia Message Service, is used to send messages containing multimedia assets(.jpg,gif,png) to mobile phones. 


## Get to know MMS
- __MMS Availability:__ Most US/Canadian carriers support receiving and displaying multimedia assets on their customers' phone.  For international carriers, Braze will automatically convert MMS messages sent from a supported US or Canada-based  phone number, and only to destinations that don't support MMS. For these messages, Braze will replace the attached media with a short URL added to the message body that links to the file.<br><br>
- __Subscription Group:__ A Subscription Group is a collection of sending phone numbers (i.e. short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. Your subscription group requires a phone number that is enabled for MMS.  A whitelisting provisioning process is required to enable your short-code for MMS sending capabilities.  Please speak with your AM regarding enabling this feature.<br><br>
- __MMS Message Limits:__ 
For MMS, the message limit is 5mb (this includes the multimedia asset and the message body size).  To be on the safer side, Braze recommends not exceeding 4mb for your multimedia asset while also including a message body.<br><br>
- __Inbound MMS:__ <br>Braze does not support incoming MMS responses at this time


[picture]: {% image_buster /assets/img/sms/sms_about.jpg %}
[1]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/create/#message-copy-limits

