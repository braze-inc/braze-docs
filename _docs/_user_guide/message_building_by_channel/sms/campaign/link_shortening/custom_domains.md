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

> This page covers how to use custom domains with [link shortening]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/) to personalize the look and feel of your shortened URLs and portray a consistent brand image. 

{% alert note %}
Contact your Braze account manager if you're interested in getting started with custom domains.
{% endalert %}

## Domain requirements

- Domains must be procured, owned, and managed by you.
- The domain used for this feature must be unique (that is, different from your website domain), and the domain can't be used to host any web content.
  - You can also use unique subdomains, such as `sms.braze.com`.
- We recommend choosing a domain with as few characters as possible to minimize the length of your URLs.

### Delegating your custom domain

When you delegate your domain to Braze, we automatically handle the certificate renewal to prevent a lapse in service. 

To delegate your domain to Braze, do the following: 

1. Bring a domain that meets the above requirements to your customer success manager. Braze will then check the existing DNS configuration for the domain and confirm that:

- No CAA records exist OR
- CAA records **do** exist but have a record for {% raw %}`<any number> issue "letsencrypt.org"`{% endraw %} or {% raw %}`<anynumber> issuewild "letsencrypt.org"`{% endraw %}

{:start="2"}
2. Create four new A records, one for each IP, and confirm that they are the only A records that exist for the domain link host:
- `151.101.130.133`
- `151.101.194.133`
- `151.101.2.133`
- `151.101.66.133`

## Using custom domains

After they're configured, custom domains can be assigned to one or multiple SMS subscription groups. 

![Subscription groups settings that allow you to select a link-shortening domain.][7]

Campaigns sent with link shortening turned on will use the assigned domain associated with your SMS subscription group.

![SMS message composer preview with a shortened link domain that is different from the domain in the "Message" box.][8]

## Frequently asked questions

### Can delegated domains be shared across multiple subscription groups?

Yes. A single domain can be used with multiple subscription groups. To do so, select the domain for each subscription group that it should be associated with.

### Can delegated domains be shared across multiple workspaces?

Yes. Domains can be associated with subscription groups in multiple workspaces, assuming the workspaces are contained within the same company.

[7]: {% image_buster /assets/img/custom_domain.png %} 
[8]: {% image_buster /assets/img/custom_domain2.png %} 

