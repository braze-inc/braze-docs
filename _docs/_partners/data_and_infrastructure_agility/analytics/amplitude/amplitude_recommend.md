---
nav_title: Amplitude Recommend
article_title: Amplitude Recommend
page_order: 0
alias: /partners/amplitude_recommend/
description: "This article outlines the partnership between Braze Currents and Amplitude, a product analytics and business intelligence platform."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude Recommend

> [Amplitude](https://amplitude.com/) is a product analytics and business intelligence platform.

The Braze and Amplitude bi-directional integration allows you to import your Amplitude Cohorts, user traits, and events into Braze, as well as create segments that can target users in future campaigns or Canvases. You can also leverage Braze Currents to [export your Braze events to Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration) to perform deeper analytics of your product and marketing data.

## Prerequisites

| Requirement | Description |
|---|---|
| Amplitude account | An [Amplitude account](https://amplitude.com/) is required to take advantage of this partnership. |
| Currents | In order to export data back into Amplitude, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2} 

## Data import integration

Use Braze and Amplitude's partnership to import Amplitude cohorts directly into Braze for audience segmentation. This allows you to perform deep analysis using Amplitude and seamlessly execute your strategies using Braze.

{% include video.html id="8a57e44be7da423e9699cedd6c241eae" source="loom"%}

Any integration you set up will count towards your account's data point volume.

### Step 1: Get the Braze data import key

In Braze, navigate to **Technology Partners** and select **Amplitude**. Here, you will find the REST endpoint and generate your Braze data import key. Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Amplitude's dashboard.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Step 2: Set up the Braze integration in Amplitude

In Amplitude, navigate to **Sources & Destinations > [project name] > Destinations > Braze**. In the prompt that appears, provide the Braze data import key and REST endpoint, and click **Save**.

![]({% image_buster /assets/img/amplitude.png %}){: style="max-width:50%;"}

### Step 3: Export an Amplitude cohort to Braze

First, to export users from Amplitude to Braze, create a [cohort](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) of users you wish to export. Once you have created a cohort, click **Sync to...** to export these users to Braze.

#### Defining Sync Cadence

Cohort syncs can be set to be one-time sync, scheduled as daily or hourly, or even real-time which updates every minute. Make sure to select an option that makes sense for your business needs while also being mindful of consuming [data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/).

### Step 4: Segment users in Braze

In Braze, to create a segment of these users, navigate to **Segments** under **Engagement**, name your segment, and select **Amplitude Cohorts** as the filter. Next, use the "includes" option and choose the cohort you created in Amplitude. 

![In the Braze segment builder, the filter "amplitude_cohorts" is set to "includes_value" and "Amplitude cohort test".]({% image_buster /assets/img/amplitude2.png %})

Once saved, you can reference this segment during Canvas or campaign creation in the targeting users step.

## Sync user traits and computations

Use Recommend to send user properties and computations to Braze as custom attributes. You will be able to sync user properties or computed properties for users who have been active in the last 90 days.

When a user’s property or a computation updates, Amplitude will update a custom attribute in Braze with the same name as that user property or computation.

User trait and computation syncs will create new users for user IDs that do not yet exist within Braze. Computations and user traits can only be synced using user ID.

## Amplitude user profile API endpoints

To check out some of the common Amplitude API endpoints that can be used with Connected Content, view our dedicated [Amplitude API documentation]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/).
