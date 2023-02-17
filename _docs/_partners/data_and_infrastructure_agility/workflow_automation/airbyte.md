---
nav_title: Airbyte
article_title: Airbyte
description: "The Braze and Airbyte integration allows brands to map the audience segments (or custom attributes) across both platforms or forward real-time events from Airbyte to Braze to deliver personalized customer experiences based on the entire breadth of their customer data."
alias: /partners/actioniq/
page_type: partner
search_tag: Airbyte

---

# Airbyte
[Airbyte](https://airbyte.com/) is an open-source data integration engine that helps you consolidate your data in your data warehouses, lakes, and databases.

The Braze and Airbyte integration allows users to create a data pipeline that enables you to collect and analyze Braze data by connecting all of your applications and databases to a central warehouse. Once data has been collected in the central warehouse, data teams can explore Braze data effectively using their preferred business intelligence tools.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Airbyte account | An Airbyte account is required to take advantage of this integration. |
| Braze REST API key | A Braze REST API key with all permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### For Airbyte Cloud
1. Log into your [Airbyte Cloud](https://cloud.airbyte.io/workspaces) account.
2. In the left navigation bar, click **Sources**. In the top-right corner, click **+ New Source**.
3. On the **Set up the source** page, enter the name for the Braze connector and select **Braze** from the source type dropdown.
4. Fill in your URL, REST API key, and start date, and then click **Set Up Source**.

### Supported sync modes
Airbyte’s Braze source connector supports the following [sync modes](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):
- Full Refresh | Overwrite
- Incremental Sync | Append

## Supported streams
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

## Performance considerations

Rate limits differ depending on the stream.
Rate limits table: https://www.braze.com/docs/api/api_limits/#rate-limits-by-request-type