---
nav_title: Clarisights
article_title: Clarisights
page_order: 1
description: "This article outlines the partnership between Braze and Clarisights, a self-serve performance marketing reporting platform."
alias: /partners/Clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisights][2] is a self-serve performance marketing reporting platform for data-driven organizations. It automatically integrates, processes, and visualizes all your data from marketing, analytical and attribution sources.

The Braze and Clarisights integration allows you to import data from Braze campaigns and Canvases to help achieve a unified reporting interface of performance and CRM/retention marketing.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Clarisights account | A Clarisights workspace is required to take advantage of this partnership |
| Braze REST API key | A Braze REST API key with the following permissions:  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
| Braze app group name | The name of the app group associated with the Braze API key. This name will be used to identify the app group integration on Clarisights. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

With the Braze and Clarisights integration, users can create different visualizations and tabled to gain insights from the campaigns they have created. Popular use cases include:

{% tabs %}
{% tab Better visibility %}
Better visibility on overall campaigns and Canvases performance.

![A graphic showing an example of better visability in the Clarisights platform. This graphic includes statisticcs for campaign and canvas opens, clicks, sent, converstions, etc.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Granular reporting %}
Granular reporting for campaigns and Canvases.

![A graphic showing granular reporting, like "overall sent by send channel" and "conversion rate".]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Unified dashboards %}
Unified dashboards for CMOs and CXOs.

![A graphic showing an example of unified dashboards.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## Integration

To sync Braze data to Clarisights, you must build a Braze connector and connect Braze app groups.

1. In Clarisights, navigate to the **Integrations** page, locate the **Braze** connector, and select **+ Connect**.<br>![A list of avalable connectors from the Clarisights integrations marketplace.][6]<br><br>
2. Next, using the integration flow, connect your Clarisights account to Braze. This can be done by providing your Braze REST API key, Braze app group name, and Braze REST endpoint.<br>![Braze app group connector in the Clarisights platform. This page has fields for Braze app group name, Braze REST API key, and Braze REST endpoint.][7]<br><br>Before successful integration, users will see the connected app groups on the same page.<br>![Within "Braze Accounts" you will find a list of connected app groups.][9]<br><br>

## Using this integration

To include Braze as a data source in your Clarisights reports, navigate to **Create New Report**. Name your report and select **Braze** as a data source in the prompt that appears. You can also choose the metrics and dimensions to include in the report. Once completed, select **Create Report**. 

The data from Braze will start flowing from the time of the next scheduled data import. Reach out to your Clarisights customer success manager to request backfills for longer durations. 

![Clarisight report settings showing fields for name and data source. For this example, "Braze" is selected as the data source.][8]

Visit Clarisights for more information on available [metrics and dimensions][10] or [report creation][11].

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://clarisights.com
[3]: {{site.baseurl}}/assets/img/clarisights/overall_view.png
[4]: {{site.baseurl}}/assets/img/clarisights/unified_dashboard.png
[5]: {{site.baseurl}}/assets/img/clarisights/granular_reporting.png
[6]: {{site.baseurl}}/assets/img/clarisights/integrations.png
[7]: {{site.baseurl}}/assets/img/clarisights/braze_flow.png
[8]: {{site.baseurl}}/assets/img/clarisights/braze_report.png
[9]: {{site.baseurl}}/assets/img/clarisights/connected.png
[10]: https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions
[11]: https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights
