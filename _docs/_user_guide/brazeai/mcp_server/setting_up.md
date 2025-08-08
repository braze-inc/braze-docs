---
nav_title: Setting up Braze MCP server
article_title: Setting Braze MCP server
description: "Learn how to set up Braze MCP server."
---

# Setting up Braze MCP server

> Learn how to set up Braze MCP server.

{% multi_lang_include mcp_server/beta_alert.md %}

## Prerequisites

Before you start, you'll need the following:

| Prerequisite | Description |
|--------------|-------------|
| MCP Client | An MCP client to connect with Braze. Recommended options: Claude Desktop (marketers) or Cursor (technical roles). |
| Base URL | Your REST endpoint URL, available on your API key page in the Braze dashboard. |
| API Key | A Braze API key with the required permissions. You'll create a new key when you [set up your Braze MCP server](#create-api-key). |
| Terminal | DESCRIPTION. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Setting up Braze MCP server

### Step 1: Create API key {#create-api-key}

{% alert warning %}
Do not reuse an existing API key. Create one specifically for your AI tool and limit scopes to prevent write or delete access.
{% endalert %}

In the Braze dashboard, go to **Settings** > **API Keys** and create a new key with the following permissions:

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Step 2: Install `uv`

You'll need to install `uv`, a tool for dependency management and Python package handling. To install, open your terminal and run the following command:

{% tabs local %}
{% tab MacOS and Linux %}
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
{% endtab %}

{% tab Windows %}
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
{% endtab %}
{% endtabs %}

For more information, refer to [Astral's UV documentation](https://docs.astral.sh/uv/getting-started/installation/).

### Step 3: Configure your MCP client

{% tabs local %}
{% tab Claude %}
{% alert note %}
If you haven't already, [download Claude](https://claude.ai/download).
{% endalert %}

Open Claude Desktop. Within Settings > Developer > Edit Config, add the following, substituting your API key and base URL:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key-here",
        "BRAZE_BASE_URL": "https://rest.iad-01.braze.com"
      }
    }
  }
}
```

Save the configuration and restart Claude Desktop.

Verify the connection by asking a question like "List my Braze campaigns".
{% endtab %}

{% tab Cursor %}
{% alert note %}
If you haven't already, [download Cursor](https://cursor.com/).
{% endalert %}

Open Cursor. Within Settings > Cursor Settings > MCP Tools > Add Custom MCP, add the following configuration:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key-here",
        "BRAZE_BASE_URL": "https://rest.iad-01.braze.com"
      }
    }
  }
}
```

Save the configuration and restart Cursor.

Verify the connection by using the MCP tools to interact with your Braze data.
{% endtab %}
{% endtabs %}

## Troubleshooting

CONTENT.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
