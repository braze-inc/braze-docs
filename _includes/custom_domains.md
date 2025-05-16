# Self-serve custom domains

> This page covers how to use custom domains to portray a consistent brand image. 

Self-serve custom domains empower you to configure and manage your own custom domains for SMS link shortening and other messaging app channels—including SMS, RCS, and WhatsApp—directly from your Braze dashboard. You can easily add, monitor, and manage up to 10 custom domains in one place.

## Benefits of self-serve custom domains

- **Streamlined setup:** Configure your domains on the **Company Settings** page, reducing the time it takes to implement link shortening.
- **Enhanced transparency:** Receive real-time updates on your domain’s setup status through in-app banners and email notifications.
- **Proactive notifications:** Get immediate alerts when your custom domain is connected or if any configuration errors occur.

## Domain requirements

- Domains must be procured, owned, and managed by you.
- The domain used for this feature must be unique (that is, different from your website domain), and the domain can't be used to host any web content.
  - You can also use unique subdomains, such as `sms.braze.com` or `whatsapp.braze.com`.

## Delegating your custom domain

When you delegate your domain to Braze, we automatically handle the certificate renewal to prevent a lapse in service. 

To delegate your domain to Braze, do the following: 

1. In Braze, go to **Company Settings** > **SMS/RCS and Messaging Apps Domains**.
!["SMS/RCS and Messaging Apps Domains" page with several domains listed.][5]{: style="max-width:70%;"}

{: start="2"}
2. Select **Add Domain** to begin a new custom domain setup.
3. Enter your desired custom domain into our in-app input, which uses our existing validation logic for proper formatting, then select **Next** and **Submit**.

!["Add Domain" button on the "SMS/RCS and Messaging Apps Domains" page.][4]{: style="max-width:70%;"}

{: start="4"}
4. Have your technical partners update your DNS configuration with the Cloudflare DNS record details that display. Your DNS records must be updated within seven days. 
  - If you need additional time to update your DNS records, a new set of DNS records can be generated after the seven-day window passes and the old set expires.

!["DNS record" section with 3 steps to complete to finish setting up your domain.][2]

{% alert note %}
Your domain progress is saved automatically. If you need to exit mid-flow, you can resume later by selecting the pending domain entry on the **SMS/RCS and Messaging Apps Domains** page.
{% endalert %}

Braze will poll your DNS configuration roughly every 15—30 minutes to check for updates. If your domain is successfully configured, you'll receive an email indicating that your domain is verified and now connected. 

If configuration errors are detected, an email will outline the issue and provide steps to resolve it. You can also refer to in-app error details or [contact Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/) for assistance.

### Ongoing management and usage

After your domain is verified, your custom domains will appear in the table on the **SMS/RCS and Messaging Apps Domains** page with status indicators. You can immediately use connected domains across multiple subscription groups, workspaces, and channels.

![List of custom domains and statuses.][3]{: style="max-width:50%;"}

Live monitoring will alert you if any of your active domains has an issue, so that your custom links remain usable.

## Using custom domains

After they're configured, custom domains can be assigned to one or multiple WhatsApp and SMS subscription groups. 

![Subscription groups settings that allow you to select a link-shortening domain.][7]

{% if include.channel == 'WhatsApp' %}
Campaigns sent with click tracking turned on or built within WhatsApp template messages will use the assigned domain associated with your subscription groups.

![WhatsApp message composer preview with a shortened link domain that is different from the domain in the "Message" box.][6]
{% endif %}

{% if include.channel == 'SMS' %}
Campaigns sent with link shortening turned on will use the assigned domain associated with your SMS subscription group.

![SMS message composer preview with a shortened link domain that is different from the domain in the "Message" box.][8]
{% endif %}

## Frequently asked questions

### Can delegated domains be shared across multiple subscription groups?

Yes. A single domain can be used with multiple subscription groups. To do so, select the domain for each subscription group that it should be associated with.

### Can delegated domains be shared across multiple workspaces?

Yes. Domains can be associated with subscription groups in multiple workspaces, assuming the workspaces are contained within the same company.

### How many custom domains can I add?

You can add up to 10 custom domains per dashboard.

### What happens if I don’t update my DNS records within seven days?

Though your Cloudflare DNS record details will expire after seven days, you can generate a set of new DNS records to extend your setup window if needed.

### Will I be notified if there is an error during the DNS update process?

Yes. If there’s an error, you’ll receive an email detailing the issue along with steps to resolve it. 

### Can I use a custom domain across multiple channels?

Yes. After a custom domain is verified, it can be used in all SMS, RCS, and WhatsApp subscription groups across all workspaces within a dashboard. 

### What if I have questions or need further support?

For additional help, [contact Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/). 

[2]: {% image_buster /assets/img/dns_record.png %} 
[3]: {% image_buster /assets/img/custom_domain_statuses.png %} 
[4]: {% image_buster /assets/img/custom_domain_button.png %} 
[5]: {% image_buster /assets/img/main_page.png %} 
[6]: {% image_buster /assets/img/custom_domain_whatsapp_composer.png %} 
[7]: {% image_buster /assets/img/custom_domain.png %} 
[8]: {% image_buster /assets/img/custom_domain2.png %}