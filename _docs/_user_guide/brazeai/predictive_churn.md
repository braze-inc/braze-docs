---
nav_title: Predictive Churn
article_title: Predictive Churn
description: "This landing page covers Predictive Churn, a tool in the Braze Predictive Suite that allows you to define what churn means for your business as well as the users you'd like to prevent from churning."
page_order: 2.0
alias: /predictive_churn/
search_rank: 2
---

# Predictive Churn

> With Predictive Churn, a tool in the Braze Predictive Suite, you can define what churn means for your business and identify the users you want to retain. When you create a prediction, Braze trains a machine learning model using [gradient boosted decision trees](https://en.wikipedia.org/wiki/Gradient_boosting) to recognize at-risk users by analyzing patterns from past behavior—both from users who churned and those who didn’t.

{% alert tip %}
For more information, see [Churn definition]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) and [Prediction audience]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## About Predictive Churn

After the prediction model is built, users in the prediction audience will be assigned a [churn risk score]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) between 0 and 100 denoting how likely they are to churn according to your definition. The higher the score, the more likely a user is to churn. 

Updating the risk scores of the prediction audience can be done at a [frequency you choose]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-prediction). This way, you can contact users who are at risk of churning before they actually do and prevent it from happening in the first place. Using up to three active predictions, you can leverage Predictive Churn to tailor individual models to help prevent churn within specific segments of your users that you deem to be the most valuable.

![An overview of churn, which includes a past prediction audience with training with historical data. This contributes to predicting risk for future churn by measuring today's predicted audience with a churn risk score.]({% image_buster /assets/img/churn/churn_overview.png %})

## Accessing Predictive Churn

The **Predictions** page is located in the **Analytics** section. For full access, contact your account manager.

Prior to purchasing this feature, it is available in preview mode. This will allow you to see a demo churn prediction with synthetic data and create one churn prediction model based on your user data at a time. This preview will not allow you to target users for messaging according to churn risk and will not regularly update after creation.

With the preview, you can also edit and rebuild your one prediction or archive it and create others to test the expected [prediction quality]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) of different [definitions]({{site.baseurl}}/user_guide/brazeai/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).
