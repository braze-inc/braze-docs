---
nav_title: Oppizi
article_title: Oppizi 
alias: /partners/oppizi/
description: "This reference article outlines the partnership between Braze and Oppizi."
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/) is the global leader in offline marketing, providing a one-stop solution for businesses to run measurable, targeted direct mail and flyering campaigns.

_This integration is maintained by Oppizi._

## Prerequisites

| Requirement                    | Description                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Oppizi account                 | An active Oppizi account is required to use this integration.                 |
| Oppizi API key                 | Found in your Oppizi account in **Integrations** > **Braze**.                |
| Oppizi Direct Mail workflow ID | Create a workflow in Oppizi on the **Direct Mail Workflow** page to obtain an ID. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

With the Oppizi integration, you can:

* **Send automated direct mail postcards** using Braze triggers connected to Oppizi's webhook and direct mail workflows.
* **Configure thresholds, waves, and limits** in Oppizi direct mail workflows to control the sending of your campaigns.
* **Design professional postcards** with Oppizi’s built-in design tool—no design experience required.
* **Track campaign performance** in real time with Oppizi’s dashboard.

## Integration

### Step 1: Generate your Oppizi API key 

To use your webhook template in Braze, you'll first need to generate your Oppizi API key.

1. Log into Oppizi.
2. Go to **Integrations** > **Braze**.
3. Generate your API key.

You can manage, revoke, and create your keys from this page as needed.

### Step 2: Create a Braze webhook template

Next, create a webhook template for Oppizi in Braze to use in future campaigns or Canvases.

1. In Braze, go to **Templates** > **Webhook templates**.

In your webhook template, fill out the following fields:

- **Webhook URL:** ```https://webhooks.oppizi.com/events```
- **Request body:** **Raw Text**

For request method and headers, Oppizi requires an HTTP method along with the following HTTP headers to be included in the template. Fill out the following fields:

- **HTTP method:** POST
- **Request headers:**
  - **Authorization:** `Bearer <oppiziAPIKey>`
  - **Content-Type:** `application/json`

![An example of the Oppizi webhook header in Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

For the **Request Body**, you must include the field **oppiziWorkflowID**. This ID is generated when a workflow is created in Oppiz and is required to specify which direct mail workflow your recipients should be added to. Each direct mail workflow in Oppizi has a unique ID, so if you create an Oppizi webhook template in Braze, make sure to always update the workflow ID to the correct one.

{% alert note %}
Check that required custom attributes are set up in your Braze account for your recipients’ postal addresses, as these are necessary for sending direct mail.
{% endalert %}

![An example of a Oppizi webhook template in Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

The following is an example request body:

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### Step 3: Create a Direct Mail Workflow in Oppizi

1. In Oppizi, go to **Direct Mail Workflow** > **Create workflow**
2. Configure workflow details, including thresholds, waves, postcard format, and artwork.
3. In the webhook details section, you’ll find a ready-to-use request body, including your workflow ID, that you can paste directly into Braze.

### Step 4: Preview and test your request in Braze

After adding your request body with Oppizi’s workflow ID, run a test to confirm your setup is working as expected.

To run the test, update `requestType` from `live` to `test` in the request body. Note this step is crucial to prevent adding test recipients to your direct mail audience.

After you finish testing, update `requestType` back to `live` and save your Canvas. Now, you’re ready to launch your automated direct mail campaigns.
