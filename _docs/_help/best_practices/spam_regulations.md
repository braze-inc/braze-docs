---
nav_title: Spam Regulations
page_order: 4

page_type: reference
description: "This article provides summaries and resources on various spam regulations that may affect you or your users."
channel:
- email
- push
- SMS
no_index: true
---
# Spam Regulations

There are a number of laws that regulate senders of electronic communications, including email, push notifications and SMS. You should always be aware of [local regulations][4] that may affect you or your users. Braze is providing relevant information based on our own research, but you should also refer to the full text of these laws for complete and up-to-date details.

- [CAN-SPAM][1]
- [Canadian Anti-Spam Law][2]

## CAN-SPAM

The CAN-SPAM Act of 2003 regulates email senders in the U.S. sending "any electronic mail message, the primary purpose of which is the commercial advertisement or promotion of a commercial product or service." You can read more details on the [FTC site][5].

There are 7 key requirements for CAN-SPAM:

1. Don’t use false or misleading header information (ie, "From", "To" and "Reply-To")
2. Don’t use deceptive subject lines
3. Identify the message as an ad
4. Tell recipients where you’re located (ie, physical address)
5. Tell recipients how to opt out of receiving future email from you
6. Honor opt-out requests promptly
7. Monitor what others are doing on your behalf

Transactional emails are exempt from these rules with the exception of #1.

## Canadian Anti-Spam Law (CASL) {#casl}

On July 1, 2014, the Canadian Anti-Spam Law (CASL) goes into effect for emails sent to Canadian residents. You can read the full text of the law [here][3]. The law essentially says that Canadian recipients of both email and push notifications need to provide "expressed or implied" consent to your communication with them.

### CASL vs CAN-SPAM

There are a couple key differences between CASL and CAN-SPAM, most notably:

- CASL applies to *where* the message is received, so senders outside of Canada are affected
- Message recipients must up opt-in, instead of opt-out

### Liability

While CASL has a three-year transition period, ending July 1, 2017, the Canadian Radio-Television and Telecommunications Commission (CRTC), the Competition Bureau and the Office of the Privacy Commissioner of Canada may begin investigation and litigation during this period. At the end of the transition period, individuals may also litigate against entities they believe to be sending spam.

### Exempt Messages

The following types of messages are exempt from the requirements of CASL:

- Messages opened outside of Canada
- Messages to family members or other personal relations
- Messages to individuals associated with your business, including employees or contractors
- Messages providing warranty information, product recall information or safety or security information about a product or service the recipient has used or purchased
- Messages providing notification of factual information about subscription, membership or account
- Messages delivering a product or service, including product updates or upgrades

>  This is not the complete list of exemptions. Please view the [full text of the law][3] for more details.

### Message Consent

Messages that do not fall under one of the exemptions require "expressed or implied" consent from the message recipient.

#### Implied Consent

Implied consent is based on previous activity with a user through an existing business or non-business relationship. Messages can be sent based on implied consent during the transition period. After July 1, 2017, express consent is required, unless the implied consent is still valid (ie, the 2 years after a purchase was made).

- The recipient of a message has purchased or leased a product, good, service or completed other business with your organization in the last 2 years
- The electronic address has been published and does not explicitly forbid unsolicited emails

Implied consent is only valid for 6 months if the recipient does not become a customer.

#### Express Consent

Express consent is written or oral confirmation from the message recipient and only valid if the message includes a clear and simple description of:

- Why consent is being sought
- The person or organization seeking consent

## Spam Filters

Just because your emails have successfully sent doesn’t mean that they have necessarily been seen. There is no cure-all solution to avoid all spam filters because each filter is unique in how they evaluate the “spamminess score” of an email. However, here are some tips to avoid having your emails labeled as “spam”:

- Get Permission: A double opt-in process consists of sending a follow up email with a confirmation link after an initial opt-in. Using this provides validation that recipients want to receive your content. You can also take this even one step further by asking users to add you to their address book. Also be sure to grow your email lists organically: purchased lists often tend to be stale!

- Build Your Reputation: Make sure you set expectations when people are signing up to receive your emails. Be explicit about what you will send and how often you will send it. Then, encourage users to interact with your email campaigns by providing valuable content. Having personalized and relevant content decreases the probability of your recipients marking the messages as spam.

- Maintain Your Reputation: Be in constant contact with your users to prevent your email lists from becoming stale. Waiting too long to send a message may cause the recipient to forget about you and mark you as spam. Keep your email lists up to date by implementing a sunset policy to remove email addresses that bounce. Bounce rates are a key factor used by ISPs to evaluate a sender’s reputation.

- Check and Test: Make sure your message does not contain anything that can trigger spam filters. This includes superfluous tags from external text editors like Microsoft Word, abnormal text formatting, over-usage of ! and ? as punctuation, writing in ALL CAPS, and spam trigger words (see [here][7] for a list of common trigger words). Send emails with varying content using Braze’s multivariate testing capabilities to make sure your emails are not going to spam.


## Messaging Channel

### Email {#spam-email}

The quality of your email list is especially important.  A handful of bad emails on your list can ruin your delivery for a million good users. Collecting a list of bad emails generates bounces, blacklisting, spam trap hits, and tanks your response rates. Culling emails that have no activity on a regular basis, and removing obvious bounces are the first step. Whether you implement a opt-in (check the box), opt-out (uncheck the box), confirm opt-in (an email that says thanks for signing up, and gives an unsubscribe link), or double opt-in (an email that that requires a click to confirm), what you want to think about is list quality.

### iOS and Windows {#spam-ios-windows}

In iOS, your users have always been asked to opt-in to push notifications. The iOS dialog boxed simply pops up on entry to the app and asks the user to opt-in for notifications to your app. The app user sees the same message pop-up the moment they open an app for the first time, so everyone who is on your iOS list for push notifications has, by definition, opted-in. Windows also requires explicit opt-ins by the user.

### Android {#spam-android}

In Android, your users can assume to be opted-in by the implied opt-in that is stated in your privacy policy or end user license agreement. You may want to implement an expressed opt-in process perhaps in an initial screen just as the user starts the app for the first time. Visit the [Push Best Practices][6] article for more details. You can also orient the user as to what types of push notifications they will receive, thereby increasing the opt-in rate.

[1]: #can-spam
[2]: #casl
[3]: http://laws-lois.justice.gc.ca/eng/annualstatutes/2010_23/FullText.html
[4]: https://en.wikipedia.org/wiki/Email_spam_legislation_by_country
[5]: http://www.business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business
[6]: {{site.baseurl}}/help/best_practices/push/#creating-custom-opt-in-prompts
[7]: http://blog.hubspot.com/blog/tabid/6307/bid/30684/The-Ultimate-List-of-Email-SPAM-Trigger-Words.aspx#sm.00001wbela64xddnmppa99vp1xa8j
