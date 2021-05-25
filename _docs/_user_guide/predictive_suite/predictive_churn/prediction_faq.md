---
nav_title: Frequently Asked Questions
title: Frequently Asked Questions
description: "This reference article covers some frequently asked questions customers have while using predictive churn."
page_order: 3

Tool:
  - Dashboard
---

# Frequently Asked Questions

> Predictive Churn, and any machine learning model, is only as good as the data available to the model. It also is highly dependent on having certain volumes of data to work with. This means that users may encounter some error messages, or low Prediction Quality, as they're getting to know this new feature. 

## Potential Errors

### Not Enough Data to Train 

This error message appears when your churn definition is too limiting and returns too few Churned users. 

To fix this, you will need to change either the number of days and/or actions that define churn to capture more users. Make sure you are using AND/OR correctly so as to not create overly restrictive definitions. 

{% alert important %}
Note that while Predictive Churn is turned on at a company level, some App Groups may not have enough users to build predictions.  The typical recommendation is to have at least 500k MAU to guarantee there will be enough. 
{% endalert %}

### Problems with Prediction Audience Size
![Predicition Size][3]{: style="float:right;max-width:60%;margin-left:15px;margin-bottom:15px;margin-top:15px;"}

When building out your Prediction Audience to fine-tune the kind of use you want your model trained against, you might encounter this message notifying you your Prediction Audience has too few users. 

If your Prediction Audience definition is too strict, you might not have a large enough pool of both historic and active users to work with. 

To fix this, you will need to either change the number of days and type of attributes used in this definition and/or switch up the actions that define churn. 

If your Prediction Audience continues to be a problem even after switching up your definitions, you may have too few users to support this optional feature. We would suggest trying to build a prediction without the extra layers and filters instead. 

### Prediction Audience Size is too Big

A Prediction Audience definition cannot exceed 40 million users. If you see a message saying your audience is too large, then we recommend adding more layers to your audience and/or changing the window of time it's based on.

### Prediction has Poor Quality
![Predicition Quality][1]{: style="float:right;max-width:40%;margin-left:15px;"}
If your model has a prediction quality of 40% and above, you are in a great place! But if your prediction quality drops to 39% and below, you may need to edit your Churn, and Prediction Audience definitions to be more specific or have different time windows. 

If you are unable to meet both the audience size requirement while building your prediction definitions and achieve a Prediction Quality of greater than 40%, it likely means that the data sent to Braze is not ideal for this use case, that there are not enough users with which to build a model against, or that your product lifecycle is longer than our current 30-day lookback window supports. 

## Timing Clarifications

You can look back up to 14 days for your churn prediction. Your "churn" definition and time window for any Last Made Purchase / Last Used App / Last Did Custom Event filters in the Prediction Audience definition cannot add up to more than 30 days.

For example, if you define churn as not starting a session in the past ten days, then your Prediction Audience can be based on up to 20 days of data. 

## Data Considerations

Listed below are some questions to ask yourself as you set up Predictive Churn. Machine learning models are only as good as the data that trains them, so having good data hygiene practices and understanding what goes into the model will make a big difference.

- What high-value actions lead to retention and loyalty?
- Have you set up custom events that map back to these specific actions? Predictive Churn works with custom events as opposed to custom attributes.
- Are you thinking in "Short Windows" of time within which you'll denim churn. Predictive churn has a lookback window of 14 days. 
- Have you considered times of the year that lead to atypical user behaviors - like holidays. Rapid shifts in consumer behavior will impact your predictions. 

[1]: {% image_buster /assets/img/churn/churn3.png %}
[3]: {% image_buster /assets/img/churn/churn5.png %}