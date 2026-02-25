---
nav_title: Create a Braze-to-Braze webhook
article_title: Create a Braze-to-Braze Webhook
page_order: 3
channel:
  - webhooks
description: "This reference article covers when to use User Update versus Braze-to-Braze webhooks and how to create a Braze-to-Braze webhook."

---

# Create a Braze-to-Braze webhook

> Braze-to-Braze webhooks let you call the [Braze REST API]({{site.baseurl}}/api/basics/) from within Braze using a [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) in a [Campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) or [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/). Use this for orchestration tasks like triggering an [API-triggered Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). For updating [User attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [Custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/), or [Purchases]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) from Canvas, use [User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) instead. It's designed for user profile changes and processes updates more efficiently.

To get the most out of this article, you should be familiar with [how webhooks work]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) and how to [create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) in Braze.

## Use User Update for user data changes

To update user profiles from within a Canvas, including modifying [Custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), recording [Custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/), or recording [Purchases]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), use [User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) instead of a Braze-to-Braze webhook. 

User Update groups multiple changes together and sends them in batches, making it faster than webhooks. It's easier to set up than a webhook and supports complex updates through its [Advanced JSON composer]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer). For example, to count how many times a user has seen a message, use User Update's [Increment and decrement feature]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#increasing-and-decreasing-values) rather than a Braze-to-Braze webhook.

{% alert tip %}
Add [User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) to your Canvas to update a user's attributes, events, and purchases using a JSON composer.
{% endalert %}

## When to use a Braze-to-Braze webhook

User Update can handle nearly all the same tasks as a Braze-to-Braze webhook for updating user profiles. For complex updates beyond simple custom attributes, you can use the [Advanced JSON composer]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer).

You can use a Braze-to-Braze webhook when you need to call Braze's [REST API]({{site.baseurl}}/api/basics/) from within Braze for scenarios other than direct user updates from Canvas steps. Common examples include:

- Triggering an [API-triggered Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) from another Canvas
- Calling other [Messaging endpoints]({{site.baseurl}}/api/endpoints/messaging/) for orchestration patterns where one workflow in Braze needs to invoke an API that doesn't have a dedicated Canvas component

For user updates inside Canvas, the recommended method is to use [User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/).

## Prerequisites

To create a Braze-to-Braze webhook, you need an [API key]({{site.baseurl}}/api/api_key/) with permissions for the endpoint you want to reach. For example, to trigger an API-triggered Canvas, you need an API key with the `canvas.trigger.send` permission.

## Setting up your Braze-to-Braze webhook

The general workflow for creating a Braze-to-Braze webhook follows these steps:

1. [Create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) as a campaign or Canvas component. 
2. Choose **Blank Template**.
3. In the **Compose** tab, specify the **Webhook URL** and **Request Body** for your API use case.
4. In the **Settings** tab, specify your **HTTP Method** and **Request Headers** as required by the endpoint.
5. Configure any additional delivery settings (for example, triggering from a custom event) and build out the rest of your campaign or Canvas.

## Trigger a second Canvas from an initial Canvas

In this use case, you create two Canvases and use a Braze-to-Braze webhook to trigger the second Canvas from the first. This acts like an entry trigger for when a user reaches a certain point in another Canvas.

1. Start by creating your second Canvas—the Canvas that should be triggered by your initial Canvas.
2. For the Canvas **Entry Schedule**, select **API-Triggered**.
3. Make note of your **Canvas ID**. You need this in a later step.
4. Continue building out the steps of your second Canvas, then save the Canvas.
5. Finally, create your first Canvas. Find the step where you want to trigger the second Canvas and create a new step with a webhook.

Refer to the following when configuring your webhook:

- **Webhook URL:** Your [REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) followed by `/canvas/trigger/send`. For example, for the `US-06` instance, the URL would be `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Request Body:** Raw Text

#### Request headers and method

Braze requires an HTTP header for authorization that includes your API key and another that declares your content type.

- **Request Headers:**
  - **Authorization:** `Bearer YOUR_API_KEY`
  - **Content-Type:** `application/json`
- **HTTP Method:** `POST`

Replace `YOUR_API_KEY` with a Braze API key that has `canvas.trigger.send` permissions. You can create an API key in the Braze dashboard by going to **Settings** > **API Keys**.

![Request headers for the webhook showing Authorization and Content-Type fields in the Braze dashboard.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Request body

Add your `/canvas/trigger/send` request in the text field. For details, see [Sending Canvas messages via API-triggered delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). The following is an example of the request body for this endpoint, where `your_canvas_id` is the Canvas ID from your second Canvas:

{% raw %}
```json
{
  "canvas_id": "your_canvas_id",
  "recipients": [
    {
      "external_user_id": "{{${user_id}}}"
    }
  ]
}
```
{% endraw %}

When a user reaches this webhook step in the first Canvas, Braze triggers the second Canvas for that user via the API.

## Considerations

- **User updates:** For updating user profiles from Canvas (attributes, events, purchases), use [User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) instead of Braze-to-Braze webhooks for better efficiency and cost-effectiveness.
- Braze-to-Braze webhooks are subject to endpoint [Rate limits]({{site.baseurl}}/api/api_limits/).
- Updates to the user profile incur [Data points]({{site.baseurl}}/user_guide/data/data_points/) that count toward your overall consumption, while triggering another message through the messaging endpoints does not.
- To target [Anonymous users]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), use `braze_id` instead of `external_id` in the request body of your webhook.
- You can save your Braze-to-Braze webhook as a [webhook template]({{site.baseurl}}/user_guide/messaging/content/templates/webhook_templates/) for reuse.
- You can check the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) to view and troubleshoot webhook failures.


