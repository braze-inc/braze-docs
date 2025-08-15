---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 1
description: "This reference article covers the steps involved in building out and creating a WhatsApp Flows message."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flows is an enhancement to the existing WhatsApp channel, allowing you to create interactive and dynamic messaging experiences. This page provides step-by-step instructions for participating in the Early Access program and using WhatsApp Flows.

## Setting up WhatsApp Flows

1. Log in to your Meta account.
2. Create Flows from one of two main locations:
    - **Account tools:** Go to the **Flows** tab to view the Flow ID and create a new Flow.
    - **Manage templates:** This is the recommended method for creating Flows. Here, you can generate templates and select a Flow option during the template creation process.

![WhatsApp Manager with a page to create a Flows template.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3. Select an existing Flow or create one. If creating a Flow, choose from two options:
  - **Custom Form:** For specific requirements
  - **Pre-designed Elements:** For quicker setup

## Configuring WhatsApp Flow messages and responses

1. In a Braze Canvas, create a WhatsApp message step that uses the template message containing the Flow you created.
2. Continue creating your template. If necessary, add media, variable content, or both to your message. Your Flow selection is chosen when the template was made, so additional information for the flow experience is not required.

![WhatsApp message composer using a WhatsApp Flow template.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% alert important %}
Flow preview is not yet available in the early access, but you can preview the Flow by sending yourself a test message. 
{% endalert %}

## Saving the full Flow response {#full-flow}

### Step 1: Create an Action Path

Create an [Action Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) with **Send a WhatsApp inbound message** trigger to process the Flow information.

{% alert note %}
You'll be able to specify the Flow when additional features are released during early access. 
{% endalert %}

### Step 2: Compose your WhatsApp message

When composing your WhatsApp message, select the plus icon to open the **Add Personalization** window, then select **WhatsApp Properties** for the personalization type and **inbound_flow_response** for the custom attribute. This will save information to user profiles or forward it to other services, like webhooks.

![WhatsApp message composer with an "Add Personalization" component to insert a WhatsApp properties personalization with the custom attribute `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:60%;"}

### Step 3: Save the full Flow response

You can use the advanced JSON editor to save attributes from the Flow response to custom attributes, or use a multi-step Canvas to save the response to a nested custom attribute. 

{% tabs %}
{% tab Advanced JSON editor %}

In the advanced JSON editor, enter {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, where “flow_1” is the custom attribute you’d like the flow to be saved to.

![User Update step with an advanced JSON editor.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endtab %}
{% tab UI editor %}

1. Confirm that you have already created a custom attribute with the object data type ("flow_1" in this example) inside of your workspace data settings.
2. In the UI editor, use the Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}``` to populate the custom attribute and save the entire user’s Flow response to it. You need to populate the key value as ```{{whats_app.${inbound_flow_response}}}```{% endraw %} before selecting the custom attribute you created.

![User Update step that uses the UI editor.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

After Braze receives a Flow response, we will save the nested custom attribute with the prescribed naming to the user profile. That custom attribute can be pulled when building Canvases. 

![A window displaying the contents of a "flow_1" custom attribute.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endtab %}
{% endtabs %}

When you’re ready, send a test message to test the Flow. Then, launch the Canvas!

## Saving specific fields from Flow responses to a specific custom attribute 

You can use nested custom attributes or the `json_parse` Liquid tag to extract specific fields from Flow responses.

{% tabs %}
{% tab Nested custom attributes %}

To save specific parts of the user's Flow response, complete all the steps in [Saving the full Flow response](#full-flow), **including launching the Canvas**. The Canvas must be launched to create the nested custom attribute that you will reference. After launching the Canvas and completing a Flow, do the following steps:

1. Create a subsequent User Update step that uses the UI editor.
2. Select **Add Personalization**, then select **Nested Custom Attribute** and the corresponding top-level attribute where the Flow is stored.  

![User Update step with a Nested Custom Attributes personalization.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3. Select the key attribute you’d like to save and insert the Liquid into the **Key Value** field.

![Window for "flow_1" with attributes to select from.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4. Choose the attribute where you want to store it.
5. Send a test message to test the Flow.

{% endtab %}
{% tab Parse function %}

Use the `json_parse` Liquid tag to extract specific responses from the flow. For example, you can pull out the Flow token and selected options to customize a follow-up message.

### Step 1: Create an Action Path

Create an [Action Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) with **Send a WhatsApp inbound message** trigger to process the Flow information.

{% alert note %}
You'll be able to specify the Flow when additional features are released during early access. 
{% endalert %}

### Step 2: Compose your WhatsApp message

When composing your WhatsApp message, select the plus icon to open the **Add Personalization** window, then select **WhatsApp Properties** for the personalization type and **inbound_flow_response** for the custom attribute. This will save information to user profiles or forward it to other services, like webhooks.

### Step 3: Save specific fields from the Flow response

In the UI editor, select the following: 

- **Attribute Name:** YOUR_CUSTOM_ATTRIBUTE (in this example: “First_name”)
- **Action:** Update
- **Key Value:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![WhatsApp message composer with an "Add Personalization" component to insert a WhatsApp properties personalization with the custom attribute `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

{% alert note %}
A new WhatsApp message “clears” the Canvas’s ability to use (and reuse) the Liquid Flow response, so make sure that follow-up messages are after all User Update steps, webhooks, or other steps that use the Liquid Flow response. 
{% endalert %}

When you’re ready, send a test message to test the Flow. Then, launch the Canvas!

{% endtab %}
{% endtabs %}

{% alert note %}
Additional Flow functionalities will be introduced, including advanced action step filters and response messages that incorporate Flow elements.
{% endalert %}

For any questions or further assistance, contact [Support]({{site.baseurl}}/braze_support/).