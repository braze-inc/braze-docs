---
nav_title: Splio
article_title: Splio
alias: /partners/splio/
description: "This reference article outlines the partnership between Braze and Splio, which lets you send more targeted campaigns, find new product opportunities, and elevate revenue."
page_type: partner
search_tag: Partner

---

# Splio

> [Splio](https://splio.com/) is an audience-building tool that lets you increase the number of campaigns and revenue without harming customer experience, and provides analytics to track the performance of CRM campaigns both online and offline.

The Braze and Splio integration lets you plan and execute better CRM strategies, send more targeted campaigns, find new product opportunities, and elevate revenue.

## Prerequisites

| Requirement | Description |
|---|---|
| Splio account | You need a Splio account for this partnership. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Data import integration

To integrate Braze and Splio, you must configure the Splio platform, export an existing Splio campaign, and create a cohort segment in Braze to target users in future campaigns.

### Step 1: Get the Braze data import key

In Braze, go to **Partner Integrations** > **Technology Partners** and select **Splio**.

Find your REST endpoint and generate your Braze data import key. After you generate the key, you can create a new key or invalidate an existing one.<br><br>![The Splio technology partner page with the REST endpoint and data import key.]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

To complete the integration, provide the data import key and REST endpoint to your Splio data operations team. Splio establishes the connection and contacts you after the setup is complete.

### Step 2: Export a campaign from the Splio platform

Each time you want to create a cohort of Splio users in Braze, you must first export it from the Splio platform.

In Splio, select the campaigns you want to export and click **Export Campaigns**. After you export, the audience is automatically uploaded to your Braze account.

![Exporting campaigns from the Splio platform.]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Step 3: Create a segment from the Splio custom audience

In Braze, navigate to **Segments**, name your Splio cohort segment, and select **Splio Cohorts** as your filter. From here, choose which Splio cohort to include. After you create your Splio cohort segment, you can select it as an audience filter when creating a campaign or Canvas.

![Creating a Splio cohort segment in Braze.]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![In the Braze segment builder, the user attributes filter "Splio cohort" is set to "includes" and "Primary cohort".]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Having trouble locating your cohort? Check out the [troubleshooting](#troubleshooting) section for guidance.

{% alert important %}
Only users who already exist in Braze are added or removed from a cohort. Cohort Import does not create new users in Braze.
{% endalert %}

## Using this integration

To use your Splio segment, create a Braze campaign or Canvas and select the segment as your target audience.

![In the Braze campaign builder on the targeting step, the "Target users by segment" filter is set to "Splio cohort".]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## User matching

Braze matches identified users by their `external_id` or `alias`. Anonymous users are matched by their `device_id`. Identified users who were originally created as anonymous users can't be matched by their `device_id`, and must be matched by their `external_id` or `alias`.

## Troubleshooting

If you can't find the right cohort in the list, view your campaign details in Splio and verify the name by checking the **Export File Name**.

![The bottom of the campaign details page shows your cohort name.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

If you're having trouble retrieving your audience, contact the [Splio team](mailto:support-team@splio.com) for support.