---
nav_title: Message activity log
article_title: Message Activity Log
page_order: 5
page_type: reference
description: "This reference article describes the Message Activity Log shows you messages associated with your campaigns and sends. Here, you can also find information on how to understand log messages."

---

# Message Activity Log {#dev-console-troubleshooting}

> The **Message Activity Log** gives you the opportunity to see any messages (especially error messages) associated with your campaigns and sends.

You can see API campaign transactions, troubleshoot details on failed messages, and gather insight on how to improve notification delivery or solve existing technical issues.

To access the log, go to **Settings** > **Message Activity Log**.

![Message Activity Log]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
In addition to this article, we also recommend checking out our [Quality Assurance and Debugging Tools](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze Learning course, which covers how to use the Message Activity Log to conduct your own troubleshooting and debugging.
{% endalert %}

You can filter by the following content logged in the **Message Activity Log**:

- Push notification errors
- Aborted message errors
- Webhook errors
- Mail errors
- API message records
- Connected Content errors
- REST API connected audience errors
- User aliasing errors
- A/B testing errors
- SMS/MMS errors
- WhatsApp errors
- Live Activity errors
- Bad user trigger errors

These messages can come from our own system, your apps or platforms, or our third-party partners. This can result in an infinite number of messages that can appear in this log.

## Understanding log messages

To determine what your messages mean, pay attention to the wording of each message and the columns that correspond with it, as it can help you troubleshoot using context clues. 

For example, if you have a log entry whose message states "empty-cart_app" and you aren't sure what that means, look to the left at the **Type** column. If you see "Aborted Message Error", you can safely assume the message was what was written as the [abort message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) using Liquid, and that the message was aborted because the intended recipient of the message had an empty cart in your app.

### Common messages

There are some common message types you might see, and some might even provide troubleshooting links to help you diagnose and fix issues.

The following messages listed are for example purposes and may not exactly match what is displayed in your log's **Message** column.

| Message Type | Potential Message | Description |
|---|---|---|
| Soft Bounce | The email address same@example.com soft bounced. | The email address was valid and the email message reached the recipient's mail server, but was rejected for a "temporary" issue. <br><br>Common soft bounce reasons include: {::nomarkdown} <ul> <li> The mailbox was full (the user is over their quota) </li> <li> The server was down </li> <li> The message was too large for the recipient’s inbox </li>  </ul> {:/} If an email has received a soft bounce, we will usually retry within a 72 hour period, but the number of retry attempts varies from receiver to receiver. |
| Hard Bounce | The email account that you tried to reach does not exist. Try double-checking the recipient's email address for typos or unnecessary spaces. | Your message never reached this person's inbox because there was no inbox to reach. If you want to dig further in, messages like this can sometimes have links in the **View Details** column that will allow you to view the intended recipient's profile.|
| Block | Spam message is rejected because of anti-spam policy. | Your message got categorized as spam. This mail error is logged for a user if we’ve received an event from the ESP indicating the email was dropped. It might just might be for that intended recipient, but if you're seeing this message a lot, you might want to re-evaluate your send habits or the content of your message. Also, think back—did you [warm up your IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? If not, contact Braze for advice on getting this going.|
| Aborted Message Error | empty-cart_web | If you have an app with a cart or you create a send with an abort message in the Liquid, you can customize what message is returned to you if the send is aborted. In this case, the message returned is empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Why isn't my message listed here?

The messages in the Message Activity Log can come from a variety of sources: Braze, your apps or platforms, or our third-party partners. This means there is an infinite number of messages that could possibly appear in this log—as you can imagine, we can't list them all!

For example, some potential "Block" messages, in addition to the one listed in the preceding table, could be:

- Unfortunately, messages from [_IP_ADDRESS_] weren't sent. Please contact your Internet Service provider since part of their network is on our block list.
- Message rejected due to local policy.
- The message was blocked by the receiver as spam.
- Service unavailable, Client host [_IP_ADDRESS_] blocked using Spamhaus.

## Storage retention period

Errors from the last 60 hours are available in the Message Activity Logs. Logs that are more than 60 hours old are cleaned and no longer accessible.

### Number of error logs stored

The number of saved logs is influenced by several conditions. For example, if a scheduled campaign is sent to thousands of users, we would potentially see a sample of the errors in the Message Activity Log instead of all errors. The following is an overview of conditions affecting how many logs will be saved:
- Up to 20 error logs of the same error type will be saved for the same campaign or Canvas step within one fixed clock hour for the following error types:
    - Connected Content errors
    - Abort Message errors
    - Webhook errors
    - SMS Rejection errors
    - SMS Delivery Failure errors
    - WhatsApp Failure errors
    - A/B Testing errors
- Up to 20 push notification error logs of the same error type will be saved for the same campaign or Canvas step and app combination for the following error types:
    - Invalid Push Credential
    - Invalid Push Token
    - No Push Credential
    - Token Errors
    - Quota Exceeded
    - Retries Timed Out
    - Invalid Payload
    - Unexpected Error
- Up to 100 error logs of the same error type will be saved for the same app within one fixed clock hour for the following error types:
    - Live Activity error (No push credential)
    - Live Activity error (Invalid push credential)
    - Other Live Activity errors
    - APNS Feedback Removed Token errors
- Up to 100 error logs of the same error type will be saved for the same campaign or Canvas step within one fixed clock hour for the following error types:
    - Email Soft Bounce errors
    - Email Hard Bounce errors
    - Email Block errors
- Up to 100 user aliasing error logs will be saved for the same workspace within one fixed clock hour.

