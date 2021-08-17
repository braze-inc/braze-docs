---
nav_title: Email Setup
layout: featured
page_order: 5
guide_top_header: "Email Setup"
guide_top_text: "So you want to start sending email campaigns? Braze Onboarding can help you with that! Either follow our guide below or check out our <a href='https://lab.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>LAB course on deliverability</a>."

page_type: landing
description: "This landing page includes resources on getting started with email campaigns."
channel: email
tool: 
- Campaigns
- Canvas

guide_featured_title: "Section Articles"
guide_featured_list:
- name: "Setting Up IPs & Domains"
  link: /docs/user_guide/onboarding_with_braze/email_setup/setting_up_ips_and_domains/
  fa_icon: far fa-dot-circle
- name: Authentication
  link: /docs/user_guide/onboarding_with_braze/email_setup/authentication/
  fa_icon: fas fa-user-shield
- name: "Consent & Address Collection"
  link: /docs/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/
  fa_icon: fas fa-address-book
- name: "Deliverability Pitfalls & Spam Traps"
  link: /docs/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/
  fa_icon: fas fa-exclamation-triangle
- name: Importing Your Email List into Braze
  link: /docs/user_guide/onboarding_with_braze/email_setup/import_your_email_list/
  fa_icon: fas fa-list
- name: Email Validation
  link: /docs/user_guide/onboarding_with_braze/email_setup/email_validation/
  fa_icon: fas fa-envelope-square
- name: IP Warming
  link: /docs/user_guide/onboarding_with_braze/email_setup/ip_warming/
  fa_icon: fas fa-exclamation
- name: SSL Overview
  link: /docs/user_guide/onboarding_with_braze/email_setup/ssl/
  fa_icon: fas fa-mouse-pointer
---

# Requirements

Before you start sending emails, there are some things you need. Refer to the chart below to learn more.

|Requirement | Description | Acquirement |
|---|---|---|
| A Dedicated IP (Internet Protocol)| A dedicated IP is a unique Internet address provided exclusively to a single hosting account. | Braze gives its customers dedicated IPs, to ensure control of your email sender reputation. Braze onboarding will set this up for you.|
| Whitelabeled Domains | These consist of a domain and a subdomain. Whitelabling ensures you pass email authentication checks for DKIM and SPF. | Braze onboarding will generate these domains for you, but you must choose their names. |
|Subdomains | This is a subdivision of a domain and typically looks like: `@news.company.com` within your email address. Having a subdomain will prevent any errors that could damage your company's official email reputation. | Braze onboarding will generate this for you, but you must decide the name of the subdomain. You cannot use subdomains that are currently being used outside of Braze. |
|IP Pools | These are an optional configuration used to separate out the reputation of different types of email (for example: "promotional" vs. "transactional") to prevent the reputation of one from impacting the other and ensure higher deliverability. | Braze onboarding will set up the pools for you; then, when composing your email, choose your email's IP pool from the IP Pool dropdown on the Target Users page.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## IP Warming

{% alert important %}
IP Warming is the __most important step__ in the email setup process. Though it is not your first step (it's actually the last!), we're calling it out here to let you know that you must absolutely warm up your IP address or any emails you send will be sent to spam or be subject to other send barriers.
{% endalert %}

[IP Warmup]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) is when you send a relatively small number of emails out in your first batch, then over time, slightly increase the volume in the following batches until you reach your typical daily volume. This is done at the very end of your email set up process.

By starting with smaller volumes of email, you are establishing a level of trust with your mailbox provider, showing you are only sending emails to relevant users.

Send your first batch of emails to your most engaged users. This will help you gain trust faster with your provider.

After you're done with your IP Warmup, feel free to [start creating and sending emails]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/)!


### For more information on Email at Braze, check out our dedicated [Email section]({{site.baseurl}}/user_guide/message_building_by_channel/email/).

<br>