---
nav_title: Event analytics
article_title: Predictive Event Analytics
description: "This reference article covers the different components included in the Predictive Events Analytics page and how they can be used to make insightful driven decisions."
page_order: 1.3

---

# Predictive event analytics

> After your prediction has been built and trained, you will have access to the **Prediction Analytics** page. This page helps you decide what users you should target based on their likelihood score or category.

## About predictive event analytics

As soon as the prediction is done training and this page is populated, you can start using [filters]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) in segments or campaigns to begin using the outputs of the model. If you want help deciding who to target and why, this page can help based on the historical accuracy of the model and your own business goals.

These are the components that make up predictive event analytics:

- [Likelihood Score](#purchase_score)
- [Prediction Quality](#prediction_quality)
- [Estimated Accuracy](#estimated_results)
- [Event Correlation Table](#correlation_table)

The distribution of the likelihood scores for the entire prediction audience is displayed at the top of the page. Users in buckets further to the right have higher scores and are more likely to perform the event. Users in buckets further to the left are less likely to perform the event. The slider beneath the chart will allow you to select a section of users and estimate what the results would be of targeting those users.

As you move the slider handles to different positions, the bar in the left half of the panel will inform you how many users out of the entire prediction audience would be targeted using the part of the population you've selected.

![]({% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}){: style="max-width:90%"} 

## Likelihood score {#purchase_score}

Users in the prediction audience will be assigned a likelihood score between 0 and 100. The higher the score, the greater the likelihood of performing the event. 

The following is how a user is categorized depending on their likelihood score:

- **Low:** between 0 and 50
- **Medium:** between 50 and 75
- **High:** between 75 and 100

The scores and the corresponding categories will be updated according to the schedule you chose in the **Prediction Creation** page. The number of users with likelihood scores in each of the 20 equally sized buckets or in each of the likelihood categories, is displayed in the chart at the top of the page.

## Estimated accuracy {#estimated_results}

In the right half of the panel beneath the chart, we show estimates of the expected accuracy of targeting the portion of the prediction audience you selected in two ways: how many selected users are expected to perform the event, and how many are expected not to.

![The selected audience and estimated accuracy shown in the Braze dashboard.]({% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %})

### Expected to perform

You can use the estimated accuracy to check how many selected users are expected to perform the event.

The prediction isn't perfectly accurate, and no prediction ever is, meaning Braze will not be able to identify every single future user to perform the event. The likelihood scores are like a set of informed and reliable predictions. The progress bar indicates how many of "true positives" expected in the prediction audience will be targeted with the audience selected. Note that we expect this number of users to perform the event even if you don't send them a message.

### Not expected to perform

You can use the estimated accuracy to check how many selected users are expected not to perform the event.

All machine learning models make errors. There may be users in your selection who have a high likelihood score but do not end up actually performing the event. They would not perform the event if you took no action. They will be targeted anyway, so this is an error or "false positive." The full width of this second progress bar represents the expected number of users who will not perform the event, and the filled portion is those who will be incorrectly targeted using the current slider position.

Using this information, we encourage you to decide how many of the true positives you want to capture, how many false positives you can accept being targeted, and what the cost of errors is for your business. If you are sending out a valuable promotion, you may want to target only non-purchasers (false positives) by favoring the left side of the chart. Or, you may want to encourage buyers who often purchase (true positives) to do so again by selecting a section of users that favors the right side of the chart.

## Prediction quality {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Event correlation table {#correlation_table}

This analysis displays user attributes or behaviors that are correlated with events in the prediction audience. The attributes assessed are Age, Country, Gender, and Language. Behaviors that are analyzed include sessions, purchases, total dollars spent, custom events, and campaigns and Canvas steps received in the last 30 days.

The tables are split into left and right for more and less likely to perform the event, respectively. For each row, the ratio by which the users with the behavior or attribute in the left column are more or less likely to perform the event is displayed in the right column. This number is the ratio of likelihood scores of users with this behavior or attribute divided by the likelihood to perform the event off the entire prediction audience.

This table is updated only when the prediction retrains and not when user likelihood scores are updated.

{% alert note %}
Correlation data for preview predictions will be partially hidden. A purchase is required to reveal this information. Contact your account manager for more information.
{% endalert %}
