---
nav_title: Send SMS messages
article_title: SMS Message Sending Overview
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

Regulations require that there are responses to all Opt-In, Opt-Out, and Help/Info SMS keyword responses. With Braze, you are able to define your own keywords to trigger Opt-In, Opt-Out, and Help responses, manage your own responses that get sent to users, and define keyword sets for different languages. For more, refer to our collection on [Keyword processing]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/).

{% alert tip %}
Want to learn how to create an SMS campaign? Check out our step-by-step guide on [Creating an SMS campaign]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/).
{% endalert %}

## Sending best practices {#sending-best-practices}

### Multi-country SMS sending

Some brands may wish to send to a group of users that have phone numbers from different countries. In order to send an SMS message to a phone number in a particular country, it is best practice to use a long code or short code that is from the same country. In fact, short codes can only send SMS to phone numbers from the same country the short code was created in. 

To overcome this limitation, during the subscription groups [setup process]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process), groups can be set up to hold long and short codes from multiple different countries. When completed, sending phone numbers with the same country code as the target user's phone number will automatically be used when launching a campaign. You will not have to create separate campaigns for users with phone numbers with different country codes, allowing you to launch one campaign or use one Canvas component to target relevant users.

![SMS payloads are sent using the same country code as the target user's phone number]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

#### Best practices

1. **Get permission**. One of the most important rules for using SMS as a business is that you must first gain permission from customers to contact them. Failing to do so can damage your brand and result in hefty legal fees.<br><br>
2. **Choose the right number for your use case**. Three main types of phone numbers can send and receive SMS messages: long codes, short codes, and alphanumeric sender IDs, and their capabilities and availability in different regions vary. Think in advance if your business is served better with a vanity code. <br><br>
3. **Pay attention to timing**. Keep in mind that customers are more responsive to materials that are addressed directly to them. A little personalization goes a long way, such as using the recipients first name or adding a conversational touch that reflects your customers' interests.<br><br>
4. **Engage in two-way conversations**. SMS is such an effective channel for engaging with customers that it's important to anticipate - and effectively handle - responses to your messages. 85% of consumers not only want to be able to receive information but also reply to businesses or engage in a conversation.<br><br>
5. **Measure what works**. Are you reaching customers at the right time, with the best frequency, and using the most effective calls to action? Using the right tracking tools can offer direct and measurable metrics that prove their ROI. 

### High-volume sending

Plan on doing some high-volume sending? We have some best practices for you to ensure it runs smoothly.

- Adjust the delivery speed rate limiting for your campaign/canvases as needed, based on target audience size. This will ensure that you reach the send volume that you need and that Braze sends the messages at the rate that Twilio is expecting and can handle.
- Ensure you stick to the 160 character limit, and be aware of special characters double-counting (for example, forward-slashes `\`, carets `^`, and tildes `~`). 

