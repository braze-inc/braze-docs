---
nav_title: January
page_order: 12
noindex: true
page_type: update
description: "This article contains release notes for January 2018."
---

# January 2018

## CSS inlining

You can now toggle [CSS Inlining][84] on or off for individual email messages - do this from [your Email Settings page][83].

## New segment filters

You can now create segments using the following filters:
- Received Canvas Step
- Opened/ Clicked Canvas Step
- Last Received Specific Canvas Step

{% alert update %}
As of March 2019, `Received Canvas Step` has been renamed to `Received Message from Canvas Step`, and `Last Received Specific Canvas Step` has been renamed to `Last Received Message from Specific Canvas Step`.
{% endalert %}

## Exporting users using device ID

This endpoint now accepts a device identifier as a parameter, which lets you to [export profiles of anonymous users][82].

You can use Device ID to export all user profiles on that device.

## Engagement Reports update

Additional stats, like **push open rate** and **conversion rate**, are [now available in reports][81].

## Apple push certificates: Using .p8 files

You can now use a [.p8 file][80] when uploading an Apple Push Certificate - ensuring that your iOS push credentials will never expire.


[80]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens
[81]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[82]: {{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint
[83]: https://dashboard-01.braze.com/app_settings/app_settings/email/
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining
