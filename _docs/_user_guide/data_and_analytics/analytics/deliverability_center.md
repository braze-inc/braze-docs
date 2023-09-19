---
nav_title: Deliverability Center
article_title: Deliverability Center
page_order: 4
description: "This reference article covers how to set up the Deliverability Center, a feature that allows marketers to view their email sending domains and IP reputations and understand their email deliverability."
channel:
  - email

---

# Deliverability Center

> The Deliverability Center provides more insight into your email performance by supporting the use of [Gmail Postmaster Tools][1] to track data on emails sent and gather data about your sending domain.

Email deliverability is the core of campaign success. Using the Deliverability Center in the Braze dashboard, you can view your domains by **IP Reputation** or **Delivery Errors** to discover and troubleshoot any potential issues with email deliverability. 

## Integrating with Google Postmaster

Before setting up your Deliverability Center, check that your domains have been [added to the Gmail Postmaster Tools][4].

Follow these steps to integrate with Google Postmaster and set up your Deliverability Center:

1. Go to **Analytics** > **Email Performance**.
2. Select the **Deliverability Center** tab. <br>![][3]
3. Click **Connect with Google Postmaster**. 
4. Select your Google Account, and click **Allow** to allow Braze to view email traffic metrics for the domains registered with the Postmaster Tools. 

Your verified domains will display in the Deliverability Center. 

![][5]

You can also access Google Postmaster in the Braze dashboard by navigating to **Partner Integrations** > **Technology Partners** > **Google Postmaster**. After integrating, Braze pulls reputation and error data for the last 30 days. The data may not be immediately available and could take several minutes to populate.

## Integrating with Microsoft Smart Network Data Servies (SNDS)

{% alert important %}
Integrating with Microsoft SNDS in the Deliverability Center is currently in early access. Contact your account manager if you're interested in participating in this early access.
{% endalert %}

If Microsoft is your main mailbox provider, you can use this integration to access and view your Microsoft reputation data. This way, you can monitor the health of your IPs to help determine how your emails are being received.

1. Go to **Analytics** > **Email Performance**.
2. Select the **Deliverability Center** tab.
3. Click **Connect with Microsoft SNDS**. 
4. Select your Microsoft account, and click **Allow** to allow Braze to view email traffic metrics for the domains registered.

Your verified domains will display in the Deliverability Center.

![][8]

## Metrics and definitions

### IP reputation 

To help understand the ratings for IP reputation, refer to this table:

| Reputation Rating | Definition |
| ----- | ---------- |
| High | Has a good track record of generating low spam complaints (i.e., users clicking the "spam" button). |
| Medium/Fair | Known to generate positive engagement but occasionally receives spam complaints. Most of the emails from this domain will be sent to the inbox, except when spam complaints increase. |
| Low | Known to receive elevated rates of spam complaints regularly. Emails from this sender will likely be filtered to the spam folder. |
| Bad | Has a history of receiving elevated rates of spam complaints. Emails from this domain will almost always be rejected at connection time or filtered to the spam folder. |
{: .reset-td-br-1 .reset-td-br-2}

### Domain reputation 

Use the following table to help monitor and understand your domain reputation ratings to help avoid being filtered into a spam folder.

| Reputation Rating | Definition |
| ----- | ---------- |
| High | Has a good track record of very low spam complaints. Complies with Gmail’s sender guidelines. Emails are rarely filtered to the spam folder. Has a good track record of a very low spam rate. Complies with [Gmail's sender guidelines][2]. |
| Medium/Fair | Known to generate positive engagement but has occasionally received a low volume of spam complaints. Most of the emails from this domain will reach the inbox (except when there is a notable increase in spam levels). |
| Low | Known to receive spam complaints regularly. Emails from this sender will likely be filtered to the spam folder. |
| Bad | Has a history of receiving elevated rates of spam complaints. Emails from this domain will almost always be rejected at connection time or filtered to the spam folder. |
{: .reset-td-br-1 .reset-td-br-2}

### Authentication

You can use the authentication dashboard to review the percentage of emails that have passed Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), and Domain-based Message Authentication, Reporting and Conformance (DMARC).

| Graph Type | Definition |
| ----- | ---------- |
| SPF | Shows the percentage of emails that passed SPF versus all emails from the domain that attempted SPF. This excludes any spoofed mail. |
| DKIM | Shows the percentage of emails that passed DKIM versus all emails from the domain that attempted DKIM. |
| DMARC | Shows the percentage of emails that passed DMARC alignment versus all emails received from the domain that passed either SPF or DKIM. |
{: .reset-td-br-1 .reset-td-br-2}

### Encryption

Refer to this table to understand what percentage of your inbound and outbound traffic is encrypted.

| Term | Definition |
| ----- | ---------- |
| TLS Inbound | Shows the percentage of incoming mail (to Gmail) that passed TLS versus all mail received from that domain. |
| TLS Outbound | Shows the percentage of outgoing mail (from Gmail) accepted over TLS versus all mail sent to that domain. |
{: .reset-td-br-1 .reset-td-br-2}

For more ideas on improving deliverability, read [Deliverability pitfalls and spam traps][6]. Be sure to reference our [Email best practices][7] for things you should check for before sending an email campaign.

[1]: https://www.gmail.com/postmaster/
[2]: https://developers.google.com/gmail/markup/registering-with-google
[3]: {% image_buster /assets/img_archive/deliverability_center1.png %}
[4]: https://support.google.com/mail/answer/9981691?hl=en
[5]: {% image_buster /assets/img_archive/deliverability_center2.png %}
[6]: {{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[8]: {% image_buster /assets/img_archive/deliverability_center_msnds.png %}