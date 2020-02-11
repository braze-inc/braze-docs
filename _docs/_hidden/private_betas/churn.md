---
nav_title: Predictive Churn
title: Predictive Churn
description: "This tutorial page covers the benefits of Predictive Churn, why you should be using it, and how to get it set up."
permalink: "/predictive_churn/"
hidden: true
---
{% alert note %}
This Predictive Churn feature is currently in Beta. Please reach out to your Braze account manager for more information.
{% endalert %}

# Predictive Churn
> Customer Churn, also known as customer turnover or client loss, is one of the most important metrics for growing businesses to consider. Having the right tools to address churn is crucial in minimizing loss and maximizing customer retention. To get a jump on these potentially churning users, Braze offers Churn Prediction, providing an understanding and level of anticipation over future churn.

Churn Prediction allows you to create custom machine-learning models of user churn, and use them to predict and respond to predicted future churn before it happens. You can also tailor these models to specific audiences within your user base. Predictive Churn will generate new predictions on a regular schedule as well as keep its understanding of actual user churn updated automatically.

## Step 1: Create a New Prediction
On the left navigation bar of the Braze dashboard, choose the Predictions page.  A Prediction is one instance of a trained machine learning model and all the parameters and data it uses. On this page, you will see a list of current active Predictions along with some basic info about them.

Choose “Create Prediction” in the upper right corner, and select a new “Churn Prediction.”

On the Edit page, give your new Prediction a unique name.

## Step 2: Define Churn
In the Churn Definition panel, use the provided filters to define what churn means for your business. In other words, what does a user have to do in what time frame for you to consider them churned? Remember, you don’t need to explain what behaviors might precede churn-- only what makes a user a churned user. For example, you might consider users who haven’t opened your app in 7 days to be churned. 

To implement this example, enter 7 days in the time window at the top of the panel.

![Churn 1][1]

Then, use the available filters to select which behaviors in that time frame constitute churn. For this case, select “Last Used App.” The time window automatically matches the one selected above. Any other filters you select will do the same. Note that not all filters available in Braze segments will be available here.

## Step 3: Choose the Users you Want to Keep from Churning
Although you can try to prevent churn as defined above in your entire population of users, the model will likely perform better if we narrow down the group of users we want to prevent from churning with some criteria. Think about the specific users who mean the most to you that you’d like to retain and define them here. For example, we might want to retain users who first used the app within the last 6 months or have ever made a purchase.

Note that for the beta period of Predictive Churn, the model will only score up to the first 5 million users that fit the above criteria.

## Step 4: Choose the Update Frequency for Churn Predictions

Next, the machine learning model will be created when you complete this page, it will be used on a regular schedule to generate fresh predictions of users’ probability to churn according to the schedule you choose here. Please select the maximum frequency of updates that you’ll find useful. For example, if you’re going to send a weekly promotion to prevent users from churning, set the update frequency to Weekly on the day and time of your choosing.

![Churn 2][2]

## Step 5: Build Prediction
Verify that the details you’ve provided are correct, and choose “Build Prediction.” You can also save your changes in draft form by selecting “Save As Draft” to return to this page and build the model later. Once you click Build Prediction, the process that generates the model will begin. This could take between 30 minutes to a few hours, depending on data volumes. For this Prediction, you will see a page explaining that training is in progress for the duration of the model building process.

Once it’s done, the page will switch to the Analytics view automatically. In the event of an error, the page will return to the Editing mode with an explanation of what went wrong.

__The model will automatically be rebuilt (i.e. retrained) on fresh data every two weeks to keep it current.__

# Understanding Results

## Lift Quality
In order to measure the accuracy of your model, the Lift Quality metric will show you how effective this particular machine learning model appears to be when tested on historical data. Braze pulls data according to the groups you specified in the model creation page. The model is trained on one data set (the “training” set) and then tested on a new, separate data set (the “test” set). Lift Quality measures how much better than random guessing* the model is on the test set. With this measure, 0% means the model is no better than randomly guessing about who will churn, and 100% indicates perfect knowledge of future knowledge of who will churn.

{% alert note %}
&#42; In this case, random guessing means randomly guessing at the measured baseline churn rate. For example, if 20% of your users usually churn on average, and you pick a random subset of 20% of your users and label them as churned (whether they truly are or not), you’d expect to correctly identify only 20% of the actual churners. If the model were to only do that well, the lift would be 0%. If the model, on the other hand, allowed you to identify 20% of the users as churned and correctly identify all the “true” churners, it would be perfect. That would correspond to a lift quality of 100%. In reality of course, models usually fall somewhere inbetween.
{% endalert %}

Here’s what we recommend for various different ranges of Lift Quality:

| Lift Quality Range (%) | Recommendation |
| ---------------------- | -------------- |
| 80 - 100 | It's unlikely your model could get any better than this, so go forth and reduce churn! |
| 70 - 80 | There's some chance different settings might improve the model, but you can certainly get good predictions out of it as is. |
| 50 - 70 | This model will produce useful predictions, but trying different audience settings could achieve something more effective. |
| 30 - 50 | This model can produce some value but consider trying different audience definitions to see if they increase performance. |
| 0 - 30 | We recommend you change your audience definitions and try again. |

## Churn Score and Category
The first 5 million users in the Retainable Users audience will be assigned a Churn Score between 0.0 and 1.0. Users with Churn Scores between 0.0 and 0.5 will also be placed in the Low Churn Risk category. Users with scores between 0.5 and 0.75, and 0.75 and 1.0 will be placed in the Medium and High Churn Risk categories, respectively. This prediction and the corresponding categories will be updated according to the schedule you chose in the model creation page. 

You can filter for users by Churn Score or Churn Category in Campaigns, Canvas, and Segments, just like you use any other filter in Braze.

[1]: {% image_buster /assets/img/churn/churn1.png %}
[2]: {% image_buster /assets/img/churn/churn2.png %}
