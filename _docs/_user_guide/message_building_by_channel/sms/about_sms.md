---
nav_title: "About SMS"
article_title: About SMS
page_order: 0
description: "This reference article covers general use cases of the SMS channel and requirements needed to get SMS up and running."
page_type: reference
channel:
  - SMS
---

# About SMS messages

![SMS message with the text "Welcome to Braze! We are excited to have you on board. Check out our documentation to get started. https://www.braze.com/docs/ Text HELP for help and STOP to stop."][picture]{: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

> This article shares some common use cases to draw from, requirements, and terms to know that will aid your SMS integration and allow you to communicate effectively and strategically with your customers. In addition to this article, you can also check out our [SMS & MMS](https://learning.braze.com/messaging-channels-sms) Braze Learning course.

SMS, also known as Short Message Service, is used to send text messages to mobile phones. Currently, there are over 23 billion text messages sent every day worldwide, with SMS being the most direct way to reach users and customers. This widespread usage and proven value have made SMS an effective marketing tool for businesses of all sizes. 

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
| A dedicated phone number (either a Short Code or Long Code) | A dedicated phone number provided exclusively to a single brand or host. | Braze handles acquiring these numbers for you. Learn more about [short and long codes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/).|
| List of users with phone numbers | Before you can start sending messages, you must add users to your account. Additionally, you must know the approximate size of your audience.  | Users are initially added to Braze through our backend. You must pass this list to us to upload for you. Phone numbers must be formatted as a 10-digit number, as well as a country area code. Learn more about [user phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/). |
| [SMS keywords and responses]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) | All base keywords must have responses attributed to it before you can begin messaging | You should list these out and send them to your Braze representative or onboarding manager during your onboarding process. View [SMS keyword templates]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Terms to know

- **Short code:** A 5 to 6-digit code, that's shorter than a full phone number. This code is used to address and send SMS messages.<br><br>
- **Long codes:** A 10-digit code that is used to address SMS messages. Most average phone numbers are considered long codes (e.g 123-456-7891). These codes are used to address and send SMS messages.<br><br>
- **Subscription group:** A Subscription Group is a collection of sending phone numbers (i.e., short codes, long codes, and/or alphanumeric sender IDs) that are used for a specific type of messaging purpose. For example, if a brand has plans to send both transactional and promotional SMS messaging, two Subscription Groups with separate pools of sending phone numbers will need to be set up within your Braze dashboard.<br><br>
- **Message segment and character limits:** A message segment refers to how many segments your initial SMS message will be split into. Each message has a character limit that if exceeded, will cause the message to be broken into segments. Based on what encoding standards you use (UTF-2 or GSM-7), there are varying character limits. Reference our [message copy limits][2] for more information on messaging segmentation and message character limits.<br><br>
- **Common SMS campaign metrics:** <br>`Sent`, `Sent to Carrier`, `Delivery Failures`, `Confirmed Delivery`, `Rejections`, `Opt-Out`, and `Help`. <br>For information on these metrics, refer to [SMS reporting][1].


[picture]: {% image_buster /assets/img/sms/sms_about.jpg %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy
