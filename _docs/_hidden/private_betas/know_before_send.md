---
nav_title: Before Your Send - Channels Guide
permalink: /amphtml/
hidden: true
---

Before You Send - Channels Guide

Braze encourages customers to launch their campaigns and Canvases with confidence! On our website, we have a [Pre Launch Checklist](https://labplaybooks.braze.com/canvas-playbooks#/subpage/b2rj8) guide for customers to learn how to ensure a smooth launch before hitting that big blue button, or after setting Canvas to active. To take this a step further, we’re breaking out additional criteria to know “before you send” for key channels such as Email, Push, SMS, and Content Cards

STOP 
Disclaimer: These practices are based on a collective knowledge here at Braze from supporting messaging on these channels throughout the years. As every account comes with individual nuances and the industry continues to evolve (channel regulars & security changes), this guide should be treated as additional resources, not ironclad rules. We highly recommend you continue to thoroughly test campaigns, particularly large sends, before sending in earnest.
  
General

- Review Braze [API rate limits](https://www.braze.com/docs/api/basics/#api-limits) per app group. If you are looking to discuss increasing API rate limits (and are already batching requests), start a discussion with your CSM. Keep in mind that this process requires lead-time so please do this with enough time prior to a key event. If you’re thinking… What’s Rate Limiting? [Read on here](https://www.braze.com/resources/articles/whats-rate-limiting).
- If you are using a Global Control Group, a percentage of all users will not receive any campaigns or Canvases. If you’d like to see which users are in your Global Control Group, you can export your Group’s members via CSV or API
- [Frequency Capping](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) and [Rate Limiting](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting) are tools that provide you greater control over your users’ messaging experience
  - In a canvas, the rate limit applies to the entire canvas, not the individual steps. Say for example you set a 10,000 message/minute rate limit on a Canvas and have 3 steps, delayed by 1 second after one another...it will be limited to 10,000 messages because the limit will have been reached at the first step
  - There may be some campaigns, like transactional messages, that you want to always reach the user, even if they have already reached their frequency cap. For example, a delivery notification. If you want a particular campaign to override frequency capping rules, you can set this up in the Braze dashboard when scheduling that campaign’s delivery by toggling Frequency Capping to OFF

Email

- <2 million emails per day on a single IP is the general recommendation, as long as that volume has been properly warmed. If you are planning to send more than 2 million emails in a day with any degree of regularity, that is when we would start suggesting using multiple IP addresses bundled into an IP Pool However, there are still many factors that determine capable sending volumes for an IP such as:
  - Mailboxes: Gmail, Microsoft, and Yahoo can likely handle millions per day from a single IP, whereas a smaller regional mailbox provider or one with wanting infrastructure like Spectrum/Charter or Optonline would balk at seeing millions from a single IP
    - If you are looking to send in a shorter time frame only, we would recommend looking at how quickly the different providers accept mail to gauge the number of IP addresses to send from
  - Sender reputation: It might be possible to send a larger volume per day from a single IP, but only if a sender has ramped up to that volume and if their sender reputation is good enough at each mailbox provider or domain they’re sending to to allow that volume
- Before sending out your initial emails, it’s important to get permission from your customers first ([Understand email subscriber states](https://www.braze.com/docs/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/)) This is an important part of the [Braze Acceptable Use Policy](https://www.braze.com/company/legal/aup).
- If you want to drastically increase your audiences yet keep optimal email delivery, you should revisit best practices from IP warming and the sample [IP warming schedule](https://www.braze.com/docs/user_guide/onboarding_with_braze/email_setup/ip_warming/#ip-warming-schedules).
- The reason for limiting sends per IP is because even if properly warmed, email providers will begin to throttle receipt of emails when a sender exceeds those numbers. This will lead to high amounts of soft bounces, and will lead to users not receiving emails at or near the time when the client would like them to. Worse, this can be damaging to an IP’s reputation, as sending too many emails from a single IP is seen as spammy behavior and can result in lowered overall deliverability rates.

Push

- Braze’s typical throughput for Push is ~20,000 personalized messages per second, 1.2m per minute, or 72m per hour. As a note, we do not commit to any sending speed SLAs contractually. [This article](https://www.braze.com/perspectives/article/building-braze-job-queues-resiliency) by one of our engineering managers details how we ensure this resilience
- There are many additional factors that could influence these send speeds, including the use of Connected Content or lots of Liquid and/or general Liquid personalisation. These numbers are only estimations
- In order for users to receive a push message from Braze they need their subscription status to be either opted in or subscribed (differences between iOS and Android) AND the Push Enabled = True. What are push enablement and push subscription? [See here](https://www.braze.com/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/).

SMS

- Understand what SMS allotments are currently attached to your account (short codes, long codes, etc.) and [how much throughput that provides you](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/phone_numbers/short_and_long_codes/). Do you have enough throughput to send in your desired time?
- Have you tested your SMS creative in the [SMS segment calculator](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy)?
  - Keep in mind that the number of SMS Segments should be taken into account with your throughput capabilities. Audience * SMS Segments = Throughput needed. See more in [How Can I Avoid Overages](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/faqs/#how-can-i-avoid-overages)
  - Throughput has changed some in the US with US A2P 10DLC registration ([more information here](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US))
  - As a note, we do not commit to any sending speed SLAs contractually due to multiple factors such as traffic congestion, carrier issues, etc. may impact the actual delivery rate
- Alphanumeric Sender ID - Two-way messaging will no longer work if you use an alphanumeric sender ID, these are one-way only
- To launch an SMS campaign through Braze, a Subscription Group must be selected
- SMS messages are normally defaulted to be sent from the Short Code in the sender pool
- [Review SMS laws, regulations and abuse prevention](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/). To ensure that you are using the SMS Services in compliance with all applicable laws, you should seek the advice of your legal counsel prior to sending.

Content Cards

- Content Card message fields are limited to 2kB in pre-compression size, calculated by adding the byte-size length of the following fields: Title, Message, Image URL, Link Text, Link URL(s), and Key/Value Pairs (names + values). Messages that exceed this size will not be sent. Note that this does not include the size of the image but rather the length of the image URL
- Each user is eligible to receive up to 100 non-expired and non-dismissed Content Cards (this 100 is across all feeds, not per feed). As a user becomes eligible for more than 100 cards, Braze will begin to remove older cards from their feed, even if they were unread
- Frequency capping does not apply to Content Cards
- Review this [Content Cards reporting documentation](https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards/reporting/) for analytics terms such as Total Impressions, Unique Impressions,  Unique Recipients that can cause confusion among clients
- Regarding how impressions are logged, there are some nuances between web, Android and iOS, but generally speaking, we log an impression once a card is seen. So scrolled to the specific "content card" inside the content card feed
- Once a card is sent, you can't "update" the copy. You have to remove the original card and send down a new card with any updates
- Is there is a way to handle cache (something like cache buster) in content cards, the same way we are able to handle in connected content?
  - While there is a segment specifically talking about [Cache Busting in Connected Content](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching) do note that the caching option for a content card would be totally different and can be referred to the below documentation links:([Content Card Customization for Android/FireOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/content_cards/customization/#customizing-card-rendering-for-android)) [AND/OR] ([appboy | Braze Web SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards)) for more information
- By default Braze refreshes content cards / requests a content cards sync at session start, on feed down swipe (mobile only), and when the cards view is shown if the last refresh was over 1 minute ago. 

In-app Messages

- How do in-app messages function? At session start, the SDK requests that all in-app messages the a user is eligible to be sent to the device along with its triggers, so if they perform the event during the session they can receive the in-app message quickly and reliably
- Due to the above, in-app messages cannot be triggered by custom events in a canvas step
- For in-app messages, we don’t have a concept of “sent” since these work a little differently than other channels. We don’t “send” an in-app message, as that seems to imply that you click launch, and people all receive it. To see an in-app message a user has to start a session, be in the eligible audience, and then perform the trigger. So we track “impressions” as it’s more clear
