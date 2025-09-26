---
nav_title: Hightouch Cohort Import
article_title: Hightouch Cohort Import
description: "This reference article outlines the cohort import functionality of Hightouch, a platform to sync your customer data from your warehouse to business tools."
page_type: partner
search_tag: Partner

---
# Hightouch cohort import

> This article describes how to import user cohorts from [Hightouch](https://hightouch.io) to Braze so you can send targeted campaigns based on data that may only exist in your warehouse. For more information on integrating Hightouch and its other functionalities, see the main [Hightouch article]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch/).

## Data import integration

### Step 1: Get the Braze data import Key
In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Hightouch**. 

Here, you will find your REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one.<br><br>![]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"} 

### Step 2: Add Braze cohorts as a Destination in Hightouch
Navigate to the **Destination** page in your Hightouch workspace, search for **Braze Cohorts**, and click **Continue**. From there, take your REST endpoint and data import key and click **Continue**.<br><br>![]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### Step 3: Sync a model (or audience) into Braze Cohorts
In Hightouch, using your created [model](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) or [audience](https://hightouch.io/docs/audiences/usage/), create a new sync. Next, select the Braze Cohorts destination you created in the previous step. Lastly, in the Braze Cohorts destination configuration, select the identifier you want to match against and decide whether or not you want Hightouch to create a new Braze Cohort or update an existing one.<br><br>![]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.
{% endalert %}

### Step 4: Create a Braze segment from the Hightouch custom audience
In Braze, navigate to **Segments**, create a new segment, and select **Hightouch Cohorts** as your filter. From here, you can choose which Hightouch cohort you wish to include. After your Hightouch cohort segment is created, you can select it as an audience filter when creating a campaign or Canvas.<br><br>![]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### Using this integration
To use your Hightouch segment, create a Braze campaign or Canvas and select the segment as your target audience.<br><br>![]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.

