---
nav_title: Creating a transformation
article_title: Creating a Transformation
page_order: 1
page_type: reference
description: "This reference article provides steps to create a transformation using Braze Data Transformation."
---

# Creating a transformation

> Braze Data Transformation enables you to build and manage webhook integrations to automate data flow from external platforms into Braze. These webhook integrations can then power even more sophisticated marketing use cases. You can build your Data Transformation from default code, or by using our dedicated template library to help you get started with certain external platforms.

## Prerequisites 

| Requirement | Description |
| --- | --- |
| Two-factor authentication or SSO | You must have [two-factor authentication]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#two-factor-authentication) (2FA) or [single sign-on]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#single-sign-on-sso-authentication) (SSO) enabled for your account. |
| Correct permissions | You must be either an account admin or a workspace admin, or have "Manage Transformations" user permissions. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Step 1: Identify a source platform

Identify an external platform you want to connect to Braze and check that the platform supports webhooks. These settings are sometimes referred to as "API notifications" or "web service requests."

The following is an example [Typeform webhook](https://www.typeform.com/help/a/webhooks-360029573471/), which is configurable by logging into their platform:

![]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## Step 2: Create a transformation

{% multi_lang_include create_transformation.md location="default" %}

## Step 3: Send a test webhook (recommended)

This step is optional, but we recommend sending a test webhook from your source platform to your newly created transformation.

1. Copy the URL from your transformation.
2. In your source platform, find a “Send Test” capability to have it generate a sample webhook to send over to this URL. 
- If your source platform prompts for a request type, select **POST**.
- If your source platform provides authentication options, select **No authentication**.
- If your source platform asks for secrets, select **No secrets**.
3. Refresh your page in the Braze dashboard to see if the webhook has been received. If it was received, you should see a webhook payload under **Most recent webhook**.

Here’s what it looks like for Typeform:

![Example Data Transformation code that maps the webhook to Braze user profiles.]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
Braze Data Transformation may not yet support external platforms that require special verification or authentication for webhooks. Consider leaving [product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) if you're interested in using this type of platform with Braze Data Transformation.
{% endalert %}

## Step 4: Write transformation code

If you have little to no experience with JavaScript code or prefer more detailed instructions, follow the **Beginner - POST: Track users** or **Beginner - PUT: Update multiple catalog items** tab for writing your transformation code.

If you're a developer or have significant experience with JavaScript code, follow the **Advanced - POST: Track users** tab for high-level instructions on writing your transformation code.

{% alert tip %}
Braze Data Transformation has an AI copilot that asks ChatGPT to help you write your code. To access the AI copilot, select <i class="fa-solid fa-wand-magic-sparkles"></i> **Generate transformation code**. To use this, a webhook must be sent to your transformation. You can also access the template library by selecting **Insert code** > **Insert template**.

![]({% image_buster /assets/img/data_transformation/data_transformation3.png %})
{% endalert %}

{% tabs %}
{% tab Beginner - Track users %}

Here, write transformation code to define how to map various webhook values to Braze user profiles.

1. New transformations have this default template in the **Transformation Code** section:

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2. To include custom attributes, custom events, and purchases in your transformation calls, skip to step 3. Otherwise, delete the sections that you don't need.<br><br>
3. Each attribute, event, and purchase object requires a user identifier, either an `external_id`, `user_alias`, `braze_id`, `email`, or `phone`. Find the user identifier in the incoming webhook's payload, and template in that value in your transformation code via a payload line. Use dot notation to access payload object properties. <br><br>
4. Find the webhook values you’d like to represent as attributes, events, or purchases, and template those values in your transformation code via a payload line. Use dot notation to access payload object properties.<br><br>
5. For each attribute, event, and purchase object, examine the `_update_existing_only` value. Set this to `false` if you want the transformation to create a new user that may not exist. Leave this as `true` to only update existing profiles.<br><br>
6. Click **Validate** to return a preview of your code’s output and to check if it is an acceptable `/users/track` request.<br><br>
7. Activate your transformation. For additional help with your code before activating it, contact your Braze account manager.<br><br>
7. Have your source platform begin sending webhooks. Your transformation code will run for each incoming webhook, and user profiles will begin updating. 

Your webhook integration is now complete!

{% endtab %}
{% tab Beginner - Update catalog items %}

Here, you can write transformation code to define how you want to map various webhook values to Braze catalog item updates.

1. New transformations will include this default template in the **Transformation Code** section:

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",
  
  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2. Transformations for `/catalogs` destinations require a `catalog_name` to define the specific catalog to update. You can hard code this field or template the field with a webhook field via a payload line. Use dot notation to access payload object properties.<br><br>
3. Define which items you’d like to update in the catalog with the `id` fields in the items array. You can hard code these fields, or template in a webhook field via a payload line. <br><br> Keep in mind, `catalog_column` is a placeholder value. Be sure item objects only contain fields that exist in the catalog.<br><br>
4. Select **Validate** to return a preview of your code’s output and to check if it is an acceptable request for the [Update multiple catalog items endpoint]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items).<br><br>
5. Activate your transformation. For additional help with your code before activating it, contact your Braze account manager.<br><br>
6. Make sure to check if your source platform has a setting to start sending webhooks. Your transformation code will run for each incoming webhook, and the catalog items will begin updating.

Your webhook integration is now complete!

{% endtab %}
{% tab Advanced - Track users %}

In this step, you'll transform the webhook payload from the source platform to a JavaScript object return value. This return value must follow the `/users/track` endpoint request body format:

- Transformation code is accepted in the JavaScript programming language. Any standard JavaScript control flow, such as if/else logic, is supported.
- Transformation code accesses the webhook request body via the `payload` variable. This variable is an object populated by parsing the request body JSON.
- Any feature supported in our `/users/track` endpoint is supported, including:
  - User attributes objects, event objects, and purchase objects
  - Nested attributes and nested custom event properties
  - Subscription group updates
  - Email address as an identifier

Select **Validate** to return a preview of your code's output and to check if it's an acceptable `/users/track` request.

{% alert note %}
External network requests, third-party libraries, and non-JSON webhooks are not currently supported.
{% endalert %}

{% endtab %}
{% endtabs %}

## Step 5: Monitor your transformation

After activating your transformation, refer to the analytics on the main **Transformations** page for a performance summary.

* **Incoming Requests:** This is the number of webhooks received at this transformation’s URL. If incoming requests are 0, your source platform hasn’t sent over any webhooks, or the connection cannot be made.
* **Deliveries:** After receiving incoming requests, Data Transformation applies your transformation code to send to your selected Braze destination.

It’s a good goal to have 100% of incoming requests leading to deliveries. The number of deliveries will never exceed the number of incoming requests.

### Troubleshooting

For more detailed monitoring and troubleshooting, refer to the **Logs** page for specific logs, which is where the last 1,000 incoming requests to all transformations across your workspaces are logged. You can select each log to view the incoming request body, transformation output, and response body from the transformation’s destination.

If there are no deliveries, check your transformation code for any syntax errors and confirm that the code compiles. Then, check whether the output is a valid destination request.

Deliveries less than the number of incoming requests indicate that at least some webhooks are delivered successfully. Refer to transformation logs for example errors, and look to see if the transformation output is expected. It’s possible that your transformation code is not accounting for every variation of webhooks received.


