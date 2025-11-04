---
nav_title: IP warming
article_title: IP Warming
page_order: 1
page_type: reference
description: "This reference article covers the topic of IP warming and best practices."
channel: email

---

# IP warming

> IP warming is the practice of getting email inbox providers used to receiving messaging from your dedicated IP addresses. It's an extremely important part of email sending with any email service provider (ESP) and standard practice at Braze to confirm your messages reach their destination inboxes at a consistently high rate.

IP warming is designed to help you establish a positive reputation with internet service providers (ISPs). Every time a new IP address is used to send an email, ISPs programmatically monitor those emails to verify that it isn't being used to send spam to users.

## What if I don't have time to warm IPs?

**IP warming is required.** If you don't warm IPs appropriately, and the pattern of your email causes any suspicion, your email delivery speed could be significantly throttled or slowed. Your domain or IP could also be blocked by the ISPs, which can result in your emails going directly to the spam folder of your user's inbox instead. As such, it's important to warm your IPs properly.

ISPs throttle email delivery when suspicion of spam arises so that they can protect their users. For example, if you send to 100,000 users, the ISP might deliver the email only to 5,000 of those users over the first hour. Then, the ISP monitors measures of engagement such as open rates, click rates, unsubscribes, and spam reports. So, if a significant number of spam reports occur, they might choose to relegate the remainder of that send to the spam folder rather than delivering it to the user's inbox. 

If engagement is moderate, they may continue to throttle your email to collect more engagement data to determine whether or not the mail is spam with more certainty. If the email has very high engagement metrics, they may cease to throttle this email entirely. They use that data to create an email reputation that will eventually determine whether or not your emails are filtered to spam automatically.

If your domain or IP is blocked by an ISP, the message logs in the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) will contain information about what websites to visit to appeal to these ISPs and to get off those lists.

## IP warming schedules

We strongly recommend adhering to this IP warming schedule strictly to support deliverability. It's also important that you don't skip days as consistent scaling improves delivery metrics.

Day | # of Emails to be Sent
----|--------------------------|
1 | 50
2 | 100
3 | 500
4 | 1,000
5 | 5,000
6 | 10,000
7 | 20,000
8 | 40,000
9 | 70,000
10 | 100,000
11 | 150,000
12 | 250,000
13 | 400,000
14 | 600,000
15 | 1,000,000
16 | 2,000,000
17 | 4,000,000
18+ | Double Daily Until Desired Volume

We suggest warming up to your peak sending. That is to say, if you normally send 2 million emails a day but plan to send 7 million for a seasonal period, that "peak" sending is what you should warm up to.

Once warming is complete and you've reached your desired daily volume, you should aim to maintain that volume daily. Some fluctuation is expected, but reaching the desired volume, then only doing a mass blast once a week may negatively affect your delivery metrics and sender reputation. 

{% alert important %}
Most ISPs only store reputation data for 30 days. If you go a month without sending any messages, you'll have to repeat the IP warming process.
{% endalert %}

## How to limit sends during warming

Our built-in user limiting feature serves as a useful tool to help you with warming your IP address. After choosing your desired messaging segments during campaign creation, on the [Target Users]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) step, select the **Advanced Options** dropdown to limit your users. As your warming schedule continues, you can gradually raise this limit to increase the volume of emails you send.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Subdomain segmentation

Many ISPs and email access providers no longer only filter by IP address reputation. These filtering technologies now also account for domain-based reputation. This means that filters will look at all data associated with the sender's domain and not just single out the IP address. For this reason, in addition to warming up your email IP, we also recommend having separate domains or subdomains for marketing, transactional, and corporate mail. 

{% alert important %}
Subdomain segmentation is especially important for large-volume senders. These senders should work with a Braze representative when setting up their account to confirm they adhere to this practice.
{% endalert %}

We recommend segmenting your domains so that corporate mail is sent through your top-level domain, and marketing and transactional mail are sent through different domains or subdomains.

## Best practices

All of the consequences of not IP warming can be avoidable if you follow these IP warming best practices.

### Start with small sending volumes of email

Increase the amount you send each day as gradually as possible. Abrupt, high-volume email campaigns are regarded with the most skepticism by ISPs. Therefore, you should begin by sending small amounts of email and scale gradually toward the volume of email you ultimately intend to send. Regardless of volume, we suggest warming up your IP to be safe. See [IP warming schedule](#ip-warming-schedule).

### Have engaging introductory content

Confirm that your first content is highly engaging and maximizes the likelihood that users click, open, and engage with your email. Always prefer well-targeted emails to indiscriminate blasts when warming IPs.

### Set a consistent sending cadence

Once IP warming is complete, create a sending cadence, making sure to also spread your emails across a day or several days. By creating as much of a consistent schedule as possible, you can prevent an IP cooldown, which can occur if sending volume stops or significantly decreases for more than a few days. 

Refer to our [IP warming schedule](#ip-warming-schedules) to spread your send across a longer time frame, rather than sending a mass blast at a single specific time.

### Clean your email lists

Confirm that your email list is clean and doesn't have old or unverified emails. Ensuring that you're both [CASL- and CAN-SPAM-compliant]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/) is ideal.

### Monitor your sender reputation

When conducting the IP warming process, be sure to carefully monitor your sender reputation while you conduct the IP warming process. These specific metrics are important to watch:
- **Bounce Rates:** If any campaign bounces at more than 3-5%, you should evaluate the cleanliness of your list by following the guidelines in our [Keep It Clean: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/) article. Additionally, you should consider implementing a [sunset policy]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) to stop emailing unengaged or dormant email addresses.
- **Spam Reports:** If any campaign is reported as spam at a rate of more than 0.08%, you should re-evaluate the content you're sending, check that it is targeted to an interested audience, and make sure your emails are appropriately worded to pique their interest.
- **Open Rates:** Open rates are a useful proxy for inbox placement. If your unique open rates are over 25%, you're likely experiencing high inbox placement, which indicates a positive sender reputation.

{% alert tip %}
Braze recommends against using [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) to warm your IPs. Because IP warming campaigns are some of the first campaigns you send, Braze won't have enough information on your users to calculate an optimal send time. In this case, all messages with Intelligent Timing would default to the fallback time and send at the same time anyway.
{% endalert %}

{% alert tip %}
It is normal for mail to be sent to the spam folder during IP warming because your domain and IP have not yet established a positive reputation. If mail lands in your spam folder, your mail administrator may need to add your Braze sending domain and IP to your company's allowlist.
{% endalert %}

