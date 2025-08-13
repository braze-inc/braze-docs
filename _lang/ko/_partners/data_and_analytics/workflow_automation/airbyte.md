---
nav_title: Airbyte
article_title: Airbyte
description: "This reference article covers the Braze and Airbyte integration. Airbyte is an open-source data integration engine that helps you consolidate your data in your data warehouses, lakes, and databases, forwarding real-time events from Airbyte to Braze."
alias: /partners/airbyte/
page_type: partner
search_tag: Airbyte

---

# Airbyte

> [Airbyte](https://airbyte.com/) is an open-source data integration engine that helps you consolidate your data in your data warehouses, lakes, and databases.

_This integration is maintained by Airbyte._

## About the integration

The Braze and Airbyte integration allows users to create a data pipeline to collect and analyze Braze data by connecting all of your applications and databases to a central warehouse. After data has been collected in the central warehouse, data teams can explore Braze data effectively using their preferred business intelligence tools.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Airbyte Cloud account | An [Airbyte Cloud](https://cloud.airbyte.io/workspaces) account is required to take advantage of this integration. |
| Braze REST API key | A Braze REST API key with all permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

1. In your Airbyte Cloud account, navigate to **Sources > + New Source > Set up the Source**.
2. Enter "Braze" as the source name and select **Braze** from the source dropdown.
3. Provide your endpoint URL, Braze REST API key, and start date. Click **Set up Source**.

### Supported sync modes

Airbyte's Braze source connector supports the following [sync modes](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):
- **Full Refresh | Overwrite**: sync all records from the source and replace data in the destination by overwriting it.
- **Incremental Sync | Append**: Sync new records from the source and add them to the destination without deleting any data.

### Supported streams

- [`campaigns`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18)
- [`campaigns_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1)
- [`canvases`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1)
- [`canvases_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73)
- [`events`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1)
- [`events_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c)
- [`kpi_daily_new_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01)
- [`kpi_daily_active_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986)
- [`kpi_daily_app_uninstalls`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae)
- [`cards`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e)
- [`cards_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8)
- [`segments`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f)
- [`segments_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e)

{% alert note %}
Rate limits differ depending on the stream. Visit the [rate limits table]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type) for more information.
{% endalert %}
