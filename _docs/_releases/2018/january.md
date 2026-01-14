---
nav_title: January
page_order: 12
noindex: true
page_type: update
description: "This article contains release notes for January 2018."
---
# January 2018

## CSS inlining

You can now toggle [CSS inlining]({{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining) on or off for individual email messages by going to your **Email Settings**.

## New segment filters

You can now create segments using the following filters:
- Received Canvas Step
- Opened/Clicked Canvas Step
- Last Received Specific Canvas Step

{% alert update %}
As of March 2019, `Received Canvas Step` has been renamed to `Received Message from Canvas Step`, and `Last Received Specific Canvas Step` has been renamed to `Last Received Message from Specific Canvas Step`.
{% endalert %}

## Exporting users using device ID

This endpoint now accepts a device identifier as a parameter, which lets you to [export anonymous user profiles]({{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint).

You can use the device ID to export all user profiles on that device.

## Engagement Reports update

Additional stats, like **push open rate** and **conversion rate**, are now available in [Engagement Reports]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports).

## Apple push certificates: Using .p8 files

You can now use a [p8 file]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens) when uploading an Apple Push Certificate, ensuring that your iOS push credentials will never expire.


