---
nav_title: Front
article_title: Front
description: "Learn how to integrate Front with Braze"
alias: /partners/front/
page_type: partner
search_tag: Partner
layout: dev_guide

---

# Front

> The Braze and Front integration enables you to leverage Braze Data Transformation and webhooks from each platform to set up a two-way conversational SMS pipeline.

## Prerequisites

Before you start, you'll need the following:

| Prerequisite                          | Description                                                                                                                              |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| A Front account                       | A Front account is required to take advantage of this partnership.|
| Braze Data Transformation Webhook URL | [Braze Data Transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/) will be used to reformat the incoming webhook from Front so it can be accepted by Braze’s /users/track endpoint.|
| A Front REST API Key                  | A Front REST API key will be used to make an outbound webhook request from Braze to Front. |


## Use cases

- Streamline the lead generation process by using Braze automated SMS messaging to identify user preferences and enable live sales agents to follow up and close sales.
- Re-engage customers who abandon their shopping carts and drive sales conversions through automated SMS responses and live chat support.

## Integrating Front


### Step 1: Set up a Data Transformation in Braze

The incoming webhook from Front will contain a payload that includes the message sent by the live agent. The request will need to be reformatted before it can be accepted by Braze’s endpoints. The Front Data Transformation template will reformat the payload and write a custom event to the user profile titled **Outbound SMS Sent,** with the message body being passed as an event property.

Before setting up a new transformation in Braze, we recommend reviewing the support matrix for each tier in our [Data Transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/) documentation. Our Free and Pro tiers offer a different number of active transformations and incoming requests per month. Confirm the current plan you’re on can support your use case. 

Follow the below steps to set up the Data Transformation in Braze : 
1. In Braze, go to **Data Settings** > **Data Transformations** and click **Create Transformation** 
2. Under **Editing Experience**, select **Start from scratch**
3. Under **Select Destination**, select **POST: Track Users**
4. Add Transformation Code Template (located below) and save/activate endpoint

![alt text](<data_transformation.png>)


#### Transformation Code Template:

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



The template can be modified for your specific use case. For example, you can customize the custom event name to something other than **Outbound SMS Sent**. More details on how to create and test a Data Transformation can be found in our docs.


### Step 2: Create a new custom channel for Braze in the Front dashboard

1. In the Front dashboard, go to **Settings** > **Channels** > **Add Channels** to My Company Workspace
2. Select **Custom Channel**
3. Enter a name for your new Braze channel

![alt text](<front_custom_channel.png>)

### Step 3: Configure the settings for your new custom Braze Channel

1. Paste the Data Transformation Webhook URL from **Step 1** into the outbound API endpoint field.  This is where all outbound messages typed by live agents from Front on the Braze channel will be pushed to.

![alt text](<front_custom_channel2.png>)

2. This channel also provides an endpoint URL for Braze to forward SMS messages to in the **Incoming URL** Field.  Copy this URL.

### Step 4: Forward inbound SMS from customers to the Front inbox 

Create a new webhook campaign in Braze to forward inbound SMS from customers to the Front inbox.  

1. Paste the Front incoming API endpoint URL in the webhook URL field in Braze’s webhook composer: 

![alt text](<sms_to_front.png>)

2. Add the following to the Raw Text Request Body:

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

3. In the Settings tab, configure the following request headers: 

![alt text](<webhook_settings.png>)

4. Schedule Delivery Step
- Select Action-Based Delivery.
- Select Trigger type **Send an SMS Inbound Message**.
- Add SMS subscription group and Keyword category.

![alt text](<braze_delivery.png>)

- In this example **Other** is selected for the keyword category and will catch and forward any inbound SMS response from a customer - whether it matches a keyword or not. 
- Use keyword groups OR the **where the message body** option for creating stricter definitions for which inbound messages should be forwarded to Front.
- Make sure re-eligibility is enabled for this campaign under Delivery Controls.

![alt text](<braze_reeligibility.png>)


### Step 5: Create outbound SMS from Front to customer  

Create an SMS campaign that will listen for webhooks from Front and template in the Front Agent’s response into an outbound SMS to the customer.

1. Compose Message Step
- Add ```{{event_properties.${message_body}}}``` to the message body and any opt-out language or other static message content to the body. 

![alt text](<sms_to_braze.png>)

2. Schedule Delivery Step
- Select Action-Based delivery.
- Add custom event trigger for **Outbound SMS Sent** (this is the custom event that the Data Transformation we set up earlier writes to the user’s profile. The Front Agent’s message was saved as an event property on that custom event). 
- Make sure re-eligibility is enabled for this campaign under Delivery Controls.

![alt text](<braze_delivery.png>)


## Considerations

### Billable Segments 
- SMS messages at Braze are charged per message segment. Understanding what defines a segment and how these messages will be split is key in understanding how you will be billed for messages. See more information in our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments).
- Long agent responses will consume more billable segments.

### Data Point Consumption
- Currently this integration requires a custom event to be written to a user profile every single time a live agent sends an SMS from Front.  This may be suitable for quick exchanges that only last a couple of messages - but as conversations get lengthier so do the data point implications. A data point is consumed for each custom event logged to Braze.

### Including Links in SMS messages
- Sending a link from the Front live chat will render with extra HTML tags.

### Attaching image file from Front
- Image files in Front will not render in SMS messages sent from Braze.

### Opt-outs 
- Conversational messages have a higher risk of containing the word “stop” or similar vernacular that can be recognized as fuzzy opt-outs.



