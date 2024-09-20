---
nav_title: "GET: 작업 동기화 상태 나열"
article_title: "GET: 작업 동기화 상태 나열"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_job_sync/
layout: api_page
page_type: reference
description: "이 문서에서는 목록 작업 동기화 상태 Braze 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 작업 동기화 상태 나열
{% apimethod get %}
/cdi/integrations/{integration_id}/job_sync_status
{% endapimethod %}

> 이 엔드포인트를 사용하여 지정된 통합에 대한 과거 동기화 상태 목록을 반환합니다.

{% alert note %}
이 엔드포인트를 사용하려면 `cdi.integration_job_status` 권한이 있는 API 키를 생성해야 합니다.
{% endalert %}

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='cdi job sync status' %}

## 경로 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
|---|---|---|---|
| `integration_id` | 필수 | 문자열 | 통합 ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 쿼리 매개변수

이 엔드포인트에 대한 각 호출은 10개 항목을 반환합니다. 10개 이상의 동기화가 있는 통합의 경우 `Link` 헤더를 사용하여 다음 예제 응답과 같이 다음 페이지에서 데이터를 검색합니다.

| 매개 변수 | 필수 | 데이터형 | 설명 |
|---|---|---|---|
| `cursor` | 선택 사항 | 문자열 | 동기화 상태의 페이지 매김을 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 요청 예시

### 커서 없이

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### 커서 사용

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

### 성공 응답의 예

`200` 상태 코드는 다음 응답 본문을 반환할 수 있습니다.

{% alert note %}
총 동기화가 10개 이하인 경우 `Link` 헤더가 존재하지 않습니다. 커서가 없는 통화의 경우 `prev`가 표시되지 않습니다. 항목의 마지막 페이지를 볼 때 `next`는 표시되지 않습니다.
{% endalert %}

```
Link: </cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow>; rel="prev",</cdi/integrations00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
        "job_status": (string) status of the sync, see below for explanation of different statuses,
        "sync_start_time": (string) time the sync started in ISO 8601,
        "sync_finish_time": (string) time the sync finished in ISO 8601,
        "last_timestamp_synced": (string) last UPDATED_AT timestamp processed by the sync in ISO 8601,
        "rows_synced": (integer) number of rows successfully synced to Braze,
        "rows_failed_with_errors": (integer) number of rows failed because of errors,
    },
  ],
  "message": "success"
}
```

| job\_status | Explanation |
| --- | --- |
| `running` | 작업이 현재 실행 중입니다. |
| `success` | 모든 행이 성공적으로 동기화되었습니다. |
| `partial` | 오류로 인해 일부 행을 동기화하지 못했습니다. |
| `error` | 행이 동기화되지 않았습니다. |
| `config_error` | 통합 구성에 오류가 있습니다. 통합 설정을 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2}

## 문제 해결

다음 표에는 반환될 수 있는 오류 및 관련 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `400 Invalid cursor` | `cursor`가 유효한지 확인하세요. |
| `400 Invalid integration ID` | `integration_id`가 유효한지 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2}

추가 상태 코드 및 관련 오류 메시지는 [심각한 오류 및 응답]({{site.baseurl}}/api/errors/#fatal-errors)을 참조하세요.

{% endapi %}
