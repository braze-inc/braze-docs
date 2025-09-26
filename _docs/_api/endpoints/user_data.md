---
nav_title: User data
article_title: User Data Endpoints
search_tag: Endpoint
page_order: 9

local_redirect: #event-object-specification #purchase-object-specification
  event-object-specification: '/docs/api/objects_filters/event_object/'
  purchase-object-specification: '/docs/api/objects_filters/purchase_object/'

layout: dev_guide

#Required
description: "This landing page lists the Braze user data endpoints."
page_type: landing

guide_top_header: "User Data Endpoints"
guide_top_text: "The Braze User Data endpoints allow you to track information on your users by logging data about your users that comes from outside your mobile app. You can also use this API to delete users for testing or other purposes. <br> <br> All API endpoints have a data payload limit of 4&nbsp;MB. Attempts to post more data than 4&nbsp;MB will fail with an HTTP 413 Request Entity Too Large. <br> <br> The examples in this section contain the URL https://rest.iad-01.braze.com, but you may need to use a different endpoint URL (for example, if you are hosted in the Braze EU data center or have a dedicated Braze installation). Your Braze customer success manager will inform you if you should use a different endpoint URL."

guide_featured_title: "User Data Endpoints"
guide_featured_list:
  - name: "POST: Create a New User Alias"
    link: /docs/api/endpoints/user_data/post_user_alias/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Update a User Alias"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Delete User Data"
    link: /docs/api/endpoints/user_data/post_user_delete/
    image: /assets/img/braze_icons/user-minus-01.svg
  - name: "POST: Identify a User"
    link: /docs/api/endpoints/user_data/post_user_identify/
    image: /assets/img/braze_icons/user-circle.svg
  - name: "POST: Track Users"
    link: /docs/api/endpoints/user_data/post_user_track/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: Track Users (Synchronous)"
    link: /docs/api/endpoints/user_data/post_user_track_synchronous/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: Merge Users"
    link: /docs/api/endpoints/user_data/post_users_merge/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title: "External ID migration endpoints"
guide_menu_list:
  - name: "POST: Rename External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Remove Deprecated External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
