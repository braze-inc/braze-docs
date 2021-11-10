---
nav_title: June
page_order: 7
noindex: true
page_type: update
description: "This article contains release notes for June 2020."
---
# June 2020

## Retention Reports

Retention Reports now offer Range Retention - Range Retention measures how many users come back and perform a selected retention event during specific intervals of time. To read more about Range Retention and Retention Reports, visit out [Canvas][1] and [Campaign][2] docs. 

## User track API updates

The [users/track][3] endpoint now has a default rate of 50,000 API requests per minute for dashboard companies created after June 2, 2020. Existing companies created before this date and their app groups will still be allowed unlimited API requests to the users/track endpoint.

Braze is imposing this default on our most heavily used customer-facing endpoint as a step toward our stability and reliability goals for our API and infrastructure. The limit imposed is very liberal, and will affect very few dashboard companies and their regular operations. In the event that you need an increase to this limit, please reach out to your Customer Success Manager or our support team to request an increase.

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
