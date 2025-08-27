---
nav_title: Mixpanel
article_title: Mixpanel Cohort Import
description: "This reference article outlines the cohort import functionality of Mixpanel, a business analytics platform, allowing you to import Mixpanel Cohorts into Braze to create Braze segments that can be used to target users in future Braze campaigns or Canvases."
page_type: partner
search_tag: Partner
---

# Mixpanel cohort import

> This article describes how to import user cohorts from [Mixpanel](https://mixpanel.com/) to Braze. For more information on integrating Mixpanel and its other functionalities, see the main [Mixpanel article]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

## Data import integration

If your Braze pricing includes data points, any integration you set up will log data points.

{% alert important %}
In adherence to Mixpanel's data retention policies, events sent before January 1, 2010 will be removed during import.
{% endalert %}

### Step 1: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Mixpanel**. Here, you will find the REST endpoint and generate your Braze data import key. 

Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Mixpanel's dashboard.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Step 2: Set up the Braze integration in Mixpanel

In Mixpanel, navigate to **Data Management > Integrations.** Next, select the Braze integration tab and click **Connect**. In the prompt that appears, provide the Braze data import key and REST endpoint, and click **Continue**.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Step 3: Export a Mixpanel cohort to Braze

In Mixpanel, navigate to **Data Management > Cohorts**. Select the cohort to send to Braze and then select **Export to Braze**. Lastly, select a one-time sync or dynamic sync. Selecting dynamic sync will sync your Braze cohort every 15 minutes to match users in Mixpanel. 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.
{% endalert %}

### Step 4: Segment users in Braze

In Braze, to create a segment of these users, go to **Audience** > **Segments**, name your segment, and select **Mixpanel_Cohorts** as the filter. Next, use the "includes" option and choose the cohort you created in Mixpanel. 

![In the Braze segment builder, the user attributes filter "Mixpanel cohorts" is set to "includes" and "Braze cohort".]({% image_buster /assets/img_archive/mixpanel1.png %})

After saving, you can reference this segment during Canvas or campaign creation in the targeting users step.

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.