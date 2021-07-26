---
nav_title: April
page_order: 9
no_index: true
page_type: update
description: "This article contains release notes for April 2017."
---

# April 2017

## HTML In Browser Messages
We now support interactive in-browser message types including custom HTML and email capture formats, enabling you to reach your customers wherever they are. Learn more about in-app messages [here][48].

## Personalized In-App Message with Connected Content

We’ve added {% raw %} {%connected_content%} {% endraw %} blocks in triggered in-app messages which allows you to add rich personalization by inserting any information accessible via API directly into your messages. Now, you can use Connected Content inside your app in addition to your push, email and webhooks. Learn more about Connected Content [here][34].

## Improved Navigation for News Feed cards
We’ve improved the UI for building News Feed cards, making it easier for you to navigate and create your campaigns. Learn more about News Feed cards [here][33].

## Improved Preview for iOS Rich Notifications
Our preview notifications on iOS now display Rich notifications giving you a clear view of exactly what you are sending out to your customers, down to the font size. Learn more about iOS Rich notifications [here][32].

## Added “Influenced Opens” to Push Statistics
We’ve added “Influenced Opens” to our list of standard campaign and Canvas statistics offered in Braze, making it easier to know your campaigns breakdown of Influenced, Direct and Total Opens. Learn more about Influenced Opens [here][31].

## Upgrade to Internal Groups

You can now create multiple Internal Groups and assign properties indicating whether the group will be used for SDK logging, REST API logging, or message content testing. Learn more about event user logs and testing [here][30].

> Update: Internal Groups can also be used to [send seed emails]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups).

## New Options for Web URLs

You now have the option of opening Web URLs in an external web browser for push messages, in-app and in-browser messages, and News Feed cards. The "Deep Link into App" action is also now compatible with HTTP/HTTPs deep links. If using a partner like Branch or Apple's Universal Links, you'll require SDK customization. Learn more about deep linking [here][29].

## New "Perform Conversion" Event Canvas

We've added a new "Performed Conversion" event and an "In Canvas Control" filter for improved retargeting options. Learn more about using retargeting filters [here][28].



[28]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
[29]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[30]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[31]: {{site.baseurl}}/user_guide/data_and_analytics/influenced_opens/#influenced-opens
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[33]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards
[34]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[48]: {{site.baseurl}}/help/best_practices/in-app_messages/
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
