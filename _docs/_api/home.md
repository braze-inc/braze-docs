---
page_order: 0
nav_title: Home
article_title: Braze API Guide
layout: api_glossary
glossary_top_header: "Braze API Guide"
glossary_top_text: "Braze provides a high-performance REST API to allow you to track users, send messages, export data, and more. This page lists available Braze API endpoints and their uses."
page_type: glossary
description: "This landing page lists available Braze API endpoints and their uses."
glossary_tag_name: Endpoint Type

glossary_filter_text: "Select endpoint type to narrow the glossary:"

glossary_mid_text: "Endpoint Search"
guide_featured_list:
  - name: API Overview
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics/
  - name: API Identifier Types
    link: /docs/api/identifier_types/
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: Objects & Filters
    link: /docs/api/objects_filters/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Errors & Responses
    link: /docs/api/errors/
    image: /assets/img/braze_icons/list.svg
  - name: Data Retention
    link: /docs/api/data_retention/
    image: /assets/img/braze_icons/laptop-02.svg
  - name: Rate Limits
    link: /docs/api/api_limits/
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: Campaigns
  - name: Canvas
  - name: Catalogs
  - name: Content Blocks
  - name: Custom Events
  - name: Email List
  - name: Email Templates
  - name: KPI
  - name: Purchases
  - name: Preference Center
  - name: Schedule Messages
  - name: SCIM
  - name: SDK Authentication
  - name: Segments
  - name: Send Messages
  - name: SMS
  - name: Subscription Groups
  - name: User Data
  - name: Live Activity
  - name: Cloud Data Ingestion

glossaries:
  - name: <a href='/docs/api/endpoints/user_data/post_user_alias/'>/users/alias/new</a>
    description: Add new user aliases for existing identified users, or to create new unidentified users.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_alias_update/'>/users/alias/update</a>
    description: Update existing user alias names to new user alias names.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_delete/'>/users/delete</a>
    description: Delete any user profile by specifying a known user identifier.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_global_control_group/'>/users/export/global_control_group</a>
    description: Export all users within a Global Control Group.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_identifier/'>/users/export/ids</a>
    description: Export data from any user profile by specifying a user identifier.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_segment/'>/users/export/segment</a>
    description: Export all the users within a segment.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/'>/users/external_ids/rename</a>
    description: Rename your users' external IDs.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/'>/users/external_ids/remove</a>
    description: Remove your users' old deprecated external IDs.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_identify/'>/users/identify</a>
    description: Identify an unidentified (alias-only) user.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_track/'>/users/track</a>
    description: Record custom events, purchases, and update user profile attributes.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_merge/'>/users/merge</a>
    description: Merge a user profile into another user.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/'>/campaigns/trigger/send</a>
    description: Send immediate, one-off messages to designated users through API-triggered delivery.
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/'>/canvas/trigger/send</a>
    description: Send Canvas messages through API-Triggered delivery.
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_messages/'>/messages/send</a>
    description: Send immediate, one-off messages to designated users through the Braze API.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids/'>/sends/id/create</a>
    description: Create send IDs to use for sending messages and tracking message performance programmatically, without campaign creation for each send.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message/'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>
    description: Send immediate, one-off transactional messages to a designated user.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/'>/campaigns/trigger/schedule/create</a>
    description: Send dashboard created campaign messages through API-triggered delivery.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/'>/campaigns/trigger/schedule/delete</a>
    description: Cancel API-triggered campaign messages that you previously scheduled before it has been sent.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/'>/campaigns/trigger/schedule/update</a>
    description: Update scheduled API-triggered campaigns created in the dashboard.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/'>/canvas/trigger/schedule/delete</a>
    description: Cancel a Canvas message that you previously scheduled via API-triggered before it has been sent.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/'>/canvas/trigger/schedule/create</a>
    description: Schedule Canvas messages through API-triggered delivery.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/'>/messages/schedule/update</a>
    description: Update scheduled messages. This endpoint accepts updates to either the <code>schedule</code> or <code>messages</code> parameter or both.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/'>/messages/schedule/delete</a>
    description: Cancel a message that you previously scheduled before it has been sent.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/'>/messages/schedule/create</a>
    description: Schedule a campaign, Canvas, or other message to be sent at a designated time.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/'>/canvas/trigger/schedule/update</a>
    description: Update scheduled API-triggered Canvases you created in the dashboard.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/'>/messages/scheduled_broadcasts</a>
    description: Return a JSON list of information about scheduled campaigns and entry Canvases between now and a designated <code>end_time</code> specified in the request.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/live_activity/update/'>/messages/live_activity/update</a>
    description: Update an iOS Live Activity.
    tags:
      - Live Activity
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/'>/subscription/status/set</a>
    description: Batch update the subscription state of up to 50 users on the Braze dashboard.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/'>/v2/subscription/status/set</a>
    description: Batch update the subscription state of up to 50 users on the Braze dashboard.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/'>/subscription/status/get</a>
    description: Get the subscription state of a user in a subscription group.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/'>/subscription/user/status</a>
    description: List and get the subscription groups of a certain user.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/email/post_blacklist/'>/email/blacklist</a>
    description: Unsubscribe a user from email and mark them as hard bounced.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_hard_bounces/'>/email/bounce/remove</a>
    description: Remove email addresses from your Braze bounce list.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_spam/'>/email/spam/remove</a>
    description: Remove email addresses from your Braze spam list.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_email_subscription_status/'>/email/status</a>
    description: Set the email subscription state for your users.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_create_email_template/'>/templates/email/create</a>
    description: Create email templates on the Braze dashboard.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_update_email_template/'>/templates/email/update</a>
    description: Update email templates on the Braze dashboard.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/email/get_list_hard_bounces/'>/email/hard_bounces</a>
    description: Pull a list of email addresses that have "hard bounced" your email messages within a certain time frame.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/'>/email/unsubscribes</a>
    description: Return emails that have unsubscribed during the time period from <code>start_date</code> to <code>end_date</code>.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information/'>/templates/email/info</a>
    description: Get information on your email templates.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates/'>/templates/email/list</a>
    description: Get a list of available email templates in your Braze account.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics/'>/campaigns/data_series</a>
    description: Retrieve a daily series of various stats for a campaign over time.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_details/'>/campaigns/details</a>
    description: Retrieve relevant information on a specified campaign.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaigns/'>/campaigns/list</a>
    description: Export a list of campaigns, each of which will include its name, campaign API identifier, whether it is an API campaign, and tags associated with the campaign.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_send_analytics/'>/sends/data_series</a>
    description: Retrieve a daily series of various stats for a tracked <code>send_id</code>.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics/'>/canvas/data_series</a>
    description: Export time series data for a Canvas.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/'>/canvas/data_summary</a>
    description: Export rollups of time series data for a Canvas, providing a concise summary of a Canvas' results.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_details/'>/canvas/details</a>
    description: Export metadata about a Canvas, such as the name, time created, current status, and more.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvases/'>/canvas/list</a>
    description: Export a list of Canvases, including the name, Canvas API identifier and associated tags.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_analytics/'>/segments/data_series</a>
    description: Retrieve a daily series of the estimated size of a segment over time.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_details/'>/segments/details</a>
    description: Retrieve relevant information on a segment.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment/'>/segments/list</a>
    description: Export a list of segments, each of which will include its name, Segment API identifier, and whether it has analytics tracking enabled.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/post_cancel_export/'>/export/segment/cancel</a>
    description: Cancel exports for the provided segment ID.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/sessions/get_sessions_analytics/'>/sessions/data_series</a>
    description: Retrieve a series of the number of sessions for your app over a designated time period.
    tags:
      - Sessions
  - name: <a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes/'>/custom_attributes</a>
    description: Export a list of custom attributes including the name, description, data type, array length (if applicable), status, and associated tags.
    tags:
      - Custom Attributes
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics/'>/events/data_series</a>
    description: Retrieve a series of the number of occurrences of a custom event in your app over a designated time period.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_data/'>/events</a>
    description: Export a list of custom events including the name, description, status, associated tags, and analytics report inclusion.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events/'>/events/list</a>
    description: Export a list of names of custom events recorded for your app.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/'>/content_blocks/create</a>
    description: Create an email Content Block.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/'>/content_blocks/update</a>
    description: Update an email Content Block.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/'>/content_blocks/info</a>
    description: Call information for your existing email Content Block.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/'>/content_blocks/list</a>
    description: List your existing Content Blocks information.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date/'>/kpi/dau/data_series</a>
    description: Retrieve a daily series of the total number of unique active users on each date.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/'>/kpi/mau/data_series</a>
    description: Retrieve a daily series of the total number of unique active users over a 30-day rolling window.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/'>/kpi/new_users/data_series</a>
    description: Retrieve a daily series of the total number of new users on each date.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/'>/kpi/uninstalls/data_series</a>
    description: Retrieve a daily series of the total number of uninstalls on each date.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/sms/post_remove_invalid_numbers/'>/sms/invalid_phone_numbers/remove</a>
    description: Remove "invalid" phone numbers from the invalid list in Braze. Use this to re-validate phone numbers after Braze marks them as invalid.
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/sms/get_query_invalid_numbers/'>/sms/invalid_phone_numbers</a>
    description: Pull a list of phone numbers that Braze marked as "invalid" within a certain time frame.
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/export/purchases/get_list_product_id/'>/purchases/product_list</a>
    description: Return a paginated lists of product IDs.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_number_of_purchases/'>/purchases/quantity_series</a>
    description: Return the total number of purchases in your app over a time range.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_revenue_series/'>/purchases/revenue_series</a>
    description: Return the total money spent in your app over a time range.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>
    description: Create a URL for a preference center.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_list_preference_center/'>/preference_center/v1/list</a>
    description: List available preference centers.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: View the details for your preference center, including when it was created and updated.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>
    description: Create a preference center to allow users to manage their notification preferences for email campaigns.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: Update a preference center.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: Delete multiple items in your catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: List a catalog item and its details.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>
    description: Edit multiple items in your catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>
    description: Create multiple items in your catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/'>/catalogs/{catalog_name}</a>
    description: Delete a catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/'>/catalogs</a>
    description: Create a catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/'>/catalogs</a>
    description: List the catalogs in a workspace.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Create an item in a catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Edit an item in a catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/'>/catalogs/{catalog_name}/items</a>
    description: Return multiple catalog items and their content.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Delete an item in a catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Replace an item in a catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/'>/catalogs/{catalog_name}/items/</a>
    description: Replace multiple items in a catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields/'>/catalogs/{catalog_name}/fields/</a>
    description: Create multiple fields in a catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field/'>/catalogs/{catalog_name}/fields/{field_name}</a>
    description: Delete a field from a catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections/'>/catalogs/{catalog_name}/selections</a>
    description: Create a selection in a catalog.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection/'>/catalogs/{catalog_name}/selections/{selection_name}</a>
    description: Delete a catalog selection.
    tags:
      - Catalogs
  - name: <a href='/docs/post_create_user_account/'>/scim/v2/Users</a>
    description: Create a new dashboard user account by specifying email, given and family names, permissions (for setting permissions at the company, workspace, and team level).
    tags:
      - SCIM
  - name: <a href='/docs/get_see_user_account_information/'>/scim/v2/Users/{id}</a>
    description: Look up an existing dashboard user account by specifying their resource ID.
    tags:
      - SCIM
  - name: <a href='/docs/post_update_existing_user_account/'>/scim/v2/Users/{id}</a>
    description: Update an existing dashboard user account by specifying email, given and family names, permissions (for setting permissions at the company, workspace, and team level).
    tags:
      - SCIM
  - name: <a href='/docs/delete_existing_dashboard_user/'>/scim/v2/Users/{id}</a>
    description: Permanently delete an existing dashboard user.
    tags:
      - SCIM
  - name: <a href='/docs/get_search_existing_dashboard_user_email/'>/scim/v2/Users?filter={userName@example.com}</a>
    description: Look up an existing dashboard user account by specifying their email.
    tags:
      - SCIM
  - name: <a href='/docs/api/endpoints/cdi/get_integration_list/'>/cdi/integrations</a>
    description: Return a list of existing integrations.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/post_job_sync/'>/cdi/integrations/{integration_id}/sync</a>
    description: Trigger a sync for a given integration.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/get_job_sync_status/'>/cdi/integrations/{integration_id}/job_sync_status</a>
    description: Return a list of sync statuses.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/'>/app_group/sdk_authentication/create</a>
    description: Create a new SDK Authentication key for your app.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys/'>/app_group/sdk_authentication/keys</a>
    description: List SDK Authentication keys for your app.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/'>/app_group/sdk_authentication/primary</a>
    description: Set an SDK Authentication key as the primary key for your app.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key/'>/app_group/sdk_authentication/delete</a>
    description: Delete an SDK Authentication key for your app.
    tags:
      - SDK Authentication
---