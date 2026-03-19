---
nav_title: Best practices
article_title: WhatsApp Best Practices
page_order: 9
description: "This article outlines suggested best practices when using the WhatsApp messaging channel, including how to maintain a high phone quality rating and avoid a high rate of blocks and reports."
page_type: reference
channel:
  - WhatsApp
 
---
# WhatsApp best practices

> Before sending your WhatsApp messages, refer to these suggested best practices to maintain a high phone quality rating, avoid blocks and reports, and opt-in and out-out users.

## Maintain a high phone quality rating 

WhatsApp bases its [phone quality rating](https://www.facebook.com/business/help/896873687365001) on actions taken by users who receive your messages, such as blocking or reporting your business. It’s important to maintain a high quality rating because if it’s low and doesn’t improve over a certain time, your messaging limit may decrease.

The first time you message a user in WhatsApp, these options are displayed within the message thread.

![WhatsApp message thread with options to block or report a business]({% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}){: style="max-width:30%;"}

{% alert note %}
For metrics about your blocks and reports, make sure the [Insights tab](https://www.facebook.com/business/help/683499390267496) is turned on in your WhatsApp Manager.
{% endalert %}

To avoid high instances of blocks and reports, Braze suggests the following best practices to maintain a high phone quality rating and stable messaging limits. 

### Follow WhatsApp opt-in requirements and guidelines

Make sure all users have actively consented to receive WhatsApp messages before you start communicating with them on WhatsApp. When asking users to opt-in, users should be told that they are specifically agreeing to receive messages from your business over WhatsApp.

{% alert note %}
For information about opt-in requirements and helpful tips, see [Get Opt-in for WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/).
{% endalert %}

### Follow messaging best practices

- Make your channel name reflect your brand so users recognize that the message is from you, not spam.
- Send a confirmation message to users after you collect their opt-in consent.
- Send messages during appropriate times.

### Give customers the option to opt-out

Opt-outs don’t impact your phone quality rating, so it’s better for a user to opt-out of receiving WhatsApp communications versus blocking or reporting you.

A suggested best practice is to provide instructions about how to out-out in the footer of the first message you send users. For example, you could state that users can unsubscribe from your WhatsApp channel by responding with your opt-out trigger word. You could also regularly include the opt-out footer in future campaigns. To learn how to set this up, see [Opt-in and opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/).
 
![WhatsApp message with a footer stating to respond STOP to unsubscribe from the channel]({% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}){: style="max-width:35%;"}

