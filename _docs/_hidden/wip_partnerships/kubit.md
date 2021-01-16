---
nav_title: Kubit
page_order: 1

description: "This article outlines the partnership between Braze and Kubit, a No-Code and Self-Service analytics platform that delivers Instant Product Insights."
alias: /partners/kubit/

page_type: partner
hidden: true
---

# Kubit

> [Kubit](https://kubit.ai/) is a No-Code, Self-Service analytics platform that delivers Instant Product Insights. Through the seamless No-Code integration with Braze, you can import user cohort information into Braze and launch engagement campaigns to target specific cohorts. Furthermore, through [Snowflake Secure Data Sharing](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/), you can integrate the raw campaign and impression data from Braze with product analytics in Kubit to measure the impact of these campaigns, in real-time. This approach provides insights to the full lifecycle of your users, without requiring any engineering efforts.

## Requirements
* The Braze Integration feature is only available to Kubit Enterprise customers.
* Your customer data in Kubit and Braze must have matching User IDs for this integration to match customers between the two platforms. This includes Anonymous UUIDs.
* Please read about [how Braze set User IDs here](https://www.braze.com/docs/developer_guide/platform_integration_guides/fireos/analytics/setting_user_ids/#setting-user-ids).

{% alert important %}
This integration invokes Braze REST API calls (/users/track) to function. These calls will be counted towards your API limits and quota on Braze side. For details on this topic, please refer to [Braze documentation here](https://www.braze.com/docs/api/basics/#api-limits).
{% endalert %}


## Configure Braze Integration
### Braze API Key
Create a dedicated Braze API Key for this integration. This step gives you full control of the permissions. 

* Visit your [Braze Developer Console](https://dashboard-01.braze.com/app_settings/developer_console/) on your Braze Dashboard. 
* Click “Create New API Key”

![Braze Developer Console]({% image_buster /assets/img/kubit/braze_developer_console.png %})

* Enter a name for the API Key (eg “Kubit”) and only grant permission for “users.track” in the “User Data” section. 

![Braze API Key]({% image_buster /assets/img/kubit/braze_api_key.png %})

You can also find references for these steps in [Braze API Key Documentation](https://www.braze.com/docs/api/basics/#app-group-rest-api-keys). 

### Configure on Kubit
Provide the Braze API Key and your Braze Endpoint location.

![Config on Kubit]({% image_buster /assets/img/kubit/config_on_kubit.png %})


## Import Cohorts to Braze
* **Create a cohort in Kubit**. First use Cohort in Kubit to define the criteria to select your target users.

![Create a Cohort]({% image_buster /assets/img/kubit/create_cohort.png %})

* **Import to Braze**. Once a cohort is saved, you can import these users to Braze so they can be used in Braze Segments to send them email or push notifications (through Campaign or Canvas). 

![Import to Braze]({% image_buster /assets/img/kubit/import_to_braze.png %})

* There are two import schedule modes:
1. One-Time Import: Import once now.
2. Scheduled Import: Import daily, weekly or monthly at a specific time. 

![Import Schedule]({% image_buster /assets/img/kubit/import_schedule.png %})

**Note**: each cohort can only have one live import schedule.

* **Check Import Status**. Whenever an import is completed, an email notification will be sent to the Recipient(s) specified in the import schedule. You can also check a cohort’s import status in Schedules. The schedule history will display every import execution time, outcome and total number of users in the cohort who were imported to Braze. 

![Import History]({% image_buster /assets/img/kubit/import_history.png %}) 

You can manually trigger an import by clicking on Import to Braze icon for that import schedule.

## Create Braze Segments with Kubit Cohorts
After cohorts are imported to Braze, you can use them as Filters to create Braze Segments and include them in Braze Campaigns or Canvas. [Here is a reference about how to create Segments on Braze.](https://www.braze.com/docs/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment)  

![Segment with Kubit Cohorts]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}) 

## Analyze Braze Data in Kubit
You can also take advantage of [Snowflake Secure Data Sharing](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) to share your Braze raw campaign and impression data with Kubit to incorporate them into Kubit’s Self-Service Analytics and provide you the full picture of users’ lifecycle, from attribution to behavior to engagement.  

For references, here are all the [Braze tables](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2) which are available to be incorporated into Kubit analytics. The details of this step are very customer specific and require special configurations. Please talk to your Kubit Account Manager or support@kubit.ai to learn more.
