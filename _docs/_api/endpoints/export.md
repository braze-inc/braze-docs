---
nav_title: Export
article_title: Export Endpoints
search_tag: Endpoint
page_order: 2
description: "This reference article explains the Braze export endpoints, including prerequisites, what you can export, how data is delivered, and a full list of endpoints."
page_type: reference
---

# Export endpoints

With the export endpoints, you can access and export various details on your KPIs, app sessions, users, segments, campaigns, and Canvases. Make sure you know your [Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/), [API key]({{site.baseurl}}/api/api_key/), and [API identifier]({{site.baseurl}}/api/identifier_types/) when building your parameters and request bodies.

## Prerequisites

Before you begin, make sure you have the following:

| Requirement | Description |
| --- | --- |
| Braze REST API key | A REST API key with the appropriate export permissions for the endpoints you plan to call. API keys are scoped to specific endpoints, and permissions can't be changed after creation. For details, refer to [REST API key]({{site.baseurl}}/api/basics/#about-rest-api-keys). |
| Relevant identifiers | The identifiers for the data you want to export, such as a campaign ID, segment ID, or Canvas ID. You can find these on the Braze dashboard. For a full list, refer to [API identifier types]({{site.baseurl}}/api/identifier_types/). |
| Cloud storage credentials (optional) | If you're exporting large datasets, connect an [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), or [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/) bucket to have export files written directly to your storage. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
If you're a marketer or team member without API access, coordinate with a developer or admin in your organization to set up API keys and integrations.
{% endalert %}

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

## How export data is delivered

API exports return data in JSON format, unlike the CSV files you download from the dashboard. The delivery method depends on whether you have cloud storage connected:

- **Without cloud storage:** Braze writes the export files to its own S3 bucket and includes a temporary download URL in the API response. This URL expires after four hours, and the export is packaged as a compressed archive (ZIP or GZIP, depending on the `output_format` parameter) containing JSON files. Each line in the JSON files represents one data object.
- **With cloud storage connected:** Braze writes the export files directly to your configured bucket. The API response doesn't include a download URL. Files follow your own retention policies and are typically more reliable for large exports.

{% alert tip %}
"Cloud storage" means your own storage bucket (for example, Amazon S3, Microsoft Azure Blob Storage, or Google Cloud Storage). You can connect your bucket in **Partner Integrations** > **Technology Partners** so Braze can write export files directly to it.
{% endalert %}

For more details on export delivery and troubleshooting, refer to [Export troubleshooting]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).

## Export endpoints

The following table lists all export APIs available.

| Category | Method | Endpoint |
| --- | --- | --- |
| Campaigns | GET | [Campaign Analytics]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) |
| Campaigns | GET | [Campaign Details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) |
| Campaigns | GET | [Campaigns List]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) |
| Campaigns | GET | [Send Analytics]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) |
| Canvases | GET | [Canvas Data Series Analytics]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) |
| Canvases | GET | [Canvas Analytics Summary]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) |
| Canvases | GET | [Canvas Details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) |
| Canvases | GET | [Canvas List]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |
| Custom events | GET | [Custom Events]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) |
| Custom events | GET | [Custom Events List]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) |
| Custom events | GET | [Custom Event Analytics]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) |
| Custom attributes | GET | [Custom Attributes]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) |
| KPIs | GET | [KPIs for Daily New Users by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) |
| KPIs | GET | [KPIs for Daily Active Users by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |
| KPIs | GET | [KPIs for Monthly Active Users Over Last 30 Days]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) |
| KPIs | GET | [KPIs for Uninstalls by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) |
| Purchases | GET | [Product IDs List]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) |
| Purchases | GET | [Number of Purchases]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) |
| Purchases | GET | [Revenue Data by Time]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) |
| Segments | GET | [Segment List]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) |
| Segments | GET | [Segment Analytics]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) |
| Segments | GET | [Segment Details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) |
| Sessions | GET | [App Sessions Time-Series Data]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) |
| User data | POST | [User Data by Identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |
| User data | POST | [User Data by Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |
| User data | POST | [User Data by Global Control Group]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Related articles

For one-off exports from the dashboard, refer to these articles:

- [Export campaign data]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data/)
- [Export Canvas data]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/)
- [Export segment data to CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/)
