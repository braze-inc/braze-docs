---
nav_title: September
page_order: 4

page_type: update
description: "This article contains release notes for September 2017."
---

# September 2017

## New Functionality for Engagement Reports

You can now use [Engagement Reports][72] to aggregate metrics for a campaign across specific periods of time. For example, you can export the total number of opens from a quarter, or the total number of clicks from the entire lifetime of a Campaign or Canvas. All you have to do is:
- Select a time frame from which to export data,
- Schedule an Engagement Report that sends to one or more recipients on a regular basis, and
- Add Campaigns and Canvases to your report based on their tags.

## Updates to User Profile Page

The [User Profile Page][73] has been updated.

## Web Push Notifications That Require User Action to Dismiss

You can now set up message close behavior for Chrome web pushes that requires the recipient to interact with the message in order for it to dismiss. This feature requires Web SDK version 1.6.13 or higher.

## Email Preheaders

When creating an email message within Braze, you can now easily insert a preheader in the "Sending Info" section.

## New API Endpoint for Raw Event Export

We've added a new [API endpoint][71], /raw_data/status, that lets you query to see if a given day has been loaded into the Raw Event Export. You can use it to check if a particular day's raw data is available, to help with debugging and automation.



[71]: {{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges
[72]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[73]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
