---
nav_title: API Usage Dashboard
article_title: API Usage Dashboard
alias: "/api_usage/"
page_order: 3.5
description: "This article provides an overview of the API usage dashboard."
---

# API usage dashboard

> The API usage dashboard lets you monitor your incoming REST API traffic into Braze to understand your trends within your usage of our REST APIs and to troubleshoot any potential issues.

## About the API usage dashboard

To view your API usage dashboard, go to **Settings** > **APIs and Identifiers**, then select **Dashboard**.

The default dashboard is a view of all incoming REST API requests for your workspace over the last day (24 hours). Depending on your use case, you can adjust the dashboard controls to filter or group traffic and also configure the time range of the dashboard.

![API Usage Dashboard with 130 total requests, with a 70 percent success rate and 30 percent failure rate.]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Available metrics

The API usage dashboard includes the following statistics:

| Metric         | Description |
|----------------|-------------|
| Total requests | The total number of requests sent to Braze for your current workspace, given the filters and controls applied to the dashboard. |
| Success rate   | The percentage of total requests where Braze issued a `2XX` success response. |
| Error rate     | The percentage of total requests where Braze issued a `4XX` or `5XX` error response. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Using the dashboard

![Filters to apply to the dashboard, including: API key, endpoint, response codes, group data, and date.]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filters

Select **Filters** to apply filters to narrow the view of REST API traffic for your workspace, including:

- API key
- Endpoint
- Response code

### Group data

You can group data into various data series to explore different patterns in your usage, including:

- Response codes (default)
- API endpoint
- API key
- Success and failure only

### Date

Adjust the date filter to show a smaller or greater time range as needed. This includes:

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
The **Last 3 Hours** and **Last 6 Hours** options will show traffic by minutes. Larger time periods will show traffic every five minutes, hour or day.
{% endalert %}

## Considerations

The API usage dashboard includes all REST API requests that Braze received and returned a `2XX`, `4XX`, or `5XX` response for. This includes Data Transformation outputs and Cloud Data Ingestion syncs. SDK traffic and User Update steps are not included in this dashboard.

Data shown in the dashboard may have up to a short delay in showing recent traffic. During periods of high usage, you can refresh the dashboard up to 4 times per minute. You may need to wait a few minutes before refreshing the dashboard again.
