---
nav_title: Creating a placeholder Klaviyo Flow 
article_title: Creating a placeholder Klaviyo Flow for BrazeAI Decisioning Studio Go
page_order: 3
description: "."
---

# Creating placeholder Klaviyo Flow for your templates

> BrazeAI Decisioning Studio™ Go imports templates that are associated with existing Flows in your Klaviyo account. To use a template that isn't associated with any Flows, you can create a placeholder Flow containing the templates you'd like to use. The Flow can be left as a draft; it doesn't need to be live.

## Step 1: Set up your Flow

{% alert note %}
The purpose of this placeholder Flow is to import your desired content into BrazeAI Decisioning Studio™ Go. You must create a separate Flow at a later step, which BrazeAI Decisioning Studio™ Go uses to trigger activations once your Experimenter is live.
{% endalert %}

1. In Klaviyo, select **Flows**. 
2. Select **Create flow** > **Create From Scratch**.
3. Give the placeholder Flow a name you'll recognize, then select **Create Flow**.

![A Flow named "OFE Placeholder Flow".]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4. Select any trigger, then save the Flow. 
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

In the BrazeAI Decisioning Studio™ Go portal, your templates should be selectable under your placeholder Flow.

![An example of a placeholder Klaviyo template in the Decisioning Studio Go portal.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})