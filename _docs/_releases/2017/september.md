---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "This article contains release notes for September 2017."
---

# September 2017

## New functionality for Engagement Reports

You can now use [Engagement Reports]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports) to aggregate metrics for a campaign across specific periods of time. For example, you can export the total number of opens from a quarter, or the total number of clicks from the entire lifetime of a campaign or Canvas. All you have to do is:
- Select a time frame from which to export data,
- Schedule an Engagement Report that sends to one or more recipients on a regular basis, and
- Add campaigns and Canvases to your report based on their tags.

## Updates to user profile page

The [User Profile Page]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search) has been updated.

## Web push notifications that require user action to dismiss

You can now set up message close behavior for Chrome web pushes that requires the recipient to interact with the message in order for it to dismiss. This feature requires Web SDK version 1.6.13 or higher.

## Email preheaders

When creating an email message within Braze, you can now easily insert a preheader in the **Sending Info** section.

## New API endpoint for raw event export

We've added a new [API endpoint]({{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges), /raw_data/status, that lets you query to see if a given day has been loaded into the Raw Event Export. You can use it to check if a particular day's raw data is available, to help with debugging and automation.



