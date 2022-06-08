---
nav_title: Predictive Purchases
article_title: Predictive Purchases
page_order: 6.4
layout: featured
alias: /predictive_purchases/

guide_top_header: "Predictive Purchases"
guide_top_text: "Knowing which of your users is likely to make a purchase is a crucial insight for growing businesses. Without it, how do you decide which campaigns to build? Who should receive discounts and promotions? Where to spend a limited budget? Braze helps answer these questions with Predictive Purchases, a machine learning model that makes it easy for marketing teams to understand future purchasing behavior and focus their resources on revenue-maximizing campaigns."
description: "Predictive Purchases gives marketers a powerful tool for identifying and messaging users based on their likelihood to make a purchase. "

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

## Overview

![Graphic titled "How Predictive Purchases Works". On the left shows user data being funneled into the machine learning model. The label reads "Train with historical data, compare the pre-purchase behaviors of previous purchases with those of potential purchases." On the right shows the results of the machine learning, where users are ranked by least likely to most likely to purchase. The label reads "Predict likelihoos of future purchases, assign a Purchase Likelihood Score to users for accurate, convenient targeting."][1]

Predictive Purchases give marketers a powerful tool for identifying and messaging users based on their likelihood to make a purchase. When you create a Purchase Prediction, Braze trains a machine learning model using [gradient boosted decision trees](https://en.wikipedia.org/wiki/Gradient_boosting) to learn from previous purchase activity and predict future purchase activity. 

Once a Prediction is built, users are assigned a [Purchase Likelihood Score]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#purchase_score) between 0 and 100 denoting how likely they are to make a purchase. The higher the score, the more likely a user is to make a purchase. Users are also sorted by Low, Medium, and High Purchase Likelihood Categories. 

The real value of Predictive Purchases lies using Prediction results to create a Segment or campaign. Marketers can build targeted campaigns directly on the **Prediction** page for immediate revenue-boosting results or save a Segment for a future campaign or Canvas. Not sure who to target first? Read our [strategic considerations]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/messaging_users/#strategy) for messaging users based on their Purchase Likelihood.

## Access Predictive Purchases

The **Predictions** page is accessible from the left navigation bar on the Braze dashboard. For full access, contact your account manager. Prior to purchasing this feature, it is available in Preview mode. This will allow you to see a Demo Purchase Prediction with synthetic data as well as create one Preview Purchase Prediction model at a time. This Prediction will be created based on your actual user data, but it will not allow you to target users for messaging according to Purchase Likelihood. It will also not update regularly after creation.

With the Preview, you can also edit and rebuild this one Prediction or archive it and create others to test the expected [Prediction Quality]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/prediction_analytics/#prediction_quality) of [different audiences]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/#audience) and become familiar with the analytics.

<br><br>

[1]: {% image_buster /assets/img/purchasePrediction/purchasesOverview.png %}

