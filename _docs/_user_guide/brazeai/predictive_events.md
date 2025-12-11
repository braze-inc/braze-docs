---
nav_title: Predictive Events
article_title: Predictive Events
description: "This article covers Predictive Events (previously Predictive Purchases), a Predictive Suite tool that gives marketers the ability to identify and message users based on their likelihood to perform an event."
page_order: 2.1
alias: /predictive_purchases/
search_rank: 1
---

# Predictive Events

> Predictive Events is a powerful tool in the Braze Predictive Suite for identifying and messaging users based on their likelihood to perform an event. When you create an event prediction, Braze trains a machine learning model using [gradient boosted decision trees](https://en.wikipedia.org/wiki/Gradient_boosting) to learn from previous activity and predict future activity.

## About Predictive Events

After a prediction is built, users are assigned a [likelihood score]({{site.baseurl}}/user_guide/brazeai/predictive_events/prediction_analytics/#purchase_score) between 0 and 100 denoting how likely they are to perform your selected event. The higher the score, the more likely a user is to perform that event. Users are also sorted by low, medium, and high likelihood categories.

The real value of Predictive Events lies in using prediction results to create a segment or campaign. Marketers can build targeted campaigns directly on the **Prediction** page for immediate revenue-boosting results or save a segment for a future campaign or Canvas. Not sure who to target first? Read our [strategic considerations]({{site.baseurl}}/user_guide/brazeai/predictive_events/messaging_users/#strategy) for messaging users based on their likelihood score.

![Graphic titled "How Predictive Events Works", displaying user data being funneled into the machine learning model. The label reads "Train with historical data, compare the behavior of users who did perform the event in a certain period with those who didn't." It also shows the results of the machine learning, where users are ranked by least likely to most likely to perform the event. The label reads "Predict likelihood of future events, assign a likelihood score to users for accurate, convenient targeting."]({% image_buster /assets/img/how_predictive_events_works.png %})

## Accessing Predictive Events

The **Predictions** page is located in the **Analytics** section. For full access, contact your account manager.

Prior to purchasing this feature, it is available in preview mode. This will allow you to see a demo prediction with synthetic data as well as create one preview prediction model at a time. This prediction will be created based on your actual user data, but it will not allow you to target users for messaging according to their likelihood score. It will also not update regularly after creation.

With the Preview, you can also edit and rebuild this one prediction or archive it and create others to test the expected [prediction quality]({{site.baseurl}}/user_guide/brazeai/predictive_events/prediction_analytics/#prediction_quality) of [different audiences]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/#audience) and become familiar with the analytics.
