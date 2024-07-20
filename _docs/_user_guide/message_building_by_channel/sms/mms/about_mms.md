---
nav_title: "About MMS"
article_title: About MMS
page_order: 0
description: "This reference article covers what MMS messages are and general use cases for the MMS channel."
page_type: reference
channel:
  - MMS
search_rank: 2  
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}About MMS messages

> MMS, also known as Multimedia Message Service, is used to send messages containing multimedia assets (JPEG, GIF, PNG) to mobile phones.<br><br>Like SMS, MMS is a high urgency messaging channel that allows you to communicate with customers immediately in a way you can't with any other channel. However, MMS extends the capabilities of SMS by giving you the ability to add media to otherwise text-only SMS.

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

A [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement) is a collection of sending phone numbers (short codes, long codes, and alphanumeric sender IDs) that are used for a specific type of messaging purpose. Your subscription group requires a phone number that is enabled for MMS. Speak with your Braze account manager regarding enabling this feature.

### MMS message limits and throughput

For MMS, the message limit is 1&nbsp;MB (this includes the multimedia asset and the message body size). To be on the safer side, Braze recommends not exceeding 600&nbsp;KB for your multimedia asset while also including a message body.

MMS throughput is one segment per second via a long code.

### Inbound MMS

When a user sends an inbound message that contains a media item, Braze will expose the URL for the media item in Currents as well as Liquid through the Liquid tag {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}

### Accepted file types

Braze accepts JPEG, GIF, PNG, and VCF files and allows you to attach a single multimedia asset to your MMS message.


[picture]: {% image_buster /assets/img/sms/MMS.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement
