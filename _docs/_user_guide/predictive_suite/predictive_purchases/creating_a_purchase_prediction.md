---
nav_title: Creating A Purchase Prediction
article_title: Creating A Purchase Prediction
page_order: 1
description: "This article covers how to create a Purchase Prediction within the Braze dashboard."

---

# Creating a Purchase Prediction

On the left navigation bar of the Braze dashboard, choose the **Predictions** page. A Prediction is one instance of a trained machine learning model and all the parameters and data it uses. On this page, you will see a list of current active Predictions and some basic info about them. Here you can rename, archive, and create new Predictions. Archived Predictions are inactive and do not update user scores. 

To create a new Prediction, choose **Create Prediction** in the upper right corner and select a new **Purchase Prediction**.

{% alert note %}
There is a limit of three concurrently active Purchase Predictions. Before purchasing Predictive Purchases, the limit is one active Preview Purchase Prediction. A Preview Purchase Prediction will not regularly update scores or target users based on the Prediction's output. Contact your account manager for details.
{% endalert %}

## Step 1: Create a new Prediction

![][1]

On the first page, give your new Prediction a unique name. You can also provide a description to save any relevant notes.

Click **Forward** to move to the next step. Optionally, you can click **Build Now** to use all the default settings and skip to the last step of creation. You will have a chance to review the settings before starting the Build process. Also, you can return to any step later by clicking it in the top bar. 

## Step 2: Specify purchase tracking

On this page, specify if your users' purchases are stored in Braze as standard [purchase events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) or [custom events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/).

Here, you'll see if the selected Purchase method provides enough data for Braze to create a machine learning model. If the requirement is not met, try and select the other logging method if it is also used by your application. Unfortunately, if it is not, Braze is unable to create a Prediction with the quantity of data available. If you believe you're incorrectly seeing this error, get in touch with your CSM.

#### Prediction Window

Prediction Window is the time frame in which you want to predict if a user will make a purchase. It can be set up to 14 days. This window is used to query historical data for training the Prediction. Additionally, once the Prediction is created and users receive scores, the Purchase Likelihood Score indicates how likely a user is to Purchase within the number of days specified by the Prediction Window.

### Step 3: Filter your Prediction Audience (optional) {#audience}

Your Prediction Audience is the group of users whose Purchase likelihood you would like to predict. Purchase Prediction allows you to run a Prediction on your entire population of users. To do this, leave the default option **All Users** selected.

The model will likely perform better if you filter the users you want to assess with some criteria. To do so, select **Define my own prediction audience** and choose your audience filters. For example, you might want to focus on users who have been using your app for at least 30 days by selecting the "First Used App" filter set to 30 days. 

The Prediction Audience definition is also used to query historical data to allow the machine learning model to learn from the past. Similiar to the previous page, the quantity of data provided by these filters is displayed along with the requirement. If you specify your desired audience and do not meet the minimum, try specifying a broader filter or use the **All Users** option.

{% alert note %}
The Prediction Audience cannot exceed 100 million users.
{% endalert %}

For filters that begin with "Last..." like "Last Used App" and "Last Made Purchase", the time window to look back for these filters **cannot exceed the Prediction Window specified in Purchase Event Tracking**. For example, if the Prediction Window is set to 14 days, the time window for the “Last...” filters cannot exceed 14 days.

#### Full Filter Mode

In order to build a new Prediction immediately, only a subset of Braze segmentation filters are supported. Full Filter Mode allows you to use all Braze filters but will require one Prediction Window to build the Prediction. For example, if the Prediction Window is set to 15 days, it will take 15 days to collect the user data and build the Prediction when using filters only supported in Full Filter Mode. Additionally, some estimates about audience sizes will not be available in Full Filter Mode.

### Step 4: Choose the update frequency

The machine learning model created when you complete this page will be used on a schedule you select here, to generate fresh scores of users’ probability to Purchase. Select the **maximum frequency of updates** that you’ll find useful. For example, if you’re going to send a weekly promotion to prevent users from Purchasing, set the update frequency to **Weekly** on the day and time of your choosing. 

{% alert note %}
Preview and Demo Predictions will never update users' likelihood to Purchase. 
{% endalert %}

### Step 5: Build Prediction

Verify that the details you've provided are correct, and choose **Build Prediction**. You can also save your changes in draft form by selecting **Save As Draft** to return to this page and build the model later. Once you click **Build Prediction**, the process that generates the model will begin. This could take between 30 minutes to a few hours, depending on data volumes. For this Prediction, you will see a page explaining that training is in progress for the duration of the model building process.

Once completed, the page will switch to the analytics view automatically, and you will also get an email informing you that the Prediction and results are ready. In the event of an error, the page will return to the editing mode with an explanation of what went wrong.

The Prediction will be rebuilt ("retrained") again every **two weeks automatically** to keep it updated on the most recent data available. Note that this is a separate process from when users' Purchase Likelihood Scores, the output of the Prediction, are produced. The latter is determined by the update frequency you chose in Step 4.

## Archived Predictions

Archived Predictions will cease updating user scores. Any archived Prediction that is unarchived will continue updating user scores on its predetermined schedule. Archived Predictions are never deleted and remain in the list.

[1]: {% image_buster /assets/img/purchasePrediction/purchases_step1.png %}

