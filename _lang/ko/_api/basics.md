---
nav_title: "API 개요"
article_title: API 개요
page_order: 2.1
description: "이 참조 문서에서는 REST API가 무엇인지, 용어, API 키에 대한 개요를 포함하여 API 기본 사항을 다룹니다."
page_type: reference
alias: /api/api_key/
---

# API 개요

> 이 참조 문서는 API 기본 사항, 일반 용어 및 REST API 키, 권한 및 이를 안전하게 유지하는 방법에 대한 개요를 다룹니다.

## Braze REST API 컬렉션

| 컬렉션                                                                 | 목적                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [카탈로그]({{site.baseurl}}/api/endpoints/catalogs/)                       | Braze 캠페인에서 참조할 카탈로그와 카탈로그 항목을 생성하고 관리합니다.    |
| [클라우드 데이터 수집]({{site.baseurl}}/api/endpoints/cdi/)                | 데이터 웨어하우스 통합 및 동기화를 관리합니다.                                    |
| [이메일 목록 및 주소]({{site.baseurl}}/api/endpoints/email/)         | Braze와 이메일 시스템 간의 양방향 동기화를 설정하고 관리하세요.           |
| [내보내기]({{site.baseurl}}/api/endpoints/export/)                           | 캠페인, 캔버스, KPI 등에 대한 다양한 세부 정보에 액세스하고 내보낼 수 있습니다.        |
| [메시지]({{site.baseurl}}/api/endpoints/messaging/)                      | 캠페인과 캔버스를 예약, 전송 및 관리하세요.                               |
| [환경 설정 센터]({{site.baseurl}}/api/endpoints/preference_center/)     | 환경설정 센터를 구축하고 스타일링을 업데이트하세요.                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | 클라우드 기반 애플리케이션 및 서비스에서 사용자 ID를 관리하세요.                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | 구독 그룹에서 사용자의 전화번호를 관리하세요.                         |
| [구독 그룹]({{site.baseurl}}/api/endpoints/subscription_groups/) | Braze 대시보드에 저장된 SMS 및 이메일 구독 그룹을 모두 나열하고 업데이트합니다. |
| [템플릿]({{site.baseurl}}/api/endpoints/templates/)                     | 이메일 메시징 및 콘텐츠 블록용 템플릿을 만들고 업데이트합니다.                   |
| [사용자 데이터]({{site.baseurl}}/api/endpoints/user_data/)                     | 사용자를 식별, 추적 및 관리하세요.                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## API 정의

다음은 Braze REST API 설명서에서 볼 수 있는 용어에 대한 개요입니다.

### 엔드포인트

Braze는 대시보드 및 REST 엔드포인트에 대한 다양한 인스턴스를 관리합니다. 계정이 프로비저닝되면 다음 URL 중 하나에 로그인하게 됩니다. 프로비저닝된 인스턴스에 따라 올바른 REST 엔드포인트를 사용하세요. 확실하지 않은 경우, [지원 티켓]({{site.baseurl}}/braze_support/)을 열거나 사용 중인 대시보드의 URL을 올바른 REST 엔드포인트에 맞추기 위해 다음 표를 사용하세요.

{% alert important %}
API 호출에 엔드포인트를 사용할 때는 REST 엔드포인트를 사용하세요.

SDK 통합을 위해 [SDK 엔드포인트]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)를 사용하고, REST 엔드포인트는 사용하지 마십시오.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='instances' %}

### API 제한

대부분의 API에 대해 Braze는 시간당 250,000개의 요청에 대한 기본값 속도 제한이 있습니다. 그러나 특정 요청 유형에는 고객 기반의 대량 데이터를 더 잘 처리하기 위해 적용되는 자체 요금 제한이 있습니다. 자세한 내용은 [API 속도 제한]({{site.baseurl}}/api/api_limits/)을 참조하십시오.

### 사용자 ID

- **외부 사용자 ID**: `external_id`는 데이터를 제출하는 사용자에 대한 고유 식별자로 사용됩니다. 이 식별자는 동일한 사용자를 위해 여러 프로필을 생성하지 않도록 Braze SDK에 설정한 것과 같아야 합니다.
- **브레이즈 사용자 ID**: `braze_id`는 브레이즈에 의해 설정된 고유 사용자 식별자로 사용됩니다. 이 식별자는 외부 ID 외에도 REST API를 통해 사용자를 삭제하는 데 사용할 수 있습니다.

자세한 내용은 플랫폼에 따라 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) 및 [웹에]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/) 대한 다음 도움말 문서를 참조하세요.

## REST API 키에 대하여

REST 애플리케이션 프로그래밍 인터페이스 키(REST API 키)는 API 호출을 인증하고 호출하는 애플리케이션 또는 사용자를 식별하기 위해 API에 전달되는 고유한 코드입니다. API 액세스는 회사의 REST API 엔드포인트에 대한 HTTPS 웹 요청을 사용하여 수행됩니다. 우리는 Braze에서 REST API 키를 앱 식별자 키와 함께 사용하여 데이터를 추적, 접근, 전송, 내보내기 및 분석하여 귀하와 저희 쪽 모두에서 모든 것이 원활하게 작동하는지 확인합니다.

작업 공간과 API 키는 Braze에서 함께 사용됩니다. 작업 공간은 여러 플랫폼에서 동일한 애플리케이션의 버전을 수용하도록 설계되었습니다. 많은 고객들이 또한 동일한 플랫폼에서 애플리케이션의 무료 및 프리미엄 버전을 포함하기 위해 작업 공간을 사용합니다. 당신이 알다시피, 이러한 작업 공간은 REST API를 사용하고 있으며 자체 REST API 키를 가지고 있습니다. 이 키는 API의 특정 엔드포인트에 대한 액세스를 포함하도록 개별적으로 범위를 지정할 수 있습니다. 각 API 호출에는 엔드포인트 히트에 대한 액세스 권한이 있는 키가 포함되어야 합니다.

우리는 REST API 키와 작업 공간 API 키를 모두 `api_key`이라고 부릅니다. 각 `api_key`는 요청 헤더로 포함되며, REST API를 사용할 수 있도록 하는 인증 키 역할을 합니다. 이 REST API는 사용자를 추적하고, 메시지를 보내고, 사용자 데이터를 내보내는 데 사용됩니다. 새로운 REST API 키를 생성할 때, 특정 엔드포인트에 대한 액세스를 부여해야 합니다. API 키에 특정 권한을 할당하면 API 키가 인증할 수 있는 호출을 정확히 제한할 수 있습니다.

![API 키 탭의 REST API 키 패널입니다.]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
REST API 키 외에도 특정 앱, 템플릿, 캔버스, 캠페인, 콘텐츠 카드 및 API의 세그먼트를 참조하는 데 사용할 수 있는 식별자 키라는 유형의 키도 존재합니다. 자세한 내용은 [API 식별자 유형]({{site.baseurl}}/api/identifier_types/)을 참조하세요.
{% endalert %}

### REST API 키 만들기

새 REST API 키를 만들려면 다음과 같이 하세요:

1. **설정** > **API 및 식별자로** 이동합니다.
2. **API 키 생성을** 선택합니다.
3. 새 키에 한눈에 식별할 수 있는 이름을 지정하세요.
4. 새 키의 [허용 목록에 있는 IP 주소](#api-ip-allowlisting) 및 서브넷을 지정합니다.
5. 새 키에 연결할 [권한을](#rest-api-key-permissions) 선택합니다.

{% alert important %}
새 API 키를 생성한 후에는 권한 범위나 허용된 IP를 편집할 수 없습니다. 이 제한은 보안상의 이유로 시행되고 있습니다. 키의 범위를 변경해야 하는 경우 업데이트된 권한으로 새 키를 만들고 이전 키 대신 해당 키를 구현하세요. 구현을 완료한 후에는 이전 키를 삭제할 수 있습니다.
{% endalert %}

### REST API 키 권한

API 키 권한은 사용자가 특정 API 호출에 대한 액세스를 제한할 수 있도록 사용자 또는 그룹에 할당할 수 있는 권한입니다. API 키 권한 목록을 보려면 **설정** > **API 및 식별자**로 이동하여 API 키를 선택하십시오.

{% tabs %}
{% tab 사용자 데이터 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | 사용자 속성, 사용자 지정 이벤트 및 구매 이벤트를 기록합니다. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | 사용자를 삭제합니다. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |기존 사용자의 새 별칭을 생성합니다. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |외부 ID로 별칭 전용 사용자를 식별합니다. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |사용자 프로필 정보를 사용자 ID별로 조회합니다. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |세그먼트별로 사용자 프로필 정보를 쿼리합니다. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | 기존 사용자 두 명을 서로 병합합니다. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | 기존 사용자의 외부 ID를 변경합니다. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | 기존 사용자의 외부 ID를 제거합니다. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | 기존 사용자의 별칭을 업데이트합니다. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | 전역 대조군에 있는 사용자 프로필 정보를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

 {% endtab %}
 {% tab 이메일 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | 구독취소한 이메일 주소를 조회합니다.  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | 이메일 주소의 상태를 변경합니다. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | 하드바운스된 이메일 주소를 조회합니다. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | 하드바운스 목록의 이메일 주소를 제거합니다. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | 스팸 목록의 이메일 주소를 제거합니다. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | 이메일 주소를 차단 목록에 추가합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 메시지 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | 특정 사용자에게 즉시 메시지를 보냅니다. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | 특정 시간에 발송할 메시지를 예약합니다. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | 예약된 메시지를 업데이트합니다. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | 예약된 메시지를 삭제합니다. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | 예약된 모든 브로드캐스트 메시지를 조회합니다. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | iOS 라이브 활동을 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 캠페인 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | 기존 캠페인 전송을 트리거합니다. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | API 트리거 전송을 통해 향후 캠페인 전송을 예약합니다. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | API 트리거 전송으로 예약된 캠페인을 업데이트합니다. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |API 트리거 전송으로 예약된 캠페인을 삭제합니다. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | 캠페인 목록을 쿼리합니다. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | 일정 기간 동안 캠페인 분석을 쿼리합니다. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | 특정 캠페인에 대한 세부 정보를 쿼리합니다. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | 일정 시간 범위에 대한 메시지 발송 분석을 조회합니다. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | 메시지 폭발 추적을 위한 전송 ID를 만듭니다. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | 캠페인 내 특정 메시지 배리언트의 URL 세부 정보를 조회합니다. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | 트랜잭션 메시징 엔드포인트를 사용하여 트랜잭션 메시징을 보낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 캔버스 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | 기존 캔버스의 발송을 트리거합니다. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | 향후 캔버스 발송을 API 트리거 전달로 예약합니다. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | API 트리거 전달로 예약된 캔버스를 업데이트합니다. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| API 트리거 전달로 예약된 캔버스를 삭제합니다. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |  캔버스의 목록을 조회합니다. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | 일정 시간 범위에 대한 캔버스 분석을 조회합니다. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | 특정 캔버스의 세부 정보를 조회합니다. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | 일정 시간 범위에 대한 캔버스 분석의 롤업을 조회합니다. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | 캔버스 단계 내에서 특정 메시지 변형에 대한 URL 세부 정보를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 세그먼트 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | 세그먼트 목록을 쿼리합니다. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | 시간 범위에 대한 세그먼트 분석을 쿼리합니다. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | 특정 세그먼트에 대한 세부 정보를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 구매 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | 해당 앱에서 구매가 일어난 제품의 목록을 조회합니다. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | 일정 시간 범위 내 해당 앱에서 기록된 일일 총 지출액을 조회합니다. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | 특정 기간 동안 앱의 하루 총 구매 수를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 이벤트 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | 사용자 지정 이벤트 목록을 쿼리합니다. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | 시간 범위에 따른 사용자 지정 이벤트 발생을 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 세션 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | 일정 시간 범위 내 일일 세션 수를 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab KPI %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |  일정 시간 범위 내 일일 고유 활성 사용자 수를 조회합니다. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | 일정 시간 범위 내 30일 롤링 기간 동안의 총 고유 활성 사용자 수를 조회합니다. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | 일정 시간 범위 내 일일 새로운 사용자 수를 조회합니다. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | 일정 시간 범위 내 일일 앱 설치 제거 횟수를 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 템플릿 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | 대시보드에서 새 이메일 템플릿을 만듭니다. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | 특정 템플릿의 정보를 조회합니다. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | 이메일 템플릿의 목록을 조회합니다. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | 대시보드에 저장된 이메일 템플릿을 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SSO %}

| 권한 | 설명 |
|---|---|---|
| `sso.saml.login` | ID 공급자 시작 로그인을 설정합니다. 자세한 내용은 [서비스 제공업체(SP) 시작 로그인을]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 콘텐츠 블록 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | 특정 템플릿의 정보를 조회합니다. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | 콘텐츠 블록의 목록을 조회합니다. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | 대시보드에서 새 콘텐츠 블록을 만듭니다. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | 대시보드에서 기존 콘텐츠 블록을 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 환경 설정 센터 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | 환경설정 센터를 가져옵니다. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | 환경설정 센터를 열거합니다. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | 환경설정 센터를 만들거나 업데이트합니다. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | 사용자 대상의 환경설정 센터 링크를 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 구독 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | 구독 그룹 상태를 설정합니다. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | 구독 그룹 상태를 가져옵니다. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | 특정 사용자가 명시적으로 구독 및 구독 취소한 구독 그룹의 상태를 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SMS %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | 잘못된 전화번호를 조회합니다. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | 사용자에게서 잘못된 전화번호 플래그를 제거합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 카탈로그 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | 기존 카탈로그에 여러 항목을 추가합니다. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | 기존 카탈로그에 포함된 여러 항목을 업데이트합니다. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | 기존 카탈로그에서 여러 항목을 삭제합니다. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | 기존 카탈로그에서 단일 항목을 가져옵니다. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | 기존 카탈로그에 포함된 단일 항목을 업데이트합니다. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 기존 카탈로그 내에 단일 항목을 생성합니다. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | 기존 카탈로그에서 단일 항목을 삭제합니다. |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | 기존 카탈로그에 포함된 단일 항목을 교체합니다. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | 카탈로그를 만듭니다. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | 카탈로그 목록 가져오기 |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | 카탈로그를 삭제합니다. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | 기존 카탈로그에서 항목 미리보기를 가져옵니다. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | 기존 카탈로그의 항목을 교체합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SDK 인증 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | 앱을 위한 새로운 SDK 인증 키를 생성하세요. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/) | 앱을 위한 SDK 인증 키를 기본 키로 표시하세요. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | 앱을 위한 SDK 인증 키를 삭제하세요. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | 앱을 위한 모든 SDK 인증 키를 가져오세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### REST API 키 관리

기존 REST API 키의 세부 정보를 보거나 삭제할 수 있습니다 **설정** > **API 및 식별자** > **API 키** 탭. REST API 키는 생성된 후에 편집할 수 없습니다.

**API Keys** 탭에는 각 키에 대한 다음 정보가 포함됩니다:

| 필드        | 설명                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| API 키 이름 | 생성 시 키에 부여된 이름입니다.                                                                            |
| 식별자   | API 키입니다.                                                                                                        |
| 생성자   | 키를 생성한 사용자의 이메일 주소입니다. 2023년 6월 이전에 생성된 키의 경우 이 필드는 "N/A"로 표시됩니다. |
| 생성일 | 이 키가 생성된 날짜입니다.                                                                                      |
| 마지막 조회    | 이 키를 마지막으로 사용한 날짜입니다. 이 필드는 한 번도 사용하지 않은 키의 경우 "N/A"로 표시됩니다.                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

API 키의 세부 정보를 보려면 키 위에 마우스를 올리고 <i class="fa-solid fa-eye" alt="View"></i> **보기**를 선택하십시오. 이에는 이 키가 가진 모든 권한, 화이트리스트에 등록된 IP(있는 경우), 그리고 이 키가 Braze IP 화이트리스트에 등록되었는지 여부가 포함됩니다.

![Braze 대시보드의 API 키 권한 목록입니다.]({% image_buster /assets/img_archive/view-api-key.png %})

사용자를 [삭제할 때]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/), 사용자가 생성한 관련 API 키는 삭제되지 않습니다. 키를 삭제하려면 키 위에 마우스를 올리고 <i class="fa-solid fa-trash-can" alt="Delete"></i> **삭제**를 선택하세요.

![휴지통 아이콘이 강조 표시된 '마지막으로 본'이라는 이름의 API 키가 '삭제'를 보여줍니다.]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### REST API 키 보안

API 키는 API 호출을 인증하는 데 사용됩니다. 새로운 REST API 키를 생성할 때, 특정 엔드포인트에 대한 액세스를 부여해야 합니다. API 키에 특정 권한을 할당하면 API 키가 인증할 수 있는 호출을 정확히 제한할 수 있습니다.

REST API 키는 잠재적으로 민감한 REST API 엔드포인트에 대한 액세스를 허용하므로 이러한 키를 안전하게 보호하고 신뢰할 수 있는 파트너와만 공유하십시오. 키가 공개적으로 노출되어서는 안 됩니다. 예를 들어, 이 키를 사용하여 웹사이트에서 AJAX 호출을 하거나 다른 공개적인 방식으로 노출하지 마십시오.

좋은 보안 관행은 사용자에게 작업을 완료하는 데 필요한 만큼의 액세스 권한만 할당하는 것입니다. 이 원칙은 각 키에 권한을 할당하여 API 키에도 적용할 수 있습니다. 이러한 권한을 통해 계정의 다양한 영역에 대한 보안과 제어를 강화할 수 있습니다.

{% alert warning %}
REST API 키는 잠재적으로 민감한 REST API 엔드포인트에 대한 액세스를 허용하므로, 안전하게 저장하고 사용해야 합니다. 예를 들어, 이 키를 사용하여 웹사이트에서 AJAX 호출을 하거나 다른 공개적인 방식으로 노출하지 마십시오.
{% endalert %}

실수로 키가 노출된 경우 개발자 콘솔에서 키를 삭제할 수 있습니다. 이 프로세스에 대한 도움을 받으려면 [지원 티켓]({{site.baseurl}}/braze_support/)을 열어주세요.

### API IP 허용 목록

보안을 강화하기 위해 특정 REST API 키에 대해 REST API 요청을 보내도록 허용할 IP 주소와 서브넷 목록을 지정할 수 있습니다. 이를 허용 목록 또는 화이트리스트라고 합니다. 특정 IP 주소 또는 서브넷을 허용하려면 새 REST API 키를 생성할 때 **화이트리스트 IP** 섹션에 추가하세요.

![API 키를 생성할 때 IP를 허용 목록에 추가하는 옵션입니다.]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

지정하지 않으면 모든 IP 주소에서 요청을 보낼 수 있습니다.

{% alert tip %}
Braze-Braze 웹훅을 생성하고 허용 목록을 사용하려면? [화이트리스트에 추가할 IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting) 목록을 확인하세요.
{% endalert %}

## 추가 리소스

### 루비 클라이언트 라이브러리

루비를 사용하여 Braze를 구현하는 경우, 데이터 가져오기 시간을 줄이기 위해 [루비 클라이언트 라이브러리](https://github.com/braze-inc/braze-api-client-ruby)를 사용할 수 있습니다. 클라이언트 라이브러리는 특정 프로그래밍 언어, 이 경우에는 루비에 대한 코드 모음으로, API를 사용하는 것을 더 쉽게 만들어 줍니다.

루비 클라이언트 라이브러리는 [사용자 엔드포인트]({{site.baseurl}}/api/endpoints/user_data)을 지원합니다.

{% alert important %}
이 클라이언트 라이브러리는 현재 베타 버전입니다. 이 라이브러리를 개선하는 데 도움을 주고 싶으신가요? [smb-product@braze.com](mailto:smb-product@braze.com) 으로 피드백을 보내주세요.
{% endalert %}

