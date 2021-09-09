---
nav_title: August
page_order: 6
noindex: true
page_type: update
description: "This article contains release notes for August 2018."
---
# August 2018

## iOS 12 Notification Groups

The recent iOS 12 release supports grouping notifications (similar to Android Notification Channels) for applications. [Braze allows you to utilize this grouping feature in iOS this using our message composer.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## Push Story Triggering

You can now retarget users based on specific page clicks on push story slides. Use the additional filter for __Interacted with Campaign__.

## S3 and Azure Data Events from Anonymous Users

Customers exporting data to Amazon S3 and Microsoft Azure can now include events from anonymous users. This functionality will default to on for all newly created integrations, but will remain off for for all existing integrations. If you have any questions, reach out to your account manager or [open a support ticket][support].

## Mixpanel Cohorts Integration

Customers of both Braze and Mixpanel can now integrate and [send Mixpanel Cohorts to Braze as segment filters]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import). You can either set up a one-time manual export or a dynamic export every two hours. Each updated user will count as a data point, but Mixpanel only sends changes since the last sync.

[support]: {{site.baseurl}}/support_contact/
