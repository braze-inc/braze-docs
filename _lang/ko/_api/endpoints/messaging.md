---
nav_title: 메시지
article_title: 메시징 엔드포인트
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
description: "이 랜딩 페이지에는 Braze 메시징 엔드포인트가 나열되어 있습니다."
page_type: landing

guide_top_header: "메시징 엔드포인트"
guide_top_text: "Braze 메시징 API는 사용자에게 메시지를 보낼 수 있는 두 가지 옵션을 제공합니다. API 요청에 메시지 내용 및 구성을 제공하면 됩니다. <code class='highlighter-rouge'>/messages/send</code> 메시지/스케줄` 엔드포인트. 또는 Braze 대시보드에서 API 트리거 캠페인으로 메시지의 세부 정보를 관리하고 `/campaigns/trigger/send` 및`/campaigns/trigger/schedule` 엔드포인트를 사용하여 언제, 누구에게 전송되는지 제어할 수 있습니다. 다음 섹션에서는 두 가지 방법의 요청 사양에 대해 자세히 설명합니다. <br> <br> 다른 캠페인과 마찬가지로, 특정 사용자가 메시징 API 캠페인을 수신할 수 있는 횟수를 제한하려면 Braze 대시보드에서 [재자격 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/#re-eligibility-with-api-triggered-campaigns)을 구성하여 특정 사용자가 메시지 API 캠페인을 받을 수 있는 횟수를 제한할 수 있습니다. Braze는 API 요청 횟수에 관계없이 캠페인에 다시 참여하지 않은 사용자에게는 API 메시지를 전달하지 않습니다. <br> <br> 메시지 보내기 엔드포인트를 사용하면 지정된 사용자에게 즉시 메시지를 보낼 수 있습니다. 세그먼트를 타겟팅하는 경우, 요청 기록이 **메시지 활동 로그**에 저장됩니다. 메시지 예약 엔드포인트를 사용하여 지정된 시간에 메시지를 보내고, 이미 예약한 메시지를 수정하거나 취소할 수 있습니다."

guide_featured_title: "메시지 엔드포인트 예약"
guide_featured_list:
  - name: "GET: 예정된 캠페인 및 캔버스 목록 보기"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: 예약된 메시지 삭제"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: 예약된 API 트리거 캠페인 삭제하기"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: 예약된 API 트리거 캔버스 삭제하기"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: 메시지 예약"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: API 트리거 캠페인 메시지 예약하기"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: API 트리거 캔버스 메시지 예약하기"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: 예약된 메시지 업데이트"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: 예약된 API 트리거 캠페인 메시지 업데이트"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: 예약된 API 트리거 캔버스 메시지 업데이트"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Send messages endpoints"
guide_menu_list:
  - name: "POST: 보내기 ID 만들기"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: 즉시 메시지 보내기"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: API 트리거 캠페인 메시지 즉시 보내기"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: API 트리거 캔버스 메시지 즉시 보내기"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Duplicate message endpoints"
guide_menu_list2:
  - name: "POST: 중복 캠페인"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns/
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST: 캔버스 복제하기"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases/
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Live Activity endpoints"
guide_menu_list3:
  - name: "POST: 실시간 활동 업데이트"
    link: /docs/api/endpoints/messaging/live_activity/update/
    image: /assets/img/braze_icons/tablet-01.svg
---
