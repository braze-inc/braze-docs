---
nav_title: "GET: 반송된 이메일 조회"
article_title: "GET: 반송된 이메일 조회"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 하드 반송된 이메일 주소를 쿼리하거나 나열하는 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 반송된 이메일 조회
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> 이 엔드포인트를 사용하여 특정 기간 내에 이메일 메시지를 '하드 바운스'된 이메일 주소 목록을 가져올 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `email.hard_bounces` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| ----------|-----------| ----------|----- |
| `start_date` | 선택 사항* | YYYY-MM-DD 형식의 문자열| * `start_date` 또는 `email` 중 하나가 필요합니다. 하드 바운스를 검색할 범위의 시작 날짜이며 `end_date` 보다 이전이어야 합니다. 이는 API에서 UTC 시간 기준 자정으로 처리됩니다. |
| `end_date` | 필수 | YYYY-MM-DD 형식의 문자열 | 범위를 검색할 종료 날짜를 하드 바운스합니다. API에 의해 이것은 UTC 시간으로 자정으로 처리됩니다. |
| `limit` | 선택 사항 | 정수 | 반환되는 결과 수를 제한하는 선택적 필드입니다. 기본값은 100, 최대값은 500입니다. |
| `offset` | 선택 사항 | 정수 | 검색할 목록의 시작점(선택 사항)입니다. |
| `email` | 선택 사항* | 문자열 | * `start_date` 또는 `email` 중 하나가 필요합니다. 제공된 경우 사용자가 하드 바운스했는지 여부를 반환합니다. 이메일 문자열이 올바르게 형식화되었는지 확인하십시오. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
`end_date` 이메일과 `email` 또는 `start_date` 이메일 중 하나를 제공해야 합니다. `start_date`, `end_date`, `email` 세 가지를 모두 제공하면 제공된 이메일의 우선순위를 지정하고 날짜 범위는 무시합니다.
{% endalert %}

날짜 범위에 하드 바운스 횟수가 `limit` 보다 많은 경우, 호출이 `limit` 보다 적거나 결과가 0이 될 때까지 매번 `offset` 을 증가시키면서 여러 번 API 호출을 수행해야 합니다. `offset` 및 `limit` 매개 변수를 `email` 과 함께 포함하면 빈 응답을 반환할 수 있습니다.

## 요청 예시
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 응답
항목은 내림차순으로 나열됩니다.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
