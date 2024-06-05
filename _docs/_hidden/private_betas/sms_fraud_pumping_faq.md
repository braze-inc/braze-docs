---
nav_title: SMS Fraud Pumping FAQs
article_title: SMS Fraud Pumping FAQs
permalink: "/sms_fraud_pumping_faq/"
description: "This reference article covers frequently asked questions for SMS fraud pumping."
hidden: true
---

# SMS fraud pumping FAQs

### What is SMS traffic pumping fraud?

SMS traffic pumping is a rising threat in the SMS space. It occurs when fraudsters find a way to trigger SMS message sends to phone numbers that are not associated with real customers in order to collect revenue tied to fraudulent message sending. Most often, they trigger high volume SMS sends using online forms, e.g. for SMS opt-ins or one-time passwords for password resets or account login.

For example, if a brand has an SMS sign-up form on their website for customers to opt-in to receive text messages, a fraudster will enter fraudulent phone numbers into the form to trigger SMS messages. The fraudster uses premium rate phone numbers for these messages and claims a revenue share from the local mobile carrier, who is responsible for the delivery of the messages to end-users. This scheme generates fraudulent charges to the brand.

### What does Braze do to mitigate SMS pumping fraud?

Braze currently maintains an SMS blocklist for both US-embargoed countries, as well as for countries known to be high risk for traffic pumping, which can be referenced in [our documentation]({{site.baseurl}}/sms_country_blocklist). All attempted sends to phone numbers with these country codes are blocked.

Additionally, Braze is introducing an SMS Geographic Permission Allow List, which will further protect against fraudulent behavior by enforcing controls on what countries you are able to send to.

### How can I protect my brand against SMS pumping fraud?

There are several ways you can protect yourself, including:
- **Monitor your daily SMS sending volumes for spikes and abnormalities**
    - We recommend customers set [campaign limits and alerts]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) to cap and notify if an implausibly high number of messages are sent. 
    - Unusual spikes in sending of messages might indicate traffic pumping.  
    - Unusually high number of opt-ins in a short time frame (outside of intentional strategies to drive opt-ins) might indicate traffic pumping.
- **Improve security for online phone number capture forms**
    - We recommend that when building online forms, customers set rules to ensure forms are fully complete. As a best practice, ensure you validate the form input both client-side and server-side for maximum protection.
    - Use tools such as CAPTCHA to ensure the form is submitted by a human and not an automated process. A CAPTCHA requirement on SMS sign-up forms can help reduce the number of fraudulent sign-ups.
- **Set up your form to only collect phone numbers with country codes that align to your target customers**
    - For example, if you only do business in the US and UK, set up the form to only collect numbers with a +1 and +44 country code (technical details can be found in [our documentation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/#step-2-customize-your-phone-number-input-component)). 

### I do business in the US and the US is on my SMS Geographic Permission Allow List. Will my customers still receive my SMS messaging when they travel outside of the US? 

Yes, as long as your customers have a phone number with a US area code, they will still receive your messages while traveling.