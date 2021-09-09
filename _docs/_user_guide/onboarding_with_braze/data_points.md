---
nav_title: Data Points
article_title: Data Points Overview
page_order: 4
page_type: reference
description: "This reference article outlines what Data Points are at Braze and how you can be aware of their usage."

---

# Data Points

At Braze, data means action: each piece of data that arrives in Braze updates segment membership, can trigger & cancel messaging, is immediately available for messaging personalization, and more. As such, data points are Braze’s way of defining a billing and pricing structure, based on pieces of information logged against user profiles. See [Consumption Count](#consumption-count) below to see what data counts toward your data point allocation.
 
Our Customer Success team can help recommend data best practices to fit your specific needs. You can find a more detailed breakdown of this definition in your Braze contract.

## Management & Usage

To view your Data Point Dashboard, select your name in the top-right corner, click the drop down, and select __Subscriptions and Usage__. For more information on the Data Point Dashboard components, check out our subscription and usage [article]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/). 

{% alert tip %}
__Only update your deltas (changing data)!__

To prevent using up your allocated data points, we recommend setting up a program that will prevent sending the same, unchanging data from your app to Braze over and over.
{% endalert %}


## Consumption Count

In sum, data points are accumulated when a user's profile data is updated or when they perform specific actions. Essentially, data points are counts of each of your users' `session starts`, `session ends`, `events`, and `purchases`.

You can find a breakdown of how Braze accumulates data points below, but there are nuances beyond what you see here, which may affect the number of remaining points you expect to see. If you ever have any questions about your billing, reach out to your Braze account manager.

{% alert note %} Connected Content does not consume data points—using Connected Content is a great way to reference data from other platforms without needing to bulk upload to Braze and use up your points! {% endalert %}

{% tabs %}
{% tab General %}

### General

|Data Type | Data Point | Does it count towards consumption? |
|---|---|---|
|Profile Data | First Name | Yes |
|Profile Data | Last Name | Yes |
|Profile Data | User ID | No |
|Profile Data | User Alias | No |
|Profile Data | Email Address | Yes |
|Profile Data | Gender | Yes |
|Profile Data | Age Group | Yes |
|Profile Data | Country | Yes |
|Profile Data | City | Yes |
|Profile Data | Language | Yes |
|Profile Data | Most Recent Device Locale | Yes |
|Profile Data | Time Zone | Yes |
|Profile Data | Date of Birth (DOB) | Yes |
|Profile Data | Bio | Yes |
|Profile Data | Phone Number  | Yes |
|Profile Data | Avatar Image URL | Yes |
|App Usage Data |Session Start | Yes |
|App Usage Data |Session End | Yes |
|Custom Attributes | All Custom Attributes | Yes |
|Recent Devices | Number of Devices | No |
|Recent Devices | Most Recent Watch | No |
|Recent Devices | App Version | No |
|Recent Devices | Device | No |
|Recent Devices | Device OS | No |
|Custom Events | All Custom Events | Yes |
|Purchases | All Purchases | Yes |
|Amplitude Cohort Assignment | All Assignments | Yes |
|Mixpanel Cohort Assignment | All Assignments | Yes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

  {% endtab %}
{% tab Location %}

### Location

|Data Type | Data Point | Does it count towards consumption? |
|---|---|---|
|Most Recent Location | All Most Recent Locations | Yes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %} Entering or exiting geofences doesn't consume data points because geofence data is not stored against the user profile. Geofences are monitored by Apple and Google location services, Braze only gets notified upon a user triggering a geofence. {% endalert %}

  {% endtab %}
{% tab Engagement %}

### Engagement

|Data Type | Data Point | Does it count towards consumption? |
|---|---|---|
| Contact Settings | Email Subscribed | No |
| Contact Settings |  Push Subscribed | No |
| Contact Settings |  Apps Registered for Push | No |
|Campaigns Received | Email Address | No |
|News Feed Cards Clicked | News Feed Cards Clicked | No |
|Install Attribution | Install Source | No |
|Install Attribution | Campaign | No |
|Install Attribution | Ad Group | No |
|Install Attribution | Ad | No |
|Miscellaneous | Random Bucket Number | No |
|Canvas Messages Received | Canvas Messages Received | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

 {% endtab %}
{% tab Social %}

### Social

|Data Type | Data Point | Does it count towards consumption? |
|---|---|---|
|Twitter | Username | Yes |
|Twitter | Followers | No |
|Twitter | Following | No |
|Twitter | Number of Tweets | No |
|Facebook | Likes | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

 {% endtab %}
{% endtabs %}

### Special Circumstances

#### CSV

Custom attributes uploaded via CSV count towards your data points, however CSV imports for segmentation purposes (imports made with `external_id` as the only field) will not consume data points.

#### Arrays

An array (or string) is an ordered collection of items stored within a custom attribute. In terms of consumption, it costs one data point per API call it takes to update the array.

That means if you set the whole array at once, it counts as one data point. However if you add values to the array incrementally, it counts as one data point per value.
