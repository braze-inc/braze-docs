
<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "기본값" %}
[API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 이 엔드포인트에 시간당 250,000건의 요청으로 기본 Braze 사용량 제한을 적용합니다.

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "대시보드 사용자 업데이트" %}
이 엔드포인트에는 1개 회사에 하루 5,000건의 요청으로 사용량 제한이 적용됩니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/scim/v2/Users/` GET, DELETE 및 POST 엔드포인트에서 공유됩니다.

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "대시보드 사용자 조회" %}
이 엔드포인트에는 1개 회사에 하루 5,000건의 요청으로 사용량 제한이 적용됩니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/scim/v2/Users/` PUT, GET, DELETE 및 POST 엔드포인트에서 공유됩니다.

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "대시보드 사용자 삭제" %}
이 엔드포인트에는 1개 회사에 하루 5,000건의 요청으로 사용량 제한이 적용됩니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/scim/v2/Users/` PUT, GET, DELETE 및 POST 엔드포인트에서 공유됩니다.

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "대시보드 사용자 생성" %}
이 엔드포인트에는 1개 회사에 하루 5,000건의 요청으로 사용량 제한이 적용됩니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/scim/v2/Users/` PUT, GET 및 DELETE 엔드포인트에서 공유됩니다.

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "대시보드 사용자 이메일 조회" %}
이 엔드포인트에는 1개 회사에 하루 5,000건의 요청으로 사용량 제한이 적용됩니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/scim/v2/Users/` PUT, GET, DELETE 및 POST 엔드포인트에서 공유됩니다.

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "외부 ID 마이그레이션" %}
{% elsif include.endpoint == "API 사용량 제한{% elsif include.endpoint == "에서 설명한 대로 이 엔드포인트에 시간당 1,000건의 요청으로 사용량 제한을 적용합니다.

<!---/users/track-->

{% elsif include.endpoint == "사용자 추적" %}
모든 고객에 대해 이 엔드포인트에 분당 50,000건의 요청으로 기본 사용량 제한을 적용합니다. 각 `/users/track` 요청에는 최대 75개의 이벤트 오브젝체, 75개의 속성 오브젝트 및 75개의 구매 오브젝트가 포함될 수 있습니다. 각 오브젝트(이벤트, 속성 및 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있습니다. 따라서 한 번의 통화로 최대 225명의 사용자를 업데이트할 수 있습니다. 또한 단일 고객 프로필을 여러 오브젝트로 업데이트할 수 있습니다.

**월간 활성 사용자 - CY 24-25**를 구매한 고객에게 다른 제한이 적용됩니다. 이러한 제한에 대한 자세한 내용은 [월간 활성 사용자 - CY 24-25 제한]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25)을 참조하세요.

자세한 내용은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)의 관련 페이지를 참조하세요. 제한을 늘려야 하는 경우 고객 성공 매니저에게 문의하세요.

<!---/users/export/ids-->

{% elsif include.endpoint == "사용자 내보내기 ID" %}
2024년 8월 22일 이후에 Braze에 온보딩한 경우 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 이 엔드포인트에는 분당 250건의 요청으로 사용량 제한이 적용됩니다.

<!---/users/delete-->

{% elsif include.endpoint == "사용자 삭제" %}
2021년 9월 16일 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 분당 20,000건의 요청으로 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/users/alias/new`, `/users/identify` 및 `/users/merge` 엔드포인트에서 공유됩니다.

<!---/users/alias/new-->

{% elsif include.endpoint == "사용자 별칭 신규" %}
2021년 9월 16일 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 분당 20,000건의 요청으로 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/users/delete`, `/users/identify`, `/users/merge` 및 `/users/alias/update` 엔드포인트에서 공유됩니다.

<!---/users/alias/update-->

{% elsif include.endpoint == "사용자 별칭 업데이트" %}
2021년 9월 16일 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 분당 20,000건의 요청으로 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/users/delete`, `/users/identify`, `/users/merge` 및 `/users/alias/new` 엔드포인트에서 공유됩니다.

<!---/users/alias/update-->

{% elsif include.endpoint == "사용자 별칭 업데이트" %}
2021년 9월 16일 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 분당 20,000건의 요청으로 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/users/delete`, `/users/identify` 및 `/users/merge` 엔드포인트에서 공유됩니다.

<!---/users/identify-->

{% elsif include.endpoint == "사용자 식별" %}
2021년 9월 16일 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 분당 20,000건의 요청으로 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/users/delete`, `/users/alias/new`, `/users/merge` 및 `/users/alias/update` 엔드포인트에서 공유됩니다.

<!---/users/merge-->

{% elsif include.endpoint == "사용자 병합" %}
2021년 9월 16일 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 분당 20,000건의 요청으로 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/users/delete`, `/users/alias/new`, `/users/identify` 및 `/users/alias/update` 엔드포인트에서 공유됩니다.

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
2021년 9월 16일 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 시간당 1,000건의 요청으로 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/events`, `/events/list` 및 `/purchases/product_list` 엔드포인트에서 공유됩니다.

<!---/events-->

{% elsif include.endpoint == "이벤트" %}
2021년 9월 16일 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 시간당 1,000건의 요청으로 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/custom_attributes`, `/events/list` 및 `/purchases/product_list` 엔드포인트에서 공유됩니다.

<!---/events/list-->

{% elsif include.endpoint == "이벤트 목록" %}
2021년 9월 16일 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 시간당 1,000건의 요청으로 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/custom_attributes`, `/events` 및 `/purchases/product_list` 엔드포인트에서 공유됩니다.

<!---/purchases/product_list-->

{% elsif include.endpoint == "구매 제품 목록" %}
2021년 9월 16일 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 시간당 1,000건의 요청으로 공유 사용량 제한을 적용합니다. 이 사용량 제한은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 `/custom_attributes`, `/events` 및 `/events/list` 엔드포인트에서 공유됩니다.

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "엔드포인트 전송" %}
요청에 세그먼트 또는 연결된 오디언스를 지정할 때 이 엔드포인트에 분당 250건의 요청으로 사용량 제한을 적용합니다. 그렇지 않으면 `external_id`를 지정하는 경우 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 이 엔드포인트에는 `/messages/send`, `/campaigns/trigger/send` 및 `/canvas/trigger/send` 간에 공유되는 시간당 250,000건의 요청으로 기본 사용량 제한이 적용됩니다.

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "트랜잭션 이메일" %}
Braze 트랜잭션 이메일에는 사용량 제한이 적용되지 않습니다. 선택한 패키지에 따라 시간당 정해진 수의 트랜잭션 이메일이 SLA에 의해 보장됩니다. 해당 사용량을 초과하는 요청은 계속 전송되지만 SLA가 적용되지 않습니다. 99.9%의 이메일이 1분 이내에 전송됩니다.

<!---/sends/id/create-->

{% elsif include.endpoint == "전송 ID 생성" %}
이 엔드포인트를 통해 생성할 수 있는 커스텀 전송 식별자의 일일 최대 개수는 지정된 워크스페이스에서 100개입니다. 생성하는 `send_id` 및 `campaign_id` 조합은 모두 일일 제한에 포함됩니다. 모든 유효한 요청의 응답 헤더에는 현재 사용량 제한 상태가 포함됩니다. 자세한 내용은 [API 사용량 제한]({{site.baseurl}}/api/api_limits/)을 참조하세요.

<!---/subscription/status/set-->
{% elsif include.endpoint == "구독 상태 설정" %}
[API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 이 엔드포인트에는 `/subscription/status/set` 및 `/v2/subscription/status/set` 엔드포인트에서 공유되는 시간당 5,000건의 요청으로 사용량 제한이 적용합니다.

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "CDI 목록 통합" %}
이 엔드포인트에는 분당 50건의 요청으로 사용량 제한이 적용됩니다.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "CDI 작업 동기화" %}
이 엔드포인트에는 분당 20건의 요청으로 사용량 제한이 적용됩니다.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "CDI 작업 동기화 상태" %}
이 엔드포인트에는 분당 100건의 요청으로 사용량 제한이 적용됩니다.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "메시지 엔드포인트" %}

Braze 엔드포인트는 [API 요청 일괄 처리]({{site.baseurl}}/api/api_limits/#batching-api-requests)를 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다.

- 각각 개별 메시지 매개변수가 있는 최대 50개의 특정 `external_ids`
- Braze 대시보드에서 생성된 모든 크기의 세그먼트로, `segment_id`로 지정됨
- 요청에서 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 오브젝트로 정의된 모든 크기의 오디언스 세그먼트

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "메시지 전송 엔드포인트" %}

Braze 엔드포인트는 [API 요청 일괄 처리]({{site.baseurl}}/api/api_limits/#batching-api-requests)를 지원합니다. 메시징 엔드포인트에 대한 단일 요청은 다음 중 하나에 도달할 수 있습니다.

- 최대 50개의 특정 `external_ids`
- Braze 대시보드에서 생성된 모든 크기의 세그먼트로, `segment_id`로 지정됨
- 요청에서 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 오브젝트로 정의된 모든 크기의 오디언스 세그먼트

{% endif %}

{% if include.endpoint == "비동기 카탈로그 항목" %}

[API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 이 엔드포인트에는 모든 비동기 카탈로그 항목 엔드포인트 간에 분당 16,000건의 요청으로 공유 사용량 제한이 적용됩니다.

{% endif %}

{% if include.endpoint == "동기식 카탈로그 항목" %}

[API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 이 엔드포인트에는 모든 동기 카탈로그 항목 엔드포인트 간에 분당 50건의 요청으로 공유 사용량 제한이 적용됩니다.

{% endif %}

{% if include.endpoint == "동기식 카탈로그" %}

[API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 이 엔드포인트에는 모든 동기 카탈로그 엔드포인트 간에 분당 50건의 요청으로 공유 사용량 제한이 적용됩니다.

{% endif %}

{% if include.endpoint == "비동기 카탈로그 필드'' 또는 include.endpoint == ''비동기 카탈로그 선택 항목" %}

[API 사용량 제한]({{site.baseurl}}/api/api_limits/)에서 설명한 대로 이 엔드포인트에는 모든 비동기 카탈로그 필드 및 선택 항목 엔드포인트 간에 분당 50건의 요청으로 공유 사용량 제한이 적용됩니다.

{% endif %}

{% if include.endpoint == "캠페인 분석 내보내기" %}

이 엔드포인트에는 분당 50,000건의 요청으로 사용량 제한이 적용됩니다.

{% endif %}
