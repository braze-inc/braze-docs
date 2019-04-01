---
nav_title: Overview & Requirements
page_order: 0
---

# Email Set Up

So you want to send email campaigns, huh? We can help you with that! Either follow our guide below or check out our [LAB course on deliverability](https://lab.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability).

## Requirements

Before you start sending emails, there are some things you need. Refer to the basic chart below to learn more.

|Requirement | Description | Acquirement |
|---|---|---|
| A Dedicated IP (Internet Protocol)| A dedicated IP is a unique Internet address provided exclusively to a single hosting account. | Braze gives its customers dedicated IPs, to ensure control of your email sender reputation. We will set this up for you.|
| Whitelabeled Domains | These consist of a domain and a subdomain. Whitelabling ensures you pass email authentication checks for DKIM and SPF. | We will generate these domains for you, but you must choose their names. |
|Subdomains | This is a subdivision of a domain and typically looks like: `@news.company.com` within your email address. Having a subdomain will prevent any errors that could damage your company's official email reputation. | We will generate this for you, but you must decide the name of the subdomain. You cannot use subdomains that are currently being used outside of Braze. |
|IP Pools | These are an optional configuration used to separate out the reputation of different types of email (for example: "promotional" vs. "transactional") to prevent the reputation of one from impacting the other and ensure higher deliverability. | We will set up the pools for you; then, when composing your email, choose your email's IP pool from the IP Pool dropdown on the Target Users page.|

## IP Warming

{% alert important %}
IP Warming is the __most important step__ in the email setup process. Though it is not your first step (it's actually the last!), we're calling it out here and now to let you know that you must absolutely warm up your IP address or any emails you send will be sent to spam or be subject to other send barriers. All of this will be for nothing!
{% endalert %}

IP Warmup is when you send a relatively small number of emails out in your first batch, then slightly increase the volume in the next batch, and so on, until you reach your typical daily volume. This is done at the very end of your email set up process.

By starting with smaller volumes of email, you are establishing a level of trust with your mailbox provider, showing you are only sending emails to relevant users.

Send your first batch of emails to your most engaged users. This will help you gain trust faster with your provider.

For more on IP Warming, please check out our [Email Best Practices section]({{ site.baseurl }}/help/best_practices/email/ip_warming/#subdomain-segmentation).

After you're done with your IP Warmup, feel free to [start creating and sending emails]({{ site.baseurl }}/user_guide/message_building_by_channel/email/creating_an_email_campaign/)!
