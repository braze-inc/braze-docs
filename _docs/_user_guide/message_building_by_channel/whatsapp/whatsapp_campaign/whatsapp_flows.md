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

{% tabs local %}
{% tab Template message %}

1. In a Braze Canvas, create a WhatsApp message step that uses the template message containing the respective Flow.
2. Continue creating your template. If necessary, add media, variable content, or both to your message. Your Flow selection is chosen when the template was made, so additional information for the flow experience is not required.

![WhatsApp message composer using a WhatsApp Flow template.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. In a Braze Canvas, create a WhatsApp message step that uses a response message and flow message.

![A message step for a WhatsApp response message type and Flow message layout.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. Select the respective Flow, then continue creating your message. 

![A Flow message response composer with an extended dropdown for selecting a Flow.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Preview Flow

Before launching a Canvas with a Flow, you can select **Preview Flow** to preview the Flow directly in Braze to confirm it behaves as expected. You can also interact with the Flow in the preview to experience how a user would navigate the Flow, and then make real-time adjustments. If a Flow contains multiple pages, you can interact with each page.

![Preview window displaying a form for a user to finish sign up.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Saving the full Flow response {#full-flow}

When incorporating a WhatsApp Flow message into a Braze Canvas or campaign, you may want to capture and utilize specific information that users submit through the Flow. Braze needs to receive additional information regarding the structure of the user response, specifically the expected shape of the JSON response, to generate the required nested custom attribute (NCA) schema.

### Step 1: Generate the Flow custom attribute

{% tabs local %}
{% tab Recommended method %}

The simplest way to give Braze the information about the response structure is to save the Flow response as a custom attribute and complete a test send.

#### Using a Flow that hasn't been used in Braze

If you're using a Flow that hasn't been previously used within Braze, when viewing the **Flow Custom Attribute** section in the **Compose Messages**, you may not see any information. This means the schema hasn't been generated yet.

![Meta Flow section with an option to view the Flow custom attribute.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

To resolve this, do the following:

1. Complete setting up your WhatsApp message step.
2. Confirm you checked **Save Flow responses as a custom attribute**.

![Meta Flow section with a checkbox to save Flow responses as a custom attribute.]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3. Send yourself a test message and complete the Flow as a user.

Now, Braze has the shape of the Flow response JSON and can generate the custom attribute.

{% endtab %}
{% tab Alternative methods %}

Use the advanced JSON editor to save attributes from the Flow response to custom attributes, or use a multi-step Canvas to save the response to a nested custom attribute. 

{% subtabs %}
{% subtab Advanced JSON editor %}

In the advanced JSON editor, enter {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, where “flow_1” is the custom attribute you’d like the flow to be saved to.

![User Update step with an advanced JSON editor.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. Confirm that you have already created a custom attribute with the object data type ("flow_1" in this example) inside of your workspace data settings.
2. In the UI editor, use the Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}``` to populate the custom attribute and save the entire user’s Flow response to it. You need to populate the key value as ```{{whats_app.${inbound_flow_response}}}```{% endraw %} before selecting the custom attribute you created.

![User Update step that uses the UI editor.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

After Braze receives a Flow response, we will save the nested custom attribute with the prescribed naming to the user profile. That custom attribute can be pulled when building Canvases. 

![A window displaying the contents of a "flow_1" custom attribute.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Step 2: View the saved Flow response

When the Flow completes, Braze automatically creates a Flow custom attribute with a name based on the Flow ID. You can then go to the user profile to view the saved Flow response as a nested object in the **Custom Attributes** section.

After the schema generates, the Flow **Custom Attribute** section will display the expected structure, including the anticipated data types for each response (for example, "String" or "String Array").

![Flow custom attributes details window with schema dropdown.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Considerations

- **Existing attributes:** If a custom attribute for a particular Flow is already generated, the Flow will load with the attribute information available. In these cases, you don't need to send a test message to generate the schema, as Braze already recognizes the expected response messages.
- **Flow changes:** If you make any changes to the Flow after the schema generates, you must send an additional test message so Braze can understand that the shape of the Flow response has changed and adjust the attribute structure accordingly. This action is limited to once every 24 hours. 
- **Consistency:** The Flow custom attribute generated is consistent and will be the same attribute for this specific Flow, regardless the Canvas it's used in.
- **Manual option:** You aren't required to select the **Save Flow responses as a custom attribute** checkbox. You can manually generate the custom attribute by [saving specific fields from Flow responses to a specific custom attribute](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), which avoids duplicating user steps.

## Saving specific fields from Flow responses to a specific custom attribute 

### Step 1: Create an Action Path

Create an [Action Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) Canvas step or an action-based campaign. Select a **Send a WhatsApp inbound message** trigger and **Responded to Flow** condition, and then select the relevant Flow or **Any Flow**.

![A trigger for users who sent an inbound WhatsApp message and responded to any Flow.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Step 2: Extract fields from Flow responses

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

In the UI editor, select the following: 

- **Attribute Name:** YOUR_CUSTOM_ATTRIBUTE (in this example: “First_name”)
- **Action:** Update
- **Key Value:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![WhatsApp message composer with an "Add Personalization" component to insert a WhatsApp properties personalization with the custom attribute `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

When you’re ready, send a test message to test the Flow. Then, launch the Canvas!

{% endtab %}
{% endtabs %}

{% alert note %}
A new WhatsApp message “clears” the Canvas’s ability to use (and reuse) the Liquid Flow response, so make sure that follow-up messages are after all User Update steps, webhooks, or other steps that use the Liquid Flow response. 
{% endalert %}

## Adding a Flow personalization tag

To use the Flow response through Liquid with [supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), complete the following steps:

1. When composing your WhatsApp message, select the plus icon to open the **Add Personalization** window
2. Select **WhatsApp Properties** for the personalization type and **inbound_flow_response** for the custom attribute. This can be used to save information to user profiles, include it in messages, or forward it to other services, like webhooks.

![WhatsApp message composer with an "Add Personalization" component to insert a WhatsApp properties personalization with the custom attribute inbound_flow_response.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

For any questions or further assistance, contact [Support]({{site.baseurl}}/braze_support/).