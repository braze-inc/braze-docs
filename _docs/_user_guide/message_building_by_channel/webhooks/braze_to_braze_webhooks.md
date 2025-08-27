---
nav_title: Creating a braze-to-braze webhook
article_title: Creating a Braze-to-Braze Webhook
page_order: 3
channel:
  - webhooks
description: "This article covers how to create a Braze-to-Braze webhook for key use cases."

---

# Creating a Braze-to-Braze webhook

> You can use webhooks to communicate with the Braze [REST API]({{site.baseurl}}/api/basics/), essentially doing anything that our API allows you to do. We refer to this as a Braze-to-Braze webhook—a webhook that is communicating from Braze to Braze. The use cases on this page assume that you're familiar with [how webhooks work]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) and how to [create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) in Braze.

## Prerequisites

To create a Braze-to-Braze webhook, you'll need an [API key]({{site.baseurl}}/api/api_key/) with permissions for the endpoint you want to reach.

## Setting up your Braze-to-Braze webhook

While the specifics of your webhook request will vary from use case to use case, the general workflow for creating a Braze-to-Braze webhook stays the same.

1. [Create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) as a campaign or Canvas component. 
2. Choose **Blank Template**.
3. In the **Compose** tab, specify the **Webhook URL** and **Request Body** as noted for your use case.
4. In the **Settings** tab, specify your **HTTP Method** and **Request Headers** as noted for your use case.
5. Continue to build out the rest of your webhook as needed. Some use cases require specific delivery settings, such as triggering the campaign or Canvas from a custom event.

## Use cases

While there's a lot you can do with Braze-to-Braze webhooks, here are some use cases to get you started:

- Increment an integer custom attribute for a counter when a user receives a message.
- Trigger a second Canvas from an initial Canvas.

{% alert tip %}
Add a [User Update step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) to your Canvas to track a user's attributes, events, and purchases in a JSON composer. This way, these updates are batched so Braze can process them more efficiently than a Braze-to-Braze webhook.
{% endalert %}

### Use case: Increment an integer custom attribute for a counter

This use case involves creating a custom attribute and using Liquid to count the number of times a specific action has occurred. 

For example, you might want to count how many times a user has seen an active in-app message campaign and prevent them from receiving the campaign again after they've seen it three times. For more ideas on what you can do with Liquid logic in Braze, check out our [Liquid use case library]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases).

Follow the general steps for creating a Braze-to-Braze webhook, and refer to the following when configuring your webhook:

- **Webhook URL:** Your [REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) followed by `/users/track`. For example, for the `US-06` instance, the URL would be `https://rest.iad-06.braze.com/users/track`.
- **Request Body:** Raw Text

#### Request headers and method

Braze requires an HTTP header for authorization that includes your API key and another that declares your `content-type`.

- **Request Header:**
  - **Authorization:** Bearer {YOUR_API_KEY}
  - **Content-Type:** application/json
- **HTTP Method:** POST

Replace `YOUR_API_KEY` with a Braze API key with `users.track` permissions. You can create an API key within the Braze dashboard at **Settings** > **API Keys**.

![The request headers for the webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Request body

Add your user track request in the request body and the Liquid to assign a counter variable. For more details, refer to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

The following is an example of both the required Liquid and request body for this endpoint, where `your_attribute_count` is the attribute you're using to count how many times a user has seen a message:

{% raw %}
```json
{% assign new_number = {{custom_attribute.${your_attribute_count}}} | plus: 1 %}
{
    "attributes": [
        {
        "external_id": "{{${user_id}}}",
        "your_attribute_count": "{{new_number}}"
        }
    ]
}
```
{% endraw %}

{% alert note %}
Each time a custom attribute counter is updated (incremented or decremented) it will log a [data point]({{site.baseurl}}/user_guide/data/data_points/), which counts toward your overall consumption.
{% endalert %}

### Use case: Trigger a second Canvas from an initial Canvas

For this use case, you'll create two Canvases and use a webhook to trigger the second Canvas from the first Canvas. This acts like an entry trigger for when a user reaches a certain point in another Canvas.

1. Start by creating your second Canvas—the Canvas that should be triggered by your initial Canvas. 
2. For the Canvas **Entry Schedule**, select **API-Triggered**.
3. Make note of your **Canvas ID**. You'll need this in a later step.
4. Continue building out the steps of your second Canvas, then save the Canvas.
5. Finally, create your first Canvas. Find the step where you want to trigger the second Canvas and create a new step with a webhook. 

Refer to the following when configuring your webhook:

- **Webhook URL:** Your [REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) followed by `canvas/trigger/send`. For example, for the US-06 instance, the URL would be `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Request Body:** Raw Text

#### Request headers and method

Braze requires an HTTP header for authorization that includes your API key and another that declares your `content-type`.

- **Request Header:**
  - **Authorization:** Bearer `YOUR_API_KEY`
  - **Content-Type:** application/json
- **HTTP Method:** POST

Replace `YOUR_API_KEY` with a Braze API key with `canvas.trigger.send` permissions. You can create an API key within the Braze dashboard at **Settings** > **API Keys**.

![The request headers for the webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Request body

Add your `canvas/trigger/send` request in the text field. For more details, refer to [Sending Canvas messages via API-triggered delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). The following is an example of the request body for this endpoint, where `your_canvas_id` is the Canvas ID from your second Canvas: 

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

## Things to know

- Braze-to-Braze webhooks are subject to endpoint [rate limits]({{site.baseurl}}/api/api_limits/).
- Updates to the user profile will log additional [data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count), while triggering another message through the messaging endpoints will not.
- If you want to target [anonymous users]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), you can use `braze_id` instead of `external_id` in the request body of your webhook.
- You can save your Braze-to-Braze webhook as a [template]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) to be used again.
- You can check the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) to view and troubleshoot webhook failures.


