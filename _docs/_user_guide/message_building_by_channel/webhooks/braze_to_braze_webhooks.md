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

- Write or update custom attributes on a user profile.
- Reference an event property throughout a Canvas.
- Increment an integer custom attribute for a counter when a user receives a message.
- Trigger a second Canvas from an initial Canvas.
- Endless "If This Then That" ([IFTTT](https://ifttt.com/about)) recipes.

The example use cases on this page assume that you're already familiar with [how webhooks work]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) and how to [create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) in Braze.

## Steps for creating a Braze to Braze webhook

While the specifics of your webhook request will vary from use case to use case, the general workflow for creating a Braze to Braze webhook stays the same.

1. [Create a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-choose-where-to-build-your-message) as a campaign or Canvas step. 
2. Choose **Blank Template**.
3. In the **Compose** tab, specify the **Webhook URL** and **Request Body** as noted for your use case.
4. In the **Settings** tab, specify your **HTTP Method** and **Request Headers** as noted for your use case.
5. Continue to build out the rest of your webhook as needed. Note that some use cases require specific delivery settings, such as triggering the campaign or Canvas off of a custom event.

### Use case: Add an event or attribute to a user's profile

With this use case, you can update a user's profile with an event, event property, or attribute as part of a campaign or Canvas. For example, a B2C website may add an attribute of `purchase_lapsers=true` to a user's profile if they don't convert from an abandoned cart campaign or Canvas to allow those users to be retargeted with subsequent messaging.

Another common use case is a workaround to make event properties persist throughout a Canvas, rather than just the first step. This involves adding an event property as a custom attribute so that you can reference that event property throughout a Canvas. Note that [Canvas persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) solves for this issue, and is currently in beta. Please reach out to your Braze account manager for more information.

{% alert important %}
In order to reference an event property throughout a Canvas, you need to add the event property to the user profile as an attribute in the first step of the Canvas. Additionally, the Canvas itself must be triggered off of that event.
{% endalert %}

Follow the general steps for creating a Braze to Braze webhook, and refer to the following sections when configuring your webhook.

#### Webhook URL

Your [REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances) followed by `/users/track`. For example, for the US-06 instance, the URL would be as follows:

```
https://rest.iad-06.braze.com/users/track
```

#### Request Body

Select **Raw Text** and add the user track request in the text field. For more details, refer to [User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). The following is an example request body for this endpoint when adding an event property as a custom attribute to a user's profile:

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

#### HTTP Method

Set the **HTTP Method** to POST.

#### Request Headers

Add two **Request Headers** with the following corresponding keys and values:

| Key | Value |
| --- | --- |
| `Content-Type` | `application/json` |
| `Authorization` | `Bearer YOUR_API_KEY`<br><br>Your API key must have `users.track` permissions. You can create an API key within the Braze dashboard at **Developer Console** > **REST API Key** > **Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2}

#### Additional settings
 
For your Delivery settings, select **Action-Based Delivery**. Set the **Trigger Action** to "Perform Custom Event" and choose the action that should trigger this webhook.

### Use case: Increment an integer custom attribute for a counter

This use case involves creating a custom attribute to count the number of times a specific action has occurred. For example, you might want to count how many times a user has seen an active in-app message campaign, and prevent them from receiving the campaign again after they've seen it three times.

Follow the general steps for creating a Braze to Braze webhook, and refer to the following sections when configuring your webhook.

#### Webhook URL

Your [REST endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances) followed by `/users/track`. For example, for the US-06 instance, the URL would be as follows:

```
https://rest.iad-06.braze.com/users/track
```

#### Request Body

Select **Raw Text** and add the user track request in the text field as well as the Liquid to assign a counter variable. For more details, refer to [User track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). 

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

#### HTTP Method

Set the **HTTP Method** to POST.

#### Request Headers

Add two **Request Headers** with the following corresponding keys and values:

| Key | Value |
| --- | --- |
| `Content-Type` | `application/json` |
| `Authorization` | `Bearer YOUR_API_KEY`<br><br>Your API key must have `users.track` permissions. You can create an API key within the Braze dashboard at **Developer Console** > **REST API Key** > **Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2}


## Things to know

- Braze to Braze webhooks are subject to endpoint [rate limits]({{site.baseurl}}/api/api_limits/).
- This method will incur additional [data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count).
- You can save your Braze to Braze webhook as a [template]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) to be re-used again.
- You can check the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/) to view and troubleshoot webhook failures.