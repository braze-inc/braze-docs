---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "This article contains release notes for April 2017."
---

# April 2017

## HTML in-browser messages

We now support interactive in-browser message types including custom HTML and email capture formats, enabling you to reach your customers wherever they are. Learn more about [in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Personalized in-app message with connected content

We've added {% raw %} {%connected_content%} {% endraw %} blocks in triggered in-app messages which allows you to add rich personalization by inserting any information accessible via API directly into your messages. Now, you can use Connected Content inside your app in addition to your push, email and webhooks. Learn more about [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/).

## Improved navigation for News Feed cards

We've improved the UI for building News Feed cards, making it easier for you to navigate and create your campaigns. Learn more about [News Feed cards]({{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards).

## Improved preview for iOS rich notifications

Our preview notifications on iOS now display rich notifications giving you a clear view of exactly what you are sending out to your customers, down to the font size. Learn more about [iOS rich notifications]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications).

## Added "Influenced Opens" to push statistics

We've added "Influenced Opens" to our list of standard campaign and Canvas statistics offered in Braze, making it easier to know your campaigns breakdown of Influenced, Direct and Total Opens. Learn more about [Influenced Opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/).

## Upgrade to internal groups

You can now create multiple Internal Groups and assign properties indicating whether the group will be used for SDK logging, REST API logging, or message content testing. Learn more about [event user logs]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab).

> Update: Internal Groups can also be used to [send seed emails]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups).

## New options for web URLs

You now have the option of opening web URLs in an external web browser for push messages, in-app and in-browser messages, and News Feed cards. The "Deep Link into App" action is also now compatible with HTTP/HTTPS deep links. If using a partner like Branch or Apple's Universal Links, you'll require SDK customization. Learn more about [deep linking]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

## New "Performed Conversion" event Canvas

We've added a new "Performed Conversion" event and an "In Canvas Control" filter for improved retargeting options. Learn more about using [retargeting filters]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns).



