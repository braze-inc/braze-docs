---
nav_title: Splio
article_title: Splio
alias: /partners/splio/
description: "This reference article outlines the partnership between Braze and Splio, which offers an audience-building feature to help you send to more targeting campaigns, find new product opportunities, and elevate revenue using an incredibly user-friendly UI."
page_type: partner
search_tag: Partner

---

# Splio

> [Splio](https://splio.com/) is an audience-building feature that offers the capability to increase the number of campaigns and revenue without harming customer experience and analytics to track the performance of CRM campaigns both online and offline.

The Braze and Splio integration offers users a path to better CRM planning and strategy, allowing users to send more targeted campaigns, find new product opportunities, and elevate revenue using an incredibly user-friendly UI.

## Prerequisites

| Requirement | Description |
|---|---|
| Splio account | A Splio account is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Data import integration

To integrate Braze and Splio, you must configure the Splio platform, export an existing Splio campaign, and create a user cohort segment in Braze that can be used to target users in future campaigns.

### Step 1: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Splio**.

Here, you will find your REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one.<br><br>![]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

To complete the integration, you must provide the data import key and REST endpoint to your Splio data operations team. Splio will then establish the connection and contact you after the setup is complete.

### Step 2: Export a campaign from the Splio platform

Each time you want to create a cohort of Splio users to use in Braze, you'll have to first export it from the Splio platform.

In Splio, select the campaign(s) you want to export and click **Export Campaigns**. Upon export, the audience will be automatically uploaded to your Braze account.

![]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Step 3: Create a segment from the Splio custom audience

In Braze, navigate to **Segments**, name your Splio cohort segment, and select **Splio Cohorts** as your filter. From here, you can choose which Splio cohort you wish to include. After your Splio cohort segment is created, you can select it as an audience filter when creating a campaign or Canvas.

![]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![In the Braze segment builder, the user attributes filter "Splio cohort" is set to "includes" and "Primary cohort".]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Having trouble locating your cohort? Check out our [troubleshooting](#troubleshooting) section for guidance.

{% alert important %}
Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.
{% endalert %}

## Using this integration

To use your Splio segment, create a Braze campaign or Canvas and select the segment as your target audience.

![In the Braze campaign builder on the targeting step, the "Target users by segment" filter is set to "Splio cohort".]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.

## Troubleshooting

Are you having trouble finding the right cohort within the list? In Splio, view your campaign details and verify the name by checking the **Export File Name**.

![The bottom of the campaign details page shows your cohort name.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Still having trouble retrieving your audience? Contact the [Splio team](mailto:support-team@splio.com) for additional support.

