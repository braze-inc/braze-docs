<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
이 엔드포인트에는 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 명시된 대로 기본값 Braze 속도 제한인 시간당 250,000개의 요청이 적용됩니다.

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
이 엔드포인트는 회사당 일일 5000건의 요청 제한이 적용됩니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 GET, DELETE 및 `/scim/v2/Users/`POST 엔드포인트와 공유됩니다.

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
이 엔드포인트는 회사당 일일 5000건의 요청 제한이 적용됩니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 PUT, GET, DELETE`/scim/v2/Users/` 및 POST 엔드포인트와 공유됩니다.

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
이 엔드포인트는 회사당 일일 5000건의 요청 제한이 적용됩니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 PUT, GET 및 POST`/scim/v2/Users/` 엔드포인트와 공유됩니다.

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
이 엔드포인트는 회사당 일일 5000건의 요청 제한이 적용됩니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 PUT, GET 및 `/scim/v2/Users/`DELETE 엔드포인트와 공유됩니다.

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
이 엔드포인트는 회사당 일일 5000건의 요청 제한이 적용됩니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 PUT, GET, DELETE`/scim/v2/Users/` 및 POST 엔드포인트와 공유됩니다.

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
이 엔드포인트에는 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 명시된 대로 분당 1,000개의 요청에 대한 속도 제한을 적용합니다.

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
2024년 10월 28일부터, 모든 고객을 대상으로 이 엔드포인트에 대해 초당 3,000개의 요청이라는 기본 속도 제한을 적용합니다. 각 `/users/track` 요청은 최대 75개의 이벤트 객체, 75개의 속성 객체 및 75개의 구매 객체를 포함할 수 있습니다. 각 개체(이벤트, 속성 및 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있습니다. 총합하면, 이는 단일 호출로 최대 225명의 사용자를 업데이트할 수 있음을 의미합니다. 또한 여러 개체로 단일 고객 프로필을 업데이트할 수 있습니다.

**월간 활성 사용자(MAU) - CY 24-25를** 구매한 고객에게는 다른 한도가 적용됩니다. 이러한 한도에 대한 자세한 내용은 [월간 활성 사용자 - CY 24-25 한도를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau) 참조하십시오.

[API 속도 제한에]({{site.baseurl}}/api/api_limits/) 대한 자세한 내용은 해당 페이지를 참조하시고, 한도 증액이 필요하시면 고객 성공 매니저에게 문의하십시오.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
2024년 8월 22일 또는 그 이후에 Braze에 온보딩한 경우, 이 엔드포인트는 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 명시된 대로 분당 250개의 요청으로 속도 제한이 적용됩니다.

다음 요구 사항을 충족하면 이 엔드포인트의 속도 제한을 초당 40개 요청으로 늘릴 수도 있습니다:

- 작업 공간에는 기본값 요청 제한(분당 250건)이 인에이블먼트되어 있습니다. 기존에 설정된 속도 제한을 해제하는 데 도움이 필요하시면 Braze 계정 매니저에게 문의하십시오.
- 귀하의 요청에는 수신하고자 하는 모든 필드를 나열하기 위한  `fields_to_export`매개변수가 포함되어 있습니다.

{% alert important %}
매개변수에  또는`campaigns_received``fields_to_export`  을`canvases_received` 포함하는 경우, 요청은 더 빠른 속도 제한 적용 대상에서 제외됩니다. 이러한 항목들은 특정 사용 사례가 있을 경우에만 요청에 포함할 것을 권장합니다.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
이 엔드포인트에는 분당 20,000개의 요청에 대한 공유 속도 제한이 적용됩니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 ,`/users/alias/new` `/users/identify`, `/users/merge`, 및`/users/alias/update`엔드포인트와 공유됩니다.

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
이 엔드포인트에는 분당 20,000개의 요청에 대한 공유 속도 제한이 적용됩니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 ,`/users/delete` `/users/identify`, `/users/merge`, 및`/users/alias/update`엔드포인트와 공유됩니다.

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
이 엔드포인트에는 분당 20,000개의 요청에 대한 공유 속도 제한이 적용됩니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 ,`/users/delete` `/users/alias/new`, `/users/identify`, 및`/users/merge`엔드포인트와 공유됩니다.

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
이 엔드포인트에는 분당 20,000개의 요청에 대한 공유 속도 제한이 적용됩니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 ,`/users/delete` `/users/alias/new`, `/users/merge`, 및`/users/alias/update`엔드포인트와 공유됩니다.

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
이 엔드포인트에는 분당 20,000개의 요청에 대한 공유 속도 제한이 적용됩니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 ,`/users/delete` `/users/alias/new`, `/users/identify`, 및`/users/alias/update`엔드포인트와 공유됩니다.

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
이 엔드포인트에는 시간당 1,000개의 요청에 대한 공유 속도 제한을 적용합니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 ,`/events/list``/events` , 및`/purchases/product_list`엔드포인트와 공유됩니다.

<!---/events-->

{% elsif include.endpoint == "events" %}
이 엔드포인트에는 시간당 1,000개의 요청에 대한 공유 속도 제한을 적용합니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 ,`/events/list``/custom_attributes` , 및`/purchases/product_list`엔드포인트와 공유됩니다.

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
이 엔드포인트에는 시간당 1,000개의 요청에 대한 공유 속도 제한을 적용합니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 ,`/events``/custom_attributes` , 및`/purchases/product_list`엔드포인트와 공유됩니다.

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
이 엔드포인트에는 시간당 1,000개의 요청에 대한 공유 속도 제한을 적용합니다. 이 속도 제한은 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 설명된 대로 ,`/events``/custom_attributes` , 및`/events/list`엔드포인트와 공유됩니다.

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
요청 시 Connected 오디언스 필터를 사용할 경우, 해당 엔드포인트에 대해 분당 250건의 요청 제한을 적용합니다. 그렇지 않은 경우, 를 지정할 때 이 엔드포인트는 [API ]({{site.baseurl}}/api/api_limits/)`external_id`[속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 명시된 대로 ,`/campaigns/trigger/send` , `/canvas/trigger/send`및 간에`/messages/send` 공유되는 시간당 250,000개의 요청이라는 기본값 속도 제한을 가집니다.

Braze 엔드포인트는 API 요청의 일괄 처리를 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 어느 것이든 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`, 각각 개별 메시지 매개변수를 가지고 있습니다.
- 요청에서 연결된 오디언스 객체로 정의된 모든 규모의 오디언스 세그먼트

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
엔드포인트는`/transactional/v1/campaigns/{campaign_id}/send` 시간당 단위로 요금이 부과되는 유료 엔드포인트입니다(예: 패키지에 따라 시간당 50,000개). 엔드포인트별 별도의 속도 제한은 없습니다: 할당된 용량을 초과하여 전송할 수 있지만, SLA 적용 대상은 할당된 용량에 한합니다. 이 엔드포인트에 대한 요청은 [전체 외부 API 속도 제한]({{site.baseurl}}/api/api_limits/)에 포함됩니다. 해당 한도(예: 모든 엔드포인트에서 시간당 250,000건의 요청)를 초과할 경우, Braze는 429를 반환하고 요청이 제한됩니다. 트랜잭션량 카운트는 매시간 초기화되므로, 1시간 후에는 새로운 할당량이 제공됩니다. SLA 적용 범위 내에서 이메일의 99.9%는 1분 이내에 발송됩니다.

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
이 엔드포인트를 사용하여 특정 워크스페이스에 대해 하루에 최대 100개의 커스텀 발신자 식별자를 생성할 수 있습니다. 만들어진 각 `send_id``campaign_id`조합은 일일 한도에 포함됩니다. 모든 유효한 요청에 대한 응답 헤더에는 현재 속도 제한 상태가 포함됩니다. 자세한 내용은 [API 속도 제한을]({{site.baseurl}}/api/api_limits/) 참조하십시오.

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
이 엔드포인트는 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 명시된 바와 같이  및`/v2/subscription/status/set`  `/subscription/status/set`엔드포인트 간에 공유되는 분당 5,000개의 요청 속도 제한을 적용받습니다.

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
이 엔드포인트는 분당 50개의 요청으로 속도 제한이 적용됩니다.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
이 엔드포인트는 분당 20개의 요청으로 속도 제한이 적용됩니다.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
이 엔드포인트는 분당 100개의 요청으로 속도 제한이 적용됩니다.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Braze 엔드포인트는 [API 요청의 일괄 처리를]({{site.baseurl}}/api/api_limits/#batching-api-requests) 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 어느 것이든 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`, 각각 개별 메시지 매개변수를 가지고 있습니다.
- Braze 대시보드에서 생성된 크기와 관계없이 세그먼트, `segment_id`에 의해 지정됨.
- 요청에서 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 객체로 정의된, 규모에 상관없는 오디언스 세그먼트

{% endif %}

{% if include.category == "send messages endpoints" %}

Braze 엔드포인트는 [API 요청의 일괄 처리를]({{site.baseurl}}/api/api_limits/#batching-api-requests) 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 어느 것이든 도달할 수 있습니다:

- 최대 50개의 특정 `external_ids`, 각각 개별 메시지 매개변수를 가지고 있습니다.
- 요청에서 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 객체로 정의된, 규모에 상관없는 오디언스 세그먼트

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

이 엔드포인트는 분당 250,000개의 요청에 대한 속도 제한이 적용됩니다.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Braze 엔드포인트는 [API 요청의 일괄 처리를]({{site.baseurl}}/api/api_limits/#batching-api-requests) 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 어느 것이든 도달할 수 있습니다:

- 최대 50개 특정 `external_ids`
- Braze 대시보드에서 생성된 크기와 관계없이 세그먼트, `segment_id`에 의해 지정됨.
- 요청에서 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 객체로 정의된, 규모에 상관없는 오디언스 세그먼트

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

이 엔드포인트는 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 명시된 바와 같이, 모든 비동기 카탈로그 항목 엔드포인트 간에 분당 16,000개의 요청이라는 공유 속도 제한을 적용받습니다.

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

이 엔드포인트는 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 명시된 바와 같이, 모든 동기식 카탈로그 항목 엔드포인트 간에 분당 50개의 요청이라는 공유 속도 제한을 적용받습니다.

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

이 엔드포인트는 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 명시된 바와 같이, 모든 동기식 카탈로그 엔드포인트 간에 분당 50개의 요청이라는 공유 속도 제한을 적용받습니다.

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

이 엔드포인트는 [API 속도 제한]({{site.baseurl}}/api/api_limits/) 설명서에 명시된 바와 같이, 모든 비동기 카탈로그 필드 및 선택 엔드포인트 간에 분당 50개의 요청이라는 공유 속도 제한을 적용받습니다.

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

이 엔드포인트는 분당 50,000개의 요청에 대한 속도 제한이 적용됩니다.

{% endif %}
