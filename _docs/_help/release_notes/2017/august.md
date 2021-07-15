---
nav_title: August
page_order: 5
no_index: true
page_type: update
description: "This article contains release notes for August 2017."
---

# August 2017

## Update to Push Action Buttons

We added support for [push action buttons][70] to our REST API messaging endpoints.

## Update to Liquid Templating

You can now [personalize a message][69] based on:
- The device it was sent to,
- Device ID,
- Carrier,
- IDFA,
- Model,
- OS, and
- Platform

## API-Triggered Canvas

You can now trigger a [Canvas][68] via API endpoints (send, schedule, update, delete) that match the existing ones for campaigns, allowing you to further automate and optimize your marketing.

## Web Push Action Buttons

We’ve added support for push action buttons on the web SDK for Chrome, allowing you increase your engagement by giving your users contextual choices that simplify their busy lives. Learn more about best practices for push notifications [here][66].

## New API Endpoints

We’ve exposed new API endpoints, /email/hard_bounces, that lets you pull hard bounces by email address or in a given date range, and /messages/scheduled_broadcasts, that lets you pull the next time that scheduled campaigns and scheduled-entry Canvases will begin. These new endpoints allow you for further customization and optimization of your campaigns. Learn more about our API endpoints [here][65].

## Geofences

We’ve added a new feature, Geofences, that allows you to trigger messages in real-time when customers enter and exit defined geographical areas, enabling personalized, relevant communication with your customers. Learn more about location marketing in [Academy][64].

## Update to Email Editor

We’ve added dynamic autocompleting to our new email editor, so you can now autocomplete with your customers’ actual custom attributes and events when using Liquid, making your life easier. Learn more about email best practices in [Academy][63].

## Update to Date Filters

We’ve added a “never” date filter so you can target customers who have never received or interacted with one of your message, enabling you to have clean customer lists and ensure email deliverability. Learn more about filters [here][62].

## Update to Canvas

We’ve added percentages to the top of each Canvas variant so now, you can see which variants are performing better at a glance. Learn more about Canvas [here][61].

## Canvas with Intelligent Selection

Canvas now has Intelligent Selection, allowing you to test your Canvases with more efficiency. Learn more about our Intelligence Suite [here][60].

## Update to Email Display Names

We’ve added support of special UTF-8 characters in email display names, so you can create even more personalized emails for your customers. Learn more about email best practices [here][67].

## Engagement Reports CSV Aggregation

Now, you can receive consolidated data for every campaign and every Canvas in two separate files regardless of how many campaigns or Canvases are selected, allowing you to have all the data you need, when you need it. Learn more about Engagement Reports [here][59].

> Update: As noted in our [September 2017 release notes]({{site.baseurl}}/help/release_notes/2017/august/#september-2017), you can now aggregate data from a specific period of time as well as schedule exports to run on a recurring basis.



[59]: {{site.baseurl}}/user_guide/data_and_analytics/engagement_reports/#creating-a-new-report
[60]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[61]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters
[63]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[64]: {{site.baseurl}}/developer_guide/platform_integration_guides/fireos/advanced_use_cases/locations_and_geofences/#locations--geofences
[65]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[66]: {{site.baseurl}}/help/best_practices/push/
[67]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[68]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[69]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[70]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
