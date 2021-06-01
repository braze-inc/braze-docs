---
nav_title: "Multi-Country SMS Sending"
page_order: 3
description: "This reference article covers multi-country sending best practices for SMS messaging."
page_type: reference
tool:
  - Dashboard
  
channel:
  - SMS
---

# Multi-Country SMS Sending

Some brands may wish to send to a group of users that have phone numbers from different countries. In order to send an SMS message to a phone number in a particular country, it is best practice to use a long code or short code that is from the same country. In fact, __short codes can only send SMS to phone numbers from the same country the short code was created in__. 

To overcome this limitation, during the Subscription Groups [setup process][5], groups can be set up to hold long and short codes from multiple different countries. Once completed, sending phone numbers with the same country code as the target user's phone number will automatically be used when launching a campaign. You will not have to create separate campaigns for users with phone numbers with different country codes, allowing you to launch one campaign or use one canvas step to target relevant users.

![picture][2]

## Best Practices:

1. __Get Permission__. One of the most important rules for using SMS as a business is that you must first gain permission from customers to contact them. Failing to do so can damage your brand and result in hefty legal fees.<br><br>
2. __Choose the right number for your use case__. Three main types of phone numbers can send and receive SMS messages: long codes, short codes, and alphanumeric sender IDs, and their capabilities and availability in different regions vary. Think in advance if your business is served better with a vanity code. <br><br>
3. __Pay attention to timing__. Keep in mind that customers are more responsive to materials that are addressed directly to them. A little personalization goes a long way, such as using the recipients first name or adding a conversational touch that reflects your customers' interests.<br><br>
4. __Engage in two-way conversations__. SMS is such an effective channel for engaging with customers that it's important to anticipate - and effectively handle - responses to your messages. 85% of consumers not only want to be able to receive information but also reply to businesses or engage in a conversation.<br><br>
5. __Measure what works__. Are you reaching customers at the right time, with the best frequency, and using the most effective calls to action? Using the right tracking tools can offer direct and measurable metrics that prove their ROI. 

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process