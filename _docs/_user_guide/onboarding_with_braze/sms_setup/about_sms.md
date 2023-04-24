---
nav_title: "About SMS"
article_title: About SMS
page_order: 0
description: "This reference article covers general use cases of the SMS channel, requirements, and terms to know."
page_type: reference
noindex: true
channel:
  - SMS
  
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}About SMS messages

> This article shares some common use cases to draw from, requirements, and terms to know that will aid your SMS integration and allow you to communicate effectively and strategically with your customers.![SMS message with the text "Welcome to Braze! We are excited to have you on board. Check out our documentation to get started. https://www.braze.com/docs/ Text HELP for help and STOP to stop."][picture]{: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
SMS, also known as Short Message Service, is used to send text messages to mobile phones. Currently, there are over 23 billion text messages sent every day worldwide, with SMS being the most direct way to reach users and customers. This widespread usage and proven value have made SMS an effective marketing tool for businesses of all sizes. 
<br><br>

## Potential use cases

| Use Case | Explanation |
|---|---|
| General Marketing | SMS messages are a direct, flexible, and efficient way to communicate upcoming deals, favorable sales, and current or anticipated products to your customers. |
| Reminders | SMS messages can be effective in notifying users who have set an appointment for a service. For example, sending an SMS message reminding a customer the day before a doctor's appointment will help minimize missed appointments, saving both you and your customers time and money. |
| Transactional Messages | SMS messages are an efficient way to send out transactional notifications such as order confirmations and shipping information, providing them all the information they need in one convenient place. Note that legal guidelines exist that must be adhered to when sending Transactional Messages. If you are unsure of these guidelines, reach out to your internal legal team.|
{: .reset-td-br-1 .reset-td-br-2}

## Requirements

Before you start sending SMS, there are some things you need. Refer to the following chart to learn more.

|Requirement | Description | Acquirement |
|---|---|---|
| A Dedicated Phone Number (either a Short Code or Long Code) | A dedicated phone number provided exclusively to a single brand or host. | Braze handles acquiring these numbers for you. For more, refer to [Short and long codes]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/).|
| List of Users with Phone Numbers | Before you can start sending messages, you must add users to your account. Additionally, you must know the approximate size of your audience.  | Users are initially added to Braze through our backend. You must pass this list to us to upload for you. Phone numbers must be formatted as a 10-digit number, as well as a country area code. For more, refer to [User data migration]({{site.baseurl}}//user_guide/onboarding_with_braze/sms_setup/user_data_migration/). |
| [SMS Keywords and Responses]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) | All base keywords must have responses attributed to it before you can begin messaging | You should list these out and send them to your Braze representative or onboarding manager during your onboarding process. For examples, refer to [Short code application]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/#short-code-application). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Terms to know

- **Short Code:** A 5 to 6-digit code, that's shorter than a full phone number. This code is used to address and send SMS messages.<br><br>
- **Long Codes:** A 10-digit code that is used to address SMS messages. Most average phone numbers are considered long codes (e.g 123-456-7891). These codes are used to address and send SMS messages.<br><br>
- **Subscription Group:** A Subscription Group is a collection of sending phone numbers (i.e., short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. For example, if a brand has plans to send both transactional and promotional SMS messaging, two Subscription Groups with separate pools of sending phone numbers will need to be set up within your Braze dashboard.<br><br>
- **Message Segment & Character Limits:** A message segment refers to how many segments your initial SMS message will be split into. Each message has a character limit that if exceeded, will cause the message to be broken into segments. Based on what encoding standards you use (UTF-2 or GSM-7), there are varying character limits. For more information on message segments and message character limits, refer to [SMS sending basics][2].<br><br>
- **Common SMS Campaign Metrics:** <br>`Sent`, `Sent to Carrier`, `Delivery Failures`, `Confirmed Delivery`, `Rejections`, `Opt-Out`, and `Help`. <br>For information on these metrics, refer to [SMS reporting][1].

<br><br>

For a full list of terms, visit our SMS [Terms to Know]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/terms/) or our dedicated [SMS section]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) for more topics like how to create a SMS campaign, SMS campaign analytics, and SMS keyword processing.

[picture]: {% image_buster /assets/img/sms/sms_about.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/sms_sending/
