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
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | 원래 예정된 콘텐츠 카드 메시지가 어떤 이유로 중단되었습니다.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | 사용자가 콘텐츠 카드를 클릭하는 경우
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | 사용자가 콘텐츠 카드를 해지하는 경우
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | 사용자가 콘텐츠 카드를 볼 때
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | 사용자에게 콘텐츠 카드를 보낼 때
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | 원래 예정된 이메일 메시지가 어떤 이유로 중단되었습니다.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | 이메일 서비스 공급자가 하드 바운스를 반환했습니다. 하드 바운스는 영구적인 전달 가능성 실패를 의미합니다.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | 사용자가 이메일의 링크를 클릭하는 경우
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | 이메일이 전달될 때
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | 이메일이 스팸으로 표시된 경우
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | 사용자가 이메일을 여는 경우
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | 사용자에게 이메일을 보낼 때
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | 이메일 소프트 바운스 발생 시
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | 사용자가 이메일 구독을 취소하는 경우
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | 원래 예정된 인앱 메시지가 어떤 이유로 인해 중단되었습니다.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | 사용자가 인앱 메시지를 클릭하는 경우
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | 사용자가 인앱 메시지를 볼 때
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | 원래 예정되어 있던 뉴스피드 카드 메시지가 어떤 이유로 중단되었습니다.
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | 사용자가 뉴스피드 카드를 클릭하는 경우
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | 사용자가 뉴스피드 카드를 볼 때
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | 원래 예정된 푸시 알림 메시지가 어떤 이유로 인해 중단되었습니다.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | 푸시 알림이 반송되는 경우
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | 사용자가 알림을 받은 후 알림을 클릭하지 않고 앱을 여는 경우
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | 사용자가 앱이 열려 있는 동안 푸시 알림을 받는 경우
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | 사용자가 푸시 알림을 열거나 푸시 알림 버튼(앱을 열지 않는 닫기 버튼 포함)을 클릭한 경우. <br><br> 푸시 버튼 동작에는 여러 가지 결과가 있습니다. 아니요, 거부 및 취소 작업은 "클릭"이고 수락 작업은 "열기"입니다. 이 표에는 두 가지가 모두 표시되어 있지만 **BUTTON_ACTION_TYPE** 열에서 구분할 수 있습니다. 예를 들어 쿼리를 사용하여 아니요, 거부 또는 취소가 아닌 `BUTTON_ACTION_TYPE`으로 그룹화할 수 있습니다.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | 사용자에게 푸시 알림을 보낼 때
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | 원래 예정된 SMS 메시지가 어떤 이유로 인해 중단되었습니다.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | 이동 통신사로 SMS 메시지가 전송되는 경우
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | SMS 메시지가 전달되는 경우
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Braze가 SMS 서비스 제공업체에 SMS 메시지를 전달할 수 없는 경우
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | 사용자로부터 SMS 메시지를 수신한 경우
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | 사용자에게 SMS 메시지가 전달되지 않은 경우
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | SMS 메시지가 전송되는 경우
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | 사용자가 SMS 메시지에 포함된 Braze 단축 URL을 클릭하는 경우
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | 원래 예정된 웹훅 메시지가 어떤 이유로 중단되었습니다.
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | 사용자에 대한 웹훅을 보낼 때
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | 원래 예정된 WhatsApp 메시지가 어떤 이유로 중단되었습니다.
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |WhatsApp 메시지가 전달되는 경우
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | WhatsApp 메시지가 사용자에게 전달되지 않은 경우
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | 사용자로부터 WhatsApp 메시지를 수신한 경우
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | 사용자가 WhatsApp 메시지를 열면
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | 사용자에게 WhatsApp 메시지를 보낼 때
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | 사용자의 임의 버킷 번호가 변경된 경우
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | 고객 요청에 의해 사용자가 삭제된 경우
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | 사용자가 다른 사용자의 프로필과 병합되어 원래 프로필이 고아가 된 경우


## 행동

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 이 작업이 발생한 앱의 API ID
`time` | `int` | 사용자가 이벤트를 수행한 유닉스 타임스탬프
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 설치한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 사용자가 설치한 유닉스 타임스탬프
`source` | `string` | 기여도의 출처
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 제거한 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 제거된 앱의 API ID
`time` | `int` | 사용자가 제거한 unix 타임스탬프
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 작업을 수행하는 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 이 세션이 발생한 앱의 API ID
`time` | `int` | 세션이 시작된 유닉스 타임스탬프
`session_id` | `string` | 세션의 UUID
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`device_id` | `null,` `string` | 세션이 발생한 기기의 ID
`sdk_version` | `null,` `string` | 세션 중에 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 뉴스피드를 본 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 사용자가 뉴스피드를 본 앱의 API ID
`time` | `int` | 사용자가 뉴스피드를 본 유닉스 타임스탬프
`device_id` | `null,` `string` | 노출이 발생한 기기의 ID
`sdk_version` | `null,` `string` | 임프레션 중에 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 작업을 수행하는 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,` `string` | 이 세션이 발생한 앱의 API ID
`time` | `int` | 세션이 종료된 유닉스 타임스탬프
`duration` | `null, float` | 세션 기간
`session_id` | `string` | 세션의 UUID
`device_id` | `null,` `string` | 세션이 발생한 기기의 ID
`sdk_version` | `null,` `string` | 세션 중에 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 영향을 받은 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`email_address` | `null,` `string` | [PII] 사용자의 이메일 주소
`state_change_source` | `null,` `string` | 상태 변경의 소스(REST, SDK, 대시보드 등)
`subscription_status` | `string` | 구독 상태: '구독함' 또는 '구독 취소함'
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 영향을 받은 사용자의 Braze ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,` `string` | 사용자가 익명인 경우 이 사용자와 연결되는 `device_id`
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`email_address` | `null,` `string` | [PII] 사용자의 이메일 주소
`phone_number` | `null,` `string` | [PII] e164 형식의 사용자 전화번호
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
`subscription_status` | `string` | 구독 상태: '구독함' 또는 '구독 취소함'
`time` | `int` | 구독 상태가 변경된 유닉스 타임스탬프
`timezone` | `null,` `string` | 사용자의 표준 시간대
`send_id` | `null,` `string` | 이 구독 상태 변경 작업이 발생한 메시지 전송 ID
`state_change_source` | `null,` `string` | 상태 변경의 소스(REST, SDK, 대시보드 등)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 캠페인

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`revenue` | `long` | 발생한 USD 수익(센트) 금액
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 캔버스

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| 필드                                  | 유형                     | 설명                                                                                                     |
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

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| 필드                                  | 유형                     | 설명                                                                                                     |
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
| `gender`                               | `string`, `null`    | [PII] 사용자 성별                                                                                        |
| `country`                              | `string`, `null`    | [PII] 사용자 국가                                                                                       |
| `timezone`                             | `string`, `null`    | 사용자의 표준 시간대                                                                                            |
| `language`                             | `string`, `null`    | [PII] 사용자 언어                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| 필드                     | 유형                     | 설명                                                          |
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
| `gender`                  | `string`, `null`    | [PII] 사용자 성별                                             |
| `country`                 | `string`, `null`    | [PII] 사용자 국가                                            |
| `timezone`                | `string`, `null`    | 사용자의 표준 시간대                                                 |
| `language`                | `string`, `null`    | [PII] 사용자 언어                                           |
| `in_control_group`        | `boolean`, `null`   | 사용자가 대조 그룹에 등록되어 있는 경우 참입니다.                   |
| `sf_created_at`           | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| 필드                     | 유형                     | 설명                                                          |
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
| `canvas_step_api_id`      | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `sf_created_at`           | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| 필드                     | 유형                     | 설명                                                          |
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
| `canvas_step_api_id`      | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `sf_created_at`           | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| 필드                       | 유형                     | 설명                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                                                               |
| `user_id`                   | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                                                                   |
| `external_user_id`          | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                                                              |
| `device_id`                 | `string`, `null`    | 사용자가 익명인 경우 이 사용자와 연결된 디바이스의 ID입니다.                                            |
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| 필드                     | 유형                     | 설명                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                 | `string`, `null`    | 이 이벤트를 수행한 사용자의 브레이즈 ID                        |
| `external_user_id`        | `string`, `null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `device_id`               | `string`, `null`    | 사용자가 익명인 경우 이 사용자와 연결된 디바이스의 ID입니다. |
| `app_group_id`            | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `time`                    | `int`, `null`       | 이벤트가 발생한 유닉스 타임스탬프                           |
| `canvas_id`               | `string`, `null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`           | `string`, `null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id` | `string`, `null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`      | `string`, `null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `experiment_step_api_id`  | `string`, `null`    | 이 이벤트가 속한 실험 단계의 API ID                  |
| `in_control_group`        | `boolean`, `null`   | 사용자가 대조 그룹에 등록되어 있는 경우 참입니다.                   |
| `sf_created_at`           | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| 필드                                  | 유형                     | 설명                                                          |
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
| `gender`                               | `string`, `null`    | [PII] 사용자 성별                                             |
| `country`                              | `string`, `null`    | [PII] 사용자 국가                                            |
| `timezone`                             | `string`, `null`    | 사용자의 표준 시간대                                                 |
| `language`                             | `string`, `null`    | [PII] 사용자 언어                                           |
| `sf_created_at`                        | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| 필드                                  | 유형                     | 설명                                                          |
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
| `gender`                               | `string`, `null`    | [PII] 사용자 성별                                             |
| `country`                              | `string`, `null`    | [PII] 사용자 국가                                            |
| `timezone`                             | `string`, `null`    | 사용자의 표준 시간대                                                 |
| `language`                             | `string`, `null`    | [PII] 사용자 언어                                           |
| `revenue`                              | `int`, `null`       | USD로 생성된 수익 금액(센트 단위로 표시)               |
| `sf_created_at`                        | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 메시지

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`abort_type` | `null,` `string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지(최대 128자)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`content_card_id` | `string` | 이 이벤트를 생성한 카드의 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`abort_type` | `null,` `string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지(최대 128자)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`sending_ip` | `null,` `string` | 이메일 전송이 이루어진 IP 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`bounce_reason` | `null,` `string` | [PII] 이 반송 이벤트에 대해 수신된 SMTP 사유 코드 및 사용자 친화적인 메시지입니다.
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`is_drop` | `null, boolean` | 이 이벤트가 드롭 이벤트로 계산됨을 나타냅니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`url` | `null,` `string` | 사용자가 클릭한 URL
`user_agent` | `null,` `string` | 클릭이 발생한 사용자 에이전트
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`link_id` | `null,` `string` | 클릭한 링크의 고유 ID(Braze에서 생성)
`link_alias` | `null,` `string` | 이 링크 ID와 연결된 별칭
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`is_amp` | `null, boolean` | AMP 이벤트임을 나타냅니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`sending_ip` | `null,` `string` | 이메일이 전송된 IP 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`user_agent` | `null,` `string` | 스팸 신고가 발생한 사용자 에이전트
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`user_agent` | `null,` `string` | 오픈이 발생한 사용자 에이전트
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`machine_open` | `null,` `string` | 예를 들어 MPP가 활성화된 Apple 기기에서 사용자 인게이지먼트 없이 열기 이벤트가 트리거되는 경우 'true'로 채워집니다. 보다 세분화된 정보를 제공하기 위해 시간이 지남에 따라 값이 변경될 수 있습니다.
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`is_amp` | `null, boolean` | AMP 이벤트임을 나타냅니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`message_extras` | `null,` `string` | [PII] Liquid 렌더링 중 태그가 지정된 키-값 페어의 JSON 문자열
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
`sf_created_at` | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`sending_ip` | `null,` `string` | 이메일 전송이 이루어진 IP 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
`bounce_reason` | `null,` `string` | [PII] 이 반송 이벤트에 대해 수신된 SMTP 사유 코드 및 사용자 친화적인 메시지입니다.
`esp` | `null,` `string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,` `string` | 이메일용 도메인 보내기
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`ip_pool` | `null,` `string` | 이메일 전송이 이루어진 IP 풀
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
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
`abort_type` | `null,` `string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지(최대 128자)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,` `string` | 카드의 API ID
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기의 해상도
`carrier` | `null,` `string` | 기기의 통신사
`browser` | `null,` `string` | 기기의 브라우저
`abort_type` | `null,` `string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지(최대 128자)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,` `string` | 카드의 API ID
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기의 해상도
`carrier` | `null,` `string` | 기기의 통신사
`browser` | `null,` `string` | 기기의 브라우저
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 브레이즈 ID
`external_user_id` | `null,` `string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,` `string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 유닉스 타임스탬프
`app_api_id` | `null,` `string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,` `string` | 카드의 API ID
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기의 해상도
`carrier` | `null,` `string` | 기기의 통신사
`browser` | `null,` `string` | 기기의 브라우저
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`platform` | `string` | 디바이스 플랫폼
`abort_type` | `null,` `string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지(최대 128자)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`platform` | `null,` `string` | 디바이스 플랫폼
`ad_id` | `null,` `string` | [PII] 당사가 전달을 시도한 기기의 광고 ID
`ad_id_type` | `null,` `string` | 광고 ID 유형
`ad_tracking_enabled` | `null, boolean` | 광고에 대한 추적 활성화 여부
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 디바이스의 브라우저
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 디바이스의 브라우저
`ad_id` | `null,` `string` | [PII] 당사가 전달을 시도한 기기의 광고 ID
`ad_id_type` | `null,` `string` | 광고 ID 유형
`ad_tracking_enabled` | `null, boolean` | 광고에 대한 추적 활성화 여부
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`device_id` | `null,` `string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,` `string` | 이벤트 기간 동안 사용 중인 Braze SDK 버전
`platform` | `null,` `string` | 디바이스 플랫폼
`os_version` | `null,` `string` | 디바이스의 운영 체제 버전
`device_model` | `null,` `string` | 기기 모델
`resolution` | `null,` `string` | 기기 해상도
`carrier` | `null,` `string` | 기기 이동 통신사
`browser` | `null,` `string` | 디바이스의 브라우저
`button_string` | `null,` `string` | 클릭한 푸시 알림 버튼의 식별자(button_string). 버튼 클릭이 아닌 경우 null
`button_action_type` | `null,` `string` | 푸시 알림 버튼의 동작 유형입니다. [URI, DEEP_LINK, NONE, CLOSE] 중 하나. 버튼 클릭이 아닌 경우 null
`slide_id` | `null,` `string` | 사용자가 클릭한 푸시 캐러셀 슬라이드의 슬라이드 식별자
`slide_action_type` | `null,` `string` | 푸시 캐러셀 슬라이드의 동작 유형
`ad_id` | `null,` `string` | [PII] 당사가 전달을 시도한 기기의 광고 ID
`ad_id_type` | `null,` `string` | 광고 ID 유형
`ad_tracking_enabled` | `null, boolean` | 광고에 대한 추적 활성화 여부
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`platform` | `string` | 디바이스 플랫폼
`ad_id` | `null,` `string` | [PII] 당사가 전달을 시도한 기기의 광고 ID
`ad_id_type` | `null,` `string` | 광고 ID 유형
`ad_tracking_enabled` | `null, boolean` | 광고에 대한 추적 활성화 여부
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

필드 | 유형 | 설명
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
`abort_type` | `null,` `string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지(최대 128자)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`from_phone_number` | `null,` `string` | SMS 메시지를 보낸 전화번호
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`from_phone_number` | `null,` `string` | SMS 메시지를 보낸 전화번호
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
`error` | `null,` `string` | 오류 이름
`provider_error_code` | `null,` `string` | SMS 서비스 제공업체의 오류 코드
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`from_phone_number` | `null,` `string` | SMS 메시지를 보낸 전화번호
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
`error` | `null,` `string` | 오류 이름
`provider_error_code` | `null,` `string` | SMS 서비스 제공업체의 오류 코드
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`to_phone_number` | `null,` `string` | [PII] 수신자의 전화번호
`subscription_group_api_id` | `null,` `string` | 구독 그룹의 외부 ID
`category` | `null,` `string` | 키워드 카테고리 이름, 자동 답글 메시지에만 입력됩니다: '옵트인', '옵트아웃', '도움말' 또는 사용자 지정 값
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `null,` `string` | short_url이 타겟팅한 사용자의 Braze ID(short_url이 사용자 클릭 추적을 사용하지 않은 경우 null)
`external_user_id` | `null,` `string` | [PII] short_url이 타겟팅한 사용자의 외부 ID(있는 경우), short_url이 사용자 클릭 추적을 사용하지 않은 경우 null
`app_group_api_id` | `null,` `string` | short_url 생성에 사용된 워크스페이스의 API ID
`time` | `int` | short_url이 클릭된 유닉스 타임스탬프
`timezone` | `null,` `string` | 사용자의 표준 시간대
`campaign_id` | `null,` `string` | 캠페인 short_url이 생성된 캠페인의 Braze ID(캠페인이 아닌 경우 null)
`campaign_api_id` | `null,` `string` | 짧은 URL이 생성된 캠페인의 API ID(캠페인에서 생성된 것이 아닌 경우 null)
`message_variation_api_id` | `null,` `string` | 짧은 URL이 생성된 메시지 변형의 API ID(캠페인에서 생성된 것이 아닌 경우 null)입니다.
`canvas_id` | `null,` `string` | 생성된 캔버스 short_url의 Braze ID(캔버스가 아닌 경우 null)
`canvas_api_id` | `null,` `string` | 생성된 캔버스 short_url의 API ID(캔버스가 아닌 경우 null)
`canvas_variation_api_id` | `null,` `string` | 캔버스 변형 short_url이 생성된 캔버스 변형의 API ID, 캔버스에서 생성된 것이 아니라면 null입니다.
`canvas_step_api_id` | `null,` `string` | 캔버스 단계 short_url이 생성된 캔버스 단계의 API ID(캔버스에서 생성되지 않은 경우 null)
`canvas_step_message_variation_api_id` | `null,` `string` | 캔버스 단계 메시지 변형 short_url이 생성된 캔버스 단계의 API ID(캔버스에서 생성되지 않은 경우 null)입니다.
`url` | `string` | short_url에 의해 리디렉션되는 메시지에 포함된 원본 URL
`short_url` | `string` | 클릭한 단축 URL
`user_agent` | `null,` `string` | short_url을 요청하는 사용자 에이전트
`user_phone_number` | `string` | [PII] 사용자 전화번호
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
`abort_type` | `null,` `string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지(최대 128자)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

필드 | 유형 | 설명
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
`gender` | `null,` `string` | [PII] 사용자 성별
`country` | `null,` `string` | [PII] 사용자 국가
`timezone` | `null,` `string` | 사용자의 표준 시간대
`language` | `null,` `string` | [PII] 사용자 언어
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

필드 | 유형 | 설명
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
`abort_type` | `null,` `string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,` `string` | [PII] 중단 세부 정보를 설명하는 로그 메시지(최대 128자)
`sf_created_at` | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

필드 | 유형 | 설명
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

필드 | 유형 | 설명
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
`message_extras` | `null,` `string` | [PII] Liquid 렌더링 중 태그가 지정된 키-값 페어의 JSON 문자열
`sf_created_at` | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 사용자

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| 필드                       | 유형                     | 설명                                        |
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

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| 필드              | 유형                     | 설명                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`, `null`    | 이 이벤트의 글로벌 고유 ID                             |
| `user_id`          | `string`, `null`    | 삭제된 사용자의 Braze ID                          |
| `app_group_id`     | `string`, `null`    | 이 사용자가 속한 워크스페이스의 Braze ID                 |
| `app_group_api_id` | `string`, `null`    | 이 사용자가 속한 워크스페이스의 API ID                  |
| `time`             | `int`, `null`       | 사용자 삭제 요청이 처리된 유닉스 타임스탬프 |
| `sf_created_at`    | `timestamp`, `null` | 이 이벤트가 Snowpipe에 포착되었을 때                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| 필드              | 유형                     | 설명                                                                   |
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
