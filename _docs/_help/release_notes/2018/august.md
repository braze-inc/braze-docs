---
nav_title: August
page_order: 6
noindex: true
page_type: update
description: "This article contains release notes for August 2018."
---
# August 2018

## iOS 12 notification groups

The recent iOS 12 release supports grouping notifications (similar to Android Notification Channels) for applications. [Braze allows you to utilize this grouping feature in iOS this using our message composer.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## Push story triggering

You can now retarget users based on specific page clicks on Push Story slides. Use the additional filter for **Interacted with Campaign**.

## S3 and Azure data events from anonymous users

Customers exporting data to Amazon S3 and Microsoft Azure can now include events from anonymous users. This functionality will default to on for all newly created integrations, but will remain off for for all existing integrations. If you have any questions, reach out to your account manager or open a [support ticket]({{site.baseurl}}/braze_support/).

## Mixpanel Cohorts integration

Customers of both Braze and Mixpanel can now integrate and [send Mixpanel Cohorts to Braze as segment filters]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import). You can either set up a one-time manual export or a dynamic export every two hours. Each updated user will count as a data point, but Mixpanel only sends changes since the last sync.

