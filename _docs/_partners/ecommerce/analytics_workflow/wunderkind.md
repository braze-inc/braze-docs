---
nav_title: Wunderkind
article_title: Wunderkind
description: "This reference article outlines the partnership between Braze and Wunderkind, that allows you to analyze the performance lift and identify more anonymous users, significantly scaling 1:1 messages sent via Braze and contacts added directly to Braze."
alias: /partners/wunderkind/
page_type: partner
search_tag: Partner

---

# Wunderkind

> [Wunderkind](https://www.wunderkind.co) is an eCommerce performance platform that uses proprietary Identity technology to recognize anonymous website visitors and resolve them to actionable email addresses. On average, Wunderkind scales identification from 3–5% of website traffic to 40–60%, enabling brands to trigger personalized, one-to-one messages at scale through their existing ESP.

*This integration is maintained by Wunderkind. For support, visit [support.wunderkind.co](https://support.wunderkind.co).*

---

## About the Signals Integration

The Wunderkind Signals integration allows high-intent behavioral signals — such as cart abandonment, product abandonment, and price drops — to trigger real-time Canvas journeys in Braze. Wunderkind identifies anonymous users on your website, resolves their identity to a deliverable email address, and delivers a structured signal payload to Braze via the Canvas Entry API, initiating your pre-configured email flows automatically.

All Wunderkind signals are prefixed with `WKND_` so they are easily identifiable in the Braze Canvas trigger dropdown and do not conflict with your native Braze events.

---

## Prerequisites

| Requirement | Description |
|---|---|
| Wunderkind account | A Wunderkind account with Signals enabled is required. Contact your Wunderkind representative to confirm eligibility. |
| Braze account | A Braze account with Canvas access is required. |
| Braze REST API key | You will create a dedicated API key with specific permissions during setup (see Step 1 below). |
| Email-keyed user profiles | Wunderkind keys profiles by email address using a `user_alias` with `alias_label: "wknd_email_id"`. Your Braze workspace must support profile creation and upsert by email. |

---

## How it Works

When Wunderkind identifies a high-intent anonymous user and resolves their identity, it initiates the following API sequence before triggering your Canvas:

1. **Profile check** — Wunderkind calls `users/export/ids` to check whether each recipient already has a Braze `user_alias` keyed by `wknd_email_id`.
2. **Alias creation (if needed)** — If no alias exists, Wunderkind calls `/users/alias/new` to create one, followed by a `/users/track` call to associate the alias with the user's email address.
3. **Processing buffer** — A brief pause is introduced to allow Braze to fully process the user updates before the Canvas send is triggered.
4. **Canvas send** — Wunderkind calls `/canvas/trigger/send` with the full signal payload, triggering the relevant Canvas journey for that user.

This sequence ensures that every recipient is correctly profiled in Braze before a message is sent, preventing delivery failures due to missing user aliases.

---

## Integration Setup

### Step 1: Create a Braze API key for Wunderkind

In your Braze dashboard:

1. Navigate to **Settings > API Keys** and click **Create New API Key**.
2. Give the key a descriptive name (e.g., `Wunderkind Signals`).
3. Grant the following permissions:

| Permission | Purpose |
|---|---|
| `users.export.ids` | Check for existing user aliases before send |
| `users.alias.new` | Create `wknd_email_id` aliases for new users |
| `users.track` | Associate aliases with user email addresses |
| `canvas.trigger.send` | Trigger Canvas entries with signal payloads |

4. Copy the API key — you will enter it in the Wunderkind platform in the next step.

> **Note:** Braze does not support OAuth for external integrations. A manually created REST API key is required.

### Step 2: Connect Braze to the Wunderkind platform

1. Log into the Wunderkind platform and navigate to **Integrations Hub**.
2. Select the **Braze** tile and click **Connect**.
3. Enter your Braze REST API key and your Braze instance endpoint URL (e.g., `https://rest.iad-01.braze.com`).
4. Define your conversion event — this single metric will be used across all Wunderkind-powered Canvas flows for attribution reporting.
5. Click **Activate**.

Upon activation, Wunderkind will automatically provision the required internal campaign objects and map them to the appropriate Braze Canvas IDs.

### Step 3: Review new Braze assets

After activation, Wunderkind creates the following assets in your Braze account:

- **Canvases** — One pre-configured, API-triggered Canvas per active signal type (see canvas types below), named with the `WKND_` prefix.
- **Segments** — Eligibility segments used by each Canvas to manage suppression and re-entry logic.
- **Tags** — Wunderkind-specific tags applied to all created assets for easy filtering.

Review these assets in your Braze dashboard before proceeding to Canvas setup.

### Step 4: Complete Canvas setup

For each active Canvas:

1. Open the Canvas in Braze and navigate to the **Message** step(s).
2. Build your email template using Braze's drag-and-drop editor or HTML. Wunderkind populates product and session data via `canvas_entry_properties` at send time — reference these using Liquid (see [Canvas entry properties](#canvas-entry-properties) below).
3. Configure your send timing, re-eligibility window, and exit criteria per your strategy.
4. Ensure the Canvas entry type is set to **API-triggered**.

### Step 5: Review Canvas eligibility

Before launching, confirm the following for each Canvas:

- The Canvas **entry audience** does not conflict with existing suppression segments in Braze (e.g., recent purchasers, global unsubscribes).
- Re-entry settings align with your desired send cadence. Wunderkind recommends disabling re-entry within a 72-hour window per signal type to avoid over-messaging.
- Each Canvas is set to **active** and not in draft mode.

### Step 6: Test and launch

Wunderkind will conduct end-to-end QA in a staging environment before go-live:

- Confirm signals are delivering to the correct Canvas IDs without API errors.
- Verify `canvas_entry_properties` (product name, image URL, deep link) are populating correctly in rendered email templates.
- Validate that user profiles are being created or updated as expected via the alias flow.
- Confirm data is flowing back to Wunderkind via Braze Currents for reporting.

Once QA passes, your Wunderkind implementation manager will coordinate the production launch with your team.

---

## Canvas Entry Properties

Wunderkind supports six signal types. Each delivers a distinct payload to its corresponding Canvas. The `WkPurpose` field identifies the signal type within the payload.

### Common fields (all canvas types)

| Property | Type | Description |
|---|---|---|
| `Origin` | String | Always `"wunderkind"` |
| `DataOnly` | String | Always `"Y"` — indicates Wunderkind is acting as a data layer only; Braze executes the send |
| `UserType` | String | `"prospect"` or `"customer"` |
| `WkChannel` | String | Always `"email"` for this integration |
| `WkPurpose` | String | Signal type identifier (see values per canvas below) |
| `WkOpen` | String | URL to deep-link the user back to their session |
| `WKCouponCode` | String | Coupon code, if applicable (empty string if not used) |
| `WKCouponPurpose` | String | Description of coupon offer (empty string if not used) |
| `Items[]` | Array | Array of product objects (see product fields below) |

### Product item fields

| Property | Type | Description |
|---|---|---|
| `WkCopy` | String | Product name |
| `WkId` | String | Product ID |
| `WkImageUrl` | String | Product image URL |
| `WkUrl` | String | Product detail page URL |
| `WkPrice` | String | Original price (price drop canvas only) |
| `WKSalePrice` | String | Sale price (price drop canvas only) |
| `WkQuantity` | String | Units remaining (low stock canvas only) |

### Canvas-specific fields and `WkPurpose` values

| Canvas type | `WkPurpose` value | Additional fields |
|---|---|---|
| Cart abandonment | `"cart abandonment"` | `WkCartReplenUrl` — URL to replenish the cart |
| Product abandonment | `"product abandonment"` | — |
| Category recap | `"category recap"` | `WkCategoryUrl` — URL to the browsed category |
| Back in stock | `"back in stock"` | — |
| Price drop | `"price drop"` | `WkPrice`, `WKSalePrice` on each item |
| Low stock | `"low stock"` | `WkQuantity` on each item |

### Example payloads

#### Cart abandonment

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "email": "user@example.com",
      "canvas_entry_properties": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/cart",
        "WkPurpose": "cart abandonment",
        "WkChannel": "email",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCartReplenUrl": "https://example.com/cart/replenish",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```

#### Product abandonment

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "email": "user@example.com",
      "canvas_entry_properties": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WkChannel": "email",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```

#### Category recap

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "email": "user@example.com",
      "canvas_entry_properties": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/category",
        "WkPurpose": "category recap",
        "WkChannel": "email",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCategoryUrl": "https://example.com/category",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```

#### Back in stock

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "email": "user@example.com",
      "canvas_entry_properties": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "back in stock",
        "WkChannel": "email",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```

#### Price drop

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "email": "user@example.com",
      "canvas_entry_properties": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "price drop",
        "WkChannel": "email",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkPrice": "49.99",
            "WKSalePrice": "39.99"
          }
        ]
      }
    }
  ]
}
```

#### Low stock

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "email": "user@example.com",
      "canvas_entry_properties": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "low stock",
        "WkChannel": "email",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkQuantity": "1"
          }
        ]
      }
    }
  ]
}
```

### Example Liquid usage

When Wunderkind calls `/canvas/trigger/send`, every field inside `canvas_entry_properties` in the payload becomes available in your Braze email template via the `canvas_entry_properties` Liquid object. This is standard Braze behavior — no additional configuration is required to access these fields in a message step.

The examples below show how to reference the most common fields. Note that `WkPurpose`, `WkOpen`, and `Items[]` are present in all signal types, while fields like `WkPrice`, `WKSalePrice`, and `WkQuantity` are exclusive to specific canvas types (see [Canvas-specific fields](#canvas-specific-fields-and-wkpurpose-values) above).

#### Rendering the first product

```liquid
{% assign first_item = canvas_entry_properties.Items[0] %}

<a href="{{ canvas_entry_properties.WkOpen }}">
  <img src="{{ first_item.WkImageUrl }}" alt="{{ first_item.WkCopy }}" />
  <p>{{ first_item.WkCopy }}</p>
</a>
```

| Liquid reference | Payload field | Notes |
|---|---|---|
| `canvas_entry_properties.WkOpen` | `WkOpen` | Deep-link URL returning the user to their session |
| `first_item.WkImageUrl` | `Items[0].WkImageUrl` | Product image URL |
| `first_item.WkCopy` | `Items[0].WkCopy` | Product name |

#### Rendering canvas-specific fields conditionally

Because all six canvas types share a common template structure but carry different payload fields, use `WkPurpose` as a conditional gate to render signal-specific content only when the relevant data is present. This allows a single Braze email template to serve multiple signal types without outputting blank values.

```liquid
{% if canvas_entry_properties.WkPurpose == "price drop" %}
  <p>Was: {{ first_item.WkPrice }} — Now: {{ first_item.WKSalePrice }}</p>
{% endif %}

{% if canvas_entry_properties.WkPurpose == "low stock" %}
  <p>Only {{ first_item.WkQuantity }} left in stock!</p>
{% endif %}

{% if canvas_entry_properties.WkPurpose == "cart abandonment" %}
  <a href="{{ canvas_entry_properties.WkCartReplenUrl }}">Restore your cart</a>
{% endif %}

{% if canvas_entry_properties.WkPurpose == "category recap" %}
  <a href="{{ canvas_entry_properties.WkCategoryUrl }}">Continue browsing</a>
{% endif %}
```

#### Looping through multiple products

The `Items[]` array can contain up to four products. Use a `for` loop to render all available items rather than referencing each by index.

```liquid
{% for item in canvas_entry_properties.Items %}
  <div>
    <a href="{{ item.WkUrl }}">
      <img src="{{ item.WkImageUrl }}" alt="{{ item.WkCopy }}" />
      <p>{{ item.WkCopy }}</p>
    </a>

    {% if canvas_entry_properties.WkPurpose == "price drop" %}
      <p>Was: {{ item.WkPrice }} — Now: {{ item.WKSalePrice }}</p>
    {% endif %}

    {% if canvas_entry_properties.WkPurpose == "low stock" %}
      <p>Only {{ item.WkQuantity }} left in stock!</p>
    {% endif %}
  </div>
{% endfor %}
```

---

## Reporting

Wunderkind ingests performance data from Braze using **Braze Currents**, which streams raw events to Google Cloud Storage. Wunderkind then normalizes and aggregates these events against the originating signal for 1:1 attribution reporting.

The following metrics are available in the Wunderkind reporting dashboard:

| Metric | Source |
|---|---|
| Delivered sends | Braze Currents |
| Email opens | Braze Currents |
| Clicks | Braze Currents |
| Conversions | Braze Currents (event defined at setup) |
| Unsubscribes | Braze Currents |

> Braze Currents setup is handled by your Wunderkind implementation manager during onboarding.

---

## Important limitations

- **No suppression/opt-out sync.** Email opt-out and suppression lists are not automatically synced between platforms. Suppression must be managed natively in Braze.
- **Single conversion metric.** Only one conversion event can be defined per Braze workspace connection.
- **Email channel only.** SMS is not currently supported through this integration.
- **New user profile processing.** For users without an existing `wknd_email_id` alias, Wunderkind creates the alias and allows Braze a brief processing window before triggering the Canvas send to ensure reliable delivery.

---

## Additional resources

| Resource | Link |
|---|---|
| Wunderkind Developer Portal — Integration Overview | [developer.wunderkind.co](https://developer.wunderkind.co/docs/integration-overview) |
| Braze API: Canvas trigger send | [braze.com/docs](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases) |
| Braze API: User alias | [braze.com/docs](https://www.braze.com/docs/api/endpoints/user_data/post_user_alias) |
| Braze API: User track | [braze.com/docs](https://www.braze.com/docs/api/endpoints/user_data/post_user_track) |
| Braze API: Export user by identifier | [braze.com/docs](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier) |
| Braze Currents documentation | [braze.com/docs](https://www.braze.com/docs/user_guide/data/distribution/braze_currents) |
