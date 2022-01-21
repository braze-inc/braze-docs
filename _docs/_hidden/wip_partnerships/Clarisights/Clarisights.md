---
nav_title: Clarisights
article_title: Clarisights
page_order: 1

description: "Analyze your Braze campaign and canvas data on Clarisights"
alias: /partners/Clarisights/

page_type: partner
search_tag: Partner
hidden: true

---

# Clarisights

> [Clarisights][2] is a self-serve performance marketing reporting platform for data driven organizations. It automatically integrates, processes and visualises all your data from marketing, analytical and attribution sources.

The Braze and Clarisights integration allows users to pull in data from Braze campaigns and canvases for their analysis. With the addition of Braze data on Clarisights, users can achieve a unified reporting interface of performance and CRM/Retention marketing.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Partner account | A Clarisights workspace is required to take advantage of this partnership |
| Braze REST API key | A Braze REST API Key with the following permissions:  <br> - campaigns.list <br>  - campaigns.details<br> - campaigns.data_series <br> - canvas.details<br> - canvas.list <br>  - canvas.data_series <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
| Braze App Group Name | The name of the App Group associated with the Braze API key so that users can identify the app group integrated on Clarisights|
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

With the Braze data on Clarisights, users can create different visualizations and tables to gain insights from the messaging campaigns they have created. We cover some of the popular usecases below :

- Better Visibility on overall Campaigns/Canvases performance <br><br>
![Image][3]<br><br>
- Granular Reporting for Campaigns/Canvases <br><br>
![Image 1][5]<br><br>
- Unified Dashboards for CMOs/CXOs<br><br>
![Image 2][4]<br>

## Integration

The Braze integration on Clarisights is an out-of-box integration where the user will be able to import data from Braze onto the platform after the connection process. Users can connect app groups on Clarisights by following the steps below:

### Step 1: Navigating to the Braze Connector on the Integrations Page

On the Integrations page, click on the ```+ Connect``` button next to the Braze integration

![Image 3][6]<br><br>

### Step 2: Complete the Integration flow for Braze

To connect an account with Braze, the user will need to fill the API Key, App Group Name and REST endpoint in the integration flow.

![Image 4][7]<br><br>

Post successful integration, the user will be able to see the connected app groups on the same page.

![Image 6][9]<br><br>

### Step 3: Include Braze as a data source in your reports

The data from the Braze will start flowing in from the time of the next scheduled data import. Users can reach out to their Clarisights Customer Success Manager to request for backfills for longer durations.

![Image 5][8]<br><br>

Visit this [help article][10] to learn more about the metrics and dimensions available from Braze in your Clarisights dashboards.
<br><br>
Read [more][11] about creating reports on Clarisights.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://clarisights.com
[3]: {{site.baseurl}}/assets/img/Clarisights/overall_view.png
[4]: {{site.baseurl}}/assets/img/Clarisights/unified_dashboard.png
[5]: {{site.baseurl}}/assets/img/Clarisights/granular_reporting.png
[6]: {{site.baseurl}}/assets/img/Clarisights/integrations.png
[7]: {{site.baseurl}}/assets/img/Clarisights/braze_flow.png
[8]: {{site.baseurl}}/assets/img/Clarisights/braze_report.png
[9]: {{site.baseurl}}/assets/img/Clarisights/connected.png
[10]: https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions
[11]: https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights
