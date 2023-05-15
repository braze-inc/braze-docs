---
nav_title: Message Archiving
article_title: Message Archiving
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "This reference article covers Message Archiving, a feature that allows you to save a copy of messages sent to users."

---

# Message Archiving

> The Message Archiving feature lets you save a copy of messages sent to users for archival or compliance purposes to your S3 bucket.

## Prerequisites

1. You have purchased this feature, and your customer success manager has enabled the feature.
2. You have connected an S3 bucket to your workspace via the **Technology Partners** page.

## Overview

When this feature is enabled and you have successfully connected an S3 bucket via your workspace's **Technology Partners** page, Braze will write a gzipped JSON file to your S3 bucket for each email, SMS, or push message sent to a user. Your customer success manager can enable any or all of the channels to be saved.

This file will contain the fields defined under [File references](#file-references) and reflect the final templated messages sent to the user. Any templated values defined in your campaign (e.g., {% raw %}`{{${first_name}}}`{% endraw %}) will show the final value that the user received based on their profile information. This will allow you to retain a copy of the message sent to satisfy compliance, audit, or customer support requirements. 

The file will be saved in your S3 bucket using the following key structure:<br>
`sent_messages/Channel/(md5Ofe164PhoneOrEmailOrPushToken)/(campaign_id OR canvas_step_id)/DispatchId.json.gz`

An example file may look like this:<br>
`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert important %}
Enabling this feature will impact the delivery speed of your messages as the S3 file upload is performed immediately before the message send to ensure accuracy. This introduces additional latency into the Braze sending pipeline, affecting sending speeds.
{% endalert %}

## File references

Below are references of the JSON payload delivered to your S3 bucket each time a message is sent:

### Email
```json
{
  "version" : 1, //numerical version of the json structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": HashOfKVP,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiKey, // may not be available
  "canvas_id": CanvasApiKey, // may not be available
  "canvas_step_id": CanvasStepID, // may not be available
  "canvas_variation_id" : CanvasVariationId, // may not be available
  "message_variation_id": MessageVariationId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
}
```

### SMS
```json
{
  "version" : 1 //numerical version of the json structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiKey, // may not be available
  "canvas_id": CanvasApiKey, // may not be available
  "canvas_step_id": CanvasStepID, // may not be available
  "canvas_variation_id" : CanvasVariationId, // may not be available
  "message_variation_id": MessagVariationId, // may not be available
}
```

### Push
```json
{
  "version" : 1, //numerical version of the json structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": ios/android/web/kindle,
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiKey, // may not be available
  "canvas_id": CanvasApiKey, // may not be available
  "canvas_step_id": CanvasStepID, // may not be available
  "canvas_variation_id" : CanvasVariationId, // may not be available
  "message_variation_id": MessagVariationId, // may not be available
}
```

## Frequently asked questions

### What templating is not included in the payload? 
Modifications done after the message leaves Braze will not be reflected in the file saved to your S3 bucket. This will include modifications our mail delivery partners make, like wrapping links for click tracking and inserting tracking pixels. 

### What are messages under the "unassociated" value in the campaign path? 
When a message is sent outside of a campaign or Canvas, the CampaignId in the file name will be "unassociated". This will happen when you send test messages from the dashboard, when Braze sends SMS auto-responses, or when messages sent through the API do not specify a campaign ID.

### How do I find more information about this send? 
Using the dispatch ID, you can cross-reference the templated message with our Currents data to find more information like the external user ID of who received it, the timestamp it was delivered, whether or not the user opened or clicked the message, and more. 

### How are retries handled? 
Should your S3 bucket be unreachable, Braze will retry up to three times with a [backoff jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). S3 rate limit retries are automatically handled by Braze.

### What happens if my credentials are invalid? 
If your S3 credentials become invalid at any point, Braze will not be able to save any messages to your S3 bucket, and those messages will be lost. We recommend configuring the [AWS credentials errors notification]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences) preference to ensure you receive alerts for any credentials issues.

### Why does my archive file's "sent_at" timestamp differ slightly from the sent timestamp in Currents? 
The S3 rendered copy is saved immediately before sending it to the end user. Because of S3 upload times, there may be a delay of a few seconds between the "sent_at" timestamp in the rendered copy versus the actual time the send occurs.
