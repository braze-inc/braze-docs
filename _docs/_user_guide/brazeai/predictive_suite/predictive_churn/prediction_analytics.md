---
nav_title: Prediction Analytics
article_title: Prediction Analytics
description: "This reference article covers the different components included in the Churn Prediction Analytics page and how they can be used to make insightful, driven decisions."
page_order: 2

---

# Prediction analytics

> After your prediction has been built and trained, you will have access to the **Prediction Analytics** page. This page helps you decide what users you should target based on their _Churn Risk Score_ or category. 

As soon as the prediction is done training and this page is populated, you can jump to simply using [filters]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) in segments or campaigns to begin using the outputs of the model. But, if you want help deciding who to target and why, this page can help based on the historical accuracy of the model and your own business goals. 

**Analytics Components**<br>
&#45; [Churn Score and Category](#churn_score)<br>
&#45; [Prediction Quality](#prediction_quality)<br>
&#45; [Estimated Results](#estimated_results)<br>
&#45; [Churn Correlation Table](#correlation_table)

## Overview

The distribution of the scores for the entire prediction audience is displayed at the top of the page in a chart that you can view, by category or by score. Users in bins further to the right have higher scores and are more likely to churn. Users in bins further to the left are less likely to churn. The slider beneath the chart will allow you to select a swath of users and estimate what the results would be of targeting users in the selected range of _Churn Risk Score_ or category.

![][4]

As you move the slider, the bar in the left half of the lower panel will inform you how many users out of the entire prediction audience would be targeted.

## Churn score and category {#churn_score}

Users in the prediction audience will be assigned a _Churn Risk Score_ between 0 and 100. The higher the score, the greater the likelihood of churn. 
- Users with scores between 0 and 50 will be labeled in the _Low Risk_ category. 
- Users with scores between 50 and 75, and 75 and 100 will be labeled in the _Medium Risk_ and _High Risk_ categories, respectively. 

The scores and the corresponding categories will be updated according to the schedule you chose on the model creation page. The number of users with churn scores in each of 20 equally sized buckets is displayed in the chart at the top of the page. This can help you determine what the churn risk looks like across the population according to this prediction.

## Targeting users to reduce churn

### Prediction quality {#prediction_quality}

To measure the accuracy of your model, the _Prediction Quality_ metric will show you how effective this particular machine learning model appears to be when tested on historical data. Refer to [Prediction Quality]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) to learn more about the metric.

Here's what we recommend for various ranges of _Prediction Quality_:

| Prediction Quality Range (%) | Recommendation |
| ---------------------- | -------------- |
| 60 - 100 | Excellent. Top tier accuracy. Changing the audience definitions is unlikely to provide additional benefit. |
| 40 - 60 | Good. This model will produce accurate predictions, but trying different audience settings may achieve even better results. |
| 20 - 40| Fair. This model can provide accuracy and value, but consider trying different audience definitions to see if they increase performance. |
| 0 - 20 | Poor. We recommend you change your audience definitions and try again. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The prediction will be trained again every two weeks and updated alongside the prediction quality metric to keep your predictions updated on the most recent user behavior patterns. The last time this retraining occurred will be displayed on the predictions list page as well as on your prediction's analytics page.

## Estimated accuracy {#estimated_results}

In the right half of the panel beneath the chart, we show estimates of the expected accuracy of targeting this swath of the prediction audience. Based on data about users in the prediction audience in the past, and the apparent accuracy for the model for discriminating between churning and non-churning users on that past data, these progress bars estimate for a future potential message using the audience highlighted with the slider:

![][6]{: style="float:right;max-width:40%;margin-left:15px;"}

- How many selected users are expected to churn
- How many selected users are expected **not** to churn


Using this information, we encourage you to decide how many of the churners you want to capture and what the cost of a false positive error is for your business. If you are sending out a valuable promo, you may want to keep non-churners targeted to a minimum while getting as many expected true churners as the model will allow. Or, if you're less sensitive to false positives and users receive extra messaging, you can message more of the audience to capture more expected churners and ignore the likely errors.

### Users expected to churn

This is an estimate of how many actual churners will be correctly targeted. Of course, we don't know the future perfectly, so we don't know precisely which users from the prediction audience will churn in the future. But the prediction is a reliable inference. Based on past performance, this progress bar indicates how many of the total "actual" or "true" churners expected in the prediction Audience (based on prior churn rates) will be targeted with the current targeting selection. We would expect this number of users to churn if you do not target them with any extra or unusual messaging.

### Users expected not to churn 

This is an estimate of how many users who wouldn't have churned will be incorrectly targeted. All machine learning models make errors. There may be users in your selection who have a high _Churn Risk Score_ but do not end up churning. They would not churn even if you took no action. They will be targeted anyway, so this is an error or "false positive." The full width of this second progress bar represents the expected number of users who will not churn, and the filled portion represents those who will be incorrectly targeted using the current slider position.

## Churn correlation table {#correlation_table}

This analysis displays any user attributes or behaviors that are correlated with user churn in the historical prediction audience. The tables are split into left and right for more and less likely to churn, respectively. For each row, the ratio by which the users with the behavior or attribute in the left column are more or less likely to churn is displayed in the right column. This number is the ratio of churn likelihood of users with this behavior or attribute divided by the likelihood to churn off the entire prediction audience.

This table is updated only when the prediction retrains and not when user _Churn Risk Scores_ are updated.

{% alert note %}
Correlation data for preview predictions will be partially hidden. A purchase is required to reveal this information. Contact your account manager for more information.
{% endalert %}

[6]: {% image_buster /assets/img/churn/churnEstimatedResults.png %}
[4]: {% image_buster /assets/img/churn/churnTargeting.gif %}