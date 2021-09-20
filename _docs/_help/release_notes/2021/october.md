---
nav_title: October
page_order: 3
noindex: true
page_type: update
description: "This article contains release notes for October 2021."
---

# October 2021

## iOS 15
### Apple Mail Privacy Protection
Apple’s Mail Privacy Protection (MPP) is a privacy update that will be available for users of the Apple Mail app on iOS 15, iPadOS 15, macOS Monterey, and watchOS 8, released in mid-September. For users who opt-in to MPP, emails will now be preloaded using proxy servers, caching images and hindering the ability to leverage tracking pixels for metrics like [open tracking]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#email-open-tracking-pixel/). To learn more about MPP and issues regarding email deliverability metrics and issues with pre-existing campaigns and Canvases that trigger based on these metrics, visit our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/mpp/).

### Push Features
iOS 15 introduced new notification features to help users stay focused and avoid frequent interruptions throughout the day. We're excited to offer support for these new features, including [Interruption Levels and Relevance Scores]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/).

## Contact Cards
Contact Cards are a standardized file format for sending business and contact information that can be easily imported into address books or contact books. You can now upload and create Contact Cards for your SMS and MMS messages. To read more about how to build Contact Cards in our built-in Contact Card Generator, visit our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/).

## Out-of-the-Box Content Cards Customization
You can create your own Content Cards interface by extending `ABKContentCardsTableViewController` to customize all UI elements and Content Cards behavior. To read more about how to customize the Content Cards Feed, visit our [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/#customizing-the-content-cards-feed/). 

## Canvas Experiment Steps
With Experiment Steps, you can now track path performance to make informed decisions about your Canvas journey. Experiment Steps allow you to test multiple Canvas paths against each other and a control group at any point in the user journey. To learn more, visit [Experiment Steps]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).

## API Rate Limits
[Rate limits]({{site.baseurl}}/api/basics/#api-limits/) will apply to all customers onboarded after September 16, 2021. 

## Updates to Android and FireOS Developer Guides
Android and FireOS developer guides have merged into one location. Dedicated FireOS articles will be available in this [new Android section]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/).

## Updates to Funnel and Retention Reports
[Funnel Reports]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/) and [Retention Reports]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/) are now available for SMS campaigns.
