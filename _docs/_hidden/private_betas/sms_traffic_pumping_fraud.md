---
nav_title: SMS Traffic Pumping Fraud FAQs
permalink: "/sms_traffic_pumping_fraud/"
description: "This reference article covers frequently asked questions for SMS traffic pumping fraud."
hidden: true
---

# SMS traffic pumping fraud FAQs 

### What is SMS traffic pumping fraud? 

SMS traffic pumping is a rising threat in the SMS space. It occurs when fraudsters find a way to trigger SMS message sends to phone numbers that are not associated with real customers in order to collect revenue tied to fraudulent message sending. Most often, they trigger high-volume SMS sends using online forms, such as forms for SMS opt-ins or one-time passwords for password resets or account login.  

For example, if a brand has an SMS sign-up form on their website for customers to opt-in to receive text messages, a fraudster will enter fraudulent phone numbers into the form to trigger SMS messages. The fraudster uses premium rate phone numbers for these messages and claims a revenue share from the local mobile carrier, who is responsible for the delivery of the messages to end-users. This scheme generates fraudulent charges to the brand. 

### What does Braze do to mitigate SMS pumping fraud?

Braze currently maintains an SMS blocklist for both US-embargoed countries, as well as for countries known to be high risk for traffic pumping, which can be referenced in [our documentation]({{site.baseurl}}/sms_country_blocklist). All attempted sends to phone numbers with these country codes are blocked.

Additionally, Braze is introducing an SMS Geographic Permission Allowlist, which will further protect against fraudulent behavior by enforcing controls on what countries you are able to send to.

### How can I protect my brand against SMS pumping fraud? 

There are several ways you can protect yourself, including: 
- **Monitor your daily SMS sending volumes for spikes and abnormalities:**
    - We recommend setting [campaign limits and alerts]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) to cap and notify if an unusually high number of messages are sent.
    - Unusual spikes in sending of messages might indicate traffic pumping.
    - Unusually high number of opt-ins in a short time frame (outside of intentional strategies to drive opt-ins) might indicate traffic pumping.
- **Improve security for online phone number capture forms:**
    - Braze [SMS sign-up form templates]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) provide out-of-the box security measures, such as validating the phone number length and format. You can also set up the form to only collect phone numbers with country codes that align to your target customers:
        - For example, if you only do business in the US and UK, set up the form to only collect numbers with a +1 and +44 country code (technical details can be found in [our documentation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/#step-2-customize-your-phone-number-input-component)).
    - If you are building a custom phone number capture on your website, we recommend setting rules to validate phone number length and format and ensuring forms are fully complete before collecting phone numbers. Be sure to work with your engineering or technical team to validate the form inputs both client-side and server-side for maximum protection.
        - Additionally, consider using tools such as CAPTCHA to ensure the form is submitted by a human and not an automated process. A CAPTCHA requirement on SMS sign-up forms can help reduce the number of fraudulent sign-ups.

### My brand does business in the US and the US is on my SMS Geographic Permission Allowlist. Will my customers still receive my SMS messaging when they travel outside of the US? 

Yes, as long as your customers have a phone number with a US area code, they will still receive your messages while traveling. 

{% alert important %}
If you have additional questions about SMS traffic pumping and how these product changes may affect your SMS sending, please reach out to your customer success manager.
{% endalert %}
