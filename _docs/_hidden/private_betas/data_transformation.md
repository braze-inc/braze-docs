---
nav_title: Braze Data Transformation
permalink: "/data_transformation/"
hidden: true
layout: dev_guide
---

# Braze data transformation

> Data transformation allows you to build and manage webhook integrations, to automate data flow from external platforms onto Braze user profiles. This user data can then power even more sophisticated marketing use cases.

Data transformation is a low-code solution, and you can be up and running in minutes, even if you have very little coding experience.
The feature can help replace your team’s dependency on manual API calls, third-party integration tools, or even customer data platforms.

{% alert important %}
Data transformation is currently in early access. Contact your Braze customer success manager if you are interested in participating in the early access.
{% endalert %}

{% alert important %}
As of April 2022, an updated version of data transformation will be available for you. This updated version no longer requires a review and approval workflow. Enabled transformations will begin working instantaneously. If you are a first-time user, it is highly recommended that you test your webhook integration in a dev or sandbox app group first.<br><br> This updated version of data transformation will no longer accept Ruby transformation code but will instead support JavaScript code.
Our team is happy to review your code before you enable a transformation; reach out to [data-transformation@braze.com](mailto:data-transformation@braze.com) if needed.
{% endalert %}

## How it works

Many modern-day platforms can send webhooks, real-time notifications, when something happens. Data transformation with Braze builds on these external webhooks by providing a Braze address to send those webhooks to.

To do this, you will have to write transformation code to map the contents of those incoming webhooks and create an output that matches Braze’s `/users/track` schema. You have full flexibility in what you want to use from the webhook, and how you want the data represented as Braze user attributes, events, and purchases. 

Lastly, you must enable your transformation and send webhooks from your external platform. Your transformation will apply to every webhook we receive, and your integration is complete.

{% details More on webhooks %}
These real-time notifications, sent via an HTTP POST request to a destination of your choice, usually describe what’s happening and who is involved. For example, an online form and survey provider can send a webhook whenever a survey response is received, and a customer software platform can send a webhook whenever a service ticket is created.
{% enddetails %}

## Prerequisites 

| Requirement | Description |
| --- | --- |
| 2FA or SSO | You must have 2FA or SSO enabled for your account. |
| Correct permissions | You must be either an account admin or an app group admin, or have user permissions for **Manage Transformations**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Example use cases

The following example use cases are possible with a combination of webhooks from the external platform and Braze data transformation:

**Typeform**<br>You host a lead generation Typeform form on your website. When new users fill out this form, you can:
- Create new users in Braze
- Add them to one of your Braze email lists
- Sync some of their responses as custom attributes in Braze, as their answers are valuable first-party data that can power personalized messaging experiences for future use.

**Zendesk**<br>When customers open customer service tickets, you can:
- Write a custom event in Braze when a Zendesk ticket is created
- Write a custom event with event properties in Braze when a negative CSAT rating is provided to Zendesk

**Iterate**<br>Braze has an [integration]({{site.baseurl}}/partners/message_orchestration/channel_extensions/surveys/iterate/) available with Iterate, a customer insights and survey platform. With Data Transformation, you can:
- Save multiple survey responses under one nested custom attribute, as opposed to the existing integration that saves multiple custom attributes

## Example transformation code

Consider this sample payload from the survey platform Typeform, which sends whenever a survey response is received.

![][3]

{% tabs local %}
{% tab Basic transformation %}


This simple use case takes some of those answers as attributes and writes an event to indicate that the survey was completed:

```
return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab Advanced transformation %}

This intermediate use case builds on the simple use case by introducing an if statement on one of the answers to categorize the user.

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
}

return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_NPS_category": nps_category
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
};
```
{% endtab %}
{% endtabs %}

## Step-by-step guide

### Step 1: Identify a source platform

Identify an external platform you want to connect to Braze and check that the platform supports webhooks. Sometimes, these settings are referred to as "API notifications" or "web service requests".

Shown below is an [example Typeform webhook](https://www.typeform.com/help/a/webhooks-360029573471/), which are easily configurable by logging on to their platform:

![][9]

### Step 2: Create a transformation

Navigate to the Braze dashboard, and select the **Transformations** page under the **Data** section.

Next, name your transformation and click **Create Transformation**. 

First, click into your transformation. This will open a detailed view showing your most recent webhook this transformation has received, and room to write your own transformation. 

![][11]

### Step 3: Send a test webhook (recommended)

This step is optional but we recommend sending a test webhook from your source platform over to your newly created transformation. 

To do this you must copy the URL from your transformation, and back in your source platform, find a “Send Test” capability to have it generate a sample webhook to send over to this URL. 
- If your source platform prompts for a request type, choose **POST**
- If your source platform provides authentication options, choose **no authentication**
- If your source platform asks for secrets, choose **no secrets**

Once this is done, refresh your page in Braze to see if the webhook has been received. You would see a webhook payload under “Most recent webhook” if it was received.

Here’s what it looks like for Typeform:<br>![][12]

{% alert note %}
If the external platform requires special verification or authentication, the current early access version of data transformation may not support this. If this is the case, consider letting us know at [data-transformation@braze.com](mailto:data-transformation@braze.com).
{% endalert %}

### Step 4: Write transformation code

If you are a developer or have significant experience with JavaScript code, follow the **Advanced** tab for high-level instructions on writing your transformation code.

If you have little to no experience with JavaScript code or would like more detailed instructions, follow the **Beginner** tab for writing your transformation code.

{% tabs %}
{% tab Advanced %}

In this step, you will transform the webhook payload from the source platform to a JavaScript object return value. This return value must adhere to Braze’s `/users/track` request body format:

- Transformation code is accepted in the JavaScript programming language. Any standard JavaScript control flow, such as if/else logic is supported.
- Transformation code accesses the webhook request body via the `payload` variable. This variable is an object populated by parsing the request body JSON.
- Any feature supported in our `/users/track` endpoint is supported, including:
  - User attributes objects, event objects, and purchase objects
  - Nested attributes and nested custom event properties
  - Subscription group updates
  - Email address as an identifier

{% alert note %}
External network requests, third-party libraries, and non-JSON webhooks are not currently supported.
{% endalert %}
{% endtab %}
{% tab Beginner %}

In this step, you will express how you'd like to map various webhook values to Braze user profiles, starting with a default data transformation template. 

1. New transformations will start with this default template in the **Transformation Code** section:
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
2. If you’d like all three (custom attributes, custom events, and purchases) in your transformation calls, skip to step 3. Otherwise, delete the sections that you do not need.<br><br>
3. Each attribute, event, and purchase object requires a user identifier, either an `external_id`, `user_alias`, email, or `braze_id`). Find the user identifier in the incoming webhook’s payload and template in that value in your transformation code via a payload line. Use dot notation to access payload object properties.<br>Simply template in the email address from the incoming webhook and use “email” as your identifier in the transformation code. For example, our Example Transformation Code page uses this new `/users/track` functionality.<br><br>
4. Find the webhook values you’d like to represent as attributes, events, and/or purchases and template those values in your transformation code via a payload line. Use dot notation to access payload object properties.<br><br>
5. For each attribute, event, and purchase object, examine the `_update_existing_only` value. Set this to `false` if you would like the transformation to create a new user that may not exist. Leave this as true if you’d like to only update existing profiles.<br><br>
6. Activate your transformation. It is highly recommended that you do this first in a dev app group to test. If you’d like help with your code before activating it, contact [data-transformation@braze.com](mailto:data-transformation@braze.com).<br><br>
7. Have your source platform begin sending webhooks. Your transformation code will run for each incoming webhook, and user profiles will begin updating. Your webhook integration is now complete!

{% alert important %}
Accepting email as an identifier is possible as data transformation early access users will also be granted early access to this new `/users/track` feature to update a user profile by email address.<br><br>Data transformation Early access users who started before April 2023 may be familiar with a `get_user_by_email` function that helped with this use case. That function is deprecated.
{% endalert %}

{% endtab %}
{% endtabs %}

### Step 5: Monitoring your transformation

After activating your transformation, refer to the analytics on the **Transformations** page to monitor its performance.

**Incoming Requests**<br>This is the number of webhooks received at this transformation’s URL. If incoming requests are 0, your source platform hasn’t sent over any webhooks, or the connection cannot be made.

**Deliveries**<br>After receiving incoming requests, data transformation applies your transformation code to create a Braze `/users/track` request.

The number of deliveries will never be greater than the number of incoming requests. However, it is a good goal to have 100% of incoming requests leading to deliveries.

- If deliveries are 0, check your transformation code to ensure there are no syntax errors and that it compiles. Then, check whether the output is a valid `/users/track` request.
- If deliveries are less than the number of incoming requests, that indicates that at least some webhooks are delivered successfully transformed to `/users/track`. Your transformation code does not account for 100% of the webhooks received.
- If your source platform has logs, look to see if there are inconsistencies across different webhooks.
- If your transformation code has if/else logic, look closely to see if one of the control flows is the cause of failure.

## Frequently asked questions

{% details What gets synced with data transformation? %}
Any data the external platform makes available in a webhook can be synced to Braze. The more an external platform sends via webhooks, the more options for choosing what gets synced.
{% enddetails %}

{% details I’m a marketer. Do I need developer resources to use data transformation? %}
While we would love for developers to use this feature as well, you don’t need to be one to use this! We’ve seen marketers successfully set up transformations without developer resources.
{% enddetails %}

{% details Can I still use data transformation if my external platform only gives an email address as an identifier and no Braze ID or Braze external ID? %}
Yes. Data transformation early access users will also be granted early access to this new [`/users/track` feature]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address) to update a user profile by email address.

Simply use `email` as your identifier property in the transformation code instead of “external_id” or `braze_id`. For example, our example [Transformation code](#example-transformation-code) uses this new `/users/track` functionality.

{% alert note %}
Data transformation early access users who started before April 2023 may be familiar with a `get_user_by_email` function that helped with this use case. That function has been deprecated.
{% endalert %}
{% enddetails %}

{% details Are there rate limits with data transformation? %}
The rate limit for incoming webhooks is 250 requests per minute across your entire company. If you need a higher rate limit, ask us at [data-transformation@braze.com](mailto:data-transformation@braze.com).
{% enddetails %}

{% details Does data transformation consume data points? %}
In most cases, yes. Data transformation eventually creates a `/users/track` call that writes the attributes, events, and purchases you want. These will consume data points in the same way as if the `/users/track` call was made independently.
You have control over how many data points will be written based on how you write your transformation.
{% enddetails %}

{% details How can I get help setting up my use case or with my transformation code? %}
Send us your questions with a link to your transformation at [data-transformation@braze.com](mailto:data-transformation@braze.com).
{% enddetails %}

[1]: {% image_buster /assets/img_archive/data_transformation1.png %}
[2]: {% image_buster /assets/img/data_transformation/data_transformation1.jpg %}
[3]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}
[5]: {% image_buster /assets/img/data_transformation/data_transformation4.png %}
[6]: {% image_buster /assets/img/data_transformation/data_transformation5.png %}
[7]: {% image_buster /assets/img/data_transformation/data_transformation6.jpg %}
[8]: {% image_buster /assets/img/data_transformation/data_transformation7.png %}
[9]: {% image_buster /assets/img/data_transformation/data_transformation8.png %}
[10]: {% image_buster /assets/img/data_transformation/data_transformation9.png %}
[11]: {% image_buster /assets/img/data_transformation/data_transformation10.png %}
[12]: {% image_buster /assets/img/data_transformation/data_transformation11.png %}