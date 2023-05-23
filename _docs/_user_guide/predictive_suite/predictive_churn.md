---
nav_title: Predictive Churn
article_title: Predictive Churn
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "Predictive Churn"
guide_top_text: "Customer churn, also known as customer turnover or client loss, is one of the most important metrics for growing businesses to consider. Having the right tools to address churn is crucial in minimizing loss and maximizing customer retention. To get a jump on these potentially churning users, Braze offers Predictive Churn, providing a proactive approach toward minimizing future churn."
description: "This landing page covers Predictive Churn, a tool that allows you to define what churn means for your business as well as the users you'd like to prevent from churning."

guide_featured_title: "Topics"
guide_featured_list:
- name: Creating A Churn Prediction
  link: /docs/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/
  fa_icon: fas fa-cogs
- name: Prediction Analytics
  link: /docs/user_guide/predictive_suite/predictive_churn/prediction_analytics/
  fa_icon: fas fa-chart-bar
- name: Messaging Users
  link: /docs/user_guide/predictive_suite/predictive_churn/messaging_users/
  fa_icon: fas fa-arrow-right
- name: Troubleshooting
  link: /docs/user_guide/predictive_suite/predictive_churn/prediction_faq/
  fa_icon: fas fa-question

---

## Overview

![An overview of churn, which includes a past prediction audience with training with historical data. This contributes to predicting risk for future churn by measuring today's predicted audience with a churn risk score.][1]

> With Predictive Churn, you can define what churn means for your business ([churn definition]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)), and the users you'd like to prevent from churning ([Prediction audience]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)). When you create a Prediction, Braze trains a machine learning model using [gradient boosted decision trees](https://en.wikipedia.org/wiki/Gradient_boosting) to identify users at risk of churn by learning from activity patterns of past users who did and did not churn according to your definition.

Once the Prediction model is built, users in the Prediction audience will be assigned a [churn risk score]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/#churn_score) between 0 and 100 denoting how likely they are to churn according to your definition. The higher the score, the more likely a user is to churn. 

Updating the risk scores of the Prediction audience can be done at a [frequency you choose]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions). This way, you can reach out to users who are at risk of churning before they actually do and prevent it from happening in the first place. Using up to three active Predictions, you can leverage Predictive Churn to tailor individual models to help prevent churn within specific segments of your users that you deem to be the most valuable.

## Access Predictive Churn

The **Predictions** page is located in the **Analytics** section. For full access, contact your account manager.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Predictions** under **Engagement**.
{% endalert %}

Prior to purchasing this feature, it is available in preview mode. This will allow you to see a demo Churn Prediction with synthetic data and create one Churn Prediction model based on your user data at a time. This preview will not allow you to target users for messaging according to churn risk and will not regularly update after creation.

With the preview, you can also edit and rebuild your one Prediction or archive it and create others to test the expected [Prediction quality]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) of different [definitions]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
