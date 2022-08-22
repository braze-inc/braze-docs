---
page_order: 0
nav_title: Braze API Explorer
article_title: Braze API Explorer
layout: api_glossary
glossary_top_header: "Braze API Explorer"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or other downloaded reports outside of your Braze account."

page_type: glossary
description: "This glossary defines terms you'll find in your reports in your Braze account."

glossary_tag_name: Endpoint Type
glossary_filter_text: "Select endpoint type to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: User Data
  - name: Send Messages
  - name: Schedule Messages
  - name: Subscription Groups
  - name: Email List and Email Templates
  - name: Campaign
  - name: Canvas
  - name: Segments
  - name: Custom Events
  - name: Content Blocks
  - name: KPI
  - name: News Feed
  - name: Purchases
  - name: SMS


glossaries:
  - name: <a href='/docs/api/endpoints/user_data/post_user_alias/'>/users/alias/new</a>
    description: Use this endpoint to add new user aliases for existing identified users, or to create new unidentified users.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_delete/'>/users/delete</a>
    description: This endpoint allows you to delete any user profile by specifying a known user identifier.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_global_control_group/'>/users/export/global_control_group</a>
    description: This endpoint allows you to export all the users within the Global Control Group.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_identifier/'>/users/export/ids</a>
    description: This endpoint allows you to export data from any user profile by specifying a form of user identifier.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_segment/'>/users/export/segment</a>
    description: This endpoint allows you to export all the users within a segment. 
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/'>/users/external_ids/rename</a>
    description: Use this endpoint to “rename” your users’ external IDs.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/'>/users/external_ids/remove</a>
    description: Use this endpoint to remove your users’ old deprecated external IDs.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_identify/'>/users/identify</a>
    description: Use this endpoint to identify an unidentified (alias-only) user.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_track/'>/users/track</a>
    description: Use this endpoint to record custom events, purchases, and update user profile attributes.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/'>/campaigns/trigger/send</a>
    description: The send endpoint allows you to send immediate, ad-hoc messages to designated users.
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/'>/canvas/trigger/send</a>
    description: This endpoint allows you to send Canvas messages via API-Triggered delivery, allowing you to decide what action should trigger the message to be sent.
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_messages/'>/messages/send</a>
    description: This endpoint allows you send your messages using our API.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids/'>/sends/id/create</a>
    description: Use this endpoint to send messages and track message performance entirely programmatically, without campaign creation for each send.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message/'>/transactional/v1/campaigns/{{CAMPAIGN_ID}}/send</a>
    description: The Send Transactional Email endpoint allows you to send immediate, ad-hoc messages to a designated user.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/'>/campaigns/trigger/schedule/create</a>
    description: Use this endpoint to trigger API-triggered campaigns, which are created on the dashboard and initiated via the API. 
    tags:
      - Schedule Messages 
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/'>/campaigns/trigger/schedule/delete</a>
    description: The delete schedule endpoint allows you to cancel a message that you previously scheduled API-triggered campaigns before it has been sent.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/'>/campaigns/trigger/schedule/update</a>
    description: Use this endpoint to update scheduled API-triggered campaigns, which are created on the dashboard and initiated via the API.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/'>/canvas/trigger/schedule/delete</a>
    description: The delete schedule endpoint allows you to cancel a message that you previously scheduled API-triggered Canvases before it has been sent.
    tags:
      - Schedule Messages 
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/'>/canvas/trigger/schedule/create</a>
    description: Use this endpoint to trigger API-Triggered Canvases, which are created on the dashboard and initiated via the API.
    tags:
      - Schedule Messages   
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/'>/messages/schedule/update</a>
    description: The messages update schedule endpoint accepts updates to either the schedule or messages parameter or both. Your request must contain at least one of those two keys.
    tags:
      - Schedule Messages      
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/'>/messages/schedule/delete</a>
    description: The delete scheduled messages endpoint allows you to cancel a message that you previously scheduled before it has been sent.
    tags:
      - Schedule Messages 
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/'>/messages/schedule/create</a>
    description: Use this endpoint to send messages directly from the API.
    tags:
      - Schedule Messages 
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/'>/canvas/trigger/schedule/update</a>
    description: Use this endpoint to update scheduled API-Triggered Canvases, which are created on the dashboard and initiated via the API.
    tags:
      - Schedule Messages    
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/'>/messages/scheduled_broadcasts</a>
    description: You can view a JSON list of upcoming and scheduled campaigns and Canvases using the following information and parameters. The endpoint will return information about scheduled campaigns and entry Canvases between now and the designated end_time specified in the request. Daily, recurring messages will only appear once with their next occurrence. Results returned in this endpoint are only for campaigns and Canvases created and scheduled in Braze.
    tags:
      - Schedule Messages    
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/'>/subscription/status/set</a>
    description: Use these endpoints to batch update the subscription state of up to 50 users on the Braze dashboard. You can access a subscription group’s subscription_group_id by navigating to the Subscription Group page.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/'>/v2/subscription/status/set</a>
    description: Use this endpoint to update the subscription group status of up to 50 users on the Braze dashboard. You can access a subscription group’s subscription_group_id by navigating to the Subscriptions Group page.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/'>/subscription/status/get</a>
    description: Use these endpoints to get the subscription state of a user in a subscription group. These groups will be available on the Subscription Group page. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call. This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/'>/subscription/user/status</a>
    description: Use these endpoints to list and get the subscription groups of a certain user.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/email/post_blacklist/'>/email/blacklist</a>
    description: Blacklisting an email address will unsubscribe the user from email and mark them as hard bounced.
    tags:
     - Email List and Email Templates
  - name: <a href='/docs/api/endpoints/email/post_remove_hard_bounces/'>/email/bounce/remove</a>
    description: This endpoint allows you to remove email addresses from your Braze bounce list. We will also remove them from the bounce list maintained by your email provider.
    tags:
      - Email List and Email Templates
  - name: <a href='/docs/api/endpoints/email/post_remove_spam/'>/email/spam/remove</a>
    description: This endpoint allows you to remove email addresses from your Braze spam list. We will also remove them from the spam list maintained by your email provider.
    tags:
     - Email List and Email Templates
  - name: <a href='/docs/api/endpoints/email/post_email_subscription_status/'>/email/status</a>
    description: This endpoint allows you to set the email subscription state for your users. Users can be opted_in, unsubscribed, or subscribed (not specifically opted in or out).
    tags:
     - Email List and Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_create_email_template/'>/templates/email/create</a>
    description: Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.
    tags:
     - Email List and Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_update_email_template/'>/templates/email/update</a>
    description: Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.
    tags:
     - Email List and Email Templates
  - name: <a href='/docs/api/endpoints/email/get_list_hard_bounces/'>/email/hard_bounces</a>
    description: This endpoint allows you to pull a list of email addresses that have “hard bounced” your email messages within a certain time frame.
    tags:
     - Email List and Email Templates
  - name: <a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/'>/email/unsubscribes</a>
    description: Use this endpoint to return emails that have unsubscribed during the time period from start_date to end_date. You can use this endpoint to set up a bi-directional sync between Braze and other email systems or your own database.
    tags:
     - Email List and Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information/'>/templates/email/info</a>
    description: Use to get information on your email templates.
    tags:
     - Email List and Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates/'>/templates/email/list</a>
    description: Use this endpoint to get a list of available templates in your Braze account.
    tags:
     - Email List and Email Templates
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics/'>/campaigns/data_series</a>
    description: This endpoint allows you to retrieve a daily series of various stats for a campaign over time. Data returned includes how many messages were sent, opened, clicked, or converted by messaging channel.
    tags:
     - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_details/'>/campaigns/details</a>
    description: This endpoint allows you to retrieve relevant information on a specified campaign, which can be identified by the campaign_id. If you want to retrieve Canvas data, refer to the Canvas Details endpoint.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaigns/'>/campaigns/list</a>
    description: This endpoint allows you to export a list of campaigns, each of which will include its name, campaign API identifier, whether it is an API campaign, and tags associated with the campaign. The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_send_analytics/'>/sends/data_series</a>
    description: This endpoint allows you to retrieve a daily series of various stats for a tracked send_id. Braze stores send analytics for 14 days after the send.
    tags:
      - Campaigns
  - name: <a href='/canvas/get_canvas_analytics/'>/canvas/data_series</a>
    description: This endpoint allows you to export time series data for a Canvas.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/'>/canvas/data_summary</a>
    description: This endpoint allows you to export rollups of time series data for a Canvas, providing a concise summary of a Canvas’ results.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_details/'>/canvas/details</a>
    description: This endpoint allows you to export metadata about a Canvas, such as the name, time created, current status, and more.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvases/'>/canvas/list</a>
    description: This endpoint allows you to export a list of Canvases, including the name, Canvas API identifier and associated tags. Canvases are returned in groups of 100 sorted by time of creation (oldest to newest by default).
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_analytics/'>/segments/data_series</a>
    description: This endpoint allows you to retrieve a daily series of the estimated size of a segment over time for a segment.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_details/'>/segments/details</a>
    description: This endpoint allows you to retrieve relevant information on the segment, which can be identified by the segment_id.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment/'>/segments/list</a>
    description: This endpoint allows you to export a list of segments, each of which will include its name, Segment API Identifier, and whether it has analytics tracking enabled. The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/sessions/get_sessions_analytics/'>/sessions/data_series</a>
    description: This endpoint allows you to retrieve a series of the number of sessions for your app over a designated time period.
    tags:
      - Sessions
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics/'>/events/data_series</a>
    description: This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events/'>/events/list</a>
    description: This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/'>/content_blocks/create</a>
    description: This endpoint will create an Email Content Block.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/'>/content_blocks/update</a>
    description: Use this endpoint to update an Email Content Block.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/'>/content_blocks/info</a>
    description: This endpoint will call information for your existing Email Content Blocks.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/'>/content_blocks/list</a>
    description: This endpoint will list your existing Content Blocks information.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date/'>/kpi/dau/data_series</a>
    description: This endpoint allows you to retrieve a daily series of the total number of unique active users on each date.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/'>/kpi/mau/data_series</a>
    description: This endpoint allows you to retrieve a daily series of the total number of unique active users over a 30-day rolling window.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/messaging/export/kpi/get_kpi_daily_new_users_date/'>/kpi/new_users/data_series</a>
    description: This endpoint allows you to retrieve a daily series of the total number of new users on each date.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/'>/kpi/uninstalls/data_series</a>
    description: This endpoint allows you to retrieve a daily series of the total number of uninstalls on each date.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/news_feed/get_news_feed_card_analytics/'>/feed/data_series</a>
    description: This endpoint allows you to retrieve a daily series of engagement stats for a card over time.
    tags:
      - News Feed
  - name: <a href='/docs/api/endpoints/export/news_feed/get_news_feed_card_details/'>/feed/details</a>
    description: This endpoint allows you to retrieve relevant information on the card, which can be identified by the card_id.
    tags:
      - News Feed
  - name: <a href='/docs/api/endpoints/export/news_feed/get_news_feed_cards/'>/feed/list</a>
    description: This endpoint allows you to export a list of News Feed cards, each of which will include its name and Card API Identifier. The cards are returned in groups of 100 sorted by time of creation (oldest to newest by default).
    tags:
      - News Feed
  - name: <a href='/docs/api/endpoints/sms/post_remove_invalid_numbers/'>/sms/invalid_phone_numbers/remove</a>
    description: This endpoint allows you to remove “invalid” phone numbers from Braze’s invalid list. This can be used to re-validate phone numbers after they have been marked as invalid.
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/sms/get_query_invalid_numbers/'>/sms/invalid_phone_numbers</a>
    description: This endpoint allows you to pull a list of phone numbers that have been deemed “invalid” within a certain time frame.
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/export/purchases/get_list_product_id/'>/purchases/product_list</a>
    description: This endpoint returns paginated lists of product IDs.
    tags:
      - Purchases
---