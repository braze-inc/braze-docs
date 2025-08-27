---
nav_title: Report Builder (legacy)
article_title: Report Builder (Legacy)
alias: /report_builder_legacy/
page_order: 0
page_type: reference
description: "This page covers how to run a report using the legacy report builder including campaign and Canvas creating comparison reports, and building reports and charts."
tool: 
  - Reports

---

# Report Builder (Legacy)

> The Report Builder allows you to compare the results of multiple campaigns or Canvases in a single view so that you can easily determine which engagement strategies most impacted your key metrics. For both campaigns and Canvases, you can export your data and save your report to view in the future.<br><br>For a descriptive list of the metrics you'll find in your reports, refer to the [Report Metrics Glossary]({{site.baseurl}}/user_guide/data/report_metrics/).

![Campaign Comparison Example]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Use this report to answer key engagement questions, for example:

- Which were the best performing campaigns or Canvases for a specific tag or channel?
- Which variants of multivariant campaigns had the most uplift over the control?  
- Which seasonal promotion campaign led to a higher purchase rate—the summer sale, fall sale, or winter sale?
- Which push notifications within this Canvas had the highest open rates?
- Which steps in this group of Canvases had the most conversions?
- Did Version 1 of a welcome email or Version 2 of a welcome email lead to higher engagement and conversion? Did the changes work?
- How do different delivery methods (for example, 3 scheduled pushes, 3 action-based pushes, and 3 API-triggered pushes) impact your open rates, conversion rates, or purchase rates?
- Have the ongoing improvements to lapsing user messages positively impacted your KPIs over time?

{% alert tip %}
Try to use the same conversion events for conversion A, B, and so on across campaigns and Canvases you wish to compare, so that you can line up these conversions in your Report Builder reports.
{% endalert %}

## Running a report

### Step 1: Create a new report

Within the dashboard, navigate to **Analytics** > **Report Builder**.

Select **Create New Report** and select either a campaign comparison report or a Canvas comparison report.

If you choose to run a report on campaigns, you can select between a **Manual** or **Automated** report. Reports may contain either campaigns or Canvases, but not both together. Any campaigns and Canvases that have last sent messages within the past 12 months will be eligible for a report.

![Campaign dashboard]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

The following are the differences between these two options:

| **Action** | **Manual** | **Automated** |
| ---- | ---------- | ------------- |
| **Building Report** | You will be able to narrow down your campaign list using filters, and then check off specific campaigns. | You will build your report by using the filter options to narrow down your campaign list. |
| **Saving and Viewing Report** | You can save your report. The next time you view it, you will be able to view the same campaign you previously added, as these campaigns still fall under your "Last Sent" filter. | You can save your report. The next time you view it, the report will automatically update to include all campaigns that currently match your filters. |
| **Editing Report** | You can select **Edit Report** to add or delete campaigns from your report | You can edit your report by adjusting your filter criteria. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %} 
Both **Manual** and **Automated** reports can include a maximum of 250 campaigns in a report. 
{% endalert %}

Canvas reports work similarly to a manual campaign report in that Canvas selections and report updates must also be done manually. You can include at most five Canvases in one report.

### Step 2: Choose your metrics

After you've created your report, you'll find a blank table containing campaigns in each row. The table will populate after you select **Edit Columns** and choose the metrics you'd like to add.

![Campaign Options]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Your table will populate with the metrics you choose. For definitions of these metrics, refer to the [Report Metrics Glossary]({{site.baseurl}}/user_guide/data/report_metrics/). Some metrics are only available for campaign comparison reports.

You can also toggle calculations for the **Average** of any rate or numerical metric and **Total** for any numerical metric.

### Step 3: Choose a time period

You can select a specific time period to view your report's data for. If a particular campaign, Canvas, Canvas variant, or Canvas component doesn't have any data for your selected time period, the results for that row will be blank. 

![Campaign numerical metric]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### Step 4: Name and save your report

Name your report before saving it. If a report is saved without being named, Braze will apply a default name of "Campaign Comparison Report".

![Campaign Note]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

When you're ready, select **Save**. Saved reports can be viewed at a later point on the **Report Builder** page.

## Campaign comparison report with multivariate campaigns

For any multivariate campaigns, you can view these metrics broken down by your variants and control group by clicking the arrow next to the campaign name. The rows containing your variants will include performance results for that variant, and the row containing your control will include just the results for your conversion events. 

![Campaign Note]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

The metrics populating the row for your overall campaign will reflect the performance of its variants, but won't include the performance of the control. For example, Primary Conversion Event A for your overall campaign will be the sum of the Primary Conversion Event A for your variants, and this won't include the Primary Conversion Event A for your control.

{% alert important %} 
If you delete a variant from a multivariant campaign, the data from that variant won't be available for use in a future report. 
{% endalert %}

## Canvas comparison report breakdown

Within a Canvas report, you can view your Canvases broken down by variant, steps, or message.

### Variant

Selecting **breakdown by variant** allows you to view the high-level stats for your overall Canvases, as well as stats for each variant, which can be expanded by selecting the arrow next to the Canvas name.

![Variants]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Steps 

Selecting **breakdown by steps** allows you to view step-level metrics, with each row of the report containing the row of a step.

![Steps]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Message

Similar to a step-level breakdown, selecting **breakdown by message** shows the name of steps in each row. However, within **edit columns**, you'll have access to message-level metrics, such as channel-specific stats like email clicks and push opens.

![Report]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Note that within the Braze dashboard, you can preview the first 50 rows of your Canvas report. You can access the full report when you export a CSV.

## Accessing saved reports

When you access a saved **Manual Report**, you can view the same campaigns you previously added, as these campaigns still fall under your "Last Sent" filter.

When you access a saved **Automatic Report**, the report will automatically update to include all campaigns that currently match your filters. For example, if your report filtered campaigns with the tag "Promotion," then each time you view this report, you will be able to see all campaigns with the "Promotion" tag, even if these campaigns were created after you made this report.

## Editing reports

In a **Manual Report**, you can edit a report by selecting **Edit**. From there, you can select or deselect campaigns to include in your report.

In an **Automatic Report**, simply toggle your filters to narrow down the results in your report.

## Exporting reports

You can also select **Export** to download your report to CSV.

If your report contains any multivariant campaigns, your export will include two CSV files: 

- One file containing only the top-level metrics for each campaign
- One file that contains variant-level metrics

The file containing variant metrics will have `variant_` appended to the beginning of its name. The first time you export an automated report, you'll receive a pop-up asking you to grant permission for downloading multiple files—click **Allow**.

![Campaign Download]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Exporting Canvas comparison reports

Your CSV export will reflect whichever breakdown view you were on when you selected **Export**. For example, if you were on the step-level breakdown view, your export will contain data on your step metrics. To export data from a different breakdown, you'll need to navigate to that breakdown first, and select **Export** from there.

If you download a variant breakdown Canvas report, you'll receive two CSV files:

- One file containing only top-level metrics for each Canvas
- One file that contains variant-level metrics

## Building Charts 

Use charts to visualize a selected metric in your report. Charts are available for reports that feature campaigns and have at least one metric added to its columns.

![Campaign Performance chart with metric Message Sent selected]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

By default, the chart on each report will display the metric in the first column of the report. To select a different metric to graph, choose your metric from the dropdown. Any metric in your report table will be available to display in your chart.

You can graph at most three metrics. The units for all metrics must be the same—for instance, if you choose a rate in the first dropdown, then only rates will be available for selection in the second dropdown.

If your chart contains only one metric, then it will display up to 30 campaigns in descending order based on the metric you've selected. For example, if your chart's metric is email clicks, then your chart will display the 30 email campaigns with the most clicks, ordered from most to fewest clicks. If your report contains more than 30 campaigns, only the top 30 will be displayed in the chart. If you select more than one metric, then your graph will only display the top five campaigns based on the first metric selected.

Charts are currently not saved when you save your report.



