---
nav_title: Creating A Purchase Prediction
title: Creating A Purchase Prediction
description: ""
page_order: 1
---

# Creating A Purchase Prediction

### Step 1: Create a New Prediction
On the left navigation bar of the Braze dashboard, choose the __Predictions__ page. A Prediction is one instance of a trained machine learning model and all the parameters and data it uses. On this page, you will see a list of current active Predictions along with some basic info about them. Here you can rename, archive, and create new Predictions. Archived predictions are inactive and do not update user scores. 

To create a new Prediction, choose “Create Prediction” in the upper right corner, and select a new “Purchase Prediction.”

{% alert note %}
There is a limit of 3 concurrently active Purchase Predictions. Prior to purchasing Predictive Purchase, the limit is 1 active Preview Purchase Prediction. A Preview Purchase Prediction will not regularly update scores or allow you to target users based on the Prediction's output. Contact your Account Manager for details.
{% endalert %}

On the Edit page, give your new Prediction a unique name.

### Step 2: Filter Your Prediction Audience (optional)

Your Prediction Audience is the group of users whose chances of making a purchase you want the Prediction assess. You can try to predict Purchases as defined above in your entire population of users, the model will likely perform better if you narrow down and filter the group of users you want to prevent from Purchaseing with some criteria. Think about the specific users who mean the most to you that you’d like to retain and define them here. For example, you might want to retain users who first used the app more than a month ago or have ever made a purchase. 

{% alert note %}
The Prediction Audience cannot exceed 40 million users.
{% endalert %}

For filters that begin with “Last...” like Last Used App and Last Made Purchase, the time window to look back for these filters __cannot exceed 30 days minus the number of days of the window specified__ in the Purchase Definition. For example, if your Purchase definition has a window of 14 days, the time window for the “Last...” filters cannot exceed 30 - 14 = 16 days.

For a sample list of Prediction Audience definitions, check out our sample definitions at the [bottom of this page](#sample-definitions).

### Step 3: Choose the Update Frequency for Purchase Predictions

The machine learning model created when you complete this page will be used on a schedule you select here to generate fresh scores of users’ probability to Purchase. Please select the __maximum frequency of updates__ that you’ll find useful. For example, if you’re going to send a weekly promotion to prevent users from Purchaseing, set the update frequency to __Weekly__ on the day and time of your choosing. 

![Purchase 2][2]

{% alert note %}
Preview and Demo Predictions will never update users' risk of Purchase. Additionally, daily updates for predictions require an additional purchase beyond Weekly or Monthly updates with Predictive Purchase. To purchase this functionality, contact your Account Manager. 
{% endalert %}

### Step 4: Build Prediction
Verify that the details you’ve provided are correct, and choose “Build Prediction.” You can also save your changes in draft form by selecting “Save As Draft” to return to this page and build the model later. Once you click __Build Prediction__, the process that generates the model will begin. This could take between 30 minutes to a few hours depending on data volumes. For this Prediction, you will see a page explaining that training is in progress for the duration of the model building process.

Once it’s done, the page will switch to the Analytics view automatically, and you will also get an e-mail informing you that the Prediction and results are ready. In the event of an error, the page will return to the Editing mode with an explanation of what went wrong.

The Prediction will be rebuilt ("retrained") again every __two weeks automatically__ to keep it updated on the most recent data available. Note that this is a separate process from when users' Purchase Risk Scores, the output of the Prediction, are produced. The latter is determined by the update frequency you chose in Step 3.

## Archived Predictions

Archived Predictions will cease updating user scores. Any archived Prediction that is unarchived will continue updating user scores on its predetermined schedule. Archived Predictions are never deleted and remain in the list.

[1]: {% image_buster /assets/img/Purchase/Purchase1.png %}
[2]: {% image_buster /assets/img/Purchase/Purchase2.png %} 

