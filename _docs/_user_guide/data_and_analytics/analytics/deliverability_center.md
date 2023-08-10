---
nav_title: Deliverability Center
article_title: Deliverability Center
page_order: 4
description: "This reference article covers how to set up the Deliverability Center, a feature that allows marketers to view their email sending domains and IP reputations, and understand their email deliverability."
channel:
  - email

---

# Deliverability Center

> The Deliverability Center provides more insight for your email performance by supporting the use [Gmail Postmaster Tools][1] to track data on emails sent and gather data about your sending domain.

Email deliverability is at the core when it comes to measuring the success of a messaging campaign. Using the Deliverability Center in the Braze dashboard, you can view your domains by **IP Reputation** or **Delivery Errors** to discover and troubleshoot any potential issues with email deliverability. 

{% alert important %}
The Deliverability Center is currently in early access. Contact your Braze customer success manager if you're interested in participating in the early access.
{% endalert %}

## Integrate with Google Postmaster

Before setting up your Deliverability Center, check that your domains have been [added to the Gmail Postmaster Tools][4].

Follow these steps to integrate with Google Postmaster and set up your Deliverability Center:

1. Go to the **Analytics** > **Email Performance**.
2. Select the **Deliverability Center** tab. <br>![][3]
3. Click **Connect with Google Postmaster**. Select your Google Account, and click the **Allow** button to allow Braze to view email traffic metrics for the domains registered with the Postmaster Tools.
4. Your verified domains will display in the Deliverability Center. <br>![][5]

You can also access Google Postmaster in the Braze dashboard by navigating to **Partner Integrations** > **Technology Partners** > **Google Postmaster**. After integrating, Braze pulls reputation and error data for the last 30 days. The data may not be immediately available and could take several minutes to populate.

#### IP reputation

To help understand the ratings for IP reputation, refer to this table:

| Reputation Level | Definition |
| ----- | ---------- |
| High | Has a good track record of a very low spam rate. Complies with [Gmail's sender guidelines][2]. Emails are rarely marked by the spam filter. |
| Medium/Fair | Known to send good emails, but has occassionally sent a low volume of spam. Most of the emails from this domain will have a fair deliverability rate (except when there is a notable increase in spam levels). |
| Low | Known to send a considerable volume of spam regularly. Emails from this sender will likely be marked as spam. |
| Bad | Has a history of sending a high volume of spam. Emails coming from this domain will almost always be rejected at connection time or marked as spam. |
{: .reset-td-br-1 .reset-td-br-2}

#### Domain reputation

Use the following table to help monitor and understand your domain reputation levels to help avoid being filtered into a spam folder.

| Reputation Level | Definition |
| ----- | ---------- |
| High | Has a good track record of a very low spam rate. Complies with [Gmail's sender guidelines][2]. Emails are rarely marked by the spam filter. |
| Medium/Fair | Known to send good emails, but has occassionally sent a low volume of spam. Most of the emails from this domain will have a fair deliverability rate (except when there is a notable increase in spam levels). |
| Low | Known to send a considerable volume of spam regularly. Emails from this sender will likely be marked as spam. |
| Bad | Has a history of sendiing a high volume of spam. Emails from this domain will almost always be rejected at connection time or marked as spam. |
{: .reset-td-br-1 .reset-td-br-2}

For more ideas on improving deliverability, read [Deliverability pitfalls and spam traps][6]. Be sure to also reference our [Email best practices][7] for things you should check for before sending an email campaign.

[1]: https://www.gmail.com/postmaster/
[2]: https://developers.google.com/gmail/markup/registering-with-google
[3]: {% image_buster /assets/img_archive/deliverability_center1.png %}
[4]: https://support.google.com/mail/answer/9981691?hl=en
[5]: {% image_buster /assets/img_archive/deliverability_center2.png %}
[6]: {{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
