---
nav_title: Configure with Klaviyo
article_title: Configure with Klaviyo for BrazeAI Decisioning Studio
page_order: 3
description: "Learn how to set up a Klaviyo Flow for use with BrazeAI Decisioning Studio<sup>TM</sup> Go."
toc_headers: h2
---

# Configure with Klaviyo for BrazeAI Decisioning Studio™ Go

> Set up a placeholder template and a flow in Klaviyo to trigger activations through BrazeAI Decisioning Studio™ Go.

{% alert important %}
You must create a new flow in Klaviyo for every new experimenter you set up. If you previously created a placeholder flow to import your templates, you must create a new flow and cannot reuse the previous placeholder flow.
{% endalert %}

Before creating a flow in Klaviyo, you must have the following details from your BrazeAI Decisioning Studio™ Go portal to reference:

- Flow name
- Trigger event name

## Creating a placeholder template in Klaviyo

BrazeAI Decisioning Studio™ Go imports templates that are associated with existing flows in your Klaviyo account. To use a template that isn't associated with any flows, you can create a placeholder flow containing the templates you'd like to use. The flow can be left as a draft; it doesn't need to be live.

## Step 1: Set up your flow

{% alert note %}
The purpose of this placeholder flows is to import your desired content into BrazeAI Decisioning Studio™ Go. You must create a separate flow at a later step, which BrazeAI Decisioning Studio™ Go uses to trigger activations once your Experimenter is live.
{% endalert %}

1. In Klaviyo, select **Flows**. 
2. Select **Create flow** > **Create From Scratch**.
3. Give the placeholder Flow a name you'll recognize, then select **Create Flow**.

![A Flow named "OFE Placeholder Flow".]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4. Select any trigger, then save the flow. 
5. Select **Confirm and save**. 

## Step 2: Create the placeholder template

Next, create the placeholder template: 

1. Drag and drop an **Email** node after the **Trigger**.

![A Flow with a Trigger node followed by an Email node.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2. In the **Email** node, select **Select template**.
3. Then, choose the template to use and select **Use template**.
4. Select **Save** > **Done**.
5. (Optional) To add more templates to be used in BrazeAI Decisioning Studio™ Go, add another **Email** node and repeat steps 2–4. 
6. Leave all emails in **Draft** mode and exit the Flow.

In the BrazeAI Decisioning Studio™ Go portal, your templates should be selectable under your placeholder flow.

![An example of a placeholder Klaviyo template in the Decisioning Studio Go portal.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

## Creating a flow in Klaviyo

### Step 1: Set up the flow

1. In Klaviyo, select **Flows** > **Create flow**.
2. Select **Build your own**.
3. For **Name**, enter the flow name from your BrazeAI Decisioning Studio™ Go portal. Then, select **Create manually**.

![]({% image_buster /assets/img/decisioning_studio_go/flow1.png %})

{: start="4"}
4. Select the trigger.
5. Match the metric name to the trigger event name from your BrazeAI Decisioning Studio™ Go portal.

![]({% image_buster /assets/img/decisioning_studio_go/flow2.png %})

{: start="6"}
6. Select **Save**.

{% alert note %}
If your Experimenter has one base template, proceed to the following steps. If your Experimenter has two or more base templates, skip to [Step 3: Add a trigger split to your flow](#step-3-add-a-trigger-split-to-your-flow).
{% endalert %}

### Step 2: Add an email to your flow 

1. Drag and drop an **Email** node after the **Trigger** node.
2. In the **Email details**, select **Select template**.

![]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3. Find and select your base template. You can search for your template by the template name in the **Resources to use** section of the BrazeAI Decisioning Studio™ Go portal.

![]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4. Select **Use template** > **Save**.
5. For the **Subject line**,  enter {% raw %}`{{event.SubjectLine}}`{% endraw %}.
6. For **Sender name** and **Sender email address**, enter the details you'd like to use.

![]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7. Select **Done**.
8. Unselect the **Skip recently emailed profiles** checkbox, then select **Save**.
9. In the email node, update the mode from **Draft** to **Live**.

![]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

You're all set! You can now trigger activations through BrazeAI Decisioning Studio™ Go. 

### Step 3: Add a trigger split to your flow 

1. Drag and drop a **Trigger split** node after the **Trigger node**.
2. Select the **Trigger split** node and set the **Dimension** to **EmailTemplateID**.

![]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

#### Step 3.1: Add your email template

1. In the BrazeAI Decisioning Studio™ Go portal, find the **Email Template ID** for your first template under the **Resources to use** section. Enter the **Email Template ID** for the **Dimension** field, then select **Save**.
2. Drag and drop an **Email** node to the **Yes** branch of the **Trigger split**. 

![]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3. In the **Email details**, select **Select template**.
4. Find and select your base template. You can search for your template by the base template name in the **Resources to use** section of the BrazeAI Decisioning Studio™ Go portal.
5. Select **Use template** > **Save**.
6. For the **Subject line**,  enter {% raw %}`{{event.SubjectLine}}`{% endraw %}.
7. For **Sender name** and **Sender email address**, enter the details you'd like to use.

![]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8. Select **Done**.
9. Unselect the **Skip recently emailed profiles** checkbox, then select **Save**.
10. In the email node, update the mode from **Draft** to **Live**.

#### Step 3.2: Add a new trigger split

Next, create a new **Trigger split** and **Email** node for each additional base template your Experimenter will use. 

1. Drag and drop another **Trigger split** node into the **No** branch of the previous **Trigger split** node.
2. Set the **Dimension** to **EmailTemplateID** and fill in the **Dimension** value with the **Email Template ID** of the base template you're setting up.
3. Select **Save**.

![]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4. Drag and drop an **Email** node in the **Yes** branch of your new trigger split.
5. Repeat steps 1-5 in [Step 3.1](#step-31-add-your-email-template) to select the corresponding template.
5. Set the **Subject line** to {% raw %}`{{event.SubjectLine}}`{% endraw %}, and uncheck the **Skip recently emailed profiles** checkbox.
6. Repeat this process until you have one **Trigger split** node and one **Email** node for each base template your Experimenter is using. Your last Trigger split should have nothing in the "No" branch.

![]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="7"}
7. In each of your **Email** nodes, update the mode from **Draft** to **Live**.

![]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

You're all set! You can now trigger activations through BrazeAI Decisioning Studio™ Go. 