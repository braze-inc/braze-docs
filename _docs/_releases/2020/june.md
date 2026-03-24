---
nav_title: June
page_order: 7
noindex: true
page_type: update
description: "This article contains release notes for June 2020."
---
# June 2020

## Retention Reports

Retention Reports now offer Range Retention for [campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/test_campaigns/retention_reports/) and [Canvases]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/). Range Retention measures how many users come back and perform a selected retention event during specific intervals of time. 

## User track API updates

The [`users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) now has a default rate of 50,000 API requests per minute for dashboard companies created after June 2, 2020. Existing companies created before this date and their workspaces will still be allowed unlimited API requests to the `users/track` endpoint.

 Braze is imposing this default on our most heavily used customer-facing endpoint as a step toward our stability and reliability goals for our API and infrastructure. The limit imposed is very liberal, and will affect very few dashboard companies and their regular operations. In the event that you need an increase to this limit, contact your customer success manager or our support team to request an increase.

