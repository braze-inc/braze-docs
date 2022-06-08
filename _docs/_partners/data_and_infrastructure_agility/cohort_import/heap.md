---
nav_title: Heap
article_title: Heap
page_order: 1
description: "This article details the integration between Braze and Heap, a digital insights platform."
alias: /partners/heap/
page_type: partner
search_tag: Partner

---

# Heap

> [Heap](https://heap.io/), a digital insights platform, focuses you on opportunities in your digital experience that most impact your business, eliminating friction, delighting your customers, and accelerating revenue.

The Braze and Heap integration enables you to [import Heap data to Braze](#data-import-integration), create user cohorts, as well as [export Braze data to Heap](#data-export-integration) to create segments.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Heap account | A [Heap](https://heap.io/about) account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
| Braze Currents | In order to export data from Braze to Heap, you will need [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) enabled on your account. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases
1. Re-engage users who have abandoned a funnel: Trigger re-engagement messaging when users abandon the purchase or subscription funnel.
2. Personalize the trial experience: Identify friction points in your trial experience and send correctly timed reminders to re-engage users during a trial and help them get to value.
3. Drive higher engagement on announcements and offers: Target promotions, updates, and new service announcements to the relevant audiences.

## Data import integration

Use the Heap to Braze integration to automatically sync cohorts defined in Heap to Braze.

### Step 1: Get the Braze data import key

In Braze, click on **Technology Partners** and then select **Heap**. On this page, you can find your data import key and a REST Endpoint. Take note of both of these values and provide them to your Heap account manager to finish setting up the integration. 

![][3]{: style="max-width:90%;"}

### Step 2: Segment imported users in Braze

In Braze, navigate to **Segments**, name your Heap cohort segment, and select **Heap Cohorts** as your filter. From here, you can choose which Heap cohort you wish to include. Once created, you can select your Heap cohort segment as an audience filter when creating a campaign or Canvas.

![In the Braze segment builder, the user attributes filter "Heap cohort" is set to "includes" and "Heap Test Cohort".][2]{: style="max-width:90%;"}

### Using this integration

To use your Heap segment, create a Braze campaign or Canvas and select the segment as your target audience. 

![In the Braze campaign builder on the targeting step, the "Target users by segment" filter is set to "Heap cohort".][4]{: style="max-width:90%;"}

## Data export integration

Use Braze Currents to automatically send engagement events (e.g email sent, push sent) from Braze to Heap for analysis.

### Step 1: Get Heap credentials

You'll need a webhook endpoint URL to configure this integration, which you can get from your Heap account manager.

### Step 2: Configure Braze Currents

In Braze, navigate to **Currents** under **Integrations** and click **Create New Current** and select **Custom Currents Export**. Give your export a name, and then proceed to the **Current Details** page. On this page, you'll need to enter the endpoint and optional bearer token (if provided).

After configuring your integration's credentials, check all message engagement, customer behavior, and user events you would like to export to Heap, and click **Launch Current**.

![][5]{: style="max-width:90%;"}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/heap/heap1.png %} 
[3]: {% image_buster /assets/img/heap/heap2.png %} 
[4]: {% image_buster /assets/img/heap/heap3.png %} 
[5]: {% image_buster /assets/img/heap/heap4.png %} 
