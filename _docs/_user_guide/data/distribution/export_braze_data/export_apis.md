---
nav_title: Export APIs
article_title: Export APIs
page_order: 8
page_type: reference
description: "This reference article covers the Braze export APIs, including what data you can export, prerequisites, how data is delivered, and when to use API exports instead of CSV downloads."
platform: API

---

# Export APIs

> The Braze export APIs let you programmatically export dashboard data as JSON. You can pull campaign analytics, user profiles, KPIs, and more through the [export endpoints]({{site.baseurl}}/api/endpoints/export/).

## What you can export

The following table summarizes the categories of data available through the export APIs.

| Category | What it includes | API reference |
| --- | --- | --- |
| Campaigns | Performance analytics, campaign details, campaign lists, and send analytics | [Campaign endpoints]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) |
| Canvases | Data series analytics, analytics summaries, Canvas details, and Canvas lists | [Canvas endpoints]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) |
| Segments | Segment lists, segment analytics, and segment details | [Segment endpoints]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) |
| User data | Full user profiles by identifier or by segment, and users by global control group | [User data endpoints]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |
| KPIs | Daily active users, monthly active users, daily new users, and uninstalls by date | [KPI endpoints]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |
| Sessions | App session time-series data | [Sessions endpoint]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) |
| Custom events | Event names, event lists, and event analytics over time | [Custom events endpoints]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) |
| Custom attributes | Attribute names | [Custom attributes endpoint]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) |
| Purchases | Revenue data by time, product ID lists, and purchase counts | [Purchase endpoints]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For the full list of endpoints with instructions and sample code, refer to [Export endpoints]({{site.baseurl}}/api/endpoints/export/).

## Prerequisites

To use the export APIs, you need:

- **A REST API key** with the appropriate export permissions for the endpoints you plan to call. API keys are scoped to specific endpoints and permissions can't be changed after creation. For details, refer to [REST API key]({{site.baseurl}}/api/basics#rest-api-key/).
- **The relevant identifiers** for the data you want to export, such as a campaign ID, segment ID, or Canvas ID. You can find these on the Braze dashboard. For a full list of identifier types, refer to [API identifier types]({{site.baseurl}}/api/identifier_types/).
- **Cloud storage credentials (optional):** If you're exporting large datasets, connect an [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), or [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/) bucket to have export files written directly to your storage.

{% alert note %}
If you're a marketer or team member without API access, coordinate with a developer or admin in your organization to set up API keys and integrations.
{% endalert %}

## How export data is delivered

API exports return data in JSON format, unlike the CSV files you download from the dashboard. The delivery method depends on whether you have cloud storage connected:

- **Without cloud storage:** Braze writes the export files to its own S3 bucket and includes a temporary download URL in the API response. This URL expires after four hours, and the export is packaged as a ZIP file containing JSON files. Each line in the JSON files represents one data object.
- **With cloud storage connected:** Braze writes the export files directly to your configured bucket. The API response doesn't include a download URL. Files follow your own retention policies and are typically more reliable for large exports.

For more details on export delivery and troubleshooting, refer to [Export troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).

## When to use export APIs instead of CSV downloads

Use the export APIs instead of CSV downloads from the dashboard when:

- **Your export is too large for the dashboard.** Dashboard CSV exports are limited to 500,000 rows. If you're exporting data on a segment with more than 500,000 users, use the export API, which has no limit on how much you can export.
- **You want to automate recurring reports.** Schedule API exports through an integration to pull data on a regular cadence without manual dashboard interaction.
- **You need to feed data into external tools.** Pull export data directly into BI tools, data warehouses, or other analytics platforms.
- **You need data not available as a dashboard CSV export.** Some data categories, including KPIs, revenue series, custom event analytics, and session data, are only available through the API.
- **You want to interact with the data programmatically.** Use the JSON output for custom processing, transformations, or integrations.

{% alert tip %}
For one-off exports of campaign, Canvas, or segment data from the dashboard, refer to [Export campaign data]({{site.baseurl}}/user_guide/data/export_braze_data/export_campaign_results_data/), [Export Canvas data]({{site.baseurl}}/user_guide/data/export_braze_data/export_canvas_data/), or [Export segment data to CSV]({{site.baseurl}}/user_guide/data/export_braze_data/segment_data_to_csv/).
{% endalert %}

