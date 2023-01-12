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

“Data Points” shall refer to a billable unit of use of the Braze Services, measured by a session start, session end, custom event or purchase recorded, as well as any attribute set on an End User profile. Data and events collected by default by the Braze Services including, for example, push tokens, device information, and all campaign engagement tracking events, such as email opens and push notification clicks, are not counted as Data Points. For clarity, the setting of an End User’s profile information at one point in time shall count as a single Data Point.

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
The following actions do not consume data points:
- Deleting users from Braze
- Using Connected Content in messaging
{% endalert %}

### Billable data points

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="large_table"></div>

| Data type | Data point | Notes |
| --------- | ---------- | ----- |
| Profile data | First name | |
| Profile data | Last name | |
| Profile data | Email address | |
| Profile data | Gender | |
| Profile data | Age group | |
| Profile data | Country | When manually collected. Does not count towards consumption when automatically collected. |
| Profile data | City | |
| Profile data | Language | When manually collected. Does not count towards consumption when automatically collected. |
| Profile data | Most recent device locale | |
| Profile data | Time zone | |
| Profile data | Date of birth (DOB) | |
| Profile data | Bio | |
| Profile data | Phone number | |
| App usage data | Session start | |
| App usage data | Session end | |
| Custom attributes | All custom attributes | |
| Custom events | All custom events | |
| Custom event properties | All custom event properties | Custom event properties enabled for segmentation with the filters `X Custom Event Property in Y Days` or `X Purchase Property in Y Days` are all counted as separate data points in addition to the data point counted by the custom event itself.
| Purchases | All purchases | |
| Amplitude cohort assignment | All assignments | |
| Mixpanel cohort assignment | All assignments | |
| Hightouch cohort assignment | All assignments | |
| Appsflyer cohort assignment | All assignments | |
| Most recent location | All most recent locations | Entering or exiting geofences doesn’t consume data points because geofence data is not stored against the user profile. Geofences are monitored by Apple and Google location services; Braze only gets notified upon a user triggering a geofence. |
| Twitter | Username | |
{: .reset-td-br-1 .reset-td-br-2}

### Non-billable data points (out of the box)

<div class="small_table"></div>

| Data type | Data point |
| --------- | ---------- |
| Profile data | Country |
| Profile data | Language |
| Profile data | User ID |
| Profile data | User alias |
| Recent devices | Number of devices |
| Recent devices | Most recent watch |
| Recent devices | App version |
| Recent devices | Device |
| Recent devices | Device OS |
| Contact settings | Email subscribed |
| Contact settings | Push subscribed |
| Contact settings | Apps registered for push |
| Contact settings | Subscription group |
| Campaigns received | Email address |
| Install attribution | Install source |
| Install attribution | Campaign |
| Install attribution | Ad Group |
| Install attribution | Ad |
| Miscellaneous | Random bucket number |
| Canvas messages received | Canvas messages received |
| Twitter | Followers |
| Twitter | Following |
| Twitter | Number of tweets |
| Facebook | Likes |
{: .reset-td-br-1 .reset-td-br-2}

### Special circumstances

#### CSV

Custom attributes uploaded via CSV count towards your data points, however CSV imports for segmentation purposes (imports made with `external_id` as the only field) will not consume data points.

#### Arrays

An array (or string) is an ordered collection of items stored within a custom attribute. In terms of consumption, it costs one data point per API call it takes to update the array.

That means if you set the whole array at once, it counts as one data point. However if you add values to the array incrementally, it counts as one data point per value.
