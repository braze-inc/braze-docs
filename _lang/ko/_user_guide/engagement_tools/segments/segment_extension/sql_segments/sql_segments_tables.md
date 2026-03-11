---
nav_title: "SQL 테이블 참조"
article_title: SQL 테이블 참조
page_order: 3
page_type: reference
toc_headers: h2
description: "이 문서에는 쿼리 빌더에서 또는 SQL 세그먼트 확장을 생성할 때 쿼리할 수 있는 테이블과 열이 포함되어 있습니다."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQL 테이블 참조

This page is a reference of tables and columns available to be queried in the [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) or when generating [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

## 목차

테이블 | 설명
------|------------
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | 삭제되지 않은 카탈로그 항목
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | 글로벌 컨트롤 그룹이 변경될 때
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | 사용자가 사용자 지정 이벤트를 수행하는 경우
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | 사용자가 앱을 설치하고 파트너에게 이를 어트리뷰션하는 경우
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | 사용자가 위치를 기록하는 경우
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | 사용자가 구매를 하는 경우
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | 사용자가 앱을 삭제하는 경우
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | 사용자가 앱을 업그레이드하는 경우
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | 사용자가 첫 번째 세션을 갖는 경우
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | 사용자가 뉴스피드를 볼 때
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | 사용자가 앱에서 세션을 종료하는 경우
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | 사용자가 앱에서 세션을 시작할 때
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | 사용자가 지오펜스 영역을 트리거하는 경우(예: 지오펜스에 들어가거나 나갈 때). 이 이벤트는 다른 이벤트와 함께 일괄 처리되어 표준 이벤트 엔드포인트를 통해 수신되었으므로 엔드포인트에서 실시간으로 수신되지 않았을 수 있습니다.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | 사용자가 지오펜스 영역을 트리거하는 경우(예: 지오펜스에 들어가거나 나갈 때). 이 이벤트는 전용 지오펜스 엔드포인트를 통해 수신되었으므로 사용자의 기기가 지오펜스를 트리거한 것을 감지하는 즉시 실시간으로 수신되었습니다. <br><br>또한 지오펜스 엔드포인트의 사용량 제한으로 인해 일부 지오펜스 이벤트가 RecordEvent로 반영되지 않을 수 있습니다. 그러나 모든 지오펜스 이벤트는 DataEvent로 표현됩니다(일괄 처리로 인해 약간의 지연이 발생할 수 있음).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | 라이브 액티비티 푸시-투-스타트 토큰이 변경될 때
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | 라이브 액티비티 업데이트 토큰이 변경될 때
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | 푸시 알림 토큰 상태가 변경될 때
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | 사용자가 이메일 등의 채널에서 전 세계적으로 구독하거나 구독을 취소하는 경우
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | 사용자가 구독 그룹을 구독하거나 구독을 취소하는 경우
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | 사용자가 캠페인에 대해 전환한 경우
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | 사용자가 캠페인의 컨트롤 그룹에 등록된 경우
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | 사용자가 캠페인에 대해 빈도 제한을 받는 경우
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | 사용자가 기본 전환 기간 내에 수익을 창출하는 경우
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | When a user progresses to a Canvas step
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | 사용자가 캔버스 전환 이벤트에 대해 전환하는 경우
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | 사용자가 캔버스에 들어가면
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | 사용자가 오디언스 종료 기준과 일치하여 캔버스를 종료하는 경우
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | 사용자가 예외 이벤트를 수행하여 캔버스를 종료하는 경우
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | 사용자가 캔버스 실험 단계로 전환하는 경우
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | 사용자가 실험 단계 경로를 입력하는 경우
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | 사용자가 캔버스 단계에 대해 빈도 제한을 받는 경우
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | 사용자가 기본 전환 이벤트 기간 내에 수익을 창출한 경우
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | 원래 예정된 배너 메시지가 어떤 이유로 중단되었습니다
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | 사용자가 배너를 클릭할 때
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | 사용자가 배너를 볼 때
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | 원래 예정된 콘텐츠 카드 메시지가 어떤 이유로 중단되었습니다.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | 사용자가 콘텐츠 카드를 클릭하는 경우
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | 사용자가 콘텐츠 카드를 해지하는 경우
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | 사용자가 콘텐츠 카드를 볼 때
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | 사용자에게 콘텐츠 카드를 보낼 때
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | 원래 예정된 이메일 메시지가 어떤 이유로 중단되었습니다.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | 이메일 서비스 공급자가 하드 바운스를 반환했습니다. 하드 바운스는 영구적인 전달 가능성 실패를 의미합니다.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | 사용자가 이메일의 링크를 클릭하는 경우
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | 이메일이 지연될 때
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | 이메일이 전달될 때
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | 이메일이 스팸으로 표시된 경우
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | 사용자가 이메일을 여는 경우
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | 사용자에게 이메일을 보낼 때
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | 이메일 소프트 바운스 발생 시
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | 사용자가 이메일 구독을 취소하는 경우
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | 사용자가 기능 플래그를 볼 때
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | 원래 예정된 인앱 메시지가 어떤 이유로 인해 중단되었습니다.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | 사용자가 인앱 메시지를 클릭하는 경우
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | 사용자가 인앱 메시지를 볼 때
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | 예약된 LINE 메시지가 전달되지 않을 경우, LINE으로 전송하기 전에
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | 사용자가 LINE 메시지 내 링크를 클릭할 때
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | 사용자로부터 LINE 메시지를 수신할 때
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | LINE 메시지가 LINE으로 전송될 때
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | 라이브 액티비티에 결과 이벤트가 있을 때
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | 라이브 액티비티 메시지가 전송될 때
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | 원래 예정된 뉴스피드 카드 메시지가 어떤 이유로 중단되었습니다
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | 사용자가 뉴스피드 카드를 클릭하는 경우
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | 사용자가 뉴스피드 카드를 볼 때
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | 원래 예정된 푸시 알림 메시지가 어떤 이유로 인해 중단되었습니다.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | 푸시 알림이 반송되는 경우
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | 사용자가 알림을 받은 후 알림을 클릭하지 않고 앱을 여는 경우
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | 사용자가 앱이 실행 중인 상태에서 푸시 알림을 수신할 때. <br><br>이 이벤트는 [Swift 소프트웨어 개발 키트](https://github.com/braze-inc/braze-swift-sdk)에서 지원되지 않으며, [Objective-C 소프트웨어 개발 키트](https://github.com/Appboy/appboy-ios-sdk)에서는 사용 중단되었습니다.
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | 사용자가 푸시 알림을 열거나 푸시 알림 버튼(앱을 열지 않는 닫기 버튼 포함)을 클릭한 경우. <br><br> 푸시 버튼 동작에는 여러 가지 결과가 있습니다. 아니요, 거부 및 취소 작업은 "클릭"이고 수락 작업은 "열기"입니다. 이 표에는 둘 다 표시되어 있지만, 열에서**BUTTON_ACTION_TYPE** 구분할 수 있습니다. 예를 들어 쿼리를 사용하여 아니요, 거부 또는 취소가 아닌 `BUTTON_ACTION_TYPE`으로 그룹화할 수 있습니다.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | 사용자에게 푸시 알림을 보낼 때
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Braze 내에서 감지된 오류로 인해 RCS 전송이 중단되고 메시지가 삭제될 때
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | 최종 사용자가 UI 요소를 탭하거나 클릭하여 RCS 메시지와 상호작용할 때
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | RCS 메시지가 최종 사용자의 모바일 기기에 성공적으로 전달될 때
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Braze가 최종 사용자로부터 발신된 RCS 메시지를 수신할 때
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | 최종 사용자가 자신의 기기에서 RCS 메시지를 열 때
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | 통신사 개입으로 인해 RCS 메시지 전달 가능성이 저하될 경우
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Braze 시스템에서 라스트마일 배송 파트너에게 RCS 메시지가 발송될 때
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | 원래 예정된 SMS 메시지가 어떤 이유로 인해 중단되었습니다.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | 이동 통신사로 SMS 메시지가 전송되는 경우
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | SMS 메시지가 전달되는 경우
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Braze가 SMS 서비스 제공업체에 SMS 메시지를 전달할 수 없는 경우
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | 사용자로부터 SMS 메시지를 수신한 경우
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | 사용자에게 SMS 메시지가 전달되지 않은 경우
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | SMS 메시지가 전송되는 경우
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | 사용자가 SMS 메시지에 포함된 Braze 단축 URL을 클릭하는 경우
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | 원래 예정된 웹훅 메시지가 어떤 이유로 중단되었습니다.
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | 웹훅 메시지가 전달되었으나 엔드포인트로부터 오류 응답으로 실패할 때
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | 사용자에 대한 웹훅을 보낼 때
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | 원래 예정된 WhatsApp 메시지가 어떤 이유로 중단되었습니다.
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | 사용자가 WhatsApp 메시지 내 링크나 버튼을 클릭할 때
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |WhatsApp 메시지가 전달되는 경우
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | WhatsApp 메시지가 사용자에게 전달되지 않은 경우
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | 사용자로부터 WhatsApp 메시지를 수신한 경우
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | 사용자가 WhatsApp 메시지를 열면
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | 사용자에게 WhatsApp 메시지를 보낼 때
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | 사용자의 임의 버킷 번호가 변경된 경우
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | 고객 요청에 의해 사용자가 삭제된 경우
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | 사용자가 다른 사용자의 프로필과 병합되어 원래 프로필이 고아가 된 경우


## 카탈로그

### CATALOGS_ITEMS_SHARED{#CATALOGS_ITEMS_SHARED}

필드 | 유형 | Description
------|------|------------
`catalog_id` | `string` | 카탈로그의 BSON ID
`item_id` | `string` | 카탈로그 항목의 BSON ID
`app_group_id` | `null,` `string` | 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 앱 그룹의 API ID
`field_name` | `null,` `string` | 필드 이름
`field_value` | `null,` `string` | 필드의 값
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 변경 로그

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED{#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`random_bucket_number` | `null, int` | 새로운 무작위 버킷 번호
`global_control_group` | `null, boolean` | 이 변경으로 버킷 번호가 글로벌 컨트롤 그룹에 포함됩니다.
`previous_global_control_group` | `null, boolean` | 이 변경 이전에는 버킷 번호가 글로벌 컨트롤 그룹에 포함되었으나, 이제는 더 이상 포함되지 않습니다.
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Behaviors

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED{#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 이 작업이 발생한 앱의 API ID
`time` | `int` | 사용자가 이벤트를 수행한 유닉스 타임스탬프
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 사용자 지정 이벤트가 발생한 디바이스의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`name` | `string` | 사용자 지정 이벤트의 이름
`properties` | `string` | JSON 인코딩된 문자열로 저장된 이벤트의 사용자 지정 속성
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | `ios_idfa`, `google_ad_id`, `windows_ad_id`, 또는 `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED{#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 설치한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 사용자가 설치한 유닉스 타임스탬프
`source` | `string` | 기여도의 출처
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED{#USERS_BEHAVIORS_LOCATION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 위치를 기록하는 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 이 위치가 기록된 앱의 API ID
`time` | `int` | 위치가 기록된 유닉스 타임스탬프
`latitude` | `float` | [PII] 기록된 위치의 위도
`longitude` | `float` | [PII] 기록된 위치의 경도
`altitude` | `null, float` | [PII] 기록된 위치의 고도
`ll_accuracy` | `null, float` | 기록된 위치의 위도 및 경도 정확도
`alt_accuracy` | `null, float` | 기록된 위치의 고도 정확도
`device_id` | `null,` `string` | 위치가 기록된 디바이스의 ID
`sdk_version` | `null,` `string` | 위치가 기록될 때 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | `ios_idfa`, `google_ad_id`, `windows_ad_id`, 또는 `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED{#USERS_BEHAVIORS_PURCHASE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 구매한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 구매가 발생한 앱의 API ID
`time` | `int` | 사용자가 구매한 유닉스 타임스탬프
`device_id` | `null,` `string` | 구매가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 구매 시 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`product_id` | `string` | 구매한 제품의 ID
`price` | `float` | 구매 가격
`currency` | `string` | 구매 통화
`properties` | `string` | JSON 인코딩 문자열로 저장된 구매의 사용자 지정 속성
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | `ios_idfa`, `google_ad_id`, `windows_ad_id`, 또는 `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED{#USERS_BEHAVIORS_UNINSTALL_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 제거한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 제거된 앱의 API ID
`time` | `int` | 사용자가 제거한 unix 타임스탬프
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED{#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 앱을 업그레이드한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 사용자가 업그레이드한 앱의 API ID
`time` | `int` | 사용자가 앱을 업그레이드한 유닉스 타임스탬프
`device_id` | `null,` `string` | 사용자가 앱을 업그레이드한 기기의 ID
`sdk_version` | `null,` `string` | 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`old_app_version` | `null,` `string` | 이전 버전의 앱
`new_app_version` | `null,` `string` | 새 버전의 앱
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED{#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 작업을 수행하는 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 이 세션이 발생한 앱의 API ID
`time` | `int` | 세션이 시작된 유닉스 타임스탬프
`session_id` | `string` | 세션의 UUID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 세션이 발생한 기기의 ID
`sdk_version` | `null,` `string` | 세션 중에 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED{#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED{#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 작업을 수행하는 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 이 세션이 발생한 앱의 API ID
`time` | `int` | 세션이 종료된 유닉스 타임스탬프
`duration` | `null, float` | 세션 지속 시간 (초)
`session_id` | `string` | 세션의 UUID
`device_id` | `null,` `string` | 세션이 발생한 기기의 ID
`sdk_version` | `null,` `string` | 세션 중에 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED{#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 작업을 수행하는 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_api_id` | `null,` `string` | 이 세션이 발생한 앱의 API ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 세션이 시작된 유닉스 타임스탬프
`session_id` | `string` | 세션의 UUID
`device_id` | `null,` `string` | 세션이 발생한 기기의 ID
`sdk_version` | `null,` `string` | 세션 중에 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED{#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 이 작업이 발생한 앱의 API ID
`time` | `int` | 사용자가 이벤트를 수행한 유닉스 타임스탬프
`device_id` | `null,` `string` | 사용자 지정 이벤트가 발생한 디바이스의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`event_type` | `string` | 트리거된 지오펜스 이벤트의 종류. (예: '진입' 또는 '종료')
`location_set_id` | `string` | 트리거된 지오펜스 위치 집합의 ID입니다.
`geofence_id` | `string` | 트리거된 지오펜스의 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED{#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 이 작업이 발생한 앱의 API ID
`time` | `int` | 사용자가 이벤트를 수행한 유닉스 타임스탬프
`device_id` | `null,` `string` | 사용자 지정 이벤트가 발생한 디바이스의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`event_type` | `string` | 트리거된 지오펜스 이벤트의 종류. (예: '진입' 또는 '종료')
`location_set_id` | `string` | 트리거된 지오펜스 위치 집합의 ID입니다.
`geofence_id` | `string` | 트리거된 지오펜스의 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED{#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`activity_attributes_type` | `null,` `string` | 실시간 활동 속성 유형
`push_to_start_token` | `null,` `string` | 라이브 액티비티 시작 토큰 푸시
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`ios_push_token_apns_gateway` | `null, int` | 푸시 토큰의 APNS 게이트웨이, iOS 푸시 토큰에만 적용됨, 개발용 1, 운영용 2
`push_token_state_change_type` | `null,` `string` | 푸시 토큰 상태 변경 유형에 대한 설명
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED{#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`activity_id` | `null,` `string` | 실시간 활동 식별자
`update_token` | `null,` `string` | 실시간 활동 업데이트 토큰
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`ios_push_token_apns_gateway` | `null, int` | 푸시 토큰의 APNS 게이트웨이, iOS 푸시 토큰에만 적용됨, 개발용 1, 운영용 2
`push_token_state_change_type` | `null,` `string` | 푸시 토큰 상태 변경 유형에 대한 설명
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED{#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`push_token` | `null,` `string` | 이벤트 푸시 토큰
`push_token_created_at` | `null, int` | 푸시 토큰이 생성된 Unix 타임스탬프
`push_token_updated_at` | `null, int` | 푸시 토큰이 마지막으로 업데이트된 Unix 타임스탬프
`push_token_foreground_push_disabled` | `null, boolean` | 푸시 토큰의 전경 푸시 비활성화 플래그
`push_token_device_id` | `null,` `string` | 푸시 토큰의 기기 ID
`push_token_provisionally_opted_in` | `null, boolean` | 푸시 토큰의 임시 옵트인 플래그
`ios_push_token_apns_gateway` | `null, int` | 푸시 토큰의 APNS 게이트웨이, iOS 푸시 토큰에만 적용됨, 개발용 1, 운영용 2
`web_push_token_public_key` | `null,` `string` | 푸시 토큰의 공개 키, 웹 푸시 토큰에만 적용됩니다
`web_push_token_user_auth` | `null,` `string` | 푸시 토큰의 사용자 인증, 웹 푸시 토큰에만 적용됨
`web_push_token_vapid_public_key` | `null,` `string` | 푸시 토큰의 VAPID 공개 키, 웹 푸시 토큰에만 적용됨
`push_token_state_change_type` | `null,` `string` | 푸시 토큰 상태 변경 유형에 대한 설명
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED{#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 영향을 받은 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`email_address` | `null,` `string` | [PII] 사용자의 이메일 주소
`state_change_source` | `null,` `string` | 상태 변경의 소스(REST, SDK, 대시보드 등)
`subscription_status` | `string` | 구독 상태: '가입됨', '탈퇴' 또는 '옵트인'
`channel` | `null,` `string` | 이메일과 같은 글로벌 구독 상태의 채널
`time` | `int` | 구독 상태가 변경된 유닉스 타임스탬프
`timezone` | `null,` `string` | 사용자의 표준 시간대
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 이벤트가 속한 앱의 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 이벤트가 속한 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`send_id` | `null,` `string` | 이 구독 상태 변경 작업이 발생한 메시지 전송 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`channel_identifier` | `null,` `string` | [PII] 이벤트가 속한 채널에서 사용자의 식별자.
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED{#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 영향을 받은 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`email_address` | `null,` `string` | [PII] 사용자의 이메일 주소
`phone_number` | `null,` `string` | [PII] 사용자의 e164 형식 전화번호
`app_api_id` | `null,` `string` | 이벤트가 속한 앱의 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 이벤트가 속한 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`channel` | `null,` `string` | 채널: 구독 그룹의 채널 유형에 따라 '이메일' 또는 'SMS'
`subscription_status` | `string` | 구독 상태: '가입됨', '탈퇴' 또는 '옵트인'
`time` | `int` | 구독 상태가 변경된 유닉스 타임스탬프
`timezone` | `null,` `string` | 사용자의 표준 시간대
`send_id` | `null,` `string` | 이 구독 상태 변경 작업이 발생한 메시지 전송 ID
`state_change_source` | `null,` `string` | 상태 변경의 소스(REST, SDK, 대시보드 등)
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`channel_identifier` | `null,` `string` | [PII] 이벤트가 속한 채널에서 사용자의 식별자.
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 캠페인

### USERS_CAMPAIGNS_CONVERSION_SHARED{#USERS_CAMPAIGNS_CONVERSION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`conversion_behavior_index` | `null, int` | 전환 행동 인덱스
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED{#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED{#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`channel` | `null,` `string` | 이 이벤트가 속한 채널
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED{#USERS_CAMPAIGNS_REVENUE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`revenue` | `long` | 발생한 USD 수익(센트) 금액
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED{#USERS_CANVASSTEP_PROGRESSION_SHARED}

| 필드                                  | 유형                     | Description                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                                                               |
| `user_id`                              | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                                                              |
| `device_id`                            | `string`, `null`    | 사용자가 익명인 경우 이 사용자와 연결된 디바이스의 ID입니다.                                            |
| `app_group_id`                         | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                                                                   |
| `app_group_api_id`                     | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID                                                                    |
| `time`                                 | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프                                                                      |
| `canvas_id`                            | `string`, `null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID                                                     |
| `canvas_api_id`                        | `string`, `null`    | 이 이벤트가 속한 캔버스의 API ID        |         
| `canvas_variation_api_id`              | `string`, `null`    | 이 이벤트가 속한 캔버스 변형의 API ID                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                                                                 |
| `progression_type`                     | `string`, `null`    | Type of step progression event |
| `is_canvas_entry`                      | `boolean`, `null`   | Whether this is entry into a first step in a Canvas        |
| `exit_reason`                          | `string`, `null`    | If this is an exit, the reason a user exited the canvas during the step                  |
| `canvas_entry_id`                      | `string`, `null`    | Unique identifier for this instance of a user in a Canvas  |
| `next_step_id`                         | `string`, `null`    | BSON ID of the next step in the canvas |
| `next_step_api_id`                     | `string`, `null`    | API ID of the next step in the Canvas |
| `sf_created_at`                        | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED{#USERS_CANVAS_CONVERSION_SHARED}

| 필드                                  | 유형                     | Description                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                                                               |
| `user_id`                              | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                                                              |
| `device_id`                            | `string`, `null`    | 사용자가 익명인 경우 이 사용자와 연결된 디바이스의 ID입니다.                                            |
| `app_group_id`                         | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                                                                   |
| `app_group_api_id`                     | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID                                                                    |
| `time`                                 | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프                                                                      |
| `app_api_id`                           | `string`, `null`    | 이 이벤트가 발생한 앱의 API ID                                                                  |
| `canvas_id`                            | `string`, `null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID                                                     |
| `canvas_api_id`                        | `string`, `null`    | 이 이벤트가 속한 캔버스의 API ID                                                                      |
| `canvas_variation_api_id`              | `string`, `null`    | 이 이벤트가 속한 캔버스 변형의 API ID                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                                                                 |
| `canvas_step_message_variation_api_id` | `string`, `null`    | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID                                                  |
| `conversion_behavior_index`            | `int`, `null`       | 사용자가 수행한 전환 이벤트 유형(여기서 '0'은 1차 전환, '1'은 2차 전환)입니다. |
| `gender`                               | `string`, `null`    | [PII] 사용자의 성별                                                                                        |
| `country`                              | `string`, `null`    | [PII] 사용자의 국가                                                                                       |
| `timezone`                             | `string`, `null`    | 사용자의 표준 시간대                                                                                            |
| `language`                             | `string`, `null`    | [PII] 사용자의 언어                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED{#USERS_CANVAS_ENTRY_SHARED}

| 필드                     | 유형                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                 | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                        |
| `external_user_id`        | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `device_id`               | `string`, `null`    | 사용자가 익명인 경우 이 사용자와 연결된 디바이스의 ID입니다. |
| `app_group_id`            | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `app_group_api_id`        | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID                         |
| `time`                    | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프                           |
| `canvas_id`               | `string`, `null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`           | `string`, `null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id` | `string`, `null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`      | `string`, `null`    | [사용 중단됨] 이 이벤트가 속한 캔버스 단계의 API ID         |
| `gender`                  | `string`, `null`    | [PII] 사용자의 성별                                             |
| `country`                 | `string`, `null`    | [PII] 사용자의 국가                                            |
| `timezone`                | `string`, `null`    | 사용자의 표준 시간대                                                 |
| `language`                | `string`, `null`    | [PII] 사용자의 언어                                           |
| `in_control_group`        | `boolean`, `null`   | 사용자가 대조 그룹에 등록되어 있는 경우 참입니다.                   |
| `sf_created_at`           | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED{#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| 필드                     | 유형                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                 | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                        |
| `external_user_id`        | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `app_group_id`            | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `app_group_api_id`        | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID                         |
| `time`                    | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프                           |
| `canvas_id`               | `string`, `null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`           | `string`, `null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id` | `string`, `null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`      | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `sf_created_at`           | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED{#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| 필드                     | 유형                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                 | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                        |
| `external_user_id`        | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `app_group_id`            | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `app_group_api_id`        | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID                         |
| `time`                    | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프                           |
| `canvas_id`               | `string`, `null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`           | `string`, `null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id` | `string`, `null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`      | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `sf_created_at`           | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED{#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| 필드                       | 유형                     | Description                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                                                               |
| `user_id`                   | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                                                                   |
| `external_user_id`          | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                                                              |
| `app_group_id`              | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                                                                   |
| `time`                      | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프                                                                      |
| `app_api_id`                | `string`, `null`    | 이 이벤트가 발생한 앱의 API ID                                                                  |
| `canvas_id`                 | `string`, `null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID                                                     |
| `canvas_api_id`             | `string`, `null`    | 이 이벤트가 속한 캔버스의 API ID                                                                      |
| `canvas_variation_api_id`   | `string`, `null`    | 이 이벤트가 속한 캔버스 변형의 API ID                                                            |
| `canvas_step_api_id`        | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                                                                 |
| `experiment_step_api_id`    | `string`, `null`    | 이 이벤트가 속한 실험 단계의 API ID                                                             |
| `conversion_behavior_index` | `int`, `null`       | 사용자가 수행한 전환 이벤트 유형(여기서 '0'은 1차 전환, '1'은 2차 전환)입니다. |
| `sf_created_at`             | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                                                                   |
| `experiment_split_api_id` | `string`, `null` | 사용자가 등록된 실험 분할의 API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED{#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| 필드                     | 유형                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                 | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                        |
| `external_user_id`        | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `app_group_id`            | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `time`                    | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프                           |
| `canvas_id`               | `string`, `null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`           | `string`, `null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id` | `string`, `null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`      | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `experiment_step_api_id`  | `string`, `null`    | 이 이벤트가 속한 실험 단계의 API ID                  |
| `in_control_group`        | `boolean`, `null`   | 사용자가 대조 그룹에 등록되어 있는 경우 참입니다.                   |
| `sf_created_at`           | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |

\|`experiment_split_api_id`  | `string`,`null`  | 사용자가 등록된 실험 분할의 API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED{#USERS_CANVAS_FREQUENCYCAP_SHARED}

| 필드                                  | 유형                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                              | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                        |
| `external_user_id`                     | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `device_id`                            | `string`, `null`    | 사용자가 익명인 경우 이 사용자와 연결된 디바이스의 ID입니다. |
| `app_group_id`                         | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `app_group_api_id`                     | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID                         |
| `time`                                 | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프                           |
| `canvas_id`                            | `string`, `null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`                        | `string`, `null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id`              | `string`, `null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`                   | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID       |
| `channel`                              | `string`, `null`    | 이 이벤트가 속한 메시징 채널(이메일, 푸시 등)          |
| `gender`                               | `string`, `null`    | [PII] 사용자의 성별                                             |
| `country`                              | `string`, `null`    | [PII] 사용자의 국가                                            |
| `timezone`                             | `string`, `null`    | 사용자의 표준 시간대                                                 |
| `language`                             | `string`, `null`    | [PII] 사용자의 언어                                           |
| `sf_created_at`                        | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED{#USERS_CANVAS_REVENUE_SHARED}

| 필드                                  | 유형                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                              | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                        |
| `external_user_id`                     | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `device_id`                            | `string`, `null`    | 사용자가 익명인 경우 이 사용자와 연결된 디바이스의 ID입니다. |
| `app_group_id`                         | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `app_group_api_id`                     | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID                         |
| `time`                                 | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프                           |
| `canvas_id`                            | `string`, `null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`                        | `string`, `null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id`              | `string`, `null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`                   | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID       |
| `gender`                               | `string`, `null`    | [PII] 사용자의 성별                                             |
| `country`                              | `string`, `null`    | [PII] 사용자의 국가                                            |
| `timezone`                             | `string`, `null`    | 사용자의 표준 시간대                                                 |
| `language`                             | `string`, `null`    | [PII] 사용자의 언어                                           |
| `revenue`                              | `int`, `null`       | USD로 생성된 수익 금액(센트 단위로 표시)               |
| `sf_created_at`                        | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
| `app_api_id` | `string`, `null` | 이 이벤트가 발생한 앱의 API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Messages


### USERS_MESSAGES_BANNER_ABORT_SHARED{#USERS_MESSAGES_BANNER_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 기기 브라우저 - 추출됨user_agent\- 열림이 발생한
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | 하나의 ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 128자)
`banner_placement_id` | `null,` `string` | 고객 지정 배너 배치 ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_CLICK_SHARED{#USERS_MESSAGES_BANNER_CLICK_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 기기 브라우저 - 추출됨user_agent\- 열림이 발생한
`button_id` | `null,` `string` | 클릭한 버튼의 ID(클릭이 버튼 클릭을 나타내는 경우)
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | 하나의 ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`banner_placement_id` | `null,` `string` | 고객 지정 배너 배치 ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED{#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 기기 브라우저 - 추출됨user_agent\- 열림이 발생한
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | 하나의 ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`banner_placement_id` | `null,` `string` | 고객 지정 배너 배치 ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED{#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED{#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`content_card_id` | `string` | 이 이벤트를 생성한 카드의 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 디바이스의 브라우저
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | `ios_idfa`, `google_ad_id`, `windows_ad_id`, 또는 `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED{#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`content_card_id` | `string` | 이 이벤트를 생성한 카드의 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 디바이스의 브라우저
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | `ios_idfa`, `google_ad_id`, `windows_ad_id`, 또는 `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED{#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`content_card_id` | `string` | 이 이벤트를 생성한 카드의 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 디바이스의 브라우저
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | `ios_idfa`, `google_ad_id`, `windows_ad_id`, 또는 `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED{#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`content_card_id` | `string` | 이 이벤트를 생성한 카드의 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`message_extras` | `null,` `string` | [PII] 액체 렌더링 중 태그된 키-값 페어의 JSON 문자열
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED{#USERS_MESSAGES_EMAIL_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED{#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`sending_ip` | `null,` `string` | 이메일 전송이 이루어진 IP 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`bounce_reason` | `null,` `string` | [PII] 이 반송 이벤트에 대해 수신된 SMTP 이유 코드 및 사용자 친화적 메시지
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`is_drop` | `null, boolean` | 이 이벤트가 드롭 이벤트로 계산됨을 나타냅니다.
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED{#USERS_MESSAGES_EMAIL_CLICK_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`url` | `null,` `string` | 사용자가 클릭한 URL
`user_agent` | `null,` `string` | 클릭이 발생한 사용자 에이전트
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`link_id` | `null,` `string` | 클릭한 링크의 고유 ID(Braze에서 생성)
`link_alias` | `null,` `string` | 이 링크 ID와 연결된 별칭
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`is_amp` | `null, boolean` | AMP 이벤트임을 나타냅니다.
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`is_suspected_bot_click` | `null, boolean` | 이 이벤트가 봇 이벤트로 처리되었는지 여부
`suspected_bot_click_reason` | `null, object` | 이 이벤트가 봇으로 분류된 이유
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED{#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`email_address` | `null,` `string` | [PII] 사용자의 이메일 주소
`recipient_domain` | `null,` `string` | 수신자의 이메일 도메인
`esp` | `null,` `string` | 이벤트와 관련된 이메일 서비스 공급자(Sparkpost, SendGrid 또는 Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`ip_pool` | `null,` `string` | 이메일이 발송된 IP 풀
`sending_ip` | `null,` `string` | 이메일 전송이 이루어진 IP 주소
`timezone` | `null,` `string` | 사용자의 표준 시간대
`deferral_reason` | `null,` `string` | [PII] 이 지연 이벤트에 대해 수신된 SMTP 이유 코드 및 사용자 친화적 메시지
`attempt_count` | `null, int` | 메시지 전송 시도 횟수
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED{#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`sending_ip` | `null,` `string` | 이메일이 전송된 IP 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED{#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`user_agent` | `null,` `string` | 스팸 신고가 발생한 사용자 에이전트
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED{#USERS_MESSAGES_EMAIL_OPEN_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`user_agent` | `null,` `string` | 오픈이 발생한 사용자 에이전트
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`machine_open` | `null,` `string` | 예를 들어 MPP가 활성화된 Apple 기기에서 사용자 인게이지먼트 없이 열기 이벤트가 트리거되는 경우 'true'로 채워집니다. 보다 세분화된 정보를 제공하기 위해 시간이 지남에 따라 값이 변경될 수 있습니다.
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`is_amp` | `null, boolean` | AMP 이벤트임을 나타냅니다.
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED{#USERS_MESSAGES_EMAIL_SEND_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`message_extras` | `null,` `string` | [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`sf_created_at` | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED{#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`sending_ip` | `null,` `string` | 이메일 전송이 이루어진 IP 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`bounce_reason` | `null,` `string` | [PII] 이 반송 이벤트에 대해 수신된 SMTP 이유 코드 및 사용자 친화적 메시지
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED{#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED{#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 BSON ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`feature_flag_id_name` | `null,` `string` | 기능 플래그 롤아웃 식별자
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`gender` | `null,` `string` | [PII] 사용자의 성별
`browser` | `null,` `string` | 기기 브라우저 - 추출됨user_agent\- 열림이 발생한
`carrier` | `null,` `string` | 기기 이동 통신사
`country` | `null,` `string` | [PII] 사용자의 국가
`device_model` | `null,` `string` | 기기 모델
`language` | `null,` `string` | [PII] 사용자의 언어
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`resolution` | `null,` `string` | 기기 해상도
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`timezone` | `null,` `string` | 사용자의 표준 시간대
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED{#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,` `string` | 카드의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 디바이스의 브라우저
`version` | `string` | 인앱 메시지, 레거시 또는 트리거된 메시지 버전
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | `ios_idfa`, `google_ad_id`, `windows_ad_id`, 또는 `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED{#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,` `string` | 카드의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기의 해상도
`carrier` | `null,` `string` | 기기의 통신사
`browser` | `null,` `string` | 기기의 브라우저
`version` | `string` | 인앱 메시지, 레거시 또는 트리거된 메시지 버전
`button_id` | `null,` `string` | 클릭한 버튼의 ID(클릭이 버튼 클릭을 나타내는 경우)
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | `ios_idfa`, `google_ad_id`, `windows_ad_id`, 또는 `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED{#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,` `string` | 카드의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기의 해상도
`carrier` | `null,` `string` | 기기의 통신사
`browser` | `null,` `string` | 기기의 브라우저
`version` | `string` | 인앱 메시지, 레거시 또는 트리거된 메시지 버전
`ad_id` | `null,` `string` | [PII] 광고 식별자
`ad_id_type` | `null,` `string` | `ios_idfa`, `google_ad_id`, `windows_ad_id`, 또는 `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | 디바이스에 대한 광고 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`message_extras` | `null,` `string` | [PII] 액체 렌더링 중 태그된 키-값 페어의 JSON 문자열
`locale_key` | `null,` `string` | [PII] 이 메시지를 구성하는 데 사용된 번역에 해당하는 키(예: 'en-us'). 기본값은 null입니다.
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_ABORT_SHARED{#USERS_MESSAGES_LINE_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 128자)
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`line_channel_id` | `null,` `string` | 메시지가 전송되거나 수신된 LINE 채널 ID
`line_channel_name` | `null,` `string` | 메시지가 전송되거나 수신된 LINE 채널 이름
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`native_line_id` | `null,` `string` | [PII] 메시지가 발신되거나 수신된 사용자의 라인 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`timezone` | `null,` `string` | 사용자의 표준 시간대
`campaign_name` | `null,` `string` | 캠페인 이름
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_CLICK_SHARED{#USERS_MESSAGES_LINE_CLICK_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`timezone` | `null,` `string` | 사용자의 표준 시간대
`native_line_id` | `null,` `string` | [PII] 메시지가 발신되거나 수신된 사용자의 라인 ID
`line_channel_id` | `null,` `string` | 메시지가 전송되거나 수신된 LINE 채널 ID
`line_channel_name` | `null,` `string` | 메시지가 전송되거나 수신된 LINE 채널 이름
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_name` | `null,` `string` | 캠페인 이름
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`is_suspected_bot_click` | `null, boolean` | 이 이벤트가 봇 이벤트로 처리되었는지 여부
`short_url` | `null,` `string` | 클릭된 짧은 URL
`url` | `null,` `string` | 사용자가 클릭한 URL
`user_agent` | `null,` `string` | 스팸 신고가 발생한 사용자 에이전트
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED{#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_name` | `null,` `string` | 캠페인 이름
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`line_channel_id` | `null,` `string` | 메시지가 전송되거나 수신된 LINE 채널 ID
`line_channel_name` | `null,` `string` | 메시지가 전송되거나 수신된 LINE 채널 이름
`media_id` | `null,` `string` | LINE에서 생성된 ID로, 이를 통해 LINE에서 수신된 미디어를 검색할 수 있습니다.
`message_body` | `null,` `string` | 사용자의 입력 응답
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`native_line_id` | `null,` `string` | [PII] 메시지가 발신되거나 수신된 사용자의 라인 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`timezone` | `null,` `string` | 사용자의 표준 시간대
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_SEND_SHARED{#USERS_MESSAGES_LINE_SEND_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_name` | `null,` `string` | 캠페인 이름
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`line_channel_id` | `null,` `string` | 메시지가 전송되거나 수신된 LINE 채널 ID
`line_channel_name` | `null,` `string` | 메시지가 전송되거나 수신된 LINE 채널 이름
`message_extras` | `null,` `string` | [PII] 액체 렌더링 중 태그된 키-값 페어의 JSON 문자열
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`native_line_id` | `null,` `string` | [PII] 메시지가 발신되거나 수신된 사용자의 라인 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`timezone` | `null,` `string` | 사용자의 표준 시간대
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED{#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`activity_id` | `null,` `string` | 실시간 활동 식별자
`activity_attributes_type` | `null,` `string` | 실시간 활동 속성 유형
`push_to_start_token` | `null,` `string` | 라이브 액티비티 시작 토큰 푸시
`update_token` | `null,` `string` | 실시간 활동 업데이트 토큰
`live_activity_event_type` | `null,` `string` | 라이브 액티비티의 이벤트 유형. ['시작', '업데이트', '종료'] 중 하나
`live_activity_event_outcome` | `null,` `string` | 실시간 활동 이벤트 결과
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED{#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`activity_id` | `null,` `string` | 실시간 활동 식별자
`activity_attributes_type` | `null,` `string` | 실시간 활동 속성 유형
`push_to_start_token` | `null,` `string` | 라이브 액티비티 시작 토큰 푸시
`update_token` | `null,` `string` | 실시간 활동 업데이트 토큰
`live_activity_event_type` | `null,` `string` | 라이브 액티비티의 이벤트 유형. ['시작', '업데이트', '종료'] 중 하나
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED{#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,` `string` | 카드의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 기기 브라우저 - 추출됨user_agent\- 열림이 발생한
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 128자)
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED{#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,` `string` | 카드의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 기기 브라우저 - 추출됨user_agent\- 열림이 발생한
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED{#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,` `string` | 카드의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 기기 브라우저 - 추출됨user_agent\- 열림이 발생한
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED{#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 전달 시도를 받은 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`platform` | `string` | 디바이스 플랫폼
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED{#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`push_token` | `null,` `string` | 반송된 푸시 토큰
`device_id` | `null,` `string` | 전달 시도를 보냈으나 반송한 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`platform` | `null,` `string` | 디바이스 플랫폼
`ad_id` | `null,` `string` | [PII] 전달 시도를 한 기기의 광고 ID
`ad_id_type` | `null,` `string` | 광고 ID 유형
`ad_tracking_enabled` | `null, boolean` | 광고에 대한 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED{#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 디바이스의 브라우저
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED{#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
이 이벤트는 [Swift 소프트웨어 개발 키트](https://github.com/braze-inc/braze-swift-sdk)에서 지원되지 않으며, [Objective-C 소프트웨어 개발 키트](https://github.com/Appboy/appboy-ios-sdk)에서는 사용 중단되었습니다.
{% endalert %}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 디바이스의 브라우저
`ad_id` | `null,` `string` | [PII] 전달 시도를 한 기기의 광고 ID
`ad_id_type` | `null,` `string` | 광고 ID 유형
`ad_tracking_enabled` | `null, boolean` | 광고에 대한 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED{#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 디바이스의 브라우저
`button_string` | `null,` `string` | 푸시 알림 버튼 클릭 식별자(button_string). 버튼 클릭이 아닌 경우 null
`button_action_type` | `null,` `string` | 푸시 알림 버튼의 동작 유형입니다. [URI,DEEP_LINK,  NONE, CLOSE] 중 하나. 버튼 클릭이 아닌 경우 null
`slide_id` | `null,` `string` | 사용자가 클릭한 푸시 캐러셀 슬라이드의 슬라이드 식별자
`slide_action_type` | `null,` `string` | 푸시 캐러셀 슬라이드의 동작 유형
`ad_id` | `null,` `string` | [PII] 전달 시도를 한 기기의 광고 ID
`ad_id_type` | `null,` `string` | 광고 ID 유형
`ad_tracking_enabled` | `null, boolean` | 광고에 대한 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED{#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`push_token` | `null,` `string` | 전달을 시도한 푸시 토큰은 다음과 같습니다
`device_id` | `null,` `string` | 전달 시도를 받은 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`platform` | `string` | 디바이스 플랫폼
`ad_id` | `null,` `string` | [PII] 전달 시도를 한 기기의 광고 ID
`ad_id_type` | `null,` `string` | 광고 ID 유형
`ad_tracking_enabled` | `null, boolean` | 광고에 대한 추적 활성화 여부
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`message_extras` | `null,` `string` | [PII] 액체 렌더링 중 태그된 키-값 페어의 JSON 문자열
`is_sampled` | `null,` `string` | 푸시 전송이 샘플링되었는지 여부와 전달 이벤트를 예상했는지 여부를 나타냅니다.
`locale_key` | `null,` `string` | [PII] 이 메시지를 구성하는 데 사용된 번역에 해당하는 키(예: 'en-us'). 기본값은 null입니다.
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_ABORT_SHARED{#USERS_MESSAGES_RCS_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 128자)
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_name` | `null,` `string` | 캠페인 이름
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_name` | `null,` `string` | 캔버스 이름
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`canvas_variation_name` | `null,` `string` | 이 사용자가 받은 캔버스 변형의 이름
`message_variation_name` | `null,` `string` | 메시지 변형의 이름
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_CLICK_SHARED{#USERS_MESSAGES_RCS_CLICK_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`campaign_name` | `null,` `string` | 캠페인 이름
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_name` | `null,` `string` | 캔버스 이름
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`is_suspected_bot_click` | `null, boolean` | 이 이벤트가 봇 이벤트로 처리되었는지 여부
`message_variation_name` | `null,` `string` | 메시지 변형의 이름
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`short_url` | `null,` `string` | 클릭된 짧은 URL
`suspected_bot_click_reason` | `null,` `string` | 이 이벤트가 봇으로 분류된 이유
`user_agent` | `null,` `string` | 스팸 신고가 발생한 사용자 에이전트
`user_phone_number` | `null,` `string` | [PII] 메시지를 수신한 사용자의 전화번호
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`interaction_type` | `null,` `string` | 클릭을 유발한 상호작용의 유형. 예시 문자열 값: 텍스트 URL, 답장, URL 열기
`element_label` | `null,` `string` | 클릭된 요소에 대한 선택적 세부 정보(예: 제안된 답글 또는 버튼의 텍스트)
`element_type` | `null,` `string` | 제안과 버튼에 공통으로 나타나는 요소가interaction_type 제안에서 비롯되었는지 버튼에서 비롯되었는지 지정합니다. 예시: 제안, 버튼
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`url` | `null,` `string` | 사용자가 클릭한 URL
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`canvas_variation_name` | `null,` `string` | 이 사용자가 받은 캔버스 변형의 이름
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED{#USERS_MESSAGES_RCS_DELIVERY_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`campaign_name` | `null,` `string` | 캠페인 이름
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_name` | `null,` `string` | 캔버스 이름
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`canvas_variation_name` | `null,` `string` | 이 사용자가 받은 캔버스 변형의 이름
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`message_variation_name` | `null,` `string` | 메시지 변형의 이름
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`to_phone_number` | `null,` `string` | [PII] 메시지를 수신하는 사용자의 전화번호 (예: +14155552671) 형식e.164
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`from_rcs_sender` | `null,` `string` | 메시지 전송에 사용된 RCS 발신자 ID 또는 에이전트 이름
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED{#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`action` | `null,` `string` | 이 메시지에 대한 조치 내용. (예: 가입, 탈퇴 또는 없음).
`campaign_name` | `null,` `string` | 캠페인 이름
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_name` | `null,` `string` | 캔버스 이름
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`media_urls` | `null,` `string` | 사용자의 미디어 URL
`message_variation_name` | `null,` `string` | 메시지 변형의 이름
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`user_phone_number` | `null,` `string` | [PII] 메시지를 수신한 사용자의 전화번호
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`message_body` | `null,` `string` | 사용자의 입력 응답
`to_rcs_sender` | `null,` `string` | 메시지가 전송된 인바운드 RCS 발신자
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_READ_SHARED{#USERS_MESSAGES_RCS_READ_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`campaign_name` | `null,` `string` | 캠페인 이름
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_name` | `null,` `string` | 캔버스 이름
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`canvas_variation_name` | `null,` `string` | 이 사용자가 받은 캔버스 변형의 이름
`message_variation_name` | `null,` `string` | 메시지 변형의 이름
`to_phone_number` | `null,` `string` | [PII] 메시지를 수신하는 사용자의 전화번호 (예: +14155552671) 형식e.164
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_REJECTION_SHARED{#USERS_MESSAGES_RCS_REJECTION_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`campaign_name` | `null,` `string` | 캠페인 이름
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_name` | `null,` `string` | 캔버스 이름
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`canvas_variation_name` | `null,` `string` | 이 사용자가 받은 캔버스 변형의 이름
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`error` | `null,` `string` | 오류 이름
`from_rcs_sender` | `null,` `string` | 메시지 전송에 사용된 RCS 발신자 ID 또는 에이전트 이름
`is_sms_fallback` | `null, boolean` | 이 거부된 RCS 메시지에 대해 SMS 대체 전송이 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트에 연결/페어링됩니다
`message_variation_name` | `null,` `string` | 메시지 변형의 이름
`provider_error_code` | `null,` `string` | 공급자로부터의 오류 코드
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`to_phone_number` | `null,` `string` | [PII] 메시지를 수신하는 사용자의 전화번호 (예: +14155552671) 형식e.164
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_SEND_SHARED{#USERS_MESSAGES_RCS_SEND_SHARED}

필드 | 유형 | Description
------|------|------------
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`campaign_name` | `null,` `string` | 캠페인 이름
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_name` | `null,` `string` | 캔버스 이름
`canvas_step_name` | `null,` `string` | 캔버스 단계 이름
`canvas_variation_name` | `null,` `string` | 이 사용자가 받은 캔버스 변형의 이름
`category` | `null,` `string` | 키워드 카테고리 이름, 자동 응답 메시지에만 적용됨: '옵트인', '수신 거부', '도움말' 또는 커스텀 값
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`from_rcs_sender` | `null,` `string` | 메시지 전송에 사용된 RCS 발신자 ID 또는 에이전트 이름
`message_extras` | `null,` `string` | 액체 렌더링 중 태그된 키-값 페어의 JSON 문자열
`message_variation_name` | `null,` `string` | 메시지 변형의 이름
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`to_phone_number` | `null,` `string` | [PII] 메시지를 수신하는 사용자의 전화번호 (예: +14155552671) 형식e.164
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED{#USERS_MESSAGES_SMS_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED{#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`from_phone_number` | `null,` `string` | SMS 메시지를 보낸 전화번호
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED{#USERS_MESSAGES_SMS_DELIVERY_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`from_phone_number` | `null,` `string` | SMS 메시지를 보낸 전화번호
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`is_sms_fallback` | `null, boolean` | 이 거부된 RCS 메시지에 대해 SMS 대체 전송이 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트에 연결/페어링됩니다
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED{#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
`error` | `null,` `string` | 오류 이름
`provider_error_code` | `null,` `string` | SMS 서비스 제공업체의 오류 코드
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`is_sms_fallback` | `null, boolean` | 이 거부된 RCS 메시지에 대해 SMS 대체 전송이 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트에 연결/페어링됩니다
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED{#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `null,` `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 인바운드 전화번호와 연결된 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`user_phone_number` | `string` | [PII] 메시지를 수신한 사용자의 전화번호
`subscription_group_id` | `null,` `string` | 이 SMS 메시지의 대상이 되는 구독 그룹의 ID
`subscription_group_api_id` | `null,` `string` | 이 SMS 메시지의 대상이 되는 구독 그룹의 API ID
`inbound_phone_number` | `string` | 메시지가 전송된 인바운드 번호입니다.
`action` | `string` | 이 메시지에 대한 응답으로 취해진 조치입니다. 예: `Subscribed`, `Unsubscribed`, 또는 `None`.
`message_body` | `string` | 사용자 응답
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | 사용자의 미디어 URL
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 이벤트가 속한 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계 메시지 변형의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED{#USERS_MESSAGES_SMS_REJECTION_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`from_phone_number` | `null,` `string` | SMS 메시지를 보낸 전화번호
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
`error` | `null,` `string` | 오류 이름
`provider_error_code` | `null,` `string` | SMS 서비스 제공업체의 오류 코드
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`is_sms_fallback` | `null, boolean` | 이 거부된 RCS 메시지에 대해 SMS 대체 전송이 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트에 연결/페어링됩니다
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED{#USERS_MESSAGES_SMS_SEND_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
`category` | `null,` `string` | 키워드 카테고리 이름, 자동 답글 메시지에만 입력됩니다: '옵트인', '옵트아웃', '도움말' 또는 사용자 지정 값
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`message_extras` | `null,` `string` | [PII] 액체 렌더링 중 태그된 키-값 페어의 JSON 문자열
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED{#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `null,` `string` | 사용자 클릭 추적을 사용하지 않은 short_url경우 대상 사용자의 Braze short_url,ID는 null입니다.
`external_user_id` | `null,` `string` | [PII] 타겟팅된 사용자의 외부 IDshort_url (존재하는 경우), 사용자 클릭 추적을 사용하지 않은short_url 경우 null
`app_group_api_id` | `null,` `string` | 생성에 사용된 작업 공간의 API ID short_url
`time` | `int` | 클릭된 short_url시점의 Unix 타임스탬프
`timezone` | `null,` `string` | 사용자의 표준 시간대
`campaign_id` | `null,` `string` | 캠페인을 위해short_url 생성된 Braze ID, 캠페인이 아닌 경우 null
`campaign_api_id` | `null,` `string` | 캠페인을 위해short_url 생성된 API ID, 캠페인이 아닌 경우 null
`message_variation_api_id` | `null,` `string` | 메시지 변형이short_url생성된 API ID, 캠페인에서 생성되지 않은 경우 null
`canvas_id` | `null,` `string` | 캔버스의 Braze ID는 해당 캔버스를 위해short_url 생성되었으며, 캔버스에서 생성되지 않은 경우 null입니다.
`canvas_api_id` | `null,` `string` | API ID는 캔버스를 위해short_url 생성되었습니다. 캔버스에서 생성되지 않은 경우 null입니다.
`canvas_variation_api_id` | `null,` `string` | 캔버스 변형에 대해 생성된 APIshort_url ID, 캔버스에서 생성되지 않은 경우 null
`canvas_step_api_id` | `null,` `string` | 캔버스 단계용으로short_url생성된 API ID입니다. 캔버스에서 생성되지 않은 경우 null입니다.
`canvas_step_message_variation_api_id` | `null,` `string` | 캔버스 단계 메시지 변형에 대해 생성된 APIshort_url ID, 캔버스에서 생성되지 않은 경우 null
`url` | `string` | 메시지에 포함된 원본 URL은 다음으로 리디렉션됩니다. short_url
`short_url` | `string` | 클릭한 단축 URL
`user_agent` | `null,` `string` | 요청하는 사용자 에이전트 short_url
`user_phone_number` | `string` | [PII] 사용자의 전화번호
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`is_suspected_bot_click` | `null, boolean` | 이 이벤트가 봇 이벤트로 처리되었는지 여부
`suspected_bot_click_reason` | `null, object` | 이 이벤트가 봇으로 분류된 이유
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED{#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED{#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

필드 | 유형 | Description
------|------|------------
`http_status_code` | `null, int` | 응답의 HTTP 코드
`endpoint_url` | `null,` `string` | 요청 중인 엔드포인트 URL
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 BSON ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`content_length` | `null, int` | 응답의 콘텐츠 길이
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`host` | `null,` `string` | 요청의 호스트
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`raw_response` | `null,` `string` | 엔드포인트에서 잘린 원시 응답
`retry_count` | `null, int` | 시도된 재시도 횟수
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`url_path` | `null,` `string` | 요청된 URL의 경로
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`webhook_duration` | `null, int` | 이 요청의 총 소요 시간 (밀리초 단위)
`webhook_failure_source` | `null,` `string` | 오류가 Braze에서 발생했는지, 아니면 엔드포인트 자체에서 발생했는지 확인하기 위해. 소스 필드는 외부 엔드포인트일 수 있으며, 상태 코드가 없으면 호스트에 연결할 수 없는 것으로 처리합니다.
`is_terminal` | `null, boolean` | 이 사건이 발송의 최종 시도였는지
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED{#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`gender` | `null,` `string` | [PII] 사용자의 성별
`country` | `null,` `string` | [PII] 사용자의 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자의 언어
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`message_extras` | `null,` `string` | [PII] 액체 렌더링 중 태그된 키-값 페어의 JSON 문자열
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED{#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`to_phone_number` | 	`null,` `string` | [PII] 수신자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`timezone` | `null,` `string` | 사용자의 표준 시간대
`app_group_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`abort_type` | `null,` `string` | 낙태 유형, 그 중 하나 ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`sf_created_at` | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED{#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 ID
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`app_group_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 시점의 Unix 타임스탬프
`timezone` | `null,` `string` | 사용자의 표준 시간대
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 BSON ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`url` | `null,` `string` | 사용자가 클릭한 URL
`short_url` | `null,` `string` | 클릭된 짧은 URL
`user_agent` | `null,` `string` | 스팸 신고가 발생한 사용자 에이전트
`user_phone_number` | `null,` `string` | [PII] 메시지를 수신한 사용자의 전화번호
`sf_created_at` | `timestamp`, `null` | 이 사건이 스노우파이프에 의해 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED{#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`timezone` | `null,` `string` | 사용자의 표준 시간대
`from_phone_number` | `null,` `string` | WhatsApp 메시지를 보낸 전화번호
`app_group_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`sf_created_at` | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때      
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`flow_id` | `null,` `string` | WhatsApp 매니저에서 플로우의 고유 ID. 사용자가 WhatsApp Flow에 응답하는 경우 true를 반환합니다.
`template_name` | `null,` `string` | [PII] WhatsApp 매니저 내 템플릿 이름. 템플릿 메시지를 보낼 경우 표시
`message_id` | `null,` `string` | 이 메시지에 대해 Meta에서 생성한 고유 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED{#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`timezone` | `null,` `string` | 사용자의 표준 시간대
`from_phone_number` | `null,` `string` | WhatsApp 메시지를 보낸 전화번호
`app_group_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`provider_error_code` | `null,` `string` | WhatsApp의 오류 코드
`provider_error_title` | `null, ` `string` | WhatsApp의 오류 제목
`sf_created_at` | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때      
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`message_id` | `null,` `string` | 이 메시지에 대해 Meta에서 생성한 고유 ID
`template_name` | `null,` `string` | [PII] WhatsApp 매니저 내 템플릿 이름. 템플릿 메시지를 보낼 경우 표시
`flow_id` | `null,` `string` | WhatsApp 매니저에서 플로우의 고유 ID. 사용자가 WhatsApp Flow에 응답하는 경우 true를 반환합니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED{#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`user_phone_number` | `string` | [PII] 메시지를 수신한 사용자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`inbound_phone_number` | `string` | 메시지가 전송된 인바운드 번호입니다.
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`timezone` | `null,` `string` | 사용자의 표준 시간대
`app_group_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`message_body` | `string` | 사용자 응답
`quick_reply_text` | `string` | 사용자가 누른 버튼의 텍스트
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | 사용자의 미디어 URL
`action` | `string` | 이 메시지에 대한 응답으로 취해진 조치입니다. 예: `Subscribed`, `Unsubscribed`, 또는 `None`.
`sf_created_at` | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때      
`catalog_id` | `null,` `string` | 인바운드 메시지에서 제품이 참조된 경우 해당 제품의 카탈로그 ID. 그렇지 않으면 비어 있다.
`product_id` | `null,` `string` | 구매한 제품의 ID
`flow_id` | `null,` `string` | WhatsApp 매니저에서 플로우의 고유 ID. 사용자가 WhatsApp Flow에 응답하는 경우 true를 반환합니다.
`flow_response_json` | `null,` `string` | [PII] 사용자가 응답한 양식 값들. 사용자가 WhatsApp Flow에 응답하는 경우 true를 반환합니다.
`message_id` | `null,` `string` | 이 메시지에 대해 Meta에서 생성한 고유 ID
`in_reply_to` | `null,` `string` | 이 메시지가 답장한 메시지의 제목message_id
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED{#USERS_MESSAGES_WHATSAPP_READ_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`timezone` | `null,` `string` | 사용자의 표준 시간대
`from_phone_number` | `null,` `string` | WhatsApp 메시지를 보낸 전화번호
`app_group_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`sf_created_at` | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때      
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`template_name` | `null,` `string` | [PII] WhatsApp 매니저 내 템플릿 이름. 템플릿 메시지를 보낼 경우 표시
`message_id` | `null,` `string` | 이 메시지에 대해 Meta에서 생성한 고유 ID
`flow_id` | `null,` `string` | WhatsApp 매니저에서 플로우의 고유 ID. 사용자가 WhatsApp Flow에 응답하는 경우 true를 반환합니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED{#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

필드 | 유형 | Description
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`to_phone_number` | `null,` `string`	| [PII] 수신자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`timezone` | `null,` `string` | 사용자의 표준 시간대
`from_phone_number` | `null,` `string` | WhatsApp 메시지를 보낸 전화번호
`app_group_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID는 다음과 같습니다.
`campaign_api_id` | `null,` `string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,` `string` | 이 사용자가 받은 메시지 변형의 API ID
`canvas_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 내부용 브레이즈 ID
`canvas_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스의 API ID
`canvas_variation_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 변형의 API ID
`canvas_step_api_id` | `null,` `string` | 이 이벤트가 속한 캔버스 단계의 API ID
`canvas_step_message_variation_api_id` | `null,` `string` | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID
`dispatch_id` | `null,` `string` | 이 메시지가 속한 발송의 ID
`message_extras` | `null,` `string` | [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`sf_created_at` | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때      
`send_id` | `null,` `string` | 이 메시지가 속한 메시지 전송 ID
`flow_id` | `null,` `string` | WhatsApp 매니저에서 플로우의 고유 ID. 사용자가 WhatsApp Flow에 응답하는 경우 true를 반환합니다.
`template_name` | `null,` `string` | [PII] WhatsApp 매니저 내 템플릿 이름. 템플릿 메시지를 보낼 경우 표시
`message_id` | `null,` `string` | 이 메시지에 대해 Meta에서 생성한 고유 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Users

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED{#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| 필드                       | 유형                     | Description                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                  |
| `app_group_id`              | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID      |
| `app_group_api_id`          | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID       |
| `user_id`                   | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID      |
| `external_user_id`          | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                 |
| `time`                      | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프         |
| `random_bucket_number`      | `int`, `null`       | 사용자에게 할당된 현재 임의의 버킷 번호  |
| `prev_random_bucket_number` | `int`, `null`       | 사용자에게 할당된 이전 무작위 버킷 번호 |
| `sf_created_at`             | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED{#USERS_USERDELETEREQUEST_SHARED}

| 필드              | 유형                     | Description                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                             |
| `user_id`          | `string`, `null`    | 삭제된 사용자의 Braze ID                          |
| `app_group_id`     | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                 |
| `app_group_api_id` | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID                  |
| `time`             | `int`, `null`       | 사용자 삭제 요청이 처리된 유닉스 타임스탬프 |
| `sf_created_at`    | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED{#USERS_USERORPHAN_SHARED}

| 필드              | 유형                     | Description                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                             |
| `user_id`          | `string`, `null`    | 고아가 된 사용자의 Braze ID                                         |
| `external_user_id` | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                            |
| `device_id`        | `string`, `null`    | 사용자가 익명인 경우 이 사용자와 연결된 디바이스의 ID입니다.          |
| `app_group_id`     | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                                 |
| `app_group_api_id` | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID                                  |
| `app_api_id`       | `string`, `null`    | 고아가 된 사용자가 소속된 앱의 API ID                               |
| `time`             | `int`, `null`       | 사용자가 고아가 된 유닉스 타임스탬프                                 |
| `orphaned_by_id`   | `string`, `null`    | 고아가 된 사용자의 프로필과 프로필이 병합된 사용자의 Braze ID |
| `sf_created_at`    | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
