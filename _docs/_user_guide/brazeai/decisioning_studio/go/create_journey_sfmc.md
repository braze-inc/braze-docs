---
nav_title: Setting up SFMC data query automation
article_title: Setting up SFMC data query automation for BrazeAI Decisioning Studio
page_order: 2
description: "Learn how to set up and integrate BrazeAI Decisioning Studio<sup>TM</sup> Go into Braze."
---

# Creating a Journey in Salesforce Marketing Cloud

> Set up a Journey in Salesforce Marketing Cloud to begin triggering sends through BrazeAI Decisioning Studio™ Go.

## Step 1: Set up the Journey

1. In Salesforce Marketing Cloud, go to **Journey Builder** > **Journey Builder**.
2. Select **Create New Journey**.
3. For your journey type, select **Multi-Step Journey**, then select **Create**.

![]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

## Step 2: Build the Journey

### Step 2.1: Create an entry source

1. For your entry source, drag **API Event** to the Journey Builder.

![]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

2. In the **API Event**, select **Create an event**.

![]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3. Select **Select Data Extension**. Locate and select the data extension that BrazeAI Decisioning Studio™ Go will be writing recommendations to.
4. Select **Summary** to save your changes.
5. Select **Done** to save the API Event.

![]({% image_buster /assets/img/decisioning_studio_go/journey4.png %})

### Step 2.2: Add a Decision Split




When finished, activate your Journey and ensure that you share the below with the OfferFit team.
* Journey ID
* Journey Name
* API Event Definition Key
* Recommendations Data Extension External Key

### Step 3: Activate the Journey

{% alert note %}
The BrazeAI Decisioning Studio™ Go portal shows you the SFMC automation it provisioned to export the subscribers and engagement data once daily. If you open this automation in SFMC, make sure to unpause and turn it back to live.
{% endalert %}

1. In the BrazeAI Decisioning Studio™ Go portal, copy the **Journey name**.
2. Next, in Salesforce Marketing Cloud Journey Builder, paste the Journey name into the search bar.
3. Select the Journey name. Note that the Journey is currently in Draft status.
4. Select **Validate** > **Activate**.

6. In the **Activate Journey** summary, select **Activate** again.




You're all set! You can now begin triggering sends through BrazeAI Decisioning Studio™ Go.