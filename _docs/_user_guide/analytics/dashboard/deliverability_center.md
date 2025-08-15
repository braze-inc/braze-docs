---
nav_title: Deliverability Center
article_title: Deliverability Center
page_order: 4
description: "This reference article covers how to set up the Deliverability Center, a feature that allows marketers to view their email sending domains and IP reputations and understand their email deliverability."
channel:
  - email

---

# Deliverability Center

> The Deliverability Center provides more insight into your email performance by supporting the use of [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) to track data on emails sent and gather data about your sending domain.

Email deliverability is the core of campaign success. Using the Deliverability Center in the Braze dashboard, you can view your domains by **IP Reputation** or **Delivery Errors** to discover and troubleshoot any potential issues with email deliverability. 

To access the Deliverability Center, you'll need "Access Campaigns, Canvases, Cards, Segments, Media Library" and "View Usage Data" [user permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).

## Setting up your Google Postmaster account

Before connecting to the Deliverability Center, you'll need to set up a Google Postmaster Tools account. You can use a work or personal Gmail account to setup your Google Postmaster. 

1. Go to the [Google Postmaster Tools dashboard](https://postmaster.google.com/managedomains?pli=1).
2. In the bottom right, select the <i class="fas fa-plus-circle"></i> plus icon.
3. Enter your root domain or subdomain to authenticate your email. If you're adding and verifying the root domain, this will allow the verification to be applied downstream to subdomains. For example, by verifying `braze.com`, you can later add `demo.braze.com` and other subdomains without having to verify these individually.
4. Google will generate a TXT record that can be added directly to your domain's DNS. This is generally owned by whoever manages your DNS. For information and guidance on how to update your specific DNS, check out [Verify your domain (host-specific steps)](https://support.google.com/a/topic/1409901).
5. Select **Next**. <br>![An example domain "demo.braze.com" to authenticate an email.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. After the TXT record is added to the DNS, return to the Google Postmaster Tools dashboard and select **Verify**. This step confirms you own the domain, so you'll be able to access Gmail deliverability metrics in your Postmaster account. <br> ![A prompt to verify ownership of the domain "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert tip %}
Be sure the TXT record is tied at the parent domain, not the subdomain you're using through Braze.
{% endalert %}

{% alert note %}
If your subdomains aren't included in the Deliverability Center for Google Postmaster, this can be a result of only adding the parent domain to Google Postmaster. After the parent domains are verified in Google Postmaster, you can add your subdomains, which will be verified automatically. This process allows Google to report back on metrics on the subdomain-level, which can then be pulled into the Braze Deliverability Center.
{% endalert %}

## Integrating Google Postmaster

Before setting up your Deliverability Center, check that your domains have been [added to the Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en).

Follow these steps to integrate with Google Postmaster and set up your Deliverability Center:

1. Go to **Analytics** > **Email Performance**.
2. Select the **Deliverability Center** tab. <br>![A Deliverability Center with Google Postmaster unconnected.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Select **Connect with Google Postmaster**. 
4. Select your Google Account and then select **Allow** to allow Braze to view email traffic metrics for the domains registered with the Postmaster Tools. 

Your verified domains will display in the Deliverability Center. 

![Two verified domains for Google Postmaster with a medium and low reputation.]({% image_buster /assets/img_archive/deliverability_center2.png %})

You can also access Google Postmaster in the Braze dashboard by going to **Partner Integrations** > **Technology Partners** > **Google Postmaster**. After integrating, Braze pulls reputation and error data for the last 30 days. The data may not be immediately available and could take several minutes to populate.

### Metrics and definitions

The following metrics and definitions apply to Google Postmaster Tools.

#### IP reputation 

To help understand the ratings for IP reputation, refer to this table:

| Reputation Rating | Definition |
| ----- | ---------- |
| High | Has a good track record of generating low spam complaints (such as users clicking the "spam" button). |
| Medium/Fair | Known to generate positive engagement but occasionally receives spam complaints. Most of the emails from this domain will be sent to the inbox, except when spam complaints increase. |
| Low | Known to receive elevated rates of spam complaints regularly. Emails from this sender will likely be filtered to the spam folder. |
| Bad | Has a history of receiving elevated rates of spam complaints. Emails from this domain will almost always be rejected at connection time or filtered to the spam folder. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Domain reputation 

Use the following table to help monitor and understand your domain reputation ratings to help avoid being filtered into a spam folder.

| Reputation Rating | Definition |
| ----- | ---------- |
| High | Has a good track record of very low spam complaints. Complies with Gmail’s sender guidelines. Emails are rarely filtered to the spam folder. Has a good track record of a very low spam rate. Complies with [Gmail's sender guidelines](https://developers.google.com/gmail/markup/registering-with-google). |
| Medium/Fair | Known to generate positive engagement but has occasionally received a low volume of spam complaints. Most of the emails from this domain will reach the inbox (except when there is a notable increase in spam levels). |
| Low | Known to receive spam complaints regularly. Emails from this sender will likely be filtered to the spam folder. |
| Bad | Has a history of receiving elevated rates of spam complaints. Emails from this domain will almost always be rejected at connection time or filtered to the spam folder. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Authentication

Use the authentication dashboard to review the percentage of emails that have passed Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), and Domain-based Message Authentication, Reporting and Conformance (DMARC).

| Graph Type | Definition |
| ----- | ---------- |
| SPF | Shows the percentage of emails that passed SPF versus all emails from the domain that attempted SPF. This excludes any spoofed mail. |
| DKIM | Shows the percentage of emails that passed DKIM versus all emails from the domain that attempted DKIM. |
| DMARC | Shows the percentage of emails that passed DMARC alignment versus all emails received from the domain that passed either SPF or DKIM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Encryption

Refer to this table to understand what percentage of your inbound and outbound traffic is encrypted.

| Term | Definition |
| ----- | ---------- |
| TLS Inbound | Shows the percentage of incoming mail (to Gmail) that passed TLS versus all mail received from that domain. |
| TLS Outbound | Shows the percentage of outgoing mail (from Gmail) accepted over TLS versus all mail sent to that domain. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more ideas on improving deliverability, read [Deliverability pitfalls and spam traps]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). Be sure to reference our [Email best practices]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) for things you should check for before sending an email campaign.

## Setting up Microsoft Smart Network Data Services (SNDS)

If Microsoft is your main mailbox provider, you can use this integration to access and view your Microsoft reputation data. This way, you can monitor the health of your IPs to help determine how your emails are being received.

{% alert important %}
If you don't see your data in the Deliverability Center, contact [Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/) with a list of your IP addresses.
{% endalert %}

![An example of results from Microsoft SNDS, including sample IPs, recipients, RCPT commands, data commands, filter result, complaint rate, trap message period start and end, and spam trap hits.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Metrics and definitions

The following metrics apply to Microsoft SNDS.

#### Recipients

This metric refers to the number of recipients on messages transmitted by the IP.

#### DATA commands

This metric tracks the number of DATA commands sent by the IP. DATA commands are part of the SMTP protocol used to send mail.

#### Filter results

Refer to this table to understand the filter results 

| Result | Definition |
| ----- | ---------- |
| Green | Judged to be spam by Microsoft’s spam filter up to 10% of the given time frame. |
| Yellow | Judged to be spam by Microsoft’s spam filter between 10% and 90% of the given time frame. |
| Red | Judged to be spam by Microsoft’s spam filter up to more than 90% of the given time frame.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Complaint rate

This is the fraction of the time that a message received from the IP is complained about by a Hotmail or Windows Live user during the activity period. Users have the option of reporting almost all messages as junk via the web user interface. 

To calculate the complaint rate, divide the number of complaints by the number of message recipients.  

| Result | Definition |
| ----- | ---------- |
| Less than 0.3% | The ideal complaint rate. |
| More than 0.3% | Review your sign-up process, and ensure your unsubscribe link is working. Also, consider whether mail could be better personalized to your audience. |
| More than 100% | Note that SNDS displays complaints for the day they were reported, not retroactively against the day the complained-about mail was delivered. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Spam trap hits

Spam trap hits are the number of messages sent to "trap accounts," which are accounts maintained by Outlook.com that don't solicit any mail. It's likely that any messages sent to these trap accounts are considered spam, so it's important to monitor this metric to make sure that it's low. Low spam trap hits means the messages aren't sent to these accounts and are being sent to actual accounts instead.

{% alert tip %}
If you're looking for records related to one of your verified domains in Braze, note the Deliverability Center lists your data from Google Postmaster or Microsoft SNDS, meaning it's likely that either platform doesn't have any data to share with Braze. Alternatively, we suggest maintaining consistent email delivery as this can lead to a higher reputation. 
{% endalert %}


