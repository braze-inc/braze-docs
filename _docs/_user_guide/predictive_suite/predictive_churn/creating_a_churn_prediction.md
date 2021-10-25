---
nav_title: Creating A Churn Prediction
article_title: Creating A Churn Prediction
description: "This article covers how to create a Churn Prediction within the Braze dashboard"
page_order: 1

---

# Creating a Churn Prediction

### Step 1: Create a new prediction

On the left navigation bar of the Braze dashboard, choose the __Predictions__ page. A Prediction is one instance of a trained machine learning model and all the parameters and data it uses. On this page, you will see a list of current active Predictions along with some basic info about them. Here you can rename, archive, and create new Predictions. Archived predictions are inactive and do not update user scores. 

To create a new Prediction, choose __Create Prediction__ in the upper right corner, and select a new __Churn Prediction__.

{% alert note %}
There is a limit of 3 concurrently active Churn Predictions. Prior to purchasing Predictive Churn, the limit is one active Preview Churn Prediction. A Preview Churn Prediction will not regularly update scores or allow you to target users based on the Prediction's output. Contact your Account Manager for details.
{% endalert %}

On the Edit page, give your new Prediction a unique name.

### Step 2: Define churn

In the __Churn Definition__ panel, use the provided filters to define what churn means for your business. In other words, what does a user have to do in what time frame for you to consider them churned? Remember, you don’t need to explain what behaviors might precede churn - only what makes a user a churned user. This should also generally be a description of what behavior a user does or doesn't do to churn as opposed to an attribute a user has. For example, you might consider users who haven’t opened your app in 7 days to be churned. 

To implement this example, enter 7 days in the time window at the top of the panel.

![Churn 1][1]

Then, use the available filters to select which behaviors in that time frame constitute churn. For this case, select "do not" and "start a session". You can combine other filters with "and" and "or" as you see fit to create the definition you need. Uninstalling, making or not making purchases, or performing or not performing particular custom events are other filters that can be included.

Interested in some potential churn definitions to consider? You’ll find some inspiration [here](#sample-definitions).

### Step 3: Filter your prediction audience

Your Prediction Audience is the group of users you want to target to keep from churning. Although you can try to prevent churn as defined above in your entire population of users, the model will likely perform better if you narrow down and filter the group of users you want to prevent from churning with some criteria. Think about the specific users who mean the most to you that you’d like to retain and define them here. For example, you might want to retain users who first used the app more than a month ago or have ever made a purchase. 

{% alert note %}
The Prediction Audience cannot exceed 40 million users.
{% endalert %}

For filters that begin with “Last...” like Last Used App and Last Made Purchase, the time window to look back for these filters __cannot exceed 30 days minus the number of days of the window specified__ in the Churn Definition. For example, if your Churn definition has a window of 14 days, the time window for the “Last...” filters cannot exceed 30 - 14 = 16 days.

For a sample list of Prediction Audience definitions, check out our sample definitions at the [bottom of this page](#sample-definitions).

### Step 4: Choose the update frequency for Churn Predictions

The machine learning model created when you complete this page will be used on a schedule you select here to generate fresh scores of users’ probability to churn. Please select the __maximum frequency of updates__ that you’ll find useful. For example, if you’re going to send a weekly promotion to prevent users from churning, set the update frequency to __Weekly__ on the day and time of your choosing. 

![Churn 2][2]

{% alert note %}
Preview and Demo Predictions will never update users' risk of churn. Additionally, daily updates for predictions require an additional purchase beyond Weekly or Monthly updates with Predictive Churn. To purchase this functionality, contact your Account Manager. 
{% endalert %}

### Step 5: Build prediction

Verify that the details you’ve provided are correct, and choose __Build Prediction__. You can also save your changes in draft form by selecting __Save As Draft__ to return to this page and build the model later. Once you click __Build Prediction__, the process that generates the model will begin. This could take between 30 minutes to a few hours depending on data volumes. For this Prediction, you will see a page explaining that training is in progress for the duration of the model building process.

Once it’s done, the page will switch to the Analytics view automatically, and you will also get an email informing you that the Prediction and results are ready. In the event of an error, the page will return to the Editing mode with an explanation of what went wrong.

The Prediction will be rebuilt ("retrained") again every __two weeks automatically__ to keep it updated on the most recent data available. Note that this is a separate process from when users' Churn Risk Scores, the output of the Prediction, are produced. The latter is determined by the update frequency you chose in Step 4.

## Sample churn and prediction audience definitions {#sample-definitions}

__Sample Churn Definitions__<br>
- “Within 7 days, did custom event ‘Subscription Cancellation’”<br>
- “Within 14 days, did custom event ‘Trial Expired’”<br>
- “Within 1 day did uninstall.” <br>
- “Within 14 days did not Make a Purchase.” <br>

For the Churn definitions we outlined above, there might be some corresponding Prediction Audience definitions:<br>
- __Started subscription more than 2 weeks ago OR Started subscription less than two weeks ago__<br>You might want to create 2 predictions in this case and then message new subscribers differently than longer-term subscribers. You could also define this as “First Made Purchase more than 30 days ago.”<br>
- __Uninstallers__<br>You might focus on customers who have purchased something in the recent past or used the app very recently.<br>
- __Those at Risk of Not Purchasing as a Definition of Churn__<br>You may want to focus on customers who have been browsing or searching or engaging with your app more recently. Perhaps the right discount intervention will prevent this more engaged group from churning.

## Archived predictions

Archived Predictions will cease updating user scores. Any archived Prediction that is unarchived will continue updating user scores on its predetermined schedule. Archived Predictions are never deleted and remain in the list.

[1]: {% image_buster /assets/img/churn/churn1.png %}
[2]: {% image_buster /assets/img/churn/churn2.png %}

