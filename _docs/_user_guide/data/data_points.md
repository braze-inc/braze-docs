---
nav_title: Data points
article_title: Data Points Overview
page_order: 0
page_type: reference
description: "This reference article outlines what data points are at Braze and how you can be aware of their usage."
search_rank: 6
---

# Data points

> At Braze, data means action: each piece of data that arrives in Braze updates segment membership, can trigger and cancel messaging, is immediately available for messaging personalization, and more. Data points help you define the most impactful information for your business. By thoughtfully considering what information to track, you ensure that you're targeting the highest-impact data for your users' experience.

Data points are based on information logged against user profiles. You can find a more detailed breakdown of this definition in your Braze contract. Our Customer Success team can help recommend data best practices to fit your needs. 

## Definition

"Data points" shall refer to a billable unit of use of the Braze Services, measured by a session start, session end, custom event, or purchase recorded, as well as any attribute set on an end user profile. For clarity, each one of the above-mentioned data (such as session start, session end, custom event, or purchase recorded, as well as any attribute) set to an end user’s profile at one point in time shall each count as a single data point.

Data and events collected by default by the Braze Services, including, for example, push tokens, device information, and all campaign engagement tracking events, such as email opens and push notification clicks, are *not* counted as data points.

See this article's [Consumption count](#consumption-count) section to understand what data counts toward your data point allocation.

## Viewing data point usage

To view your data point usage, go to **Settings** > **Billing** and select the **Total Data Points Usage** tab.

For more information on the data point dashboard components, refer to [Billing]({{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/).

{% alert tip %}
**Don't waste data points. Only update changing data!**<br><br>
To minimize data point usage, we recommend setting up a program to prevent sending the same unchanging data and only passing new and relevant data to Braze. Braze will work with you to establish this best practice during onboarding. 
{% endalert %}

## Consumption count

In sum, data points are accumulated when a user's profile data is updated or when they perform specific actions. Essentially, data points are counts of each of your user's `session starts`, `session ends`, `events`, and `purchases`.

You can find a breakdown of how Braze accumulates data points in the following sections. If you ever have any questions about the nuances of Braze data points, your Braze account manager can answer them.

The following actions do not log data points:
- Deleting users from Braze
- Using Connected Content in messaging
- Subscription state changes globally and around subscription groups
- Renaming your users' external IDs through [API calls]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)
- Blocking events, attributes, or event properties

### Special circumstances

#### Arrays

An array is an ordered collection of items stored within a custom attribute. In terms of consumption, updating an array costs one data point per API call. If you add values to an array incrementally, it will count as one data point per value. 

{% alert tip %}
If you set the whole array at once, it will count as a single data point. As such, arrays are a great tool to keep user profiles up-to-date with relevant information and reduce costs.
{% endalert %}

#### Nested custom attributes

Nested custom attributes refer to an object that defines a set of attributes as a property of another attribute. Every key in the object will count as a data point.

{% alert note %}
Updating a custom attribute object to `null` also consumes a data point.
{% endalert %}

#### CSV

Custom attributes uploaded through CSV import count toward your data points. However, CSV imports for segmentation purposes (imports made with `external_id`, `braze_id`, or `user_alias_name` as the only field) will not log data points.

Also, as subscription state changes do not log data points, updating the `email_subscribe`, `push_subscribe`, `subscription_group_id`, or `subscription_state` fields in your CSV file will not incur charges.

## Data points

{% alert note %}
The following tables are intended to be illustrative. For exact naming conventions, capitalization, and accepted values for certain fields, refer to the relevant documentation for your ingestion method.
{% endalert %}

{% tabs %}
{% tab Non-billable %}

#### Non-billable data points (default)

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
| Message engagement | All engagement events (such as opens, clicks, impressions, and dismissals) |
| Twitter | Followers |
| Twitter | Following |
| Twitter | Number of tweets |
| Facebook | Likes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Billable %}

#### Billable data points

{% alert important %}
Adding, removing, or updating the following data types will incur a billable data point.
{% endalert %}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 30%;
}
table th:nth-child(3) {
    width: 50%;
}
table td {
    word-break: break-word;
}
</style>

| Data type | Data point | Notes |
| --------- | ---------- | ----- |
| Profile data | First name | |
| Profile data | Last name | |
| Profile data | Email address | |
| Profile data | Gender | |
| Profile data | Age group | |
| Profile data | Country | When manually collected. Does not count toward consumption when automatically collected. |
| Profile data | City | |
| Profile data | Language | When manually collected. Does not count toward consumption when automatically collected. |
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
| Purchase properties | All purchase properties | |
| Amplitude cohort assignment | All assignments | |
| Mixpanel cohort assignment | All assignments | |
| Hightouch cohort assignment | All assignments | |
| Appsflyer cohort assignment | All assignments | |
| Most recent location | All most recent locations | Entering or exiting geofences doesn't log data points because geofence data is not stored against the user profile. Geofences are monitored by Apple and Google location services; Braze only gets notified upon a user triggering a geofence. |
| Twitter | Username | |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

