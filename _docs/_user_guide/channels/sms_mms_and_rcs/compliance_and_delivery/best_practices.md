---
nav_title: "Best practices"
article_title: Best Practices for SMS, MMS, and RCS 
page_order: 2
description: "This reference article covers best practices for SMS/MMS."
alias: /sms_mms_rcs_best_practices/
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Best practices for SMS, MMS, and RCS 

> Learn more about best practices for SMS, MMS, and RCS with Braze, including our recommendations for opt-out monitoring and traffic pumping.

## Opt-out monitoring recommendations

Complying with recipient requests to opt-out of communications is required by law. Failing to comply with requests by SMS recipients to opt-out of the channel can incur penalties, including fines, and can lead to lawsuits. Braze has features in place to enable robust SMS and MMS opt-in and out management, plus mechanisms to assist in making sure requests are correctly processed.

Under their subscription agreements with us, our customers are solely responsible  for their compliance with applicable law in their use of our services. Accordingly, we strongly recommend that customers pay close attention to correctly configuring their SMS set-up, and that they test those set-ups thoroughly, take measures to monitor opt-out compliance, and act promptly should they identify instances of non-compliance with opt-out requests.

When setting up SMS and MMS in Braze to manage opt-ins and opt-outs, refer to the following list of resources:
* [SMS subscription groups]({{site.baseurl}}/sms_rcs_subscription_groups/): Subscription groups and opt-in/out methods and statuses.
* [Subscription Group REST APIs]({{site.baseurl}}/api/endpoints/subscription_groups): How to process opt-ins and outs they receive from a source other than a direct response to a message.
* [Keyword processing]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/): Explanations for how Braze approaches keyword processing and management.
* [SMS double opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/): Requires users to explicitly confirm their opt-in intent before they can receive SMS messages. SMS double opt-in is a requirement for some countries, so Braze recommends configuring this.
* [SMS message sending]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending/): Fundamentals of SMS sending at Braze, including the importance of subscription groups, requirements for SMS segments and message bodies, and more.

### Considerations

Where SMSand MMS have been set up across multiple instances, and due to misconfiguration, a campaign or Canvas opt-outs are sent to the wrong workspace.

* Braze has monitoring in place to identify such instances. If this behavior is flagged, Braze will repoint opt-outs to the correct instance and backfill any opt-outs that occurred during the period.
* We strongly recommend customers test opt-outs for each subscription group they have in Braze. Identifying this issue before launching a message is better than mitigating after an issue has been identified.

Braze manages SMS/MMS subscriptions at both the user profile (`user_id`) level and the phone number (`channel_id`) level. When a phone number is opted-in or out, the update applies to all profiles which share that number. In the case where an end user opted-in with a certain phone number, but then changes phone number, the new phone number will inherit the subscription group status of the user. Accordingly, if an end user has opted-out, but then re-enters the app or website with a new phone number, they will not receive unwanted messages.

## Traffic pumping recommendations

### What is traffic pumping?

Traffic pumping is a form of fraud that occurs when a bad actor uses an online form to trigger SMS messages to be sent at high volume (for example opt-in messages or one-time passwords). The bad actor sets up a premium rate phone number for these messages to be sent to and claims a revenue share from the mobile operator with which the premium rate number has been set up, thus generating illicit revenue.

### How to spot traffic pumping

* Premium rate numbers supporting this kind of scam are often, but not always, set up in countries outside of your normal sending geographies.
* Unusual spikes in sending of messages from online forms might indicate traffic pumping.
    * We recommend setting up [campaign alerts]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) to cap and notify if an implausibly high number of messages are sent.
* Incomplete online forms can indicate programmatic form filling.
* When building online forms, we recommend setting rules to ensure forms are fully complete and use tools such as CAPTCHA to minimise risk.

### Impact of traffic pumping

Customers are responsible for monitoring the traffic that they are sending and will be invoiced for all SMS sent through their account. Between Braze and Customer, Customer is the party in the better position to detect and prevent traffic pumping.

## Multi-country SMS sending

Some brands may wish to send to a group of users that have phone numbers from different countries. In order to send an SMS message to a phone number in a particular country, it is best practice to use a long code or short code that is from the same country. In fact, short codes can only send SMS to phone numbers from the same country the short code was created in. 

To overcome this limitation, during the subscription groups [setup process]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/), groups can be set up to hold long and short codes from multiple different countries. When completed, sending phone numbers with the same country code as the target user's phone number will automatically be used when launching a campaign. You will not have to create separate campaigns for users with phone numbers with different country codes, allowing you to launch one campaign or use one Canvas component to target relevant users.

![SMS payloads are sent using the same country code as the target user's phone number.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### General sending best practices

1. **Get permission.** One of the most important rules for using SMS as a business is that you must first gain permission from customers to contact them. Failing to do so can damage your brand and result in hefty legal fees.
2. **Choose the right number for your use case.** Three main types of phone numbers can send and receive SMS messages: long codes, short codes, and alphanumeric sender IDs, and their capabilities and availability in different regions vary. Think in advance if your business is served better with a vanity code.
3. **Pay attention to timing.** Keep in mind that customers are more responsive to materials that are addressed directly to them. A little personalization goes a long way, such as using the recipient's first name or adding a conversational touch that reflects your customers' interests.
4. **Engage in two-way conversations.** SMS is such an effective channel for engaging with customers that it's important to anticipate and effectively handle responses to your messages. 85% of consumers not only want to be able to receive information but also reply to businesses or engage in a conversation.
5. **Measure what works.** Are you reaching customers at the right time, with the best frequency, and using the most effective calls to action? Using the right tracking tools can offer direct and measurable metrics that prove their ROI. 

## High-volume sending

Plan on doing some high-volume sending? We have some best practices for you to ensure it runs smoothly.

- Adjust the delivery speed rate limiting for your campaign or Canvases as needed, based on target audience size. This ensures that you reach the send volume that you need and that Braze sends the messages at the rate that Twilio is expecting and can handle.
- Ensure you stick to the 160-character limit, and be aware of special characters double-counting (for example, forward-slashes `\`, carets `^`, and tildes `~`). 
