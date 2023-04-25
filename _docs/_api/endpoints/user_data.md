---
nav_title: User Data
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
guide_top_text: "The User API allows you to track information on your users by logging data about your users that comes from outside your mobile app. You can also use this API to delete users for testing or other purposes. <br> <br> All API endpoints have a data payload limit of 4&nbsp;MB. Attempts to post more data than 4&nbsp;MB will fail with an HTTP 413 Request Entity Too Large. <br> <br> The following examples contain the URL https://rest.iad-01.braze.com, but some customers will need to use a different endpoint URL, for example if you are hosted in Braze's EU data center or have a dedicated Braze installation. Your Success Manager will inform you if you should use a different endpoint URL."

guide_featured_title: "User Data Endpoints"
guide_featured_list:
  - name: "POST: Create a New User Alias"
    link: /docs/api/endpoints/user_data/post_user_alias/
    fa_icon: fas fa-user
  - name: "POST: Update a User Alias"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    fa_icon: fas fa-user-edit
  - name: "POST: Delete User Data"
    link: /docs/api/endpoints/user_data/post_user_delete/
    fa_icon: fas fa-user-minus
  - name: "POST: Identify a User"
    link: /docs/api/endpoints/user_data/post_user_identify/
    fa_icon: fas fa-user-circle
  - name: "POST: Track Users"
    link: /docs/api/endpoints/user_data/post_user_track/
    fa_icon: fas fa-database
  - name: "POST: Merge Users"
    link: /docs/api/endpoints/user_data/post_users_merge/
    fa_icon: fas fa-users

guide_menu_title: "External ID Migration Endpoints"
guide_menu_list:
  - name: "POST: Rename External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    fa_icon: fas fa-user
  - name: "POST: Remove Deprecated External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    fa_icon: fas fa-user-minus
---
