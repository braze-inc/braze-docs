---
nav_title: Self-Serve Custom Domains
article_title: Self-Serve Custom Domains
page_order: 0
description: "This page covers how to use custom domains with link shortening to personalize the look and feel of your shortened URLs."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Self-serve custom domains

> This page covers how to set up your own custom domains in the Braze dashboard. Custom domains allow you to use a branded shortened link that reflects your brand’s identity instead of a generic shortened link or the Braze domain (`brz.ai`)—improving user trust and campaign engagement with SMS links.

Self-serve custom domains empower you to configure and manage your own custom domains for SMS, RCS, and WhatsApp—directly from your Braze dashboard. You can easily add, monitor, and manage up to 10 custom domains in one place.

## Benefits of self-serve custom domains

- **Streamlined setup:** Configure your domains on the **Company Settings** page, reducing set up time.
- **Enhanced transparency:** Receive real-time updates on your domain’s setup status through banners in the dashboard.
- **Proactive notifications:** Get immediate alerts when your custom domain is connected or if any configuration errors occur.

## Domain requirements

- Domains must be procured, owned, and managed by you. This can be done through a domain registrar, such as GoDaddy, Amazon Route 53, or Google Domains.
- The domain used for this feature must be:
  - Unique (different from your website domain)
  - Can't be used to host any web content
    - You can also use unique subdomains. For example, the domain `braze.com` could have subdomains of `sms.braze.com` or `whatsapp.braze.com`.

## Delegating your custom domain

We require you to delegate your custom domain to Braze so that we can faciliate proper routing and infrastructure compatibility with our link shortening and click tracking services. When you delegate your domain to Braze, we automatically handle the certificate renewal to prevent a lapse in service. 

## Adding a custom domain

1. In Braze, go to **Company Settings** > **SMS/RCS and Messaging Apps Domains**.
!["SMS/RCS and Messaging Apps Domains" page with several domains listed.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2. Select **Add Domain** to begin a new custom domain setup.
3. Enter the custom domain you've purchased into our in-app input, which uses our existing validation logic for proper formatting, then select **Next** and **Submit**.

!["Add Domain" button on the "SMS/RCS and Messaging Apps Domains" page.]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4. Have your technical team (such as engineering or IT) update your DNS configuration with the Cloudflare DNS record details that display. Your technical team must update your DNS records with these details within 45 days.
  - If you need additional time to update your DNS records, you can restart the process and generate a new set of DNS records for your domain.

Braze will poll your DNS configuration roughly every 30 minutes to check for updates.

!["DNS record" section with 3 steps to complete to finish setting up your domain.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
Your domain progress is saved automatically. If you need to exit mid-flow, you can resume later by selecting the pending domain entry on the **SMS/RCS and Messaging Apps Domains** page.
{% endalert %}

### Ongoing management and usage

After your domain is verified, your custom domains will appear in the table on the **SMS/RCS and Messaging Apps Domains** page with status indicators. You can immediately use connected domains across multiple subscription groups, workspaces, and across SMS, RCS, and WhatsApp channels.

![List of custom domains and statuses.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

Live monitoring will alert you in the Braze dashboard if any of your active domains have an issue, so that your custom links remain usable. If you encounter any issues, refer to the in-app error details or contact Braze [Support]({{site.baseurl}}/braze_support/) for assistance.

## Using custom domains

After they're configured, custom domains can be assigned to one or multiple SMS, RCS, and WhatsApp subscription groups.

![Subscription groups settings that allow you to select a link-shortening domain.]({% image_buster /assets/img/custom_domain.png %})

Campaigns sent with link shortening turned on will use the assigned domain associated with your SMS, RCS, or WhatsApp subscription group.

![SMS message composer preview with a shortened link domain that is different from the domain in the "Message" box.]({% image_buster /assets/img/custom_domain2.png %})

## Frequently asked questions

### Can delegated domains be shared across multiple subscription groups?

Yes. A single domain can be used with multiple subscription groups. To do so, select the domain for each subscription group that it should be associated with.

### Can delegated domains be shared across multiple workspaces?

Yes. Domains can be associated with subscription groups in multiple workspaces, assuming the workspaces are contained within the same company.

### How many custom domains can I add?

You can add up to 10 custom domains per dashboard.

### What happens if I don’t update my DNS records within 45 days?

Though your Cloudflare DNS record details will expire after 45 days, you can restart the setup process with the same domain and Braze will generate a set of new DNS records to extend your setup window.

### Will I be notified if there is an error during the DNS update process?

Yes. If there’s an error, you’ll receive a banner in the Braze dashboard detailing the issue along with steps to resolve it. 

### Can I use a custom domain across multiple channels?

Yes. After a custom domain is verified, it can be used in all SMS, RCS, and WhatsApp subscription groups across all workspaces within a dashboard. 

### What if I have questions or need further support?

For more detailed guidance on setting up and managing custom domains, including troubleshooting steps and technical requirements, [contact Support]({{site.baseurl}}/braze_support/).