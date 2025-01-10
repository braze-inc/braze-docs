---
nav_title: Message Archiving
article_title: Message Archiving
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "This reference article covers message archiving, a feature that allows you to save a copy of messages sent to users."

---

# Message archiving

> Message archiving lets you save a copy of messages sent to users for archival or compliance purposes to your AWS S3 bucket, Azure Blob Storage container or Google Cloud Storage bucket. <br><br> This article covers how to set up message archiving, JSON payloads references, and frequently asked questions.

Message archiving is available as an add-on feature. To get started with message archiving, reach out to your Braze customer success manager.

## How it works

When this feature is turned on, if you have connected a cloud storage bucket to Braze and marked it as the default data export destination, Braze will write a gzipped JSON file to your cloud storage bucket for each message sent to a user through your selected channels (email, SMS, or push). 

This file will contain the fields defined under [File references](#file-references) and reflect the final templated messages sent to the user. Any templated values defined in your campaign (for example, {% raw %}`{{${first_name}}}`{% endraw %}) will show the final value that the user received based on their profile information. This allows you to retain a copy of the message sent to satisfy compliance, audit, or customer support requirements.

If you set up credentials for multiple cloud storage providers, message archiving will only export to the one explicitly marked as the default data export destination. If no explicit default is provided and an AWS S3 bucket is connected, message archiving will upload to that bucket.

{% alert important %}
Turning on this feature will impact the delivery speed of your messages, as the file upload is performed immediately before the message send to maintain accuracy. This introduces additional latency into the Braze sending pipeline, affecting sending speeds.
{% endalert %}

The JSON will be saved in your storage bucket using the following key structure:

`sent_messages/channel/(one of: md5, e164 phone number, email, or push token)/(campaign_id OR canvas_step_id)/DispatchId.json.gz`

An example file may look like this:

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
**Having trouble finding your push tokens in your buckets?**<br>
Braze downcases your push tokens before we hash them. This results in the push token `Test_Push_Token12345` being downcased to `test_push_token12345` in the key path with the hash `32b802170652af2b5624b695f34de089`.
{% endalert %}

## Setting up message archiving

This section guides you through setting up message archiving for your workspace. Before proceeding, confirm that your company has purchased and turned on message archiving.

### Step 1: Connect a cloud storage bucket

If you haven't done so already, connect a cloud storage bucket to Braze. For steps, refer to our partner documentation on [Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/), [Azure Blob Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/) or [Google Cloud Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/).

### Step 2: Select channels for message archiving

The **Message Archiving** settings page controls which channels will save a copy of sent messages to your cloud storage bucket.

To select channels:

1. Go to **Settings** > **Message Archiving**.
2. Select your channels.
3. Select **Save changes**.

![The Message Archiving page has three channels to select: Email, Push, and SMS.][1]

{% alert note %}
If you don't see **Message Archiving** in **Settings**, confirm that your company has purchased and turned on message archiving.
{% endalert %}

## File references

The following are references of the JSON payload delivered to your cloud storage bucket each time a message is sent. Refer to our code example repository for [message archive sample files](https://github.com/braze-inc/braze-examples/tree/main/message-archiving).

{% tabs %}
{% tab Email %}

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
  "extras": Extra hash—for SendGrid users, this will be passed to SendGrid as Unique Arguments,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessageVariationApiId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

The `extras` field referred to in this payload is from the key-value pairs added in the **Email Extras** field when composing an email. For sending data back to Currents, refer to [Message extras]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/).

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS %}

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
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": ios/android/web/kindle,
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from a Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% endtabs %}

## Frequently asked questions

### What templating is not included in the payload?

Modifications done after the message leaves Braze won't be reflected in the file saved to your cloud storage bucket. This includes modifications our mail delivery partners make, like wrapping links for click tracking and inserting tracking pixels.

### What are messages under the "unassociated" value in the campaign path?

When a message is sent outside of a campaign or Canvas, the campaign ID in the file name will be "unassociated". This will happen when you send test messages from the dashboard, when Braze sends SMS auto-responses, or when messages sent through the API do not specify a campaign ID.

### How do I find more information about this send?

You can use either the `external_id` or `dispatch_id` in conjunction with the `user_id` to cross-reference the templated message with our Currents data to find more information like the timestamp it was delivered, whether the user opened or clicked the message, and more.

### How are retries handled?

If your cloud storage bucket is unreachable, Braze will retry up to three times with a [backoff jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). AWS S3 rate limit retries are automatically handled by Braze.

### What happens if my credentials are invalid?

If your cloud storage credentials become invalid at any point, Braze won't be able to save any messages to your cloud storage bucket, and those messages will be lost. We recommend configuring your [notification preferences]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences) for Amazon Web Services, Google Cloud Services, or Azure (Microsoft Cloud Services) so you'll receive alerts for any credentials issues.

### Why does my archive file's `sent_at` timestamp differ slightly from the sent timestamp in Currents?

The rendered copy is uploaded immediately before sending the message to the user. Because of cloud storage upload times, there may be a delay of a few seconds between the `sent_at` timestamp in the rendered copy versus the actual time the send occurs.

[1]: {% image_buster /assets/img/message_archiving_settings.png %}
