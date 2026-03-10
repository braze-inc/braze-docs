---
nav_title: "Reporting"
article_title: Reporting for SMS, MMS, and RCS
page_order: 12
description: "This reference article covers SMS, MMS, and RCS metrics used at Braze, as well as how to view them in your SMS, MMS, and RCS campaigns."
alias: /sms_mms_rcs_reporting/
page_type: reference
tool:
  - Reports
channel:
  - SMS
  - MMS
  - RCS
  
---

# Reporting for SMS, MMS, and RCS

> This reference article covers SMS, MMS, and RCS metrics used at Braze, as well as how to view them in your SMS, MMS, and RCS campaigns.

{% multi_lang_include analytics/campaign_analytics.md channel="SMS" %}

## Track SMS opt-ins and opt-outs

You can track SMS opt-ins and opt-outs with the following methods:

| Method | Description |
|--------|-------------|
| Segmenter | The segmenter displays the number of users in a specific [Subscription Group]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#subscription-group). It does not deduplicate by phone number—if multiple users share the same phone number, each instance is counted separately. |
| Subscription group timeseries | Provides a daily snapshot of subscriptions for email and phone numbers. The timeseries counts subscriptions, unsubscribes, and resubscribes. For example, if a user subscribes, unsubscribes, and then resubscribes, they are counted as one subscribed user. |
| Currents | Use Currents to export [subscription and engagement events]({{site.baseurl}}/message_events_glossary/) for your own reporting. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
The _Opt-In_ and _Opt-Out_ statistics in the **SMS/MMS/RCS Performance** panel reflect users opting in or out through inbound keywords (for example, texting "START" for opt-in or "STOP" for opt-out). These numbers are typically lower than what is shown in the segmenter, as they count the number of times these keywords were texted, not the total number of users subscribed to SMS.
{% endalert %}

### Track SMS campaign opt-outs

Track SMS opt-outs at the campaign level by using the inbound receive table instead of the subscription group state change table. For example, in [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) or your data warehouse, you can run a query like:

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

This returns users who opted out of SMS communications for the given app group and subscription group, filtered to those associated with campaigns or Canvases.

## Charges applied to SMS sending outcomes

| Outcome | Definition | Charge |
|--------|------------|--------|
| Sent | A campaign or Canvas step has launched or triggered, and an SMS payload has been sent to the SMS provider. | No charge |
| Delivery Failed | The SMS payload couldn't be sent to the SMS provider. This can occur due to overflowing queues, suspended accounts, or media errors (in the case of MMS). | No charge |
| Delivered | The SMS provider received confirmation of message delivery from the upstream carrier (and, where available, from the destination device). | Charge |
| Rejected | The SMS provider received a rejected receipt indicating that the message wasn't delivered. This can happen for several reasons, including carrier content filtering or availability of the destination device. | Charge |
| Sent to Carrier | The SMS provider received the SMS payload from Braze and attempted to send it to the carriers. This statistic includes delivered messages, rejected messages, and sends where delivery or rejection was not confirmed. | Charges may apply based on individual message sending outcomes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


