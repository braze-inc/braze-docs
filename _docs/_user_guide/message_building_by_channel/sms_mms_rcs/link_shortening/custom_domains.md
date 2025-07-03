---
nav_title: Custom Domains
article_title: Custom Domains
page_order: 0
description: "This page covers how to use custom domains with link shortening to personalize the look and feel of your shortened URLs."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Custom domains

> This page covers how to use custom domains with link shortening to personalize the look and feel of your shortened URLs, and portray a consistent brand image. 

{% alert note %}
Contact your Braze account manager if you're interested in getting started with custom domains.
{% endalert %}

## Domain requirements

- Domains must be procured, owned, and managed by you.
- The domain used for this feature must be unique (that is, different from your website domain), and the domain can't be used to host any web content.
  - You can also use unique subdomains, such as `sms.braze.com`.
- We recommend choosing a domain with as few characters as possible to minimize the length of your URLs.

## Delegating your custom domain

When you delegate your domain to Braze, we automatically handle the certificate renewal to prevent a lapse in service. 

To delegate your domain to Braze, do the following: 

### Step 1: Select a domain

1. Choose a domain or subdomain (such as `sms.yourbrand.com`) that meets the above requirements.
2. Confirm you have access to the domain’s DNS settings.
3. Contact your Braze customer success manager to begin the setup process.

### Step 2: Verify DNS configuration

Your Braze customer success manager will check the domain’s DNS configuration and work with you to update the DNS settings.

### Step 3: Wait for the Braze configuration

{% alert important %}
Do not update your DNS A records until instructed by your Braze customer success manager.
{% endalert %}

### Step 4: Update DNS A records

After receiving confirmation from your customer success manager, update your DNS settings with the A records provided to you for your custom domain. For example, for `sms.yourbrand.com`, you'd create four A records pointing to the IPs. Ensure these are the only A records for the domain. 

### Step 5: Verify setup

Your Braze customer success manager will verify the A records. After they're verified, your custom domain will be ready to be assigned to one or more SMS subscription groups.

## Using custom domains

Once configured, custom domains can be assigned to one or multiple SMS subscription groups. 

![Subscription groups settings that allow you to select a link-shortening domain.]({% image_buster /assets/img/custom_domain.png %})

Campaigns sent with link shortening turned on will use the assigned domain associated with your SMS subscription group.

![SMS message composer preview with a shortened link domain that is different from the domain in the "Message" box.]({% image_buster /assets/img/custom_domain2.png %})

## Frequently asked questions

### Can delegated domains be shared across multiple subscription groups?

Yes. A single domain can be used with multiple subscription groups. To do so, select the domain for each subscription group that it should be associated with.

### Can delegated domains be shared across multiple workspaces?

Yes. Domains can be associated with subscription groups in multiple workspaces, assuming the workspaces are contained within the same company.
