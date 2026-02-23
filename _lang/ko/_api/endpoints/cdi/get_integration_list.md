---
nav_title: "GET: 목록 통합"
article_title: "GET: 목록 통합"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "이 문서에서는 목록 통합 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 목록 통합
{% apimethod get %}
/cdi/integrations
{% endapimethod %}

> 이 엔드포인트를 사용하여 기존 연동 목록을 반환합니다.


{% alert note %}
이 엔드포인트를 사용하려면 `cdi.integration_list` 권한이 있는 API 키를 생성해야 합니다.
{% endalert %}

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## 쿼리 매개변수

이 엔드포인트에 대한 각 호출은 10개 항목을 반환합니다. 10개가 넘는 통합이 있는 목록의 경우 `Link` 헤더를 사용하여 예제 응답에 표시된 대로 다음 페이지에서 데이터를 검색합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `cursor` | Optional | 문자열 | 통합 목록의 페이지 매김을 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 예시

### 커서 없음

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### 커서 포함

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

### 성공 응답의 예

`200` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

{% alert note %}
총 통합 수가 10개 이하인 경우 `Link` 헤더는 존재하지 않습니다. 커서가 없는 통화의 경우 `prev`가 표시되지 않습니다. 항목의 마지막 페이지를 보면 `next` 이 표시되지 않습니다.
{% endalert %}

```
Link: </cdi/integrations?cursor=c2tpcDow>; rel="prev",</cdi/integrations?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
      "integration_id": (string) integration ID,
      "app_group_id": (string) app group ID,
      "integration_name": (string) integration name,
      "integration_type": (string) integration type,
      "integration_status": (string) integration status,
      "contact_emails": (string) contact email(s),
      "last_updated_at": (string) last timestamp that was synced in ISO 8601,
      "warehouse_type": (string) data warehouse type,
      "last_job_start_time": (string) timestamp of the last sync run in ISO 8601,
      "last_job_status": (string) status of the last sync run,
      "next_scheduled_run": (string) timestamp of the next scheduled sync in ISO 8601,
    },
  ],
  "message": "success"
}
```

## 문제 해결

다음 표에는 가능한 반환 오류와 관련된 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `400 Invalid cursor` | `cursor` 주소가 유효한지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

추가 상태 코드 및 관련 오류 메시지는 [심각한 오류 & 응답을]({{site.baseurl}}/api/errors/#fatal-errors) 참조하세요.

{% endapi %}
