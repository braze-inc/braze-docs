---
nav_title: "SMS Laws & Regulations"
page_order: 1
description: "This reference article covers laws and regulations surrounding SMS."
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

# SMS Laws, Regulations, & Abuse Prevention

Because SMS messages are one of the most direct ways to reach customers and users, going directly to the user’s phone, regulations must exist that prevent brands from abusing or over-using this relationship, and fines for violations could cost thousands of dollars. 

{% alert warning %}
This article is not intended to provide, nor may it be relied upon as providing legal advice. The use of SMS is subject to specific legal requirements. To ensure that you are using the SMS Services in compliance with all applicable laws, you should seek the advice of your legal counsel.
{% endalert %}

## The Six Rules to Get Compliance Right

In general, we encourage using your best judgment when approaching SMS sending. Braze, as well as our sending partners, have checks in place that prevent most SMS abuses.

__There are the six rules you should follow:__

1. __Obtain explicit consent from users before sending them SMS.__ Whenever users provide consent, it's your responsibility to log, update, and maintain that information in a compliant user database. According to basic legal guidelines, the most important information you need to retain regarding consent is:
- __The time and date the user gave consent__
- __The type of SMS messaging they consented to__
- __The users' phone number__
- __The language in which they opted-in__<br><br>

2. __Clearly communicate the types of SMS you'll be sending__. Users should understand what messages to expect from your brand in this channel and the kinds of information or offers they'll be receiving. Explicitly state the purpose of your future campaigns, message frequency, and remind users that message/data rates apply.<br><br>

3. __Keep essential information updated and visible__. Ensure that the most up to date version of your brand's Terms and Conditions and your SMS Marketing Privacy Policy are clearly visible and easily accessible from your SMS opt-in page.<br><br>

4. __Only send SMS to legally obtained, opted-in phone numbers__. As part of technical migration planning, ensure that your team understands the mechanism for tying opt-in statuses to each and every user profile in your customer engagement platform.<br><br>

5. __Ensure SHAFT compliance in the US and other relevant regions.__ Sending SMS messages that contain language around sex, hate, alcohol, firearms, and tobacco (SHAFT) is generally considered to be illegal in the US and some other regions.<br><br>

6. __Double-check everything__. Work with your legal team to ensure that your SMS program is fully compliant with all applicable rules and regulations for the regions your brand operates in.<br><br>

## Resources

Here are some links you might need to consult as you build up your SMS campaign:

- [CTIA's Messaging Principles and Best Practices for 2019](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf)
- [Twilio's Guide to US SMS Compliance](https://www.twilio.com/learn/call-and-text-marketing/guide-to-us-sms-compliance)
- [IBM's Introduction to SMS Compliance](https://www.ibm.com/support/knowledgecenter/en/SSWU4L/Mobile/imc_Mobile/SMS_Compliance_Information.html)

## Considerations for Compliance

### Data and Privacy

A customer's privacy is key to a meaningful and respectful relationship. Respecting a customer's privacy and information is just another opportunity to create a bond between them and your brand. Sometimes, using marketing tools can put data and privacy last.

Luckily for you, Braze follows the guidelines of [many security regulations]({{site.baseurl}}/developer_guide/disclosures/security_qualifications/#security-qualifications), including [GDPR]({{site.baseurl}}/help/gdpr_compliance/).

The CTIA recommends that you maintain and conspicuously display a clear and easy-to-understand privacy policy.

### Consent

Opt-in, help, and opt-out options are an absolute must when creating SMS campaigns.

The [TCPA](https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991) (Telephone Consumer Protection Act) mandates that a business must receive "express written consent" to send customers messages - you can do this in a multitude of ways, including web or mobile. You must be clear with the customer about how you intend to use SMS to communicate with them.

Remember to comply with the [National Do Not Call Registry](https://www.donotcall.gov/).

Braze uses [Subscription Groups]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) to manage groups of users based on their level of consent.

### Spam and Cadence

Similar to email, your users or customer can experience inbox burnout. But this is only one reason not to relentlessly message your customers. You should look specifically at [Section 5 of the FTC Act to ensure compliance (in the U.S.)](https://www.federalreserve.gov/boarddocs/supmanual/cch/ftca.pdf).

Some spam considerations are built into SMS capabilities in general (long and short code sending limits), as well as Braze's rate limits. However, you should still consider compliance laws when planning your campaigns.

### Content

This can be a tricky one, but when in doubt, avoid topics that involve violence, sex, drugs, tobacco, or other paraphernalia. Be wise when sending messages regarding these topics - you may still be charged for messages that are blocked by various carriers.

The [CTIA](https://www.ctia.org/) (a trade association representing the wireless communications industry in the United States) recommends that you follow __SHAFT Compliance__, which defines the following topics as generally "illegal" when messaging in the United States:

- Sex
- Hate
- Alcohol
- Firearms
- Tobacco

You can [read more about the CTIA's Messaging Principles and Best Practices for 2019 here](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf).

### Scheduling

Please ensure you comply with the [TCPA](https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991) (Telephone Consumer Protection Act), which dictates that you shouldn't send messages during late hours (see the regulation's contents for exact hours). However, you shouldn't send messages that late anyway - don't you want high engagement?

### International

Most of these best practices apply to guidelines set forth in the United States of America. If you are reaching customers outside of U.S. regions, _please research best practices and laws in those areas_. It is always best practice to act in a way that _adheres to the most stringent regulations_, which are usually applied in the United States, Canada, and countries part of the European Union.

Better to be safe than sorry!