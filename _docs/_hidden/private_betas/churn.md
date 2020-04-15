---
nav_title: Predictive Churn
title: Predictive Churn
description: "This tutorial page covers the benefits of Predictive Churn, why you should be using it, and how to get it set up."
permalink: "/predictive_churn/"
hidden: true
---
{% alert note %}
This feature is currently in Beta. Please reach out to your Braze account manager for more information.
{% endalert %}

# Predictive Churn
> Customer Churn, also known as customer turnover or client loss, is one of the most important metrics for growing businesses to consider. Having the right tools to address churn is crucial in minimizing loss and maximizing customer retention. To get a jump on these potentially churning users, Braze offers Churn Prediction, providing a proactive approach toward minimizing future churn.

Churn Prediction allows you to create custom machine-learning models of user churn, and use them to predict and respond to predicted future churn before it happens. You can also tailor these models to specific audiences within your user base. Predictive Churn will generate new predictions on a regular schedule as well as keep its understanding of actual user churn updated automatically.

## Step 1: Create a New Prediction
On the left navigation bar of the Braze dashboard, choose the Predictions page.  A Prediction is one instance of a trained machine learning model and all the parameters and data it uses. On this page, you will see a list of current active Predictions along with some basic info about them. Here you can rename, archive, and create new Predictions. Archived predictions are inactive and do not update user scores. 

To create a new Prediction, choose “Create Prediction” in the upper right corner, and select a new “Churn Prediction.”

{% alert note %}
During the beta of Predictive Churn, there is a limit of 3 concurrently active Predictions.
{% endalert %}

On the Edit page, give your new Prediction a unique name.

## Step 2: Define Churn
In the Churn Definition panel, use the provided filters to define what churn means for your business. In other words, what does a user have to do in what time frame for you to consider them churned? Remember, you don’t need to explain what behaviors might precede churn-- only what makes a user a churned user. This should also generally be a description of what behavior a user does or doesn't do to churn as opposed to an attribute a user has. 	For example, you might consider users who haven’t opened your app in 7 days to be churned. 

To implement this example, enter 7 days in the time window at the top of the panel.

![Churn 1][1]

Then, use the available filters to select which behaviors in that time frame constitute churn. For this case, select “Last Used App.” The time window automatically matches the one selected above. Any other filters you select will do the same. Note that not all filters available in Braze segments will be available here.

Interested in some potential churn definitions to consider? You’ll find some inspiration at the [bottom of this page](#sample-definitions).

## Step 3: Choose the Users you Want to Keep from Churning
Although you can try to prevent churn as defined above in your entire population of users, the model will likely perform better if we narrow down the group of users we want to prevent from churning with some criteria. Think about the specific users who mean the most to you that you’d like to retain and define them here. For example, we might want to retain users who first used the app more than a month ago or have ever made a purchase.

{% alert note %}
During the beta of Predictive Churn, the Retainable Users audience cannot exceed 5 million users.
{% endalert %}

For filters that begin with “Last...” like Last Used App and Last Made Purchase, the time window to look back for these filters cannot exceed 30 days - the # of days of the window specified in the Churn Definition. For example, if your Churn definition has a window of 14 days, the time window for the “Last...” filters cannot exceed 30 - 14 = 16 days.

For a sample list of Retainable User definitions, check out the [bottom of the page](#sample-definitions)! 

## Step 4: Choose the Update Frequency for Churn Predictions

Next, the machine learning model will be created when you complete this page, it will be used on a regular schedule to generate fresh predictions of users’ probability to churn according to the schedule you choose here. Please select the maximum frequency of updates that you’ll find useful. For example, if you’re going to send a weekly promotion to prevent users from churning, set the update frequency to Weekly on the day and time of your choosing.

![Churn 2][2]

## Step 5: Build Prediction
Verify that the details you’ve provided are correct, and choose “Build Prediction.” You can also save your changes in draft form by selecting “Save As Draft” to return to this page and build the model later. Once you click Build Prediction, the process that generates the model will begin. This could take between 30 minutes to a few hours, depending on data volumes. For this Prediction, you will see a page explaining that training is in progress for the duration of the model building process.

Once it’s done, the page will switch to the Analytics view automatically. In the event of an error, the page will return to the Editing mode with an explanation of what went wrong.

The model will automatically be rebuilt (i.e. retrained) on fresh data every two weeks to keep it current.

# Understanding Results

## Lift Quality
In order to measure the accuracy of your model, the Lift Quality metric will show you how effective this particular machine learning model appears to be when tested on historical data. Braze pulls data according to the groups you specified in the model creation page. The model is trained on one data set (the “training” set) and then tested on a new, separate data set (the “test” set). Lift Quality measures how much better than random guessing the model is on the test set. With this measure, 0% means the model is no better than randomly guessing about who will churn, and 100% indicates perfect knowledge of future knowledge of who will churn.

The Prediction will be trained again every two weeks to keep it updated on the most recent user behavior patterns. This is also when the Lift Quality metric will be updated. The last time the model was created is displayed at thet of the Prediction's analytics page.

{% alert note %}
If 20% of your users usually churn on average, and you pick a random subset of 20% of your users and label them as churned (whether they truly are or not), you’d expect to correctly identify only 20% of the actual churners. If the model were to only do that well, the lift would be 0%. If the model, on the other hand, allowed you to identify 20% of the users as churned and correctly identify all the “true” churners, it would be perfect. That would correspond to a lift quality of 100%. In reality, models are usually somewhere in between. For more detail, see [here](https://humboldt-wi.github.io/blog/research/theses/uplift_modeling_blogpost/).
{% endalert %}

Here’s what we recommend for various different ranges of Lift Quality:

| Lift Quality Range (%) | Recommendation |
| ---------------------- | -------------- |
| 80 - 100 | It's unlikely your model could get any better than this, so go forth and reduce churn! |
| 70 - 80 | There's some chance different settings might improve the model, but you can certainly get good predictions out of it as is. |
| 50 - 70 | This model will produce useful predictions, but trying different audience settings could achieve something more effective. |
| 30 - 50 | This model can produce some value but consider trying different audience definitions to see if they increase performance. |
| 0 - 30 | We recommend you change your audience definitions and try again. |
{: .reset-td-br-1 .reset-td-br-2}

## Churn Score and Category

Users in the Retainable Users audience will be assigned a Churn Score between 0 and 100. The higher the score, the greater the likelihood of Churn. Users with Churn Scores between 0 and 50 will be placed in the Low Churn Risk category. Users with scores between 50 and 75, and 75 and 100 will be placed in the Medium and High Churn Risk categories, respectively. The scores and the corresponding categories will be updated according to the schedule you chose in the model creation page. The number of users with Churn Scores in each of 20 equally sized buckets is displayed in the chart at the top of the page. This can help you determine what the churn risk looks like across the population according to this Prediction.

Below the chart of Churn Scores, three sentences will help you decide who to target in your Retainable Users population, and what the risks are. Based on the data used during creation of the Prediction, the sentences with editable fields will help you determine what accuracy (true positive rate) and number of false positives or false alarms to expect based on the number of users you target for messaging.

The first sentence allows you to set the number of users out of the Retainable Users audience that you could potentially target with a message. (100% would mean sending a message to everyone in the Retainable Users group. Of course, this is not the goal.) Once you set this percentage, the other editable field will change to what percentage of actual churners this is likely to successfully identify based on previously estimated accuracy. Notice both fields are editable and change when the other is changed. The second sentence will identify what threshold for the churn score corresponds to the audience percentage and accuracy currently populated in the editable fields, i.e. the churn score cutoff above which to send users a message.

 The third sentence will also identify how many users are likely to be misidentified as churners (again based on previous estimates.) Because no predictions are perfect, this allows you to gauge the trade off between correctly targeting more actual churners and falsely identifying users who seem like they may churn but ultimately would not have in truth. The better the model, the fewer users you'll need to message to capture more of the true churners.

### Target Users

Once you've decided what threshold to use for your Churn Score, you can use filters in campaigns or segments to target the users according to that threshold. You can filter for users by Churn Score or Churn Category in Campaigns, Canvas, and Segments, just like you use any other filter in Braze.

As a shortcut, you can use the "Create Segment" or "Create Campaign" buttons below the targeting sentences to create a new segment or campaign that filters for users with a Churn Risk Score above the value currently displayed in the sentence.

### Archived Predictions

Archived Predictions will cease updating user scores. Any archived Prediction that is unarchived will continue updating user scores on its predetermined schedule. Archived Predictions are never deleted and remain in the list.

### What To Do Next? {what-do-next}

Now that you’ve identified and selected the group of users at risk of churn that you feel require some incentives or a new messaging series to keep ‘em active and engaged, what do you do? Do you just add them proactively to your current passive user series? Or do you build out a brand new series of Canvases and Campaigns? Here’s a few ideas to consider:

- Target your predicted medium-to-high-risk users with a special discount, free merchandise (physical gift or digital credits), exclusive content, or early access to a new experience (product, app feature, level).
- You could drop these users into a daily Canvas for a week, delivering messages on the channel they prefer most, do a concentrated blast for three days, reaching customers on every channel, from email to Facebook, or Send a message from a real person, asking for brand feedback or offering a pro tip.
- Maybe you just need a new, fun way to reiterate the value of your brand, and all the ways these customers have found value in yours before. This could look like a persona-specific weekly newsletter, a series of real stories from real users about your brand, or some other content marketing play.

Keep in mind that you can message different levels of at-risk users differently! So the highest-risk customers could get higher discounts than the medium-risk customers, while the lowest-risk customers simply get new kinds of messaging or content but no larger incentive. You can also layer other filters into these segments, to further qualify who gets what offers, messages, etc.

### Sample Churn and Retainable Users definitions {#sample-definitions}

- “Cancelled Subscription within the past 7 days.” This might look something like “last did custom event ‘Subscription Cancellation’ less than one weeks ago.”
- “Free Trial Expired within the past 14 days.” This might look something like “last did custom event ‘Trial Expired’ less than two weeks ago.”
- “Uninstalled the app in the last 24 hours.” This might look something like “Uninstalled less than 1 days ago.” 
- “Purchased more than 14 days ago.” This might look something like “Last made purchase more than 2 weeks ago.”

For the Churn definitions we outlined above, here might be some corresponding “Retainable Users” definitions:
- Started subscription more than 2 weeks ago OR Started subscription less than two weeks ago. You might want to create 2 predictions in this case, and then message new subscribers differently than longer-term subscribers. You could also define this as “First Made Purchase more than 30 days ago.”
- For uninstallers, you might focus on customers who have purchased something in the recent past or used the app very recently.
- For those at risk of not purchasing as a definition of churn, you may want to focus on customers who have been browsing or searching or engaging with your app more recently. Perhaps the right discount intervention wi


[1]: {% image_buster /assets/img/churn/churn1.png %}
[2]: {% image_buster /assets/img/churn/churn2.png %}
