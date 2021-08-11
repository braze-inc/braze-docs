---
nav_title: "A2P 10DLC"
page_order: 2.9
description: "This article covers A2P 10DLC, why 10DLC registration is necessary for US long code customers, helpful costs and throughput information, and how to get started with registration."
page_type: reference

channel:
  - SMS
---

# Application-to-Person 10-Digit Long Codes (A2P 10DLC)

> A2P 10DLC refers to a system in the United States that allows businesses to send Application-to-Person (A2P) type messaging via a standard 10-digit long code (10DLC) phone number. These registered long codes are granted higher throughput, better deliverability, and improved compliance than the standard long code.

{% alert important %}
All customers who currently have and/or use US long codes to send to US customers are required to register their long codes for 10DLC; those who fail to do so will experience heavy filtering of all messages.
{% endalert %}

## Why It's Necessary

10DLC service was created to specifically facilitate A2P messaging using long codes. Historically, long codes were meant for Person-to-Person (P2P) messaging, but when used for marketing reasons, they caused businesses to be constrained by limited throughput and heightened filtering. 

10DLC helps alleviate those issues by offering: 
- __Higher Throughput__: 10DLC numbers support a higher volume of messages than regular long codes.
- __Better Deliverability__: 10DLC numbers are designated for A2P traffic, so messages sent with these numbers are more likely to reach the recipient and are less likely to get filtered or rejected by the carrier than messages sent via regular local long codes. 
- __Improved Compliance__: Using a local long code for commercial text messaging is against the [CTIA](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf) guidelines. 10DLC numbers were designated for mass messaging and allow brands to comply with industry regulations without relying on short codes.
- __Budget Friendly__: 10DLC is a great option for companies who want to get started sending SMS or send SMS at small volumes. For brands sending at larger messaging volumes of over 100,000 messages a day, Braze would recommend using a short code. 

Since 2019, carriers have begun adopting 10DLC for commercial messaging, with Verizon and AT&T currently supporting 10DLC, and we expect all major carriers to follow soon. While it may cause inconveniences in the short term, in the long term, customers will enjoy better deliverability rates while protecting their consumers from unwanted messages. 

## What You Need to Know

### Costs 
Registering with A2P 10DLC may include several types of fees:

| Fee Type | Description |
| -------- | ---------- |
| Registration Fees | Nominal fees applied when registering your brand and use case across all major US networks. |
| Secondary Vetting Fees | Brands can appeal their [Brand Trust Score](#trust-score) and request a secondary vetting process to improve their overall throughput; there is a fee associated with this process. |
| Carrier Fees | Fees charged by carriers for outbound SMS and MMS messages sent to users once registered for 10DLC. Starting October 1, 2021, carrier fees will be higher on unregistered traffic (standard long codes) than registered traffic (10DLC). |
{: .reset-td-br-1 .reset-td-br-2}

Visit the Twilio 10DLC article to check out updated [fee estimates](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-).

### Throughput
Message throughput for your 10DLC depends on several factors, including brand trust score, daily message limits, and your messaging use cases.

#### Brand Trust Score {#trust-score}
The Campaign Registry (TCR) is a third-party agency that uses a reputation algorithm to review specific criteria relating to your company and assign a trust score that determines messaging throughput for each brand. This trust score will be assigned when a customer registers for US 10DLC messaging. The higher the trust score, the better the messages per second (MPS) you will experience. 

|     | Trust Score | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| High | 76-100 | 60 MPS | 60 MPS | 60 MPS |
| Medium | 51-75 | 10 MPS | 10 MPS | 10 MPS |
| Low | 16-50 | 1 MPS | 1 MPS | 1 MPS | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert tip %}
Companies listed in the Russel 3000 Index will be granted a high throughput and brand trust score after 10DLC registration and review. 
{% endalert %} 

#### Daily Message Limits

Daily limits range from 2,000 to 200,000 messages depending on your brand trust score and apply across all long codes. While high brand trust scores come with a throughput of 60 messages per second, any daily message limits set by the carrier will still apply. This means that short codes would be a better option if a brand's daily peak messages are higher than the imposed daily limit. 

#### Messaging Use Cases

Throughput is also affected by the type of messaging use case you choose. Most customers will fall under the standard marketing or mixed marketing use case. Other less common use cases will be susceptible to differing throughput values.

Depending on your use case, the trust score needed to achieve the maximum throughput will vary. The tables below list standard use cases and common use case trust score ranges. For special use cases such as emergency services or charity, please reference the [Twilio docs](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Standard Use Cases | Description |
| ------------------ | ----------- |
| Marketing | Promotional content such as sales and limited time offers. |
| Mixed | Campaign that covers multiple use cases such as Customer Care. | 
| Higher Education | Campaigns for higher education institutions. |
| Polling & Voting | Non-political polling and voting such as customer surveys. |
| PSA | PSAs to raise awareness about a given topic. |
| Customer Care | Support, account management, and other customer interactions. |
| Delivery Notifications | Status of delivery messages. |
| Account Notifications | Notifications about the status of an account. |
| 2FA | Any authentication of account verification such as OTP. | 
| Security Alerts | Notification of a compromised system. |
| Fraud Alerts | Messaging about potentially fraudulent activity. |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs %}
{% tab Declared Use Case %}
A declared use case means you have chosen one specific non-marketing use case (for example, 2FA or Account Notifications).

| Trust Score | Total throughput toward major US networks | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 76-100 | 180 MPS | 60 MPS | 60 MPS | 60 MPS |
| 51-75 | 30 MPS | 10 MPS | 10 MPS | 10 MPS |
| 16-50 | 3 MPS | 1 MPS | 1 MPS | 1 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% tab Mixed/Marketing Use Case %}

Mixed/Marketing use cases can be registered for customers who want to send messages for multiple use cases from the same set of numbers or for marketing.

| Trust Score | Total throughput toward major US networks | AT&T | T-Mobile  | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 86-100 | 180 MPS | 60 MPS | 60 MPS | 60 MPS |
| 66-85 | 30 MPS | 10 MPS | 10 MPS | 10 MPS |
| 26-65 | 3 MPS | 1 MPS | 1 MPS | 1 MPS| 
| 15-25 | 2.2 MPS | 0.2 MPS | 1 MPS | 1 MPS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endtab %}
{% endtabs %}

Visit the Twilio 10DLC article to check out updated [throughput estimates](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

## Next Steps

Customers who have not yet registered for 10DLC must work with their COM or CSM to register their long codes. __If customers fail to register their long codes, starting October 1, 2021, any A2P sender using long codes will experience heavy filtering of all messages.__ Reach out to your CSM to get started on your 10DLC registration. 
