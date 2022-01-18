---
nav_title: Kubit
article_title: Kubit
page_order: 1
description: "This article outlines the partnership between Braze and Kubit, a no-code, self-service analytics platform that delivers instant product insights."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/) is a no-code, self-service analytics platform that delivers instant product insights. 

The Braze and Kubit integration allows you to import Kubit user cohorts and target them in the Braze messaging. In addition, through the use of [Snowflake secure data sharing]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/), you can also integrate the raw campaign and impression data from Braze with Kubit product analytics to measure the impact of these campaigns in real-time. This approach provides insights into the full lifecycle of your users without requiring any engineering efforts.

## Prerequisites

| Requirement | Description |
|---|---|
|Kubit enterprise account | A Kubit enterprise account is required to take advantage of this partnership. |
| Matching user IDs | Your customer data in Kubit and Braze must have matching user IDs across the two platforms. This also includes anonymous UUIDs. Visit our [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) to read about how Braze sets user IDs. |
{: .reset-td-br-1 .reset-td-br-2} 

## Integration

### Step 1: Get the Braze data import key

In Braze, navigate to **Technology Partners** and select **Kubit**. Here, you will find the REST endpoint and generate your Braze data import key. Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Kubit's dashboard.<br><br>![Config on Kubit]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Step 2: Configure Braze in Kubit

Provide the Braze data import key and Braze REST endpoint to your Kubit support contact. They will configure the integration on their side and let you know when the integration is live.  

### Step 3: Import Cohorts to Braze

#### Create a cohort in Kubit
[Create a cohort](https://www.kubit.ai/doc/fundamentals#cohort) in Kubit and define the criteria of your target users.<br><br>![Create a cohort]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Import users to Braze
Once you have saved your cohort, you can import them to Braze to be used in Braze segments. These segments can then be used to create targeted email or push campaigns and Canvases.

To do this, navigate to your existing cohort and under **Cohort Control** select **Import to Braze**.

![Import to Braze]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

Next, select the desired import cadence. One-time imports allow you to import once now. Scheduled imports allow you to import daily, weekly, or monthly at a specific time. Note that each cohort can only have one live import schedule. 

![Import Schedule]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

#### Verify import status
Once an import has been completed, an email notification will be sent to the recipients(s) specified in the import schedule. You can also check a cohort's import status under **Schedule** in Kubit. The schedule history will display every import execution time, outcome, and the total number of users in the cohort who were imported to Braze.<br><br>![Import History]({% image_buster /assets/img/kubit/import_history.png %})<br><br>You can manually trigger an import by clicking on **Import to Braze** icon for that import schedule.

### Step 4: Create Braze segments with Kubit cohorts
After importing cohorts to Braze, you can use them as filters to create Braze segments and include them in Braze campaigns or Canvas. Visit our segment documentation to learn more about [how to create Braze segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

![Segment with Kubit Cohorts]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## Analyze Braze data in Kubit (optional)
Take advantage of [Snowflake secure data sharing]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) to share your Braze raw campaign and impression data with Kubit to incorporate them into Kubit’s self-service analytics, providing you a full picture of users’ lifecycle.

For reference, here are all the [Braze fields]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2) which are available to be incorporated into Kubit analytics. The details of this step are very customer-specific and require special configurations. Please talk to your Kubit Account Manager or [support@kubit.ai](support@kubit.ai) to learn more.