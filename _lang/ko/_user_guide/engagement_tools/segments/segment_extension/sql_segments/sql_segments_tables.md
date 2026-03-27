---
nav_title: "SQL 테이블 참조"
article_title: SQL 테이블 참조
page_order: 3
page_type: reference
toc_headers: h2
description: "이 페이지는 쿼리 빌더, SQL 세그먼트 확장, Snowflake 데이터 공유에서 사용되는 Snowflake SQL 테이블과 열에 대한 참조 문서입니다."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQL 테이블 참조

이 페이지는 다음 Braze 도구에서 사용할 수 있는 Snowflake SQL 테이블과 열에 대한 참조 문서입니다:

- [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/query_builder/)
- [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)
- [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

대부분의 테이블은 세 가지 도구 모두에서 사용할 수 있습니다. **Snowflake 데이터 공유 전용**으로 표시된 테이블은 Snowflake 데이터 공유에서만 사용할 수 있으며, 쿼리 빌더나 SQL 세그먼트 확장에서는 접근할 수 없습니다.

{% alert tip %}
이 SQL 테이블은 [커런츠 이벤트 용어집]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)에 문서화된 이벤트에 해당합니다. 예를 들어, SQL 테이블 `USERS_MESSAGES_EMAIL_SEND_SHARED`는 커런츠 이벤트 `users.messages.email.Send`에 해당합니다. JSON 이벤트 스키마 또는 파트너별 형식(Amplitude, Mixpanel, Segment)이 필요한 경우 커런츠 용어집을 참조하세요.
{% endalert %}

## 목차

테이블 | 설명
------|------------
[AGENTCONSOLE_AGENTEXECUTED_SHARED](#AGENTCONSOLE_AGENTEXECUTED_SHARED) | Agent Console 에이전트가 실행될 때 (**Snowflake 데이터 공유 전용**)
[AGENTCONSOLE_TOOLINVOCATION_SHARED](#AGENTCONSOLE_TOOLINVOCATION_SHARED) | 도구가 실행될 때 (**Snowflake 데이터 공유 전용**)
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | 삭제되지 않은 카탈로그 항목
[CHANGELOGS_CAMPAIGN_SHARED](#CHANGELOGS_CAMPAIGN_SHARED) | 캠페인이 변경될 때 (**Snowflake 데이터 공유 전용**)
[CHANGELOGS_CANVAS_SHARED](#CHANGELOGS_CANVAS_SHARED) | Canvas가 변경될 때 (**Snowflake 데이터 공유 전용**)
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | 글로벌 컨트롤 그룹이 변경될 때
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | 사용자가 커스텀 이벤트를 수행할 때
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | 사용자가 앱을 설치하고 파트너에 기여도가 부여될 때
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | 사용자가 위치를 기록할 때
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | 사용자가 구매할 때
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | 사용자가 앱을 삭제할 때
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | 사용자가 앱을 업그레이드할 때
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | 사용자가 첫 번째 세션을 시작할 때
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | 사용자가 News Feed를 조회할 때
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | 사용자가 앱에서 세션을 종료할 때
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | 사용자가 앱에서 세션을 시작할 때
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | 사용자가 지오펜스 영역을 트리거할 때(예: 지오펜스에 진입하거나 이탈할 때). 이 이벤트는 다른 이벤트와 함께 배치 처리되어 표준 이벤트 엔드포인트를 통해 수신되었으므로, 엔드포인트에서 실시간으로 수신되지 않았을 수 있습니다.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | 사용자가 지오펜스 영역을 트리거할 때(예: 지오펜스에 진입하거나 이탈할 때). 이 이벤트는 전용 지오펜스 엔드포인트를 통해 수신되므로, 사용자의 기기가 지오펜스 트리거를 감지하는 즉시 실시간으로 수신됩니다. <br><br>또한 지오펜스 엔드포인트의 사용량 제한으로 인해 일부 지오펜스 이벤트가 RecordEvent로 반영되지 않을 수 있습니다. 그러나 모든 지오펜스 이벤트는 DataEvent로 표현됩니다(다만 배치 처리로 인해 약간의 지연이 있을 수 있습니다).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Live Activity push-to-start 토큰이 변경될 때
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Live Activity 업데이트 토큰이 변경될 때
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | 푸시 알림 토큰 상태가 변경될 때
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | 사용자가 이메일 등의 채널에서 전역적으로 구독 또는 구독 취소될 때
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | 사용자가 구독 그룹에 구독 또는 구독 취소될 때
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | 사용자가 캠페인에서 전환할 때
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | 사용자가 캠페인의 대조군에 등록될 때
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | 사용자가 캠페인에서 빈도 제한에 도달할 때
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | 사용자가 주요 전환 기간 내에 매출을 발생시킬 때
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | 사용자가 캔버스 단계로 진행할 때
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | 사용자가 Canvas 전환 이벤트에서 전환할 때
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | 사용자가 Canvas에 진입할 때
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | 사용자가 오디언스 이탈 기준에 일치하여 Canvas에서 이탈할 때
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | 사용자가 예외 이벤트를 수행하여 Canvas에서 이탈할 때
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | 사용자가 캔버스 실험 단계에서 전환할 때
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | 사용자가 실험 단계 경로에 진입할 때
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | 사용자가 캔버스 단계에서 빈도 제한에 도달할 때
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | 사용자가 주요 전환 이벤트 기간 내에 매출을 발생시킬 때
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | 원래 예약된 배너 메시지가 어떤 이유로 중단된 경우
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | 사용자가 배너를 클릭할 때
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | 사용자가 배너를 조회할 때
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | 원래 예약된 콘텐츠 카드 메시지가 어떤 이유로 중단된 경우
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | 사용자가 콘텐츠 카드를 클릭할 때
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | 사용자가 콘텐츠 카드를 닫을 때
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | 사용자가 콘텐츠 카드를 조회할 때
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | 사용자에게 콘텐츠 카드를 발송할 때
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | 원래 예약된 이메일 메시지가 어떤 이유로 중단된 경우
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | 이메일 서비스 공급자가 하드바운스를 반환한 경우. 하드바운스는 영구적인 전달 가능성 실패를 의미합니다.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | 사용자가 이메일의 링크를 클릭할 때
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | 이메일이 지연될 때
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | 이메일이 전달될 때
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | 이메일이 스팸으로 표시될 때
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | 사용자가 이메일을 열 때
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | 사용자에게 이메일을 발송할 때
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | 이메일이 소프트바운스될 때
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | 사용자가 이메일 구독을 취소할 때
[USERS_MESSAGES_EMAIL_RETRY_SHARED](#USERS_MESSAGES_EMAIL_RETRY_SHARED) | 이메일 메시지가 우선순위 하향 또는 빈도 제한 후 재시도될 때 (**Snowflake 데이터 공유 전용**)
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | 사용자가 기능 플래그를 조회할 때
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | 원래 예약된 인앱 메시지가 어떤 이유로 중단된 경우
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | 사용자가 인앱 메시지를 클릭할 때
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | 사용자가 인앱 메시지를 조회할 때
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | 예약된 LINE 메시지가 LINE으로 발송되기 전에 전달할 수 없을 때
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | 사용자가 LINE 메시지의 링크를 클릭할 때
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | 사용자로부터 LINE 메시지를 수신할 때
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | LINE 메시지가 LINE으로 발송될 때
[USERS_MESSAGES_LINE_RETRY_SHARED](#USERS_MESSAGES_LINE_RETRY_SHARED) | LINE 메시지가 우선순위 하향 또는 빈도 제한 후 재시도될 때 (**Snowflake 데이터 공유 전용**)
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Live Activity에 결과 이벤트가 발생할 때
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Live Activity 메시지가 발송될 때
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | 원래 예약된 뉴스피드 카드 메시지가 어떤 이유로 중단된 경우
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | 사용자가 뉴스피드 카드를 클릭할 때
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | 사용자가 뉴스피드 카드를 조회할 때
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | 원래 예약된 푸시 알림 메시지가 어떤 이유로 중단된 경우
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | 푸시 알림이 반송될 때
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | 사용자가 알림을 수신한 후 알림을 클릭하지 않고 앱을 열 때
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | 앱이 열려 있는 상태에서 사용자가 푸시 알림을 수신할 때. <br><br>이 이벤트는 [Swift SDK](https://github.com/braze-inc/braze-swift-sdk)에서 지원되지 않으며, [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk)에서는 더 이상 사용되지 않습니다.
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | 사용자가 푸시 알림을 열거나 푸시 알림 버튼(앱을 열지 않는 닫기 버튼 포함)을 클릭할 때. <br><br> 푸시 버튼 동작에는 여러 결과가 있습니다. No, Decline, Cancel 동작은 "클릭"이고, Accept 동작은 "열기"입니다. 두 가지 모두 이 테이블에 표시되지만, **BUTTON_ACTION_TYPE** 열에서 구분할 수 있습니다. 예를 들어, No, Decline 또는 Cancel이 아닌 `BUTTON_ACTION_TYPE`으로 그룹화하는 쿼리를 사용할 수 있습니다.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | 사용자에게 푸시 알림을 발송할 때
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Braze 내에서 오류가 감지되어 RCS 발송이 중단되고 메시지가 삭제될 때
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | 최종 사용자가 UI 요소를 탭하거나 클릭하여 RCS 메시지와 상호작용할 때
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | RCS 메시지가 최종 사용자의 모바일 기기에 성공적으로 전달될 때
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Braze가 최종 사용자로부터 발신된 RCS 메시지를 수신할 때
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | 최종 사용자가 기기에서 RCS 메시지를 열 때
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | 통신사의 개입으로 RCS 메시지 전달이 실패할 때
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | RCS 메시지가 Braze 시스템에서 최종 전달 파트너로 발송될 때
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | 원래 예약된 SMS 메시지가 어떤 이유로 중단된 경우
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | SMS 메시지가 통신사로 발송될 때
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | SMS 메시지가 전달될 때
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Braze가 SMS 서비스 공급자에게 SMS 메시지를 전달할 수 없을 때
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | 사용자로부터 SMS 메시지를 수신할 때
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | SMS 메시지가 사용자에게 전달되지 않을 때
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | SMS 메시지가 발송될 때
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | 사용자가 SMS 메시지에 포함된 Braze 단축 URL을 클릭할 때
[USERS_MESSAGES_SMS_RETRY_SHARED](#USERS_MESSAGES_SMS_RETRY_SHARED) | SMS 메시지가 우선순위 하향 또는 빈도 제한 후 재시도될 때 (**Snowflake 데이터 공유 전용**)
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | 원래 예약된 웹훅 메시지가 어떤 이유로 중단된 경우
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | 웹훅 메시지가 전달되었지만 엔드포인트에서 오류 응답이 반환될 때
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | 사용자에 대해 웹훅을 발송할 때
[USERS_MESSAGES_WEBHOOK_RETRY_SHARED](#USERS_MESSAGES_WEBHOOK_RETRY_SHARED) | 웹훅 메시지가 우선순위 하향 또는 빈도 제한 후 재시도될 때 (**Snowflake 데이터 공유 전용**)
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | 원래 예약된 WhatsApp 메시지가 어떤 이유로 중단된 경우
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | 사용자가 WhatsApp 메시지의 링크 또는 버튼을 클릭할 때
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) | WhatsApp 메시지가 전달될 때
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | WhatsApp 메시지가 사용자에게 전달되지 않을 때
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | 사용자로부터 WhatsApp 메시지를 수신할 때
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | 사용자가 WhatsApp 메시지를 열 때
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | 사용자에 대해 WhatsApp 메시지를 발송할 때
[USERS_MESSAGES_WHATSAPP_RETRY_SHARED](#USERS_MESSAGES_WHATSAPP_RETRY_SHARED) | WhatsApp 메시지가 우선순위 하향 또는 빈도 제한 후 재시도될 때 (**Snowflake 데이터 공유 전용**)
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | 사용자의 무작위 버킷 번호가 변경될 때
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | 고객 요청에 의해 사용자가 삭제될 때
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | 사용자가 다른 사용자의 프로필과 병합되어 원래 프로필이 고아 상태가 될 때
[SNAPSHOTS_APP_SHARED](#SNAPSHOTS_APP_SHARED) | 앱 스냅샷 (**Snowflake 데이터 공유 전용**)
[SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED](#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED) | 캠페인 메시지 변형 스냅샷 (**Snowflake 데이터 공유 전용**)
[SNAPSHOTS_CANVAS_FLOW_STEP_SHARED](#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED) | Canvas Flow 단계 스냅샷 (**Snowflake 데이터 공유 전용**)
[SNAPSHOTS_CANVAS_STEP_SHARED](#SNAPSHOTS_CANVAS_STEP_SHARED) | 캔버스 단계 스냅샷 (**Snowflake 데이터 공유 전용**)
[SNAPSHOTS_CANVAS_VARIATION_SHARED](#SNAPSHOTS_CANVAS_VARIATION_SHARED) | 캔버스 변형 스냅샷 (**Snowflake 데이터 공유 전용**)
[SNAPSHOTS_EXPERIMENT_STEP_SHARED](#SNAPSHOTS_EXPERIMENT_STEP_SHARED) | 실험 단계 스냅샷 (**Snowflake 데이터 공유 전용**)


## Agent Console {#agent-console}

{% alert note %}
Agent Console 테이블은 Snowflake 데이터 공유에서만 사용할 수 있습니다.
{% endalert %}

### AGENTCONSOLE_AGENTEXECUTED_SHARED {#AGENTCONSOLE_AGENTEXECUTED_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`invocation_id` | `string` | 이 메시지의 글로벌 고유 ID
`request_id` | `string` | 이 전체 LLM 요청 및 완전한 실행에 대한 고유 ID
`duration` | `int` | 세션 지속 시간(초)
`prompt_tokens` | `int` | 이 요청에서 사용한 프롬프트 토큰 수
`completion_tokens` | `int` | 이 요청에서 사용한 완성 토큰 수
`total_tokens` | `int` | 이 요청에서 사용한 총 토큰 수
`cache_tokens` | `int` | 이 요청에서 사용한 캐시 토큰 수
`reasoning_tokens` | `int` | 이 요청에서 사용한 추론 토큰 수
`time` | `int` | 이벤트가 발생한 시점의 UNIX 타임스탬프
`app_group_id` | `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`agent_id` | `string` | CustomerDefinedAgent의 BSON ID
`agent_name` | `string` | CustomerDefinedAgent의 이름
`model_provider` | `string` | LLM 모델 공급자의 이름
`model_name` | `string` | 이 요청에서 사용된 LLM 모델의 이름
`provider_request_id` | `string` | API 호출에 대해 모델 공급자가 제공한 요청 ID
`cache_hit` | `boolean` | 이 요청이 캐시에 적중하여 응답을 반환했는지 여부
`llm_owned_by_customer` | `boolean` | true이면 고객의 API 키가 사용되었고, false이면 Braze의 키가 사용되었습니다
`is_error` | `boolean` | 이 요청에서 오류가 발생했는지 여부
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캔버스 단계의 API ID
`user_id` | `string` | [PII] 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`input` | `null,`&nbsp;`string` | [PII] LLM에 대한 입력
`output` | `null,`&nbsp;`string` | [PII] LLM의 응답
`invocation_source` | `null,`&nbsp;`string` | LLM 요청을 호출한 Ruby 객체
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### AGENTCONSOLE_TOOLINVOCATION_SHARED {#AGENTCONSOLE_TOOLINVOCATION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`tool_call_id` | `string` | 이 도구 호출의 글로벌 고유 ID
`duration` | `int` | 세션 지속 시간(초)
`time` | `int` | 이벤트가 발생한 시점의 UNIX 타임스탬프
`app_group_id` | `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`agent_id` | `string` | CustomerDefinedAgent의 BSON ID
`agent_name` | `string` | CustomerDefinedAgent의 이름
`is_error` | `boolean` | 이 요청에서 오류가 발생했는지 여부
`tool_name` | `string` | 도구의 이름
`tool_arguments` | `null,`&nbsp;`string` | [PII] 도구 인수의 JSON
`invocation_source` | `null,`&nbsp;`string` | LLM 요청을 호출한 Ruby 객체
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 카탈로그

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

필드 | 유형 | 설명
------|------|------------
`catalog_id` | `string` | 카탈로그의 BSON ID
`item_id` | `string` | 카탈로그 항목의 BSON ID
`app_group_id` | `null,`&nbsp;`string` | 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 앱 그룹의 API ID
`field_name` | `null,`&nbsp;`string` | 필드의 이름
`field_value` | `null,`&nbsp;`string` | 필드의 값
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 체인지로그

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 시점의 UNIX 타임스탬프
`random_bucket_number` | `null, int` | 새로운 무작위 버킷 번호
`global_control_group` | `null, boolean` | 이 변경으로 해당 버킷 번호가 글로벌 컨트롤 그룹에 포함됨
`previous_global_control_group` | `null, boolean` | 이 변경 이전에 해당 버킷 번호가 글로벌 컨트롤 그룹에 포함되어 있었지만 더 이상 포함되지 않음
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### CHANGELOGS_CAMPAIGN_SHARED {#CHANGELOGS_CAMPAIGN_SHARED}

{% alert note %}
이 테이블은 Snowflake 데이터 공유에서만 사용할 수 있습니다.
{% endalert %}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 UNIX 타임스탬프
`app_group_id` | `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`api_id` | `string` | 캠페인의 API ID
`name` | `null,`&nbsp;`string` | 캠페인의 이름
`conversion_behaviors` | `null,`&nbsp;`string` | 캠페인의 전환 동작
`actions` | `null,`&nbsp;`string` | 캠페인의 동작
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### CHANGELOGS_CANVAS_SHARED {#CHANGELOGS_CANVAS_SHARED}

{% alert note %}
이 테이블은 Snowflake 데이터 공유에서만 사용할 수 있습니다.
{% endalert %}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 UNIX 타임스탬프
`app_group_id` | `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`api_id` | `string` | Canvas의 API ID
`name` | `null,`&nbsp;`string` | Canvas의 이름
`conversion_behaviors` | `null,`&nbsp;`string` | Canvas의 전환 동작
`variations` | `null,`&nbsp;`string` | Canvas의 변형
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## 동작

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 동작이 발생한 앱의 API ID
`time` | `int` | 사용자가 이벤트를 수행한 시점의 Unix 타임스탬프
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 커스텀 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`name` | `string` | 커스텀 이벤트의 이름
`properties` | `string` | JSON 인코딩 문자열로 저장된 이벤트의 커스텀 등록정보
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`, `google_ad_id`, `windows_ad_id` 또는 `roku_ad_id` 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 설치한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 사용자가 설치한 시점의 Unix 타임스탬프
`source` | `string` | 기여도의 소스
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 위치를 기록한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 위치가 기록된 앱의 API ID
`time` | `int` | 위치가 기록된 시점의 Unix 타임스탬프
`latitude` | `float` | [PII] 기록된 위치의 위도
`longitude` | `float` | [PII] 기록된 위치의 경도
`altitude` | `null, float` | [PII] 기록된 위치의 고도
`ll_accuracy` | `null, float` | 기록된 위치의 위도 및 경도 정확도
`alt_accuracy` | `null, float` | 기록된 위치의 고도 정확도
`device_id` | `null,`&nbsp;`string` | 위치가 기록된 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 위치 기록 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`, `google_ad_id`, `windows_ad_id` 또는 `roku_ad_id` 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 구매한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,`&nbsp;`string` | 구매가 발생한 앱의 API ID
`time` | `int` | 사용자가 구매한 시점의 Unix 타임스탬프
`device_id` | `null,`&nbsp;`string` | 구매가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 구매 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`product_id` | `string` | 구매한 제품의 ID
`price` | `float` | 구매 가격
`currency` | `string` | 구매 통화
`properties` | `string` | JSON 인코딩 문자열로 저장된 구매의 커스텀 등록정보
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`, `google_ad_id`, `windows_ad_id` 또는 `roku_ad_id` 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 앱을 삭제한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,`&nbsp;`string` | 삭제된 앱의 API ID
`time` | `int` | 사용자가 앱을 삭제한 시점의 Unix 타임스탬프
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 앱을 업그레이드한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,`&nbsp;`string` | 사용자가 업그레이드한 앱의 API ID
`time` | `int` | 사용자가 앱을 업그레이드한 시점의 Unix 타임스탬프
`device_id` | `null,`&nbsp;`string` | 사용자가 앱을 업그레이드한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`old_app_version` | `null,`&nbsp;`string` | 앱의 이전 버전
`new_app_version` | `null,`&nbsp;`string` | 앱의 새 버전
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 동작을 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 세션이 발생한 앱의 API ID
`time` | `int` | 세션이 시작된 시점의 Unix 타임스탬프
`session_id` | `string` | 세션의 UUID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 세션이 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 세션 중 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`time` | `int` | 이벤트가 발생한 시점의 UNIX 타임스탬프
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 동작을 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 세션이 발생한 앱의 API ID
`time` | `int` | 세션이 종료된 시점의 Unix 타임스탬프
`duration` | `null, float` | 세션 지속 시간(초)
`session_id` | `string` | 세션의 UUID
`device_id` | `null,`&nbsp;`string` | 세션이 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 세션 중 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 동작을 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_api_id` | `null,`&nbsp;`string` | 이 세션이 발생한 앱의 API ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 세션이 시작된 시점의 Unix 타임스탬프
`session_id` | `string` | 세션의 UUID
`device_id` | `null,`&nbsp;`string` | 세션이 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 세션 중 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 동작이 발생한 앱의 API ID
`time` | `int` | 사용자가 이벤트를 수행한 시점의 Unix 타임스탬프
`device_id` | `null,`&nbsp;`string` | 커스텀 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`event_type` | `string` | 트리거된 지오펜스 이벤트의 종류(예: 'enter' 또는 'exit')
`location_set_id` | `string` | 트리거된 지오펜스의 위치 세트 ID
`geofence_id` | `string` | 트리거된 지오펜스의 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 동작이 발생한 앱의 API ID
`time` | `int` | 사용자가 이벤트를 수행한 시점의 Unix 타임스탬프
`device_id` | `null,`&nbsp;`string` | 커스텀 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`event_type` | `string` | 트리거된 지오펜스 이벤트의 종류(예: 'enter' 또는 'exit')
`location_set_id` | `string` | 트리거된 지오펜스의 위치 세트 ID
`geofence_id` | `string` | 트리거된 지오펜스의 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`time` | `int` | 이벤트가 발생한 시점의 UNIX 타임스탬프
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`activity_attributes_type` | `null,`&nbsp;`string` | Live Activity 속성 유형
`push_to_start_token` | `null,`&nbsp;`string` | Live Activity push-to-start 토큰
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`ios_push_token_apns_gateway` | `null, int` | 푸시 토큰의 APN 게이트웨이, iOS 푸시 토큰에만 적용, 1은 개발용, 2는 프로덕션용
`push_token_state_change_type` | `null,`&nbsp;`string` | 푸시 토큰 상태 변경 유형에 대한 설명
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`time` | `int` | 이벤트가 발생한 시점의 UNIX 타임스탬프
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`activity_id` | `null,`&nbsp;`string` | Live Activity 식별자
`update_token` | `null,`&nbsp;`string` | Live Activity 업데이트 토큰
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`ios_push_token_apns_gateway` | `null, int` | 푸시 토큰의 APN 게이트웨이, iOS 푸시 토큰에만 적용, 1은 개발용, 2는 프로덕션용
`push_token_state_change_type` | `null,`&nbsp;`string` | 푸시 토큰 상태 변경 유형에 대한 설명
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 시점의 UNIX 타임스탬프
`time_ms` | `int` | 이벤트가 발생한 시점의 밀리초 단위 시간
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`push_token` | `null,`&nbsp;`string` | 이벤트의 푸시 토큰
`push_token_created_at` | `null, int` | 푸시 토큰이 생성된 시점의 UNIX 타임스탬프
`push_token_updated_at` | `null, int` | 푸시 토큰이 마지막으로 업데이트된 시점의 UNIX 타임스탬프
`push_token_foreground_push_disabled` | `null, boolean` | 푸시 토큰의 포그라운드 푸시 비활성화 플래그
`push_token_device_id` | `null,`&nbsp;`string` | 푸시 토큰의 기기 ID
`push_token_provisionally_opted_in` | `null, boolean` | 푸시 토큰의 임시 옵트인 플래그
`ios_push_token_apns_gateway` | `null, int` | 푸시 토큰의 APN 게이트웨이, iOS 푸시 토큰에만 적용, 1은 개발용, 2는 프로덕션용
`web_push_token_public_key` | `null,`&nbsp;`string` | 푸시 토큰의 공개 키, 웹 푸시 토큰에만 적용
`web_push_token_user_auth` | `null,`&nbsp;`string` | 푸시 토큰의 사용자 인증, 웹 푸시 토큰에만 적용
`web_push_token_vapid_public_key` | `null,`&nbsp;`string` | 푸시 토큰의 VAPID 공개 키, 웹 푸시 토큰에만 적용
`push_token_state_change_type` | `null,`&nbsp;`string` | 푸시 토큰 상태 변경 유형에 대한 설명
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 영향을 받은 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`email_address` | `null,`&nbsp;`string` | [PII] 사용자의 이메일 주소
`state_change_source` | `null,`&nbsp;`string` | 상태 변경의 소스(REST, SDK, 대시보드 등)
`subscription_status` | `string` | 구독 상태: 'Subscribed', 'Unsubscribed' 또는 'Opted In'
`channel` | `null,`&nbsp;`string` | 이메일 등 전역 구독 상태의 채널
`time` | `int` | 구독 상태가 변경된 시점의 Unix 타임스탬프
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이벤트가 속한 앱의 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캔버스 단계의 API ID
`send_id` | `null,`&nbsp;`string` | 이 구독 상태 변경 동작이 발생한 메시지 발송 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`channel_identifier` | `null,`&nbsp;`string` | [PII] 이벤트 대상 채널에서의 사용자 식별자
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 영향을 받은 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`email_address` | `null,`&nbsp;`string` | [PII] 사용자의 이메일 주소
`phone_number` | `null,`&nbsp;`string` | [PII] e164 형식의 사용자 전화번호
`app_api_id` | `null,`&nbsp;`string` | 이벤트가 속한 앱의 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캔버스 단계의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`channel` | `null,`&nbsp;`string` | 채널: 구독 그룹의 채널 유형에 따라 'email' 또는 'sms'
`subscription_status` | `string` | 구독 상태: 'Subscribed', 'Unsubscribed' 또는 'Opted In'
`time` | `int` | 구독 상태가 변경된 시점의 Unix 타임스탬프
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`send_id` | `null,`&nbsp;`string` | 이 구독 상태 변경 동작이 발생한 메시지 발송 ID
`state_change_source` | `null,`&nbsp;`string` | 상태 변경의 소스(REST, SDK, 대시보드 등)
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`channel_identifier` | `null,`&nbsp;`string` | [PII] 이벤트 대상 채널에서의 사용자 식별자
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 캠페인

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자와 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 받은 메시지 변형의 API ID
`conversion_behavior_index` | `null, int` | 전환 동작의 인덱스
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자와 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 받은 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자와 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 받은 메시지 변형의 API ID
`channel` | `null,`&nbsp;`string` | 이 이벤트가 속한 채널
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자와 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 받은 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`revenue` | `long` | 생성된 USD 매출 금액(센트 단위)
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| 필드                                  | 유형                     | 설명                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | 이 이벤트를 수행한 사용자의 Braze ID                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | 사용자가 익명인 경우 이 사용자와 연결된 기기의 ID                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 API ID                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | 이벤트가 발생한 Unix 타임스탬프                                                                      |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스의 API ID        |         
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 변형의 API ID                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 단계의 API ID                                                                 |
| `progression_type`                     | `string`,&nbsp;`null`    | 단계 진행 이벤트의 유형 |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | 캔버스의 첫 번째 단계에 진입한 것인지 여부        |
| `exit_reason`                          | `string`,&nbsp;`null`    | 이탈인 경우, 해당 단계에서 사용자가 캔버스를 이탈한 이유                  |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | 캔버스 내 이 사용자 인스턴스의 고유 식별자  |
| `next_step_id`                         | `string`,&nbsp;`null`    | 캔버스 내 다음 단계의 BSON ID |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | 캔버스 내 다음 단계의 API ID |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| 필드                                  | 유형                     | 설명                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | 이 이벤트를 수행한 사용자의 Braze ID                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | 사용자가 익명인 경우 이 사용자와 연결된 기기의 ID                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 API ID                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | 이벤트가 발생한 Unix 타임스탬프                                                                      |
| `app_api_id`                           | `string`,&nbsp;`null`    | 이 이벤트가 발생한 앱의 API ID                                                                  |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스의 API ID                                                                      |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 변형의 API ID                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 단계의 API ID                                                                 |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID                                                  |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | 사용자가 수행한 전환 이벤트 유형(여기서 "0"은 1차 전환, "1"은 2차 전환)입니다. |
| `gender`                               | `string`,&nbsp;`null`    | [PII] 사용자의 성별                                                                                        |
| `country`                              | `string`,&nbsp;`null`    | [PII] 사용자의 국가                                                                                       |
| `timezone`                             | `string`,&nbsp;`null`    | 사용자의 시간대                                                                                            |
| `language`                             | `string`,&nbsp;`null`    | [PII] 사용자의 언어                                                                                      |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| 필드                     | 유형                     | 설명                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | 이 이벤트를 수행한 사용자의 Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `device_id`               | `string`,&nbsp;`null`    | 사용자가 익명인 경우 이 사용자와 연결된 기기의 ID |
| `app_group_id`            | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 API ID                         |
| `time`                    | `int`,&nbsp;`null`       | 이벤트가 발생한 Unix 타임스탬프                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [사용 중단됨] 이 이벤트가 속한 캔버스 단계의 API ID         |
| `gender`                  | `string`,&nbsp;`null`    | [PII] 사용자의 성별                                             |
| `country`                 | `string`,&nbsp;`null`    | [PII] 사용자의 국가                                            |
| `timezone`                | `string`,&nbsp;`null`    | 사용자의 시간대                                                 |
| `language`                | `string`,&nbsp;`null`    | [PII] 사용자의 언어                                           |
| `in_control_group`        | `boolean`,&nbsp;`null`   | 사용자가 대조군에 등록되어 있는 경우 참입니다.                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| 필드                     | 유형                     | 설명                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | 이 이벤트를 수행한 사용자의 Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 API ID                         |
| `time`                    | `int`,&nbsp;`null`       | 이벤트가 발생한 Unix 타임스탬프                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| 필드                     | 유형                     | 설명                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | 이 이벤트를 수행한 사용자의 Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 API ID                         |
| `time`                    | `int`,&nbsp;`null`       | 이벤트가 발생한 Unix 타임스탬프                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| 필드                       | 유형                     | 설명                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                                                                               |
| `user_id`                   | `string`,&nbsp;`null`    | 이 이벤트를 수행한 사용자의 Braze ID                                                                   |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                                                                              |
| `app_group_id`              | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                                                                   |
| `time`                      | `int`,&nbsp;`null`       | 이벤트가 발생한 Unix 타임스탬프                                                                      |
| `app_api_id`                | `string`,&nbsp;`null`    | 이 이벤트가 발생한 앱의 API ID                                                                  |
| `canvas_id`                 | `string`,&nbsp;`null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID                                                     |
| `canvas_api_id`             | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스의 API ID                                                                      |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 변형의 API ID                                                            |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 단계의 API ID                                                                 |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | 이 이벤트가 속한 실험 단계의 API ID                                                             |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | 사용자가 수행한 전환 이벤트 유형(여기서 "0"은 1차 전환, "1"은 2차 전환)입니다. |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때                                                                   |
| `experiment_split_api_id` | `string`,&nbsp;`null` | 사용자가 등록된 실험 분할의 API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| 필드                     | 유형                     | 설명                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | 이 이벤트를 수행한 사용자의 Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `time`                    | `int`,&nbsp;`null`       | 이벤트가 발생한 Unix 타임스탬프                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | 이 이벤트가 속한 실험 단계의 API ID                  |
| `in_control_group`        | `boolean`,&nbsp;`null`   | 사용자가 대조군에 등록되어 있는 경우 참입니다.                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |

| `experiment_split_api_id` | `string`,&nbsp;`null` | 사용자가 등록된 실험 분할의 API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| 필드                                  | 유형                     | 설명                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                              | `string`,&nbsp;`null`    | 이 이벤트를 수행한 사용자의 Braze ID                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `device_id`                            | `string`,&nbsp;`null`    | 사용자가 익명인 경우 이 사용자와 연결된 기기의 ID |
| `app_group_id`                         | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 API ID                         |
| `time`                                 | `int`,&nbsp;`null`       | 이벤트가 발생한 Unix 타임스탬프                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID       |
| `channel`                              | `string`,&nbsp;`null`    | 이 이벤트가 속한 메시징 채널(이메일, 푸시 등)          |
| `gender`                               | `string`,&nbsp;`null`    | [PII] 사용자의 성별                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] 사용자의 국가                                            |
| `timezone`                             | `string`,&nbsp;`null`    | 사용자의 시간대                                                 |
| `language`                             | `string`,&nbsp;`null`    | [PII] 사용자의 언어                                           |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| 필드                                  | 유형                     | 설명                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                                    |
| `user_id`                              | `string`,&nbsp;`null`    | 이 이벤트를 수행한 사용자의 Braze ID                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                                   |
| `device_id`                            | `string`,&nbsp;`null`    | 사용자가 익명인 경우 이 사용자와 연결된 기기의 ID |
| `app_group_id`                         | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 API ID                         |
| `time`                                 | `int`,&nbsp;`null`       | 이벤트가 발생한 Unix 타임스탬프                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 전용) 이 이벤트가 속한 캔버스의 ID          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스의 API ID                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 변형의 API ID                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | 이 이벤트가 속한 캔버스 단계의 API ID                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID       |
| `gender`                               | `string`,&nbsp;`null`    | [PII] 사용자의 성별                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] 사용자의 국가                                            |
| `timezone`                             | `string`,&nbsp;`null`    | 사용자의 시간대                                                 |
| `language`                             | `string`,&nbsp;`null`    | [PII] 사용자의 언어                                           |
| `revenue`                              | `int`,&nbsp;`null`       | USD로 생성된 매출 금액(센트 단위로 표시)               |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 포착되었을 때                        |
| `app_api_id` | `string`,&nbsp;`null` | 이 이벤트가 발생한 앱의 API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 메시지


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 열기가 발생한 기기 브라우저 - user_agent에서 추출
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id'] 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 128자)
`banner_placement_id` | `null,`&nbsp;`string` | 고객이 지정한 배너 배치 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 열기가 발생한 기기 브라우저 - user_agent에서 추출
`button_id` | `null,`&nbsp;`string` | 클릭된 버튼의 ID, 이 클릭이 버튼 클릭을 나타내는 경우
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id'] 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`banner_placement_id` | `null,`&nbsp;`string` | 고객이 지정한 배너 배치 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 열기가 발생한 기기 브라우저 - user_agent에서 추출
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id'] 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`banner_placement_id` | `null,`&nbsp;`string` | 고객이 지정한 배너 배치 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`content_card_id` | `string` | 이 이벤트를 생성한 카드의 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 기기의 브라우저
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`, `google_ad_id`, `windows_ad_id` 또는 `roku_ad_id` 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`content_card_id` | `string` | 이 이벤트를 생성한 카드의 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 기기의 브라우저
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`, `google_ad_id`, `windows_ad_id` 또는 `roku_ad_id` 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`content_card_id` | `string` | 이 이벤트를 생성한 카드의 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 기기의 브라우저
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`, `google_ad_id`, `windows_ad_id` 또는 `roku_ad_id` 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`content_card_id` | `string` | 이 이벤트를 생성한 카드의 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`sending_ip` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 주소
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`bounce_reason` | `null,`&nbsp;`string` | [PII] 이 반송 이벤트에 대해 수신된 SMTP 사유 코드 및 사용자 친화적 메시지
`esp` | `null,`&nbsp;`string` | 이벤트와 관련된 이메일 서비스 공급자 (SparkPost, SendGrid 또는 Amazon SES)
`from_domain` | `null,`&nbsp;`string` | 이메일의 발신 도메인
`is_drop` | `null, boolean` | 이 이벤트가 드롭 이벤트로 집계되는지 여부를 나타냅니다
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`url` | `null,`&nbsp;`string` | 사용자가 클릭한 URL
`user_agent` | `null,`&nbsp;`string` | 클릭이 발생한 사용자 에이전트
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`link_id` | `null,`&nbsp;`string` | Braze에서 생성한 클릭된 링크의 고유 ID
`link_alias` | `null,`&nbsp;`string` | 이 링크 ID와 연결된 별칭
`esp` | `null,`&nbsp;`string` | 이벤트와 관련된 이메일 서비스 공급자 (SparkPost, SendGrid 또는 Amazon SES)
`from_domain` | `null,`&nbsp;`string` | 이메일의 발신 도메인
`is_amp` | `null, boolean` | AMP 이벤트인지 여부를 나타냅니다
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`is_suspected_bot_click` | `null, boolean` | 이 이벤트가 봇 이벤트로 처리되었는지 여부
`suspected_bot_click_reason` | `null, object` | 이 이벤트가 봇으로 분류된 이유
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`email_address` | `null,`&nbsp;`string` | [PII] 사용자의 이메일 주소
`recipient_domain` | `null,`&nbsp;`string` | 수신자의 이메일 도메인
`esp` | `null,`&nbsp;`string` | 이벤트와 관련된 이메일 서비스 공급자 (Sparkpost, Sendgrid 또는 Amazon SES)
`from_domain` | `null,`&nbsp;`string` | 이메일의 발신 도메인
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`sending_ip` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 주소
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`deferral_reason` | `null,`&nbsp;`string` | [PII] 이 지연 이벤트에 대해 수신된 SMTP 사유 코드 및 사용자 친화적 메시지
`attempt_count` | `null, int` | 메시지 전송 시도 횟수
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`sending_ip` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 주소
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`esp` | `null,`&nbsp;`string` | 이벤트와 관련된 이메일 서비스 공급자 (SparkPost, SendGrid 또는 Amazon SES)
`from_domain` | `null,`&nbsp;`string` | 이메일의 발신 도메인
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`user_agent` | `null,`&nbsp;`string` | 스팸 신고가 발생한 사용자 에이전트
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`esp` | `null,`&nbsp;`string` | 이벤트와 관련된 이메일 서비스 공급자 (SparkPost, SendGrid 또는 Amazon SES)
`from_domain` | `null,`&nbsp;`string` | 이메일의 발신 도메인
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`user_agent` | `null,`&nbsp;`string` | 열기가 발생한 사용자 에이전트
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`machine_open` | `null,`&nbsp;`string` | 사용자 상호작용 없이 열기 이벤트가 트리거된 경우 'true'로 채워집니다. 예를 들어 MPP가 활성화된 Apple 기기에서 발생한 경우입니다. 값은 더 세분화된 정보를 제공하기 위해 시간이 지남에 따라 변경될 수 있습니다.
`esp` | `null,`&nbsp;`string` | 이벤트와 관련된 이메일 서비스 공급자 (SparkPost, SendGrid 또는 Amazon SES)
`from_domain` | `null,`&nbsp;`string` | 이메일의 발신 도메인
`is_amp` | `null, boolean` | AMP 이벤트인지 여부를 나타냅니다
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`esp` | `null,`&nbsp;`string` | 이벤트와 관련된 이메일 서비스 공급자 (SparkPost, SendGrid 또는 Amazon SES)
`from_domain` | `null,`&nbsp;`string` | 이메일의 발신 도메인
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`sending_ip` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 주소
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`bounce_reason` | `null,`&nbsp;`string` | [PII] 이 반송 이벤트에 대해 수신된 SMTP 사유 코드 및 사용자 친화적 메시지
`esp` | `null,`&nbsp;`string` | 이벤트와 관련된 이메일 서비스 공급자 (SparkPost, SendGrid 또는 Amazon SES)
`from_domain` | `null,`&nbsp;`string` | 이메일의 발신 도메인
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`email_address` | `string` | [PII] 사용자의 이메일 주소
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_RETRY_SHARED {#USERS_MESSAGES_EMAIL_RETRY_SHARED}

{% alert note %}
이 테이블은 Snowflake 데이터 공유에서만 사용할 수 있습니다.
{% endalert %}

이 이벤트는 메시지의 우선순위가 낮아지거나 빈도 제한이 적용되어 설정된 재시도 기간 내에 나중에 재시도될 때 발생합니다.

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | [PII] 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`retry_type` | `null,`&nbsp;`string` | 재시도 유형
`retry_log` | `null,`&nbsp;`string` | 재시도 세부 정보를 설명하는 로그 메시지
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`email_address` | `null,`&nbsp;`string` | [PII] 사용자의 이메일 주소
`ip_pool` | `null,`&nbsp;`string` | 이메일 전송에 사용된 IP 풀
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`feature_flag_id_name` | `null,`&nbsp;`string` | 기능 플래그 롤아웃 식별자
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`browser` | `null,`&nbsp;`string` | 열기가 발생한 기기 브라우저 - user_agent에서 추출
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,`&nbsp;`string` | 카드의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 기기의 브라우저
`version` | `string` | 인앱 메시지 버전, 레거시 또는 트리거됨
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`, `google_ad_id`, `windows_ad_id` 또는 `roku_ad_id` 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,`&nbsp;`string` | 카드의 API ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 기기의 브라우저
`version` | `string` | 인앱 메시지 버전, 레거시 또는 트리거됨
`button_id` | `null,`&nbsp;`string` | 클릭된 버튼의 ID, 이 클릭이 버튼 클릭을 나타내는 경우
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`, `google_ad_id`, `windows_ad_id` 또는 `roku_ad_id` 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,`&nbsp;`string` | 카드의 API ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 기기의 브라우저
`version` | `string` | 인앱 메시지 버전, 레거시 또는 트리거됨
`ad_id` | `null,`&nbsp;`string` | [PII] 광고 식별자
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`, `google_ad_id`, `windows_ad_id` 또는 `roku_ad_id` 중 하나
`ad_tracking_enabled` | `null, boolean` | 기기에서 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`locale_key` | `null,`&nbsp;`string` | [PII] 이 메시지를 작성하는 데 사용된 번역에 해당하는 키 (예: 'en-us') (기본값의 경우 null).
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 128자)
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`line_channel_id` | `null,`&nbsp;`string` | 메시지가 전송되거나 수신된 LINE 채널 ID
`line_channel_name` | `null,`&nbsp;`string` | 메시지가 전송되거나 수신된 LINE 채널 이름
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`native_line_id` | `null,`&nbsp;`string` | [PII] 메시지가 전송되거나 수신된 사용자의 Line ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`native_line_id` | `null,`&nbsp;`string` | [PII] 메시지가 전송되거나 수신된 사용자의 Line ID
`line_channel_id` | `null,`&nbsp;`string` | 메시지가 전송되거나 수신된 LINE 채널 ID
`line_channel_name` | `null,`&nbsp;`string` | 메시지가 전송되거나 수신된 LINE 채널 이름
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`is_suspected_bot_click` | `null, boolean` | 이 이벤트가 봇 이벤트로 처리되었는지 여부
`short_url` | `null,`&nbsp;`string` | 클릭된 단축 URL
`url` | `null,`&nbsp;`string` | 사용자가 클릭한 URL
`user_agent` | `null,`&nbsp;`string` | 스팸 신고가 발생한 사용자 에이전트
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`line_channel_id` | `null,`&nbsp;`string` | 메시지가 전송되거나 수신된 LINE 채널 ID
`line_channel_name` | `null,`&nbsp;`string` | 메시지가 전송되거나 수신된 LINE 채널 이름
`media_id` | `null,`&nbsp;`string` | LINE에서 인바운드 미디어를 검색하는 데 사용할 수 있는 LINE 생성 ID
`message_body` | `null,`&nbsp;`string` | 사용자의 입력 응답
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`native_line_id` | `null,`&nbsp;`string` | [PII] 메시지가 전송되거나 수신된 사용자의 Line ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`line_channel_id` | `null,`&nbsp;`string` | 메시지가 전송되거나 수신된 LINE 채널 ID
`line_channel_name` | `null,`&nbsp;`string` | 메시지가 전송되거나 수신된 LINE 채널 이름
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`native_line_id` | `null,`&nbsp;`string` | [PII] 메시지가 전송되거나 수신된 사용자의 Line ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_LINE_RETRY_SHARED {#USERS_MESSAGES_LINE_RETRY_SHARED}

{% alert note %}
이 테이블은 Snowflake 데이터 공유에서만 사용할 수 있습니다.
{% endalert %}

이 이벤트는 메시지의 우선순위가 낮아지거나 빈도 제한이 적용되어 설정된 재시도 기간 내에 나중에 재시도될 때 발생합니다.

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | [PII] 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`retry_type` | `null,`&nbsp;`string` | 재시도 유형
`retry_log` | `null,`&nbsp;`string` | 재시도 세부 정보를 설명하는 로그 메시지
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`line_channel_id` | `null,`&nbsp;`string` | 메시지가 전송되거나 수신된 LINE 채널 ID
`line_channel_name` | `null,`&nbsp;`string` | 메시지가 전송되거나 수신된 LINE 채널 이름
`native_line_id` | `null,`&nbsp;`string` | [PII] 메시지가 전송되거나 수신된 사용자의 Line ID
`subscription_group_api_id` | `null,`&nbsp;`string` | 구독 그룹 API ID
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`activity_id` | `null,`&nbsp;`string` | Live Activity 식별자
`activity_attributes_type` | `null,`&nbsp;`string` | Live Activity 속성 유형
`push_to_start_token` | `null,`&nbsp;`string` | Live Activity 시작 푸시 토큰
`update_token` | `null,`&nbsp;`string` | Live Activity 업데이트 토큰
`live_activity_event_type` | `null,`&nbsp;`string` | Live Activity의 이벤트 유형. ['start', 'update', 'end'] 중 하나
`live_activity_event_outcome` | `null,`&nbsp;`string` | Live Activity 이벤트의 결과
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`activity_id` | `null,`&nbsp;`string` | Live Activity 식별자
`activity_attributes_type` | `null,`&nbsp;`string` | Live Activity 속성 유형
`push_to_start_token` | `null,`&nbsp;`string` | Live Activity 시작 푸시 토큰
`update_token` | `null,`&nbsp;`string` | Live Activity 업데이트 토큰
`live_activity_event_type` | `null,`&nbsp;`string` | Live Activity의 이벤트 유형. ['start', 'update', 'end'] 중 하나
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,`&nbsp;`string` | 카드의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 열기가 발생한 기기 브라우저 - user_agent에서 추출
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 128자)
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,`&nbsp;`string` | 카드의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 열기가 발생한 기기 브라우저 - user_agent에서 추출
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`card_api_id` | `null,`&nbsp;`string` | 카드의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 열기가 발생한 기기 브라우저 - user_agent에서 추출
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 전달을 시도한 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`platform` | `string` | 기기의 플랫폼
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`push_token` | `null,`&nbsp;`string` | 반송된 푸시 토큰
`device_id` | `null,`&nbsp;`string` | 전달을 시도했으나 반송된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`ad_id` | `null,`&nbsp;`string` | [PII] 전달을 시도한 기기의 광고 ID
`ad_id_type` | `null,`&nbsp;`string` | 광고 ID의 유형
`ad_tracking_enabled` | `null, boolean` | 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 기기의 브라우저
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
이 이벤트는 [Swift SDK](https://github.com/braze-inc/braze-swift-sdk)에서 지원되지 않으며 [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk)에서는 더 이상 사용되지 않습니다.
{% endalert %}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 기기의 브라우저
`ad_id` | `null,`&nbsp;`string` | [PII] 전달을 시도한 기기의 광고 ID
`ad_id_type` | `null,`&nbsp;`string` | 광고 ID의 유형
`ad_tracking_enabled` | `null, boolean` | 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`sdk_version` | `null,`&nbsp;`string` | 이벤트 발생 시 사용 중인 Braze SDK 버전
`platform` | `null,`&nbsp;`string` | 기기의 플랫폼
`os_version` | `null,`&nbsp;`string` | 기기의 운영체제 버전
`device_model` | `null,`&nbsp;`string` | 기기의 모델
`resolution` | `null,`&nbsp;`string` | 기기의 해상도
`carrier` | `null,`&nbsp;`string` | 기기의 통신사
`browser` | `null,`&nbsp;`string` | 기기의 브라우저
`button_string` | `null,`&nbsp;`string` | 클릭된 푸시 알림 버튼의 식별자(button_string). 버튼 클릭이 아닌 경우 null
`button_action_type` | `null,`&nbsp;`string` | 푸시 알림 버튼의 동작 유형. [URI, DEEP_LINK, NONE, CLOSE] 중 하나. 버튼 클릭이 아닌 경우 null
`slide_id` | `null,`&nbsp;`string` | 사용자가 클릭한 푸시 캐러셀 슬라이드의 슬라이드 식별자
`slide_action_type` | `null,`&nbsp;`string` | 푸시 캐러셀 슬라이드의 동작 유형
`ad_id` | `null,`&nbsp;`string` | [PII] 전달을 시도한 기기의 광고 ID
`ad_id_type` | `null,`&nbsp;`string` | 광고 ID의 유형
`ad_tracking_enabled` | `null, boolean` | 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`push_token` | `null,`&nbsp;`string` | 전달을 시도한 푸시 토큰
`device_id` | `null,`&nbsp;`string` | 전달을 시도한 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`app_api_id` | `null,`&nbsp;`string` | 이 이벤트가 발생한 앱의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`platform` | `string` | 기기의 플랫폼
`ad_id` | `null,`&nbsp;`string` | [PII] 전달을 시도한 기기의 광고 ID
`ad_id_type` | `null,`&nbsp;`string` | 광고 ID의 유형
`ad_tracking_enabled` | `null, boolean` | 광고 추적이 활성화되어 있는지 여부
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`is_sampled` | `null,`&nbsp;`string` | 푸시 전송이 샘플링되었으며 전달 이벤트가 예상되는지 여부를 나타냅니다
`locale_key` | `null,`&nbsp;`string` | [PII] 이 메시지를 작성하는 데 사용된 번역에 해당하는 키 (예: 'en-us') (기본값의 경우 null).
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 128자)
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas 이름
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`canvas_variation_name` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 변형 이름
`message_variation_name` | `null,`&nbsp;`string` | 메시지 변형 이름
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas 이름
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`is_suspected_bot_click` | `null, boolean` | 이 이벤트가 봇 이벤트로 처리되었는지 여부
`message_variation_name` | `null,`&nbsp;`string` | 메시지 변형 이름
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`short_url` | `null,`&nbsp;`string` | 클릭된 단축 URL
`suspected_bot_click_reason` | `null,`&nbsp;`string` | 이 이벤트가 봇으로 분류된 이유
`user_agent` | `null,`&nbsp;`string` | 스팸 신고가 발생한 사용자 에이전트
`user_phone_number` | `null,`&nbsp;`string` | [PII] 메시지를 수신한 사용자의 전화번호
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`interaction_type` | `null,`&nbsp;`string` | 클릭을 생성한 상호작용 유형. 예시 문자열 값: Text URL, Reply, OpenURL
`element_label` | `null,`&nbsp;`string` | 클릭된 요소에 대한 선택적 세부 정보(예: 추천 답변 또는 버튼의 텍스트)
`element_type` | `null,`&nbsp;`string` | 추천과 버튼에 공통적인 interaction_type이 추천에서 왔는지 버튼에서 왔는지를 지정합니다. 예시: Suggestion, Button
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`url` | `null,`&nbsp;`string` | 사용자가 클릭한 URL
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`canvas_variation_name` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 변형 이름
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas 이름
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`canvas_variation_name` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 변형 이름
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`message_variation_name` | `null,`&nbsp;`string` | 메시지 변형 이름
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] 메시지를 수신하는 사용자의 전화번호(e.164 형식, 예: +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`from_rcs_sender` | `null,`&nbsp;`string` | 메시지 전송에 사용된 RCS 발신자 ID 또는 에이전트 이름
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`action` | `null,`&nbsp;`string` | 이 메시지에 대한 응답으로 취한 동작 (예: Subscribed, Unsubscribed 또는 None).
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas 이름
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`media_urls` | `null,`&nbsp;`string` | 사용자의 미디어 URL
`message_variation_name` | `null,`&nbsp;`string` | 메시지 변형 이름
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`user_phone_number` | `null,`&nbsp;`string` | [PII] 메시지를 수신한 사용자의 전화번호
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`message_body` | `null,`&nbsp;`string` | 사용자의 입력 응답
`to_rcs_sender` | `null,`&nbsp;`string` | 메시지가 전송된 인바운드 RCS 발신자
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas 이름
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`canvas_variation_name` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 변형 이름
`message_variation_name` | `null,`&nbsp;`string` | 메시지 변형 이름
`to_phone_number` | `null,`&nbsp;`string` | [PII] 메시지를 수신하는 사용자의 전화번호(e.164 형식, 예: +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas 이름
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`canvas_variation_name` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 변형 이름
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`error` | `null,`&nbsp;`string` | 오류 이름
`from_rcs_sender` | `null,`&nbsp;`string` | 메시지 전송에 사용된 RCS 발신자 ID 또는 에이전트 이름
`is_sms_fallback` | `null, boolean` | 이 거부된 RCS 메시지에 대해 SMS 대체가 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트와 연결/페어링됩니다
`message_variation_name` | `null,`&nbsp;`string` | 메시지 변형 이름
`provider_error_code` | `null,`&nbsp;`string` | 공급자의 오류 코드
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] 메시지를 수신하는 사용자의 전화번호(e.164 형식, 예: +14155552671)
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvas 이름
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`canvas_variation_name` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 변형 이름
`category` | `null,`&nbsp;`string` | 키워드 카테고리 이름, 자동 응답 메시지에만 채워짐: 'opt-in', 'opt-out', 'help' 또는 커스텀 값
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`from_rcs_sender` | `null,`&nbsp;`string` | 메시지 전송에 사용된 RCS 발신자 ID 또는 에이전트 이름
`message_extras` | `null,`&nbsp;`string` | Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`message_variation_name` | `null,`&nbsp;`string` | 메시지 변형 이름
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] 메시지를 수신하는 사용자의 전화번호(e.164 형식, 예: +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`subscription_group_api_id` | `null,`&nbsp;`string` | 구독 그룹의 외부 ID
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`to_phone_number` | `null,`&nbsp;`string` | [PII] 수신자의 전화번호
`from_phone_number` | `null,`&nbsp;`string` | SMS 메시지가 전송된 전화번호
`subscription_group_api_id` | `null,`&nbsp;`string` | 구독 그룹의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`to_phone_number` | `null,`&nbsp;`string` | [PII] 수신자의 전화번호
`from_phone_number` | `null,`&nbsp;`string` | SMS 메시지가 전송된 전화번호
`subscription_group_api_id` | `null,`&nbsp;`string` | 구독 그룹의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`is_sms_fallback` | `null, boolean` | 이 거부된 RCS 메시지에 대해 SMS 대체가 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트와 연결/페어링됩니다
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`to_phone_number` | `null,`&nbsp;`string` | [PII] 수신자의 전화번호
`subscription_group_api_id` | `null,`&nbsp;`string` | 구독 그룹의 외부 ID
`error` | `null,`&nbsp;`string` | 오류 이름
`provider_error_code` | `null,`&nbsp;`string` | SMS 서비스 공급자의 오류 코드
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`is_sms_fallback` | `null, boolean` | 이 거부된 RCS 메시지에 대해 SMS 대체가 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트와 연결/페어링됩니다
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `null,`&nbsp;`string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`app_group_api_id` | `null,`&nbsp;`string` | 인바운드 전화번호와 연결된 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_phone_number` | `string` | [PII] 메시지를 수신한 사용자의 전화번호
`subscription_group_id` | `null,`&nbsp;`string` | 이 SMS 메시지의 대상 구독 그룹 ID
`subscription_group_api_id` | `null,`&nbsp;`string` | 이 SMS 메시지의 대상 구독 그룹 API ID
`inbound_phone_number` | `string` | 메시지가 전송된 인바운드 번호
`action` | `string` | 이 메시지에 대한 응답으로 취한 동작. 예: `Subscribed`, `Unsubscribed` 또는 `None`.
`message_body` | `string` | 사용자의 응답
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | 사용자의 미디어 URL
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계 메시지 변형의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`to_phone_number` | `null,`&nbsp;`string` | [PII] 수신자의 전화번호
`from_phone_number` | `null,`&nbsp;`string` | SMS 메시지가 전송된 전화번호
`subscription_group_api_id` | `null,`&nbsp;`string` | 구독 그룹의 외부 ID
`error` | `null,`&nbsp;`string` | 오류 이름
`provider_error_code` | `null,`&nbsp;`string` | SMS 서비스 공급자의 오류 코드
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`is_sms_fallback` | `null, boolean` | 이 거부된 RCS 메시지에 대해 SMS 대체가 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트와 연결/페어링됩니다
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`to_phone_number` | `null,`&nbsp;`string` | [PII] 수신자의 전화번호
`subscription_group_api_id` | `null,`&nbsp;`string` | 구독 그룹의 외부 ID
`category` | `null,`&nbsp;`string` | 키워드 카테고리 이름, 자동 응답 메시지에만 채워짐: 'Opt-in', 'Opt-out', 'Help' 또는 커스텀 값
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `null,`&nbsp;`string` | short_url의 대상 사용자의 Braze ID, short_url이 사용자 클릭 추적을 사용하지 않는 경우 null
`external_user_id` | `null,`&nbsp;`string` | [PII] short_url의 대상 사용자의 외부 ID(존재하는 경우), short_url이 사용자 클릭 추적을 사용하지 않는 경우 null
`app_group_api_id` | `null,`&nbsp;`string` | short_url 생성에 사용된 워크스페이스의 API ID
`time` | `int` | short_url이 클릭된 Unix 타임스탬프
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`campaign_id` | `null,`&nbsp;`string` | short_url이 생성된 캠페인의 Braze ID, 캠페인이 아닌 경우 null
`campaign_api_id` | `null,`&nbsp;`string` | short_url이 생성된 캠페인의 API ID, 캠페인이 아닌 경우 null
`message_variation_api_id` | `null,`&nbsp;`string` | short_url이 생성된 메시지 변형의 API ID, 캠페인이 아닌 경우 null
`canvas_id` | `null,`&nbsp;`string` | short_url이 생성된 Canvas의 Braze ID, Canvas가 아닌 경우 null
`canvas_api_id` | `null,`&nbsp;`string` | short_url이 생성된 Canvas의 API ID, Canvas가 아닌 경우 null
`canvas_variation_api_id` | `null,`&nbsp;`string` | short_url이 생성된 Canvas 변형의 API ID, Canvas가 아닌 경우 null
`canvas_step_api_id` | `null,`&nbsp;`string` | short_url이 생성된 Canvas 단계의 API ID, Canvas가 아닌 경우 null
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | short_url이 생성된 Canvas 단계 메시지 변형의 API ID, Canvas가 아닌 경우 null
`url` | `string` | short_url이 리디렉션하는 메시지에 포함된 원본 URL
`short_url` | `string` | 클릭된 단축 URL
`user_agent` | `null,`&nbsp;`string` | short_url을 요청하는 사용자 에이전트
`user_phone_number` | `string` | [PII] 사용자의 전화번호
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`is_suspected_bot_click` | `null, boolean` | 이 이벤트가 봇 이벤트로 처리되었는지 여부
`suspected_bot_click_reason` | `null, object` | 이 이벤트가 봇으로 분류된 이유
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_RETRY_SHARED {#USERS_MESSAGES_SMS_RETRY_SHARED}

{% alert note %}
이 테이블은 Snowflake 데이터 공유에서만 사용할 수 있습니다.
{% endalert %}

이 이벤트는 메시지의 우선순위가 낮아지거나 빈도 제한이 적용되어 설정된 재시도 기간 내에 나중에 재시도될 때 발생합니다.

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | [PII] 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`subscription_group_api_id` | `null,`&nbsp;`string` | 구독 그룹 API ID
`retry_type` | `null,`&nbsp;`string` | 재시도 유형
`retry_log` | `null,`&nbsp;`string` | 재시도 세부 정보를 설명하는 로그 메시지
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

필드 | 유형 | 설명
------|------|------------
`http_status_code` | `null, int` | 응답의 HTTP 상태 코드
`endpoint_url` | `null,`&nbsp;`string` | 요청 중인 엔드포인트 URL
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`content_length` | `null, int` | 응답의 콘텐츠 길이
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`host` | `null,`&nbsp;`string` | 요청의 호스트
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`raw_response` | `null,`&nbsp;`string` | 엔드포인트의 잘린 원시 응답
`retry_count` | `null, int` | 시도된 재시도 횟수
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`url_path` | `null,`&nbsp;`string` | 요청 중인 URL의 경로
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`webhook_duration` | `null, int` | 이 요청의 총 소요 시간(밀리초)
`webhook_failure_source` | `null,`&nbsp;`string` | 오류가 Braze에 의해 생성되었는지 엔드포인트 자체에 의해 생성되었는지를 나타냅니다. 소스 필드는 External Endpoint, Treat no status code to host unreachable일 수 있습니다
`is_terminal` | `null, boolean` | 이 이벤트가 전송의 최종 시도였는지 여부
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`campaign_name` | `null,`&nbsp;`string` | 캠페인 이름
`message_variation_name` | `null,`&nbsp;`string` | 메시지 변형 이름
`canvas_name` | `null,`&nbsp;`string` | Canvas 이름
`canvas_variation_name` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 변형 이름
`canvas_step_name` | `null,`&nbsp;`string` | Canvas 단계 이름
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_RETRY_SHARED {#USERS_MESSAGES_WEBHOOK_RETRY_SHARED}

{% alert note %}
이 테이블은 Snowflake 데이터 공유에서만 사용할 수 있습니다.
{% endalert %}

이 이벤트는 메시지의 우선순위가 낮아지거나 빈도 제한이 적용되어 설정된 재시도 기간 내에 나중에 재시도될 때 발생합니다.

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | [PII] 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`gender` | `null,`&nbsp;`string` | [PII] 사용자의 성별
`country` | `null,`&nbsp;`string` | [PII] 사용자의 국가
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`language` | `null,`&nbsp;`string` | [PII] 사용자의 언어
`retry_type` | `null,`&nbsp;`string` | 재시도 유형
`retry_log` | `null,`&nbsp;`string` | 재시도 세부 정보를 설명하는 로그 메시지
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`to_phone_number` | 	`null,`&nbsp;`string` | [PII] 수신자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`abort_type` | `null,`&nbsp;`string` | 중단 유형. 값 목록은 [중단 유형](#abort-types)을 참조하세요.
`abort_log` | `null,`&nbsp;`string` | [PII] 중단 세부 정보를 설명하는 로그 메시지 (최대 2,000자)
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`url` | `null,`&nbsp;`string` | 사용자가 클릭한 URL
`short_url` | `null,`&nbsp;`string` | 클릭된 단축 URL
`user_agent` | `null,`&nbsp;`string` | 스팸 신고가 발생한 사용자 에이전트
`user_phone_number` | `null,`&nbsp;`string` | [PII] 메시지를 수신한 사용자의 전화번호
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`to_phone_number` | `null,`&nbsp;`string` | [PII] 수신자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp 메시지가 전송된 전화번호
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager의 Flow 고유 ID. 사용자가 WhatsApp Flow에 응답하는 경우 존재합니다.
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager의 템플릿 이름. 템플릿 메시지를 전송하는 경우 존재합니다
`message_id` | `null,`&nbsp;`string` | Meta에서 이 메시지에 대해 생성한 고유 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`to_phone_number` | `null,`&nbsp;`string` | [PII] 수신자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp 메시지가 전송된 전화번호
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`provider_error_code` | `null,`&nbsp;`string` | WhatsApp의 오류 코드
`provider_error_title` | `null, `&nbsp;`string` | WhatsApp의 오류 제목
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`message_id` | `null,`&nbsp;`string` | Meta에서 이 메시지에 대해 생성한 고유 ID
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager의 템플릿 이름. 템플릿 메시지를 전송하는 경우 존재합니다
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager의 Flow 고유 ID. 사용자가 WhatsApp Flow에 응답하는 경우 존재합니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`user_phone_number` | `string` | [PII] 메시지를 수신한 사용자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`inbound_phone_number` | `string` | 메시지가 전송된 인바운드 번호
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`message_body` | `string` | 사용자의 응답
`quick_reply_text` | `string` | 사용자가 누른 버튼의 텍스트
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | 사용자의 미디어 URL
`action` | `string` | 이 메시지에 대한 응답으로 취한 동작. 예: `Subscribed`, `Unsubscribed` 또는 `None`.
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
`catalog_id` | `null,`&nbsp;`string` | 인바운드 메시지에서 제품이 참조된 경우 제품의 카탈로그 ID. 그렇지 않으면 비어 있습니다.
`product_id` | `null,`&nbsp;`string` | 구매한 제품의 ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager의 Flow 고유 ID. 사용자가 WhatsApp Flow에 응답하는 경우 존재합니다.
`flow_response_json` | `null,`&nbsp;`string` | [PII] 사용자가 응답한 양식 값. 사용자가 WhatsApp Flow에 응답하는 경우 존재합니다.
`message_id` | `null,`&nbsp;`string` | Meta에서 이 메시지에 대해 생성한 고유 ID
`in_reply_to` | `null,`&nbsp;`string` | 이 메시지가 답장한 메시지의 message_id
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`to_phone_number` | `null,`&nbsp;`string` | [PII] 수신자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp 메시지가 전송된 전화번호
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager의 템플릿 이름. 템플릿 메시지를 전송하는 경우 존재합니다
`message_id` | `null,`&nbsp;`string` | Meta에서 이 메시지에 대해 생성한 고유 ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager의 Flow 고유 ID. 사용자가 WhatsApp Flow에 응답하는 경우 존재합니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`to_phone_number` | `null,`&nbsp;`string`	| [PII] 수신자의 전화번호
`user_id` | `string` | 이 이벤트를 수행한 사용자의 Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 사용자 ID
`device_id` | `null,`&nbsp;`string` | 사용자가 익명인 경우 이 사용자에게 연결된 `device_id`
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp 메시지가 전송된 전화번호
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 워크스페이스의 API ID
`subscription_group_api_id` | `string` | 구독 그룹 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 내부용 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 내부용 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid 렌더링 중 태그된 키-값 페어의 JSON 문자열
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
`send_id` | `null,`&nbsp;`string` | 이 메시지가 속한 메시지 전송 ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager의 Flow 고유 ID. 사용자가 WhatsApp Flow에 응답하는 경우 존재합니다.
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager의 템플릿 이름. 템플릿 메시지를 전송하는 경우 존재합니다
`message_id` | `null,`&nbsp;`string` | Meta에서 이 메시지에 대해 생성한 고유 ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED {#USERS_MESSAGES_WHATSAPP_RETRY_SHARED}

{% alert note %}
이 테이블은 Snowflake 데이터 공유에서만 사용할 수 있습니다.
{% endalert %}

이 이벤트는 메시지의 우선순위가 낮아지거나 빈도 제한이 적용되어 설정된 재시도 기간 내에 나중에 재시도될 때 발생합니다.

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`user_id` | `string` | [PII] 이 이벤트를 수행한 사용자의 Braze 사용자 ID
`external_user_id` | `null,`&nbsp;`string` | [PII] 사용자의 외부 ID
`app_group_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | 이 사용자가 속한 앱 그룹의 API ID
`time` | `int` | 이벤트가 발생한 Unix 타임스탬프
`to_phone_number` | `null,`&nbsp;`string` | [PII] 메시지를 수신하는 사용자의 전화번호(e.164 형식)
`device_id` | `null,`&nbsp;`string` | 이벤트가 발생한 기기의 ID
`timezone` | `null,`&nbsp;`string` | 사용자의 시간대
`subscription_group_api_id` | `null,`&nbsp;`string` | 구독 그룹 API ID
`campaign_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 캠페인의 API ID
`message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 메시지 변형의 API ID
`canvas_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas의 API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 변형의 API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | 이 이벤트가 속한 Canvas 단계의 API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | 이 사용자가 수신한 Canvas 단계 메시지 변형의 API ID
`dispatch_id` | `null,`&nbsp;`string` | 이 메시지가 속한 디스패치의 ID
`retry_type` | `null,`&nbsp;`string` | 재시도 유형
`retry_log` | `null,`&nbsp;`string` | 재시도 세부 정보를 설명하는 로그 메시지
`sf_created_at` | `timestamp`,&nbsp;`null` | 이 이벤트가 Snowpipe에 의해 수집된 시점
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 사용자

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| 필드                       | 유형                     | 설명                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                  |
| `app_group_id`              | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID      |
| `app_group_api_id`          | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 API ID       |
| `user_id`                   | `string`,&nbsp;`null`    | 이 이벤트를 수행한 사용자의 Braze ID      |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                 |
| `time`                      | `int`,&nbsp;`null`       | 이벤트가 발생한 Unix 타임스탬프         |
| `random_bucket_number`      | `int`,&nbsp;`null`       | 사용자에게 할당된 현재 무작위 버킷 번호  |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | 사용자에게 할당된 이전 무작위 버킷 번호 |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Snowpipe에서 이 이벤트를 수집한 시점      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| 필드              | 유형                     | 설명                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                             |
| `user_id`          | `string`,&nbsp;`null`    | 삭제된 사용자의 Braze ID                          |
| `app_group_id`     | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                 |
| `app_group_api_id` | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 API ID                  |
| `time`             | `int`,&nbsp;`null`       | 사용자 삭제 요청이 처리된 Unix 타임스탬프 |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Snowpipe에서 이 이벤트를 수집한 시점                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| 필드              | 유형                     | 설명                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | 이 이벤트의 글로벌 고유 ID                                             |
| `user_id`          | `string`,&nbsp;`null`    | 고아 상태가 된 사용자의 Braze ID                                         |
| `external_user_id` | `string`,&nbsp;`null`    | [PII] 사용자의 외부 사용자 ID                                            |
| `device_id`        | `string`,&nbsp;`null`    | 이 사용자에게 연결된 기기의 ID(사용자가 익명인 경우)          |
| `app_group_id`     | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 Braze ID                                 |
| `app_group_api_id` | `string`,&nbsp;`null`    | 이 사용자가 속한 워크스페이스의 API ID                                  |
| `app_api_id`       | `string`,&nbsp;`null`    | 고아 상태가 된 사용자가 속했던 앱의 API ID                               |
| `time`             | `int`,&nbsp;`null`       | 사용자가 고아 상태가 된 Unix 타임스탬프                                 |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | 고아 상태가 된 사용자의 프로필과 병합된 사용자의 Braze ID |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Snowpipe에서 이 이벤트를 수집한 시점                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 스냅샷 {#snapshots}

{% alert note %}
스냅샷 테이블은 Snowflake 데이터 공유에서만 사용할 수 있습니다.
{% endalert %}

### SNAPSHOTS_APP_SHARED {#SNAPSHOTS_APP_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 UNIX 타임스탬프
`app_group_id` | `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`api_id` | `string` | 앱의 API ID
`name` | `null,`&nbsp;`string` | 앱의 이름
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED {#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 UNIX 타임스탬프
`app_group_id` | `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`api_id` | `string` | 캠페인 메시지 변형의 API ID
`name` | `null,`&nbsp;`string` | 캠페인 메시지 변형의 이름
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED {#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 UNIX 타임스탬프
`app_group_id` | `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`type` | `null,`&nbsp;`string` | Canvas Flow 단계의 유형
`api_step_id` | `string` | 캔버스 단계의 API ID
`experiment_splits` | `null,`&nbsp;`string` | 단계의 실험 분할
`conversion_behaviors` | `null,`&nbsp;`string` | 단계의 전환 동작
`name` | `null,`&nbsp;`string` | Canvas Flow 단계의 이름
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_STEP_SHARED {#SNAPSHOTS_CANVAS_STEP_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 UNIX 타임스탬프
`app_group_id` | `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`api_id` | `string` | 캔버스 단계의 API ID
`name` | `null,`&nbsp;`string` | 캔버스 단계의 이름
`actions` | `null,`&nbsp;`string` | 캔버스 단계의 동작
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_VARIATION_SHARED {#SNAPSHOTS_CANVAS_VARIATION_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 UNIX 타임스탬프
`app_group_id` | `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`api_id` | `string` | 캔버스 변형의 API ID
`name` | `null,`&nbsp;`string` | 캔버스 변형의 이름
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_EXPERIMENT_STEP_SHARED {#SNAPSHOTS_EXPERIMENT_STEP_SHARED}

필드 | 유형 | 설명
------|------|------------
`id` | `string` | 이 이벤트의 글로벌 고유 ID
`time` | `int` | 이벤트가 발생한 UNIX 타임스탬프
`app_group_id` | `string` | 이 사용자가 속한 앱 그룹의 BSON ID
`type` | `null,`&nbsp;`string` | 실험 단계의 유형
`api_step_id` | `string` | 실험 단계의 API ID
`experiment_splits` | `null,`&nbsp;`string` | 단계의 실험 분할
`conversion_behaviors` | `null,`&nbsp;`string` | 단계의 전환 동작
`name` | `null,`&nbsp;`string` | 실험 단계의 이름
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 중단 유형

{% include abort_types_reference.md %}