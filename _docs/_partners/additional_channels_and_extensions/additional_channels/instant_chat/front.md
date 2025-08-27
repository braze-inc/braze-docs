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

The incoming webhook from Front will contain a payload that includes the message sent by the live agent. The request will need to be reformatted before it can be accepted by Braze endpoints. The Front Data Transformation template will reformat the payload and write a custom event to the user profile titled **Outbound SMS Sent,** with the message body being passed as an event property.

Before setting up a new transformation in Braze, we recommend reviewing the support matrix for each tier in our [Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview/) documentation. Our Free and Pro tiers offer a different number of active transformations and incoming requests per month. Confirm the current plan you’re on can support your use case.

## Prerequisites

Before you start, you'll need the following:

| Prerequisite             | Description                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| A Front account            | A Front account is required to take advantage of this partnership.|
| Braze Data Transformation Webhook URL | [Braze Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview/) will be used to reformat the incoming webhook from Front so it can be accepted by the Braze /users/track endpoint.|
| A Front REST API Key         | A Front REST API key will be used to make an outbound webhook request from Braze to Front. |

## Use cases

- Streamline your lead generation process using Braze automated SMS messaging to identify user preferences and enable live sales agents to follow up and close sales.
- Re-engage customers who abandoned their shopping carts by driving sales conversions through automated SMS responses and live chat support.

## Integrating Front

### Step 1: Create a data transformation

First, you'll create a new data transformation in Braze. The following steps are simplified; for a full walkthrough, see [Creating a transformation]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/).

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

    ![An example data transformation.]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
You can modify this template to meet your specific needs. For example, you can customize the pre-set custom event name. For more information, see [Data transformation overview]({{site.baseurl}}/user_guide/data/data_transformation/overview/). 
{% endalert %}

### Step 2: Create an outbound SMS campaign

Next, you'll create an SMS campaign that will listen for webhooks from Front and an custom SMS response to your customers.

#### Step 2.1: Compose your message

In the **Message** textbox, add the following Liquid code, along with any opt-out language or other static content.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Your message should be similar to the following:

![An example message using Liquid code.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Schedule the delivery

For the delivery type, select **Action-Based delivery**; then for the custom event trigger, select **Outbound SMS Sent**.

![The "Schedule Delivery" page.]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
This custom event is the Data Transformation that writes to the user’s profile. Agent messages will be saved as an event property on this event.
{% endalert %}

Finally, under **Delivery Controls**, enable re-eligibility.

![Re-eligibility enabled under "Delivery Controls."]({% image_buster /assets/img/front/braze_reeligibility.png %})

### Step 3: Create a custom channel

In the Front dashboard, go to **Settings** > **Channels** > **Add Channels**, then select **Custom Channel** and enter a name for your new Braze channel.

![A custom channel for Braze in the Front dashboard.]({% image_buster /assets/img/front/front_custom_channel.png %})

### Step 4: Configure the settings

In the outbound API endpoint field, enter the Data Transformation Webhook URL [you created earlier](#step-1-set-up-a-data-transformation-in-braze). All outbound messages from live agents on your new Braze channel will be sent here. This channel also provides an endpoint URL for Braze to forward SMS messages to in the **Incoming URL** Field.

Be sure to make a note of this URL&#8212;you'll need it later.

![The channel settings for the newly created Braze channel in Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### Step 5: Set up inbound-SMS forwarding

Next, you’ll create two new webhook campaigns in Braze so you can forward inbound SMS from customers to the Front inbox.

|Number|Purpose|
|---|---|
|Webhook campaign 1|Signals to Front that a live chat conversation is being requested.|
|Webhook campaign 2|Forwards all conversational SMS responses sent inbound from the customer to the Front inbox.|
{: .reset-td-br-1 .reset-td-br-2 }

#### Step 5.1: Create an SMS keyword category

In the Braze dashboard, go to **Audience**, choose your **SMS subscription group**, then select **Add Custom Keyword**. To create an exclusive SMS keyword category for Front, fill out the following fields.

|Field|Description|
|---|---|
|Keyword Category|The name of your keyword category, such as `FrontSMS1`.|
|Keywords|Your custom keywords, such as `TIMETOMOW`. Avoid common words to prevent accidental triggers. Keep in mind, keywords are case insensitive, so `lawn` would match `LAWN`.|
|Reply Message|The message that will be sent when a keyword is detected, such as "A landscaper will reach out to you shortly."|
{: .reset-td-br-1 .reset-td-br-2 }

![An example SMS keyword category in Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### Step 5.2: Create your first webhook campaign

In the Braze dashboard, create your first webhook campaign using the URL [you created previously](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![An example of the first webhook campaign that should be created in Braze.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

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

In the Settings tab, configure your `Authorization`, `content-type`, and `accept` request headers.

![An example request with the three required headers.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### Step 5.3: Schedule the first delivery

For **Schedule Delivery**, select **Action-Based Delivery**, then choose **Send an SMS Inbound Message** for your trigger type. Also add the SMS subscription group and keyword category you [set up previously](#step-51-create-an-sms-keyword-category).

![The "Schedule Delivery" page for the first webhook campaign.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

Under **Delivery Controls**, enable re-eligibility.

![Re-eligibility selected under "Delivery Controls" for the first webhook campaign.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Step 5.4: Create your second webhook campaign

Since your second webhook campaign will match the first, you can [duplicate the first one and rename it]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns). You can do so now.

#### Step 5.5: Schedule the second delivery

For **Schedule Delivery**, set the **action-based trigger** and the **SMS subscription group** to the same as [your the first delivery](#step-53-schedule-the-first-delivery). However, for **keyword category**, choose **Other**.

![The "Scheduled Delivery" page for the second webhook campaign, with "Other" chosen as the keyword category.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Step 5.6: Add an audience filter

Your webhook campaign can now forward inbound SMS responses from your customers. To filter SMS responses so only messages for live chats are forwarded, add the **Last Received Message From Specific Campaign** segmentation filter to the **Target Audiences Step**.

![An audience filter with "Last Received Message From Specific Campaign" selected.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Then configure your filter:

1. For **Campaign**, select the SMS campaign [you previously created](#step-2-create-an-outbound-sms-campaign).
2. For **Operator**, select **Less Than**.
3. For **Time Window**, choose the length of time a chat should stay open without a response from the customer.

![The configuration settings for the selected audience filter.]({% image_buster /assets/img/front/front_target_audience.png %})

## Considerations

### Billable Segments

- SMS messages at Braze are charged per message segment. Understanding what defines a segment and how these messages will be split is key in understanding how you will be billed for messages. See more information in our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/).
- Long agent responses will consume more billable segments.

### Data Point Consumption

Currently this integration requires a custom event to be written to a user profile every single time a live agent sends an SMS from Front. This may be suitable for quick exchanges that only last a couple of messages - but as conversations get lengthier so do the data point implications. A data point is consumed for each custom event logged to Braze.

### Including Links in SMS messages

Sending a link from the Front live chat will render with extra HTML tags.

### Attaching image file from Front

Image files in Front will not render in SMS messages sent from Braze.

### Opt-outs 

Conversational messages have a higher risk of containing the word “stop” or similar vernacular that can be recognized as fuzzy opt-outs.
