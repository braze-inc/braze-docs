---
nav_title: Front
article_title: Front
description: "Learn how to integrate Front with Braze"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> Front's integration enables you to leverage Braze Data Transformation and webhooks from each platform to set up a two-way conversational SMS pipeline.

The incoming webhook from Front will contain a payload that includes the message sent by the live agent. The request will need to be reformatted before it can be accepted by Braze’s endpoints. The Front Data Transformation template will reformat the payload and write a custom event to the user profile titled **Outbound SMS Sent,** with the message body being passed as an event property.

Before setting up a new transformation in Braze, we recommend reviewing the support matrix for each tier in our [Data Transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/) documentation. Our Free and Pro tiers offer a different number of active transformations and incoming requests per month. Confirm the current plan you’re on can support your use case.

## Prerequisites

Before you start, you'll need the following:

| Prerequisite             | Description                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| A Front account            | A Front account is required to take advantage of this partnership.|
| Braze Data Transformation Webhook URL | [Braze Data Transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/) will be used to reformat the incoming webhook from Front so it can be accepted by Braze’s /users/track endpoint.|
| A Front REST API Key         | A Front REST API key will be used to make an outbound webhook request from Braze to Front. |

## Use cases

- Streamline your lead generation process using Braze's automated SMS messaging to identify user preferences and enable live sales agents to follow up and close sales.
- Re-engage customers who abandoned their shopping carts by driving sales conversions through automated SMS responses and live chat support.

## Integrating Front

### Step 1: Create a data transformation

First, you'll create a new data transformation in Braze. The following steps are simplified; for a full walkthrough, see [Creating a transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation).

1. In Braze, go to **Data Settings** > **Data Transformations**, then select **Create Transformation** .
2. Under **Editing Experience**, select **Start from scratch**.
3. Under **Select Destination**, select **POST: Track Users**.
4. Copy and paste the following transformation template, then save and activate endpoint.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    Your transformation should be similar to the following:

    ![alt text]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
You can modify this template to meet your specific needs. For example, you can customize the pre-set custom event name. For more information, see [Data transformation overview]({{site.baseurl}}/docs/user_guide/data_and_analytics/data_transformation/overview/). 
{% endalert %}

### Step 2: Create a new custom channel in the Front dashboard

In the Front dashboard, go to **Settings** > **Channels** > **Add Channels**, then select **Custom Channel** and enter a name for your new Braze channel.

![alt text]({% image_buster /assets/img/front/front_custom_channel.png %})

### Step 3: Configure the settings for your new custom Braze Channel

In the outbound API endpoint field, enter the Data Transformation Webhook URL [you created earlier](#step-1-set-up-a-data-transformation-in-braze). All outbound messages from live agents on your new Braze channel will be sent here. This channel also provides an endpoint URL for Braze to forward SMS messages to in the **Incoming URL** Field.

Be sure to make a note of this URL&#8212;you'll need it later.

![alt text]({% image_buster /assets/img/front/front_custom_channel2.png %})

### Step 4: Forward inbound SMS from customers to the Front inbox 

Next, you'll create a new webhook campaign in Braze to forward inbound SMS from customers to the Front inbox.

#### Step 4.1: Create a webhook campaign 

In the Braze dashboard, create a new webhook campaign using the URL [you created previously](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![alt text]({% image_buster /assets/img/front/sms_to_front.png %})

Add the following to your request body:

{% raw %}
```liquid
{ 
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

In the Settings tab, configure the following request headers:

| Header         | Definition                  |
|----------------|-----------------------------|
| `Authorization`  | ENTER DEFINITION HERE.      |
| `content-type`   | ENTER DEFINITION HERE.      |
| `accept`         | ENTER DEFINITION HERE.      |
{: .reset-td-br-1 .reset-td-br-2 }

![alt text]({% image_buster /assets/img/front/webhook_settings.png %})

#### Step 4.2: Schedule the delivery

For **Schedule Delivery**, select **Action-Based Delivery**, then choose **Send an SMS Inbound Message** for your trigger type. Also add an SMS subscription group and keyword category.

Under **Delivery Controls**, enable re-eligibility.

![alt text]({% image_buster /assets/img/front/braze_reeligibility.png %})

##### Example

In the following example **Other** is selected for the keyword category and will catch and forward any inbound SMS response from a customer&#8212;whether it matches a keyword or not. To create stricter definitions for which inbound messages should be forwarded to Front, you can either use the keyword groups _or_ the option: **where the message body**.

![alt text]({% image_buster /assets/img/front/braze_delivery.png %})

### Step 5: Create outbound SMS from Front to customer 

Next, you'll create an SMS campaign that will listen for webhooks from Front and template in the Front Agent’s response into an outbound SMS to the customer.

#### Step 5.1: Compose your message

In the **Message** textbox, add the following liquid code, along with any opt-out language or other static content.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Your message should be similar to the following:

![alt text]({% image_buster /assets/img/front/sms_to_braze.png %})

#### 5.2 Schedule the delivery

For the delivery type, select **Action-Based delivery**; then under **Outbound SMS Sent**, add a custom event trigger.

![alt text]({% image_buster /assets/img/front/braze_delivery.png %})

{% alert note %}
This is the custom event that the Data Transformation we set up earlier writes to the user’s profile. The Front Agent’s message was saved as an event property on that custom event.
{% endalert %}

Finally, under **Delivery Controls**, enable re-eligibility.

![alt text]({% image_buster /assets/img/front/braze_reeligibility.png %})

## Considerations

### Billable Segments

- SMS messages at Braze are charged per message segment. Understanding what defines a segment and how these messages will be split is key in understanding how you will be billed for messages. See more information in our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments).
- Long agent responses will consume more billable segments.

### Data Point Consumption

Currently this integration requires a custom event to be written to a user profile every single time a live agent sends an SMS from Front. This may be suitable for quick exchanges that only last a couple of messages - but as conversations get lengthier so do the data point implications. A data point is consumed for each custom event logged to Braze.

### Including Links in SMS messages

Sending a link from the Front live chat will render with extra HTML tags.

### Attaching image file from Front

Image files in Front will not render in SMS messages sent from Braze.

### Opt-outs 

Conversational messages have a higher risk of containing the word “stop” or similar vernacular that can be recognized as fuzzy opt-outs.
