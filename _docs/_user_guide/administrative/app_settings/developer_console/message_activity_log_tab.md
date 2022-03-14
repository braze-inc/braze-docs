---
nav_title: Message Activity Log
article_title: Message Activity Log
page_order: 1
page_type: reference
description: "This reference article describes the Message Activity Log in the Developer Console, which shows you messages associated with your campaigns and sends."

---

# Message Activity Log tab {#dev-console-troubleshooting}

> This reference article describes the Message Activity Log in the Developer Console, which shows you messages associated with your campaigns and sends. In addition to this article, we also recommend checking out our [Quality Assurance and Debugging Tools](https://lab.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) LAB course, which covers how to use the Message Activity Log to conduct your own troubleshooting and debugging.

The **Message Activity Log** in the Developer Console, gives you the opportunity to see any messages (especially error messages) associated with your campaigns and sends. You can see API campaign transactions, troubleshoot details on failed messages, and gather insight on how to improve notification delivery or solve existing technical issues.

![Message Activity Log][2]

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

These messages can come from our own system, your apps or platforms, or our third party partners. This can result in an infinite number of messages that can appear in this log.

## Understanding log messages

To determine what your messages mean, pay attention to the wording of each message and the columns that correspond with it, as it can help you troubleshoot using context clues. 

For example, if you have a log entry whose message states "empty-cart_app" and you aren't sure what that means, look to the left at the **Type** column. If you see "Aborted Message Error", you can safely assume the message was what was written as the [abort message][1] using Liquid, and that the message was aborted because the intended recipient of the message had an empty cart in your app.

### Common messages

There are some common message types you might see, and some might even provide troubleshooting links to help you diagnose and fix issues. Refer to the following table for details.

{% alert note %}
The messages listed below are for example purposes and may not exactly match what is displayed in your log's **Message** column.
{% endalert %}

| Message Type | Sample Message | Description |
|---|---|---|
| Soft Bounce | The email address same@example.com soft bounced. | The email address was valid and the email message reached the recipient's mail server, but was rejected for a "temporary" issue. Common soft bounce reasons include:<br><br>- The mailbox was full (the user is over their quota)<br>- The server was down<br>- The message was too large for the recipient's inbox<br><br>If an email has received a soft bounce, we will usually retry within a 72 hour period, but the number of retry attempts varies from receiver to receiver. |
| Hard Bounce | The email account that you tried to reach does not exist. Please try double-checking the recipient's email address for typos or unnecessary spaces. Learn more at _SAMPLE URL_.| Your message never reached this person's inbox—because there was no inbox to reach! If you want to dig further in, messages like this can sometimes have links in the **View Details** column that will allow you to view the intended recipient's profile.|
| Block | Spam message is rejected because of anti-spam policy. For more information, please visit _SAMPLE URL_.| Uh oh. Looks like your message got categorized as spam here. It might just might be for that intended recipient, but if you're seeing this message a lot, you might want to re-evaluate your send habits or the content of your message. Also, think back—did you [warm up your IP][8]? If not, reach out to Braze for advice on getting this going.|
| Aborted Message Error | empty-cart_web | If you have an app with a cart or you create a send with an abort message in the Liquid, you can customize what message is returned to you if the send is aborted. In this case, the message returned is empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages
[2]: {% image_buster /assets/img_archive/message_activity_log.png %}
[8]: {{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/
