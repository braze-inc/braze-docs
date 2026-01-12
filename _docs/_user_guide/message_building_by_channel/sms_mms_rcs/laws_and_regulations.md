---
nav_title: "Laws & regulations"
article_title: Laws & Regulations for SMS, MMS, and RCS
page_order: 0
description: "This reference article covers laws and regulations surrounding SMS, MMS, and RCS."
page_type: reference
alias: /sms_mms_rcs_laws/
channel:
  - SMS
  - MMS
  - RCS
---

# Laws, regulations, and abuse prevention for SMS, MMS, and RCS

> Because SMS, MMS, and RCS messages are one of the most direct ways to reach customers and users, going directly to the user's phone, regulations must exist that prevent brands from abusing or over-using this relationship, and fines for violations could cost thousands of dollars. 

{% alert warning %}
This article is not intended to provide, nor may it be relied upon as providing legal advice. The use of SMS, MMS, and RCS is subject to specific legal requirements. To ensure that you are using the SMS, MMS, and RCS Services in compliance with all applicable laws, you should seek the advice of your legal counsel.
{% endalert %}

## The six rules to get compliance right

In general, we encourage using your best judgment when sending SMS, MMS, or RCS messages. Braze, as well as our sending partners, have checks in place that prevent most SMS, MMS, and RCS abuses.

Use the following rules when sending messages:

1. **Obtain explicit consent from users before sending them SMS, MMS, or RCS.** Whenever users provide consent, it's your responsibility to log, update, and maintain that information in a compliant user database. According to basic legal guidelines, the most important information you need to retain regarding consent is:
  - The time and date the user gave consent
  - The type of SMS, MMS, or RCS messaging they consented to
  - The users' phone number
  - The language in which they opted-in<br><br>

2. **Clearly communicate the types of SMS, MMS, or RCS you'll be sending**. Users should understand what messages to expect from your brand in this channel and the kinds of information or offers they'll be receiving. Explicitly state the purpose of your future campaigns, message frequency, and remind users that message/data rates apply.<br><br>

3. **Keep essential information updated and visible**. Ensure that the most up-to-date version of your brand's Terms and Conditions and your SMS/MMS/RCS Marketing Privacy Policy are clearly visible and easily accessible from your opt-in page.<br><br>

4. **Only send SMS, MMS, or RCS to legally obtained, opted-in phone numbers**. As part of technical migration planning, ensure that your team understands the mechanism for tying opt-in statuses to each and every user profile in your customer engagement platform.<br><br>

5. **Ensure SHAFT compliance in the US and other relevant regions.** Sending SMS, MMS, or RCS messages that contain language around sex, hate, alcohol, firearms, and tobacco (SHAFT) is generally considered to be illegal in the US and some other regions.<br><br>

6. **Double-check everything**. Work with your legal team to ensure that your SMS, MMS, or RCS program is fully compliant with all applicable rules and regulations for the regions your brand operates in.<br><br>

## RCS compliance best practices

{% alert note %}
RCS is an emerging and evolving space. States, countries, and other regulatory bodies may introduce new or different legislation or regulations. The following information is for general guidance and educational purposes. Brands should always consult with their legal team before sending RCS messages.
{% endalert %}

- **Understand regulatory overlap:** Because RCS and SMS share many similarities, the same laws, regulations, and carrier policies apply. This includes TCPA rules for collecting opt-in and CTIA guidelines (such as SHAFT).
- **Consents:** Work with your legal team to assess whether you need to collect additional consents to send RCS to your existing SMS users.
- **Update policies and disclaimers:** It is recommended to update your Mobile Terms of Service & Privacy Policy to include RCS references. It is also recommended that your opt-in campaigns include language about RCS, in addition to SMS.

## Resources

Here are some links you might need to consult as you build up your SMS, MMS, or RCS campaign:

- [CTIA's Messaging Principles and Best Practices for 2023](https://api.ctia.org/wp-content/uploads/2023/05/230523-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf)
- [Twilio's Guide to US SMS Compliance](https://www.twilio.com/learn/call-and-text-marketing/guide-to-us-sms-compliance)
- [Acoustic's United States SMS compliance and resources](https://help.goacoustic.com/hc/en-us/articles/360043717414-United-States-SMS-compliance-and-resources)

## Considerations for compliance

### Data and privacy

A customer's privacy is key to a meaningful and respectful relationship. Respecting a customer's privacy and information is just another opportunity to create a bond between them and your brand. Sometimes, using marketing tools can put data and privacy last.

Luckily for you, Braze follows the guidelines of many [security regulations]({{site.baseurl}}/developer_guide/disclosures/security_qualifications/#security-qualifications), including [GDPR]({{site.baseurl}}/dp-technical-assistance/).

The [CTIA](https://www.ctia.org/) (a trade association representing the wireless communications industry in the United States) recommends that you maintain and conspicuously display a clear and easy-to-understand privacy policy.

### Consent

Opt-in, help, and opt-out options are an absolute must when creating SMS, MMS, or RCS campaigns.

The Telephone Consumer Protection Act ([TCPA](https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991)) mandates that a business must receive "express written consent" to send customers messages - you can do this in a multitude of ways, including web or mobile. You must be clear with the customer about how you intend to use SMS to communicate with them.

Remember to comply with the [National Do Not Call Registry](https://www.donotcall.gov/).

Braze uses [Subscription Groups]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/) to manage groups of users based on their level of consent.

### Spam and cadence

Similar to email, your users or customers can experience inbox burnout. But this is only one reason not to relentlessly message your customers. You should look specifically at [Section 5 of the FTC Act](https://www.federalreserve.gov/boarddocs/supmanual/cch/ftca.pdf) to ensure compliance (in the U.S.).

Some spam considerations are built into SMS capabilities in general (long and short code sending limits), as well as Braze rate limits. However, you should still consider compliance laws when planning your campaigns.

### Content

This can be a tricky one, but when in doubt, avoid topics that involve violence, sex, drugs, tobacco, or other paraphernalia. Be wise when sending messages regarding these topics—you may still be charged for messages that are blocked by various carriers.

The [CTIA](https://www.ctia.org/) recommends that you ensure SHAFT compliance, which defines the following topics as generally "illegal" when messaging in the United States:

- Sex
- Hate
- Alcohol
- Firearms
- Tobacco

For more on this topic, check out the CTIA's [Messaging Principles and Best Practices for 2019](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf).

### Scheduling

Ensure you comply with the [TCPA](https://en.wikipedia.org/wiki/telephone_consumer_protection_act_of_1991), which dictates that you shouldn't send messages during late hours. Refer to the regulation's contents for exact hours. However, you shouldn't send messages that late anyway—don't you want high engagement?

### International

Most of these best practices apply to guidelines set forth in the United States of America. If you're reaching customers outside of U.S. regions, research best practices and laws in those areas. It's always a best practice to act in a way that adheres to the most stringent regulations, which are usually applied in the United States, Canada, and countries part of the European Union.
