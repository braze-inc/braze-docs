---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "This article contains release notes for April 2018."
---
# April 2018

## Webhooks update on the way

In May, Braze will be implementing a security initiative for webhook redirects. Going forward, the webhook sender will not be able to follow those redirects. Instead, redirects will be treated as errors to prevent infinite redirect loops. Braze does not expect this to affect anyone, but if you have webhooks that redirect, we recommend revisiting and editing that campaign.

## CSV storage increased

Braze has updated the CSV X filter to include the 100 most recent CSVs a user was updated in, as opposed to the previous 10.

## Uninstall tracking on by default for android apps

The [Uninstall Tracking][94] function for all new Android apps will default to "on." All existing Android apps that have uninstall tracking turned off will now be changed to "on." Android uninstall tracking no longer sends push to the device, and no other updates or actions are required on your part.

## Updated and improved search functions

Braze has added tagging and better search functionality to Braze to improve your experience managing large-scale deployments of Braze while you search for [custom events and attributes][92], templates, and more.

## Push stories

[Create notifications][95] with multiple pages, an image, click behavior, and an optional title & subtitle. Just create a push message and select "Push Story" from the dropdown.

_Please note that you must update to the latest version of Android (version 2.2.0+) and iOS (version 3.2.0+) to use this feature._


## Inbox vision

You can now [preview your emails][96] based on your customer's platform, either via an overview page of thumbnails or a list view that includes a large screenshot and more specific analysis of any issues that may exist with the HTML rendering for each client. Talk to your Customer Success Manager or Account Manager for pricing and options.


[92]: {{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management
[94]: {{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking-for-campaigns
[95]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/#push-stories
[96]: {{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision
