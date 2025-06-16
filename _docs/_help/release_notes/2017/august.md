---
nav_title: August
page_order: 5
noindex: true
page_type: update
description: "This article contains release notes for August 2017."
---

# August 2017

## Update to push action buttons

We added support for [push action buttons]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons) to our REST API messaging endpoints.

## Update to Liquid templating

You can now [personalize a message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) based on:
- The device it was sent to,
- Device ID,
- Carrier,
- IDFA,
- Model,
- OS, and
- Platform

## API-triggered Canvas

You can now trigger a [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) via API endpoints (send, schedule, update, delete) that match the existing ones for campaigns, allowing you to further automate and optimize your marketing.

## Web push action buttons

We've added support for push action buttons on the web SDK for Chrome, allowing you increase your engagement by giving your users contextual choices that simplify their busy lives. Check out the [best practices for push notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

## New API endpoints

We've exposed new API endpoints, /email/hard_bounces, that lets you pull hard bounces by email address or in a given date range, and /messages/scheduled_broadcasts, that lets you pull the next time that scheduled campaigns and scheduled-entry Canvases will begin. These new endpoints allow you for further customization and optimization of your campaigns. Learn more about our [API endpoints]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Geofences

We've added a new feature, geofences, that allows you to trigger messages in real-time when customers enter and exit defined geographical areas, enabling personalized, relevant communication with your customers. Learn more about [location marketing]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/).

## Update to email editor

We've added dynamic autocompleting to our new email editor, so you can now autocomplete with your customers' actual custom attributes and events when using Liquid, making your life easier. Learn more about [email best practices]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices).

## Update to date filters

We've added a "never" date filter so you can target customers who have never received or interacted with one of your message, enabling you to have clean customer lists and ensure email deliverability. Learn more about [filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Update to Canvas

We've added percentages to the top of each Canvas variant so now, you can see which variants are performing better at a glance. Learn more about [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

## Canvas with Intelligent Selection

Canvas now has Intelligent Selection, allowing you to test your Canvases with more efficiency. Learn more about our [Intelligence Suite]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

## Update to email display names

We've added support of special UTF-8 characters in email display names, so you can create even more personalized emails for your customers. Learn more about [email best practices]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices).

## Engagement Reports CSV aggregation

Now, you can receive consolidated data for every campaign and every Canvas in two separate files regardless of how many campaigns or Canvases are selected, allowing you to have all the data you need, when you need it. Learn more about [Engagement Reports]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/).

> As noted in our [September 2017 release notes]({{site.baseurl}}/help/release_notes/2017/september/), you can now aggregate data from a specific period of time as well as schedule exports to run on a recurring basis.


