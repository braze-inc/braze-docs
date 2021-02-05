---
nav_title: Predictive Purchases
page_order: 6.4
layout: featured
alias: /predictive_purchases/
hidden: true
guide_top_header: "Predictive Purchases"
guide_top_text: "NEEDS REVISION Customer purchase, also known as customer turnover or client loss, is one of the most important metrics for growing businesses to consider. Having the right tools to address purchase is crucial in minimizing loss and maximizing customer retention. To get a jump on these potentially purchaseing users, Braze offers Predictive purchase, providing a proactive approach toward minimizing future purchase."

guide_featured_title: "Topics"
guide_featured_list:
- name: Creating A Purchase Prediction
  link: /docs/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/
  fa_icon: fas fa-cogs
- name: Prediction Analytics
  link: /docs/user_guide/predictive_suite/predictive_purchases/prediction_analytics/
  fa_icon: fas fa-chart-bar
- name: Messaging Users
  link: /docs/user_guide/predictive_suite/predictive_purchases/messaging_users/
  fa_icon: fas fa-arrow-right
---

## Overview NEEDS REVISION

![Churn Overview][1]

With Predictive purchase, you can define what purchase means for your business (__[purchase Definition]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchase/creating_a_purchase_prediction/#step-2-define-purchase)__) as well as the users you'd like to prevent from purchaseing (__[Prediction Audience]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchase/creating_a_purchase_prediction/#step-3-filter-your-prediction-audience)__). When you create a Prediction, Braze trains a machine learning model using __[gradient boosted decision trees](https://en.wikipedia.org/wiki/Gradient_boosting)__ to identify users at risk of purchase by learning from activity patterns of past users who did and did not purchase according to your definition.

Once the Prediction model is built, users in the Prediction Audience will be assigned a __[Purchaser Likelihood Risk Score]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#purchase_score)__ between 0 and 100 denoting how likely they are to purchase according to your definition. The higher the score, the more likely a user is to purchase. 

Updating the risk scores of the Prediction Audience can be done with a __[frequency you choose]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/#step-3-choose-the-update-frequency-for-purchase-predictions)__. This way, you can reach out to users who are at risk of purchaseing before they actually do and prevent it from happening in the first place. Using up to three active Predictions, you can leverage Predictive purchase to tailor individual models to help prevent purchase within specific segments of your users that you deem to be the most valuable.

## Access Predictive purchase

The Predictions page is accessible from the left navigation bar on the Braze dashboard. For full access, contact your Account Manager. Prior to purchasing this feature, it is available in Preview mode. This will allow you to see a Demo purchase Prediction with synthetic data as well as create one purchase Prediction model at a time. This Prediction will be created based on your actual user data, but it will not allow you to target users for messaging according to purchase Risk. It will also not update regularly after creation.

With the Preview, you can also edit and rebuild this one Prediction or archive it and create others to test the expected [Prediction Quality]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchase/prediction_analytics/prediction_quality/) of different audiences ({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/#step-2-define-purchase).

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}

