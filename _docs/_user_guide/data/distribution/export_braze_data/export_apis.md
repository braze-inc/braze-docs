---
nav_title: Export APIs
article_title: Export APIs
page_order: 5
page_type: reference
description: "This reference article helps you decide when to use export APIs instead of CSV downloads from the dashboard."
platform: API

---

# Export APIs

> This page helps you decide when to use export APIs instead of CSV downloads from the dashboard.

The Braze export APIs let you programmatically export Braze data as JSON. For details on what you can export, prerequisites, and how delivery works, see [Export endpoints]({{site.baseurl}}/api/endpoints/export/). 

## When to use export APIs instead of CSV downloads

The following table describes common scenarios where using the export API is a better choice than a dashboard CSV download.

| Scenario | Details |
| --- | --- |
| Your export is too large for the dashboard | Dashboard CSV exports are limited to 500,000 rows. If you're exporting data on a segment with more than 500,000 users, use the export API, which has no limit on how much you can export. |
| You want to automate recurring reports | Schedule API exports through an integration to pull data on a regular cadence without manual dashboard interaction. |
| You need to feed data into external tools | Pull export data directly into BI tools, data warehouses, or other analytics platforms. |
| You need data not available as a dashboard CSV export | Some data categories, including KPIs, revenue series, custom event analytics, and session data, are only available through the API. |
| You want to interact with the data programmatically | Use the JSON output for custom processing, transformations, or integrations. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
For help with CSV and API exports, refer to [Export troubleshooting]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}
