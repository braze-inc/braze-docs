---
nav_title: SMS sending
article_title: SMS sending
page_order: 4
alias: /sms_message_sending/
description: "This reference article covers the basics and best practices of SMS sending."
page_type: reference
channel:
  - SMS
  
---

# SMS message sending

> Messaging can be complicated, but it doesn't have to be. The following sections list the fundamentals of SMS message sending at Braze including the importance of subscription groups, the requirements for SMS segments and message bodies, as well as advanced customization options available.

## SMS sending basics

### Select your subscription group

SMS messages must be sent from a [subscription group]({{site.baseurl}}/sms_rcs_subscription_groups/). A subscription group is a collection of sending phone numbers (such as short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. You must designate a subscription group to ensure only subscribed users are targeted. Some clients may find they have multiple subscription groups for different use cases, such as transactional SMS messaging and promotional SMS messaging.<br><br>

### Input message body

An SMS message body accepts up to 1,600 characters, including emojis, Liquid, and Connected Content. A single campaign send can result in many message segment sends. Braze SMS message bodies can be composed of either [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) or [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) encoding standards. In the event that a UCS-2 character (for example, an Emoji) is used, the message body will automatically format for that encoding standard.<br><br> 

### Understand message segments and character limits

SMS message segments are how the SMS industry counts messages. A message segment is a grouping of up to a defined number of characters (160 for GSM-7 encoding; 67 for UCS-2 encoding) that will be sent in a single SMS dispatch. If you dispatch an SMS with 161 characters using GSM-7 encoding, you will see that there are two (2) message segments that were sent. Sending multiple message segments may result in additional charges.<br><br>

### Keyword customization (optional)

Regulations require that there are responses to all Opt-In, Opt-Out, and Help/Info SMS keyword responses. With Braze, you are able to define your own keywords to trigger Opt-In, Opt-Out, and Help responses, manage your own responses that get sent to users, and define keyword sets for different languages. For more, refer to our collection on [Keyword processing]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/keywords/).

{% alert tip %}
Want to learn how to create an SMS campaign? Check out our step-by-step guide on [Creating an SMS, MMS, or RCS message]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/).
{% endalert %}

For sending best practices, including multi-country and high-volume sending guidance, refer to [Best practices for SMS, MMS, and RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices/).

