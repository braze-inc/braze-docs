다음 표에는 가능한 `abort_type` 값이 나열되어 있습니다. 중단 유형은 메시지가 발송되지 않은 구체적인 이유를 설명합니다.

{% if include.channel %}
{% assign ch = include.channel %}
{% else %}
{% assign ch = "all" %}
{% endif %}

### 일반

이러한 중단 유형은 모든 메시징 채널에서 발생할 수 있습니다.

| `abort_type` 값 | 설명 |
| --- | --- |
| `liquid_abort_message` | [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) Liquid 태그가 호출되어 발송이 취소되었습니다. |
| `template_parse_error` | 구문 또는 렌더링 오류로 인해 메시지 템플릿을 구문 분석할 수 없어 발송이 취소되었습니다. |
| `rate_limit` | 설정된 [사용량 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)을 초과하여 메시지가 중단되었습니다. |
| `campaign_disabled` | 메시지가 발송되기 전에 캠페인이 비활성화되었습니다. |
| `campaign_does_not_exist` | 이 메시지와 연결된 캠페인이 더 이상 존재하지 않습니다. |
| `campaign_action_does_not_exist` | 이 메시지와 연결된 캠페인 동작이 더 이상 존재하지 않습니다. |
| `message_variation_does_not_exist` | 이 사용자에게 할당된 메시지 변형이 더 이상 존재하지 않습니다. |
| `user_not_in_segment` | 사용자가 타겟 세그먼트에 포함되지 않아 메시지가 발송되지 않았습니다. |
| `trigger_event_blacklisted` | 트리거 이벤트가 차단 목록에 있어 메시지가 발송되지 않았습니다. |
| `exhausted_retries` | 최대 재시도 횟수를 초과한 후에도 메시지를 발송할 수 없었습니다. |
| `frequency_capped` | 워크스페이스의 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) 규칙에서 허용하는 최대 메시지 수를 사용자가 이미 수신했습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% unless ch == "newsfeedcard" or ch == "rcs" %}

### 콘텐츠 및 렌더링

| `abort_type` 값 | 설명 |
| --- | --- |
| `exhausted_cc_retries` | 최대 재시도 횟수를 초과한 후에도 연결된 콘텐츠가 실패하여 메시지가 중단되었습니다. |
| `connected_content_not_supported` | 이 컨텍스트에서는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)가 지원되지 않아 메시지가 중단되었습니다. |
| `promo_codes_not_supported` | 이 컨텍스트에서는 프로모션 코드가 지원되지 않아 메시지가 중단되었습니다. |
| `catalog_items_rerender_not_supported` | 이 컨텍스트에서는 카탈로그 항목 재렌더링이 지원되지 않아 메시지가 중단되었습니다. |
{% if ch == "all" or ch == "email" or ch == "push" or ch == "inappmessage" or ch == "contentcard" or ch == "webhook" or ch == "banner" %}| `blacklisted_media_url` | 미디어 URL이 차단 목록에 있어 메시지에 사용할 수 없습니다. |
| `blocked_media_url` | 보안 정책에 의해 미디어 URL이 차단되었습니다. |
| `invalid_media_url` | 미디어 URL이 유효하지 않거나 확인할 수 없습니다. |{% endif %}
{% if ch == "all" or ch == "email" or ch == "webhook" %}| `ssl_error` | 요청 중 SSL 오류가 발생했습니다. |
| `invalid_http_status` | HTTP 요청이 실패 상태 코드를 반환했습니다. |
| `http_timeout` | 응답을 받기 전에 HTTP 요청이 시간 초과되었습니다. |
| `missing_hostname` | 요청 URL에 호스트 이름이 없습니다. |{% endif %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endunless %}

{% if ch == "all" or ch == "email" %}

### 이메일

| `abort_type` 값 | 설명 |
| --- | --- |
| `exhausted_link_shortening_retries` | 최대 재시도 횟수를 초과한 후에도 링크 단축이 실패했습니다. |
| `missing_email` | 사용자의 프로필에 이메일 주소가 없습니다. |
| `invalid_domain` | 이메일 주소의 도메인이 유효하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "push" %}

### 푸시

| `abort_type` 값 | 설명 |
| --- | --- |
| `invalid_push_payload` | 푸시 알림 페이로드가 유효하지 않거나 형식이 잘못되었습니다. |
| `sdk_not_supported` | 사용자 기기의 SDK 버전이 이 유형의 푸시 알림을 지원하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "sms" %}

### SMS/MMS

| `abort_type` 값 | 설명 |
| --- | --- |
| `exhausted_link_shortening_retries` | 최대 재시도 횟수를 초과한 후에도 링크 단축이 실패했습니다. |
| `sms_empty_payload` | SMS 메시지 본문이 비어 있습니다. |
| `sms_no_sending_numbers` | 이 구독 그룹에 사용 가능한 발신 전화번호가 없습니다. |
| `sms_fatal_provider_error` | SMS 공급자에서 심각한 오류가 발생하여 메시지를 전달할 수 없습니다. |
| `sms_gateway_domain_not_allowed` | SMS 게이트웨이 도메인이 허용 목록에 없습니다. |
| `blocked_recipient_country` | 수신자의 전화번호가 [지역 권한]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/)에 의해 차단된 국가에 있습니다. |
| `mms_not_supported` | 이 수신자 또는 발신 번호에 대해 MMS가 지원되지 않습니다. |
| `no_current_messaging_service` | 이 구독 그룹에 활성 메시징 서비스가 구성되어 있지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "whatsapp" %}

### WhatsApp

| `abort_type` 값 | 설명 |
| --- | --- |
| `whats_app_no_sending_numbers` | 이 WhatsApp 구독 그룹에 사용 가능한 발신 전화번호가 없습니다. |
| `whats_app_invalid_template_message` | WhatsApp 템플릿 메시지가 유효하지 않거나 승인되지 않았습니다. |
| `whats_app_invalid_response_message` | WhatsApp 응답 메시지가 유효하지 않습니다. |
| `whats_app_fatal_provider_error` | WhatsApp 공급자에서 심각한 오류가 발생하여 메시지를 전달할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "line" %}

### LINE

| `abort_type` 값 | 설명 |
| --- | --- |
| `line_fatal_provider_error` | LINE 공급자에서 심각한 오류가 발생하여 메시지를 전달할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "kakao" %}

### Kakao

| `abort_type` 값 | 설명 |
| --- | --- |
| `kakao_fatal_provider_error` | Kakao 공급자에서 심각한 오류가 발생하여 메시지를 전달할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "contentcard" %}

### 콘텐츠 카드

| `abort_type` 값 | 설명 |
| --- | --- |
| `content_card_size_exceeded` | 콘텐츠 카드 페이로드가 최대 크기 제한(2 KB)을 초과했습니다. |
| `content_card_content_invalid` | 콘텐츠 카드 콘텐츠가 유효하지 않거나 지원되지 않는 문자를 포함하고 있습니다. |
| `content_card_expiration_invalid` | 콘텐츠 카드 만료 날짜가 유효하지 않습니다. |
| `content_card_general` | 일반 오류로 인해 콘텐츠 카드를 생성할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "inappmessage" %}

### 인앱 메시지

| `abort_type` 값 | 설명 |
| --- | --- |
| `no_longer_in_availability_window` | 설정된 가용 기간 내에 메시지를 발송할 수 없어 중단되었습니다. |
| `maximum_impressions_reached` | 인앱 메시지가 이미 최대 노출 횟수에 도달했습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "webhook" %}

### 웹훅

| `abort_type` 값 | 설명 |
| --- | --- |
| `blocked_webhook_url` | 보안 정책에 의해 웹훅 URL이 차단되었습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}