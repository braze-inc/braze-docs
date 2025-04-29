---
nav_title: Troubleshooting
article_title: Predictive Churn Troubleshooting
description: "This reference article covers some troubleshooting steps and considerations to keep in mind while using Predictive Churn."
page_order: 3

---

# Troubleshooting

> Predictive Churn (and any machine learning model) is only as good as the data available to the model. It also is highly dependent on having certain volumes of data to work with. 

## Potential errors

### Not enough data to train 

This error message appears when your churn definition is too limiting and returns too few churned users. 

To fix this, you will need to change either the number of days and/or actions that define churn to capture more users. Make sure you are using `AND/OR` filters correctly so as to not create overly restrictive definitions. 

{% alert important %}
While Predictive Churn is turned on at a company level, some workspaces may not have enough users to build predictions. Typically, you need 300,000 Monthly Active Users in a single workspace.
{% endalert %}

### Problems with prediction audience size

When building out your prediction audience to fine-tune the kind of use you want your model trained against, you might encounter this message notifying you your prediction audience has too few users: 

"Not enough past non-churners to reliably build the Prediction"

![Prediction data requirements showing 31 past churners (meets requirement) and 0 past non-churners (below minimum). A warning message indicates not enough non-churners to build the prediction.][3]

If your prediction audience definition is too strict, you might not have a large enough pool of both historic and active users to work with. To fix this, you will need to either change the number of days and type of attributes used in this definition, switch up the actions that define churn, or both. 

If your prediction audience continues to be a problem even after switching up your definitions, you may have too few users to support this optional feature. We would suggest trying to build a prediction without the extra layers and filters instead. 

### Prediction audience size is too big

A prediction audience definition cannot exceed 100 million users. If you see a message saying your audience is too large, then we recommend adding more layers to your audience or changing the window of time it's based on.

### Prediction has poor quality

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}
If your model has a [prediction quality]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) of 40% or greater, you are in a great place! But if your prediction quality drops to 39% or less, you may need to edit your churn and prediction audience definitions to be more specific or have different time windows. 

If you are unable to meet both the audience size requirement while building your prediction definitions and achieve a prediction quality of greater than 40%, it likely means that the data sent to Braze is not ideal for this use case, that there are not enough users with which to build a model against, or that your product life cycle is longer than our current 60-day lookback window supports. 

## Data considerations

The following are questions to ask yourself as you set up Predictive Churn. Machine learning models are only as good as the data that trains them, so having good data hygiene practices and understanding what goes into the model will make a big difference.

- What High-Value Actions lead to retention and loyalty?
- Have you set up custom events that map back to these specific actions? Predictive Churn works with custom events as opposed to custom attributes.
- Are you thinking in windows of time within which you'll define churn? You can define churn as something that happens in up to 60 days.
- Have you considered times of the year that lead to atypical user behaviors such as holidays? Rapid shifts in consumer behavior will impact your predictions. 

[1]: {% image_buster /assets/img/churn/churn3.png %}
[3]: {% image_buster /assets/img/churn/audience_size_error.png %}
