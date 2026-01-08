---
nav_title: Amplitude
article_title: Amplitude Cohort Import
description: "This reference article outlines the cohort import functionality of Amplitude, a product analytics and business intelligence platform."
page_type: partner
search_tag: Partner
---

# Amplitude cohort import

> This article covers how to import user cohorts from [Amplitude](https://amplitude.com/) to Braze. For more information on integrating Amplitude and its other functionalities, see the main [Amplitude article]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Data import integration

Any integration you set up will count toward your account's data point volume.

### Step 1: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Amplitude**. Here, you will find the REST endpoint and generate your Braze data import key. 

Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Amplitude's dashboard.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Step 2: Set up the Braze integration in Amplitude

In Amplitude, navigate to **Sources & Destinations** > **[project name]** > **Destinations** > **Braze**. In the prompt that appears, provide the Braze data import key and REST endpoint, and click **Save**.

![]({% image_buster /assets/img/amplitude.png %})

### Step 3: Export an Amplitude cohort to Braze

First, to export users from Amplitude to Braze, create a [cohort](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) of users you wish to export. Amplitude can sync cohorts to Braze using the following identifiers:
- User Alias
- Device ID
- User ID (External ID)

Amplitude supports multiple identifier mapping properties in priority order. You can configure a primary, secondary, and tertiary identifier mapping. During sync, if a user is missing the primary, Amplitude uses the next available one. This improves sync coverage, reduces dropped users, and includes more anonymous and partially identified users in your sync. 

Once you have created a cohort, click **Sync to...** to export these users to Braze.

{% alert important %}
Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.
{% endalert %}

#### Defining sync cadence

Cohort syncs can be set to be one-time sync, scheduled as daily or hourly, or even real-time which updates every minute. 

Any integration you set up will log data points. If you have any questions about the nuances of Braze data points, your Braze account manager can answer them.

### Step 4: Segment users in Braze

In Braze, to create a segment of these users, navigate to **Segments** under **Engagement**, name your segment, and select **Amplitude Cohorts** as the filter. Next, use the "includes" option and choose the cohort you created in Amplitude. 

![In the Braze segment builder, the filter "amplitude_cohorts" is set to "includes_value" and "Amplitude cohort test".]({% image_buster /assets/img/amplitude2.png %})

After saving, you can reference this segment during Canvas or campaign creation in the targeting users step.

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.
