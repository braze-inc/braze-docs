---
nav_title: Consent & address collection
article_title: Consent & Address Collection
page_order: 6
page_type: reference
description: "This reference article covers best practices for gathering consent and user email addresses and defines the different possible user subscriber states."
channel: email

---

# Consent and address collection

> Before sending out your initial emails, it's important to get permission from your customers first. It's a common courtesy and does wonders for your open rates!

## Subscriber states

There are three email subscription states for a user: **opted in**, **subscribed**, and **unsubscribed**. To change a user's subscription state, check out our article on [changing subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-subscriptions) or use our [Subscription APIs]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

| Subscriber State | Description |
|---|---|
| Opted In | These customers have clicked on the link in a confirmation email and actively opted in to receiving your messages. |
| Subscribed | By default, users are subscribed to email as long as they have a valid email address stored on their profile. users remain subscribed until they unsubscribe or opt-in. |
| Unsubscribed | To be marked as unsubscribed, a customer has either explicitly unsubscribed from your emails or has marked an email as spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Address collection methods

In addition to getting permission from your users prior to messaging, there are several methods for collecting these email addresses that can impact your deliverability. 

### Purchased address lists

Sending emails to purchased or rented lists is in violation of your Braze contract! If you're purchasing emails, you're sending totally unsolicited messages and are putting yourself at risk for deliverability issues.

### Co-registration

Co-registration refers to an arrangement between companies to collect user information. This is a risky method of collection. It opts users into receiving emails from third parties, sometimes without the customer's knowledge or permission. If you go this route, be sure to have clear disclosures and the ability to unsubscribe at the point of collection.

### Pre-selected or forced opt-in

Pre-selected opt-in is an email registration method in which the email sign-up box is already checked for subscribers to receive your email. By leaving the box checked, subscribers are opting in and giving their consent to receive your email. This method has a tendency to annoy people (it's also illegal for mail sent into or within Canada). You may end up with a decent-sized email list, but you really can't be sure that these users want your marketing emails.

### Single opt-in

Single opt-in happens when subscribers sign up via a subscription form and are immediately added to your email list. With this method, users take a single step to subscribe, like typing in their email address in a collection field or selecting a box as part of a transaction.

### Confirmed opt-in

A confirmed opt-in occurs when a user checks a box asking for email communication, and a confirmation message is sent in return. This method allows users to choose the type and frequency of the content improves engagement. 

To confirm that you're targeting only the most engaged users, you could also use the double confirmed opt-in method. This approach adds an extra step in which the user must click a button or link in the confirmation email to be placed in the email list. 
