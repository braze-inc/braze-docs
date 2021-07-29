---
nav_title: "About MMS"
page_order: 0
description: "This reference article covers what MMS message are and general use cases of the MMS channel."
page_type: reference

channel:
  - MMS
---

# What is an MMS Message?
![MMS][picture]{: style="float:right; max-width:30%; margin-left:15px; margin-bottom:15px; border:0"}
MMS, also known as Multimedia Message Service, is used to send messages containing multimedia assets(jpg, gif, png) to mobile phones. 

## Get to Know MMS
- __MMS Availability:__ Most US/Canadian carriers support receiving and displaying multimedia assets on their customers' phones. For international carriers, Braze will automatically convert MMS messages sent from a supported US or Canada-based phone number, and only to destinations that don't support MMS. For these messages, Braze will replace the attached media with a short URL added to the message body that links to the file.<br><br>
- __Subscription Group:__ A [Subscription Group][1] is a collection of sending phone numbers (i.e. short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. Your subscription group requires a phone number that is enabled for MMS. A whitelisting provisioning process is required to enable your short-code for MMS sending capabilities. Please speak with your Braze Account Manager regarding enabling this feature.<br><br>
- __MMS Message Limits:__ For MMS, the message limit is 5MB (this includes the multimedia asset and the message body size). To be on the safer side, Braze recommends not exceeding 4MB for your multimedia asset while also including a message body.<br><br>
- __MMS Throughput:__ MMS throughput is 1 segment per second via a long code.<br><br>
- __Inbound MMS:__ Braze does not support incoming MMS responses at this time<br><br>
- __Accepted File Types:__ Currently, Braze accepts jpg, gif, png, and .vcf files and allows you to attach a single multimedia asset to your MMS message. Future iterations of MMS at Braze will allow customers to attach up to 10 different assets as well as support a wider range of file types.


[picture]: {% image_buster /assets/img/sms/MMS.jpg %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement