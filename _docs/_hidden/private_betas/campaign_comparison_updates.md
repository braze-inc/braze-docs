---
nav_title: Campaign Comparison Updates
permalink: /campaign_comparison_updates/
description: "This reference article notes updates to the existing Campaign Comparison feature within the Dashboard."
hidden: true
---

{% alert note %}
This feature is currently in Beta and this page may not reflect the most recent changes to the feature. Please contact your CSM or Account Manager for early access to this feature.
{% endalert %}

# Campaign Comparison

The Campaign Comparison Report allows you to compare the results of multiple campaigns in a single view so that you can easily determine which engagement strategies most impacted your key metrics. This reference article notes updates to the [existing Campaign Comparison][0] feature within the Dashboard.

Use this report to answer key engagement questions, for example:
- Which were the best performing campaigns for a specific tag or channel?
- Which variants of multivariant campaigns had the most uplift over the control?  
- Which seasonal promotion campaign led to a higher purchase rate—the summer sale, fall sale, or winter sale?
- Did Version 1 of a welcome email or Version 2 of a welcome email lead to higher engagement and conversion? Did the changes work?
- How do different delivery methods (e.g 3 scheduled pushes vs. 3 action-based pushes vs. 3 API-triggered pushes) impact your open rates, conversion rates, or purchase rates?
- Have the ongoing improvements to lapsing user messages positively impacted your KPIs over time?

## Run a Report

1. Within the Dashboard, navigate to the Campaign Comparisons page.
2. Create a new report by slecting one of two options: manual or automated. Below are the differences between these two options.<br><br>Note: For both options, the current limit on the maximum number of campaigns in a report is 50.

|   | Manual | Automated |
| Building Report | You will be able to narrow down your campaign list using filters, and then check off specific campaigns. | You will build your report by using filters options to narrow down your campaign list. |
| Saving and Viewing Report | You can save your report. The next time you view it, you will be able to view the same campaign you previously added, as these campaigns still fall under your "Last Sent" filter. | You can save your report. The next time you view it, the report will automatically update to include all campaigns that currently match your filters. |
| Editing Report | You can click Edit Report to add or delte capaigns from your report | You can edit your report by adjusting your filter criteria. |


3. Once you've created your report, you’ll find a blank table containing campaigns in earch row. The table will populate once you select __Edit Columns__ and choose the metrics you’d like to add. Then, click __Run Report__ to generate your metrics.
![Campaign Options][2]{: style="margin-left:10px"}<br><br>For any multivariate campaigns, you can view these metrics broken down by your variants and control group by clicking the arrow next to the campaign name. The rows containing your variants will include performance results for that variant, and the row containing your control will include just the results for your conversion events. 
![Campaign Note][3]{: style="float:right;max-width:15%;margin-left:15px;margin-top:15px;"}
<br>
Note: The metrics populating the row for your overall campaign will reflect the performance of its variants, but __will not include the performance of the control__. For instance, Primary Conversion Event A for your overall campaign will be the sum of the Primary Conversion Event A for your variants, and this will not include the Primary conversion Event A for your control.

## Saving reports and accessing saved reports

You can save your report and name it by using the Save button. Saved reports can be viewed at a later point on the Campaign Comparison page.

When you access a saved manual report, you will be able to view the same campaigns you previously added, as these campaigns still fall under your “Last Sent” filter.

When you access a saved automatic report, the report will automatically update to include all campaigns that currently match your filters. For instance, if your report used the filters for “Last Sent” in the last 7 days for campaigns with the tag “Promotion,” then each time you view this report, you will be able to see all campaigns with the “Promotion” tag that last sent in the last 7 days, even if these campaigns were created after you made this report.

## Exporting Reports

You can also download your report to CSV using the Export button. 

If your report contains any multivariant campaigns, your export will include 2 CSV files - one file containing only the top level metrics for each campaign, and another file that contains variant level metrics. 


[0]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/#comparing-campaigns
[1]: {% image_buster /assets/img/campaign_comparison/compare_button.png %}
[2]: {% image_buster /assets/img/campaign_comparison/compare_option.png %}
[3]: {% image_buster /assets/img/campaign_comparison/compare_note.png %}
