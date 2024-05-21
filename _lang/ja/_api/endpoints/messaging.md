---
nav_title: メッセージ
article_title: メッセージングエンドポイント
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
description: "このランディングページには、Braze メッセージングエンドポイントが一覧表示されます。"
page_type: landing

guide_top_header: "メッセージングエンドポイント"
guide_top_text: "Braze Messaging API には、ユーザーにメッセージを送信するための2 つの異なるオプションがあります。API リクエストでは、<code class='highlighter-rouge'>/messages/send</code>および`/messages/schedule` エンドポイントを使用してメッセージの内容と設定を指定できます。または、メッセージの詳細を、API トリガキャンペーンを使用してBraze ダッシュボードで管理し、`/campaigns/trigger/send` および`/campaigns/trigger/schedule` エンドポイントとともに送信される時期と宛先を制御することもできます。以下のセクションでは、両方のメソッドのリクエスト仕様について詳しく説明します。<br><br>他のキャンペーンと同様に、Brazeダッシュボードで[re-eligibility settings](/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/#re-eligibility-with-api-trigBraze は、送信されるAPI リクエストの数に関係なく、キャンペーンの対象になっていないユーザにAPI メッセージを配信しません。<br><br>Send Message エンドポイントでは、指定されたユーザに即時メッセージを送信できます。セグメントをターゲットにする場合、リクエストのレコードは**Message Activity Log** に保存されます。スケジュールメッセージエンドポイントを使用して、指定した時間にメッセージを送信し、すでにスケジュールされているメッセージを変更またはキャンセルします。"

guide_featured_title: "メッセージエンドポイントのスケジュール"
guide_featured_list:
  - name: "GET: List Upcoming Scheduled Campaigns and Canvases"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    fa_icon: fas fa-calendar
  - name: "POST: Delete Scheduled Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    fa_icon: fas fa-calendar-minus
  - name: "POST: Delete Scheduled API-Triggered Campaigns"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    fa_icon: fas fa-calendar-minus
  - name: "POST: Delete Scheduled API-Triggered Canvases"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    fa_icon: fas fa-calendar-minus
  - name: "POST: Schedule Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    fa_icon: fas fa-calendar-plus
  - name: "POST: Schedule API-Triggered Campaign Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    fa_icon: fas fa-calendar-alt
  - name: "POST: Schedule API-Triggered Canvas Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    fa_icon: fas fa-calendar-alt
  - name: "POST: Update Scheduled Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    fa_icon: fas fa-calendar
  - name: "POST: Update Scheduled API-Triggered Campaign Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    fa_icon: fas fa-calendar
  - name: "POST: Update Scheduled API-Triggered Canvas Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    fa_icon: fas fa-calendar-alt

guide_menu_title: "Send messages endpoints"
guide_menu_list:
  - name: "POST: Create Send IDs"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    fa_icon: fas fa-id-card
  - name: "POST: Send Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    fa_icon: fas fa-paper-plane
  - name: "POST: Send API-Triggered Campaign Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    fa_icon: fas fa-inbox
  - name: "POST: Send API-Triggered Canvas Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    fa_icon: fas fa-inbox

guide_menu_title2: "Live Activity endpoints"
guide_menu_list2:
  - name: "POST: Update Live Activity"
    link: /docs/api/endpoints/messaging/live_activity/update/
    fa_icon: fas fa-tablet-alt
---
