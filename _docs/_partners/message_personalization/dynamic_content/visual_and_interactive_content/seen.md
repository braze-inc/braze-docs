---
nav_title: Seen
article_title: Seen
description: "Seen enables personalized video experiences at scale, helping brands drive higher engagement across the customer journey."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Seen

> [Seen](https://seen.io) enables brands to create and deliver personalized video experiences at scale. With Seen, you can design a video around your data, personalize it at scale in the cloud, then distribute it where it works best.
>
> The Braze and Seen integration lets you send user data from Braze to Seen, dynamically generate personalized videos, and return video assets—such as a unique player URL and thumbnail—back into Braze for use in campaigns and Canvases.


## Use cases

Seen supports automated, personalized video delivery across the customer lifecycle, including:

- **Onboarding**: Welcome new users with videos personalized to their profile or signup context
- **Conversion and activation**: Reinforce key actions with contextual video messaging
- **Loyalty and upsell**: Highlight personalized offers or usage milestones
- **Win-back and churn prevention**: Re-engage inactive users with tailored video content


## Prerequisites

Before you begin, you need the following:

| Prerequisite | Description |
|--------------|-------------|
| Seen Platform access | You need a Seen Platform subscription or active Seen campaign. You need access to your Workspace settings to retrieve your Workspace ID and generate an API token. |
| Braze Data Transformation Webhook URL | Braze Data Transformation reformats the incoming data from Seen so it can be accepted by Braze’s /users/track endpoint. |
| Braze user data | Video personalization requires user-level data. Ensure the relevant attributes are available in Braze and that you pass **braze_id** as the unique identifier. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}




## How Seen Journeys work

Seen uses [Journeys](https://docs.seen.io/journey) to control how incoming data is processed and how video outputs are generated.

A Journey is a configurable workflow that:
- Receives data from external systems (such as Braze)
- Applies logic and personalization rules
- Generates a video and associated assets
- Returns a configurable response payload

Journeys are composed of **nodes**, each with a specific function:

- **Trigger node**: Defines how and when a Journey starts (for Braze integrations, use an `On Create` trigger)
- **Conditional node**: Routes users through different logic paths based on data values
- **Project node**: Applies dynamic video personalization using the incoming data
- **Player node**: Generates a unique video player URL
- **Webhook node**: Defines the response payload sent back to Braze

Because Journey responses are configurable, ensure the output fields returned by Seen match the attributes expected by your Braze Data Transformation.


## Rate limit
The Seen API accepts up to 100 calls every 10 seconds.


## Integration

In this example, Braze sends user data to Seen to generate a personalized video. Seen then returns a unique video player URL and thumbnail URL, which are stored as custom attributes in Braze for use in messaging.

If you have multiple video campaigns with Seen, repeat the process to connect Braze with all video campaigns.

### Step 1: Create a webhook campaign to send data to Seen

Create a new [Webhook Campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) in Braze.

Configure the webhook as follows:

- **Webhook URL**:  
  `https://next.seen.io/v1/workspaces/{WORKSPACE_ID}/data`  
  Find your Workspace ID in the Seen Platform settings.

- **HTTP Method**: POST
- **Request body**: Raw Text  
  Use the following example as a starting point. Refer to [Seen’s data creation documentation](https://docs.seen.io/create-data) for further information.

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}
- **Request headers**:
  - `Authorization`: Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  > Generate an [API token](https://docs.seen.io/authorization) in the Seen Platform under Workspace settings. You can reach out to your Seen Customer Success Manager for assistance.

- To test the webhook with a user, switch to the **Test** tab.
- After confirming the test works as intended, complete the webhook setup.


### Step 2: Configure a Journey in the Seen Platform

Seen uses [Journeys](https://docs.seen.io/journey) to define how incoming data is processed, personalized, and returned to Braze.  
Each Journey is a configurable workflow composed of nodes that let you control both video generation logic and the response payload.

To configure your Journey:

1. Create a new Journey in the Seen Platform
2. Add a **Trigger node** and select the `On Create` trigger  
   This ensures the Journey starts when Braze sends data to Seen. Create and add any [segmentation](https://docs.seen.io/segments) logic within your workspace if needed.
3. Build your logic using the following nodes as needed:
   - **Conditional node**: Route users based on attribute values (for example, plan type or region)
   - **Project node**: Apply dynamic video personalization using the incoming data
   - **Player node**: Generate a unique video player URL
4. Add a **Webhook node** to define the response sent back to Braze

#### Webhook node response requirements

Because the response payload is configurable, ensure the following fields are returned to support the Braze Data Transformation described in the next step:

| Field | Description |
|------|-------------|
| `id` | Must match the `braze_id` sent from Braze |
| `player_url` | Unique URL for the personalized video player |
| `email_thumbnail_url` | URL of the generated video thumbnail |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

If your use case requires additional attributes, include them in the response and map them in Braze.


### Step 3: Create a Data Transformation to receive data from Seen

Use Braze Data Transformations to ingest the Seen Journey response and store video assets on the user profile.

1. Create the following [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) in Braze:
   - `player_url`
   - `email_thumbnail_url`
2. Navigate to **Data Settings** → **Data Transformation** and click **Create transformation**
3. Configure the transformation:
   - **Start from scratch**
   - **Destination** → POST: Track users
4. Share the generated webhook URL with Seen, or add it directly to the Journey **Webhook node**
5. Use the following transformation code:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6. Send a test payload to the provided endpoint. Send data to Seen Platform to run your Journey, or send the payload directly to Braze with [Postman](https://www.postman.com/) or another similar service.
7. Select **Validate** to ensure everything works as intended.
8. Select **Save** and **Activate**.