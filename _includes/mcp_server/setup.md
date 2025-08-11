# Setting up Braze MCP server

> Learn how to set up Braze MCP server, so you can interact with your Braze data using natural-language tools like Claude and Cursor. For more general information, see [Braze MCP server]({{site.baseurl}}/developer_guide/mcp_server/).

{% multi_lang_include mcp_server/beta_alert.md %}

## Prerequisites

Before you start, you'll need the following:

| Prerequisite | Description |
|--------------|-------------|
| MCP Client | Currently, only [Claude](https://claude.ai/) and [Cursor](https://cursor.com/) are supported. You'll need an account for one of these clients to use Braze MCP server. |
| Braze REST Endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
| Braze API Key | A Braze API key with the required permissions. You'll create a new key when you [set up your Braze MCP server](#create-api-key). |
| Terminal | A terminal app so you can run commands and install tooling. Use your preferred terminal app or the one that's pre-installed on your computer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Setting up Braze MCP server

### Step 1: Create API key {#create-api-key}

Braze MCP server supports 38 read-only endpoints that do not typically return Personally Identifiable Information (PII) data. Go to **Settings** > **APIs and Identifiers** > **API Keys** and create a new key with some or all the following permissions.

{% details List of read-only, non-PII permissions %}
#### Campaigns

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Canvas

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Catalogs

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Cloud Data Ingestion

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Content Blocks

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Custom Attributes

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Events

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### KPIs

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Messages

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Preference Center

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Purchases

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Segments

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Sessions

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### SDK Authentication Keys

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Subscription

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Templates

| Endpoint | Required API Key Scope |
|----------|------------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% enddetails %}

{% alert warning %}
Do not reuse an existing API key&#8212;create one specifically for your MCP client. Additionally, only assign read-only, non-PII permissions, as agents may try to write or delete data in Braze.
{% endalert %}

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

{% alert tip %}
For more information, refer to [Astral's UV documentation](https://docs.astral.sh/uv/getting-started/installation/).
{% endalert %}

### Step 3: Configure your MCP client {#configure-client}

Next, configure your MCP client using our pre-provided configuration file.

{% tabs local %}
{% tab Claude %}
1. In [Claude Desktop](https://claude.ai/download), go to **Settings** > **Developer** > **Edit Config**, then add the following snippet:
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
2. Save the configuration and restart Claude Desktop.
3. To verify your connection, try asking a question like "List my Braze campaigns".
{% endtab %}

{% tab Cursor %}
1. In [Cursor](https://cursor.com/), go to **Settings** > **Cursor Settings** > **MCP Tools** > **Add Custom MCP**, then add the following snippet:
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
2. When you're finished, save the configuration and restart Cursor.
3. To verify your connection, try using the provided MCP tools to interact with your Braze data.
{% endtab %}
{% endtabs %}

## Troubleshooting

### Terminal errors

#### `uvx` command not found

If you receive an error that `uvx` command not found, reinstall `uv` and restart your terminal.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` error

If you receive a `spawn uvx ENOENT` errors, you may need to update the filepath in your client's config file. First, open your terminal and run the following command:

```bash
which uvx
```

The command should return a message similar to the following:

```bash
/Users/alex-lee/.local/bin/uvx
```

Copy the message to your clipboard and open [your client's config file](#configure-client). Replace `"command": "uvx"` with the path you copied, then restart your client. For example:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### Package installation fails

If your package installation fails, try installing a specific Python version instead.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Client configuration

#### MCP client can't find the Braze server

1. Verify your MCP client configuration syntax is correct.
2. Restart your MCP client after configuration changes.
3. Check that `uvx` is in your system PATH.

#### Authentication errors

1. Verify your `BRAZE_API_KEY` is correct and active.
2. Ensure your `BRAZE_BASE_URL` matches your Braze instance.
3. Check that your API key has the [correct permissions](#create-api-key).

#### Connection timeouts or network errors

1. Verify your `BRAZE_BASE_URL` is correct for your instance
2. Check your network connection and firewall settings
3. Ensure you're using HTTPS in your base URL

{% multi_lang_include mcp_server/legal_disclaimer.md %}
