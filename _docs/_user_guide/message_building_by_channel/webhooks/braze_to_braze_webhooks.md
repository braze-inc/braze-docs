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

You can use webhooks to communicate with the Braze [REST API]({{site.baseurl}}/api/basics/), essentially doing anything that our API allows you to do. We refer to this as a Braze to Braze webhook—a webhook that is communicating from Braze to Braze. 

## Prerequisites

To create a Braze to Braze webhook, you'll need an [API key]({{site.baseurl}}/api/api_key/) with permissions for the endpoint you want to reach. For example, if you're using the User track endpoint, you'll need an API key with `users.track` permissions.

## Use cases

While there's a lot you can do with Braze to Braze webhooks, here are some common use cases to get you started:

- [Write or update custom attributes](#use-case-custom-attribute) on a user profile.
- [Reference an event property](#use-case-event-property) throughout a Canvas.
- [Increment an integer custom attribute](#use-case-increment-counter) for a counter when a user receives a message.
- Trigger a second Canvas from an initial Canvas.
- Endless "If This Then That" ([IFTTT](https://ifttt.com/about)) recipes.

The example use cases on this page assume that you're already familiar with [how webhooks work]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) and how to [create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) in Braze.

### Write a custom attribute {#use-case-custom-attribute}

This use case involves using a webhook to update user information as part of a Canvas step or campaign. With this use case, you'll leverage the `users/track` endpoint.

1. [Create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-choose-where-to-build-your-message) as a campaign or Canvas step. Choose **Blank Template**.
2. In the **Compose** tab, fill out the following fields:<br><br>
    - **Webhook URL:** Your [REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances) followed by `/users/track`. For example, for the US-06 instance, the URL would be as follows:
    ```
    https://rest.iad-06.braze.com/users/track
    ```
    - **Request Body:** Select **Raw Text** and add the user track request in the text field. For more details, refer to [User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). The following is an example request body for this endpoint: {% raw %}
    ```json
{
  "app_group_id": "your_app_group_id",
  "attributes": [
    {
      "external_id": "{{${user_id}}}",
      "new_custom_attribute": "{{event_properties.${your_event_property}}}"
    }
  ]
}
    ```
{% endraw %}

3. In the **Settings** tab, set the **HTTP Method** to POST and add a **Request Header** with a key of `Content-Type` and a value of `application/json`.
4. Continue to step 2 and configure your delivery options.<br><br>
    - Select **Action-Based Delivery**.   
    - Set the **Trigger Action** to "Perform Custom Event" and choose the action that should trigger this webhook.

Continue to build out the rest of your webhook as needed. Braze recommends that you always test your messages before sending. Test by targeting yourself and triggered the custom event, then verify that the custom attribute was written to your profile.

### Reference an event property throughout a Canvas {#use-case-event-property}

This use case involves using a webhook to have event properties persist throughout a Canvas, not just in the first step. In the first step of a Canvas, add a webhook that takes the event property and permanently writes that as a custom attribute to be referenced later in the Canvas. With this use case, you'll leverage the `users/track` endpoint.

1. [Create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-choose-where-to-build-your-message) as a Canvas step. Choose **Blank Template**.
2. In the **Compose** tab, fill out the following fields:<br><br>
    - **Webhook URL:** Your [REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances) followed by `/users/track`. For example, for the US-06 instance, the URL would be as follows:
    ```
    https://rest.iad-06.braze.com/users/track
    ```
    - **Request Body:** Select **Raw Text** and add the user track request in the text field. For more details, refer to [User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). The following is an example request body for this endpoint where `your_attribute` is the attribute you're writing to the user's profile: {% raw %}
    ```json
{
    "attributes": [
        {
        "external_id": "{{${user_id}}}",
        "your_attribute": "{{event_properties.${your_event_property}}}"
        }
    ]
}
    ```
{% endraw %}

3. In the **Settings** tab, set the **HTTP Method** to POST and configure the following key-value pairs for your **Request Headers:**<br><br>
    - `Content-Type` --> `application/json`
    - `Authorization` --> `Bearer YOUR_API_KEY`<br><br>

Continue to build out the rest of your webhook as needed. Braze recommends that you always test your messages before sending. Test by targeting and triggering yourself and sending the event and event property, then verify that the event property was written to your profile.

### Increment an integer custom attribute for a counter {#use-case-increment-counter}

This use case involves creating a custom attribute to count the number of times a specific action has occurred. For example, you might want to count how many times a user has seen an active in-app message campaign, and prevent them from receiving the campaign again after they've seen it three times. With this use case, you'll leverage the `/users/track` endpoint.

1. [Create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-choose-where-to-build-your-message) as a campaign or Canvas step. Choose **Blank Template**.
2. In the **Compose** tab, fill out the following fields:<br><br>
    - **Webhook URL:** Your [REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances) followed by `/users/track`. For example, for the US-06 instance, the URL would be as follows:
    ```
    https://rest.iad-06.braze.com/users/track
    ```
    - **Request Body:** Select **Raw Text** and add the user track request in the text field as well as the Liquid to assign a counter variable. For more details, refer to [User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). The following is an example of both the required Liquid and request body for this endpoint, where `your_attribute_count` is the attribute you're using to count how many times a user has seen a message: {% raw %}
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

3. In the **Settings** tab, set the **HTTP Method** to POST and configure the following key-value pairs for your **Request Headers:**<br><br>
    - `Content-Type` --> `application/json`
    - `Authorization` --> `Bearer YOUR_API_KEY`<br><br>

Continue to build out the rest of your webhook as needed. Braze recommends that you always test your messages before sending.

## Things to know

- Braze to Braze webhooks are subject to endpoint [rate limits]({{site.baseurl}}/api/api_limits/).
- This method will incur additional [data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count).
- You can save your Braze to Braze webhook as a [template]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) to be re-used again.
- You can check the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/) to view and troubleshoot webhook failures.