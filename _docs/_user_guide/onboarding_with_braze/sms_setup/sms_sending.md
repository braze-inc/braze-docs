---
nav_title: "SMS Message Sending"
page_order: 4
description: ""
page_type: reference
tool:
  - Dashboard
  - Docs
  - Campaigns

platform:
  - iOS
  - Android

channel:
  - SMS
---

# SMS Message Sending

## SMS Sending Basics

1. __Select Your Subscription Group__<br>
SMS messages must be sent from a [subscription group](({{Site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/sms_subscription_groups/)). A subscription group is a collection of sending phone numbers (i.e. short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. You must designate a subscription group to ensure only subscribed users are targeted. Some clients may find they have multiple subscription groups for different use cases, such as transactional SMS messaging and promotional SMS messaging.<br><br>

2. __Input Message Body__<br>
An SMS message body accepts up to 1600 characters, including Emojis, Liquid and Connected Content. A single campaign send can result in many message segment sends. Braze SMS message bodies can be composed of either [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) or [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) encoding standards. In the event that a UCS-2 character (for example, an Emoji) is used, the message body will automatically format for that encoding standard.<br><br> 

3. __Understand Message Segments & Character Limits__<br>
SMS message segments are how the SMS industry counts messages. A message segment is a grouping of up to a defined number of characters (160 for GSM-7 encoding; 67 for UCS-2 encoding) that will be sent in a single SMS dispatch. If you dispatch an SMS with 161 characters using GSM-7 encoding, you will see that there are two (2) message segments that were sent. Sending multiple message segments may result in additional charges.<br><br>

4. __Keyword Customization (Optional)__<br>
Regulations require that there are responses to all Opt-In, Opt-Out, and Help/Info SMS keyword responses. With Braze, you are able to define your own keywords to trigger Opt-In, Opt-Out, and Help responses, manage your own responsese that get sent to users, and define keyword sets for different languages. Read more about keyword customization [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/).

{% alert tip %}
For a step-by-step guide on how to create an SMS campaign in the Braze dashboard, check out our documentation [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/create/).
{% endalert %}

## Sending Best Practices

### Multi-Country SMS Sending
Some brands may wish to send to a group of users that have phone numbers from different countries. In order to send an SMS message to a phone number in a particular country, it is best practice to use a long code or short code that is from the same country. In fact, __short codes can only send SMS to phone numbers from the same country the short code was created in__. 

To overcome this limitation, during the Subscription Groups [setup process][5], groups can be set up to hold long and short codes from multiple different countries. Once completed, sending phone numbers with the same country code as the target user's phone number will automatically be used when launching a campaign. You will not have to create separate campaigns for users with phone numbers with different country codes, allowing you to launch one campaign or use one canvas step to target relevant users.

![picture][2]

#### Best Practices:

1. __Get Permission__. One of the most important rules for using SMS as a business is that you must first gain permission from customers to contact them. Failing to do so can damage your brand and result in hefty legal fees.<br><br>
2. __Choose the right number for your use case__. Three main types of phone numbers can send and receive SMS messages: long codes, short codes, and alphanumeric sender IDs, and their capabilities and availability in different regions vary. Think in advance if your business is served better with a vanity code. <br><br>
3. __Pay attention to timing__. Keep in mind that customers are more responsive to materials that are addressed directly to them. A little personalization goes a long way, such as using the recipients first name or adding a conversational touch that reflects your customers' interests.<br><br>
4. __Engage in two-way conversations__. SMS is such an effective channel for engaging with customers that it's important to anticipate - and effectively handle - responses to your messages. 85% of consumers not only want to be able to receive information but also reply to businesses or engage in a conversation.<br><br>
5. __Measure what works__. Are you reaching customers at the right time, with the best frequency, and using the most effective calls to action? Using the right tracking tools can offer direct and measurable metrics that prove their ROI. 

### High Volume Sending

Plan on doing some high volume sending? We have some best practices for you to ensure it runs smoothly.

- Adjust the delivery speed rate-limiting for your campaign/canvases as needed, based on target audience size. This will ensure that (1) you reach the send volume that you need and (2) Braze sends the messages at the rate that Twilio is expecting and can handle.
- Look to AE/leadership to assist with increased MPS rate discussions with Twilio.
Please note: higher throughput pricing needs to go through a deal desk.
- Ensure you are sticking to the 160 character limit, and aware of special characters double-counting (i.e. \ ^ &#126;). 

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
