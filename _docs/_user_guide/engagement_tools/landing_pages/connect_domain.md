---
nav_title: Connecting Your Domain
article_title: Connecting Your Domain
description: "This article covers how to connect your own custom domain to Braze landing pages."
page_order: 1
alias: /landing_pages/connect_domain/
---

# Connecting your domain

> Connect your own domain to your Braze workspace to customize your landing page URLs with your brand.

To connect a domain or subdomain to your Braze account, have an administrator follow the steps below.

1. Go to **Settings** > **Landing Page Settings**.
2. Enter the domain or subdomain you want to connect and select **Submit**. For example, `forms.example.com`.
3. Copy and paste the **TXT** and **CNAME** records into the DNS settings of your domain provider.
4. Return to the Braze dashboard to verify the connection.

![Landing Page Settings page with one TXT and two CNAME records listed with their respective names and values.][1]

{% alert note %}
Depending on your domain provider, the connection can take up to 48 hours. When the process is complete, we’ll start using your custom domain for your landing pages in the Braze dashboard.
{% endalert %}

## Using your domain in Braze

After your domain verification is completed, it will be used by default in Braze. For example, if you connect the subdomain `forms.example.com`, your landing page URLs will be updated to look like `forms.example.com/holiday-sale`.

{% alert note %}
Custom domain deletion is coming soon. Contact your customer success manager if you need to remove your subdomain.
{% endalert %}

## Resources from domain providers

Listed below are resources for creating and managing DNS records with commonly used domain providers. If you're using a different provider, refer to that provider's documentation or contact their support team for information.

| Domain provider | Resources |
| --- | --- |
| Bluehost | [DNS Records Explained](https://my.bluehost.com/hosting/help/508)<br> [DNS Management Add Edit or Delete DNS Entries](https://my.bluehost.com/hosting/help/559) |
| Dreamhost | [How do I add custom DNS records?](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| GoDaddy | [Add a CNAME record](https://www.godaddy.com/help/add-a-cname-record-19236?) |
| Cloudflare | [Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Squarespace | [Adding custom DNS settings](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Troubleshooting 

### My domain connection failed

Verify that your domain was entered correctly and that it matches what you submitted to Braze from your domain provider account. If it's correct and matches, check the TXT and CNAME records provided by Braze. They should match the records you entered into your domain provider account.

## Frequently asked questions

### Can I connect multiple subdomains to my workspace or connect one subdomain to multiple workspaces?

No, you currently can only connect one subdomain to a workspace.

[1]: {% image_buster /assets/img/landing_pages/connect_subdomain.png %}
