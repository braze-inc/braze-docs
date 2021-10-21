---
nav_title: Consent & Address Collection
article_title: Consent & Address Collection
page_order: 2
page_type: reference
description: "This reference article covers best practices for gathering consent and user email addresses and defines the different possible user subscriber states."
channel: email

---

# Consent & address collection

## Consent
before sending out your initial emails, it's important to get permission from your customers first. it's a common courtesy and does wonders for your open rates!

### Subscriber states
There are three email subscription states for a user: __opted in__, __subscribed__, and __unsubscribed__. To change a user's subscription state, in addition to using the methods described above, you can use our [REST APIs]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

|Subscriber State | Description |
|---|---|
|Opted In| These customers have clicked on the link in a confirmation email and actively opted in to receiving your messages.|
|Subscribed | By default, your customers are subscribed to email as long as they have a valid email address stored on their profile. Customers remain subscribed until they unsubscribe or opt in.|
|Unsubscribed|To be marked as unsubscribed, a customer has either explicitly unsubscribed from your emails or has marked an email as spam.|
{: .reset-td-br-1 .reset-td-br-2}

## Address collection methods

| Method | Description |
|---|---|
|Purchased Address List| Sending emails to purchased or rented lists is in violation of your Braze contract! If you're purchasing emails, you're sending totally unsolicited messages and are putting yourself at risk for deliverability issues.|
|Co-Registration | Co-registration refers to an arrangement between companies to collect user information.<br><br>This is a risky method of collection. It opts users into receiving emails from third parties, sometimes without the customer's knowledge or permission. If you go this route, be sure to have clear disclosures and the ability to unsubscribe at the point of collection. |
|Pre-Selected / Forced Opt-In| Pre-selected opt-in is an email registration method in which the email sign-up box is already checked for subscribers to receive your email. By leaving the box checked, subscribers are opting in and giving their consent to receive your email.<br><br>This method has a tendency to annoy people (it's also illegal for mail sent into or within Canada). You may end up with a decent-sized email list, but you really can't be sure that these users want your marketing emails.|
|Single Opt-In| Single opt-in happens when subscribers sign up via a subscription form and are immediately added to your email list. <br><br>With this method, users take a single step to subscribe, like typing in their email address in a collection field or selecting a box as part of a transaction.|
|Confirmed Opt-In |A confirmed opt-in happens when a user checks a box asking for email communication, and a confirmation message is sent in return. <br><br>This method allows users to choose the type and frequency of the content improves engagement. To ensure you're targeting only the most engaged users, you could also go the route of double confirmed opt-in. This approach adds an extra step in which the user must click a button/link in the confirmation email to be placed in the list. |
{: .reset-td-br-1 .reset-td-br-2}