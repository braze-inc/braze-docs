---
nav_title: Predictive Events
article_title: Predictive Events
page_order: 6.4
layout: featured
alias: /predictive_purchases/
search_rank: 1
guide_top_header: "Predictive Events"
guide_top_text: "Knowing which of your users is likely to perform a specific event—like a purchase—is a crucial insight for growing businesses. Without it, how do you decide which campaigns to build? Who should receive discounts and promotions? Where to spend a limited budget? Braze helps answer these questions with Predictive Events (previously Predictive Purchases), a machine learning model that makes it easy for marketing teams to understand future behavior and focus their resources on engagement and revenue-maximizing campaigns."
description: "This article covers Predictive Events (previously Predictive Purchases), a tool that gives marketers the ability to identify and message users based on their likelihood to perform an event."

guide_featured_title: "Topics"
guide_featured_list:
- name: Creating a Prediction
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: Prediction Analytics
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Messaging Users
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg

---

## Overview

![Graphic titled "How Predictive Events Works", displaying user data being funneled into the machine learning model. The label reads "Train with historical data, compare the behavior of users who did perform the event in a certain period with those who didn't." It also shows the results of the machine learning, where users are ranked by least likely to most likely to perform the event. The label reads "Predict likelihood of future events, assign a likelihood score to users for accurate, convenient targeting."][1]

> Predictive Events give marketers a powerful tool for identifying and messaging users based on their likelihood to perform an event. When you create an event prediction, Braze trains a machine learning model using [gradient boosted decision trees](https://en.wikipedia.org/wiki/Gradient_boosting) to learn from previous activity and predict future activity.

Once a prediction is built, users are assigned a [likelihood score]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) between 0 and 100 denoting how likely they are to perform your selected event. The higher the score, the more likely a user is to perform that event. Users are also sorted by low, medium, and high likelihood categories.

The real value of Predictive Events lies in using prediction results to create a segment or campaign. Marketers can build targeted campaigns directly on the **Prediction** page for immediate revenue-boosting results or save a segment for a future campaign or Canvas. Not sure who to target first? Read our [strategic considerations]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) for messaging users based on their likelihood score.

## Access Predictive Events

The **Predictions** page is located in the **Analytics** section. For full access, contact your account manager.

Prior to purchasing this feature, it is available in preview mode. This will allow you to see a demo prediction with synthetic data as well as create one preview prediction model at a time. This prediction will be created based on your actual user data, but it will not allow you to target users for messaging according to their likelihood score. It will also not update regularly after creation.

With the Preview, you can also edit and rebuild this one prediction or archive it and create others to test the expected [prediction quality]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) of [different audiences]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) and become familiar with the analytics.

<br><br>

[1]: {% image_buster /assets/img/how_predictive_events_works.png %}

