---
nav_title: "About SMS"
page_order: 0
description: "This reference article covers general use cases of the SMS channel and the laws and regulations surrounding SMS."
page_type: reference
channel: SMS
tool:
  - Docs
  - Dashboard
  - Campaigns
---

# What are SMS Messages?

> SMS, also known as Short Message Service, is used to send text messages to mobile phones. Currently, there are over 23 billion text messages sent every day worldwide, with SMS being the most direct way to reach users and customers. This widespread usage and proven value has made SMS an effective marketing tool for businesses of all sizes. <br><br>This article discusses some common use cases as well as some resources and practical guidance that will allow you to work within the bounds of regulations and laws while still communicating effectively and strategically with your customers.

## Potential Use Cases

| Use Case | Explanation |
|---|---|
| General Marketing | SMS messages are a direct, flexible and efficient way to communicate upcoming deals, favorable sales, and current or anticipated products to your customers. |
| Reminders | SMS messages can be effective in notifying users who have set an appointment for a service. For example, sending an SMS message reminding a customer the day before a doctor's appointment will help minimize missed appointments, saving both our clients and their users time and money. |
| Product Verification or Password Confirmation | If your application requires authentication to access it, the SMS channel could be a good way to accomplish this.|
{: .reset-td-br-1 .reset-td-br-2}

## SMS Laws, Regulations, & Abuse Prevention

Because SMS messages are one of the most direct ways to reach customers and users, going directly to the user’s phone, regulations must exist that prevent brands from abusing or over-using this relationship, and fines for violations could cost thousands of dollars. 

{% alert warning %}
This article is not intended to provide, nor may it be relied upon as providing legal advice. The use of SMS is subject to specific legal requirements.  To ensure that you are using the SMS Services in compliance with all applicable laws, you should seek the advice of your own legal counsel.
{% endalert %}

In general, we encourage using your best judgment when approaching SMS sending. Braze, as well as our sending partners, have checks in place that prevent most SMS abuses. There are a few general rules you should follow:

- Do not SPAM.
- Offer your recipients a way to opt-out and get help via SMS.
- Send at a healthy cadence - do not overwhelm your customers.
- Do not send abusive or inappropriate content (for example, sending marketing content to someone who only wants transactional content).

### Resources

Here are some links you might need to consult as you build up your SMS campaign:

- [CTIA's Messaging Principles and Best Practices for 2019](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf)
- Twilio's [Guide to US SMS Compliance](https://www.twilio.com/learn/call-and-text-marketing/guide-to-us-sms-compliance)
- IBM's [Introduction to SMS Compliance](https://www.ibm.com/support/knowledgecenter/en/SSWU4L/Mobile/imc_Mobile/SMS_Compliance_Information.html)

### Considerations for Compliance

#### Data and Privacy

A customer's privacy is key to a meaningful and respectful relationship. Respecting a customer's privacy and information is just another opportunity to create a bond between them and your brand. Sometimes, using marketing tools can put data and privacy last.

Luckily for you, Braze follows the guidelines of [many security regulations]({{ site.basurl }}/developer_guide/disclosures/security_qualifications/#security-qualifications), including [GDPR]({{ site.baseurl }}/help/gdpr_compliance/).

The CTIA recommends that you maintain and conspicuously display a clear and easy-to-understand privacy policy.

#### Consent

Opt-in, help, and opt-out options are an absolute must when creating SMS campaigns.

The [TCPA](https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991) (Telephone Consumer Protection Act) mandates that a business must receive "express written consent" in order to send customers messages - you can do this in a multitude of ways, including web or mobile. You must be clear with the customer about how you intend to use SMS to communicate with them.

Remember to comply with the [National Do Not Call Registry](https://www.donotcall.gov/).

Braze uses [Subscription Groups]({{ site.baseurl }}/user_guide/message_building_by_channel/sms/keywords/) to manage groups of users based on their level of consent.

#### Spam and Cadence

Similar to email, your users or customer can experience inbox burnout. But this is only one reason not to relentlessly message your customers. You should look specifically at [Section 5 of the FTC Act to ensure compliance (in the U.S.)](https://www.federalreserve.gov/boarddocs/supmanual/cch/ftca.pdf).

Some spam considerations are built into SMS capabilities in general (long and short code sending limits), as well as Braze's own rate limits. However, you should still take the compliance laws into consideration when planning your campaigns.

#### Content

This can be a tricky one, but when in doubt, avoid topics that involve violence, sex, drugs, tobacco, or other paraphernalia. Be wise when sending messages regarding these topics - you may still be charged for messages that are blocked by various carriers.

The [CTIA](https://www.ctia.org/) (a trade association representing the wireless communications industry in the United States) recommends that you follow __SHAFT Compliance__, which defines the following topics as generally "illegal" when messaging in the United States:

- Sex
- Hate
- Alcohol
- Firearms
- Tobacco

You can [read more about the CTIA's Messaging Principles and Best Practices for 2019 here](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf).

#### Scheduling

Please ensure you comply with the [TCPA](https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991) (Telephone Consumer Protection Act), which dictates that you shouldn't send messages during late hours (see the regulation's contents for exact hours). However, you shouldn't send messages that late anyway - don't you want high engagement?

#### International

Most of these best practices apply to guidelines set forth in the United States of America. If you are reaching customers outside of U.S. regions, _please research best practices and laws in those areas_. It is always best practice to act in a way that _adheres to the most stringent regulations_, which are usually applied in the United States, Canada, and countries part of the European Union.

Better to be safe than sorry!
