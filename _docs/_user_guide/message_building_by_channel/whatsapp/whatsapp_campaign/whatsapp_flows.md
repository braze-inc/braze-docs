---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 1
description: "This reference article covers the steps involved in building out and creating a WhatsApp Flows message."
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> WhatsApp Flows is an enhancement to the existing WhatsApp channel, allowing you to create interactive and dynamic messaging experiences. This page provides step-by-step instructions for participating in the Early Access program and using WhatsApp Flows.

## Setting up WhatsApp Flows

1. Log into your Meta account.
2. Create Flows from one of two main locations:
    - **Account tools:** Go to the **Flows** tab to view the Flow ID and create a new Flow.
    - **Manage templates:** This is the recommended method for creating Flows. Here, you can generate templates and select a Flow option during the template creation process.

![WhatsApp Manager with a page to create a Flows template.]()

{: start="3"}  
3. Choose your Flow creation method:
    3.1 Select an existing Flow or create one.
    3.2 If creating a Flow, choose from two options:
        - **Custom Form:** For specific requirements.
        - **Pre-designed Elements:** For quicker setup.

## Configuring WhatsApp Flow messages and responses

1. In a Braze Canvas, create a WhatsApp message step that uses the template message containing the Flow you created.
2. Continue creating your template. If necessary, add media, variable content, or both to your message. Your Flow selection is chosen when the template was made, so additional information for the flow experience is not required.

![WhatsApp message composer using a WhastApp Flow template.]()

{% alert important %}
Flow preview is not yet available in the early access, but you can preview the Flow by sending yourself a test message with the flow button. 
{% endalert %}

### Saving the Flow response

You can save the user's full response or specific parts of the Flow response.

#### Step 1: Create an Action Path

Create an [Action Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) with **Send a WhatsApp inbound message** trigger to process the Flow information.

{% alert note %}
You'll be able to specify the flow when additional features are released during the early access. 
{% endalert %}

#### Step 2: Create an inbound Flow response

When composing your WhatsApp message, select the plus icon to open the **Add Personalization** window, then select **WhatsApp Properties** for the personalization type and **inbound_flow_response** for the custom attribute. This will save information to user profiles or forward it to other services, like Webhooks.

![WhatsApp message composer with an "Add Personalization" component to insert a WhatsApp properties personalization with the custom attribute `inbound_flow_response`.]()

#### Step 3: Save the full Flow response

You can use the advanced JSON editor to save attributes from the Flow response to custom attributes, or use a multi-step Canvas to save the response to a nested custom attribute. 

##### Advanced JSON editor

In the advanced JSON editor, enter `{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`, where “flow_1” is the custom attribute you’d like the flow to be saved to.

![User Update step with an Advanced JSON editor.]()

##### UI editor

1. Confirm that you have already created an `inbound_flow_response` custom attribute with the object data type inside of your workspace data settings.
2. In the UI editor, use the Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}``` to populate the custom attribute and save the entire user’s flow response to it. You need to populate the Key Value as ```{{whats_app.${inbound_flow_response}}}```{% endraw %} before selecting the custom attribute you created.

![User Update step that uses the UI editor.]()

After Braze recieves a Flow response, we will save the nested custom attribute with the prescribed naming to the user profile. That custom attribute can be pulled when building Canvases. 

![A window displaying the contents of a "flow_1" custom attribute.]()

#### (Optional) Step 4: Save specific field Flow responses to a specific custom attribute 

To save specific parts of the user's Flow response, the generic User Update step that saves the entire Flow response to a custom attribute (in Step 3) must be deployed and populated. To do this, test the Canvas and launch it to complete a Flow response. 

The User Update step must always precede subsequent Canvas steps that want to use the new nested custom attribute.

1. Create a subsequent User Update step that uses the UI editor.
2. Similar to Step 2, select **Add Personalization**, but this time, select **Nested Custom Attribute** and the corresponding top-level attribute where the Flow is stored.  

![User Update step with a Nested Custom Attributes personalization.]()

{: start="3" }
3. Select the key attribute you’d like to save elsewhere and insert the Liquid into the **Key Value** field.

![Window for "flow_1" with attributes to select from]()

{: start="4" }
4. Choose the attribute where you want to store it.
5. (optional) Use the `parse_json` Liquid helper to extract specific responses from the flow. For example, you can pull out the Flow token and selected options to customize a follow-up message.

{% raw %}
```liquid
Received your flow response 
{{whats_app.${inbound_flow_response}}}
{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}

Flow Token: {{ parsed_json.flow_token }}
Selected Options: {{ parsed_json.screen_0_Choose_all_that_apply_0 }}
```
{% endraw %}

{% alert note %}
A new WhatsApp message “clears” the Canvas’s ability to use (and reuse) the Liquid Flow response, so make sure that follow up messages are after all User Update steps, webhooks, or other steps that use the Liquid Flow response. 
{% endalert %}

#### Step 5: Test your WhatsApp Flow

Send a test message to confirm how your test behaves.

## Future enhancements

Additional Flow functionalities will be introduced, including advanced action step filters and response messages that incorporate Flow elements.

For any questions or further assistance, contact [Support]({{site.baseurl}}/braze_support/).