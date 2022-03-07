---
nav_title: Creating a Churn Prediction
article_title: Creating a Churn Prediction
description: "This article covers how to create a Churn Prediction within the Braze dashboard"
page_order: 1

---

# Creating a Churn Prediction

## Step 1: Create a new prediction

On the left navigation bar of the Braze dashboard, choose the __Predictions__ page. A Prediction is one instance of a trained machine learning model and all the parameters and data it uses. On this page, you will see a list of current active Predictions along with some basic info about them. Here you can rename, archive, and create new Predictions. Archived predictions are inactive and do not update user scores. 

To create a new Prediction, choose __Create Prediction__ in the upper right corner, and select a new __Churn Prediction__.

{% alert note %}
There is a limit of 3 concurrently active Churn Predictions. Prior to purchasing Predictive Churn, the limit is one active Preview Churn Prediction. A Preview Churn Prediction will not regularly update scores or allow you to target users based on the Prediction's output. Contact your Account Manager for details.
{% endalert %}

On the **Basics** page, give your new Prediction a unique name. You can also provide an optional description to take any notes on this particular Prediction.

Click __Forward__ to move to the next step. Optionally, you can click __Build Now__ to use all the default settings and skip to the last step of creation. You will have a chance to review the settings before starting the build process. You can return to any step later by selecting it in the progress tracker on the top.

## Step 2: Define churn

In the __Churn Definition__ panel, use the provided filters to specify how you define user churn for your business. In other words, what does a user have to do in what time frame for you to consider them churned?

Remember, you don’t need to explain what behaviors might precede churn—only what makes a user a churned user. Think of this in terms of something a user either does once (`do`) or stops doing (`do not`) that constitutes churning. For example, you might consider users who haven’t opened your app in 7 days to be churned. You might consider uninstalling, or custom events like unsubscribing, disabling an account, or others to cause a user to become churned. 

#### Churn Window
Churn Window is the time frame in which a user performs the behavior specified to constitute churning. It can be set up to 14 days. This window is used to query historical data for training the Prediction. Additionally, once the Prediction is created and users receive scores, the Churn Likelihood Score indicates how likely a user is to churn within the number of days specified by the Churn Window. 

Here's an example of a simple definition based on lapsing sessions in the last 7 days.

![Churn Definition][1]

For this case, we select `do not` and `start a session`. You can combine other filters with `AND` and `OR` as you see fit to create the definition you need. Interested in some potential churn definitions to consider? You can find some inspiration in the section on [Sample churn definitions](#sample-definitions) below.

{% alert note %}
For `do`, we assume that active users did not take the action you specify for this row prior to becoming churned. Doing the action causes them to become churned. <br><br>For `do not`, we consider active users to be those that did do that action in the days prior, and then stopped.
{% endalert %}

Underneath the definition, you will see estimates of how many users (in the past who churned and who didn't churn according to your definition) are available. You will also see the minimum values required. Braze must have this minimum count of users available in historical data so that the Prediction has enough data to learn from.

## Step 3: Filter your prediction audience

Your Prediction Audience is the group of users you want to predict churn risk for. By default, this will be set to __All Users__, which means that this Prediction will create Churn Risk Scores for all of your active users. Usually, the model will likely perform better if you narrow down and filter the group of users you want to prevent from churning with some criteria. Think about the specific users who mean the most to you that you’d like to retain and define them here. For example, you might want to retain users who first used the app more than a month ago or have ever made a purchase.

{% alert note %}
The Prediction Audience cannot exceed 100 million users.
{% endalert %}

For filters that begin with “Last...” like Last Used App and Last Made Purchase, the time window to look back for these filters __cannot exceed the Churn Window specified__ in the Churn Definition. For example, if your Churn definition has a window of 14 days, the time window for the “Last...” filters cannot exceed 14 days.

#### Full Filter Mode
In order to build a new Prediction immediately, only a subset of Braze segmentation filters is supported. Full Filter Mode allows you to use all Braze filters but will require one Churn Window to build the Prediction. For example, if the Churn Window is set to 15 days, it will take 15 days to collect the user data and build the Prediction when using filters only supported in Full Filter Mode. Additionally, some estimates about audience sizes will not be available in Full Filter Mode.

For a sample list of Prediction Audience definitions, check out our sample definitions in the section on [Sample churn definitions](#sample-definitions) below.

![Prediction Audience][3]

Just like the previous page, the bottom panel will show you the estimated number of historic users that result from your Churn definition and Prediction Audience definition. These estimates must meet the minimum requirements shown in order to create a Prediction.

## Step 4: Choose the update frequency for Churn Predictions

The machine learning model created when you complete this page will be used on a schedule you select here to generate fresh Churn Risk Scores. Please select the __maximum frequency of updates__ that you’ll find useful. For example, if you’re going to send a weekly promotion to prevent users from churning, set the update frequency to __Weekly__ on the day and time of your choosing. 

![Prediction Update Schedule][2]

{% alert note %}
Preview and Demo Predictions will never update users' risk of churn. Additionally, daily updates for predictions require an additional purchase beyond Weekly or Monthly updates with Predictive Churn. To purchase this functionality, contact your Account Manager. 
{% endalert %}

## Step 5: Build prediction

Verify that the details you’ve provided are correct, and choose __Build Prediction__. You can also save your changes in draft form by selecting __Save As Draft__ to return to this page and build the model later. Once you click __Build Prediction__, the process that generates the model will begin. This could take between 30 minutes to a few hours depending on data volumes. For this Prediction, you will see a page explaining that training is in progress for the duration of the model building process.

Once it’s done, the page will switch to the Analytics view automatically, and you will also get an email informing you that the Prediction and results are ready. In the event of an error, the page will return to the Editing mode with an explanation of what went wrong.

The Prediction will be rebuilt ("retrained") again every __two weeks automatically__ to keep it updated on the most recent data available. Note that this is a separate process from when users' Churn Risk Scores, the output of the Prediction, are produced. The latter is determined by the update frequency you chose in Step 4.

## Sample churn and prediction audience definitions {#sample-definitions}

__Sample Churn Definitions__<br>
- “Within 7 days, do custom event ‘Subscription Cancellation’”<br>
- “Within 14 days, do custom event ‘Trial Expired’”<br>
- “Within 1 day do uninstall.” <br>
- “Within 14 days do not Make a Purchase.” <br>

For the Churn definitions we outlined above, there might be some corresponding Prediction Audience definitions:<br>
- __Started subscription more than 2 weeks ago OR Started subscription less than two weeks ago__<br>You might want to create 2 predictions in this case and then message new subscribers differently than longer-term subscribers. You could also define this as “First Made Purchase more than 30 days ago.”<br>
- __Uninstallers__<br>You might focus on customers who have purchased something in the recent past or used the app very recently.<br>
- __Those at Risk of Not Purchasing as a Definition of Churn__<br>You may want to focus on customers who have been browsing or searching or engaging with your app more recently. Perhaps the right discount intervention will prevent this more engaged group from churning.

## Archived predictions

Archived Predictions will cease updating user scores. Any archived Prediction that is unarchived will continue updating user scores on its predetermined schedule. Archived Predictions are never deleted and remain in the list.

[1]: {% image_buster /assets/img/churn/churn1.png %}
[2]: {% image_buster /assets/img/churn/churn2.png %}
[3]: {% image_buster /assets/img/churn/churn5.png %}

