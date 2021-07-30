---
nav_title: Prediction Analytics
title: Prediction Analytics
description: "This reference article covers the different components included in the Predictive Purchases Analytics Page and how they can be used to make insightful driven decisions."
page_order: 2
---

# Prediction Analytics

Once your Prediction has been built and trained, you will have access to the Prediction Analytics page. This page helps you decide what users you should target based on their Purchase Likelihood Score or Category. As soon as the Prediction is done training and this page is populated, you can jump to simply using [Filters]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/messaging_users/#filters) in Segments or campaigns to begin using the outputs of the model. But, if you want help deciding who to target and why, this page can help based on the historical accuracy of the model and your own business goals. 

__Analytics Components__<br>
&#45; [Purchase Likelihood Score](#purchase_score)<br>
&#45; [Targeting Users](#target_users)<br>
&#45; [Prediction Quality](#prediction_quality)<br>
&#45; [Estimated Results](#estimated_results)<br>
&#45; [Purchase Correlation Table](#correlation_table)

## Purchase Likelihood Score {#purchase_score}

Users in the Prediction Audience will be assigned a Purchase Likelihood Score between 0 and 100. The higher the score, the greater the likelihood of Purchase. Users with Purchase Likelihood Scores between 0 and 50 will be labeled in the Low category. Users with scores between 50 and 75, and 75 and 100 will be labeled in the Medium and High likelihood categories, respectively. The scores and the corresponding categories will be updated according to the schedule you chose in the Prediction creation page. The number of users with Purchase Likelihood Scores in each of 20 equally sized buckets or in each of the Purchase Likelihood Categories is displayed in the chart at the top of the page.

## Audience Builder {#target_users}

The distribution of the Purchase Likelihood Scores for the entire Prediction Audience is displayed at the top of the page. Users in buckets further to the right have higher scores and are more likely to purchase. Users in buckets further to the left are less likely to purchase. The slider beneath the chart will allow you to select a swath of users and estimate what the results would be of targeting those users.

![Churn Targeting][4]{: style="max-width:90%"} 

As you move the slider handles to different positions, the bar in the left half of the panel below it will inform you how many users out of the entire Prediction Audience would be targeted using the part of the population you've selected.

### Estimated Results {#estimated_results}

![Estimated Results][6]

In the right half of the panel beneath the chart, we show estimates of the expected accuracy of targeting the portion of the Prediction Audience you selected above in two ways:

1. How many selected users are expected to purchase<br><br> The Prediction isn't perfectly accurate, and no Prediction ever is. So, Braze will not be able to identify every single future purchaser. The Likelihood Scores are like a set of informed and reliable predictions. This progress bar indicates how many of "actual" or "true" purchasers expected in the Prediction Audience will be targeted with the audience selected above. Note that we expect this number of users to purchase even if you don't send them a message. <br><br>

2. How many selected users are expected not to purchase<br><br>All machine learning models make errors. There may be users in your selection who have a high Purchase Likelihood Score but do not end up actually making a purchase. They would not make a purchase if you took no action. They will be targeted anyway, so this is an error or "false positive." The full width of this second progress bar represents the expected number of users who will not purchase, and the red portion is those who will be incorrectly targeted using the current slider position.

Using this information, we encourage you to decide how many of the purchasers you want to capture, how many non-purchasers you can accept being targeted, and what the cost of errors is for your business. If you are sending out a valuable promo, you may want to target only non-purchasers by favoring the left side of the chart. Or, you may want to encourage buyers who often purchase to do so again by selecting a swath of users that favors the right side of the chart.

### Prediction Quality {#prediction_quality}

To measure the accuracy of your model, the __Prediction Quality__ metric will show you how effective this particular machine learning model appears to be. Essentially, it's a measure of how good this Prediction is at telling apart the buyers from non-buyers. A Prediction Quality of 100 would mean it perfectly knows who will and will not purchase without error (this never happens!), and 0 means it's randomly guessing. Check out this doc to read more about what goes into [Prediction Quality]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/).

Here’s what we recommend for various ranges of Prediction Quality:

| Prediction Quality Range (%) | Recommendation |
| ---------------------- | -------------- |
| 60 - 100 | Excellent. Top tier accuracy. Changing the audience definitions is unlikely to provide additional benefit. |
| 40 - 60 | Good. This model will produce accurate predictions, but trying different audience settings may achieve even better results. |
| 20 - 40| Fair. This model can provide accuracy and value, but consider trying different audience definitions to see if they increase performance. |
| 0 - 20 | Poor. We recommend you change your audience definitions and try again. |
{: .reset-td-br-1 .reset-td-br-2}

The Prediction will be trained again every two weeks and updated alongside the Prediction Quality metric to keep your predictions updated on the most recent user behavior patterns. The last time this retraining occurred will be displayed on the Predictions list page as well as on your Prediction's analytics page. 

When a Prediction is first created, the Prediction Quality will be based upon historical data that is queried when you click Build Prediction. Every two weeks thereafter, the Prediction Quality is derived by comparing prediction scores to real-world outcomes.


## Purchase Correlation Table {#correlation_table}

This analysis displays user attributes or behaviors that are correlated with purchases in the Prediction Audience. The attributes assessed are Age, Country, Gender, and Language. Behaviors that are analyzed include sessions, purchases, total dollars spent, custom events, and campaigns & canvas steps received in the last 30 days. The tables are split into left and right for more and less likely to purchase, respectively. For each row, the ratio by which the users with the behavior or attribute in the left column are more or less likely to purchase is displayed in the right column. This number is the ratio of purchase likelihood of users with this behavior or attribute divided by the likelihood to purchase off the entire Prediction Audience.

This table is updated only when the Prediction retrains and not when user Purchase Likelihood Scores are updated.

{% alert note %}
Correlation data for Preview Predictions will be partially hidden. A purchase is required to reveal this information. Please contact your Account Manager for more information.
{% endalert %}

[6]: {% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %}
[4]: {% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}