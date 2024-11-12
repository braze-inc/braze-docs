---
article_title: Rate Limiting for Campaigns and Canvases
permalink: /rate_limiting/
page_type: reference
description: "This reference article describes the previous Braze delivery speed rate limiting behavior."
---

# Rate limiting

> This article describes the previous Braze delivery speed rate limiting behavior. The updated rate limiting behavior is described [here]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#rate-limiting).

Braze allows you to control marketing pressure by rate limiting your campaigns and Canvases, regulating the amount of outgoing traffic from your platform. You can implement two different types of rate limiting for your campaigns:

1. **Delivery speed rate limiting** takes into consideration the bandwidth of your servers.
2. **User-centric rate limiting** focuses on providing the best experience for the user. 

For more information, refer to [About rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-rate-limiting).

## About delivery speed rate limiting

If you anticipate large campaigns driving a spike in user activity and overloading your servers, you can specify a per-minute rate limit for sending messages&#8212;this means Braze will send no more than your set rate limit within a minute. 

When targeting users during campaign creation, you can navigate to either **Target Audiences** (for campaigns) or **Send Settings** (for Canvas) to select a message delivery speed rate limit (in various increments from as low as 10 to as high as 500,000 messages per minute). Note that non-rate-limited campaigns may exceed these delivery limits.

For instance, if you're trying to send 75,000 messages with a 10,000-per-minute rate limit, the delivery will be spread out over eight minutes. Your campaign will deliver no more than 10,000 messages for each of the first seven minutes, and 5,000 messages over the last minute. 

### Considerations

Messages sent using a rate limit won’t have the rate limit setting (such as 10,000 per minute) evenly sent out over 60 seconds. Instead, Braze makes sure no more than 10,000 messages are sent per minute (this could mean a higher percentage of the 10,000 messages are sent within the first half minute versus the last half minute). 

Be wary of delaying time-sensitive messages with this form of rate limiting. If the message’s audience contains 30 million users but we set the rate limit to 10,000 per minute, a large portion of your user base won’t receive the message until the following day. 

Be aware that messages will be aborted if they’re delayed 72 hours or more due to a low rate limit. The user who created the campaign will receive alerts in the dashboard and via email if the rate limit is too low.

## Campaigns delivery speed rate limiting

### Single-channel campaigns

When sending a single-channel campaign with a delivery speed rate limit, the rate limit is applied for all messages together. For example, an email campaign with a rate limit of 10,000 messages per minute will send a maximum of 10,000 total messages per minute.


| Maximum emails sent per minute | Maximum total messages sent per minute |
|--------------------------------|----------------------------------------|
| 10,000                         | 10,000                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Multi-channel campaigns

When sending a multi-channel campaign with a speed rate limit, each channel is sent independently of the others. As a consequence of this, the following may occur:

- The total number of messages sent per minute could be more than the rate limit. For example, if your campaign has a rate limit of 10,000 per min and utilizes email and SMS, Braze can send a max of 20,000 total messages each minute (10,000 email and 10,000 webhooks).

| Maximum emails sent per minute | Maximum SMS messages sent per minute | Maximum total messages sent per minute |
|--------------------------------|--------------------------------------|----------------------------------------|
| 10,000                         | 10,000                               | 20,000                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- Users could receive the different channels at different times, and it is not necessarily predictable which channel they will get first. 

For example, if you send a campaign that contains email and SMS, you may have 10,000 users with valid phone numbers, but 50,000 users with valid email addresses. If you set the campaign to send 100 messages per minute (a slow rate limit for the campaign size), a user could receive the SMS in the first batch of sends and the email in the last batch of sends, almost nine hours later.

### Multi-platform push campaigns

For push campaigns delivering on multiple platforms, the rate limit selected will be equally distributed across platforms. A push campaign leveraging Android and iOS with a 10,000 rate-limit per minute will equally distribute the 10,000 messages across the two platforms.

| Maximum Android notifications sent per minute | Maximum iOS push notifications sent per minute | Maximum total push notifications sent per minute |
|--------------------------------|--------------------------------------|----------------------------------------|
| 10,000                         | 10,000                               | 10,000                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas delivery speed rate limiting

When sending a Canvas with a speed rate limit, each channel is sent independently of the others. As a consequence of this, the following may occur:

- The total number of messages sent per minute could be more than the rate limit. 
    - For example, if your Canvas has a rate limit of 10,000 per min and utilizes email and in-app messages, Braze can send up to 20,000 total messages each minute (10,000 email and 10,000 in-app messages).

- Rate limits may impact the order in which users receive messages in a Canvas. 
    - For example, if you send a Canvas that contains emails and push notifications to 50,000 users, it may be that all 50,000 have valid email addresses but only 10,000 users have valid push tokens. In this case, if you set the Canvas to send 1,000 messages per minute and there is a multi-channel Canvas step that contains both email and push, it is possible that a user can advance to the next Canvas step (and be eligible to receive this next step) after receiving only the push notification but not yet the email. 

## Overview of previous and new rate limiting behavior

Your Braze account is currently using the previous delivery speed rate limiting behavior. The information below details the overall difference between previous and new delivery speed rate limiting behavior:

- **Single-channel campaigns and Canvases:** Rate limits will always be applied across all messages together.
- **Multi-channel campaigns and Canvases (including multi-platform push):**


<style>
table td {
    word-break: normal;
}
</style>

<table>
  <tr>
    <th></th>
    <th><b>Campaigns</b></th>
    <th><b>Canvas</b></th>
  </tr>
  <tr>
    <td><b>Previous</b></td>
    <td>Applied for each channel separately, with push platforms* sharing the limit collectively</td>
    <td>Applied for each channel separately, with push platforms* sharing the limit collectively</td>
  </tr>
  <tr>
    <td><b>New</b></td>
    <td>Applied separately per channel and push platform</td>
    <td>Shared collectively</td>
  </tr>
</table>

_*Push platforms include: Android, iOS, Web Push, and Kindle._