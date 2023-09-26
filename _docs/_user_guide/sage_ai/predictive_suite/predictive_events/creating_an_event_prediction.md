---
nav_title: Creating an Event Prediction
article_title: Creating an Event Prediction
page_order: 1
description: "This article covers how to create an Event Prediction within the Braze dashboard."

---

# Creating an Event Prediction

> A Prediction is one instance of a trained machine learning model and all the parameters and data it uses. To learn more about Predictive Events, refer to the [Predictive Events overview]({{site.baseurl}}/user_guide/sage_ai/predictive_suite/predictive_events).

In Braze, go to **Analytics** > **Predictive Events**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Predictions** under **Engagement**.
{% endalert %}

On this page, you will see a list of current active Event Predictions and some basic information about them. Here, you can rename, archive, and create new Predictions. Archived Predictions are inactive and do not update user scores.

## Step 1: Create a new Prediction

1. Choose **Create Prediction** and select a new **Event Prediction**.

{% alert note %}
There is a limit of five concurrently active Predictions. Before purchasing Predictive Events, the limit is one active preview Prediction. A preview Prediction will not regularly update scores or target users based on the Prediction's output. Contact your account manager for details.
{% endalert %}

{: start="2"}
2. Give your Prediction a unique name. You can also provide a description to save any relevant notes.

![][1]

{: start="3"}
3. Click **Forward** to move to the next step. <br><br>Optionally, you can click **Build Now** to use all the default settings and skip to the last step of creation. You will have a chance to review the settings before starting the build process. Also, you can return to any step later by clicking it in the top bar.

## Step 2: Specify event tracking {#event-tracking}

Specify if your users' events are stored in Braze as [purchase events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) or [custom events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/).

Here, you'll see if the selected method provides enough data for Braze to create a machine learning model. If the requirement is not met, try and select the other logging method if it is also used by your application. Unfortunately, if it is not, Braze is unable to create a Prediction with the quantity of data available. If you believe you're incorrectly seeing this error, get in touch with your customer success manager.

#### Event Window

The Event Window is the time frame in which you want to predict if a user will perform the event. It can be set up to 60 days. This window is used to query historical data for training the Prediction. Additionally, after the Prediction is created and users receive scores, the Likelihood Score indicates how likely a user is to perform the event within the number of days specified by the Event Window.

### Step 3: Filter your Prediction Audience (optional) {#audience}

Your Prediction Audience is the group of users whose Likelihood Score you would like to predict. If desired, you can run a Prediction on your entire population of users. To do this, leave the default option **All Users** selected.

The model typically performs better if you filter the users you want to assess with some criteria. To do so, select **Define my own prediction audience** and choose your audience filters. For example, you might want to focus on users who have been using your app for at least 30 days by selecting the "First Used App" filter set to 30 days.

The Prediction Audience definition is also used to query historical data to allow the machine learning model to learn from the past. Similar to the previous page, the quantity of data provided by these filters is displayed along with the requirement. If you specify your desired audience and do not meet the minimum, try specifying a broader filter or use the **All Users** option.

{% alert note %}
The Prediction Audience cannot exceed 100 million users.
{% endalert %}

When the Event Window is 14 days or less, the time window for filters that begin with "Last..." like "Last Used App" and "Last Made Purchase" **cannot exceed the Event Window specified in [event tracking](#event-tracking)**. For example, if the Event Window is set to 14 days, the time window for the "Last..." filters cannot exceed 14 days.

#### Full Filter Mode

In order to build a new Prediction immediately, only a subset of Braze segmentation filters are supported. Full Filter Mode allows you to use all Braze filters but will require one Event Window to build the Prediction. 

For example, if the Event Window is set to 14 days, it will take 14 days to collect the user data and build the Prediction when using filters only supported in Full Filter Mode. Additionally, some estimates about audience sizes will not be available in Full Filter Mode.

### Step 4: Choose the update schedule

The machine learning model created when you complete this page will be used on a schedule you select here, to generate fresh scores of users' probability to perform the event (Likelihood Score). Select the **maximum frequency of updates** that you'll find useful. For example, if you're predicting purchases and are planning to send a weekly promotion, set the update frequency to **Weekly** on the day and time of your choosing.

{% alert note %}
Preview and Demo Predictions will never update users' Likelihood Scores.
{% endalert %}

### Step 5: Build Prediction

Verify that the details you've provided are correct, and choose **Build Prediction**. You can also save your changes in draft form by selecting **Save As Draft** to return to this page and build the model later. 

After you click **Build Prediction**, the process that generates the model will begin. This could take between 30 minutes to a few hours, depending on data volumes. For this Prediction, you will see a page explaining that training is in progress for the duration of the model building process.

When completed, the page will switch to the analytics view automatically, and you will receive an email informing you that the Prediction and results are ready. In the event of an error, the page will return to the editing mode with an explanation of what went wrong.

The Prediction will be automatically rebuilt ("retrained") every **two weeks** to keep it updated on the most recent data available. Note that this is a separate process from when users' Likelihood Scores, the output of the Prediction, are produced. The latter is determined by the update frequency you chose in Step 4.

## Archived Predictions

Archived Predictions will stop updating user scores. Any archived Prediction that is unarchived will continue updating user scores on its predetermined schedule. Archived Predictions are never deleted and remain in the list.

[1]: {% image_buster /assets/img/purchasePrediction/purchases_step1.png %}

