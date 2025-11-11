---
nav_title: "SMS"
article_title: About SMS
page_order: 13
description: "This reference article covers general use cases of the SMS channel and requirements needed to get SMS up and running."
page_type: reference
alias: /about_sms/
channel:
  - SMS
search_rank: 2
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}About SMS

> This article shares some common use cases to draw from, requirements, and terms to know that will aid your SMS integration and allow you to communicate effectively and strategically with your customers.![SMS message with the text "Welcome to Braze! We are excited to have you on board. Check out our documentation to get started. https://www.braze.com/docs/ Text HELP for help and STOP to stop."]({% image_buster /assets/img/sms/sms_about.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
SMS, also known as Short Message Service, is used to send text messages to mobile phones. Currently, there are over 23 billion text messages sent every day worldwide, with SMS being the most direct way to reach users and customers. This widespread usage and proven value have made SMS an effective marketing tool for businesses of all sizes. 
<br><br>
## Potential use cases

| Use Case | Explanation |
|---|---|
| General Marketing | SMS messages are a direct, flexible, and efficient way to communicate upcoming deals, favorable sales, and current or anticipated products to your customers. |
| Reminders | SMS messages can be effective in notifying users who have set an appointment for a service. For example, sending an SMS message reminding a customer the day before a doctor's appointment will help minimize missed appointments, saving both you and your customers time and money. |
| Transactional Messages | SMS messages are an efficient way to send out transactional notifications such as order confirmations and shipping information, providing them all the information they need in one convenient place. Note that legal guidelines exist that must be adhered to when sending Transactional Messages. If you are unsure of these guidelines, contact your internal legal team.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Requirements

Before you start sending SMS, there are some things you need. Refer to the following chart to learn more.

|Requirement | Description | Acquirement |
|---|---|---|
| A dedicated phone number (either a Short Code or Long Code) | A dedicated phone number provided exclusively to a single brand or host. | Braze handles acquiring these numbers for you. Learn more about [short and long codes]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).|
| List of users with phone numbers | Before you can start sending messages, you must add users to your account. Additionally, you must know the approximate size of your audience.  | Users are initially added to Braze through our backend. You must pass this list to us to upload for you. Phone numbers must be formatted as a 10-digit number, as well as a country area code. Learn more about [user phone numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). |
| [SMS keywords and responses]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/) | All base keywords must have responses attributed to it before you can begin messaging | You should list these out and send them to your Braze representative or onboarding manager during your onboarding process. View [SMS keyword templates]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Terms to know

For a full list of terms, visit our SMS [Terms to Know]({{site.baseurl}}/sms_terms_to_know/).

