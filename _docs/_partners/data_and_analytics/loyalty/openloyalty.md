---
nav_title: Open Loyalty
article_title: Open Loyalty
description: "The Braze and Open Loyalty integration allows you to sync loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time."
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Open Loyalty

> [Open Loyalty](https://www.openloyalty.io/) is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user's loyalty status changes.

_This integration is maintained by Open Loyalty_

## About the integration

This integration uses Braze Data Transformations to capture webhooks from Open Loyalty and map them to Braze user profiles.

* **Real-time Updates**: Push loyalty events (points earned, tier upgrades) to Braze.
* **Personalization**: Use loyalty attributes (current balance, next tier name) in your Braze templates.
* **Bi-directional**: Update Open Loyalty customer custom attributes based on Braze engagement data.

## Use cases

This integration covers the following data flows:

1. **Syncing Events to Braze (Inbound)**: Track point changes, tier upgrades, or reward redemptions by sending data from Open Loyalty to Braze. Data Transformation converts this data into a User Event.
2. **Modifying Open Loyalty Members (Outbound)**: Automatically update member data in Open Loyalty based on user behavior in Braze, such as adding "VIP" labels or updating custom attributes.

## Prerequisites

Before you start, you need the following:

| Requirement | Description |
| :--- | :--- |
| Open Loyalty account | You need an Admin account on an Open Loyalty Tenant to take advantage of this partnership. |
| Open Loyalty REST API Key | An Open Loyalty REST API Key (for integrations that send data from Braze to Open Loyalty). <br><br> Create this in **Settings > Admins > API Keys**. |
| Braze REST API Key | A Braze REST API key with `users.track` permissions. <br><br> Create this key in the Braze dashboard from **Settings** > **API Keys**. |
| Braze Data Transformation | You need access to the "Data Settings" tab in Braze to configure webhook listeners. |
| Matching IDs | The user's `external_id` in Braze must match their `loyaltyCardNumber` (or another default identifier) in Open Loyalty. |
| Tenant ID | Your Open Loyalty Tenant ID (required for Outbound updates). |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integration

The primary integration syncs Open Loyalty webhook events to Braze using Data Transformation.

### Step 1: Generate the Webhook URL in Braze

First, create a data transformation in Braze to generate a unique URL for receiving data.

1.  In Braze, open **Data Settings > Data Transformation**.
2.  Click **Create Transformation**.
3.  Complete the following fields:
     * **Transformation name**: Provide a descriptive name (for example, "Open Loyalty Point Update Events").
     * **Select destination**: Choose **POST: Track users**.
4.  Click **Create Transformation**.
5.  Locate the **Webhook URL** on the right side and click **Copy**.

{% alert important %}
Keep this URL safe; you need it for the next step.
{% endalert %}

### Step 2: Create the Webhook Subscription in Open Loyalty

Tell Open Loyalty to send specific events to the URL you just generated.

1.  Log in to your Open Loyalty Admin Panel.
2.  Navigate to **General > Webhooks**.
3.  Click **Add new webhook** and configure the subscription:
    * **eventName**: Select the event you want to track (for example, `AvailablePointsAmountChanged`, `CustomerLevelChanged`, or `CampaignEffectWasApplied`).
    * **url**: Paste the Braze Webhook URL from Step 1.
    * Add the following headers:
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  Save the webhook subscription.

### Step 3: Configure the Data Transformation

Write the JavaScript logic in Braze to map the incoming Open Loyalty payload to Braze properties.

1.  In Braze, open the data transformation you created in Step 1.
2.  Trigger the event in Open Loyalty (for example, change a member's points or assign a tier) to generate a sample payload in the **Webhook details** pane.
3.  In the **Transformation code** editor, write a script to map the incoming data. Use the following example as a guide:

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,
     
      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",
     
      // timestamp
      "time": new Date().toISOString(),
     
      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4. Click **Validate** to ensure the code runs against your sample payload, then click **Activate**.


## Using Open Loyalty with Braze

After you complete the inbound integration, configure **Outbound Updates** to modify Open Loyalty members based on Braze behavior.

### Step 1: Configure Braze Webhook Campaign

This process uses Braze Webhooks to send a `PATCH` request to the Open Loyalty Member API (for example, to add a "VIP" label).

1.  In Braze, create a new **Webhook Campaign** (or use a Webhook within a Canvas).
2.  Click **Compose Webhook**.
3.  **Webhook URL**: Construct the URL using your Open Loyalty instance, Tenant ID, and the Braze Liquid variable for the user ID.
    * Format:
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. Complete the following fields:   
    * **Request Method**: `PATCH`
    * **Request Headers**:
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **Request Body**: Select `Raw text` and paste the payload:

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### Step 2: Configure the Trigger

1.  Navigate to the **Delivery** or **Entry Schedule** tab.
2.  Complete the following fields:
    * **Delivery Method**: Action-Based.
    * **Trigger**: Define the relevant trigger (for example, a user enters a specific Segment in Braze).
    * **Launch**: Activate the campaign.

## Troubleshooting

### Verify Inbound Events
When the Data Transformation is active, data appears in Braze as a custom event. Verify this by creating a campaign with a **Perform Custom Event** trigger and checking if your defined event (for example, `Loyalty Event Triggered`) is available.

### Verify Outbound Webhooks
Check the Message Activity Log in Braze to ensure the webhook returned a `200 OK` status.
* **401 Error**: Check your Open Loyalty API Token.
* **404 Error**: The user ID in Braze does not exist in Open Loyalty.