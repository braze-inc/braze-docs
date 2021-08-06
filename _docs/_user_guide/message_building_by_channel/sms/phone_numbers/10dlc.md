---
nav_title: "A2P 10DLC"
page_order: 1
description: "This article covers A2P 10DLC, why it's are necessary at Braze, helpful costs and throughput information, and how to get started with registration."
page_type: reference

channel:
  - SMS
---

# Application-to-Person 10-Digit Long Codes (A2P 10DLC)

> A2P 10DLC refers to a system in the United States that allows businesses to send Application-to-Person (A2P) type messaging via a standard 10-digit long code (10DLC) phone number. These registered long codes are granted higher throughput, better deliverability, improved compliance, and lower costs than the standard long code user.

{% alert important %}
All customers who currently have and/or use long codes are required to register their long codes for 10DLC; customers who fail to do so will experience heavy filtering of all messages.
{% endalert %}

## Why it's Necessary

10DLC service was created to specifically facilitate A2P messaging using long codes. Historically, long codes were meant for Person-to-Person (P2P) messaging, but when used for marketing reasons, they caused businesses to be constrained by limited throughput and heightened filtering. 

10DLC helps alleviate those issues by offering: 
- __Higher Throughput__: 10DLC numbers support a higher volume of messages than regular long codes.
- __Better Deliverability__: 10DLC numbers are designated for A2P traffic, so messages sent on these numbers are more likely to reach the recipient and are less likely to get filtered or rejected by the carrier than messages sent via regular local long codes. 
- __Improved Compliance__: Using a local long code for commercial text messaging is against the CTIA guidelines. 10DLC numbers were designated for mass messaging and allow brands to comply with industry regulations without relying on short codes.
- __Lower Costs__: 10DLC numbers are a budget-friendly alternative for smaller brands and companies looking to scale their SMS program over time. Plus, brands with existing long codes can simply register those codes with 10DLC and ensure continuity of their existing SMS programs. 

Since 2019, carriers have begun adopting 10DLC for commercial messaging, with Verizon and AT&T currently support 10DLC, and we expect all major carriers to follow soon. While it may cause inconveniences in the short term, in the long term, customers will enjoy better deliverability rates while protecting their consumers from unwanted messages. 

## What you Need to Know

### Costs 
Registering with A2P 10DLC may include several types of fees:

| Fee Type | Descrption |
| -------- | ---------- |
| Registration Fees | Nominal fees that are applied when registering your brand and use case across all major US networks. |
| Secondary Vetting Fees | Brands can appeal their [Brand Trust Score](#trust-score) and request a secondary vetting process to improve their overall throughput; there is a fee associated with this process. |
| Carrier Fees | Fees charged by carriers for outbound SMS and MMS messages sent to users, all existing long codes already have carrier fees in effect. Fees are higher on unregistered traffic (standard long codes) vs. registered traffic (10DLC). |
{: .reset-td-br-1 .reset-td-br-2}

Visit the Twilio 10DLC article to check out updated [fee estimates](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-).

### Throughput
Message throughput for your 10DLC depends on several factors, including brand trust score, daily message limits, and your messaging use cases.

#### Brand Trust Score {#trust-score}
A trust score is assigned when a customer registers for US 10DLC messaging. The higher the trust score, the better the throughput you will experience with your messages. 

The Campaign Registry (TCR) is a third-party agency that uses a reputation algorithm to review specific criteria relating to your company and assign a trust score that determines messaging throughput for each brand. 

|     | Trust Score | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| High | 76-100 | 60 | 60 | 60 |
| Medium | 51-75 | 10 | 10 | 10 |
| Low | 16-50 | 1 | 1 | 1| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Daily Message Limits

Daily limits range from 2000 to 200,000 messages depending on your brand trust score and apply across all long codes. While high brand trust scores come with a throughout of 60 messages per second, any daily message limits set by the carrier will still apply. This means that short codes would be a better option if a brand's daily peak messages are higher than the imposed daily limit. 

{% alert tip %}
Companies listed in the Russel 3000 index are automatically granted the maximum message limit and skip registration and verification. 
{% endalert %}

#### Messaging Use Cases

Throughput is also affected by the type of messaging use case. Specific use cases like social engagement will be susceptible to higher throughput values. The values for this can be found in the following table:

| Standard Use Cases | Description |
| ------------------ | ----------- |
| Marketing | Promotional content such as sales and limited time offers |
| Mixed | Campaign that covers multiple use cases such as Customer Care | 
| Transactional Use Cases | Customer Care, Delivery and Account Notificaitons, 2FA, Security and Fraud Alerts | 

| Special Use Cases | Description |
| ----------------- | ----------- |
| Charity | Messages from a registerd charity such as 501c3 organizations |
| Emergency Services | Notifications about supporting public saftey during emergency situations. Restricted to government and healthcare entities |


Visit the Twilio 10DLC article to check out updated [throughput estimates](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

## Next Steps

Customers who have not yet registered for 10DLC must work with their COM or CSM to register their long codes. __If customers fail to register their long codes, starting June 1, 2021, any A2P sender using long codes will experience heavy filtering of all messages.__ Reach out to your CSM to get started on your 10DLC registration. 