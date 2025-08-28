---
nav_title: 요금 한도
article_title: API 속도 제한
page_order: 4.5
description: "이 참조 문서는 Braze API 인프라에 대한 API 속도 제한을 다룹니다."
page_type: reference

---

# 요금 제한

> 브레이즈 API 인프라는 고객 기반의 대량 데이터를 처리하도록 설계되었습니다. 이를 위해 우리는 작업 공간별로 API 속도 제한을 시행합니다.

요금 제한은 API가 주어진 시간 동안 수신할 수 있는 요청의 수입니다. 대규모 시스템에서 발생하는 부하 기반 서비스 거부 사고의 대부분은 악의적인 공격이 아닌 소프트웨어 또는 구성 오류로 인해 의도하지 않게 발생합니다. 요금 제한은 이러한 오류가 고객의 Braze API 리소스를 빼앗지 않도록 확인합니다. 지정된 시간 프레임 내에 너무 많은 요청이 전송되면, `429`의 상태 코드와 함께 오류 응답이 표시될 수 있으며, 이는 속도 제한이 초과되었음을 나타냅니다.

{% alert warning %}
API 사용량에 따라 API 속도 제한이 변경될 수 있습니다. 손상이나 오용을 방지하기 위해 API 호출 시 합리적인 제한을 두는 것이 좋습니다.
{% endalert %}

## 요청 유형별 속도 제한

다음은 다양한 요청 유형의 기본 API 속도 제한을 참조하십시오. 이러한 기본 한도는 요청에 따라 늘릴 수 있습니다. 자세한 내용은 고객 성공 관리자에게 문의하세요.

### 속도 제한이 다른 요청

| 요청 유형                                                                                                                                                                                                                                           | 기본 API 요금 한도                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                                                                                                                                                                                                                   | **요청:** 3,000 요청이 3초마다 발생합니다.<br><br>**배치 처리:** API 요청당 이벤트 75개, 구매 75개, 속성 75개 자세한 내용은 [사용자 추적 요청 일괄 처리를](#batch-user-track) 참조하세요.<br><br>**2024-2025년 월간 활성 사용자 한도:** [2024-2025년 월간 활성 사용자 한도]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25) |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                                                                                                                                                                                                                              | **2024년 8월 22일 또는 그 이후에 온보딩한 경우:** 1분에 250개의 요청. <br><br> **2024년 8월 22일 이전에 온보딩한 경우:** 분당 2,500건의 요청이 발생합니다.                                                                                                                                                                                                                               |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)                                                                                                                    | 분당 20,000건의 요청이 엔드포인트 간에 공유됩니다.                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)                                                                                                                                                                                                                      | 분당 1,000건의 요청.                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/)                                                                                                                                                                                                                      | 분당 1,000건의 요청.                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/)                                                                                                                                                                                                                                   | 시간당 1,000건의 요청이 `/purchases/product_list` 엔드포인트와 공유됩니다.                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)                                                                                                                                                                                                                        | 시간당 1,000건의 요청이 `/events/list` 엔드포인트와 공유됩니다.                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                                                                                                                                                                                                                       | 분당 요청 50,000건                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)                                                                                                                                                          | 브로드캐스트 통화의 경우 분당 250건의 요청(세그먼트 또는 연결된 오디언스만 지정한 경우). 그렇지 않으면 엔드포인트 간에 시간당 250,000건의 요청이 공유됩니다.                                                                                                                                                                                                                    |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)                                                                                                                                                                                                                               | 하루 100건의 요청.                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)                                                                                                                                                                                                                       | 분당 5,000건의 요청.                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)                                                                            | 분당 1,000건의 요청.                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)                                                                                                                                                            | 분당 10개의 요청.                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)                                                                                                                                                                             | 엔드포인트 간에 분당 50건의 요청이 공유됩니다.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/)                                                                                                                             | 분당 16,000건의 요청이 엔드포인트 간에 공유됩니다.                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 엔드포인트 간에 분당 50건의 요청이 공유됩니다.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 엔드포인트 간에 분당 50건의 요청이 공유됩니다. |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information/)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email/)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account/)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user/)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account/)                                                                          | 회사당 하루 5,000건의 요청이 엔드포인트 간에 공유됩니다.                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)                                                                                                                                                                                                                              | 분당 50개의 요청.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)                                                                                                                                                                                                        | 분당 20개의 요청.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/)                                                                                                                                                                                             | 분당 100개의 요청.                                                                                                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 공유 속도 제한이 있는 요청

다음 요청은 시간당 250,000개의 요청의 속도 제한이 있으며, 이들 간에 공유됩니다.

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key/)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/)
- [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/)
- [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/)
- [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)
- [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)
- [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)
- [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/)
- [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/)
- [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/)
- [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/)
- [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)
- [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/)
- [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
- [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/)
- [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)
- [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)

## API 요청 일괄 처리

Braze API는 일괄 처리를 지원하도록 구축되었습니다. 배치 처리를 통해 Braze는 단일 API 호출에서 가능한 한 많은 데이터를 수집할 수 있으므로 많은 API 호출을 할 필요가 없습니다. 브레이즈가 데이터를 한 번에 하나씩 처리하는 것보다 배치로 처리하는 것이 더 효율적입니다. 예를 들어, 1,000개의 배치된 API 호출을 처리하는 데는 75,000개의 개별 호출을 처리하는 것보다 적은 리소스가 필요합니다. 배치 처리는 시간당 75,000회 이상의 호출이 필요할 수 있는 모든 애플리케이션에 대해 매우 중요합니다.

{% alert note %}
REST API 속도 제한 증가가 API 배치 기능을 사용하는 고객의 필요에 따라 고려됩니다.
{% endalert %}

### Track 사용자 엔드포인트에 대한 요청 배치 {#batch-user-track}

각 `/users/track` 요청은 최대 75개의 이벤트 객체, 75개의 속성 객체 및 75개의 구매 객체를 포함할 수 있습니다. 각 개체(이벤트, 속성 및 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있습니다. 총 225명의 사용자가 한 번의 호출로 업데이트될 수 있음을 의미합니다. 또한, 단일 고객 프로필은 여러 객체에 의해 업데이트될 수 있습니다.

이 엔드포인트에 대한 요청은 일반적으로 이 순서대로 처리가 시작됩니다:

1. 속성
2. 이벤트
3. 구매

### 배치 메시징 엔드포인트 요청

단일 요청은 [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/) 중 하나에 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`, 각각 개별 메시지 매개변수를 가지고 있습니다.
- Braze 대시보드에서 생성된 크기와 관계없이 세그먼트, `segment_id`에 의해 지정됨.
- 요청에서 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 객체로 정의된 크기의 추가 오디언스 필터와 일치하는 사용자

### 일괄 요청 예시

다음 예제에서는 `external_id`를 사용하여 이메일과 SMS에 대해 하나의 API 호출을 수행합니다.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## 사용량 제한 모니터링

Braze로 전송된 모든 단일 API 요청은 응답 헤더에 다음 정보를 반환합니다.

| 헤더 이름             | 설명                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | 지정된 간격으로 요청할 수 있는 최대 요청 수(비율 제한)입니다. |
| `X-RateLimit-Remaining` | 현재 속도 제한 창에 남은 요청 수입니다.                          |
| `X-RateLimit-Reset`     | 현재 속도 제한 창이 재설정되는 시간(UTC 에포크 초)입니다.                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이 정보는 Braze 대시보드가 아닌 API 요청의 응답 헤더에 의도적으로 포함됩니다. 이것은 귀하의 시스템이 우리 API와 상호 작용할 때 실시간으로 더 잘 반응할 수 있도록 합니다. 예를 들어, `X-RateLimit-Remaining` 값이 특정 임계값 이하로 떨어지면 모든 거래 이메일이 발송되도록 보내는 속도를 늦추고 싶을 수 있습니다. 또는, 만약 그것이 0에 도달하면, `X-RateLimit-Reset`에 지정된 시간이 경과할 때까지 모든 전송을 일시 중지하고 싶을 수 있습니다.

{% alert note %}
HTTP 헤더는 모두 소문자로 반환됩니다. 이 행동은 모든 헤더 필드 이름이 소문자여야 한다고 규정한 HTTP/2 프로토콜과 일치합니다. 이것은 HTTP/1.X와 다릅니다. HTTP/1.X에서는 헤더 이름이 대소문자를 구분하지 않았지만 일반적으로 다양한 대문자 형태로 작성되었습니다.
{% endalert %}

API 한도에 대한 질문이 있는 경우 고객 성공 매니저에게 문의하거나 [지원 티켓]({{site.baseurl}}/braze_support/)을 열어주세요.

{% alert tip %}
[API 사용 대시보드]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/)를 사용하여 들어오는 트래픽을 속도 제한과 비교하여 볼 수 있습니다.
{% endalert %}

### 엔드포인트 간 최적의 지연

{% alert note %}
연속적인 엔드포인트 호출 사이에 5분의 지연을 두어 오류를 최소화할 것을 권장합니다.
{% endalert %}

엔드포인트 간의 최적 지연 시간을 이해하는 것은 Braze API에 연속 호출을 할 때 매우 중요합니다. 엔드포인트가 다른 엔드포인트의 성공적인 처리에 의존하는 경우 문제가 발생하며, 너무 빨리 호출되면 오류가 발생할 수 있습니다. 예를 들어 `/user/alias/new` 엔드포인트를 통해 사용자에게 별칭을 할당하고 해당 별칭을 눌러 `/users/track` 엔드포인트를 통해 사용자 지정 이벤트를 전송하는 경우 얼마나 기다려야 할까요?

정상적인 조건에서 데이터의 최종 일관성이 발생하는 데 걸리는 시간은 10~100ms(1/10초)입니다. 그러나 일관성이 발생하는 데 더 오랜 시간이 걸리는 경우가 있을 수 있으므로, 오류 확률을 최소화하기 위해 후속 호출 사이에 5분의 지연을 두는 것이 좋습니다.

