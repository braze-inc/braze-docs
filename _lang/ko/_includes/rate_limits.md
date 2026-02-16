<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "기본값" %}
[API 속도 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 이 엔드포인트에는 시간당 250,000건의 요청이라는 기본값의 Braze 속도 제한을 적용합니다.

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "대시보드 사용자 업데이트" %}
이 엔드포인트에는 회사당 하루에 5,000건의 요청이 제한되어 있습니다. 이 전송률 제한은 [API 전송률 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/scim/v2/Users/` GET, DELETE, POST 엔드포인트와 공유됩니다.

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "대시보드 사용자 조회하기" %}
이 엔드포인트에는 회사당 하루에 5,000건의 요청이 제한되어 있습니다. 이 전송률 제한은 [API 전송률 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/scim/v2/Users/` PUT, GET, DELETE 및 POST 엔드포인트와 공유됩니다.

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "대시보드 사용자 삭제" %}
이 엔드포인트에는 회사당 하루에 5,000건의 요청이 제한되어 있습니다. 이 전송률 제한은 [API 전송률 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/scim/v2/Users/` PUT, GET 및 POST 엔드포인트와 공유됩니다.

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "대시보드 사용자 만들기" %}
이 엔드포인트에는 회사당 하루에 5,000건의 요청이 제한되어 있습니다. 이 전송률 제한은 [API 전송률 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/scim/v2/Users/` PUT, GET, DELETE 엔드포인트와 공유됩니다.

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "대시보드 사용자 이메일 조회하기" %}
이 엔드포인트에는 회사당 하루에 5,000건의 요청이 제한되어 있습니다. 이 전송률 제한은 [API 전송률 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/scim/v2/Users/` PUT, GET, DELETE 및 POST 엔드포인트와 공유됩니다.

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "외부 ID 마이그레이션" %}
[API 속도 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 이 엔드포인트에는 분당 1,000건의 요청 속도 제한이 적용됩니다.

<!---/users/track-->

{% elsif include.endpoint == "사용자 추적" %}
2024년 10월 28일부터 모든 고객을 대상으로 이 엔드포인트에 3초당 3,000건의 기본 요청 속도 제한을 적용합니다. 각 `/users/track` 요청에는 최대 75개의 이벤트 개체, 75개의 속성 개체, 75개의 구매 개체가 포함될 수 있습니다. 각 오브젝트(이벤트, 속성, 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있습니다. 즉, 한 번의 통화로 최대 225명의 사용자를 업데이트할 수 있습니다. 또한 단일 고객 프로필을 여러 개체로 업데이트할 수 있습니다.

**월간 활성 사용자 - CY 24-25를** 구매한 고객에게는 다른 한도가 적용됩니다. 이러한 한도에 대한 자세한 내용은 [월간 활성 사용자 - CY 24-25 한도를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau) 참조하세요.

자세한 내용은 [API 요금 한도]({{site.baseurl}}/api/api_limits/) 페이지를 참조하고, 한도를 늘려야 하는 경우 고객 성공 매니저에게 문의하세요.

<!---/users/export/ids-->

{% elsif include.endpoint == "사용자 내보내기 ID" %}
2024년 8월 22일 이후에 Braze를 온보딩한 경우, 이 엔드포인트는 [API 속도 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 분당 250건의 요청으로 속도 제한이 적용됩니다.

또한 다음 요구 사항을 충족하여 이 엔드포인트의 속도 제한을 초당 40건의 요청으로 늘릴 수도 있습니다:

- 워크스페이스에 기본값(분당 250건의 요청)의 속도 제한이 인에이블먼트되어 있습니다. 기존 요금 제한을 해제하는 데 대한 자세한 내용은 Braze 계정 매니저에게 문의하세요.
- 요청에 `fields_to_export` 매개변수를 포함하면 수신하려는 모든 필드를 나열할 수 있습니다.

{% alert important %}
`fields_to_export` 매개변수에 `canvases_received` 또는 `campaigns_received` 을 포함하면 요청에 더 빠른 속도 제한이 적용되지 않습니다. 구체적인 사용 사례가 있는 경우에만 요청에 포함하는 것이 좋습니다.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "사용자 삭제" %}
이 엔드포인트에는 분당 20,000건의 요청 공유 속도 제한을 적용합니다. 이 요금 제한은 [API 요금 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/users/alias/new`, `/users/identify`, `/users/merge`, `/users/alias/update` 엔드포인트와 공유됩니다.

<!---/users/alias/new-->

{% elsif include.endpoint == "사용자 별칭 지정 신규" %}
이 엔드포인트에는 분당 20,000건의 요청 공유 속도 제한을 적용합니다. 이 요금 제한은 [API 요금 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/users/delete`, `/users/identify`, `/users/merge`, `/users/alias/update` 엔드포인트와 공유됩니다.

<!---/users/alias/update-->

{% elsif include.endpoint == "사용자 별칭 지정 업데이트" %}
이 엔드포인트에는 분당 20,000건의 요청 공유 속도 제한을 적용합니다. 이 요금 제한은 [API 요금 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/users/delete`, `/users/alias/new`, `/users/identify`, `/users/merge` 엔드포인트와 공유됩니다.

<!---/users/identify-->

{% elsif include.endpoint == "사용자 식별자" %}
이 엔드포인트에는 분당 20,000건의 요청 공유 속도 제한을 적용합니다. 이 요금 제한은 [API 요금 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/users/delete`, `/users/alias/new`, `/users/merge`, `/users/alias/update` 엔드포인트와 공유됩니다.

<!---/users/merge-->

{% elsif include.endpoint == "사용자 병합" %}
이 엔드포인트에는 분당 20,000건의 요청 공유 속도 제한을 적용합니다. 이 요금 제한은 [API 요금 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/users/delete`, `/users/alias/new`, `/users/identify`, `/users/alias/update` 엔드포인트와 공유됩니다.

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
이 엔드포인트에는 시간당 1,000건의 공유 속도 제한을 적용합니다. 이 요금 제한은 [API 요금 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/events`, `/events/list`, `/purchases/product_list` 엔드포인트와 공유됩니다.

<!---/events-->

{% elsif include.endpoint == "이벤트" %}
이 엔드포인트에는 시간당 1,000건의 공유 속도 제한을 적용합니다. 이 요금 제한은 [API 요금 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/custom_attributes`, `/events/list`, `/purchases/product_list` 엔드포인트와 공유됩니다.

<!---/events/list-->

{% elsif include.endpoint == "이벤트 목록" %}
이 엔드포인트에는 시간당 1,000건의 공유 속도 제한을 적용합니다. 이 요금 제한은 [API 요금 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/custom_attributes`, `/events`, `/purchases/product_list` 엔드포인트와 공유됩니다.

<!---/purchases/product_list-->

{% elsif include.endpoint == "구매 제품 목록" %}
이 엔드포인트에는 시간당 1,000건의 공유 속도 제한을 적용합니다. 이 요금 제한은 [API 요금 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/custom_attributes`, `/events`, `/events/list` 엔드포인트와 공유됩니다.

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "엔드포인트 보내기" %}
요청에 커넥티드 오디언스 필터를 사용하는 경우, 이 엔드포인트에는 분당 250건의 요청 속도 제한이 적용됩니다. 그렇지 않으면 `external_id` 을 지정하는 경우 이 엔드포인트의 기본값은 [API 속도 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/messages/send`, `/campaigns/trigger/send`, `/canvas/trigger/send` 간에 공유되는 시간당 250,000건의 요청으로 제한됩니다.

Braze 엔드포인트는 API 요청 일괄 처리를 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`, 각각 개별 메시지 매개변수 포함
- 요청에 연결된 오디언스 개체로 정의된 모든 규모의 오디언스 세그먼트입니다.

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "트랜잭션 이메일" %}
`/transactional/v1/campaigns/{campaign_id}/send` 엔드포인트는 시간당 단위(예: 패키지에 따라 시간당 50,000)로 유료로 제공되는 엔드포인트입니다. 엔드포인트당 별도의 요금 제한은 없습니다. 할당된 용량을 초과하여 전송할 수 있지만 할당된 용량에 대해서만 SLA가 적용됩니다. 이 엔드포인트에 대한 요청은 [전체 외부 API 요금 한도에]({{site.baseurl}}/api/api_limits/) 포함됩니다. 이 제한을 초과하면(예: 모든 엔드포인트에서 시간당 250,000건의 요청) Braze는 429를 반환하고 요청이 스로틀링됩니다. 트랜잭션 수량은 1시간마다 초기화되므로 1시간이 지나면 다른 할당을 사용할 수 있습니다. SLA가 적용되는 이메일 발송량 내에서 99.9%의 이메일이 1분 이내에 전송됩니다.

<!---/sends/id/create-->

{% elsif include.endpoint == "SEND ID CREATE" %}
주어진 워크스페이스에 대해 이 엔드포인트를 사용하여 하루에 최대 100개의 커스텀 전송 식별자를 만들 수 있습니다. `send_id` 및 `campaign_id` 조합을 생성할 때마다 일일 한도에 포함됩니다. 유효한 요청에 대한 응답 헤더에는 현재 요금 제한 상태가 포함됩니다. 자세한 내용은 [API 요금 한도를]({{site.baseurl}}/api/api_limits/) 참조하세요.

<!---/subscription/status/set-->
{% elsif include.endpoint == "구독 상태 설정" %}
이 엔드포인트는 [API 속도 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 `/subscription/status/set` 및 `/v2/subscription/status/set` 엔드포인트에서 공유되는 분당 5,000건의 요청으로 속도 제한이 설정되어 있습니다.

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "CDI 목록 통합" %}
이 엔드포인트는 분당 50건의 요청으로 속도 제한이 있습니다.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "CDI 작업 동기화" %}
이 엔드포인트는 분당 20건의 요청으로 속도 제한이 있습니다.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "CDI 작업 동기화 상태" %}
이 엔드포인트는 분당 100건의 요청으로 속도 제한이 있습니다.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "메시지 엔드포인트" %}

Braze 엔드포인트는 [API 요청 일괄 처리를]({{site.baseurl}}/api/api_limits/#batching-api-requests) 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`, 각각 개별 메시지 매개변수 포함
- Braze 대시보드에서 생성된 임의의 크기의 세그먼트로, 해당 세그먼트의 `segment_id`
- 요청에 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 개체로 정의된 모든 규모의 오디언스 세그먼트입니다.

{% endif %}

{% if include.category == "메시지 엔드포인트 보내기" %}

Braze 엔드포인트는 [API 요청 일괄 처리를]({{site.baseurl}}/api/api_limits/#batching-api-requests) 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`, 각각 개별 메시지 매개변수 포함
- 요청에 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 개체로 정의된 모든 규모의 오디언스 세그먼트입니다.

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "번역 엔드포인트" %}

이 엔드포인트의 속도 제한은 분당 250,000건의 요청입니다.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "메시지 전송 엔드포인트" %}

Braze 엔드포인트는 [API 요청 일괄 처리를]({{site.baseurl}}/api/api_limits/#batching-api-requests) 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`
- Braze 대시보드에서 생성된 임의의 크기의 세그먼트로, 해당 세그먼트의 `segment_id`
- 요청에 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 개체로 정의된 모든 규모의 오디언스 세그먼트입니다.

{% endif %}

{% if include.endpoint == "비동기 카탈로그 항목" %}

이 엔드포인트는 [API 속도 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 모든 비동기 카탈로그 항목 엔드포인트 간에 분당 16,000건의 요청이 공유 속도 제한으로 설정되어 있습니다.

{% endif %}

{% if include.endpoint == "동기식 카탈로그 항목" %}

이 엔드포인트에는 [API 속도 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 모든 동기식 카탈로그 항목 엔드포인트 간에 분당 50건의 요청이 공유 속도 제한으로 설정되어 있습니다.

{% endif %}

{% if include.endpoint == "동기식 카탈로그" %}

이 엔드포인트에는 [API 속도 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 모든 동기식 카탈로그 엔드포인트 간에 분당 50건의 요청이 공유 속도 제한이 있습니다.

{% endif %}

{% if include.endpoint == "비동기 카탈로그 필드" 또는 포함.엔드포인트 == "비동기 카탈로그 선택 항목" %}

이 엔드포인트에는 [API 속도 제한에]({{site.baseurl}}/api/api_limits/) 설명된 대로 모든 비동기 카탈로그 필드와 선택 엔드포인트 간에 분당 50건의 요청 공유 속도 제한이 있습니다.

{% endif %}

{% if include.endpoint == "캠페인 분석 내보내기" %}

이 엔드포인트의 속도 제한은 분당 50,000건의 요청입니다.

{% endif %}
