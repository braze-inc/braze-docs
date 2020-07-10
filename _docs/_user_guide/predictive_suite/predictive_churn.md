---
nav_title: Predictive Churn
page_order: 6.4
layout: featured
alias: /predictive_churn/

guide_top_header: "Predictive Churn"
guide_top_text: "Customer Churn, also known as customer turnover or client loss, is one of the most important metrics for growing businesses to consider. Having the right tools to address churn is crucial in minimizing loss and maximizing customer retention. To get a jump on these potentially churning users, Braze offers Predictive Churn, providing a proactive approach toward minimizing future churn."

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
---

## Overview

![Churn Overview][1]

With Predictive Churn, you can define what churn means for your business (__[Churn Definition]({{site.baseurl}}\/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)__) as well as the users you'd like to prevent from churning (__[Prediction Audience]({{site.baseurl}}\/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)__). When you build the Prediction, Braze will train a machine learning model to predict churn by comparing the churn behaviors of users in the historical Prediction Audience to your churn definition. 

Once the Prediction model is built and done training, users that currently fit the definition of the Prediction Audience will be assigned a __[Churn Risk Score]({{site.baseurl}}\/user_guide/predictive_suite/predictive_churn/prediction_analytics/#churn_score)__ between 0 and 100 denoting how likely they are to Churn according to your definition. The higher the score, the more likely a user is to churn. 

Updating the risk scores of the Prediction Audience can be done with a __[frequency you choose]({{site.baseurl}}\/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions)__. This way, you can reach out to users who are at risk of Churning before they actually do and prevent it from happening in the first place.

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
