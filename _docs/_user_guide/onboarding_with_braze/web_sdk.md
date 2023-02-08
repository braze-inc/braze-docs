---
nav_title: SDK Overview for Marketers
article_title: SDK Overview for Marketers
page_order: 3
page_type: reference
description: "This onboarding reference article covers the basics of the Braze SDK."

---

# SDK overview for marketers

The Braze SDK makes it easy to collect session data, identify users, and record purchases and custom events through your website or app. You can also use the SDK to engage with your users by sending in-app messages and push notifications directly from the Braze dashboard.

## What is an SDK?
The Braze SDK (Software Development Kit) is how we send and get information to and from your app or site. 

## Implementation

Your Engineering team will do the work needed to integrate your websites and apps with the Braze SDK. Your developers are, essentially, tying our apps together so that information and actions flow between them. Learn more about the steps that your Marketing and Engineering teams will need to think through together in our [implementation article][4]. 

## Data aggregation

The SDK collects a default set of data, making it easy to see key metrics for your app and user base. You will group similar apps into a single app group on your dashboard. For example, you will group the iOS and Android versions of your app into the same app group, allowing you to see the collected data from users across both platforms. This gives you a more complete view of your users across web and mobile channels. See the article on the [Overview page][3] for more information.

## In-app messaging

The SDK makes it easy to compose and send in-app messages to directly engage with users. You can choose to send slideup, modal, or full-screen messages based on your campaign strategy. For more information on composing an in-app message, see our page on [creating an in-app message][8].

## Push notifications

![Push displayed on a web browser][11]{: style="float:right;max-width:60%;margin-left:20px;border:0;"}

Push notifications are another great option to engage with your users, and are especially useful to handle time-sensitive calls to action. Mobile push notifications appear on your users' device, and web push notifications appear even when your site is not open. For specifics on using push notifications, see our [push notification article][5].

![System notification requesting push notification permissions][12]

Users of your website or app need to opt-in to receive push notifications. See [push priming][13] for more details. 

## Segmentation and delivery rules

By default, a campaign containing in-app messages will be sent to all versions of the app in that app group. For example, the message will send to both web and mobile users. To send an in-app message exclusively to web or mobile, you will need to segment your campaign accordingly, which is supported by default through the Braze SDK. 

You can create a segment of your web users by selecting only your website’s app icon in the **Apps Used** section of a segment.

![Segment Details page with web app selected][10]

This will allow you to target users based on their behavior in an intelligent way. If you wanted to target web users to encourage them to download your mobile app, you’d create this segment as your target audience. If you wanted to send a messaging campaign that included a mobile in-app message but not a web message, you would simply uncheck your website’s icon in your segment.

[3]: {{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/
[4]: {{site.baseurl}}/user_guide/onboarding_with_braze/integration/#the-technical-side-of-the-integration-process
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/about/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[7]: {% image_buster /assets/img_archive/app_group_list.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[10]: {% image_buster /assets/img_archive/web-users-segment.png %}
[11]: {% image_buster /assets/img_archive/web_push_macbook.png %}
[12]: {% image_buster /assets/img_archive/web_push_prompt.png %}
[13]: {{site.baseurl}}user_guide/message_building_by_channel/push/push_primer_messages/