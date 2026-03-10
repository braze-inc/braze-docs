<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
[API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 이 엔드포인트에는 시간당 250,000건의 요청이라는 기본 Braze 사용량 제한을 적용합니다.

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
이 엔드포인트에는 회사당 하루 5,000건의 요청 제한이 있습니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/scim/v2/Users/` GET, DELETE, POST 엔드포인트와 공유됩니다.

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
이 엔드포인트에는 회사당 하루 5,000건의 요청 제한이 있습니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/scim/v2/Users/` PUT, GET, DELETE 및 POST 엔드포인트와 공유됩니다.

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
이 엔드포인트에는 회사당 하루 5,000건의 요청 제한이 있습니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/scim/v2/Users/` PUT, GET 및 POST 엔드포인트와 공유됩니다.

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
이 엔드포인트에는 회사당 하루 5,000건의 요청 제한이 있습니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/scim/v2/Users/` PUT, GET, DELETE 엔드포인트와 공유됩니다.

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
이 엔드포인트에는 회사당 하루 5,000건의 요청 제한이 있습니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/scim/v2/Users/` PUT, GET, DELETE 및 POST 엔드포인트와 공유됩니다.

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
[API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 이 엔드포인트에는 분당 1,000건의 요청 사용량 제한이 적용됩니다.

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
2024년 10월 28일부터 모든 고객을 대상으로 이 엔드포인트에 3초당 3,000건의 기본 속도 제한을 적용합니다. 각 `/users/track` 요청에는 최대 75개의 이벤트 오브젝트, 75개의 속성 오브젝트, 75개의 구매 오브젝트가 포함될 수 있습니다. 각 오브젝트(이벤트, 속성, 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있습니다. 즉, 한 번의 호출로 최대 225명의 사용자를 업데이트할 수 있습니다. 또한 단일 고객 프로필을 여러 오브젝트로 업데이트할 수 있습니다.

**월간 활성 사용자 - CY 24-25**를 구매한 고객에게는 다른 한도가 적용됩니다. 이러한 한도에 대한 자세한 내용은 [월간 활성 사용자 - CY 24-25 한도]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau)를 참조하세요.

자세한 내용은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/) 페이지를 참조하고, 한도를 늘려야 하는 경우 고객 성공 매니저에게 문의하세요.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
2024년 8월 22일 이후에 Braze를 온보딩한 경우, 이 엔드포인트는 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 분당 250건의 요청으로 사용량 제한이 적용됩니다.

또한 다음 요구 사항을 충족하면 이 엔드포인트의 사용량 제한을 초당 40건의 요청으로 늘릴 수 있습니다:

- 워크스페이스에 기본 사용량 제한(분당 250건의 요청)이 활성화되어 있어야 합니다. 기존 사용량 제한 해제에 대한 추가 지원은 Braze 계정 매니저에게 문의하세요.
- 요청에 `fields_to_export` 매개변수를 포함하여 수신하려는 모든 필드를 나열해야 합니다.

{% alert important %}
`fields_to_export` 매개변수에 `canvases_received` 또는 `campaigns_received`를 포함하면 더 빠른 사용량 제한이 적용되지 않습니다. 구체적인 사용 사례가 있는 경우에만 요청에 포함하는 것이 좋습니다.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
이 엔드포인트에는 분당 20,000건의 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/users/alias/new`, `/users/identify`, `/users/merge`, `/users/alias/update` 엔드포인트와 공유됩니다.

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
이 엔드포인트에는 분당 20,000건의 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/users/delete`, `/users/identify`, `/users/merge`, `/users/alias/update` 엔드포인트와 공유됩니다.

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
이 엔드포인트에는 분당 20,000건의 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/users/delete`, `/users/alias/new`, `/users/identify`, `/users/merge` 엔드포인트와 공유됩니다.

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
이 엔드포인트에는 분당 20,000건의 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/users/delete`, `/users/alias/new`, `/users/merge`, `/users/alias/update` 엔드포인트와 공유됩니다.

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
이 엔드포인트에는 분당 20,000건의 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/users/delete`, `/users/alias/new`, `/users/identify`, `/users/alias/update` 엔드포인트와 공유됩니다.

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
이 엔드포인트에는 시간당 1,000건의 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/events`, `/events/list`, `/purchases/product_list` 엔드포인트와 공유됩니다.

<!---/events-->

{% elsif include.endpoint == "events" %}
이 엔드포인트에는 시간당 1,000건의 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/custom_attributes`, `/events/list`, `/purchases/product_list` 엔드포인트와 공유됩니다.

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
이 엔드포인트에는 시간당 1,000건의 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/custom_attributes`, `/events`, `/purchases/product_list` 엔드포인트와 공유됩니다.

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
이 엔드포인트에는 시간당 1,000건의 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/custom_attributes`, `/events`, `/events/list` 엔드포인트와 공유됩니다.

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
요청에 커넥티드 오디언스 필터를 사용하는 경우, 이 엔드포인트에는 분당 250건의 요청 사용량 제한이 적용됩니다. 그렇지 않고 `external_id`를 지정하는 경우, 이 엔드포인트의 기본 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/messages/send`, `/campaigns/trigger/send`, `/canvas/trigger/send` 간에 공유되는 시간당 250,000건의 요청입니다.

Braze 엔드포인트는 API 요청 일괄 처리를 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`, 각각 개별 메시지 매개변수 포함
- 요청에 커넥티드 오디언스 오브젝트로 정의된 모든 규모의 오디언스 세그먼트

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
`/transactional/v1/campaigns/{campaign_id}/send` 엔드포인트는 시간당 단위(예: 패키지에 따라 시간당 50,000)로 유료 제공되는 엔드포인트입니다. 엔드포인트당 별도의 사용량 제한은 없습니다. 할당된 용량을 초과하여 전송할 수 있지만 할당된 용량에 대해서만 SLA가 적용됩니다. 이 엔드포인트에 대한 요청은 [전체 외부 API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 포함됩니다. 이 제한을 초과하면(예: 모든 엔드포인트에서 시간당 250,000건의 요청) Braze는 429를 반환하고 요청이 스로틀링됩니다. 트랜잭션 발송량은 1시간마다 초기화되므로 1시간이 지나면 새로운 할당량을 사용할 수 있습니다. SLA가 적용되는 발송량 내에서 99.9%의 이메일이 1분 이내에 전송됩니다.

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
주어진 워크스페이스에 대해 이 엔드포인트를 사용하여 하루에 최대 100개의 커스텀 전송 식별자를 만들 수 있습니다. `send_id` 및 `campaign_id` 조합을 생성할 때마다 일일 한도에 포함됩니다. 유효한 요청에 대한 응답 헤더에는 현재 사용량 제한 상태가 포함됩니다. 자세한 내용은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)을 참조하세요.

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
이 엔드포인트는 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 `/subscription/status/set` 및 `/v2/subscription/status/set` 엔드포인트에서 공유되는 분당 5,000건의 요청으로 사용량 제한이 설정되어 있습니다.

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
이 엔드포인트는 분당 50건의 요청으로 사용량 제한이 있습니다.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
이 엔드포인트는 분당 20건의 요청으로 사용량 제한이 있습니다.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
이 엔드포인트는 분당 100건의 요청으로 사용량 제한이 있습니다.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Braze 엔드포인트는 [API 요청 일괄 처리]({{site.baseurl}}/api/api_limits/#batching-api-requests)를 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`, 각각 개별 메시지 매개변수 포함
- Braze 대시보드에서 생성된 모든 규모의 세그먼트, `segment_id`로 지정
- 요청에 [커넥티드 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 오브젝트로 정의된 모든 규모의 오디언스 세그먼트

{% endif %}

{% if include.category == "send messages endpoints" %}

Braze 엔드포인트는 [API 요청 일괄 처리]({{site.baseurl}}/api/api_limits/#batching-api-requests)를 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`, 각각 개별 메시지 매개변수 포함
- 요청에 [커넥티드 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 오브젝트로 정의된 모든 규모의 오디언스 세그먼트

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

이 엔드포인트의 사용량 제한은 분당 250,000건의 요청입니다.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Braze 엔드포인트는 [API 요청 일괄 처리]({{site.baseurl}}/api/api_limits/#batching-api-requests)를 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`
- Braze 대시보드에서 생성된 모든 규모의 세그먼트, `segment_id`로 지정
- 요청에 [커넥티드 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 오브젝트로 정의된 모든 규모의 오디언스 세그먼트

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

이 엔드포인트는 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 모든 비동기 카탈로그 항목 엔드포인트 간에 분당 16,000건의 공유 사용량 제한이 있습니다.

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

이 엔드포인트는 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 모든 동기식 카탈로그 항목 엔드포인트 간에 분당 50건의 공유 사용량 제한이 있습니다.

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

이 엔드포인트는 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 모든 동기식 카탈로그 엔드포인트 간에 분당 50건의 공유 사용량 제한이 있습니다.

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

이 엔드포인트는 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에 설명된 대로 모든 비동기 카탈로그 필드 및 선택 엔드포인트 간에 분당 50건의 공유 사용량 제한이 있습니다.

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

이 엔드포인트의 사용량 제한은 분당 50,000건의 요청입니다.

{% endif %}