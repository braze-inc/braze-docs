---
nav_title: Heap
article_title: "Heap Analytics"
description: "This reference article outlines how to use Braze Currents to automatically analyze engagement events with Heap, a digital insights platform, that allows you to import Heap data to Braze, create user cohorts, and export Braze data to Heap to create segments."
page_type: partner
alias: /partners/heap/
search_tag: Partner

---

# Heap analytics

> This article describes how to automatically send engagement events from Braze to Heap for analysis. For more information on integrating Heap and its other functionalities, such as [syncing Heap cohorts]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/#data-import-integration) to Braze, see the main [Heap article]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import/).

## Data export integration

Use Braze Currents to automatically send engagement events (for example, email sent, push sent) from Braze to Heap for analysis.

### Step 1: Get Heap credentials

You’ll need a webhook endpoint URL to configure this integration, which you can get from your Heap account manager.

### Step 2: Configure Braze Currents

In Braze, navigate to **Partner Integrations** > **Data Export**, click **Create New Current**, and select **Heap Export**. 

Give your export a name, then proceed to the **Current Details** page. On this page, enter the endpoint and optional bearer token (if provided).

After configuring your integration's credentials, check all message engagement, customer behavior, and user events you would like to export to Heap, and click **Launch Current**.

![]({% image_buster /assets/img/heap/heap4.png %}){: style="max-width:90%;"}

