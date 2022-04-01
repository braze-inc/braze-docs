---
nav_title: Before Your Send - Channels Guide
permalink: /before_send/
hidden: true
---

# Before You Send - Channels Guide

We encourage customers to launch their campaigns and Canvases with confidence! After visiting our [Pre-Launch Guide](https://labplaybooks.braze.com/canvas-playbooks#/subpage/b2rj8) that covers the necessary components that ensure a smooth post-launch of your campaigns and Canvases, refer to this final list of checks or "gotchas" for email, push, in-app messages, SMS, and Content Cards.

{% alert note %}
While we provide an extensive list of resources for customers to reference pre-send, each channel has individual nuances that continue to grow as we evolve our products. The checks listed below are purely suggestions, we recommend thoroughly testing your campaigns, and large sends before sending. 
{% endalert %}

order according to mention order
Notes: "per app group" vs "per endpoint" for API rate limits. 

### General

- [Rate Limiting]({{site.baseurl}}/resources/articles/whats-rate-limiting): Review the Braze [API rate limits]({{site.baseurl}}/docs/api/basics/#api-limits) for each endpoint. If you are looking to increase your API rate limits (and are already batching requests), reach out to your customer success manager. Keep in mind that this process requires lead-time, so plan accordingly.
- Global Control Groups: If you are using a Global Control Group, a percentage of your users will not receive any campaigns or Canvases. If you would like to see a list of these users, export them via CSV or [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).
- [Frequency Capping]({{site.baseurl}}/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) and [Rate Limiting]({{site.baseurl}}/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting) are tools that provide you greater control over your users’ messaging experience
  - In a Canvas, the rate limit applies across the entire Canvas, not the individual steps. For example, if you were to set a 10,000 message/minute rate limit on a Canvas with multiple steps, it will still be limited to 10,000 messages because the limit will have been reached at the first step.
  - There are some campaigns, like transactional messages, that you will want to always reach the user, even if you have already reached their frequency cap (for example, a delivery notification). If you want a particular campaign to override frequency capping rules, you can set this up in the Braze dashboard when scheduling that campaign's delivery by toggling frequency capping off.

### Email

- 2 million emails per day in a single IP is the general recommendation, as long as that volume had been properly warmed. If you are planning to send more than 2 million emails in a day with any degree of regularity, you might want to consider using multiple IP addresses bundled into an IP Pool. However, there are still many factors that determine the capable sending volumes for an IP such as: 
  - Mailboxes: Gmail, Microsoft, and Yahoo can likely handle millions per day from a single IP, whereas a smaller regional mailbox provider or one with a smaller infrastructure might not be able to handle that amount.
    - If you are looking to send in a shorter time frame only, we recommend looking at how quickly different providers accept mail to gauge the number of IP addresses to send from.
  - Sender reputation: You might be able to send a larger volume per day from a single IP if a sender has ramped up to that volume and if their sender reputation is good enough at each mailbox provider or domain they’re sending to, to allow that volume.
- Before sending out your initial emails, it’s important to get permission from your customers first. Refer to [Consent and address collection]({{site.baseurl}}/docs/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/) and our [Braze Acceptable Use Policy]({{site.baseurl}}/company/legal/aup) for more information.
- If you want to drastically increase your audiences yet keep optimal email delivery, revisit best practices from IP warming and the sample [IP warming schedule]({{site.baseurl}}/docs/user_guide/onboarding_with_braze/email_setup/ip_warming/#ip-warming-schedules).
- The reason for limiting sends per IP is because even if properly warmed, email providers will begin to throttle receipt of emails when a sender exceeds those numbers. This will lead to high amounts of soft bounces and will lead to users not receiving emails at or near the time when the client would like them to.  This could also affect an IP's reputation and lead to lowered deliverability rates, as sending too many emails from a single IP is seen as "spammy".

### Push

- Braze's typical throughput for push is around 20,000 personalized messages per second, 1.2 million per minute, or 72 million per hour. Note that we do not commit to any sending speed SLAs contractually. Refer to [Building Braze Job Queues Resiliency]({{site.baseurl}}/perspectives/article/building-braze-job-queues-resiliency) on how we ensure this resilience. 

- The use of Connected Content and Liquid personalization may influence sending speeds, among other factors.
- There are many factors that could influence these sending speeds, including the use of Connected Content and Liquid personalization.

# do more research on this
- In order for users to recieve a push message from Braze, they need their subscription statuses to be either opted-in (iOS) or subscribed (Android) AND `Push Enabled = True`. Refer to [Users and subscription]({{site.baseurl}}/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/) for more information. 

### SMS

- Understand what SMS allotments are currently attached to your account (short code, long code, etc.) and [how much throughput that provides you]({{site.baseurl}}/docs/user_guide/message_building_by_channel/sms/phone_numbers/short_and_long_codes/) to ensure you have enough throughput to send in your desired time.
- Test your SMS copy in the [SMS segment calculator]({{site.baseurl}}/docs/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy). 
  - Keep in mind that the number of SMS segments should be taken into account with your throughput capabilities. (Audience * SMS segments = Throughput needed). Refer to SMS FAQs on [avoiding overages]({{site.baseurl}}/docs/user_guide/message_building_by_channel/sms/faqs/#how-can-i-avoid-overages) for more information.
  - Throughput has changes in the US with US [A2P 10DLC registration](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). 
  - Note that we do not commit to any sending speed SLAs contractually due to multiple factors such as traffic congestion, carrier issues, etc. that may impact the actual delivery rates.
- Alphanumeric sender ID: Two-way messaging will no longer work if you use an alphanumeric sender ID, these are one-way only.
- To launch an SMS campaign through Braze, a subscription group must be selected.
- SMS messages are normally defaulted to be sent from the short code in the sender pool.
- [Review SMS laws, regulations and abuse prevention]({{site.baseurl}}/docs/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) to ensure that you are using the SMS services in compliance with all applicable laws. Make sure you should seek the advice of your legal counsel prior to sending.

### Content Cards

- Content Card message fields are limited to 2KB in pre-compression size, calculated by adding the byte-size length of the following fields: title, message, image URL, link text, link URLs, and key-value pairs. Messages that exceed this size will not be sent. Note that this does not include the size of the image, but rather the length of the image URL. 
- Each user is eligible to receive up to 100 non-expired and non-dismissed Content Cards (100 across all feeds, not per feed). As a user becomes eligible for more than 100 cards, Braze will begin to remove older cards from their feed, even if they were unread.
- Frequency capping does not apply to Content Cards.
- Review Content Card [reporting terms]({{site.baseurl}}/docs/user_guide/message_building_by_channel/content_cards/reporting/) such as total impressions, unique impressions, unique recipients that can cause confusions. 
- Regarding how impressions are logged, there are some nuances between Web, Android, and iOS, but generally, we log an impression once a card is seen. 

# What does this mean?
So scrolling to the specific Content Card inside the Content Card feed.

- Once a card is sent, you will be unable to update the copy. You have to remove the original card and send down a new card with any updates.
- Is there a way to handle cache in Content Cards, the same way we can handle in Connected Content? 
  - While there is a segment specifically talking about [Cache Busting]({{site.baseurl}}/docs/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching) in Connected Content, the caching option for a Content Card would be totally different and can be referred in the following resources:
    - [Content Card customization for Android/FireOS]({{site.baseurl}}/docs/developer_guide/platform_integration_guides/android/content_cards/customization/#customizing-card-rendering-for-android)
    - [Appboy Braze Web SDK caching methods](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards) 
- By default, Braze refreshes Content Card requests as Content Cards sync at session start, on feed down swipe (mobile only), and when the cards view is shown if the last refresh was over one minute ago.

### In-app messages

- How do in-app messages function?<br>At session start, the SDK requests that all in-app messages that a user is eligible for, be sent to the device along with its triggers, so if they perform the event during the session they can receive the in-app message quickly and reliable. Due to this, in-app messages cannot be triggered by custom events in a Canvas step.
- For in-app messages, we do not have a concept of "sent" since they work differently than other channels. We do not send an in-app message, as that seems to imply that you click **Launch**, and people all receive it. To see an in-app message, a user has to start a session, be in the eligible audience, and then perform the trigger. So we track "impressions" as it's more clear.
