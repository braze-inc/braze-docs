---
nav_title: Braze to Braze Webhooks
article_title: Braze to Braze Webhooks
page_order: 3
channel:
  - webhooks
description: "This tutorial covers how to create a Braze to Braze webhook for key use cases."

---

# Braze to Braze webhooks

You can use webhooks to communicate with the Braze REST API, essentially doing anything that our API allows you to do. We refer to this as a Braze to Braze webhook—a webhook that is communicating from Braze to Braze.

## Use cases

Here are some common use cases for Braze to Braze webhooks: 

- Write or update custom attributes on a user profile.
- Reference an event property throughout a Canvas.
- Increment an integer custom attribute for a counter when a user receives a message.
- Endless "If This Then That" ([IFTTT](https://ifttt.com/about)) recipes.

### Write a custom attribute {#use-case-custom-attribute}

1. [Create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-choose-where-to-build-your-message) as a campaign or Canvas step.
2. From the list of templates, choose **Blank Template**.
3. In the **Compose** tab, fill out the following fields:<br><br>
    - **Webhook URL:** Your [REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances) followed by `/users/track`. For example, for US-06 instance, your URL would be as follows:
    ```
    https://rest.iad-06.braze.com/users/track
    ```
    - **Request Body:** Select **Raw Text** and add the user track request in the text field. For more details, refer to [User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). The following is an example request body for this endpoint: {% raw %}
    ```json
{
  "app_group_id": "YOUR_APP_GROUP_ID",
  "attributes": [
    {
      "external_id": "{{${USER_ID}}}",
      "new_custom_attribute": "{{event_properties.${YOUR_EVENT_PROPERTY}}}"
    }
  ]
}
    ```
{% endraw %}

4. In the **Settings** tab, set the **HTTP Method** to POST and add a **Request Header** with a key of `Content-Type` and a value of `application/json`.
5. Continue to step 2 and configure your delivery options.
    - Select **Action-Based Delivery**.
    - Set the **Trigger Action** to "Perform Custom Event" and choose the action that should trigger this webhook.
5. Continue to build out the rest of your webhook as needed. Braze recommends that you always test your messages before sending. Test by targeting yourself and triggered the custom event, then verify that the custom attribute was written to your profile.

### Reference an event property throughout a Canvas {#use-case-event-property}

You can use a webhook to have event properties persist throughout a Canvas, not just in the first step. In the first step of a Canvas, add a webhook that takes the event property and permanently writes that as a custom attribute to be referenced later in the Canvas.

This example use case leverages the [User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint.

1. [Create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-choose-where-to-build-your-message) as a Canvas step.
2. From the list of templates, choose **Blank Template**.
3. In the **Compose** tab, fill out the following fields:<br><br>
    - **Webhook URL:** Your [REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances) followed by `/users/track`. For example, for US-06 instance, your URL would be as follows:
    ```
    https://rest.iad-06.braze.com/users/track
    ```
    - **Request Body:** Select **Raw Text** and add the user track request in the text field. For more details, refer to [User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). The following is an example request body for this endpoint: {% raw %}
    ```json
{
    "attributes": [
        {
        "external_id": "{{${USER_ID}}}",
        "your_attribute": "{{event_properties.${YOUR_EVENT_PROPERTY}}}"
        }
    ]
}
    ```
{% endraw %}

4. In the **Settings** tab, set the **HTTP Method** to POST and configure the following key-value pairs for your **Request Headers:**<br><br>
    - `Content-Type` --> `application/json`
    - `Authorization` --> `Bearer YOUR_API_KEY`<br><br>

5. Continue to build out the rest of your webhook as needed. Braze recommends that you always test your messages before sending. Test by targeting and triggering yourself and sending the event and event property, then verify that the event property was written to your profile.

## Things to know

- Braze to Braze webhooks are subject to endpoint [rate limits]({{site.baseurl}}/api/api_limits/).
- This method will incur additional [data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count).
- You can save your Braze to Braze webhook as a [template]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) to be re-used again.
- You can check the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/) to view and troubleshoot webhook failures.