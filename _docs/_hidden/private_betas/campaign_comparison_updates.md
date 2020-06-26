---
nav_title: Campaign Comparison Updates
permalink: /campaign_comparison_updates/
description: "This reference article notes updates to the existing Campaign Comparison feature within the Dashbaord."
hidden: true
---

{% alert note %}
This feature is currently in Beta and this page may not reflect the most recent changes to the feature. Please contact your CSM or Account Manager for early access to this feature.
{% endalert %}

# Campaign Comparison Updates

The Campaign Comparison Report allows you to compare the results of multiple campaigns in a single view so that you can easily determine which engagement strategies most impacted your key metrics. This reference article notes updates to the [existing Campaign Comparison][0] feature within the Dashboard.

Use this report to answer key engagement questions, for example:
- Which seasonal promotion campaign led to a higher purchase rate—the summer sale, fall sale, or winter sale?
- Did Version 1 of a welcome email or Version 2 of a welcome email lead to higher engagement and conversion? Did the changes work?
- How do different delivery methods (e.g 3 scheduled pushes vs. 3 action-based pushes vs. 3 API-triggered pushes) impact your open rates, conversion rates, or purchase rates?
- Have the ongoing improvements to lapsing user messages positively impacted your KPIs over time?

## Run a Report

1. Within the Dashboard, navigate to your campaigns page, and select __Compare__.
![Campaign Button][1]{: style="margin-left:10px"}<br><br>
2. Add the campaigns you wish to compare and click __Compare Selected__.<br><br>
3. From the Comparison Details page, you’ll find a blank table containing the campaigns you selected. The table will populate once you select __Edit Columns__. From here, choose the metrics you’d like to add as columns and click __Run Report__.
![Campaign Options][2]{: style="margin-left:10px"}<br><br>
4. Your table will populate with the metrics you chose.<br><br> 
5. For any multivariate campaigns, you can view these metrics broken down by your variants and control group by clicking the arrow next to the campaign name. The rows containing your variants will include performance results for that variant, and the row containing your control will include just the results for your conversion events. 
![Campgin Note][3]{: style="float:right;max-width:15%;margin-left:15px;margin-top:15px;"}
<br>
Note: The metrics populating the row for your overall campaign will reflect the performance of its variants, but __will not include the performance of the control__. For instance, Primary Conversion Event A for your overall campaign will be the sum of the Primary Conversion Event A for your variants, and this will not include the Primary conversion Event A for your control.

[0]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/#comparing-campaigns
[1]: {% image_buster /assets/img/campaign_comparison/compare_button.png %}
[2]: {% image_buster /assets/img/campaign_comparison/compare_option.png %}
[3]: {% image_buster /assets/img/campaign_comparison/compare_note.png %}
