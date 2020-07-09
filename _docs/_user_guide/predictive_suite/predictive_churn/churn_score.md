---
nav_title: Churn Score and Category
title: Churn Score and Category
description: ""
page_order: 3
---

## Churn Score and Category

Users in the Prediction Audience will be assigned a Churn Score between 0 and 100. The higher the score, the greater the likelihood of Churn. Users with Churn Scores between 0 and 50 will be labeled in the Low Churn Risk category. Users with scores between 50 and 75, and 75 and 100 will be labeled as the Medium and High Churn Risk categories, respectively. The scores and the corresponding categories will be updated according to the schedule you chose in the model creation page. The number of users with Churn Scores in each of 20 equally sized buckets is displayed in the chart at the top of the page. This can help you determine what the churn risk looks like across the population according to this Prediction.

## Targeting Users

The Prediction analytics page lets you decide what users you should target based on their Churn Risk Score or Category. As soon as the Prediction is done training and this page is populated, you can jump to simply using [Filters](#filters) in Segments or Campaigns to begin using the outputs of the model. But, if you want help deciding who to target and why, this page can help based on the historical accuracy of the model and your own business goals. 

The distribution of the scores for the entire Prediction Audience is displayed at the top of the page in a chart that you can view, by category, or by score. Users in bins further to the right have higher scores and are more likely to churn. Users in bins further to the left are less likely to churn. The slider beneath the chart will allow you to select a swath of users and estimate what the results would be of targeting users in the selected range of Churn Risk Score or Category.

As you move the slider, the bar in the left half of the lower panel will inform you how many users out of the entire Prediction Audience would be targeted.

### Estimated Results

![Estimated Results][6]

In the right half of the panel beneath the chart, we show estimates of the expected accuracy of targeting this swath of the Prediction Audience. Based on data about users in the Prediction Audience in the past, and the apparent accuracy for the model for discriminating between churning and non-churning users on that past data, these progress bars estimate for a future potential message using the audience highlighted with the slider:

1. An estimate of how many actual churners will be correctly targeted

Of course, we don't know the future perfectly, so we don't know precisely which users from the Prediction Audience will churn in the future. But the Prediction is a reliable inference. Based on past performance, this progress bar indicates how many of the total "actual" or "true" churners expected in the Prediction Audience (based on prior churn rates) will be targeted with the current targeting selection. We would expect this number of users to churn if you do not target them with any extra or unusual messaging. 

2. An estimate of how many users who wouldn't have actually churned will be incorrectly targeted

All machine learning models make errors. There may be users in your selection who have a high Churn Risk Score but do not end up churning. They would not churn even if you take no action. They will be targeted anyway, so this is an error or "false positive." The full width of this second progress bar represents the expected number of users who will not churn, and the red portion is those who will be incorrectly targeted using the current slider position.

Using this information, we encourage you to decide how many of the churners you want to capture, and what the cost of a false positive error is for your business. If you are sending out a valuable promo, you may want to keep non-churners targeted to a minimum while getting as many expected true churners as the model will allow. Or, if you're less sensitive to false positives and users receive extra messaging, you can message more of the audience to capture more expected churners and ignore the likely errors.

### Filters {#filters}

Once you've decided what range of Churn Risk Score or Category you want to target, you can use the "Create Segment" or "Create Campaign" buttons below the targeting sentences to create a new segment or campaign that filters for users with the Churn Risk Score or Category selected with the slider.

![Churn Filters][5]

You can also use filters in campaigns or segments to target the users according to that threshold. You can filter for users by Churn Score or Churn Category in Campaigns, Canvas, and Segments, just like you use any other filter in Braze.

## Churn Correlation Table

This analysis displays any user attributes or behaviors that are correlated with user churn in the historical Prediction Audience. The tables are split into left and right for more and less likely to churn, respectively. For each row, the ratio by which the users with the behavior or attribute in the left column are more or less likely to churn is displayed in the right column. This number is the ratio of churn likelihood of users with this behavior or attribute divided by the likelihood to churn off the entire Prediction Audience.

This table is updated only when the Prediction retrains and not when user Churn Risk Scores are updated.

## Archived Predictions

Archived Predictions will cease updating user scores. Any archived Prediction that is unarchived will continue updating user scores on its predetermined schedule. Archived Predictions are never deleted and remain in the list.

### Sample Churn and Prediction Audience Definitions {#sample-definitions}

- “Within 7 days, did custom event ‘Subscription Cancellation’”
- “Within 14 days, did custom event ‘Trial Expired’”
- “Within 1 day did uninstall.” 
- “Within 14 days did not Make a Purchase.” 

For the Churn definitions we outlined above, there might be some corresponding Prediction Audience definitions:
- Started subscription more than 2 weeks ago OR Started subscription less than two weeks ago. You might want to create 2 predictions in this case and then message new subscribers differently than longer-term subscribers. You could also define this as “First Made Purchase more than 30 days ago.”
- For uninstallers, you might focus on customers who have purchased something in the recent past or used the app very recently.
- For those at risk of not purchasing as a definition of churn, you may want to focus on customers who have been browsing or searching or engaging with your app more recently. Perhaps the right discount intervention will prevent this more engaged group from churning.

[5]: {% image_buster /assets/img/churn/churnFilters.png %}
[6]: {% image_buster /assets/img/churn/churnEstimatedResults.png %}



