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

# What are SMS Messages?
![SMS about][picture]{: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

MMS, also known as Multimedia Message Service, is used to send messages containing multimedia assets(.jpg,gif,png) to mobile phones. 

This article discusses some common use cases to draw from and terms to know that will aid your MMS integration and allow you to communicate effectively and strategically with your customers.

## Potential Use Cases

| Use Case | Explanation |
|---|---|
| General Marketing | SMS messages are a direct, flexible and efficient way to communicate upcoming deals, favorable sales, and current or anticipated products to your customers. |
| Reminders | SMS messages can be effective in notifying users who have set an appointment for a service. For example, sending an SMS message reminding a customer the day before a doctor's appointment will help minimize missed appointments, saving both you and your users time and money. |
| Transactional Messages | SMS messages are an efficient way to send out transactional notifications such as order confirmations and shipping information, providing them all the information they need in one convenient place. Note that there exists legal guidelines that must be adhered when sending Transactional Messages. If you are unsure please reach out to your internal legal team.|
{: .reset-td-br-1 .reset-td-br-2}

## Get to know MMS

- __MMS Availability:__ Most US/Canadian carriers support receiving and displaying multimedia assets on their customers' phone.  For international carriers, Braze will automatically convert MMS messages sent from a supported US or Canada-based  phone number, and only to destinations that don't support MMS. For these messages, Braze will replace the attached media with a short URL added to the message body that links to the file.<br><br>

- __Subscription Group:__ A Subscription Group is a collection of sending phone numbers (i.e. short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. Your subscription group requires a phone number that is enabled for MMS.  A whitelisting provisioning process is required to enable your short-code for MMS sending capabilities.  Please speak with your AM regarding enabling this feature.<br><br>

- __Message Segment & Character Limits:__ A message segment refers to how many segments your inital SMS message will be split into. Each message has a character limit that if exceeded, will cause the message to be broken into segments. Based on what encoding standards you use (UTF-2 or GSM-7), there are varying character limits. Please reference our [Message Copy Limits][2] documentation for more information on messaging segmentation and message character limits.<br>
For MMS, the message limit is 5mb (this includes the multimedia asset and the message body size).  To be on the safer side, Braze recommends not exceeding 4mb for your multimedia asset while also including a message body.<br><br>

- __Inbound MMS:__ <br>Braze does not support incoming MMS responses at this time


[picture]: {% image_buster /assets/img/sms/sms_about.jpg %}
[1]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/create/#message-copy-limits

