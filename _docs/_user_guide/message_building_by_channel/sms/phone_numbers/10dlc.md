---
nav_title: "A2P 10DLC"
page_order: 1
description: "This article covers A2P 10DLC, why it's are neccessary at Braze, helpful costs and througput information, and how to get started with registration."
page_type: reference

channel:
  - SMS
---

# Application-to-Person 10-Digit Long Codes (A2P 10DLC)

> A2P 10DLC refers to a system in the United States that allows businesses to send Application-to-Person (A2P) type messaging via a standard 10-digit long code (10DLC) phone number. 

All customers who currently have and/or use long codes are required to register their long codes for 10DLC, customers who fail to do so will experiance heavy filtering of all messages.

## Why it's Neccesary

10DLC service was created to specifically facilitate Application-to-Person (A2P) messaging using long codes. Historically, long codes were meant for Person-to-Person (P2P) messaging, and when used for marketing reasons, they caused businesses to be constrained by limited throughput and heightened filtering. 10DLC helps alleviate those issues, improving overall message deliverability, allowing brands to send messages at scale, including links and calls to action, and helping further protect consumers from unwanted messages. 

Since 2019, carriers have begun adopting 10DLC for commercial messaging instead of using long codes meant for person-to-person messaging. Verizon and AT&T currently support 10DLC, and we expect all major carriers to follow soon. While it may cause inconveniences in the short term, in the long term, customers will enjoy better deliverability rates while protecting their consumers from unwanted messages. 

## What you Need to Know

### Costs 

Registering with A2P 10DLC includes two types of fees, registration fees and carrier fees.
- Registration Fees: fees that are applied when registering your brand, and use case. 
- Carrier Fees: fees that are charged by carriers for 10DLC messages sent to users. These fees are applied for each outbound SMS segment or MMS message. 

Visit the Twilio 10DLC article to check out updated [pricing estimates](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-).

### Throughput

Throughput is dependent on several different factors:
- Trust Score: A trust score is assigned when a customer registers for US 10DLC messaging. The higher the trust score, the better the throughput you will experience with your messages. 
- Use Cases: Throughput is also affected by the type of messaging use case. Specific use cases like social engagement will be susceptible to higher throughput values. The values for this can be found in the following table.

Visit the Twilio 10DLC article to check out updated [throughput estimates](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

## Next Steps

Customers who have not yet registered for 10DLC must work with their COM or CSM to register their long codes. __If customers fail to register their long codes, starting June 1, 2021, any A2P sender using long codes will experience heavy filtering of all messages.__ Reach out to your CSM to get started on your 10DLC registration. 