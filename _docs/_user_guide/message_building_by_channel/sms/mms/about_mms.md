---
nav_title: "About MMS"
article_title: About MMS
page_order: 0
description: "This reference article covers what MMS message are and general use cases of the MMS channel."
page_type: reference
channel:
  - MMS
  
---

# About MMS messages

![MMS][picture]{: style="float:right; max-width:30%; margin-left:15px; margin-bottom:15px; border:0"}

> This reference article covers what MMS message are and general use cases of the MMS channel. In addition to this article, you can also check out our [SMS & MMS](https://lab.braze.com/messaging-channels-sms) LAB course.

MMS, also known as Multimedia Message Service, is used to send messages containing multimedia assets (JPG, GIF, PNG) to mobile phones. 

Like SMS, MMS is a high urgency messaging channel that allows you to communicate with customers immediately in a way you can't with any other channel. However, MMS extends the capabilities of SMS by giving you the ability to add media to otherwise text-only SMS.

## Potential use cases

| Use case | Explanation |
| --- | --- |
| Promotions | Reach users with high-visibility SMS campaigns but also leverage the media aspect of MMS to entice buyers with what you're offering. | 
| Re-engagement campaigns | Re-engage customers who opted in to receive SMS when all other channels fail to bring them back. |
{: .reset-td-br-1 .reset-td-br-2}

## Get to know MMS

### MMS availability

Most US and Canadian carriers support receiving and displaying multimedia assets on their customers' phones. For international carriers, Braze will automatically convert MMS messages sent from a supported US or Canada-based phone number, and only to destinations that don't support MMS. For these messages, Braze will replace the attached media with a short URL added to the message body that links to the file.

### Subscription groups

A [Subscription Group][1] is a collection of sending phone numbers (i.e. short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. Your subscription group requires a phone number that is enabled for MMS. A whitelisting provisioning process is required to enable your short-code for MMS sending capabilities. Please speak with your Braze Account Manager regarding enabling this feature.

### MMS message limits and throughput

For MMS, the message limit is 5MB (this includes the multimedia asset and the message body size). To be on the safer side, Braze recommends not exceeding 4MB for your multimedia asset while also including a message body.

MMS throughput is one segment per second via a long code.

### Inbound MMS

Braze does not support incoming MMS responses.

### Accepted file types

Braze accepts JPG, GIF, PNG, and VCF files and allows you to attach a single multimedia asset to your MMS message. Future iterations of MMS at Braze will allow customers to attach up to 10 different assets as well as support a wider range of file types.


[picture]: {% image_buster /assets/img/sms/MMS.jpg %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement