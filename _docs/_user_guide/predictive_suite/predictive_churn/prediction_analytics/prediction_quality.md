---
nav_title: Prediction Quality
title: Prediction Quality
description: "This reference article takes an in-depth look at the prediction quality metric located on the Prediction Analytics Page."
page_order: 1
---

# Prediction Quality

To measure the accuracy of your model, the __Prediction Quality__ metric will show you how effective this particular machine learning model appears to be when tested on historical data. Braze pulls data according to the groups you specified in the model creation page. The model is trained on one data set (the “training” set) and then tested on a new, separate data set (the “test” set). 

Our measure of Prediction Quality is [Lift Quality](https://dl.acm.org/doi/10.1145/380995.381018). You are probably familiar with "lift", which often measures the increase, as a ratio or percentage, of some successful outcome like a conversion. In this case, the successful outcome is correctly identifying a user who would have churned. Lift Quality is the average lift the Prediction provides across all possible audience sizes for messaging the test set. This approach measures how much better than random guessing the model is. With this measure, 0% means the model is no better than randomly guessing about who will churn, and 100% indicates perfect knowledge of who will churn.

Here’s what we recommend for various ranges of Prediction Quality:

| Prediction Quality Range (%) | Recommendation |
| ---------------------- | -------------- |
| 60 - 100 | Excellent. Top tier accuracy. Changing the audience definitions is unlikely to provide additional benefit. |
| 40 - 60 | Good. This model will produce accurate predictions, but trying different audience settings may achieve even better results. |
| 20 - 40| Fair. This model can provide accuracy and value, but consider trying different audience definitions to see if they increase performance. |
| 0 - 20 | Poor. We recommend you change your audience definitions and try again. |
{: .reset-td-br-1 .reset-td-br-2}

The Prediction will be trained again every two weeks and updated alongside the Prediction Quality metric to keep your predictions updated on the most recent user behavior patterns. The last time this retraining occurred will be displayed on the Predictions list page as well as on an individual Prediction's analytics page.

>__Prediction Quality Details__ <br><br> Example: If 20% of your users usually churn on average, and you pick a random subset of 20% of your users and label them as churned at random (whether they truly are or not), you’d expect to correctly identify only 20% of the actual churners. That's random guessing. If the model were to only do that well, the lift would be 1 for this case.<br> If the model, on the other hand, allowed you to message 20% of the users and, in doing so capture all the “true” churners and no one else, the lift would be 100% / 20% = 5. If you chart this ratio for every proportion of the likeliest churners you could message, you get the [Lift Curve](https://towardsdatascience.com/the-lift-curve-unveiled-998851147871). <br><br>Another way to think of Lift Quality (and also Prediction Quality) is how far along the way between random guessing (0%) and perfection (100%) the Prediction's lift curve is at identifying churners on the test set. For the original paper on Lift Quality see [here](https://dl.acm.org/doi/10.1145/380995.381018).

