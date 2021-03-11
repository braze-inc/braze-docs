---
nav_title: Messaging
page_order: 2
local_redirect: #parameter-definitions #app-group-rest-api-key #app-identifier #external-user-id #segment-identifier #campaign-identifier #canvas-identifier #trigger-properties #canvas-identifier #server-responses #fatal-errors #responses-for-tracked-send-ids #messaging-queued #canvas-entry-properties
  parameter-definitions: '/docs/api/parameters/'
  app-group-rest-api-key: '/docs/api/parameters/'
  app-identifier: '/docs/api/parameters/'
  external-user-id: '/docs/api/parameters/'
  segment-identifier: '/docs/api/parameters/'
  campaign-identifier: '/docs/api/parameters/'
  canvas-identifier: '/docs/api/parameters/'
  send-identifier: '/docs/api/parameters/'
  trigger-properties: '/docs/api/parameters/'
  canvas-entry-properties: '/docs/api/parameters/'
  server-responses: '/docs/api/errors/'
  messaging-queued: '/docs/api/errors/'
  responses-for-tracked-send-ids: '/docs/api/errors/'
  fatal-errors: '/docs/api/errors/'


layout: dev_guide

#Required
description: "This landing page explains and lists the Braze Messaging Endpoints."
page_type: landing
tool:
  - Canvas
  - Campaigns

#Use if applicable
platform:
  - API
channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

guide_top_header: "Messaging Endpoints"
guide_top_text: "The Braze messaging API provides you with two distinct options for sending messages to your users. You can provide the message contents and configuration in the API request with the <code class='highlighter-rouge'>/messages/send</code> and `/messages/schedule` endpoints. Alternatively, you can manage the details of your message with an API-Triggered Delivery campaign in the dashboard and just control when and to whom it is sent with the `campaigns/trigger/send` and `campaigns/trigger/schedule` endpoints. The following sections will detail the request specification for both methods. <br> <br> Similarly to other campaigns, you can limit the number of times a particular user can receive a Messaging API campaign by configuring [re-eligibility settings](/docs/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/api_triggered_delivery/#re-eligibility-with-api-triggered-campaigns) in the Braze Dashboard. Braze will not deliver API messages to users that haven't become re-eligible for the campaign regardless of how many API requests are sent. <br> <br> The Send endpoints allow you to send immediate, ad-hoc messages to designated users. If you are targeting a segment, a record of your request will be stored in the Developer Console. The Schedule endpoints allow you to send messages at a designated time and modify or cancel messages that you have already scheduled."

guide_featured_title: "Schedule Messages Endpoints"
guide_featured_list:
  - name: "GET: List Upcoming Scheduled Campaigns and Canvases"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    fa_icon: fas fa-calendar
  - name: "POST: Delete Scheduled Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    fa_icon: fas fa-calendar-minus
  - name: "POST: Delete Scheduled API Triggered Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    fa_icon: fas fa-calendar-minus
  - name: "POST: Schedule Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    fa_icon: fas fa-calendar-plus
  - name: "POST: Schedule API Triggered Campaign Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    fa_icon: fas fa-calendar-alt
  - name: "POST: Schedule API Triggered Canvas Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    fa_icon: fas fa-calendar-alt
  - name: "POST: Update Scheduled Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    fa_icon: fas fa-calendar
  - name: "POST: Update Scheduled API Triggered Campaign Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    fa_icon: fas fa-calendar
  - name: "POST: Update Scheduled API Triggered Canvas Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    fa_icon: fas fa-calendar-alt

guide_menu_title: "Send Messages Endpoints"
guide_menu_list:
  - name: "POST: Create Send IDs"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    fa_icon: fas fa-id-card
  - name: "POST: Send Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    fa_icon: fas fa-paper-plane
  - name: "POST: Send API Triggered Campaign Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    fa_icon: fas fa-inbox
  - name: "POST: Send API Triggered Canvas Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    fa_icon: fas fa-inbox
---
