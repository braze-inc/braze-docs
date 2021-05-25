---
nav_title: IP Warming
page_order: 5

page_type: reference
description: "This reference article covers the topic of IP warming and best practices."
channel: email
---

# IP Warming

## What is IP Warming?

IP Warming is the practice of getting email inbox providers used to receiving messaging from your dedicated IP addresses. It's an extremely important part of sending email with any Email Service Provider, and standard practice at Braze, to ensure your messages reach their destination inboxes at a consistently high rate.

IP Warming is designed to help you establish a positive reputation with ISPs (Internet Service Providers). Every time a new IP address is used to send email, ISPs programmatically monitor email from it in order to verify that it isn't being used to send spam to users.

## What if I don't have time to warm IPs?

__IP Warming is not optional.__ If you fail to warm IPs appropriately, and the pattern of your email causes any suspicion, any or all of the following may happen:

1. __Your email delivery speed could be significantly throttled or slowed.__
      - ISPs throttle email delivery when suspicion of spam arises so that they can protect their users. For example, if you send to 100000 users the ISP might deliver the email only to 5000 of those users over the first hour. The ISP then monitors measures of engagement such as open rates, click rates, unsubscribes, and spam reports.
      - If a significant number of spam reports occur, they might choose to relegate the remainder of that send to the spam folder rather than delivering it to the user's inbox.
      - If engagement is moderate, they may continue to throttle your email to collect more engagement data to determine whether or not the mail is spam with more certainty.
      - If the email has very high engagement metrics, they may cease to throttle this email entirely. They use that data to create an email reputation that will eventually determine whether or not your emails are filtered to spam automatically.

2. __Your domain and or IP could be blacklisted by the IPs at which point all of your email will begin going directly to the spam folder of your user's inbox.__
  - If this occurs, the response codes in the Braze Developer Console will contain information about what websites to visit in order to appeal to these ISPs to get off those lists.

## IP Warming Best Practices

All of __the above consequences are entirely avoidable__ if you follow the following guidelines:

1. __Start by sending small volumes of email, and increase the amount you send each day as gradually as possible.__
      - Abrupt, high volume email campaigns are regarded with the most skepticism by ISPs. Therefore, you should begin by sending small amounts of email and scale gradually towards the volume of email you ultimately intend to send. Regardless of volume, we suggest warming up your IP to be safe. Please see the schedule below for details.
2. __Ensure that your first content is highly engaging, and maximizes the likelihood that users, click, open and engage with your email.__
      - Always prefer well targeted emails to indiscriminate blasts when warming IPs.
3. __When IP warming is complete, continue sending on as consistent a cadence as possible.__ 
      - IPs can cool down if volume stops or significantly decreases for more than a few days.
4. __Spread your email sends across a day or several days.__
      - Features like Braze's Local Time Zone delivery and [Intelligent Timing]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) can help automatically spread your send across a longer timeframe, rather than sending a mass blast at a single specific time.
5. __Ensure that your email list is clean, and doesn't have old or un-verified emails.__ 
      - Ensuring that you're both [CASL- and CAN-SPAM-compliant][40] is ideal.
6. __Carefully monitor your Sender Reputation while you conduct the IP warming process.__ 
  - The following metrics are important to watch during warming:<br>__- Bounce Rates__: If any campaign bounces at more than 3-5%, you should evaluate the cleanliness of your list by following the guidelines in our ["Keep It Clean: The Importance of Email List Hygiene" article][43]. Additionally you should consider implementing a [Sunset Policy][46] to stop emailing unengaged or dormant email addresses.<br>__- Spam Reports__: If any campaign is reported as spam at a rate of more than 0.08%, you should re-evaluate the content you're sending, and ensure that it is targeted to an interested audience, and is appropriately worded to pique their interest.
      - Sender Reputation Scores: The following services are useful for checking how your reputation is progressing: [ReturnPath's SenderScore][44] & Cisco's IronPort [SenderBase][45]

## IP Warming Schedules

We strongly recommend adhering to this IP warming schedule strictly in order to ensure deliverability. It's also important that you don't skip days as consistent scaling improves deliverability.

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

Once warming is complete, and you've reached your desired daily volume you should aim to maintain that volume on a daily basis. Some fluctuation is alright, but reaching the desired volume, then only doing a mass blast once a week may have negative consequences for your deliverability and sender reputation. Lastly, most ISPs only store reputation data for 30 days. If go a month without sending, you will have to repeat the IP warming process.

## How to Limit Sends During Warming

Braze's built-in user limiting feature serves as an useful tool to help you with warming your IP address. After you choose your desired messaging segments during campaign creation (Step 3: Target Users), select the 'Advanced Options' dropdown in order to limit your users. As your warming schedule continues, you can gradually raise this limit to increase the volume of email you send.

![Limit Users][18]

## IP Warming notifications

Braze takes your deliverability very seriously. As such, we’ve built a number of warnings and notifications throughout the dashboard to limit any issues during the IP warming process.  Braze will work very closely with you to define your IP Warming time frame as well as understand how many emails should be sent daily.

During your established IP warming period, there will be numerous reminders in the Dashboard that your app group is going through IP Warming. Additionally, Braze will provide warnings throughout the Campaign or Canvas creation process if you accidentally go beyond your daily quota.

As a last issue deterrent, Braze will automatically email a select number of individuals regarding any breach of your quota so that it can be addressed immediately.

## Subdomain Segmentation

Many ISPs and email access providers no longer only filter by IP address reputation. These filtering technologies now also account for domain-based reputation.  This means that filters will look at all data associated with the sender's domain and not just single out the IP address. For this reason, in addition to warming up your email IP we also recommend having separate domains or subdomains for marketing, transactional, and corporate mail. We recommend segmenting your domains such that corporate mail is sent through your top level domain, and marketing and transactional mail are sent through different domains or subdomains.

{% alert important %}
  Subdomain segmentation is especially important for large-volume senders. These senders should work with a Braze representative when setting up their account to ensure they are adhering to this practice.
{% endalert %}

[18]: {% image_buster /assets/img_archive/Email_IP_Warming_Sends_Limit_new.png %}
[40]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
[43]: https://www.braze.com/blog/email-list-hygiene/
[44]: https://senderscore.org/
[45]: http://www.senderbase.org/
[46]: {{site.baseurl}}/help/best_practices/email/sunset_policies/
