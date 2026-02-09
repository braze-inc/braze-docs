---
nav_title: "Best practices"
article_title: Best Practices for SMS, MMS, and RCS 
page_order: 15
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
* [Keyword processing]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/): Explanations for how Braze approaches keyword processing and management.
* [SMS double opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/): Requires users to explicitly confirm their opt-in intent before they can receive SMS messages. SMS double opt-in is a requirement for some countries, so Braze recommends configuring this.
* [SMS message sending]({{site.baseurl}}/sending_phone_numbers/): Fundamentals of SMS sending at Braze, including the importance of subscription groups, requirements for SMS segments and message bodies, and more.

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

