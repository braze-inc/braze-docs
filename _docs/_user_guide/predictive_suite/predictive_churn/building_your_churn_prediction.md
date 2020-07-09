---
nav_title: Building your Churn Prediction
title: Building your Churn Prediction
description: ""
page_order: 1
---

# Predictive Churn
> Customer Churn, also known as customer turnover or client loss, is one of the most important metrics for growing businesses to consider. Having the right tools to address churn is crucial in minimizing loss and maximizing customer retention. To get a jump on these potentially churning users, Braze offers Predictive Churn, providing a proactive approach toward minimizing future churn.

![Churn Overview][3]

With Predictive Churn, you can define what churn means for your business ([Churn Definition](#step-2-define-churn)) as well as the users you'd like to prevent from churning ([Prediction Audience](#step-3-choose-the-users-you-want-to-keep-from-churning)). When you build the Prediction, Braze will train a machine learning model to predict churn by comparing the behaviors of users in the historical Prediction Audience who did or did not churn according to your definition. 

Once the Prediction model is built and done training, users that currently fit the definition of the Prediction Audience will be assigned a Churn Risk Score between 0 and 100 denoting how likely they are to Churn according to your definition. The higher the score, the more likely a user is to churn. 

Updating the risk scores of the Prediction Audience can be done with a [frequency you choose](#step-4-choose-the-update-frequency-for-churn-predictions). This way, you can reach out to users who are at risk of Churning before they actually do and prevent it from happening in the first place.

## Step 1: Create a New Prediction
On the left navigation bar of the Braze dashboard, choose the Predictions page.  A Prediction is one instance of a trained machine learning model and all the parameters and data it uses. On this page, you will see a list of current active Predictions along with some basic info about them. Here you can rename, archive, and create new Predictions. Archived predictions are inactive and do not update user scores. 

To create a new Prediction, choose “Create Prediction” in the upper right corner, and select a new “Churn Prediction.”

{% alert note %}
There is a limit of 3 concurrently active Churn Predictions.
{% endalert %}

On the Edit page, give your new Prediction a unique name.

## Step 2: Define Churn
In the Churn Definition panel, use the provided filters to define what churn means for your business. In other words, what does a user have to do in what time frame for you to consider them churned? Remember, you don’t need to explain what behaviors might precede churn-- only what makes a user a churned user. This should also generally be a description of what behavior a user does or doesn't do to churn as opposed to an attribute a user has.     For example, you might consider users who haven’t opened your app in 7 days to be churned. 

To implement this example, enter 7 days in the time window at the top of the panel.

![Churn 1][1]

Then, use the available filters to select which behaviors in that time frame constitute churn. For this case, select "do not" and "start a session". You can combine other filters with "and" and "or" as you see fit to create the definition you need. Uninstalling, making or not making purchases, or performing or not performing particular custom events are other filters you can include.

Interested in some potential churn definitions to consider? You’ll find some inspiration at the [bottom of this page](#sample-definitions).

## Step 3: Choose the Users you Want to Keep from Churning
Although you can try to prevent churn as defined above in your entire population of users, the model will likely perform better if you narrow down the group of users you want to prevent from churning with some criteria. Think about the specific users who mean the most to you that you’d like to retain and define them here. For example, you might want to retain users who first used the app more than a month ago or have ever made a purchase. 

{% alert note %}
The Prediction Audience cannot exceed 40 million users.
{% endalert %}

For filters that begin with “Last...” like Last Used App and Last Made Purchase, the time window to look back for these filters cannot exceed 30 days minus the number of days of the window specified in the Churn Definition. For example, if your Churn definition has a window of 14 days, the time window for the “Last...” filters cannot exceed 30 - 14 = 16 days.

For a sample list of Prediction Audience definitions, check out the [bottom of the page](#sample-definitions)! 

## Step 4: Choose the Update Frequency for Churn Predictions

The machine learning model created when you complete this page will be used on a schedule you select here to generate fresh scores of users’ probability to churn. Please select the maximum frequency of updates that you’ll find useful. For example, if you’re going to send a weekly promotion to prevent users from churning, set the update frequency to Weekly on the day and time of your choosing.

![Churn 2][2]

## Step 5: Build Prediction
Verify that the details you’ve provided are correct, and choose “Build Prediction.” You can also save your changes in draft form by selecting “Save As Draft” to return to this page and build the model later. Once you click Build Prediction, the process that generates the model will begin. This could take between 30 minutes to a few hours, depending on data volumes. For this Prediction, you will see a page explaining that training is in progress for the duration of the model building process.

Once it’s done, the page will switch to the Analytics view automatically, and you will also get an e-mail informing you that the Prediction and results are ready. In the event of an error, the page will return to the Editing mode with an explanation of what went wrong.

The Prediction will be rebuilt ("retrained") again every two weeks automatically to keep it updated on the most recent data available. Note that this is a separate process from when users' Churn Risk Scores, the output of the Prediction, are produced. The latter is determined by the update frequency you chose in Step 4.

[1]: {% image_buster /assets/img/churn/churn1.png %}
[2]: {% image_buster /assets/img/churn/churn2.png %}
[3]: {% image_buster /assets/img/churn/churn_overview.png %}

