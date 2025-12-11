---
nav_title: Creating a Journey in Salesforce Marketing Cloud
article_title: Creating a Journey in Salesforce Marketing Cloud for BrazeAI Decisioning Studio
page_order: 5
description: "Learn how to set up and integrate BrazeAI Decisioning Studio<sup>TM</sup> Go into Braze."
---

# Creating a Journey in Salesforce Marketing Cloud for BrazeAI Decisioning Studio

> Set up a Journey in Salesforce Marketing Cloud (SFMC) to begin triggering sends through BrazeAI Decisioning Studio™ Go.

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
5. Select **Done** to save the API event.

![]({% image_buster /assets/img/decisioning_studio_go/journey4.png %})

### Step 2.2: Add a Decision Split

1. Drag and drop a **Decision Split** after the **API Entry Event**. 
2. In the **Decision Split** details, select **Edit** for the first path.

![]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3. Update the **Decision Split** to use the template ID passed in by the recommendations data extension. Locate the appropriate field under **Journey Data**.

![]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. Select your entry event and locate the desired template ID field. drag it into the workspace to the right.

![]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. Enter the template ID of your first email template, then select **Done**.
6. Select **Summary** to save this path.
7. Add a path for each of your email templates, then repeat steps 4-6 above to set the filter criteria so that the template ID matches the ID value of each template.
8. Select **Done** to save the **Decision Split** node.

![]({% image_buster /assets/img/decisioning_studio_go/journey10.png %})

### Step 2.3: Add an Email for each Decision Split

1. Drag an **Email** node into each path of of the **Decision Split**.
2. Select **Email**, then select the appropriate template that should go in each Path (meaning the template with the ID value should match the logic in your Decision Split).

![]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

### Step 3: Activate the Journey

After setting up your Journey, activate it and share the following details with the BrazeAI Decisioning Studio™ Go team: 

* Journey ID
* Journey name
* API event definition key
* Recommendations data extension external key

{% alert note %}
The BrazeAI Decisioning Studio™ Go portal shows you the SFMC automation it provisioned to export the subscribers and engagement data once daily. If you open this automation in SFMC, make sure to unpause and turn it back to live.
{% endalert %}

1. In the BrazeAI Decisioning Studio™ Go portal, copy the **Journey name**.
2. Next, in Salesforce Marketing Cloud Journey Builder, paste the Journey name into the search bar.
3. Select the Journey name. Note that the Journey is currently in Draft status.
4. Select **Validate**.

![]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. Then, review the validation results and select **Activate**.

![]({% image_buster /assets/img/decisioning_studio_go/activate1.png %})

6. In the **Activate Journey** summary, select **Activate** again.

![]({% image_buster /assets/img/decisioning_studio_go/activate2.png %})

You're all set! You can now begin triggering sends through BrazeAI Decisioning Studio™ Go.
