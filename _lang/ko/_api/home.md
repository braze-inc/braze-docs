---
page_order: 0
nav_title: 홈
article_title: Braze API 가이드
layout: api_glossary
glossary_top_header: "Braze API Guide"
glossary_top_text: "Braze provides a high-performance REST API to allow you to track users, send messages, export data, and more. This page lists available Braze API endpoints and their uses."
page_type: glossary
description: "이 랜딩 페이지에는 사용 가능한 Braze API 엔드포인트와 그 용도가 나열되어 있습니다."
glossary_tag_name: Endpoint Type

glossary_filter_text: "Select endpoint type to narrow the glossary:"

glossary_mid_text: "Endpoint Search"
guide_featured_list:
  - name: API 개요
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics/
  - name: API 식별자 유형
    link: /docs/api/identifier_types/
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: 개체 및 필터
    link: /docs/api/objects_filters/
    image: /assets/img/braze_icons/settings-01.svg
  - name: 오류 및 응답
    link: /docs/api/errors/
    image: /assets/img/braze_icons/list.svg
  - name: 데이터 보존
    link: /docs/api/data_retention/
    image: /assets/img/braze_icons/laptop-02.svg
  - name: 요금 한도
    link: /docs/api/api_limits/
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: 캠페인
  - name: 캔버스
  - name: 카탈로그
  - name: 콘텐츠 블록
  - name: 사용자 지정 이벤트
  - name: 이메일 목록
  - name: 이메일 템플릿
  - name: KPI
  - name: 구매
  - name: 환경설정 센터
  - name: 메시지 예약
  - name: SCIM
  - name: SDK 인증
  - name: 세그먼트
  - name: 메시지 보내기
  - name: SMS
  - name: 구독 그룹
  - name: 사용자 데이터
  - name: 라이브 활동
  - name: 클라우드 데이터 수집

glossaries:
  - name: "<a href='/docs/api/endpoints/user_data/post_user_alias/'>/users/alias/new</a>"
    description: 기존 식별된 사용자에 대한 새 사용자 별칭을 추가하거나 식별되지 않은 새 사용자를 만들 수 있습니다.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_alias_update/'>/users/alias/update</a>"
    description: 기존 사용자 별칭 이름을 새 사용자 별칭 이름으로 업데이트합니다.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_delete/'>/users/delete</a>"
    description: 알려진 사용자 식별자를 지정하여 모든 사용자 프로필을 삭제합니다.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_global_control_group/'>/users/export/global_control_group</a>"
    description: 글로벌 제어 그룹 내의 모든 사용자를 내보냅니다.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_identifier/'>/users/export/ids</a>"
    description: 사용자 식별자를 지정하여 모든 사용자 프로필에서 데이터를 내보낼 수 있습니다.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_segment/'>/users/export/segment</a>"
    description: 세그먼트 내의 모든 사용자를 내보냅니다.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/'>/users/external_ids/rename</a>"
    description: 사용자의 외부 ID 이름을 변경합니다.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/'>/users/external_ids/remove</a>"
    description: 더 이상 사용되지 않는 사용자의 이전 외부 ID를 제거합니다.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_identify/'>/users/identify</a>"
    description: 미확인(별칭 전용) 사용자를 식별합니다.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_track/'>/users/track</a>"
    description: "사용자 지정 이벤트, 구매를 기록하고 사용자 프로필 속성을 업데이트하세요."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_merge/'>/users/merge</a>"
    description: 사용자 프로필을 다른 사용자와 병합합니다.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/'>/campaigns/trigger/send</a>"
    description: API 트리거 전송을 통해 지정된 사용자에게 즉시 일회성 메시지를 보낼 수 있습니다. - 메시지 보내기
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/'>/canvas/trigger/send</a>"
    description: API 트리거 배달을 통해 캔버스 메시지를 전송합니다. - 메시지 보내기
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_messages/'>/messages/send</a>"
    description: Braze API를 통해 지정된 사용자에게 즉시 일회성 메시지를 보낼 수 있습니다.
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids/'>/sends/id/create</a>"
    description: 각 전송에 대해 캠페인을 만들지 않고도 프로그래밍 방식으로 메시지를 전송하고 메시지 실적을 추적하는 데 사용할 수 있는 전송 ID를 만듭니다.
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message/'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>"
    description: 지정된 사용자에게 즉시 일회성 트랜잭션 메시지를 전송할 수 있습니다.
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/'>/campaigns/trigger/schedule/create</a>"
    description: 대시보드에서 생성한 캠페인 메시지를 API 트리거 전달을 통해 전송합니다.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/'>/campaigns/trigger/schedule/delete</a>"
    description: 이전에 예약한 API 트리거 캠페인 메시지가 전송되기 전에 취소합니다.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/'>/campaigns/trigger/schedule/update</a>"
    description: 대시보드에서 생성된 예약된 API 트리거 캠페인을 업데이트합니다.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/'>/canvas/trigger/schedule/delete</a>"
    description: 이전에 API 트리거를 통해 예약한 캔버스 메시지가 전송되기 전에 취소합니다.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/'>/canvas/trigger/schedule/create</a>"
    description: API 트리거 배달을 통해 캔버스 메시지를 예약하세요.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/'>/messages/schedule/update</a>"
    description: 예약된 메시지를 업데이트합니다. 이 엔드포인트는 다음 중 하나에 대한 업데이트를 허용합니다. <code>schedule</code> 또는 <code>messages</code> 매개변수 또는 둘 다.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/'>/messages/schedule/delete</a>"
    description: 이전에 예약한 메시지가 전송되기 전에 취소합니다.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/'>/messages/schedule/create</a>"
    description: "캠페인, 캔버스 또는 기타 메시지를 지정된 시간에 전송하도록 예약합니다."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/'>/canvas/trigger/schedule/update</a>"
    description: 대시보드에서 생성된 예약된 API 트리거 캔버스를 업데이트합니다.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/'>/messages/scheduled_broadcasts</a>"
    description: 지금부터 지정된 날짜 사이에 예약된 캠페인 및 참가 캔버스에 대한 정보의 JSON 목록을 반환합니다. <code>end_time</code> 를 요청에 지정합니다.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/live_activity/update/'>/messages/live_activity/update</a>"
    description: iOS 라이브 활동을 업데이트합니다.
    tags:
      - Live Activity
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/'>/subscription/status/set</a>"
    description: Braze 대시보드에서 최대 50명의 사용자 구독 상태를 일괄 업데이트할 수 있습니다.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/'>/v2/subscription/status/set</a>"
    description: Braze 대시보드에서 최대 50명의 사용자 구독 상태를 일괄 업데이트할 수 있습니다.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/'>/subscription/status/get</a>"
    description: 구독 그룹에 속한 사용자의 구독 상태를 가져옵니다.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/'>/subscription/user/status</a>"
    description: 특정 사용자의 구독 그룹을 나열하고 가져옵니다.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/email/post_blacklist/'>/email/blacklist</a>"
    description: 이메일에서 사용자의 수신을 취소하고 하드 반송으로 표시합니다.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_hard_bounces/'>/email/bounce/remove</a>"
    description: Braze 반송 목록에서 이메일 주소를 제거합니다.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_spam/'>/email/spam/remove</a>"
    description: Braze 스팸 목록에서 이메일 주소를 삭제하세요.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_email_subscription_status/'>/email/status</a>"
    description: 사용자의 이메일 구독 상태를 설정합니다.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_create_email_template/'>/templates/email/create</a>"
    description: Braze 대시보드에서 이메일 템플릿을 만듭니다.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_update_email_template/'>/templates/email/update</a>"
    description: Braze 대시보드에서 이메일 템플릿을 업데이트하세요.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/email/get_list_hard_bounces/'>/email/hard_bounces</a>"
    description: "특정 기간 내에 이메일 메시지를 '하드 반송'한 이메일 주소 목록을 가져옵니다."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/'>/email/unsubscribes</a>"
    description: 다음 기간 동안 구독을 취소한 이메일을 반환합니다. <code>start_date</code> 대상 <code>end_date</code>.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information/'>/templates/email/info</a>"
    description: 이메일 템플릿에 대한 정보를 얻으세요.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates/'>/templates/email/list</a>"
    description: Braze 계정에서 사용 가능한 이메일 템플릿 목록을 확인하세요.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics/'>/campaigns/data_series</a>"
    description: 시간에 따른 캠페인의 다양한 통계를 매일 시리즈로 검색할 수 있습니다.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_details/'>/캠페인/세부정보</a>"
    description: 지정된 캠페인에 대한 관련 정보를 검색합니다.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaigns/'>/campaigns/list</a>"
    description: "캠페인 목록 내보내기에는 각 캠페인의 이름, 캠페인 API 식별자, API 캠페인인지 여부, 캠페인과 연결된 태그가 포함됩니다."
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_send_analytics/'>/sends/data_series</a>"
    description: 추적된 다양한 통계의 일별 시리즈를 검색합니다. <code>send_id</code>.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics/'>/canvas/data_series</a>"
    description: 캔버스에 대한 시계열 데이터를 내보냅니다.
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/'>/canvas/data_summary</a>"
    description: 캔버스에 대한 시계열 데이터의 롤업을 내보내 캔버스의 결과를 간결하게 요약할 수 있습니다.
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_details/'>/canvas/details</a>"
    description: "이름, 만든 시간, 현재 상태 등 캔버스에 대한 메타데이터를 내보낼 수 있습니다."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvases/'>/canvas/list</a>"
    description: "캔버스 이름, 캔버스 API 식별자 및 관련 태그를 포함한 캔버스 목록을 내보냅니다."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_analytics/'>/segments/data_series</a>"
    description: 시간 경과에 따른 세그먼트의 예상 크기 일별 계열을 검색합니다.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_details/'>/segments/details</a>"
    description: 세그먼트에 대한 관련 정보를 검색합니다.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment/'>/segments/list</a>"
    description: "각 세그먼트의 이름, 세그먼트 API 식별자, 애널리틱스 추적이 활성화되어 있는지 여부가 포함된 세그먼트 목록을 내보냅니다."
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/sessions/get_sessions_analytics/'>/sessions/data_series</a>"
    description: 지정된 기간 동안 앱에 대한 일련의 세션 수를 검색합니다.
    tags:
      - Sessions
  - name: "<a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes/'>/custom_attributes</a>"
    description: "이름, 설명, 데이터 유형, 배열 길이(해당되는 경우), 상태 및 관련 태그를 포함한 사용자 지정 속성 목록을 내보냅니다."
    tags:
      - Custom Attributes
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics/'>/events/data_series</a>"
    description: 지정된 기간 동안 앱에서 사용자 지정 이벤트가 발생한 일련의 횟수를 검색합니다.
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_data/'>/events</a>"
    description: "이름, 설명, 상태, 관련 태그 및 애널리틱스 보고서 포함을 포함한 사용자 지정 이벤트 목록을 내보냅니다."
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events/'>/events/list</a>"
    description: 앱에 대해 기록된 사용자 지정 이벤트의 이름 목록을 내보냅니다.
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/'>/content_blocks/create</a>"
    description: 이메일 콘텐츠 블록을 만듭니다.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/'>/content_blocks/update</a>"
    description: 이메일 콘텐츠 블록을 업데이트합니다.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/'>/content_blocks/info</a>"
    description: 기존 이메일 콘텐츠 차단에 대한 통화 정보입니다.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/'>/content_blocks/list</a>"
    description: 기존 콘텐츠 블록 정보를 나열합니다.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date/'>/kpi/dau/data_series</a>"
    description: 각 날짜의 총 순 활성 사용자 수에 대한 일별 시리즈를 검색합니다.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/'>/kpi/mau/data_series</a>"
    description: 30일 동안의 총 순 활성 사용자 수에 대한 일별 시리즈를 검색합니다.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/'>/kpi/new_users/data_series</a>"
    description: 각 날짜의 총 신규 사용자 수에 대한 일별 시리즈를 검색합니다.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/'>/kpi/uninstalls/data_series</a>"
    description: 각 날짜의 총 제거 횟수에 대한 일별 시리즈를 검색합니다.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/sms/post_remove_invalid_numbers/'>/sms/invalid_phone_numbers/remove</a>"
    description: "Braze의 유효하지 않은 전화번호 목록에서 \"유효하지 않은\" 전화번호를 제거합니다. 유효하지 않은 것으로 표시된 전화번호의 유효성을 다시 검사하는 데 사용할 수 있습니다."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/sms/get_query_invalid_numbers/'>/sms/invalid_phone_numbers</a>"
    description: "특정 기간 내에 '유효하지 않은' 것으로 간주된 전화번호 목록을 가져옵니다."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/export/purchases/get_list_product_id/'>/purchases/product_list</a>"
    description: 페이지가 지정된 제품 ID 목록을 반환합니다.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_number_of_purchases/'>/purchases/quantity_series</a>"
    description: 일정 기간 동안 앱에서 발생한 총 구매 수를 반환합니다.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_revenue_series/'>/purchases/revenue_series</a>"
    description: 일정 기간 동안 앱에서 지출한 총 금액을 반환합니다.
    tags:
      - Purchases    
  - name: "<a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>"
    description: 환경 설정 센터의 URL을 만듭니다.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_list_preference_center/'>/preference_center/v1/list</a>"
    description: 사용 가능한 환경설정 센터를 나열합니다.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: 환경설정 센터의 생성 및 업데이트 시기를 포함하여 환경설정 센터에 대한 세부 정보를 확인합니다.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>"
    description: 환경설정 센터를 만들어 사용자가 이메일 캠페인에 대한 알림 환경설정을 관리할 수 있도록 합니다.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: 환경설정 센터를 업데이트합니다.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>"
    description: 카탈로그에서 여러 항목을 삭제합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: 카탈로그 항목과 세부 정보를 나열합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: 카탈로그에서 여러 항목을 편집합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: 카탈로그에 여러 항목을 생성합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/'>/catalogs/{catalog_name}</a>"
    description: 카탈로그를 삭제합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/'>/catalogs</a>"
    description: 카탈로그를 만듭니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/'>/catalogs</a>"
    description: 워크스페이스에 카탈로그를 나열합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: 카탈로그에서 품목을 생성합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: 카탈로그에서 품목을 편집합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: 여러 카탈로그 항목과 해당 콘텐츠를 반환합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: 카탈로그에서 품목을 삭제합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: 카탈로그에서 품목을 교체합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/'>/catalogs/{catalog_name}/items/</a>"
    description: 카탈로그에서 여러 항목을 교체합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields/'>/catalogs/{catalog_name}/fields/</a>"
    description: 카탈로그에 여러 필드를 생성합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field/'>/catalogs/{catalog_name}/fields/{field_name}</a>"
    description: 카탈로그에서 필드를 삭제합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections/'>/catalogs/{catalog_name}/selections</a>"
    description: 카탈로그에서 선택 항목을 만듭니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection/'>/catalogs/{catalog_name}/selections/{selection_name}</a>"
    description: 카탈로그 선택 항목을 삭제합니다.
    tags:
      - Catalogs
  - name: "<a href='/docs/post_create_user_account/'>/scim/v2/Users</a>"
    description: "이메일, 주어진 이름 및 가족 이름, 권한(회사, 워크스페이스 및 팀 수준에서 권한을 설정하기 위한)을 지정하여 새 대시보드 사용자 계정을 만듭니다."
    tags:
      - SCIM
  - name: "<a href='/docs/get_see_user_account_information/'>/scim/v2/Users/{id}</a>"
    description: 리소스 ID를 지정하여 기존 대시보드 사용자 계정을 조회합니다.
    tags:
      - SCIM
  - name: "<a href='/docs/post_update_existing_user_account/'>/scim/v2/Users/{id}</a>"
    description: "이메일, 주어진 이름 및 가족 이름, 권한(회사, 워크스페이스 및 팀 수준에서 권한을 설정하기 위한)을 지정하여 기존 대시보드 사용자 계정을 업데이트합니다."
    tags:
      - SCIM
  - name: "<a href='/docs/delete_existing_dashboard_user/'>/scim/v2/Users/{id}</a>"
    description: 기존 대시보드 사용자를 영구 삭제합니다.
    tags:
      - SCIM
  - name: "<a href='/docs/get_search_existing_dashboard_user_email/'>/scim/v2/Users?filter={userName@example.com}</a>"
    description: 이메일을 지정하여 기존 대시보드 사용자 계정을 조회합니다.
    tags:
      - SCIM
  - name: "<a href='/docs/api/endpoints/cdi/get_integration_list/'>/cdi/integrations</a>"
    description: 기존 연동 목록을 반환합니다.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/post_job_sync/'>/cdi/integrations/{integration_id}/sync</a>"
    description: 지정된 통합에 대한 동기화를 트리거합니다.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/get_job_sync_status/'>/cdi/integrations/{integration_id}/job_sync_status</a>"
    description: 동기화 상태 목록을 반환합니다.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/'>/app_group/sdk_authentication/create</a>"
    description: 앱을 위한 새로운 SDK 인증 키를 생성하세요.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys/'>/app_group/sdk_authentication/keys</a>"
    description: 앱의 SDK 인증 키를 나열합니다.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/'>/app_group/sdk_authentication/primary</a>"
    description: SDK 인증 키를 앱의 기본 키로 설정합니다.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key/'>/app_group/sdk_authentication/delete</a>"
    description: 앱을 위한 SDK 인증 키를 삭제하세요.
    tags:
      - SDK Authentication  
---