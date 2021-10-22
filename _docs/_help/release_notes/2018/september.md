---
nav_title: September
page_order: 5
noindex: true
page_type: update
description: "This article contains release notes for September 2018."
---
# September 2018

## iOS 12 notification groups: Additional abilities

You can now access [Apple's Notification Group features]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) using Braze! You can add Summary Arguments and Groups, utilize Critical Alerts, filter for Provisionally Authenticated users, and view Provisionally Authenticated status on user profiles.

## Quiet time

Customers can now specify [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (the time during which your messages will not send) for Canvas. Just go to your __Canvas Send Settings__ and check "Enable Quiet Hours". Then, select your Quiet Hours in your user's local time and what action will follow if the message triggers inside of those Quiet Hours.

Campaigns now also use Quiet Time instead of “send this message during a specific portion of the day”.

## Adjust customers

Braze Customers using [Adjust]({{site.baseurl}}/partners/advertising_technologies/attribution/adjust/) are now able to see their Braze API Key and Braze instance URL, which they will then use in the Adjust platform to integrate.

## Not in segment filter

Customers can now create a segment out of users who are [not included in a certain segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting).

## Canvas recipient CSV exports

Customers can now [export data on the users that have entered a Canvas]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_canvas_data/). The CSV generated will be similar to the Campaign CSV.

## Provisionally authorized iOS 12 segment filter

A [segment filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) that allows you to find users who are provisionally authorized on iOS 12 for a given app has been added.

## In-app message image uploader

The image uploader for in-app messages has moved from the design (paintbrush) panel to the compose (pencil) panel.

## Read-only permissions on User Profile page

Prior to this release, customers were able to change the subscription status and email address in the user profile with [read-only permission]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). We renamed the `import_user` permission to `import_and_update_user` permission and restricted edit access to subscription status and email address. Now when a developer is read-only impersonating or lacks this permission, they cannot change the subscription status or email address.
