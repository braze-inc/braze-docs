---
nav_title: Amazon Personalize
article_title: Amazon Personalize
alias: /partners/amazon_personalize/
description: "This article outlines a reference architecture for and integration between Braze and Amazon Personalize."
page_type: partner
search_tag: Partner
---

# Amazon Personalize

> Amazon Personalize is like having your very own Amazon.com machine learning recommendation system, 24 hours a day. Based on over 20 years of recommendation experience, Amazon Personalize enables you to improve customer engagement by powering real-time personalized product and content recommendations, and targeted marketing promotions.

Using machine learning, Amazon Personalize creates higher-quality recommendations for your websites and applications. You can get started without any prior machine learning experience using simple APIs to easily build sophisticated personalization capabilities in just a few clicks. The service will process and examine your data, identify what is meaningful, allow you to pick a machine learning algorithm. Then it will train and optimize a custom model based on your data and the selected algorithm.

With Amazon Personalize you can create a model that will recommend items based on user's past behavior, sort items in the most relevant order or recommend items that are similar to other items. Using the trained models, you can run Personalize recommendation campaigns and use Personalize API to obtain a list of recommended items and integrate them with Braze through Connected Content. You retain the freedom to control the parameters used to train the models and the optional business objective that optimizes the algorithm's output.

This article will help you understand the use cases Amazon Personalize offers, the data it works with and the process of configuring the service. Then you will learn how to integrate it with Braze and run a campaign using Connected Content.

### Use Cases

The first step to working with Amazon Personalize is determining your use case. You can recommend items for users based on their previous interactions with the items or how popular the items. That will allow you to provide the best personalized recommendations to each user.  
You can provide a list of items or search results, tailored to each individual user to help increase engagement and interaction by making sure the most relevant items for the user appear first.  
Finally, you can find recommendations for similar items such as items frequently bought together or items that other users interacted with to help your users discover new things.

In the guide below, we will focus on the user personalized recommendations recipe.

### Requirements

To get started with Amazon Personalize recommendation models, you need three types of datasets:

- Interactions
  - Stores historical interactions between users and items
  - Requires a `USER_ID`, `ITEM_ID`, `EVENT_TYPE` and `TIMESTAMP` values and optionally accepts metadata about the event
- Users
  - Stores metadata about the users
  - Requires a `USER_ID` value and at least one metadata field (string or numerical) such as gender, age, loyalty membership
- Items
  - Stores metadata about items
  - Requires an `ITEM_ID` and at least one metadata field (textural, categorical or numerical) which describes the item

For the user recommendations recipe you must provide an interactions dataset containing at least 1000 points of interaction data from at least 25 unique users with at least 2 interactions each. The datasets can be uploaded in bulk using CSV files stored in S3 or incrementally through the API.

### Creating Models

#### Training

Once datasets are imported, it is time to create a solution. A solution uses one of Amazon Personalize recipes (algorithms) to train a model. In our case, we will use the `USER_PERSONALIZATION` recipe. Training the solution results in a solution version (a trained model) which you may evaluate based on the performance metrics of the model.

Amazon Personalize lets you adjust hyperparameters that the model uses for training. For example, user history length percentile lets you adjust the percentile of user history to include in the training. Adjusting minimum user history length percentile excludes a percentage of users with very short history lengths which can be useful to eliminate popular items and build recommendations based on deeper underlying patterns. Max user history length percentile setting, on the other hand, lets you adjust the percentage of users to take into account when training with very long history lengths.

The number of hidden dimensions helps detect more complicated patterns for complex datasets, while the back-propagation through time technique (bptt) adjusts rewards for an early event, after a chain of events took place that resulted in a high value action.

Additionally, Amazon Personalize offers automatic hyperparameter tuning by running multiple versions of the solution with different values at the same time. To use the tuning, turn on `Perform HPO` when creating a solution.

#### Evaluating

Once a solution finished training, you are ready to evaluate it and compare different versions. Each solution version displays computed metrics. Some of the available metrics include:

- `Normalize discounted cumulative gain` - compares recommended order of items to the actual list of items and gives each item a weight corresponding to its position in the list
- `Precision @k` - the amount of properly recommended items divided by the amount of all recommended items where `k` is the amount of items
- `Mean reciprocal rank` - focuses on the first, highest ranked recommendation and calculates how many recommended items are seen before the first matched recommendation appears
- `Coverage` - proportion of unique recommended items to the total number on unique items in the dataset

### Getting Recommendations

Once you created a solution version that you're happy with, it is time to put the recommendations to use. There are two ways to access the recommendations:

1. Real-time campaign
2. Batch job

A campaign is a deployed solution version with a defined minimum transaction throughput. A transaction is a single API call to get recommendation output and it is defined as TPS, or transactions per second, with a minimum value of 1. The campaign will scale resources in case of an increased load but it will not ever drop below your minimum value. You can query the recommendations in the console, AWS CLI or through AWS SDKs in your code.

A second option is to create a batch job that exports the recommendations to an S3 bucket. The job takes an input of a JSON file with a list of user IDs for which you want to export the recommendations. Then, after specifying the correct permissions and the output destination, you're ready to run the job. The runtime depends on the size of your datasets and the recommendations list length.

#### Filters

Filters let you adjust the recommendation output by excluding items based on the item's ID, its event type or the metadata. You can also filter users based on their metadata such as age or loyalty membership status. Filters can come in handy to prevent recommending items that the user has already interacted with.

### Integrating results with Braze

With the created model and recommendations campaign, we are ready to run a Braze campaign for our users using Content Cards and Connected Content.
Before we are able to run a Braze campaign, we must create a service that can serve these recommendations through an API. You can follow the instructions in [Step 3.5][1] in the workshop to deploy the service using AWS services. You can also deploy your own independent backend service that provides the recommendations.

Let's run a Content Card campaign with the first recommended item from the list.
In the examples below, we are going to query
`GET http://<service-endpoint.com>/recommendations?user_id=user123` endpoint with a `user_id` parameter which will return a list of recommended items:

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

In the Braze dashboard, create a new Content Card campaign. In the message text field, create a connected content liquid block to query the API and save the response in the `recommendations` variable:

{% raw %}

```
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

You can then reference the first item in the resulting array and display the content to the user:

```
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

Including the title, the image and linking the URL, this is what the complete Content Card would look like:

![Personalize Campaign][2]

[1]: {{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/workshop/#step-3-send-personalized-emails-from-braze
[2]: {% image_buster /assets/img/amazon_personalize/content-card-campaign.png %}
