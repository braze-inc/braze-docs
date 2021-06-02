---
nav_title: Messenger
alias: /partners/messenger/

description: "This article outlines the partnership between Braze and Facebook Messenger, one of the world’s most popular instant messaging platforms."
page_type: partner
---

# Overview

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) is one of the world’s most popular instant messaging platforms, used by nearly one billion monthly active users. Through this platform, brands can create engaging Chatbots to interact intelligently and automatically with their customers.

Use our Webhook and advanced segmentation, personalization, and triggering features to message your users in Facebook Messenger through the Messenger Platform API. We've included the Facebook Messenger Webhook template in the Braze platform under __Templates & Media__.

The Facebook Messenger platform is intended for “non-promotional messages that facilitate a pre-existing transaction, provide other customer support actions, or deliver content requested by a person.” To read more, see [Facebook’s Platform Guidelines](https://developers.facebook.com/docs/messenger-platform/guidelines) and [Examples of Acceptable Use Cases](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable).

## Prerequisites

Please note that Facebook does not allow usage of the Messenger Platform to send marketing messages. In addition, to send messages to users who are not test users of your Facebook App, your App will need to pass Facebook's [App Review](https://developers.facebook.com/docs/messenger-platform/app-review).

| Requirement| Origin| Access| Description|
| ---| ---| ---|
| Facebook Messenger Page| Facebook| https://www.facebook.com/pages/create | A Facebook Page will be used as the identity of your bot. When people chat with your app, they will see the Page name and the Page profile picture.|
| Facebook Messenger App| Facebook| https://developers.facebook.com/apps | The Facebook App contains the settings for your Messenger bot, including access tokens.
| App Bot Review and Approval | Facebook | https://developers.facebook.com/docs/messenger-platform/app-review | When you are ready to release your bot to the public, you must submit it to Facebook for review and approval. This review process allows us to ensure your Messenger bot abides by our policies and functions as expected before it is made available to everyone on Messenger. |
| Page-Scope IDs (PSIDs) | Facebook | https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages | You need to have users PSIDs in order to send messages on Facebook Messenger. Once a user interacts with your app via Messenger, Facebook will create a PSID. This PSID can be sent to Braze as a string custom attribute.
| Page Access Token | Facebook | https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token | These access tokens are similar to user access tokens, except that they provide permission to APIs that read, write or modify the data belonging to a Facebook Page. To obtain a page access token you need to start by obtaining a user access token and asking for the `manage_pagespermission`. Once you have the user access token you then get the page access token via the Graph API.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

You need the user's explicit permission for messages from your page.

## Integration

Read this quick guide to set up your Facebook Messenger Webhook. Braze also offers a full tutorial for creating a Messenger bot with example code in a [GitHub repository](https://github.com/Appboy/appboy-fb-messenger-bot)!

### Step 1: Collect Your PSIDs

In order to send messages on Facebook Messenger, you need to collect your users' page-specific IDs (PSIDs) in order to identify your user and interact with them consistently.

__What is a PSID?__
PSIDs are not the same as the user's Facebook ID. Facebook creates this identifier any time you message a customer or when a customer messages you.

__Where do you find it?__
Use one of the various [entry points](https://developers.facebook.com/docs/messenger-platform/discovery) Facebook offers. Once the user messages your app or takes an action in a conversation, such as tapping a button or sending a message, their PSID will be included in the `sender.id` property of the webhook event, so your bot can identify who took the action (shown below).

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

Whenever you send a message, their PSID will be included in the `recipient.id` property of the request to identify who should receive the message.

__What do I do with it?__

Once you are confident that you are receiving PSIDs, send it to Braze as a Custom Attribute.

### Step 2: Send to Braze as a Custom Attribute

Coordinate and share this with your developer to send the PSIDs to Braze as a [Custom Attribute]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes). PSIDs are strings that can be accessed by making an [API call](https://developers.facebook.com/docs/messenger-platform/reference/send-api).

## Usage

From __Templates & Media__, go to Webhook Templates and choose the Facebook Messenger Webhook Template.

1. Enter your Template Name, add teams, and add tags.
2. Enter your message or choose a message template from [those made available by Facebook](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages). You can also choose your message [type](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) or [tag](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags).
3. Include the PSID as a Custom Attribute (Hint: Use the blue and white + button in the corner of the __Request Body__ box.)
3. Put your Page Access Token in the Webhook URL (Hint: Replace the text `FACEBOOK_PAGE_ACCESS_TOKEN` in the URL with your Token.)

#### Previewing and Testing Your Webhook

Before you send your message, test your webhook. Make sure your Messenger ID is saved in Braze (or find it and test as a Customized User), and use the preview to send the test message:

![Sending a message to yourself][60]

If you receive the message successfully, you can start to configure its delivery settings.

#### Targeting Facebook Messenger Users

If you are not sending messages using users' phone numbers and plan on sending Messenger messages repeatedly, you should [create a segment][62] for all users for whom the Messenger ID exists as a custom attribute and turn on [Analytics Tracking][61] to track your Messenger subscription rates over time. If you choose not to create a specific segment for Messenger subscribers, make sure to include a filter for Messenger ID existing to avoid errors:

![Segment filter for Messenger IDs][63]

You may also use other segmentation to target your Messenger campaigns, and the rest of the campaign creation process is as with any other campaign.


[60]: {% image_buster /assets/img_archive/fbm-test.png %}
[61]: {{site.baseurl}}/user_guide/data_and_analytics/viewing_and_understanding_segment_data/#turning-analytics-tracking-on-and-off
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/fbm-segmentation.png %}
