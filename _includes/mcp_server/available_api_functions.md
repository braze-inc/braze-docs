# Braze MCP server functions

> The Braze MCP server exposes a set of read-only API functions that map to specific Braze REST API endpoints. MCP clients like Claude and Cursor can call these functions to retrieve data without accessing PII or making changes to your workspace. For more general information, see [Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Prerequisites

Before you can use this feature, you'll need to [set up the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Available Braze API Functions

These are the API functions that your MCP client references to interact with The Braze MCP server:

### General functions

| Function | Description |
|----------|-------------|
| `list_functions` | Lists all available Braze API functions with their descriptions and parameters |
| `call_function` | Calls a specific Braze API function with provided parameters |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Campaigns

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Export a list of campaigns with metadata. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Get detailed information about specific campaigns. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Retrieve time series analytics data for campaigns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Canvases

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Export a list of Canvases with metadata. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | Get detailed information about specific Canvases. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | Get summary analytics for Canvas performance. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Retrieve time series analytics data for Canvases. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Catalogs

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | Return a list of catalogs in a workspace. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | Return multiple catalog items and their content with pagination support. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | Return a specific catalog item and its content by ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Cloud Data Ingestion

| Function | Endpoint | Description |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | Return a list of existing CDI integrations. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | Return past sync statuses for a given CDI integration. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Content Blocks

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | List your available content blocks. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | Get information on your content blocks. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Custom Attributes

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | Export custom attributes recorded for your app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Events

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | Export a list of custom events recorded for your app. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | Retrieve time series data for custom events. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | Get detailed event data with pagination support. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### KPIs

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | Daily series of new user counts. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | Daily Active Users time series data. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | Monthly Active Users time series data. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | App uninstall time series data. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Messages

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | List upcoming scheduled campaigns and Canvases. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Preference Centers

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | List your available preference centers. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | View details for a specific preference center including HTML content and options. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Purchases

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | Export paginated list of product IDs. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | Revenue analytics time series data. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | Purchase quantity time series data. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Segments

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Export list of segments with analytics tracking status. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Time series analytics data for segments. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | Detailed information about specific segments. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Sends

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | Daily analytics for tracked campaign sends. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Sessions

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | Time series data for app session counts. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### SDK Authentication Keys

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | List all SDK Authentication keys for your app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Subscription

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | List and get the subscription groups of a certain user. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | Get the subscription state of a user in a subscription group. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

### Templates

| Function | Endpoint | Description |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | List your available email templates. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Get information on your email templates. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
