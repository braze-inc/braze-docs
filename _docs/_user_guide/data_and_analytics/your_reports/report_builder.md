---
nav_title: Report Builder
article_title: Report Builder
alias: /report_builder/
page_order: 4
page_type: reference
description: "This reference article notes updates to the Report Builder feature within the Dashboard."
tool: 
  - Reports

---

# Report Builder

> The Report Builder allows you to compare the results of multiple campaigns or Canvases in a single view so that you can easily determine which engagement strategies most impacted your key metrics. For both campaigns and Canvases, you’re able to export your data and save your report to view in the future.

![Campaign Comparison Example][5]{: style="max-width:80%;"}

Use this report to answer key engagement questions, for example:

- Which were the best performing campaigns or Canvases for a specific tag or channel?
- Which variants of multivariant campaigns had the most uplift over the control?  
- Which seasonal promotion campaign led to a higher purchase rate — the summer sale, fall sale, or winter sale?
- Which push notifications within this Canvas had the highest open rates?
- Which steps in this group of Canvases had the most conversions?
- Did Version 1 of a welcome email or Version 2 of a welcome email lead to higher engagement and conversion? Did the changes work?
- How do different delivery methods (e.g. 3 scheduled pushes vs. 3 action-based pushes vs. 3 API-triggered pushes) impact your open rates, conversion rates, or purchase rates?
- Have the ongoing improvements to lapsing user messages positively impacted your KPIs over time?

## Run a Report

### Step 1: Create a New Report

Within the Dashboard, navigate to the **Report Builder** page in the lefthand navigation. Click **Create New Report** and select either a campaign comparison report or a Canvas comparison report. 

If you choose to run a report on campaigns, you can select between a __Manual__ or __Automated__ report. Reports may contain either campaigns or Canvases, but not both together.

{% alert note %} Any campaigns and Canvases that have last sent messages within the past 12 months will be eligible for a report. {% endalert %}

![Campaign Dashboard][6]{: style="max-width:80%;"}

Below are the differences between these two options:

| __Action__ | __Manual__ | __Automated__ |
| ---- | ---------- | ------------- |
| __Building Report__ | You will be able to narrow down your campaign list using filters, and then check off specific campaigns. | You will build your report by using the filter options to narrow down your campaign list. |
| __Saving and Viewing Report__ | You can save your report. The next time you view it, you will be able to view the same campaign you previously added, as these campaigns still fall under your "Last Sent" filter. | You can save your report. The next time you view it, the report will automatically update to include all campaigns that currently match your filters. |
| __Editing Report__ | You can click Edit Report to add or delete campaigns from your report | You can edit your report by adjusting your filter criteria. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %} Both **Manual** and **Automated** reports can include a maximum of 50 campaigns in a report. {% endalert %}

Canvas reports work similarly to a manual campaign report in that Canvas selections and report updates must also be done manually. You can include at most five Canvases in one report.

### Step 2: Choose Your Metrics

Once you've created your report, you’ll find a blank table containing campaigns in each row. The table will populate once you select __Edit Columns__ and choose the metrics you’d like to add. From here, click __Run Report__ to generate your metrics.

![Campaign Options][15]{: style="max-width:80%;"}

Your table will populate with the metrics you choose. For definitions of these metrics, refer to the [Report Metrics Glossary][16]. Some metrics are only available for campaign comparison reports.

You can also toggle calculations for the __Average__ of any rate or numerical metric and __Total__ for any numerical metric.

### Step 3: Choose a Time Period

You can select a specific time period to view your report's data for. If a particular campaign, Canvas, Canvas variant, or Canvas step does not have any data for your selected time period, the results for that row will be blank. 

![Campaign numerical metric][4]{: style="max-width:60%;"}

### Step 4: Name and Save Your Report

Name your report before saving it. If a report is saved without being named, Braze will apply a default name of "Campaign Comparison Report".

![Campaign Note][7]{: style="max-width:60%;"}

When you're ready, click __Save__. Saved reports can be viewed at a later point on the **Report Builder** page.

## Campaign Comparison Report with Multivariate Campaigns

For any multivariate campaigns, you can view these metrics broken down by your variants and control group by clicking the arrow next to the campaign name. The rows containing your variants will include performance results for that variant, and the row containing your control will include just the results for your conversion events. 

![Campaign Note][3]{: style="float:right;max-width:15%;margin-left:15px;"}

The metrics populating the row for your overall campaign will reflect the performance of its variants, but will not include the performance of the control. For instance, Primary Conversion Event A for your overall campaign will be the sum of the Primary Conversion Event A for your variants, and this will not include the Primary conversion Event A for your control.

{% alert important %} If you delete a variant from a multivariant campaign, the data from that variant will not be available for use in a future report. {% endalert %}

## Canvas Comparison Report Breakdown

Within a Canvas report, you can view your Canvases broken down by variant, steps, or message.

### Variant

Selecting **Breakdown by Variant** will allow you to see the high-level stats for your overall Canvases, as well as stats for each variant, which can be expanded by clicking the arrow next to the Canvas name.

![Variants][12]{: style="max-width:90%;"}

### Steps 

Selecting **Breakdown by Steps** will allow you to view step-level metrics, with each row of the report containing the row of a step.

![Steps][13]{: style="max-width:90%;"}

### Message

Similar to a step-level breakdown, selecting **Breakdown by Message** shows the name of steps in each row. However, within **Edit Columns**, you’ll have access to message-level metrics, such as channel-specific stats like email clicks and push opens.

![Report][14]{: style="max-width:90%;"}

Note that within the Braze dashboard, you can preview the first 50 rows of your Canvas report. You can access the full report when you export a CSV.

## Accessing Saved Reports

When you access a saved __Manual Report__, you will be able to view the same campaigns you previously added, as these campaigns still fall under your “Last Sent” filter.

When you access a saved __Automatic Report__, the report will automatically update to include all campaigns that currently match your filters. For instance, if your report filtered campaigns with the tag “Promotion,” then each time you view this report, you will be able to see all campaigns with the “Promotion” tag, even if these campaigns were created after you made this report.

## Editing Reports

In a __Manual Report__, you can edit a report by clicking **Edit**. From there, you can select or deselect campaigns to include in your report.

In an __Automatic Report__, simply toggle your filters to narrow down the results in your report.

## Exporting Reports

You can also click **Export** to download your report to CSV.

If your report contains any multivariant campaigns, your export will include two CSV files: 

- One file containing only the top-level metrics for each campaign
- One file that contains variant-level metrics

The file containing variant metrics will have `variant_` appended to the beginning of its name. The first time you export an automated report, you’ll receive a pop-up asking you to grant permission for downloading multiple files—click __Allow__.

![Campaign Download][8]{: style="max-width:60%;"}

### Exporting Canvas Comparison Reports

Your CSV export will reflect whichever breakdown view you were on when you clicked **Export**. For instance, if you were on the step-level breakdown view, your export will contain data on your step metrics. To export data from a different breakdown, you’ll need to navigate to that breakdown first, and click __Export__ from there.

If you download a variant breakdown Canvas report, you'll receive two CSV files:

- One file containing only top-level metrics for each Canvas
- One file that contains variant-level metrics

## Building Charts 

{% alert note %} This new feature is currently in early access. We will be making frequent enhancements to it, so if there's a use case you can't accomplish right now, be sure to check back again in the near future. If you have product feedback, please sumit it through [product feedback portal](https://dashboard.braze.com/resources/roadmap/). {% endalert %}

Charts are available for reports that feature campaigns and have at least one metric added to its columns. 

By default, the chart on each report will display the metric in the first column of the report; however, you can use a dropdown menu to select a particular metric to graph. Any metric in your report table will be available to display in your chart.

Your chart will display up to 30 campaigns, in descending order based on the metric you've selected. For instance, if your chart's metric if email clicks, then your chart will display the 30 email campaigns will the most clicks, ordered from most to fewest clicks. If your report contains more than 30 campaigns, only the top 30 will be displayed in the chart.

Charts are currently not saved when you save your report.




[3]: {% image_buster /assets/img/campaign_comparison/compare_note.png %}
[4]: {% image_buster /assets/img/campaign_comparison/metric.png %}
[5]: {% image_buster /assets/img/campaign_comparison/campaign_main.png %}
[6]: {% image_buster /assets/img/campaign_comparison/create_report.png %}
[7]: {% image_buster /assets/img/campaign_comparison/comparison_name.png %}
[8]: {% image_buster /assets/img/campaign_comparison/download.png %}
[12]: {% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}
[13]: {% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}
[14]: {% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}
[15]: {% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}

[16]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
