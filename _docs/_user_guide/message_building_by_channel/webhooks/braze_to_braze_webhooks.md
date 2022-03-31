---
nav_title: Braze to Braze Webhooks
article_title: Braze to Braze Webhooks
page_order: 3
channel:
  - webhooks
description: "This article covers how to create a Braze to Braze webhook for key use cases."

---

# Braze to Braze webhooks

> This article covers how to create a Braze to Braze webhook for key use cases.

You can use webhooks to communicate with the Braze [REST API][2], essentially doing anything that our API allows you to do. We refer to this as a Braze to Braze webhook—a webhook that is communicating from Braze to Braze. 

## Prerequisites

To create a Braze to Braze webhook, you'll need an [API key][3] with permissions for the endpoint you want to reach. For example, if you're using the User track endpoint, you'll need an API key with `users.track` permissions.

## Use cases

While there's a lot you can do with Braze to Braze webhooks, here are some common use cases to get you started:

- Write or update custom attributes on a user profile.
- Reference an event property throughout a Canvas by storing the event property on the user profile as an attribute.
- Increment an integer custom attribute for a counter when a user receives a message.
- Trigger a second Canvas from an initial Canvas.

The example use cases on this page assume that you're already familiar with [how webhooks work][4] and how to [create a webhook][5] in Braze.

## Steps for creating a Braze to Braze webhook

While the specifics of your webhook request will vary from use case to use case, the general workflow for creating a Braze to Braze webhook stays the same.

1. [Create a webhook][5] as a campaign or Canvas step. 
2. Choose **Blank Template**.
3. In the **Compose** tab, specify the **Webhook URL** and **Request Body** as noted for your use case.
4. In the **Settings** tab, specify your **HTTP Method** and **Request Headers** as noted for your use case.
5. Continue to build out the rest of your webhook as needed. Note that some use cases require specific delivery settings, such as triggering the campaign or Canvas off of a custom event.

### Use case: Add an event or attribute to a user's profile

With this use case, you can update a user's profile with an event, event property, or attribute as part of a campaign or Canvas. For example, a B2C website may add an attribute of `purchase_lapsers=true` to a user's profile if they don't convert from an abandoned cart campaign or Canvas to allow those users to be retargeted with subsequent messaging.

Another common use case is a workaround to make event properties persist throughout a Canvas, rather than just the first step. This involves adding an event property as a custom attribute so that you can reference that event property throughout a Canvas. Note that [Canvas persistent entry properties][6] solves for this issue, and is currently in beta. Reach out to your Braze account manager for more information.

{% alert important %}
In order to reference an event property throughout a Canvas, you need to add the event property to the user profile as an attribute in the first step of the Canvas. Additionally, the Canvas itself must be triggered off of that event.
{% endalert %}

Follow the general steps for creating a Braze to Braze webhook, and refer to the following when configuring your webhook:

- **Webhook URL:** Your [REST endpoint URL][7] followed by `/users/track`. For example, for the US-06 instance, the URL would be `https://rest.iad-06.braze.com/users/track`.
- **Request Body:** Raw Text

#### Request headers and method

Braze requires an HTTP header for authorization that includes your API key and another that declares your `content-type`.

- **Request Header:**
  - **Authorization:** Bearer `YOUR_API_KEY`
  - **Content-Type:** application/json
- **HTTP Method:** POST

Replace `YOUR_API_KEY` with a Braze API key with `users.track` permissions. You can create an API key within the Braze dashboard at **Developer Console** > **REST API Key** > **Create New API Key**.

![][1]

#### Request body

Add your user track request in the request body. For more details, refer to [User track][8]. The following is an example request body for this endpoint when adding an event property as a custom attribute to a user's profile:

{% raw %}

```json
{
  "attributes": [
    {
      "external_id": "{{${user_id}}}",
      "new_custom_attribute": "{{event_properties.${your_event_property}}}"
    }
  ]
}
```

{% endraw %}

{% alert note %}
Each custom event, event attribute, or attribute updated on a user's profile counts toward your [data point]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/) consumption. 
{% endalert %}

#### Additional settings
 
For your Delivery settings, select **Action-Based Delivery**. Set the **Trigger Action** to "Perform Custom Event" and choose the action that should trigger this webhook.

### Use case: Increment an integer custom attribute for a counter

This use case involves creating a custom attribute and using Liquid to count the number of times a specific action has occurred. 

For example, you might want to count how many times a user has seen an active in-app message campaign, and prevent them from receiving the campaign again after they've seen it three times. For more ideas on what you can do with Liquid logic in Braze, check out our [Liquid use case library]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases).

Follow the general steps for creating a Braze to Braze webhook, and refer to the following when configuring your webhook:

- **Webhook URL:** Your [REST endpoint URL][7] followed by `/users/track`. For example, for the US-06 instance, the URL would be `https://rest.iad-06.braze.com/users/track`.
- **Request Body:** Raw Text

#### Request headers and method

Braze requires an HTTP header for authorization that includes your API key and another that declares your `content-type`.

- **Request Header:**
  - **Authorization:** Bearer `YOUR_API_KEY`
  - **Content-Type:** application/json
- **HTTP Method:** POST

Replace `YOUR_API_KEY` with a Braze API key with `users.track` permissions. You can create an API key within the Braze dashboard at **Developer Console** > **REST API Key** > **Create New API Key**.

![][1]

#### Request body

Add your user track request in the request body as well as the Liquid to assign a counter variable. For more details, refer to [User track][8].

The following is an example of both the required Liquid and request body for this endpoint, where `your_attribute_count` is the attribute you're using to count how many times a user has seen a message: {% raw %}

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
Each time a custom attribute counter is updated (incremented or decremented) it will consume a [data point]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/), which counts toward your overall consumption.
{% endalert %}

### Use case: Trigger a second Canvas from an initial Canvas

For this use case, you'll create two Canvases and use a webhook to trigger the second Canvas from the first Canvas. This acts like an entry trigger for when a user reaches a certain point in another Canvas.

1. Start by creating your second Canvas—the Canvas that should be triggered by your initial Canvas. 
2. For the Canvas **Entry Schedule**, select **API-Triggered**.
3. Make note of your **Canvas ID**, you'll need this in a later step.
4. Continue building out the steps of your second Canvas, then save the Canvas.
5. Finally, create your first Canvas. Find the step where you want to trigger the second Canvas and create a new step with a webhook. 

Refer to the following when configuring your webhook:

- **Webhook URL:** Your [REST endpoint URL][7] followed by `canvas/trigger/send`. For example, for the US-06 instance, the URL would be `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Request Body:** Raw Text

#### Request headers and method

Braze requires an HTTP header for authorization that includes your API key and another that declares your `content-type`.

- **Request Header:**
  - **Authorization:** Bearer `YOUR_API_KEY`
  - **Content-Type:** application/json
- **HTTP Method:** POST

Replace `YOUR_API_KEY` with a Braze API key with `canvas.trigger.send` permissions. You can create an API key within the Braze dashboard at **Developer Console** > **REST API Key** > **Create New API Key**.

![][1]

#### Request body

Add your `canvas/trigger/send` request in the text field. For more details, refer to [Sending Canvas messages via API-triggered delivery][9]. The following is an example of the request body for this endpoint, where `your_canvas_id` is the Canvas ID from your second Canvas: 

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

- Braze to Braze webhooks are subject to endpoint [rate limits]({{site.baseurl}}/api/api_limits/).
- Updates to the user profile will incur additional [data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count), while triggering another message through the messaging endpoints will not.
- If you want to target [anonymous users]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), you can use `braze_id` instead of `external_id` in the request body of your webhook.
- You can save your Braze to Braze webhook as a [template]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) to be re-used again.
- You can check the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/) to view and troubleshoot webhook failures.


[1]: {% image_buster /assets/img_archive/webhook_settings.png %}
[2]: {{site.baseurl}}/api/basics/
[3]: {{site.baseurl}}/api/api_key/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[6]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/
[7]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/