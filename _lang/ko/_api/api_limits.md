---
nav_title: 요율 제한
article_title: API 사용량 제한
page_order: 4.5
description: "이 참조 문서에서는 Braze API 인프라의 API 사용량 제한을 다룹니다."
page_type: reference

---

# 요율 제한

> Braze API 인프라는 고객 기반 전체에서 대량의 데이터를 처리하도록 설계되었습니다. 이를 위해 워크스페이스당 API 사용량 제한을 적용합니다. 

사용량 제한은 지정된 기간 동안 API가 수신할 수 있는 요청 수입니다. 대규모 시스템에서 발생하는 로드 기반 서비스 거부 사고는 대부분 소프트웨어 또는 구성 오류로 인해 발생하는 의도치 않은 것이지 악의적인 공격이 아닙니다. 사용량 제한은 이러한 오류로 인해 고객의 Braze API 리소스가 박탈되지 않는지 확인합니다. 지정된 기간 동안 너무 많은 요청이 전송되면 사용량 제한에 도달했음을 나타내는 `429` 상태 코드가 로 표시된 오류 응답이 표시될 수 있습니다.

{% alert warning %}
API 사용량 제한은 시스템의 적절한 사용에 따라 변경될 수 있습니다. API 호출을 할 때는 피해나 오용을 방지하기 위해 합리적인 제한을 두는 것이 좋습니다.
{% endalert %}

## 요청 유형별 사용량 제한

다음 표에는 다양한 요청 유형에 대한 기본 API 사용량 제한이 나와 있습니다. 이러한 기본 한도는 요청 시 늘릴 수 있습니다. 자세한 내용은 고객 성공 관리자에게 문의하세요.

{% alert note %}
이 표에 나열되지 않은 요청은 시간당 총 250,000개 요청의 기본 사용량 제한을 공유합니다.
{% endalert %}

| 요청 유형 | 기본 API 속도 제한 |
| --- | --- |
| [`/users/track`][10]| **요청:** 분당 요청 50,000건<br><br>**일괄 처리:** API 요청당 이벤트 75개, 구매 75개, 속성 75개 자세한 내용은 [사용자 추적 요청 일괄 처리](#batch-user-track)를 참조하세요. |
| [`/users/export/ids`][11] | 분당 2,500개의 요청|
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44] | 분당 20,000개의 요청, 엔드포인트 간에 공유. |
| [`/users/external_id/rename`][20]| 분당 1,000건의 요청.|
| [`/users/external_id/remove`][21]| 분당 1,000건의 요청.|
| [`/events/list`][15] | 시간당 1,000개의 요청이 `/purchases/product_list` 엔드포인트와 공유됩니다. |
| [`/purchases/product_list`][16] | 시간당 1,000개의 요청이 `/events/list` 엔드포인트와 공유됩니다. |
| [`/campaigns/data_series`][17.3]| 분당 요청 5만 건|
| [`/messages/send`][17] | 브로드캐스트 통화에 대한 분당 250개의 요청 (세그먼트 또는 연결된 오디언스만 지정하는 경우). 그렇지 않으면 시간당 요청은 250,000건입니다. |
| [`/campaigns/trigger/send`][17.1] | 브로드캐스트 통화에 대한 분당 250개의 요청 (세그먼트 또는 연결된 오디언스만 지정하는 경우). 그렇지 않으면 시간당 요청은 250,000건입니다. |
| [`/canvas/trigger/send`][17.2] | 브로드캐스트 통화에 대한 분당 250개의 요청 (세그먼트 또는 연결된 오디언스만 지정하는 경우). 그렇지 않으면 시간당 요청은 250,000건입니다. |
| [`/sends/id/create`][18]| 하루에 100건의 요청.|
| [`/subscription/status/set`][19]| 분당 5,000건의 요청|
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28] | 워크스페이스당 분당 요청 1,000개. |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30] | 워크스페이스당 분당 요청 10개. |
| [`/catalogs/{catalog_name}`][31]<br>[`/catalogs`][32]<br>[`/catalogs`][33] | 엔드포인트 간에 분당 50건의 요청이 공유됩니다. |
| [`/catalogs/{catalog_name}/items`][34]<br>[`/catalogs/{catalog_name}/items`][35]<br>[`/catalogs/{catalog_name}/items`][36] | 엔드포인트 간에 분당 16,000개의 요청이 공유됩니다. |
| [`/catalogs/{catalog_name}/items/{item_id}`][37]<br>[`/catalogs/{catalog_name}/items/{item_id}`][38]<br>[`/catalogs/{catalog_name}/items`][39]<br>[`/catalogs/{catalog_name}/items/{item_id}`][40]<br>[`/catalogs/{catalog_name}/items/{item_id}`][41] | 엔드포인트 간에 분당 50건의 요청이 공유됩니다. |
| [`/scim/v2/Users/{id}`][22]<br>[`/scim/v2/Users?filter={userName@example.com}`][43]<br>[`/scim/v2/Users/{id}`][25]<br>[`/scim/v2/Users/{id}}`][24]<br>[`/scim/v2/Users/`][23] | 기업당 하루 5,000건의 요청이 엔드포인트 간에 공유됩니다. |
{: .reset-td-br-1 .reset-td-br-2}

<!-- Add during CDI endpoints GA
| [`/cdi/integrations`][46] | 50 requests per minute. |
| [`/cdi/integrations/{integration_id}/sync`][47] | 20 requests per minute. |
| [`/cdi/integrations/{integration_id}/job_sync_status`][48] | 100 requests per minute. |
-->

## API 요청 일괄 처리

Braze API는 일괄 처리를 지원하도록 구축되었습니다. Braze는 일괄 처리를 통해 단일 API 호출로 최대한 많은 데이터를 가져올 수 있으므로 많은 API 호출을 할 필요가 없습니다. Braze는 한 번에 하나씩 데이터를 처리하는 것보다 일괄적으로 처리하는 것이 더 효율적입니다. 예를 들어 1,000건의 일괄 처리된 API 호출을 처리하는 것은 개별 호출 75,000건을 처리하는 것보다 적은 리소스를 필요로 합니다. 일괄 처리는 시간당 75,000회 이상의 호출이 필요할 수 있는 모든 애플리케이션에서 매우 중요합니다.

{% alert note %}
REST API 사용량 제한 상승은 API 일괄 처리 기능을 사용하는 고객의 필요에 따라 고려됩니다.
{% endalert %}

### 사용자 추적 요청 일괄 처리 {#batch-user-track}

각 `/users/track` 요청에는 최대 75개의 이벤트 객체, 75개의 속성 객체 및 75개의 구매 객체가 포함될 수 있습니다. 각 객체(이벤트, 속성 및 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있습니다. 따라서 한 번의 통화로 최대 225명의 사용자를 업데이트할 수 있습니다. 또한 단일 고객 프로필을 여러 객체로 업데이트할 수 있습니다.

이 엔드포인트에 대한 요청은 일반적으로 다음 순서로 처리를 시작합니다. 

1. 속성
2. 이벤트
3. 구매

### 메시징 엔드포인트 요청 일괄 처리

[메시징 엔드포인트][1]에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다.

- 각각 개별 메시지 매개 변수가 있는 최대 50개의 특정 `external_ids`
- Braze 대시보드에서 생성된 모든 크기의 세그먼트로, `segment_id`로 지정됩니다
- 요청에 [연결된 오디언스][2] 객체로 정의된 모든 규모의 추가 오디언스 필터와 일치하는 사용자

### 배치 요청 예시

다음 예시에서는 이메일과 SMS에 대해 하나의 API 호출을 만드는 데 `external_id` 사용합니다.

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

헤더 이름 | 설명
----------------------- | -----------------------
`X-RateLimit-Limit`     | 지정된 기간 동안 수행할 수 있는 최대 요청 수 (사용량 제한).
`X-RateLimit-Remaining` | 현재 사용량 제한 창에 남아 있는 요청 수입니다.
`X-RateLimit-Reset`     | 현재 사용량 제한 창이 재설정되는 시간 (UTC 에포크 초)입니다.
{: .reset-td-br-1 .reset-td-br-2}

이 정보는 Braze 대시보드가 아닌 API 요청에 대한 응답의 헤더에 의도적으로 포함됩니다. 이를 통해 API와 상호 작용할 때 시스템이 실시간으로 더 잘 반응할 수 있습니다. 예를 들어 `X-RateLimit-Remaining` 값이 특정 임계값 아래로 떨어지면 모든 트랜잭션 이메일이 전송되도록 전송 사용량를 늦추는 것이 좋습니다. 또는 0에 도달하면 `X-RateLimit-Reset`에 지정된 시간이 경과할 때까지 모든 전송을 일시 중지하는 것이 좋습니다.

API 한도에 대해 궁금한 점이 있으면 고객 성공 매니저에게 문의하거나 [지원 티켓][support]을 개설하세요.

### 엔드포인트 간 최적 지연

{% alert note %}
오류를 최소화하려면 연속적인 엔드포인트 호출 사이에 5분의 지연을 허용하는 것이 좋습니다.
{% endalert %}

Braze API를 연속으로 호출할 때는 엔드포인트 간의 최적 지연을 이해하는 것이 중요합니다. 엔드포인트가 다른 엔드포인트의 성공적인 처리에 의존하는 경우 문제가 발생하며, 너무 빨리 호출되면 오류가 발생할 수 있습니다. 예를 들어 `/user/alias/new` 엔드포인트를 통해 사용자에게 별칭을 할당한 다음 해당 별칭에 도달하여 엔드포인트를 통해 `/users/track` 커스텀 이벤트를 보내는 경우 얼마나 기다려야 할까요?

정상적인 조건에서 데이터의 최종 일관성이 발생하는 데 걸리는 시간은 10~100ms(1/10초)입니다. 하지만 이러한 일관성이 유지되는 데 시간이 더 오래 걸리는 경우도 있으므로 오류 가능성을 최소화하기 위해 후속 호출 사이에 5분의 지연을 허용하는 것이 좋습니다.

[1]: {{site.baseurl}}/api/endpoints/messaging/
[2]: {{site.baseurl}}/api/objects_filters/connected_audience/
[support]: {{site.baseurl}}/braze_support/
[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_delete/
[13]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[14]: {{site.baseurl}}/api/endpoints/user_data/post_user_identify/
[15]: {{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/
[16]: {{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/
[17]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[17.1]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[17.2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[17.3]: {{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/
[18]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/
[19]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[20]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
[21]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
[22]: {{site.baseurl}}/get_see_user_account_information/
[23]: {{site.baseurl}}/post_create_user_account/
[24]: {{site.baseurl}}/delete_existing_dashboard_user/
[25]: {{site.baseurl}}/post_update_existing_user_account/
[26]: {{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/
[27]: {{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/
[28]: {{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/
[29]: {{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/
[30]: {{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/
[31]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/
[32]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/
[33]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/
[34]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/
[35]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/
[36]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/
[37]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/
[38]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/
[39]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/
[40]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/
[41]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/
[43]: {{site.baseurl}}/get_search_existing_dashboard_user_email/
[44]: {{site.baseurl}}/api/endpoints/user_data/post_users_merge/
[45]: {{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/
[46]: {{site.baseurl}}/api/endpoints/cdi/get_integration_list/
[47]: {{site.baseurl}}/api/endpoints/cdi/job_sync/
[48]: {{site.baseurl}}/api/endpoints/cdi/job_sync_status/
