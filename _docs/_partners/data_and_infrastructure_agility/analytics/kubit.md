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

> [kubit](https://kubit.ai/) is a no-code, self-service analytics platform that delivers instant product insights. through the seamless no-code integration with braze, you can import user cohort information into braze and launch engagement campaigns to target specific cohorts. in addition, through the use of [snowflake secure data sharing]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/), you can integrate the raw campaign and impression data from braze with product analytics in kubit to measure the impact of these campaigns in real-time. this approach provides insights into the full lifecycle of your users, without requiring any engineering efforts.

## Requirements

* __kubit enterprise__ - the braze integration feature is only available to kubit enterprise customers.
* __Braze Data Import Key and REST Endpoint__ - This integration invokes the Braze [/users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to function. These calls will be counted toward your Braze [API limits]({{site.baseurl}}/api/basics/#api-limits).
* __Matching User IDs__ - Your customer data in Kubit and Braze must have matching User IDs for this integration to match customers between the two platforms. This includes Anonymous UUIDs. To read about how Braze sets user IDs, visit our documentation [here]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/). 

## Braze and kubit integration
### Step 1: generate braze data import key
From the Braze dashboard, navigate to __Technology Partners__ and select __Kubit__. 

Here, you will find the REST Endpoint and generate your Braze Data Import Key. Once generated, you will be able to create a new key, or invalidate an existing one as needed. The Data Import Key and the REST Endpoint are used in the next step when setting up a postback in Kubits's dashboard.

![Config on Kubit]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Step 2: configure kubit
Provide the Braze Data Import Key and Braze REST endpoint found in step 1. 

![Config on Kubit]({% image_buster /assets/img/kubit/config_on_kubit.png %}){: style="max-width:30%;"}

### Step 3: import cohorts to braze
1. __Create a Cohort in Kubit__<br>
Create a Cohort in Kubit and define the criteria of yout target users.<br><br>![Create a Cohort]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}<br><br>
2. __Import Users to Braze__<br>
Once you have saved a Cohort in Kubit, you can import these users to Braze to be used in Braze Segments to send email or push notifications to through the use of campaigns or Canvases.<br><br>![Import to Braze]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}<br><br>There are two import schedule modes:<br>- One-Time Import: Import once now.<br>- Scheduled Import: Import daily, weekly or monthly at a specific time. <br><br>![Import Schedule]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}<br><br>Note that each Cohort can only have one live import schedule.<br><br>
3. __Verify Import Status__<br>
Once an import has been completed, an email notification will be sent to the recipients(s) specified in the import schedule. You can also check a Cohort's import status under Schedule in Kubit. The schedule history will display every import execution time, outcome, and the total number of users in the Cohort who were imported to Braze.<br><br>![Import History]({% image_buster /assets/img/kubit/import_history.png %})<br><br>You can manually trigger an import by clicking on Import to Braze icon for that import schedule.

### Step 4: create braze segments with kubit cohorts
After Cohorts are imported to Braze, you can use them as filters to create Braze Segments and include them in Braze campaigns or Canvas. Visit our segment documentation to learn more about [how to create Braze Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

![Segment with Kubit Cohorts]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

### Step 5: analyze braze data in kubit (optional)
You can also take advantage of [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) to share your Braze raw campaign and impression data with Kubit to incorporate them into Kubit’s Self-Service Analytics and provide you the full picture of users’ lifecycle, from attribution to behavior to engagement.  

For references, here are all the [Braze tables]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2) which are available to be incorporated into Kubit analytics. The details of this step are very customer specific and require special configurations. Please talk to your Kubit Account Manager or support@kubit.ai to learn more.