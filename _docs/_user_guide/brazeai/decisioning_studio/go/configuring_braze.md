---
nav_title: Configuring with Braze
article_title: Configuring with Braze
page_order: 1
description: "Learn how to set up and integrate BrazeAI Decisioning Studio<sup>TM</sup> Go into Braze."
---

# Configuring with Braze

> Create an API campaign in Braze designed for BrazeAI Decisioning Studio™ Go.

## Step 1: Create your campaign 

1. In the Braze dashboard, go to **Messaging** > **Campaigns**.
2. Select **Create campaign**.
3. For your campaign type, select **API campaign**.
4. Enter a name for your campaign. An example is "Decisioning Studio Go Email".

![An API campaign named "Decisioning Studio Go Email".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5. For your messaging channel, select **Email**.

![Option to select your messaging channel for API campaign.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6. In **Additional Options**, select the **Allow users to become re-eligible to receive campaign** checkbox.
7. For the time to become re-eligible, enter **1** and select **Hours** from the dropdown.

![Re-eligibility for the API campaign selected.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8. Select **Save Campaign**.

## Step 2: Copy and paste your campaign ID

In your API campaign, copy the **Campaign ID**. Then, go to the BrazeAI Decisioning Studio™ Go portal and paste the **Campaign ID**.

![An example message variation ID to be copy and pasted.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

## Step 3: Copy and paste your message variation ID

In your API campaign, copy the **Message Variation ID**. Then, go to the BrazeAI Decisioning Studio™ Go portal and paste the **Message Variation ID**.
