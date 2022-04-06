---
nav_title: Before You Send
description: "After visiting out pre-launch guide, refer to this final list of checks or 'gotchas' for Content Cards, email, in-app messages, push, and SMS."
permalink: /know_before_send/
hidden: true
---

# Know before you send - a channels guide

Launch your campaigns and Canvases with confidence! After visiting our [pre-launch guide](https://labplaybooks.braze.com/canvas-playbooks#/subpage/b2rj8), refer to this final list of checks or "gotchas" for Content Cards, email, in-app messages, push, and SMS.

{% alert note %}
While we provide an extensive list of resources for customers to reference pre-send, each channel has individual nuances that continue to grow as we evolve our products. The checks listed below are helpful suggestions and we recommend thoroughly testing your campaigns and large sends before sending. 
{% endalert %}

## General

#### Things to check for
- [**API rate limits**](https://braze.com/resources/articles/whats-rate-limiting): Review the Braze API [rate limits]({{site.baseurl}}/api/api_limits/) for each endpoint to avoid running into errors. If you are looking to increase your rate limits (and are already batching requests), reach out to your customer success manager. Keep in mind that this process requires lead-time, so plan accordingly.
- [**Necessary frequency capping overrides**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): There are some campaigns, like transactional messages, that you will want to always reach the user, even if you have already reached their frequency cap (for example, a delivery notification). If you want a particular campaign to override frequency capping rules, you can set this up in the Braze dashboard when scheduling that campaign's delivery by toggling frequency capping off.

#### Things to know about
- [**Global control groups**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group): If you are using a global control group, a percentage of users will not recieve any campaigns or Canvases. If you would like to see a list of these users, export them via CSV or [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).
- [**Canvas rate limits**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): In a Canvas, the rate limit applies across the entire Canvas, not the individual steps. For example, if you were to set a 10,000 message/minute rate limit on a Canvas with multiple steps, it will still be limited to 10,000 messages because the limit will have been reached at the first step.


## Email

#### Things to check for:
- **Customer consent**: Before sending out your initial emails, it’s important to get permission from your customers first. Refer to [Consent and address collection]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/) and our [Braze Acceptable Use Policy]({{site.baseurl}}/company/legal/aup) for more information.
- **Anticipated volume**: 2 million emails per day for a single IP is the general recommendation as long as that volume has been [properly warmed]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming). 
  - If you plan on consistently sending a higher volume than this, to avoid providers throttling receipt of emails resulting in a high amount of soft bounces, lowered deliverability rate, and a decreased IP reputation, consider using multiple IP addresses bundled into an IP pool. 
  - If you are looking to send in a shorter time frame only, we recommend looking into how quickly different providers accept mail to gauge the appropriate number of IPs to send from. 

#### Things to know about:
- **Sending volume factors**: Some factors that determine the capable sending volumes for an IP include:
  - Mailboxes: Large email providers can likely handle millions per day from a single IP, whereas a smaller regional mailbox provider or one with a smaller infrastructure might not be able to handle that amount.
  - Sender reputation: You may be able to send a larger volume per day from a single IP if the sender is ramped up to that volume and if their sender reputation is strong enough at each mailbox or domain they are sending to.

## Push

#### Things to check for:
- [**Opted-in/subscribed and push enabled**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/): In order for users to recieve a push message from Braze, they need their subscription statuses to be either opted-in (iOS) or subscribed (Android) and `Push Enabled = True`. 

#### Things to know about:
- **Expected throughput**: Braze's typical throughput for push is around 20,000 personalized messages per second, 1.2 million per minute, or 72 million per hour. Note that we do not commit to any sending speed SLAs contractually. Refer to [Building Braze job queues resiliency](https://braze.com/perspectives/article/building-braze-job-queues-resiliency) on how we ensure this resilience.
- **Sending speed factors**: The use of Connected Content and Liquid personalization may influence sending speeds among other factors.<br><br>


## SMS

#### Things to check for:
- **Allotments and throughput**: Understand what SMS allotments are currently attached to your account (short code, long code, etc.) and [how much throughput that provides you]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/short_and_long_codes/) to ensure you have enough throughput to send in your desired time.
- **Estimate segment from SMS copy**: Test your SMS copy in the [SMS segment calculator]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy). Keep in mind that the number of SMS segments should be taken into account with your throughput capabilities. (Audience * SMS segments = Throughput needed). Refer to SMS FAQs on [avoiding overages]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/#how-can-i-avoid-overages).
- **SMS laws and regulations**: [Review SMS laws, regulations and abuse prevention]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) to ensure that you are using the SMS services in compliance with all applicable laws. Make sure you should seek the advice of your legal counsel before sending.

#### Things to know about:
- **SMS message defaulting**: SMS messages are normally defaulted to be sent from the short code in the sender pool.
- **Alphanumeric sender ID**: Two-way messaging will no longer work if you use an alphanumeric sender ID, these are now one-way only.
- **Updated throughput in the US**: Throughput has changed in the US with US [A2P 10DLC registration](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). Note that we do not commit to any sending speed SLAs contractually due to multiple factors such as traffic congestion, carrier issues, etc. that may impact the actual delivery rates.

## Content Cards

#### Things to check for:
- **Content Card size**: Content Card message fields are limited to 2KB in pre-compression size, calculated by adding the byte-size length of the following fields: title, message, image URL, link text, link URLs, and key-value pairs. Messages that exceed this size will not be sent. Note that this does not include the size of the image, but rather the length of the image URL.
- **Updating copy post-send**: Once a card is sent, you will be unable to update the copy. You will instead, need to remove the original card and send down a new card with any updates.

#### Things to know about:
- **Eligible Content Card limits**: Each user is eligible to receive up to 100 non-expired and non-dismissed Content Cards (100 across all feeds, not per feed). As a user becomes eligible for more than 100 cards, Braze will begin to remove older cards from their feed, even if they were unread.
- [**Reporting terms**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): Review terms such as total impressions, unique impressions, and unique recipients as the definitions can sometimes cause confusion.
- **Content Card refresh**: By default, Braze refreshes Content Card requests as they sync at session start, on feed down swipe (mobile), and when the cards view is shown if the last refresh was over one minute ago.
- **Caching Content Cards**: Content Card caching options can be found in our [Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/#customizing-card-rendering-for-android) and [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards) docs. 
- **Frequency capping**: Frequency capping does not apply to Content Cards.
- **Impressions**: Impressions are generally logged once a card is seen. There are some nuances to this between the Web, Android, and iOS platforms. 

## In-app messages

#### Things to know about:
- **In-app message triggering**: At the session start, the SDK requests that all eligible in-app messages be sent to the device along with its triggers, so if they perform the event during the session, they can receive the in-app message quickly and reliably. Due to this, in-app messages cannot be triggered by custom events in Canvas.
- **Sent vs. impressions**: For in-app messages, the concept of "sent" differs from the other available channels. To see an in-app message, a user has to start a session, be in the eligible audience, and then perform the trigger. Because of this, we track "impressions" as it is more clear. 
