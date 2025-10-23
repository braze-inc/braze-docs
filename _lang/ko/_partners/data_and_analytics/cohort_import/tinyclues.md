---
nav_title: Tinyclues
article_title: Tinyclues
alias: /partners/tinyclues/
description: "This reference article outlines the partnership between Braze and Tinyclues, which offers an audience-building feature to help you send to more targeting campaigns, find new product opportunities, and elevate revenue using an incredibly user-friendly UI."
page_type: partner
search_tag: Partner

---

# Tinyclues

> [Tinyclues](https://www.tinyclues.com/) is an audience-building feature that offers the capability to increase the number of campaigns and revenue without harming customer experience and analytics to track the performance of CRM campaigns both online and offline.

The Braze and Tinyclues integration offers users a path to better CRM planning and strategy, allowing users to send more targeted campaigns, find new product opportunities, and elevate revenue using an incredibly user-friendly UI.

## Prerequisites

| Requirement | Description |
|---|---|
| Tinyclues account | A Tinyclues account is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Data import integration

To integrate Braze and Tinyclues, you must configure the Tinyclues platform, export an existing Tinyclues campaign, and create a user cohort segment in Braze that can be used to target users in future campaigns.

### Step 1: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Tinyclues**. 

Here, you will find your REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one.<br><br>![]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"} 

To complete the integration, you will need to provide the data import key and REST endpoint to your Tinyclues data operations team. Tinyclues will then establish the connection and reach out to you after the setup is complete.

### Step 2: Export a campaign from the Tinyclues platform

Each time you want to create a cohort of Tinyclues users to use in Braze, you'll have to first export it from the Tinyclues platform.

In Tinyclues, select the campaign(s) you want to export and click **Export Campaigns**. Upon export, the audience will be automatically uploaded to your Braze account.

![]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Step 3: Create a segment from the Tinyclues custom audience

In Braze, navigate to **Segments**, name your Tinyclues cohort segment, and select **Tinyclues Cohorts** as your filter. From here, you can choose which Tinyclues cohort you wish to include. After your Tinyclues cohort segment is created, you can select it as an audience filter when creating a campaign or Canvas.

![]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![In the Braze segment builder, the user attributes filter "Tinyclues cohort" is set to "includes" and "Primary cohort".]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Having trouble locating your cohort? Check out our [troubleshooting](#troubleshooting) section for guidance. 

{% alert important %}
Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.
{% endalert %}

## Using this integration

To use your Tinyclues segment, create a Braze campaign or Canvas and select the segment as your target audience. 

![In the Braze campaign builder on the targeting step, the "Target users by segment" filter is set to "Tinyclues cohort".]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.

## Troubleshooting

Are you having trouble finding the right cohort within the list? In Tinyclues, view your campaign details and verify the name by checking the **Export File Name**.

![The bottom of the campaign details page shows your cohort name.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Still having trouble retrieving your audience? Contact the [Tinyclues team](mailto:support@tinyclues.com) for additional support.

