---
nav_title: Customizing the URL
article_title: Customizing landing page URLs
description: "Learn how to customize your landing page URLs with your company's brand, by connecting your domain to your Braze workspace."
page_order: 1
---

# Customizing landing page URLs

> Learn how to customize your landing page URLs with your company's brand, by connecting your domain to your Braze workspace.

## How it works

When you [connect your domain to Braze](#connecting-your-domain-to-braze), it will be used as the default domain for all landing pages. For example, if you connect the subdomain `forms.example.com`, your landing page URLs would now be `forms.example.com/holiday-sale`.

## Connecting your domain to Braze

To connect a domain to your Braze account, have an administrator follow the steps below.

1. Go to **Settings** > **Landing Page Settings**.
2. Enter the domain you want to connect and select **Submit**. For example, `forms.example.com`.
3. Copy and paste the **TXT** and **CNAME** records into the DNS settings of your domain provider.
4. Return to the Braze dashboard to verify the connection.

![Landing Page Settings page with one TXT and two CNAME records listed with their respective names and values.][1]

{% alert note %}
Depending on your domain provider, the connection can take up to 48 hours. When the process is complete, we’ll start using your custom domain for your landing pages in the Braze dashboard.
{% endalert %}

## Removing your domain

If you're a Braze administrator, you can remove a previously-configured domain by completing the following steps:

1. Go to **Settings** > **Landing Page Settings**.
2. Select **Remove Custom Domain**
3. Confirm removal of the domain.
4. Remove the listed DNS records from your domain settings.

{% alert important %}
When you remove a custom domain, that URL will no longer be valid. Any landing pages that were using this domain will automatically revert back to the default domain set by Braze.
{% endalert %}


## DNS resources

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

### Can I use the same subdomain that I currently use for my main website or my sending domain?

No, you can't use subdomains that are already in use. While these subdomains are valid, they can't be used for landing pages if they are already assigned to other purposes or have DNS records that conflict with the required CNAME records.

[1]: {% image_buster /assets/img/landing_pages/connect_subdomain.png %}
