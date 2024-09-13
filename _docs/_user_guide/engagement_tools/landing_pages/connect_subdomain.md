---
nav_title: Connecting a Subdomain
article_title: Connecting a Subdomain
description: "This article covers how to connect your third-party domain's subdomains to your Braze account."
page_order: 1
alias: /landing_pages/connect_subdomain/
---

# Connecting a subdomain

> If you own a domain through a third-party service, you can connect its subdomains to your Braze account. You can then use subdomains with your Braze-hosted landing pages to brand and customize your URLs. 

{% alert note %}
Landing pages are currently in beta. Contact your Braze account manager if you’re interested in participating in this beta.
{% endalert %}

To connect a subdomain to your Braze account, have an administrator follow the steps below.

1. Go to **Settings** > **Landing Page Settings**.
2. Enter the subdomain you want to connect and select **Submit**.
3. Copy and paste the **TXT** and **CNAME** records into the relevant settings of your domain provider account.
4. Return to the Braze dashboard to verify the connection.

![Landing Page Settings page with one TXT and two CNAME records listed with their respective names and values.][1]

{% alert note %}
The subdomain connection can take up to 48 hours, depending on your domain provider. We’ll update your **Landing Page Settings** page when the process is complete.
{% endalert %}

## Using your subdomain

After your subdomain verification is complete, you can use your subdomain for your Braze-hosted landing pages by default. For example, if you connect the subdomain `promo.example.com`, you can add a URL to your landing page that looks like `promo.example.com/holiday-sale`.

{% alert note %}
Contact your customer success manager if you need to remove your subdomain.
{% endalert %}

## Resources from domain providers

Listed below are resources for creating and managing DNS records with commonly used domain providers. If you're using a different provider, refer to that provider's documentation or contact their support team for information.

| Domain provider | Resources |
| --- | --- |
| Bluehost | [DNS Records Explained](https://my.bluehost.com/hosting/help/508)<br> [DNS Management Add Edit or Delete DNS Entries](https://my.bluehost.com/hosting/help/559) |
| Dreamhost | [How do I add custom DNS records?](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| GoDaddy | [Add a CNAME record](https://www.godaddy.com/help/add-a-cname-record-19236?) |
{: .reset-td-br-1 .reset-td-br-2}

## Troubleshooting 

### My subdomain connection failed

Verify that your subdomain was entered correctly and that it matches what you submitted to Braze from your domain provider account. If it's correct and matches, check the TXT and CNAME records provided by Braze. They should match the records you entered into your domain provider account.

## Frequently asked questions

### Can I connect multiple subdomains to my workspace or connect one subdomain to multiple workspaces?

No, you currently can only connect one subdomain to a workspace.

[1]: {% image_buster /assets/img/landing_pages/connect_subdomain.png %}