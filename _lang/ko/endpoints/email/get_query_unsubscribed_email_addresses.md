---
nav_title: "GET: 수신 거부된 이메일 주소 목록 조회하기"
article_title: "GET: 수신 거부된 이메일 주소 목록 조회하기"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "이 문서에서는 Braze 엔드포인트의 목록 검색 또는 구독 취소 이메일 조회에 대한 자세한 내용을 간략하게 설명합니다."

---
{% api %}
# 수신 거부된 이메일 주소 목록 조회하기
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> 이 엔드포인트를 사용하여 `start_date` 에서 `end_date` 까지의 기간 동안 구독을 취소한 최신 이메일을 반환합니다. 전체 구독 상태 기록을 보려면 [Currents를]({{site.baseurl}}/user_guide/data/braze_currents/) 사용하여 이 데이터를 추적하세요.

이 엔드포인트를 사용하여 Braze와 다른 이메일 시스템 또는 자체 데이터베이스 간의 양방향 동기화를 설정할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `email.unsubscribe` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| ----------|-----------| ---------|------ |
| `start_date` | 선택 사항 <br>(참고 참조) | YYYY-MM-DD 형식의 문자열| 탈퇴를 검색할 범위의 시작 날짜는 end_date. 보다 이전이어야 합니다. 이는 API에서 UTC 시간 기준 자정으로 처리됩니다. |
| `end_date` | 선택 사항 <br>(참고 참조) | YYYY-MM-DD 형식의 문자열 | 구독 취소를 검색할 범위의 종료일입니다. 이는 API에서 UTC 시간 기준 자정으로 처리됩니다. |
| `limit` | 선택 사항 | 정수 | 반환되는 결과 수를 제한하는 선택적 필드입니다. 기본값은 100, 최대값은 500입니다. |
| `offset` | 선택 사항 | 정수 | 검색할 목록의 시작점(선택 사항)입니다. |
| `sort_direction` | Optional | 문자열 | `asc` 값을 전달하여 구독 취소를 가장 오래된 것부터 최신 것 순으로 정렬합니다. `desc` 을 입력하여 최신에서 오래된 순으로 정렬합니다. `sort_direction` 이 포함되지 않은 경우 기본 순서는 최신에서 오래된 순서입니다. |
| `email` | 선택 사항 <br>(참고 참조) | 문자열 | 제공된 경우 사용자가 구독을 취소했는지 여부를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
`end_date` 이메일 주소와 `email` 또는 `start_date` 이메일 주소를 제공해야 합니다.
{% endalert %}

날짜 범위에 `limit` 이상의 구독 취소 횟수가 있는 경우, 호출이 `limit` 보다 적거나 결과가 0이 될 때까지 매번 `offset` 을 늘려가며 여러 번 API 호출을 수행해야 합니다.

## 예시 요청
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
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
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
