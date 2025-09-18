---
nav_title: "API overview"
article_title: API Overview
page_order: 2.1
description: "This reference article covers the API basics including what a REST API is, the terminology, and an overview of API keys."
page_type: reference
alias: /api/api_key/
---

# API overview

> This reference article covers the API basics, including common terminology and an overview of REST API keys, permissions, and how to keep them secure.

## Braze REST API collection

| Collection                                                                 | Purpose                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Catalogs]({{site.baseurl}}/api/endpoints/catalogs/)                       | Create and manage catalogs and catalog items to reference in your Braze campaigns.    |
| [Cloud Data Ingestion]({{site.baseurl}}/api/endpoints/cdi/)                | Manage your data warehouse integrations and syncs.                                    |
| [Email lists and addresses]({{site.baseurl}}/api/endpoints/email/)         | Set up and manage bi-directional sync between Braze and your email systems.           |
| [Export]({{site.baseurl}}/api/endpoints/export/)                           | Access and export various details of your campaigns, Canvases, KPIs, and more.        |
| [Messages]({{site.baseurl}}/api/endpoints/messaging/)                      | Schedule, send, and manage your campaigns and Canvases.                               |
| [Preference center]({{site.baseurl}}/api/endpoints/preference_center/)     | Build your preference center and update the styling of it.                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | Manage user identities in cloud-based applications and services.                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | Manage your users' phone numbers in your subscription groups.                         |
| [Subscription groups]({{site.baseurl}}/api/endpoints/subscription_groups/) | List and update both SMS and email subscription groups stored in the Braze dashboard. |
| [Templates]({{site.baseurl}}/api/endpoints/templates/)                     | Create and update templates for email messaging and Content Blocks.                   |
| [User data]({{site.baseurl}}/api/endpoints/user_data/)                     | Identify, track, and manage your users.                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## API definitions

The following is an overview of terms you may see in the Braze REST API documentation.

### Endpoints

Braze manages a number of different instances for our dashboard and REST endpoints. When your account is provisioned you will log in to one of the following URLs. Use the correct REST endpoint based on which instance you are provisioned to. If you are unsure, open a [support ticket]({{site.baseurl}}/braze_support/) or use the following table to match the URL of the dashboard you use to the correct REST Endpoint.

{% alert important %}
When using endpoints for API calls, use the REST endpoint.

For SDK integration, use the [SDK endpoint]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), not the REST endpoint.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='instances' %}

### API limits

For most APIs, Braze has a default rate limit of 250,000 requests per hour. However, certain request types have their own rate limit applied to better handle high volumes of data across our customer base. For details, refer to [API rate limits]({{site.baseurl}}/api/api_limits/)

### User IDs

- **External user ID**: The `external_id` serves as a unique user identifier for whom you are submitting data. This identifier should be the same as the one you set in the Braze SDK in order to avoid creating multiple profiles for the same user.
- **Braze user ID**: `braze_id` serves as a unique user identifier that is set by Braze. This identifier can be used to delete users through the REST API in addition to external_ids.

For more information, refer to the following articles based on your platform: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/), and [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/).

## About REST API keys

A REST Application Programming Interface key (REST API key) is a unique code that is passed into an API to authenticate the API call and identify the calling application or user. API access is done using HTTPS web requests to your company's REST API endpoint. We use REST API keys at Braze in tandem with our App Identifier keys to track, access, send, export, and analyze data to help make sure everything is running smoothly on both your and our end.

Workspaces and API keys go hand in hand at Braze. Workspaces are designed to house versions of the same application across multiple platforms. Many customers also use workspaces to contain free and premium versions of their applications on the same platform. As you may notice, these workspaces are also making use of the REST API and have their own REST API keys. These keys can be individually scoped to include access to specific endpoints on the API. Each call to the API must include a key with access to the endpoint hit.

We refer to both the REST API key and workspace API key as the `api_key`. The `api_key` is included in each request as a request header and acts as an authentication key that allows you to use our REST APIs. These REST APIs are used to track users, send messages, export user data, and more. When you create a new REST API key, you will need to give it access to specific endpoints. By assigning specific permissions to an API key, you can limit exactly which calls an API key can authenticate.

![REST API keys panel on the API Keys tab.]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
In addition to REST API keys, there also exists a type of key called Identifier keys that can be used to reference specific things like apps, templates, Canvases, campaigns, Content Cards, and segments from the API. For more information, refer to [API identifier types]({{site.baseurl}}/api/identifier_types/).
{% endalert %}

### Creating REST API keys

To create a new REST API key:

1. Go to **Settings** > **APIs and Identifiers**.
2. Select **Create API Key**.
3. Give your new key a name for identification at a glance.
4. Specify [allowlisted IP addresses](#api-ip-allowlisting) and subnets for the new key.
5. Select which [permissions](#rest-api-key-permissions) you want to be associated with your new key.

{% alert important %}
Keep in mind that after you create a new API key, you cannot edit the scope of permissions or the allowlisted IPs. This limitation is in place for security reasons. If you need to change the scope of a key, create a new key with the updated permissions and implement that key in place of the old one. After you've completed your implementation, you can delete the old key.
{% endalert %}

### REST API key permissions

API key permissions are permissions you can assign a user or group to limit their access to certain API calls. To view your list of API key permissions, go to **Settings** > **APIs and Identifiers**, and select your API key.

{% tabs %}
{% tab User Data %}

| Permission | Endpoint | Description |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | Record user attributes, custom events, and purchases. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | Delete any user. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |Create a new alias for an existing user. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |Identify an alias-only user with an external ID. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |Query for user profile information by user ID. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |Query for user profile information by segment. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | Merges two existing users into each other. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | Change the external ID for an existing user. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | Remove the external ID for an existing user. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | Update an alias for an existing user. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | Query for user profile information in the Global Control Group. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

 {% endtab %}
 {% tab Email %}

| Permission | Endpoint | Description |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | Query for unsubscribed email addresses.  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | Change email address status. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | Query for hard bounced email addresses. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | Remove email addresses from your hard bounce list. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | Remove email addresses from your spam list. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | Blocklist email addresses. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Messages %}

| Permission | Endpoint | Description |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | Send an immediate message to specific users. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | Schedule a message to be sent at a specific time. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | Update a scheduled message. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | Delete a scheduled message. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | Query all scheduled broadcast messages. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | Update an iOS Live Activity. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Campaigns %}

| Permission | Endpoint | Description |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | Trigger the sending of an existing campaign. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | Schedule a future send of a campaign with API-triggered delivery. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | Update a campaign scheduled with API-triggered delivery. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |Delete a campaign scheduled with API-triggered delivery. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | Query for a list of campaigns. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Query for campaign analytics over a time range. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | Query for details of a specific campaign. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | Query for message send analytics over a time range. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | Create send ID for message blast tracking. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | Query for URL details of a specific message variation within a campaign. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | Allows for ability to send transactional messaging using the Transactional messaging endpoint. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Permission | Endpoint | Description |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | Trigger the sending of an existing Canvas. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | Schedule a future send of a Canvas with API-triggered delivery. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | Update a Canvas scheduled with API-triggered delivery. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| Delete a Canvas scheduled with API-triggered delivery. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |  Query for a list of Canvases. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Query for Canvas analytics over a time range. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | Query for details of a specific Canvas. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Query for rollups of Canvas analytics over a time range. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | Query for URL details of a specific message variation within a Canvas step. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Segments %}

| Permission | Endpoint | Description |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | Query for a list of segments. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Query for segment analytics over a time range. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | Query for details of a specific segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Purchases %}

| Permission | Endpoint | Description |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | Query for a list of products purchased in your app. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | Query for total money spent per day in your app over a time range. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | Query for the total number of purchases per day in your app over a time range. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Events %}

| Permission | Endpoint | Description |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | Query for a list of custom events. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | Query occurrences of a custom event over a time range. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Sessions %}

| Permission | Endpoint | Description |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | Query for sessions per day over a time range. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab KPIs %}

| Permission | Endpoint | Description |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |  Query for unique active users per day over a time range. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Query for total unique active users over a 30-day rolling window over a time range. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | Query for new users per day over a time range. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | Query for app uninstalls per day over a time range. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Templates %}

| Permission | Endpoint | Description |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | Create a new email template on the dashboard. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Query for information of a specific template. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Query for a list of email templates. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | Update an email template stored on the dashboard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SSO %}

| Permission | Description |
|---|---|---|
| `sso.saml.login` | Set up identity provider-initiated login. For more information, refer to [Service Provider (SP) initiated login]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Content Blocks %}

| Permission | Endpoint | Description |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | Query for information of a specific template. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | Query for a list of Content Blocks. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | Create a new Content Block on the dashboard. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | Update an existing Content Block on the dashboard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Preference Center %}

| Permission | Endpoint | Description |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Get a preference center. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | List preference centers. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | Create or update a preference center. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Get a preference center link for a user. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Subscription %}

| Permission | Endpoint | Description |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | Set subscription group status. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | Get subscription group status. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | Get status of subscription groups that specific users are explicitly subscribed and unsubscribed to. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SMS %}

| Permission | Endpoint | Description |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | Query for invalid phone numbers. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | Remove the invalid phone number flag from users. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Catalogs %}

| Permission | Endpoint | Description |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | Add multiple items to an existing catalog. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | Update multiple items in an existing catalog. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | Delete multiple items from an existing catalog. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | Get a single item from an existing catalog. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Update a single item in an existing catalog. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | Create a single item in an existing catalog. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | Delete a single item from an existing catalog. |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Replace a single item from an existing catalog. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | Create a catalog. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | Get a list of catalogs |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | Delete a catalog. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | Get items preview from an existing catalog. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | Replace items in an existing catalog. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SDK Authentication %}

| Permission | Endpoint | Description |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | Create a new SDK Authentication key for your app. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/) | Mark an SDK Authentication key as the primary key for your app. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | Delete an SDK Authentication key for your app. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Get all SDK Authentication keys for your app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### Managing REST API keys

You can view details for or delete existing REST API keys from **Settings** > **APIs and Identifiers** > **API Keys** tab. Note that REST API keys cannot be edited after they're created.

The **API Keys** tab includes the following information for each key:

| Field        | Description                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| API Key Name | The name given to the key upon creation.                                                                            |
| Identifier   | The API key.                                                                                                        |
| Created By   | The email address of the user who created the key. This field will show as "N/A" for keys created before June 2023. |
| Date Created | The date this key was created.                                                                                      |
| Last Seen    | The date this key was last used. This field will show as "N/A" for keys that have never been used.                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

To view the details of an API key, hover over the key and select <i class="fa-solid fa-eye" alt="View"></i> **View**. This includes all the permissions this key has, whitelisted IPs (if any), and if this key is opted into Braze IP whitelisting.

![The list of API key permissions in the Braze dashboard.]({% image_buster /assets/img_archive/view-api-key.png %})

Note when [deleting a user]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/), the associated API keys a user created won't be deleted. To delete a key, hover over the key and select <i class="fa-solid fa-trash-can" alt="Delete"></i> **Delete**.

![An API key named 'Last Seen' with the trash icon highlighted, showing 'Delete'.]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### REST API key security

API keys are used to authenticate an API call. When you create a new REST API key, you need to give it access to specific endpoints. By assigning specific permissions to an API key, you can limit exactly which calls an API key can authenticate.

Given that REST API keys allow access to potentially sensitive REST API endpoints, secure these keys and only share them with trusted partners. They should never be publicly exposed. For example, do not use this key to make AJAX calls from your website or expose it in any other public manner.

A good security practice is to assign a user only as much access as is necessary to complete their job: this principle can also be applied to API keys by assigning permissions to each key. These permissions give you better security and control over the different areas of your account.

{% alert warning %}
Given that REST API keys allow access to potentially sensitive REST API endpoints, make sure they are stored and used securely. For example, do not use this key to make AJAX calls from your website or expose it in any other public manner.
{% endalert %}

If accidental exposure of a key occurs, it can be deleted from the Developer Console. For help with this process, open a [support ticket]({{site.baseurl}}/braze_support/).

### API IP allowlisting

For additional security, you can specify a list of IP addresses and subnets which are allowed to make REST API requests for a given REST API key. This is referred to as allowlisting, or whitelisting. To allow specific IP addresses or subnets, add them to the **Whitelist IPs** section when creating a new REST API key:

![Option to allowlist IPs when creating an API key.]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

If you don't specify any, requests can be sent from any IP address.

{% alert tip %}
Making a Braze-to-Braze webhook and using allowlisting? Check out our list of [IPs to whitelist]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

## Additional resources

### Ruby client library

If you're implementing Braze using Ruby, you can use our [Ruby client library](https://github.com/braze-inc/braze-api-client-ruby) to reduce your data import time. A client library is a collection of code specific to one programming language—in this case, Ruby—that makes it easier to use an API.

The Ruby client library supports the [User endpoints]({{site.baseurl}}/api/endpoints/user_data).

{% alert important %}
This client library is currently in beta. Want to help us make this library better? Send us feedback at [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}

