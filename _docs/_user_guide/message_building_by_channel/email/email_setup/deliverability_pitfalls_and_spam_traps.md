---
nav_title: Deliverability pitfalls & spam traps
article_title: Deliverability Pitfalls & Spam Traps
page_order: 7
page_type: reference
description: "This reference article covers potential email deliverability pitfalls, spam traps, and how to avoid them."
channel: email

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}Deliverability pitfalls and spam traps

Your email deliverability can be affected by any of the following spam traps:

| Trap Type | Description |
|---|---|
| Pristine Traps | Email addresses and domains that have never been used. |
| Recycled Traps | Email addresses that were originally real users, but are now dormant. |
| Typo Traps | Email addresses containing common typos. |
| Spam Complaints | When your email is marked as spam by a customer. |
| High Bounce Rate | When your email consistently fails to deliver because the recipient's address is invalid. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## How to avoid spam traps

These traps can be avoided if you set up a confirmed opt-in process. By sending an initial opt-in email and asking customers to verify that they want your messages, you're ensuring your recipients want to hear from you, and that you're sending to real, valid addresses. Here are additional ways to avoid spam traps:

1. Send a double opt-in email. This is an email that will require users to confirm their subscription choices by clicking a link.
2. As a best practice, implement a [sunset policy]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).
3. **Never purchase email lists.** 

{% alert tip %}
The Braze Customer Success and Deliverability teams can help make sure you're following best practices to maximize deliverability across the globe.
{% endalert %}

## Improving deliverability

> A mailbox provider (MBP) will consider the reputation of a sending domain when determining whether a message is accepted or bounced. However, in some cases the email may be accepted by the MBP, but it will not be delivered to the user's inbox. In these instances, the message may be diverted to a spam folder where a user is unlikely to view it. This article outlines some high-level guidance that should enable you to send messages with the optimal chance of reaching your users' inboxes.

### Sending patterns

Refer to the following best practices to decrease the possibility of your messages being bounced:

- Collect good subscriber data and valid addresses.
- Consider using confirmed opt-in or a data validation service to vet or validate addresses before sending to them. Note that opt-in must be voluntary and the process and language should ensure that subscribers clearly understand that they're opting in to receive mail.
- Optimize the opt-in process to be more user friendly, informative, and fraud-proof.
- Set clear expectations with subscribers so that they understand exactly what they are going to receive and how often. Stick with those expectations rather than sending mail for products or services that the subscriber didn't sign up for or sending more often than was promised.
- Send mail that subscribers want to open and interact with. Consider the value of each campaign. Seek to fulfill and meet subscriber needs rather than the brand's needs.
- If possible, limit sending to just those subscribers who are most likely to positively interact with the mail being sent. Typically those who have most recently opted in and opened, clicked, or interacted with mail or the brand, like website visitors. Do not send to subscribers who have not been responsive to repeated emails and those with which the brand has not interacted for months.
- Many ISPs are particularly sensitive about getting transactional mail delivered to the inbox. They suggest that senders make it easy to identify transactional and marketing messages by sending them from separate IPs and domains. Gmail's guidance suggests that sending different mail streams from different from addresses can be enough separation. Separating marketing mail from transactional mail can help achieve inbox placement for transactional mail and sometimes for commercial mail as well.

### Message content

The MBP will use automated tools to assess the message content. The aim of the MBP is to protect the experience of their users. Consider the following questions as you're composing your messages:

- Does your message unintentionally look like it might be harmful?
- Where are images hosted?
- What's a subscriber's motivation for opening the same email received from the brand previously?

### Recipient reports and behaviours

MBPs will act quickly on user reports. Consider that the MBP has access to a huge amount of aggregated behavioural data from their users. Are users deleting your messages without even opening them? If so, this could be a symptom of spam.

- If many users flag a message as spam, the MBP might divert your future emails. The spam folder can be seen as a quarantined location where the users or the MBP is unconvinced of the quality of the message.
- Send relevant, compelling mail with good subject lines and good calls-to-action. Subscribers decide before they open mail, based solely on from address and subject line, whether they're going to open the message, delete it, or mark it as spam.
- Ask subscribers to look for the brand's email in the spam folder (if that is where it is being delivered) and to mark that mail as "not spam." You can use other channels to make this request, such as in-app messages or push notifications.
- Consider asking subscribers to add the brand's from address to their email software or app contacts list.
- Google's Postmaster team has recommended that senders ask subscribers to mark the brand's messages as "important" to help ensure that they get delivered to the inbox consistently.
- If mail isn't being delivered to the inbox, it's often because of subscriber feedback.

## How to resolve a freemail block for Microsoft

It is very rare for Microsoft to unblock a sender who is having trouble delivering to the free mail domains (Hotmail, Live, MSN, Outlook). Instead, we recommend that senders aggressively reduce their volumes to those domains and send only to recently engaged contacts, or even stop sending to those domains altogether if they're unable to identify a core group of engaged recipients.

An example freemail block message is: `550 5.7.1 Unfortunately, messages from [xx.xx.xx.xx] weren't sent. Please contact your Internet service provider since part of their network is on our block list (S3150). You can also refer your provider to: http://mail.live.com/mail/troubleshooting.aspx#errors.`

By targeting only engaged recipients, Microsoft will receive signals of positive engagement that indicate the sender's mail is wanted and expected by recipients.

You can slowly add more volume similar to during the initial warming period, paying close attention to metrics. There's often a root cause of the deliverability issues to identify and resolve. Generally, this is a lack of proper permission having been obtained, a lack of ongoing list hygiene, or a combination of those factors.

## Removing an email address from your bounce or spam list

You can remove bounced emails and emails on your Braze spam list with the following endpoints:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)