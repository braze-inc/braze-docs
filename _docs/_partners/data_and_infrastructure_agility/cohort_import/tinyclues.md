---
nav_title: Tinyclues
article_title: Tinyclues
alias: /partners/tinyclues/
description: "This article outlines the partnership between Braze and Tinyclues, which offers an audience-building feature to help you send to more targeting campaigns, find new product opportunities, and elevate revenue using an incredibly user-friendly UI."
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
{: .reset-td-br-1 .reset-td-br-2}

## Integration

To integrate Braze and Tinyclues, you must configure the Tinyclues platform, export an existing Tinyclues campaign, and create a user cohort segment in Braze that can be used to target users in future campaigns.

### Step 1: Get the Braze data import key

In Braze, navigate to **Technology Partners** and select **Tinyclues**. Here, you will find your REST Endpoint and generate your Braze data import key. Once generated, you can create a new key or invalidate an existing one.<br><br>![Tinyclues][6]{: style="max-width:90%;"} 

To complete the integration, you will need to provide the data import key and REST endpoint to your Tinyclues data operations team. Tinyclues will then establish the connection and reach out to you once the setup is complete.

### Step 2: Export a campaign from the Tinyclues platform

Each time you want to create a cohort of Tinyclues users to use in Braze, you'll have to first export it from the Tinyclues platform.

In Tinyclues, select the campaign(s) you want to export and click **Export Campaigns**. Upon export, the audience will be automatically uploaded to your Braze account.

![Tinyclues dashboard][1]

### Step 3: Create a segment from the Tinyclues custom audience

In Braze, navigate to **Segments**, name your Tinyclues cohort segment, and select **Tinyclues Cohorts** as your filter. From here, you can choose which Tinyclues cohort you wish to include. Once created, you can select your Tinyclues cohort segment as an audience filter when creating a campaign or Canvas.

![Tinyclues create segement][3]{: style="max-width:90%;"}<br><br>
![Tinyclues select cohort][4]{: style="max-width:90%;"}

Having trouble locating your cohort? Check out our [troubleshooting](#troubleshooting) section for guidance. 

## Using this integration

To use your Tinyclues segment, create a Braze campaign or Canvas and select the segment as your target audience. 

![Tinyclues audience][5]{: style="max-width:90%;"}

## Troubleshooting

Are you having trouble finding the right cohort within the list? In Tinyclues, view your campaign details and verify the name by checking the **Export File Name**.

![Tinyclues troubleshooting][2]{: style="max-width:30%;"}

Still having trouble retrieving your audience? Contact the [Tinyclues team](mailto:support@tinyclues.com) for additional support.

[1]: {% image_buster /assets/img/tinyclues/tinyclues_1.png %} 
[2]: {% image_buster /assets/img/tinyclues/tinyclues_2.png %} 
[3]: {% image_buster /assets/img/tinyclues/tinyclues_3.png %} 
[4]: {% image_buster /assets/img/tinyclues/tinyclues_4.png %}
[5]: {% image_buster /assets/img/tinyclues/tinyclues_5.png %}  
[6]: {% image_buster /assets/img/tinyclues/tinyclues_6.png %}  