---
nav_title: Creating a Transformation
article_title: Creating a Transformation
page_order: 1
page_type: reference
description: "This reference article provides steps to create a transformation using Braze Data Transformation."
---

# Creating a transformation

> Braze Data Transformation enables you to build and manage webhook integrations to automate data flow from external platforms into Braze user profiles. This integrated user data can then power even more sophisticated marketing use cases.

## Prerequisites 

| Requirement | Description |
| --- | --- |
| Two-factor authentication or SSO | You must have [two-factor authentication]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#two-factor-authentication) (2FA) or [single sign-on]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#single-sign-on-sso-authentication) (SSO) enabled for your account. |
| Correct permissions | You must be either an account admin or a workspace admin, or have "Manage Transformations" user permissions. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Step 1: Identify a source platform

Identify an external platform you want to connect to Braze and check that the platform supports webhooks. Sometimes, these settings are referred to as "API notifications" or "web service requests".

The following is an example [Typeform webhook](https://www.typeform.com/help/a/webhooks-360029573471/), which is configurable by logging into their platform:

![][9]

## Step 2: Create a transformation

Navigate to the Braze dashboard, and go to **Data Settings** > **Data Transformations**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Transformations** under **Data**.
{% endalert %}

Create and name your new transformation. This will open a detailed view, showing your most recent webhook this transformation has received and a space to write your transformation. 

![][11]

## Step 3: Send a test webhook (recommended)

This step is optional, but we recommend sending a test webhook from your source platform to your newly created transformation. 

1. Copy the URL from your transformation.
2. In your source platform, find a “Send Test” capability to have it generate a sample webhook to send over to this URL. 
- If your source platform prompts for a request type, select **POST**.
- If your source platform provides authentication options, select **No authentication**.
- If your source platform asks for secrets, select **No secrets**.
3. Refresh your page in Braze to see if the webhook has been received. If it was received, you should see a webhook payload under “Most recent webhook”.

Here’s what it looks like for Typeform:<br>![][12]

{% alert note %}
Braze Data Dransformation may not yet support external platforms that require special verification or authentication for webhooks. Consider leaving [product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) if you're interested in using this type of platform with Braze Data Transformation.
{% endalert %}

## Step 4: Write transformation code

If you have little to no experience with JavaScript code or prefer more detailed instructions, follow the **Beginner** tab for writing your transformation code.

If you're a developer or have significant experience with JavaScript code, follow the **Advanced** tab for high-level instructions on writing your transformation code.

{% alert tip %}
Braze Data Transformation has an AI copilot that asks ChatGPT to help you write your code, instead of using the default template. Access the AI copilot by clicking <i class="fa-solid fa-wand-magic-sparkles"></i> **Generate transformation code**. To use this, a webhook must be sent to your transformation.

![]({% image_buster /assets/img/data_transformation/data_transformation3.png %})
{% endalert %}

{% tabs %}
{% tab Beginner %}

Here, you will write transformation code to define how you’d like to map various webhook values to Braze user profiles.

1. New transformations will include this default template in the **Transformation Code** section:
    ```
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

    // After the/users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```

2. If you’d like all three (custom attributes, custom events, and purchases) in your transformation calls, skip to step 3. Otherwise, delete the sections that you don't need.<br><br>
3. Each attribute, event, and purchase object requires a user identifier, either an `external_id`, `user_alias`, `braze_id`, `email`, or `phone`. Find the user identifier in the incoming webhook's payload, and template in that value in your transformation code via a payload line. Use dot notation to access payload object properties. <br><br> Note that using `email` or `phone` as your identifier requires early access to this functionality. Reach out to us at [data-transformation@braze.com](mailto:data-transformation@braze.com) for access. The example [transformation code]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/#example-transformation-code) uses this functionality.<br><br>
4. Find the webhook values you’d like to represent as attributes, events, or purchases, and template those values in your transformation code via a payload line. Use dot notation to access payload object properties.<br><br>
5. For each attribute, event, and purchase object, examine the `_update_existing_only` value. Set this to `false` if you want the transformation to create a new user that may not exist. Leave this as `true` to only update existing profiles.<br><br>
6. Click **Validate** to return a preview of your code’s output and to check if it is an acceptable `/users/track` request.<br><br>
7. Activate your transformation. For additional help with your code before activating it, contact your Braze account manager.<br><br>
7. Have your source platform begin sending webhooks. Your transformation code will run for each incoming webhook, and user profiles will begin updating. 

Your webhook integration is now complete!

{% alert important %}
Accepting an email or phone number as an identifier is possible because Braze Data Transformation users can be granted early access to the `/users/track` feature. If you're interested in participating in this early access, contact [data-transformation@braze.com](mailto:data-transformation@braze.com).<br><br>Early access users of Braze Data Transformation who started before April 2023 may be familiar with a `get_user_by_email` function that helped with this use case. That function is deprecated.
{% endalert %}

{% endtab %}
{% tab Advanced %}

In this step, you will transform the webhook payload from the source platform to a JavaScript object return value. This return value must adhere to Braze’s `/users/track` request body format:

- Transformation code is accepted in the JavaScript programming language. Any standard JavaScript control flow, such as if/else logic, is supported.
- Transformation code accesses the webhook request body via the `payload` variable. This variable is an object populated by parsing the request body JSON.
- Any feature supported in our `/users/track` endpoint is supported, including:
  - User attributes objects, event objects, and purchase objects
  - Nested attributes and nested custom event properties
  - Subscription group updates
  - Email address as an identifier

Click **Validate** to return a preview of your code's output and to check if it's an acceptable `/users/track` request.

{% alert note %}
External network requests, third-party libraries, and non-JSON webhooks are not currently supported.
{% endalert %}

{% alert important %}
Accepting an email or phone number as an identifier is possible because Braze Data Transformation users can be granted early access to the `/users/track` feature. If you're interested in participating in this early access, reach out to [data-transformation@braze.com](mailto:data-transformation@braze.com).<br><br>Early access users of Braze Data Transformation who started before April 2023 may be familiar with a `get_user_by_email` function that helped with this use case. That function is deprecated.
{% endalert %}

{% endtab %}
{% endtabs %}

## Step 5: Monitor your transformation

After activating your transformation, refer to the analytics on the **Transformations** page to monitor its performance.

- **Incoming Requests:** This is the number of webhooks received at this transformation’s URL. If incoming requests are 0, your source platform hasn’t sent over any webhooks, or the connection cannot be made.
- **Deliveries:** After receiving incoming requests, Data Transformation applies your transformation code to create a Braze `/users/track` request.

The number of deliveries will never exceed the number of incoming requests. However, it's a good goal to have 100% of incoming requests leading to deliveries.

### Troubleshooting

- If deliveries are 0, check your transformation code to ensure there are no syntax errors and that it compiles. Then, check whether the output is a valid `/users/track` request.
- If deliveries are less than the number of incoming requests, that indicates that at least some webhooks are delivered successfully transformed to `/users/track`. Your transformation code doesn't account for 100% of the webhooks received.
- If your source platform has logs, check for inconsistencies across different webhooks.
- If your transformation code has if/else logic, check if one of the control flows is the cause of failure.


[4]: {% image_buster /assets/img/data_transformation/data_transformation3.png %}
[5]: {% image_buster /assets/img/data_transformation/data_transformation4.png %}
[6]: {% image_buster /assets/img/data_transformation/data_transformation5.png %}
[7]: {% image_buster /assets/img/data_transformation/data_transformation6.jpg %}
[8]: {% image_buster /assets/img/data_transformation/data_transformation7.png %}
[9]: {% image_buster /assets/img/data_transformation/data_transformation8.png %}
[10]: {% image_buster /assets/img/data_transformation/data_transformation9.png %}
[11]: {% image_buster /assets/img/data_transformation/data_transformation10.png %}
[12]: {% image_buster /assets/img/data_transformation/data_transformation11.png %}
