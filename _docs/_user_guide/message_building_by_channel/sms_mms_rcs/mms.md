---
nav_title: "MMS"
article_title: About MMS
page_order: 16
description: "This reference article covers what MMS messages are and general use cases for the MMS channel."
page_type: reference
alias: /about_mms/
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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Get to know MMS

### MMS availability

Most US and Canadian carriers support receiving and displaying multimedia assets on their customers' phones. For international carriers, Braze will automatically convert MMS messages sent from a supported US or Canada-based phone number, and only to destinations that don't support MMS. For these messages, Braze will replace the attached media with a short URL added to the message body that links to the file.

### Subscription groups

A [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement) is a collection of sending phone numbers (short codes, long codes, and alphanumeric sender IDs) that are used for a specific type of messaging purpose. Your subscription group requires a phone number that is enabled for MMS. Speak with your Braze account manager regarding enabling this feature.

### MMS message limits and throughput

Carriers impose their own file size limits, which ultimately determine the success of MMS sends. These limits can vary by geography and carrier, so to be on the safer side, Braze recommends not exceeding 600&nbsp;KB for your multimedia asset while also including a message body. We also recommend testing to confirm that your media can be delivered across your users' carriers.

MMS throughput is one segment per second through a long code.

#### Carrier file size limits

| File&nbsp;size | Carrier handling |
| --- | --- |
| 300&nbsp;KB | All carriers should reliably handle MMS messages of this size. |
| 600&nbsp;KB | This is considered the standard maximum file size for MMS across most carriers. |
| 1&nbsp;MB |  Most US and Canadian carriers can handle MMS messages of this size, although this may vary by carrier. Some carriers may allow for larger file sizes than this. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Inbound MMS

When a user sends an inbound message that contains a media item, Braze will expose the URL for the media item in Currents as well as Liquid through the Liquid tag {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}

### Accepted file types

Braze accepts JPEG, GIF, PNG, and VCF files and allows you to attach a single multimedia asset to your MMS message.


