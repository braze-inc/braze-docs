---
nav_title: Creating a Formula
article_title: Creating a Formula
page_order: 1.2
page_type: reference
description: "This reference article covers creating and managing formulas, which help you easily understand complex relationships that exist in your data."
tool: Reports

---
# Creating a formula

## What are formulas?

Braze's analytics views now allow you to combine several data points together to provide valuable insights into your user data. Formulas will allow you to normalize your time series data based on your total number of MAU/DAU as well as to easily understand complex relationships that exist in your data. For example, you can compare how many custom events were completed by daily active users that qualify for a particular segment versus the general population (or against another segment).

## Where to access your formulas

Formulas can be accessed in the "Detailed Statistics" panels on the [Overview][9], [Revenue][10] and [Custom Events][11] pages in the dashboard. To view this panel, change the **View Statistics For** dropdown to "KPI Formulas".

![View statistics for KPI formulas in the Braze dashboard][16]

## How to create a new formula

To create a new formula, navigate to the appropriate dashboard (Overview, Revenue, or Custom Events) and click **Manage Formulas** in the detailed statistics section. From there, enter a name for your formula and select the relevant numerators and denominators. Save your formula.

## Available numerators and denominators

### App usage dashboard
The available numerators are:

* DAU
* Sessions

The available denominators are:

* MAU
* DAU
* Segment Size

### Revenue dashboard
The available numerators are:

* Purchases (all)
* Select Purchases (e.g a gift card or a product ID)

The available denominators are:

* DAU
* MAU

### Custom event dashboard
The available numerators are:

* Custom Event Count

The available numerators are:

* MAU
* DAU
* Segment Size (only segments that have [analytics tracking][17] enabled can be used)

## Use cases
Formulas, especially when combined with custom events, allow you to better understand user behaviors within your app. Formulas can also lend deeper insight into segment purchasing patterns, even if your company uses paid media in conjunction with Braze, e.g., Google Ads or TV. The following are some examples of the kinds of behavior patterns that can be detected using Formulas:

* Ride-sharing apps: If you have a custom event for when the user cancels a ride, configuring a function for Cancelled Rides / DAU can be used to find if certain user segments tend to cancel more rides than others.
* E-commerce apps: By configuring a function for purchases of a certain product ID / MAU, you can, for example, compare the popularity of a recently promoted product between segments, even if all of the promotions couldn't be tracked using Braze.
* Media apps using ads: If the users' experience is interrupted by ads between video or audio clips, recording mid-ad exits as a custom event and calculating the ratio of mid-ad exits / DAU can help find the best segments to target with a campaign for ad-free premium subscriptions.

[9]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/
[10]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[16]: {% image_buster /assets/img_archive/kpi_forms.png %}
[17]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
