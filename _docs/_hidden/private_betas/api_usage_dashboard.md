---
nav_title: API Usage Dashboard
article_title: API Usage Dashboard
permalink: "/api_usage/"
hidden: true
description: "This article provides an overview of the API usage dashboard."
---

# API usage dashboard

> The API usage dashboard lets you monitor your incoming REST API traffic into Braze to understand your trends within your usage of our REST APIs and to troubleshoot any potential issues.

The default dashboard is a view of all incoming REST API requests for your workspace over the last day (24 hours). Depending on your use case, you can adjust the dashboard controls to filter or group traffic and also configure the time range of the dashboard.

![]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Summary statistics

- **Total requests:** The total number of requests sent to Braze for your current workspace, given the filters and controls applied to the dashboard.
- **Success rate:** The percentage of total requests where Braze issued a `2XX` success response.
- **Error rate:** The percentage of total requests where Braze issued a `4XX` or `5XX` error response.

## Dashboard controls

![]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filters

Apply filters to narrow the view of REST API traffic for your workspace. Available filters include:

- API endpoint
- API key
- Response code

### Group data

Group data into various data series to explore different patterns in your usage. Available grouping options are:

- Response codes (default)
- API endpoint
- API key
- Success and failure only

### Date

Adjust the date filter to show a smaller or greater time range as needed. Available date options include:

- Today (default)
- Custom
- Last 3 Hours
- Last 6 Hours
- Last 12 Hours
- Last 24 Hours
- Yesterday
- Last 7 Days
- Last 14 Days
- Last 30 Days
- Last Month to Date

{% alert note %}
The **Last 3 Hours** and **Last 6 Hours** options will show traffic by minutes. Larger time periods will show traffic by hours or days.
{% endalert %}

## Considerations

The API usage dashboard includes all REST API requests that Braze received and returned a `2XX`, `4XX`, or `5XX` response for. This includes Data Transformation outputs and Cloud Data Ingestion syncs. SDK traffic and User Update steps are not included in this dashboard.

Data shown in the dashboard may have up to a 15 minute delay in showing recent traffic. During periods of high usage, you can refresh the dashboard up to 4 times per minute. You may need to wait a few minutes before refreshing the dashboard again.
