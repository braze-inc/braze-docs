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
---
