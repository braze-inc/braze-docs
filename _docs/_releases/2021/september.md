---
nav_title: September
page_order: 3
noindex: true
page_type: update
description: "This article contains release notes for September 2021."
---

# September 2021

## iOS 15

### Apple Mail Privacy Protection 

Apple's Mail Privacy Protection (MPP) is a privacy update that will be available for users of the Apple Mail app on iOS 15, iPadOS 15, macOS Monterey, and watchOS 8, released in mid-September. For users who opt-in to MPP, emails will now be preloaded using proxy servers, caching images and hindering the ability to leverage tracking pixels for metrics like [open tracking]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#open-tracking-pixel). To learn more about MPP and issues regarding email deliverability metrics and issues with pre-existing campaigns and Canvases that trigger based on these metrics, visit our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/).

### Push features

iOS 15 introduced new notification features to help users stay focused and avoid frequent interruptions throughout the day. We're excited to offer support for these new features, including [Interruption Levels and Relevance Scores]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/).

## Contact Cards

Contact Cards are a standardized file format for sending business and contact information that can be easily imported into address books or contact books. You can now upload and create Contact Cards for your SMS and MMS messages. To read more about how to build Contact Cards in our built-in Contact Card Generator, visit our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/).

## Default Content Cards customization

You can create your own Content Cards interface by extending `ABKContentCardsTableViewController` to customize all UI elements and Content Cards behavior. To read more about how to customize the Content Cards Feed, visit our [documentation]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/). 

## API rate limits

[Rate limits]({{site.baseurl}}/api/basics/#api-limits/) will apply to all customers onboarded after September 16, 2021. 

## Updates to Android and FireOS developer guides

Android and FireOS developer guides have merged into one location. Dedicated FireOS articles will be available in this [new Android section]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Updates to Funnel and Retention Reports

[Funnel Reports]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) and [Retention Reports]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) are now available for SMS campaigns.
