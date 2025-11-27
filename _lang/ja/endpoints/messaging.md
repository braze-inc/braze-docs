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
description: "このランディングページには、Braze メッセージングエンドポイントがリストされます。"
page_type: landing

guide_top_header: "メッセージングエンドポイント"
guide_top_text: "Braze メッセージング API でユーザーにメッセージを送信する方法は、2 種類あります。<code class='highlighter-rouge'>messages/sendと</code>`/messages/schedule`エンドポイントを使えば、APIリクエストの中でメッセージの内容とコンフィギュレーションを提供することができる。また、BrazeダッシュボードでAPIトリガーキャンペーンを使ってメッセージの詳細を管理し、`/campaigns/trigger/send`と`/campaigns/trigger/schedule`エンドポイントを使って、いつ誰に送信するかをコントロールすることもできる。以下のセクションでは、両方のメソッドのリクエスト指定について詳しく説明します。<br> <br> 他のキャンペーンと同様に、Braze ダッシュボードで [再資格設定]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/#re-eligibility-with-api-triggered-campaigns) を構成することで、特定のユーザーがメッセージング API キャンペーンを受信できる回数を制限できます。Braze は、送信されたAPI リクエスト数に関係なく、キャンペーンの再受信を設定していないユーザーには API メッセージを配信しません。<br> <br> 「メッセージを送信」エンドポイントでは、指定したユーザーに即時メッセージを送信できます。セグメントをターゲットにしている場合、リクエストの記録は **メッセージアクティビティログ** に保存されます。「メッセージをスケジュール」エンドポイントを使用して、指定した時間にメッセージを送信するか、すでにスケジュールしたメッセージを変更またはキャンセルします。"

guide_featured_title: "「メッセージをスケジュール」エンドポイント"
guide_featured_list:
  - name: "取得:今後スケジュールされているキャンペーンとキャンバスをリスト"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST:スケジュールされたメッセージを削除"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST:スケジュールされた API トリガーキャンペーンを削除"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST:スケジュールされた API トリガーキャンバスを削除"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST:メッセージをスケジュール"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST:API トリガーキャンペーンメッセージをスケジュール"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST:API トリガーキャンバスメッセージをスケジュール"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST:スケジュールされたメッセージを更新"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST:スケジュールされた API トリガーキャンペーンメッセージを更新"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST:スケジュールされた API トリガーキャンバスメッセージを更新"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Send messages endpoints"
guide_menu_list:
  - name: "POST:送信 ID を作成"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST:メッセージをすぐに送信"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST:API トリガーキャンペーンメッセージをすぐに送信"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST:API トリガーキャンバスメッセージをすぐに送信"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Duplicate message endpoints"
guide_menu_list2:
  - name: "POST:重複キャンペーン"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns/
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST:キャンバスの複製"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases/
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Live Activity endpoints"
guide_menu_list3:
  - name: "POST:ライブアクティビティを更新"
    link: /docs/api/endpoints/messaging/live_activity/update/
    image: /assets/img/braze_icons/tablet-01.svg
---
