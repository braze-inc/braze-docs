---
nav_title: Messages
article_title: Messaging Endpoints
search_tag: Endpoint
page_order: 3
local_redirect: #app-group-rest-api-key #app-identifier #external-user-id #segment-identifier #campaign-identifier #canvas-identifier #trigger-properties #canvas-identifier #server-responses #fatal-errors #responses-for-tracked-send-ids #messaging-queued #canvas-entry-properties
  app-group-rest-api-key: '/docs/api/basics/#rest-api-key'
  app-identifier: '/docs/api/identifier_types/'
  external-user-id: '/docs/api/objects_filters/user_attributes_object/#braze-user-profile-fields'
  segment-identifier: '/docs/api/identifier_types/'
  campaign-identifier: '/docs/api/identifier_types/'
  canvas-identifier: '/docs/api/identifier_types/'
  send-identifier: '/docs/api/identifier_types/'
  trigger-properties: '/docs/api/objects_filters/trigger_properties_object'
  canvas-entry-properties: '/docs/api/objects_filters/canvas_entry_properties_object'
  server-responses: '/docs/api/errors/'
  messaging-queued: '/docs/api/errors/'
  responses-for-tracked-send-ids: '/docs/api/errors/'
  fatal-errors: '/docs/api/errors/'

layout: dev_guide

#Required
description: "This landing page lists the Braze messaging endpoints."
page_type: landing

guide_top_header: "Messaging Endpoints"
guide_top_text: "The Braze Messaging API provides you with two distinct options for sending messages to your users. You can provide the message contents and configuration in the API request with the <code class='highlighter-rouge'>/messages/send</code> and `/messages/schedule` endpoints. Alternatively, you can manage the details of your message with an API-triggered campaign in the Braze dashboard and control when and to whom it is sent with the `/campaigns/trigger/send` and `/campaigns/trigger/schedule` endpoints. The following sections will detail the request specification for both methods. <br> <br> Similarly to other campaigns, you can limit the number of times a particular user can receive a messaging API campaign by configuring [re-eligibility settings]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/#re-eligibility-with-API-triggered-campaigns) in the Braze dashboard. Braze will not deliver API messages to users that haven't become re-eligible for the campaign regardless of how many API requests are sent. <br> <br> The Send Message endpoints allow you to send immediate messages to designated users. If you are targeting a segment, a record of your request will be stored in the **Message Activity Log**. Use the Schedule Message endpoints to send messages at a designated time, and modify or cancel messages that you have already scheduled."

guide_featured_title: "Schedule messages endpoints"
guide_featured_list:
  - name: "GET: List Upcoming Scheduled Campaigns and Canvases"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Delete Scheduled Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Delete Scheduled API-Triggered Campaigns"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Delete Scheduled API-Triggered Canvases"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Schedule Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: Schedule API-Triggered Campaign Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Schedule API-Triggered Canvas Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Update Scheduled Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Update Scheduled API-Triggered Campaign Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Update Scheduled API-Triggered Canvas Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Send messages endpoints"
guide_menu_list:
  - name: "POST: Create Send IDs"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: Send Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: Send API-Triggered Campaign Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: Send API-Triggered Canvas Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Duplicate message endpoints"
guide_menu_list2:
  - name: "POST: Duplicate Campaigns"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns/
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST: Duplicate Canvases"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases/
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Live Activity endpoints"
guide_menu_list3:
  - name: "POST: Update Live Activity"
    link: /docs/api/endpoints/messaging/live_activity/update/
    image: /assets/img/braze_icons/tablet-01.svg
---
