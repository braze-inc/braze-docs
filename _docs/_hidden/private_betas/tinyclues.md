---
nav_title: Tinyclues
permalink: /partners/tinyclues/
description: "This article outlines the partnership between Braze and Tinyclues, which offers an audience-building feature to help you send to more targeting campaigns, find new product opportunities, and elevate revenue using an incredibly user-friendly UI."
page_type: partner
hidden: true

---

# Tinyclues

> [Tinyclues](https://www.tinyclues.com/) is an audience-building feature that offers the capability to increase the number of campaigns and revenue without harming customer experience and analytics to track the performance of CRM campaigns both online and offline.

Together, the Braze and Tinyclues integration offers users a path to better CRM planning and strategy, allowing users to send more targeting campaigns, find new product opportunities, and elevate revenue using an incredibly user-friendly UI.

## Overview

To integrate Braze and Tinyclues, you must export an existing Tinyclues campaign and create a user cohort segment in the Braze platform to filter future campaigns.

1. Configure the Tinyclues platform with the appropriate settings.
2. Each time a campaign is executed on Tinyclues Action, the associated audience is automatically pushed to Braze.
3. On the Braze platform, create a segment of the Tinyclues campaign users.
3. Create a Braze campaign and use the dedicated audience filtering option to target Tinyclues users.

## Integration Requirements
- An active Tinyclues account
- An active Braze account with the ability to use Tinyclues integration.
- The API key corresponding to Tincylues' integration must be communicated to your Tinyclues Data Operation representative to set up the integration.

## Implementation Process

### Step 1: Get the Braze Data Import Key
In your Braze account, navigate to __Technology Partners__ and select __Tinyclues__. Here, you will find your REST Endpoint and generate your Braze data import key. 

### Step 2: Share API Key with TinyClues Data Operations

You will need to provide the data import key and your REST endpoint to the Tinyclues Data Operations Team for the integration to be complete. Tinyclues will then establish the connection and reach out to you once the setup is complete. 

### Step 3: Export a Campaign from the Tinyclues Platform
Each time you want to activate a given campaign through Braze, you'll have to first export it from the Tinyclues platform.

On the Tinyclues platform, select the campaign(s) you want to export and click on __Export__.

![Tinyclues][1]

Upon export, the audience will be automatically uploaded to your Braze account.

### Step 4: Use TinyClue Custom Audience in Braze

Next on the Braze platform, navigate to __Segments__ and select __Tinyclues Cohorts__ as your filter. From here, you can choose which Tinyclues audience cohort you wish to include. Once created, you will be able to select your Tinyclues Cohort Segment as an audience filter.

Having trouble locating your cohort? Check out our [troubleshooting](#troubleshooting) section for guidance. 

![Tinyclues][3]{: style="max-width:70%;"}
![Tinyclues][4]{: style="max-width:70%;"}

### Step 5: Retrieve your Audience in Braze

On the Braze platform, create a campaign and use the dedicated audience filtering option to target your Tinyclues users. Select the specific Tinyclues Cohort Segment that corresponds to your exported Tinyclues campaign and begin your Braze campaign.

## Troubleshooting
Are you having trouble finding the right cohort within the list? Verify the name in Tinyclues UI by clicking on the campaign and checking the "Export File Name".

![Tinyclues][2]{: style="max-width:30%;"}

Still having trouble retrieving your audience, contact the Tinyclues Team for additional support: support@tinyclues.com.

[1]: {% image_buster /assets/img/tinyclues/tinyclues_1.png %} 
[2]: {% image_buster /assets/img/tinyclues/tinyclues_2.png %} 
[3]: {% image_buster /assets/img/tinyclues/tiny_clues3.png %} 
[4]: {% image_buster /assets/img/tinyclues/tiny_clues4.png %} 