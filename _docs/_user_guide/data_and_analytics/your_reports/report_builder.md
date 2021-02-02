---
nav_title: Report Builder
alias: /report_builder/
description: "This reference article notes updates to the Report Builder feature within the Dashboard."
---

# Report Builder

> The Report Builder allows you to compare the results of multiple campaigns or Canvases in a single view so that you can easily determine which engagement strategies most impacted your key metrics.

![Campaign Comparison Example][5]{: style="max-width:80%;"}

{% alert note %}
Canvases have recently been added to Report Builder. Canvas reports currently cannot be named, saved, or edited, but this functionality is coming soon. 
{% endalert %}

#### Use this report to answer key engagement questions, for example:<br><br>
- Which were the best performing campaigns or Canvases for a specific tag or channel?
- Which variants of multivariant campaigns had the most uplift over the control?  
- Which seasonal promotion campaign led to a higher purchase rate — the summer sale, fall sale, or winter sale?
- Which push notifications within this Canvas had the highest open rates?
- Which steps in this group of Canvases had the most conversions?
- Did Version 1 of a welcome email or Version 2 of a welcome email lead to higher engagement and conversion? Did the changes work?
- How do different delivery methods (e.g. 3 scheduled pushes vs. 3 action-based pushes vs. 3 API-triggered pushes) impact your open rates, conversion rates, or purchase rates?
- Have the ongoing improvements to lapsing user messages positively impacted your KPIs over time?

## Run a Report

__1.__ Within the Dashboard, navigate to the Report Builder page in the lefthand navigation.<br><br>
__2.__ Create a new report by selecting one of your options: a campaign comparison report or a Canvas comparison report. If you choose to run a report on campaigns, you can select between a __Manual__ or __Automated__ report. Reports may contain either campaigns or Canvases, but not both together.<br><br>![Campaign Dashboard][6]{: style="max-width:80%;"}<br><br> Below are the differences between these two options.

| __Action__ | __Manual__ | __Automated__ |
| ---- | ---------- | ------------- |
| __Building Report__ | You will be able to narrow down your campaign list using filters, and then check off specific campaigns. | You will build your report by using the filter options to narrow down your campaign list. |
| __Saving and Viewing Report__ | You can save your report. The next time you view it, you will be able to view the same campaign you previously added, as these campaigns still fall under your "Last Sent" filter. | You can save your report. The next time you view it, the report will automatically update to include all campaigns that currently match your filters. |
| __Editing Report__ | You can click Edit Report to add or delete campaigns from your report | You can edit your report by adjusting your filter criteria. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Note that for both options, the current limit on the maximum number of campaigns in a report is 50. 

Canvas reports work similarly to a manual campaign report in that Canvas selections and report updates must also be done manually. You can include at most 5 Canvases in one report.

__3.__ Once you've created your report, you’ll find a blank table containing campaigns in each row. The table will populate once you select __Edit Columns__ and choose the metrics you’d like to add. From here, click __Run Report__ to generate your metrics.
<br><br>
![Campaign Options][2]{: style="max-width:80%;"}
<br>

Your table will populate with the metrics you choose.

You can also toggle calculations for the __average__ of any rate or numerical metric or __total__ for any numerical metric.

![Campaign numerical metric][4]{: style="max-width:60%;"}<br>

### Campaign Comparison Report with Multivariate Campaigns

For any multivariate campaigns, you can view these metrics broken down by your variants and control group by clicking the arrow next to the campaign name. The rows containing your variants will include performance results for that variant, and the row containing your control will include just the results for your conversion events. 
<br><br>
![Campaign Note][3]{: style="float:right;max-width:15%;margin-left:15px;"}
Note: The metrics populating the row for your overall campaign will reflect the performance of its variants, but __will not include the performance of the control__. For instance, Primary Conversion Event A for your overall campaign will be the sum of the Primary Conversion Event A for your variants, and this will not include the Primary conversion Event A for your control.

### Canvas Comparison Report Breakdown

Within a Canvas report, you can view your Canvases broken down by:

- __Variants__ - this will allow you to see the high-level stats for your overall Canvases, as well as stats for each variant, which can be expanded by clicking the arrow next to the Canvas name.
- __Steps__ - you’ll be able to view step-level metrics, with each row of the report containing the row of a step.
- __Message__ - similar to a step-level breakdown, the message-level breakdown contains the name of steps in each row. However, within Edit Columns, you’ll have access to message-level metrics, such as channel-specific stats like email clicks and push opens.

Note that within the Braze dashboard, you can preview the first 50 rows of your Canvas report. You can access the full report when you export a CSV.

## Naming Your Report

Name your report before saving it. If a report is saved without being named, Braze will apply a default name of Campaign Comparison Report. 

![Campaign Note][7]{: style="max-width:60%;"}

{% alert note %}
This functionality is not yet available for Canvas reports.
{% endalert %}

## Saving and Accessing Reports

You can save your report and name it by using the __Save__ button. Saved reports can be viewed at a later point on the Report Builder page.

When you access a saved __manual report__, you will be able to view the same campaigns you previously added, as these campaigns still fall under your “Last Sent” filter.

When you access a saved __automatic report__, the report will automatically update to include all campaigns that currently match your filters. For instance, if your report used the filters for “Last Sent” in the last 7 days for campaigns with the tag “Promotion,” then each time you view this report, you will be able to see all campaigns with the “Promotion” tag that last sent in the last 7 days, even if these campaigns were created after you made this report.

{% alert note %}
This functionality is not yet available for Canvas reports.
{% endalert %}

## Editing Reports

In a __manual report__, you can edit a report via the Edit button in the upper right. From there, you can select/un-select campaigns to include in your report.

In an __automatic report__, simply toggle your filters to narrow down the results in your report.

{% alert note %}
This functionality is not yet available for Canvas reports.
{% endalert %}

## Exporting Reports

You can also download your report to CSV using the __Export__ button. 

### Campaign Comparison Reports

If your report contains any multivariant campaigns, your export will include 2 CSV files - one file containing only the top-level metrics for each campaign, and another file that contains variant level metrics. The file containing variant metrics will have `variant_` appended to the beginning of its name. The first time you export an automated report, you’ll receive a pop-up asking you to grant permission for downloading multiple files -  click __Allow__.

### Canvas Comparison Reports

Your CSV export will reflect whichever breakdown view you were on when you clicked Export. For instance, if you were on the step-level breakdown view, your export will contain data on your step metrics. To export data from a different breakdown, you’ll need to navigate to that breakdown first, and click __Export__ from there.

If you download a variant breakdown Canvas report, you’ll receive 2 CSV files - one containing top-level metrics for each Canvas, and another containing variant level metrics. The first time you export a report like this, you’ll receive a pop-up asking you to grant permission for downloading multiple files - click __Allow__.

![Campaign Download][8]{: style="max-width:60%;"}

[2]: {% image_buster /assets/img/campaign_comparison/compare_option.png %}
[3]: {% image_buster /assets/img/campaign_comparison/compare_note.png %}
[4]: {% image_buster /assets/img/campaign_comparison/metric.png %}
[5]: {% image_buster /assets/img/campaign_comparison/campaign_main.png %}
[6]: {% image_buster /assets/img/campaign_comparison/create_report.png %}
[7]: {% image_buster /assets/img/campaign_comparison/comparison_name.png %}
[8]: {% image_buster /assets/img/campaign_comparison/download.png %}
