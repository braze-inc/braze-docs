---
nav_title: Know before you send
article_title: Know Before You Send
description: "After visiting our pre-launch guide, refer to this final list of checks or 'gotchas' for Content Cards, email, in-app messages, push, and SMS."
alias: /know_before_send/
page_order: 10.2
tool:
    - Campaigns
    - Canvas
---

# Know before you send: channels

Launch your campaigns and Canvases with confidence! Refer to this final list of checks or "gotchas" for Content Cards, email, in-app messages, push, and SMS.

{% alert note %}
While we provide an extensive list of resources to reference pre-send, each channel has individual nuances that continue to grow as we evolve our products. The checks listed below are helpful suggestions, and we recommend thoroughly testing your campaigns and large sends before sending. 
{% endalert %}

## General

#### Things to check
- [**API rate limits**](https://braze.com/resources/articles/whats-rate-limiting): Review the Braze API [rate limits]({{site.baseurl}}/api/api_limits/) for your workspaces to avoid running into errors. If you are looking to increase your rate limits (and are already batching requests), reach out to your customer success manager. Keep in mind that this process requires lead-time, so plan accordingly.
- [**Necessary frequency capping overrides**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): There are some campaigns, like transactional messages, that you will want to always reach the user, even if you have already reached their frequency cap (for example, a delivery notification). If you want a particular campaign to override frequency capping rules, you can set this up in the Braze dashboard when scheduling that campaign's delivery by toggling frequency capping off.

#### Things to know
- [**Global control groups**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group): If you are using a global control group, a percentage of users will not receive any campaigns or Canvases. (You can create exceptions with [exclusion settings]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)). To see a list of these users, export them via CSV or [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).
- [**Canvas rate limits**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): In a Canvas, the rate limit applies across the entire Canvas, not the individual steps. For example, if you were to set a 10,000 message per minute rate limit on a Canvas with multiple steps, it will still be limited to 10,000 messages because the limit will have been reached at the first step.
- **Frequency capping**: 
  - Frequency capping rules will be applied to push, email, SMS, and webhooks, but not to in-app messages and Content Cards.
  - Global frequency capping is scheduled based on the user's time zone and is calculated by calendar days, not 24-hour periods. For example, if you set up a frequency capping rule of sending no more than one campaign a day, a user may receive a message at 11 pm in their local time zone, and they would be eligible to receive another message an hour later.

{% alert tip %}
For further assistance with Canvas and campaign troubleshooting, be sure to contact Braze Support within 30 days of your issue's occurrence as we only have the last 30 days of diagnostic logs.
{% endalert %}

## Email

#### Things to check
- **Customer consent**: Before sending out your initial emails, it's important to get permission from your customers first. Refer to [Consent and address collection]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/) and our [Braze Acceptable Use Policy](https://www.braze.com/company/legal/aup) for more information.
- **Anticipated volume**: 2 million emails per day for a single IP is the general recommendation as long as that volume has been [properly warmed]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming). 
  - If you plan on consistently sending a higher volume than this, to avoid providers throttling receipt of emails resulting in a high amount of soft bounces, lowered deliverability rate, and a decreased IP reputation, consider using multiple IP addresses bundled into an IP pool. 
  - If you are looking to send in a shorter time frame only, we recommend looking into how quickly different providers accept mail to gauge the appropriate number of IPs to send from. 

#### Things to know
- **Sending volume factors**: Some factors that determine the capable sending volumes for an IP include:
  - Mailboxes: Large email providers can likely handle millions per day from a single IP, whereas a smaller regional mailbox provider or one with a smaller infrastructure might not be able to handle that amount.
  - Sender reputation: You may be able to send a larger volume per day from a single IP if the sender is ramped up to that volume and if their sender reputation is strong enough at each mailbox or domain they are sending to.
- **Best practices**: Review Braze [email best practices]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) and reach out to your Braze Account Team if you would like to learn more about deliverability services.

## Push

#### Things to check
- [**Opted-in/subscribed and push enabled**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/): For users to receive a push message from Braze, they need their subscription statuses to be either opted-in (iOS) or subscribed (Android) and `Push Enabled = True`. Note that Android 13 introduces a major change in how users manage apps that send push notifications. The Braze [Android 13 SDK upgrade guide]({{site.baseurl}}/developer_guide/platforms/android/android_13/) will continue to update as new Android 13 beta versions are released.

#### Things to know
- **Web push**: If you have Braze [Web SDK setup]({{site.baseurl}}/user_guide/message_building_by_channel/push/web), consider utilizing Web push to engage users. Web push works the same way app push notifications operate on your phone. For more information on composing a web push, check out [Creating a push notification]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).
- **Targeting a singular app**: Review the [differences in segmentation]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app) to target a singular app and its users.

## SMS

#### Things to check
- **Allotments and throughput**: Understand what SMS allotments are currently attached to your account (short code, long code, and similar) and [how much throughput that provides you]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) to confirm you have enough throughput to send in your desired time.
- **Estimate segment from SMS copy**: Test your SMS copy in the [SMS segment calculator]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy). Keep in mind that the number of SMS segments should be taken into account with your throughput capabilities. (Audience * SMS segments = Throughput needed). Refer to SMS FAQ on [avoiding overages]({{site.baseurl}}/sms_faq/).
- **SMS laws and regulations**: [Review SMS laws, regulations, and abuse prevention]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) to confirm that you are using the SMS services in compliance with all applicable laws. Make sure you should seek the advice of your legal counsel before sending.

#### Things to know
- **SMS message defaulting**: SMS messages are normally defaulted to be sent from the short code in the sender pool.
- **Alphanumeric sender ID**: Two-way messaging will no longer work if you use an alphanumeric sender ID; these are now one-way only.
- **Updated throughput in the US**: Throughput has changed in the US with US [A2P 10DLC registration](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). Note that we do not commit to any sending speed SLAs contractually due to multiple factors such as traffic congestion and carrier issues that may impact the actual delivery rates.
- **Subscription group**: To launch an SMS campaign through Braze, a subscription group must be selected. As well, to adhere to international [telecommunication compliance and guidelines]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), Braze will never send SMS to users that have not [subscribed to the selected subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group).

## WhatsApp

#### Things to know

- [**Best practices**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/): Review our suggested WhatsApp best practices.

## Banners

#### Things to check
- **Banner dimensions:** Build your Banners using a fixed dimension element and test them in the editor.
- **Priority:** If you’re launching multiple Banners, you can manually set the priority for how each banner is displayed.

#### Things to know
- **Liquid personalization:** Liquid personalization refreshes at every session start.
- **Placement and Banner ratio:** Each Banner placement can be used in up to 10 campaigns in a workspace.  
- **Clicks and impressions:** Clicks and impressions for Banners are tracked automatically with the SDK.
- **Limitations:**  Currently, the following features aren't supported: Canvas integration, API-triggered and action-based campaigns, Connected Content, promotion codes, user-controlled dismissals, and `catalog_items` using the [`:rerender` tag]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).
- **Testing:** To display the test Banner, the device you’re using must be able to receive foreground push notifications.
- **Custom HTML:** Leverage [JS bridge]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge) to log clicks when using custom HTML to define click actions, like links and buttons. Click actions are only logged automatically when using the pre-built components in the drag-and-drop editor.
- **Requesting Placements:** Up to 10 placements can be returned to the SDK once per session. Each placement will include the highest priority Banner a user is eligible for.

## Content Cards

#### Things to check
- **Content Card size**: Content Card message fields are limited to 2&nbsp;KB in pre-compression size, calculated by adding the byte-size length of the following fields: title, message, image URL, link text, link URLs, and key-value pairs. Messages that exceed this size will not be sent. Note that this does not include the size of the image but rather the length of the image URL.
- **Updating copy post-send**: After a card is sent, you will be unable to update the copy on that same card. Refer to [Updating sent cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards) to understand how you can approach this scenario.

#### Things to know
- **Active Content Card campaigns limit**: You can have up to 500 active Content Card campaigns. This count includes Content Cards sent with either [card creation]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) option.  
- [**Reporting terms**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): Review terms such as total impressions, unique impressions, and unique recipients as the definitions can sometimes cause confusion.
- **Content Card refresh**: By default, Braze refreshes Content Card requests as they sync at session start, on feed down swipe (mobile), and when the cards view is opened if the last refresh was over one minute ago.
- **Caching Content Cards**: Content Card caching options can be found in our [Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) and [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards) docs. 
- **Frequency capping**: Frequency capping does not apply to Content Cards.
- **Impressions**: Impressions are generally logged when a card is seen. For example, if you have a full inbox of Content Cards, an impression will not be logged until the user scrolls to the specific Content Card. There are some nuances between the Web, Android, and iOS platforms.  

## In-app messages

#### Things to know
- **In-app message triggering**: At the session start, the SDK requests that all eligible in-app messages be sent to the device along with its triggers, so if they perform the event during the session, they can receive the in-app message quickly and reliably.
- **Sent versus impressions**: For in-app messages, the concept of "sent" differs from the other available channels. To see an in-app message, a user has to start a session, be in the eligible audience, and perform the trigger. Because of this, we track "impressions" as it is more clear.
- **Triggering**: By default, in-app messages are triggered by events logged by the SDK. If you want to trigger in-app messages by server-sent events, you can also achieve this through these guides for [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift) and [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).
- [Canvas in-app messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options): These messages appear the first time that your user opens the app (triggered by the start session) after the scheduled message in the Canvas component has been sent to them.
- **Connected Content calls**: Using Connected Content allows you to send dynamic content in messages. When you send messages through a channel like in-app messages, this can create more simultaneous connections to your users’ devices (messages are sent one by one rather than in batches). To manage this, we recommend [rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) your messages.
