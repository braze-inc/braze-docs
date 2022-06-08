---
nav_title: Troubleshooting
article_title: Predictive Churn Troubleshooting
description: "This reference article covers some troubleshooting steps and considerations to keep in mind while using Predictive Churn."
page_order: 3

---

# Predictive Churn Troubleshooting

> Predictive Churn (and any machine learning model) is only as good as the data available to the model. it also is highly dependent on having certain volumes of data to work with. this means that users may encounter some error messages, or low prediction quality, as they're getting to know this new feature. 

## Potential errors

### Not enough data to train 

This error message appears when your churn definition is too limiting and returns too few Churned users. 

To fix this, you will need to change either the number of days and/or actions that define churn to capture more users. Make sure you are using `AND/OR` filters correctly so as to not create overly restrictive definitions. 

{% alert important %}
While Predictive Churn is turned on at a company level, some app groups may not have enough users to build predictions. Typically, you need 300,000 Monthly Active Users in a single app group.
{% endalert %}

### Problems with prediction audience size

![][3]{: style="float:right;max-width:60%;margin-left:15px;margin-bottom:15px;margin-top:15px;"}

When building out your Prediction Audience to fine-tune the kind of use you want your model trained against, you might encounter this message notifying you your Prediction Audience has too few users: 

"Not enough past churners availble from the selected Prediction Audience in the past 7 days to reliably build the Prediction."

If your Prediction Audience definition is too strict, you might not have a large enough pool of both historic and active users to work with. To fix this, you will need to either change the number of days and type of attributes used in this definition and/or switch up the actions that define churn. 

If your Prediction Audience continues to be a problem even after switching up your definitions, you may have too few users to support this optional feature. We would suggest trying to build a prediction without the extra layers and filters instead. 

### Prediction audience size is too big

A Prediction Audience definition cannot exceed 100 million users. If you see a message saying your audience is too large, then we recommend adding more layers to your audience and/or changing the window of time it's based on.

### Prediction has poor quality

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}
If your model has a [prediction quality]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) of 40% or greater, you are in a great place! But if your prediction quality drops to 39% or less, you may need to edit your Churn and Prediction Audience definitions to be more specific or have different time windows. 

If you are unable to meet both the audience size requirement while building your prediction definitions and achieve a prediction quality of greater than 40%, it likely means that the data sent to Braze is not ideal for this use case, that there are not enough users with which to build a model against, or that your product lifecycle is longer than our current 30-day lookback window supports. 

## Timing clarifications

You can look back up to 14 days for your churn prediction. Your "churn" definition and time window for any `Last Made Purchase` / `Last Used App` / `Last Did Custom Event` filters in the Prediction Audience definition cannot add up to more than 30 days.

For example, if you define churn as not starting a session in the past ten days, then your Prediction Audience can be based on up to 20 days of data. 

## Data considerations

The following lists some questions to ask yourself as you set up Predictive Churn. Machine learning models are only as good as the data that trains them, so having good data hygiene practices and understanding what goes into the model will make a big difference.

- What high-value actions lead to retention and loyalty?
- Have you set up custom events that map back to these specific actions? Predictive Churn works with custom events as opposed to custom attributes.
- Are you thinking in windows of time within which you'll define churn? You can define churn as something that happens in up to 14 days.
- Have you considered times of the year that lead to atypical user behaviors - like holidays. Rapid shifts in consumer behavior will impact your predictions. 

[1]: {% image_buster /assets/img/churn/churn3.png %}
[3]: {% image_buster /assets/img/churn/audience_size_error.png %}