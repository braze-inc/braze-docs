---
nav_title: Customize the URL
article_title: Customize landing page URLs
description: "Learn how to customize your landing page URLs with your company's brand, by connecting your domain to your Braze workspace."
page_order: 1
---

# Customize landing page URLs

> Learn how to customize your landing page URLs with your company's brand, by connecting your domain to your Braze workspace.

## How it works

When you [connect your domain to Braze](#connecting-your-domain-to-braze), it will be used as the default domain for all landing pages. For example, if you connect the subdomain `forms.example.com`, your landing page URLs would now be `forms.example.com/holiday-sale`.

The number of custom domains you can connect to your Braze account depends on your [plan tier]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers). To increase your limit, contact your Braze account manager.

## Connecting your domain to Braze

To connect a domain to your Braze account, have an administrator follow the steps below.

1. Go to **Settings** > **Landing Page Settings**.
2. Enter the domain you want to connect and select **Submit**. For example, `forms.example.com`.
3. Copy and paste the **TXT** and **CNAME** records into the DNS settings of your domain provider.
4. Return to the Braze dashboard to verify the connection.

![Landing Page Settings page with one TXT and two CNAME records listed with their respective names and values.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

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

{% multi_lang_include dns_records.md %}

## Troubleshooting 

### My domain connection failed

Verify that your domain was entered correctly and that it matches what you submitted to Braze from your domain provider account. If it's correct and matches, check the TXT and CNAME records provided by Braze. They should match the records you entered into your domain provider account.

## Frequently asked questions

### Can I connect multiple subdomains to my workspace or connect one subdomain to multiple workspaces?

No, you currently can only connect one subdomain to a workspace.

### Can I use the same subdomain that I currently use for my main website or my sending domain?

No, you can't use subdomains that are already in use. While these subdomains are valid, they can't be used for landing pages if they are already assigned to other purposes or have DNS records that conflict with the required CNAME records.

### Why is my custom domain stuck on "Connecting" despite valid DNS records?

If your custom domain shows all DNS records as "Connected" but the domain status remains on "Connecting" for more than four hours, your organization may be using CAA (Certificate Authority Authorization) records or Cloudflare zone holds that prevent Braze from securing your page.

#### CAA records

CAA records restrict which certificate authorities can issue SSL certificates for your domain. If your CAA records don't include LetsEncrypt, Braze (through Cloudflare) can't issue the required SSL certificate.

To resolve this, ask your IT team to add a CAA record to your subdomain with the following values:
- **Record type:** CAA
- **Value:** `0 issue "letsencrypt.org"`

For more information, refer to [LetsEncrypt's CAA documentation](https://letsencrypt.org/docs/caa/).

#### Cloudflare zone holds

If your organization uses Cloudflare, a zone hold security feature may be preventing Braze from creating your custom domain.

To resolve this, ask your IT team to temporarily release the zone hold. For more information, refer to [Cloudflare's zone hold documentation](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds).

#### Restarting the validation process

After resolving either issue, delete and recreate your custom domain in the Braze dashboard to restart the validation process.

