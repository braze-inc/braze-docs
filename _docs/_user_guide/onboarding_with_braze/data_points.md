---
nav_title: Data Points
article_title: Data Points Overview
page_order: 4
page_type: reference
description: "This reference article outlines what Data Points are at Braze and how you can be aware of their usage."

---

# Data points

At Braze, data means action: each piece of data that arrives in Braze updates segment membership, can trigger and cancel messaging, is immediately available for messaging personalization, and more. As such, data points are Braze’s way of defining a billing and pricing structure, based on pieces of information logged against user profiles. See the [Consumption count](#consumption-count) section of this article to understand what data counts toward your data point allocation.
 
Our Customer Success team can help recommend data best practices to fit your specific needs. You can find a more detailed breakdown of this definition in your Braze contract.

## Management and usage

To view your Data Point Dashboard, select your name in the top-right corner, click the drop down, and select **Subscriptions and Usage**. For more information on the Data Point Dashboard components, refer to [Subscriptions and usage]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/).

{% alert tip %}
**Only update your deltas (changing data)!**

To prevent using up your allocated data points, we recommend setting up a program that will prevent sending the same, unchanging data from your app to Braze over and over.
{% endalert %}

## Consumption count

In sum, data points are accumulated when a user's profile data is updated or when they perform specific actions. Essentially, data points are counts of each of your users' `session starts`, `session ends`, `events`, and `purchases`.

You can find a breakdown of how Braze accumulates data points in the following sections, but there are nuances beyond what you see here, which may affect the number of remaining points you expect to see. If you ever have any questions about your billing, reach out to your Braze account manager.

{% alert note %} 
Connected Content does not consume data points—using Connected Content is a great way to reference data from other platforms without needing to bulk upload to Braze and use up your points! 
{% endalert %}

{% tabs %}
{% tab General %}

### General

|Data type | Data point | Does it count towards consumption? |
|---|---|---|
|Profile data | First name | Yes |
|Profile data | Last name | Yes |
|Profile data | User ID | No |
|Profile data | User alias | No |
|Profile data | Email address | Yes |
|Profile data | Gender | Yes |
|Profile data | Age group | Yes |
|Profile data | Country | Yes |
|Profile data | City | Yes |
|Profile data | Language | Yes |
|Profile data | Most recent device locale | Yes |
|Profile data | Time zone | Yes |
|Profile data | Date of birth (DOB) | Yes |
|Profile data | Bio | Yes |
|Profile data | Phone number  | Yes |
|App usage data |Session start | Yes |
|App usage data |Session end | Yes |
|Custom attributes | All custom attributes | Yes |
|Recent devices | Number of devices | No |
|Recent devices | Most recent watch | No |
|Recent devices | App version | No |
|Recent devices | Device | No |
|Recent devices | Device OS | No |
|Custom events | All custom events | Yes |
|Custom event properties | All custom event properties* | Yes |
|Purchases | All purchases | Yes |
|Amplitude cohort assignment | All assignments | Yes |
|Mixpanel cohort assignment | All assignments | Yes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
In regards to subscription usage, custom event properties enabled for segmentation with the filters `X Custom Event Property in Y Days` or `X Purchase Property in Y Days` are all counted as separate data points in addition to the data point counted by the custom event itself.
{% endalert %}

{% endtab %}
{% tab Location %}

### Location

|Data type | Data point | Does it count towards consumption? |
|---|---|---|
|Most recent location | All most recent locations | Yes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %} Entering or exiting geofences doesn't consume data points because geofence data is not stored against the user profile. Geofences are monitored by Apple and Google location services, Braze only gets notified upon a user triggering a geofence. {% endalert %}

  {% endtab %}
{% tab Engagement %}

### Engagement

|Data type | Data point | Does it count towards consumption? |
|---|---|---|
| Contact settings | Email subscribed | No |
| Contact settings |  Push subscribed | No |
| Contact settings |  Apps registered for push | No |
|Campaigns received | Email address | No |
|News Feed cards clicked | News Feed Cards clicked | No |
|Install attribution | Install source | No |
|Install attribution | Campaign | No |
|Install attribution | Ad Group | No |
|Install attribution | Ad | No |
|Miscellaneous | Random bucket number | No |
|Canvas messages received | Canvas messages received | No |
| Contact settings | Subscription group | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

 {% endtab %}
{% tab Social %}

### Social

|Data type | Data point | Does it count towards consumption? |
|---|---|---|
|Twitter | Username | Yes |
|Twitter | Followers | No |
|Twitter | Following | No |
|Twitter | Number of tweets | No |
|Facebook | Likes | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

 {% endtab %}
{% endtabs %}

### Special circumstances

#### CSV

Custom attributes uploaded via CSV count towards your data points, however csv imports for segmentation purposes (imports made with `external_id` as the only field) will not consume data points.

#### Arrays

An array (or string) is an ordered collection of items stored within a custom attribute. In terms of consumption, it costs one data point per API call it takes to update the array.

That means if you set the whole array at once, it counts as one data point. However if you add values to the array incrementally, it counts as one data point per value.
