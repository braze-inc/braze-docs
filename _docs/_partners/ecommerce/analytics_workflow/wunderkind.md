# Wunderkind (Signals)

> [Wunderkind](https://www.wunderkind.co) is an eCommerce performance platform that uses proprietary Identity technology to recognize anonymous website visitors and resolve them to actionable email addresses. On average, Wunderkind scales identification from 3–5% of website traffic to 40–60%, enabling brands to trigger personalized, one-to-one messages at scale through their existing ESP.

*This integration is maintained by Wunderkind. For support, visit [support.wunderkind.co](https://support.wunderkind.co).*

---

## About the integration

The Wunderkind Signals integration allows high-intent behavioral signals — such as cart abandonment, product abandonment, and price drops — to trigger real-time Canvas journeys in Braze. Wunderkind identifies anonymous users on your website, resolves their identity to a deliverable email address, and delivers a structured signal payload to Braze via the Canvas Entry API, initiating your pre-configured email flows automatically.

---

## Prerequisites

| Requirement | Description |
|---|---|
| Wunderkind account | A Wunderkind account with Signals enabled is required. Contact your Wunderkind representative to confirm eligibility. |
| Braze account | A Braze account with Canvas access is required. The Wunderkind team must be granted a seat in your account. See full details [here](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account). |
| Braze REST API key | You will create a dedicated API key with specific permissions during setup (see Step 1 below). |
| Email-keyed user profiles | Wunderkind keys profiles by email address using a `user_alias` with `alias_label: "wknd_email_id"`. Your Braze workspace must support profile creation and upsert by email. |

---

## How it works

When Wunderkind identifies a high-intent anonymous user and resolves their identity, it initiates the following API sequence before triggering your Canvas:

1. **Profile check** — Wunderkind calls `users/export/ids` to check whether each recipient already has a Braze `user_alias` keyed by `wknd_email_id`.
2. **Alias creation (if needed)** — If no alias exists, Wunderkind calls `/users/alias/new` to create one, followed by a `/users/track` call to associate the alias with the user's email address.
3. **Processing buffer** — A brief pause is introduced to allow Braze to fully process the user updates before the Canvas send is triggered.
4. **Canvas send** — Wunderkind calls `/canvas/trigger/send` with the full signal payload, triggering the relevant Canvas journey for that user.

This sequence ensures that every recipient is correctly profiled in Braze before a message is sent, preventing delivery failures due to missing user aliases.

---

## Integration setup

This integration is maintained by Wunderkind. To see the full implementation guide, visit [support.wunderkind.co](https://support.wunderkind.co).

### Step 1: Create a Braze API key for Wunderkind

In your Braze dashboard:

1. Navigate to **Settings > API Keys** and click **Create New API Key**.
2. Give the key a descriptive name (e.g., `Wunderkind Signals`).
3. Grant the permissions listed on [this page](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account).
4. Copy the API key — you will enter it in the Wunderkind platform in the next section.

> **Note:** Braze does not support OAuth for external integrations. A manually created REST API key is required.

### Step 2: Connect Braze to the Wunderkind platform

1. Log into the Wunderkind platform and navigate to **Integrations Hub**.
2. Select the **Braze** tile and click **Connect**.
3. Enter your Braze REST API key and select your cluster.
4. Click **Save**.

### Step 3: Review new Braze assets

Upon activation, Wunderkind will provision new implementation assets in your Braze workspace based on the strategy aligned on with your Wunderkind representative:

| Asset type | Wunderkind creation method |
|---|---|
| Content Blocks | Automatic |
| API-Triggered Canvases | Managed Service |
| Tags, Custom Attributes, Link Templates | Managed Service |

### Step 4: Complete Canvas setup

For each Signals Canvas, build your email templates using Braze's drag-and-drop editor or HTML.

- Wunderkind populates product and session data via `canvas_entry_properties` at send time.
- For in-depth instructions on how to leverage Liquid to display Wunderkind's Canvas entry properties, see our [Help Center article](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup).

### Step 5: Review Canvas eligibility

For each Signals Canvas, go to the **Target Audience** settings to review Wunderkind's default Entry Audience and Exit Criteria.

- To ensure that you are not messaging your users too often, see Braze's documentation on [user-centric rate limiting](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/).
- We recommend adjusting settings to prevent users from continuing to receive Canvas messages after they make a purchase. For example, add the exception **Make Purchase**.
- Certain Signals Canvases are pre-configured with Custom Attribute Filters to ensure users always receive the highest-intent message possible.
- See Wunderkind's [Help Center article](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility) for details on Canvas eligibility and priority.

### Step 6: Test and launch

Wunderkind will conduct end-to-end QA before go-live:

- Confirm signals are delivering to the correct Canvas IDs without API errors.
- Verify `canvas_entry_properties` (product name, image, URL) are populating correctly in rendered email templates.
- See Wunderkind's [Help Center article](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze) for instructions on previewing templates with mock Wunderkind products.

Once QA passes, your Wunderkind implementation manager will coordinate the production launch with your team.

---

## Canvas entry properties

Wunderkind supports six signal types. Each delivers a distinct payload to its corresponding Canvas. The `WkPurpose` field identifies the signal type within the payload.

### Common fields (all canvas types)

| Property | Type | Description |
|---|---|---|
| `Origin` | String | Always `"wunderkind"` |
| `DataOnly` | String | Always `"Y"` — indicates Wunderkind is acting as a data layer only; Braze executes the send |
| `UserType` | String | `"prospect"` or `"customer"` |
| `WkChannel` | String | Always `"email"` for this integration |
| `WkPurpose` | String | Signal type identifier (see values per Canvas below) |
| `WKCouponCode` | String | Coupon code, if applicable (empty string if not used) |
| `WKCouponPurpose` | String | Description of coupon offer (empty string if not used) |
| `Items[]` | Array | Array of product objects (see product fields below) |
| `WkOpen` | String | Tracking pixel available for reporting purposes |

### Product item fields

| Property | Type | Description |
|---|---|---|
| `WkCopy` | String | Product name |
| `WkId` | String | Product ID |
| `WkImageUrl` | String | Product image URL |
| `WkUrl` | String | Product detail page URL |
| `WkPrice` | String | Original price (price drop Canvas only) |
| `WKSalePrice` | String | Sale price (price drop Canvas only) |
| `WkQuantity` | String | Units remaining (low stock Canvas only) |

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

The example below shows how to loop through Wunderkind products and reference common fields:

```liquid
{% for item in {{canvas_entry_properties.${Items}}} %}
  <tr>
    <td>
      <a href="{{ item.WkUrl }}">
        <img src="{{ item.WkImageUrl }}" />
        <p>{{ item.WkCopy }}</p>
      </a>
    </td>
  </tr>
{% endfor %}
```

---

## Reporting (Coming Soon)

Wunderkind ingests performance data from Braze using **Braze Currents**, which streams raw events to Google Cloud Storage. Wunderkind then normalizes and aggregates these events against the originating signal for 1:1 attribution reporting.

The following metrics will be available soon in the Wunderkind reporting dashboard:

| Metric | Source |
|---|---|
| Delivered sends | Braze Currents |
| Email opens | Braze Currents |
| Clicks | Braze Currents |
| Conversions | Braze Currents (event defined at setup) |
| Unsubscribes | Braze Currents |

---

## Important limitations

- **No suppression/opt-out sync.** Suppression must be managed natively in Braze. Note: For existing Wunderkind clients migrating onto Braze Signals, Wunderkind will work with your team to preserve your current setup.
- **Email channel only.** SMS is not currently supported through this integration.
- **New user profile processing.** For users without an existing `wknd_email_id` alias, Wunderkind creates the alias and allows Braze a brief processing window before triggering the Canvas send to ensure reliable delivery.

---

## Additional resources

| Resource | Link |
|---|---|
| Wunderkind Help Center — Signals for Braze Overview | [support.wunderkind.co](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview) |
| Wunderkind Developer Portal — Integration Overview | [developer.wunderkind.co](https://developer.wunderkind.co/docs/integration-overview) |
| Braze API: Canvas trigger send | [braze.com/docs](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases) |
| Braze API: User alias | [braze.com/docs](https://www.braze.com/docs/api/endpoints/user_data/post_user_alias) |
| Braze API: User track | [braze.com/docs](https://www.braze.com/docs/api/endpoints/user_data/post_user_track) |
| Braze API: Export user by identifier | [braze.com/docs](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier) |
| Braze Currents documentation | [braze.com/docs](https://www.braze.com/docs/user_guide/data/distribution/braze_currents) |
