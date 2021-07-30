---
nav_title: Creating A Purchase Prediction
title: Creating A Purchase Prediction
description: ""
page_order: 1

description: "This article covers how to create a Purchase Prediction within the Braze dashboard."
Tool:
  - Dashboard
---

# Creating A Purchase Prediction

On the left navigation bar of the Braze dashboard, choose the __Predictions__ page. A Prediction is one instance of a trained machine learning model and all the parameters and data it uses. On this page, you will see a list of current active Predictions along with some basic info about them. Here you can rename, archive, and create new Predictions. Archived predictions are inactive and do not update user scores. 

To create a new Prediction, choose “Create Prediction” in the upper right corner, and select a new “Purchase Prediction.”

{% alert note %}
There is a limit of 3 concurrently active Purchase Predictions. Prior to purchasing Predictive Purchases, the limit is 1 active Preview Purchase Prediction. A Preview Purchase Prediction will not regularly update scores or allow you to target users based on the Prediction's output. Contact your Account Manager for details.
{% endalert %}

### Step 1: Create a New Prediction

![Purchase 1][1]

On the first page, give your new Prediction a unique name. You can also optionally provide a description to save any relevant notes.

Click Forward to move to the next step. Optionally, you can click Build Now to skip to use all the default settings and skip to the last step of creation. You will have a chance to review the settings before starting the Build process. Also, you can return to any step later by clicking it in the top bar. 

### Step 2: Purchase Tracking

On this page, specify if your users' purchases are stored on Braze as standard [purchase events](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events) or a [custom event](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_events/).

On this page, you'll see if the specific Purchase method provides enough data for Braze to create a machine learning model. If the requirement is not met, try and select the other logging method above if it is used by your application. If it is not, unfortunately Braze is unable to create a Prediction with the quantity of data available. If you believe you're incorrectly seeing this error, please contact your CSM.

### Step 3: Filter Your Prediction Audience (optional) {#audience}

Your Prediction Audience is the group of users whose Purchase likelihood you would like to predict. Purchase Prediction allows you to run a Prediction on your entire population of users. To do this, leave the default option, "All Users", selected.

The model will likely perform better if you filter the group of users you want to assess with some criteria. To do so, select "Define my own prediction audience" and choose your audience filters. For example, you might want to focus on users who been using your app for at least 30 days, so you would use the "First Used App" filter set to 30 days. 

The Prediction Audience definition is also used to query historical data that will allow the machine learning model to learn from the past. Like on the previous page, the quantity of data provided by these filters is displayed along with the requirement. If you specify your desired audience and do not meet the minimum, try specifying a broader filter or use the "All Users" option.

{% alert note %}
The Prediction Audience cannot exceed 100 million users.
{% endalert %}

For filters that begin with “Last...” like Last Used App and Last Made Purchase, the time window to look back for these filters __cannot exceed 16 days__.

### Step 4: Choose the Update Frequency for Purchase Predictions

The machine learning model created when you complete this page will be used on a schedule you select here to generate fresh scores of users’ probability to Purchase. Please select the __maximum frequency of updates__ that you’ll find useful. For example, if you’re going to send a weekly promotion to prevent users from Purchasing, set the update frequency to __Weekly__ on the day and time of your choosing. 

{% alert note %}
Preview and Demo Predictions will never update users' likelihood to Purchase. 
{% endalert %}

### Step 5: Build Prediction
Verify that the details you’ve provided are correct, and choose “Build Prediction.” You can also save your changes in draft form by selecting “Save As Draft” to return to this page and build the model later. Once you click __Build Prediction__, the process that generates the model will begin. This could take between 30 minutes to a few hours depending on data volumes. For this Prediction, you will see a page explaining that training is in progress for the duration of the model building process.

Once it’s done, the page will switch to the Analytics view automatically, and you will also get an email informing you that the Prediction and results are ready. In the event of an error, the page will return to the Editing mode with an explanation of what went wrong.

The Prediction will be rebuilt ("retrained") again every __two weeks automatically__ to keep it updated on the most recent data available. Note that this is a separate process from when users' Purchase Likelihood Scores, the output of the Prediction, are produced. The latter is determined by the update frequency you chose in Step 4.

## Archived Predictions

Archived Predictions will cease updating user scores. Any archived Prediction that is unarchived will continue updating user scores on its predetermined schedule. Archived Predictions are never deleted and remain in the list.

[1]: {% image_buster /assets/img/purchasePrediction/purchasesStep1.png %}

