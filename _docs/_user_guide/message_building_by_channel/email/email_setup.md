---
nav_title: Email setup
article_title: Onboarding Email Setup
layout: dev_guide
page_order: 1
guide_top_header: "Email Setup"
guide_top_text: "Braze can help you start sending email campaigns. Either follow our guides or check out our <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>Email Onboarding</a> Braze Learning course."
page_type: landing
description: "This landing page includes resources on getting started with email campaigns including setting up your IPs and domains, IP warming, email validation, and more."
channel: email

guide_featured_title: "Section articles"
guide_featured_list:
- name: "Setting Up IPs and Domains"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/
  image: /assets/img/braze_icons/target-05.svg
- name: "IP Warming"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "Email Validation"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/email_validation/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "Email Authentication"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/authentication/
  image: /assets/img/braze_icons/user-square.svg
- name: "Importing Your Email List"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/
  image: /assets/img/braze_icons/list.svg
- name: "SSL Overview"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ssl/
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Consent and Address Collection"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/
  image: /assets/img/braze_icons/book-closed.svg
- name: "Deliverability Pitfalls and Spam Traps"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/deliverability_pitfalls_and_spam_traps/
  image: /assets/img/braze_icons/alert-triangle.svg
---

## Requirements

Before you start sending emails, there are some things you need. Refer to the following chart to learn more about these requirements.

| Requirement | Description | Source |
|---|---|---|
| A Dedicated IP (Internet Protocol)| A dedicated IP is a unique internet address provided exclusively to a single hosting account. | Braze gives its customers dedicated IPs, to ensure control of your email sender reputation. Braze onboarding will set this up for you.|
| Whitelabeled Domains | These consist of a domain and a subdomain. By using whitelabeling, you can pass email authentication checks for DKIM and SPF. | The Braze Onboarding team will generate these domains for you, but you must choose their names. |
| Subdomains | This is a subdivision of a domain (such as "@news.company.com") within your email address. Having a subdomain will prevent any errors that could damage your company's official email reputation. | The Onboarding team will generate this for you, but you must decide the name of the subdomain. You cannot use subdomains that are currently being used outside of Braze. |
| IP Pools | These are an optional configuration used to separate out the reputation of different types of email (such as "promotional" and "transactional") to prevent the reputation of one from impacting the other and support higher deliverability. | The Onboarding team will set up the pools for you. Then, when composing your email, select your email's IP pool from the **IP Pool** dropdown on the **Target Audiences** page.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## IP warming

{% alert important %}
IP warming is the **most important step** in the email setup process. Though it is not your first step (it's actually the last), we're calling it out here to let you know that you must warm up your IP address, or else any emails you send will be sent to spam or be subject to other send barriers.
{% endalert %}

[IP warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) is when you send a relatively small number of emails out in your first batch, then over time, slightly increase the volume in the following batches until you reach your typical daily volume. This is done at the very end of your email set up process.

By starting with smaller volumes of email, you are establishing a level of trust with your email provider, showing you are only sending emails to relevant users. By sending your first batch of emails to your most engaged users, this can help you gain trust faster with your provider.

After you're done warming up your IP, you can [start creating and sending emails]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)!

<br><br>