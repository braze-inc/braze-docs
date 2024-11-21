---
nav_title: Prediction Quality
title: Prediction Quality
description: "This reference article takes an in-depth look at the prediction quality metric located on the Prediction Analytics Page."
page_order: 1
Tool:
  - Dashboard
---

# Prediction quality

> To measure the accuracy of your model, the _Prediction Quality_ metric will show you how effective this particular machine learning model appears to be when tested on historical data. Braze pulls data according to the groups you specified in the model creation page. The model is trained on one data set (the "training" set) and then tested on a new, separate data set (the "test" set). 

Our measure of _Prediction Quality_ is [lift quality](https://dl.acm.org/doi/10.1145/380995.381018). You're probably familiar with "lift," which often measures the increase, as a ratio or percentage, of some successful outcome like a conversion. In this case, the successful outcome is correctly identifying a user who would have churned. Lift quality is the average lift the prediction provides across all possible audience sizes for messaging the test set. This approach measures how much better than random guessing the model is. With this measure, 0% means the model is no better than randomly guessing about who will churn, and 100% indicates perfect knowledge of who will churn.

Here's what we recommend for various ranges of _Prediction Quality_:

| Prediction Quality Range (%) | Recommendation |
| ---------------------- | -------------- |
| 60 - 100 | Excellent. Top tier accuracy. Changing the audience definitions is unlikely to provide additional benefit. |
| 40 - 60 | Good. This model will produce accurate predictions, but trying different audience settings may achieve even better results. |
| 20 - 40| Fair. This model can provide accuracy and value, but consider trying different audience definitions to see if they increase performance. |
| 0 - 20 | Poor. We recommend you change your audience definitions and try again. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The prediction will be trained again every two weeks and updated alongside the _Prediction Quality_ metric to keep your predictions updated on the most recent user behavior patterns. Additionally, each time this occurs, the last two weeks of predictions will be tested against actual user outcomes. The _Prediction Quality_ will then be calculated based on these real outcomes (rather than estimates). This is an automatic backtest (that is, testing a predictive model on historical data) to ensure the prediction is accurate in real-world scenarios. The last time this retraining and backtesting occurred will be displayed on the **Predictions** page and an individual prediction's analytics page. Even a preview prediction will perform this backtest once after its creation. This way, you can be sure of the accuracy of your customized prediction even with the free version of the feature.

{% details Prediction Quality details %}

For example, if 20% of your users usually churn on average, and you pick a random subset of 20% of your users and label them as churned at random (whether they truly are or not), you'd expect to correctly identify only 20% of the actual churners. That's random guessing. If the model were to only do that well, the lift would be 1 for this case.

If the model, on the other hand, allowed you to message 20% of the users and, in doing so capture all the "true" churners and no one else, the lift would be 100% / 20% = 5. If you chart this ratio for every proportion of the likeliest churners you could message, you get the [Lift Curve](https://towardsdatascience.com/the-lift-curve-unveiled-998851147871). 

Another way to think of lift quality (and also _Prediction Quality_) is how far along the way between random guessing (0%) and perfection (100%) the prediction's lift curve is at identifying churners on the test set. For the original paper on lift quality, see [Measuring lift quality in database marketing](https://dl.acm.org/doi/10.1145/380995.381018).

{% enddetails %}
