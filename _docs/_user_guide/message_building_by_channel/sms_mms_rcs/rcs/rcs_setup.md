---
nav_title: "RCS Setup"
article_title: RCS Setup
page_order: 1
description: "This reference article covers the requirements needed to get RCS up and running."
page_type: reference
channel:
  - RCS
---

# Setting up RCS

> This article covers the requirements needed to get your RCS channel up and running.

## Prerequisites

| Requirement | Description |
|----|----|
| Message Credits | Contact your Braze customer success manager to confirm that you're set up on a Message Credits contract. Message Credits is a flexible contract type that allows you to purchase and allocate message volume across various channels, such as SMS and WhatsApp. |
| RCS-verified sender | The sending entity of an RCS message that the recipient sees on their device to identify where the message is coming from. An RCS-Verified Sender consists of a company name, visual branding, and a verified badge. <br><br>Braze will help you apply and register for an RCS-verified sender in eligible regions. You’ll need to provide your Braze representative with some basic information. |
| List of users with phone numbers | Before you can start sending messages, you must add users to your account. Additionally, you must know the approximate size of your audience. Users and phone numbers can be added to Braze through several different methods. Phone numbers must be formatted as a 10-digit number, as well as a country area code. Learn more about [user phone numbers](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting). |
| Keywords and responses | All base keywords must have responses attributed to it before you can begin messaging. Braze will process opt-in, opt-out, and help keywords automatically. Customization options and additional keyword-response configurations are available. <br><br>Learn more about [keywords and responses](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/keywords/optin_optout). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## RCS verified senders

After you have purchased your RCS SKUs, confirmed your region eligibility, and are up and running on our Message Credits system, you’re ready to set up your RCS-verified senders. These are the sending entities that your customers will see on their mobile devices which represent your business, and that RCS presents robustly to enhance trust. As opposed to SMS, which identifies your business by a simple phone number, an RCS-verified sender consists of a company name, visual branding, and a verified badge. 

To set up an RCS-verified sender, contact your Braze representative. We'll guide you through the RCS sender registration process and handle the creation of any subscription groups.

## SMS fallback

For optimal message delivery, it's recommended for each subscription group to have an RCS and an SMS sender because Braze will attempt to fallback to SMS when RCS is unavailable. The SMS sender should be capable of delivering messages to the target country. For example, if your RCS sender is registered to send in the UK, you would include a UK long code in the subscription group.

A few example scenarios of where RCS may be unavailable include:

- The recipient's mobile device does not support RCS due to older hardware or software versions
- An RCS send attempt to a region where the RCS sender is not registered