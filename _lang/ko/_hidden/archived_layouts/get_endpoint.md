---
nav_title: "가져오기: [엔드포인트 이름]"
article_title: "레이아웃 예시: 가져오기: [엔드포인트 이름]"
search_tag: Endpoint
page_order: 1
excerpt_separator: ""
layout: api_page
page_type: reference
description: "이 문서에서는 [엔드포인트 이름] 가져오기 Braze 엔드포인트의 사용법과 매개변수에 대해 간략하게 설명합니다."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# 쿼리 또는 목록 [항목 엔드포인트 "Gets"]

{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
이 엔드포인트를 사용하여 특정 기간 내에 '유효하지 않음'으로 간주된 전화번호 목록을 가져올 수 있습니다.

<!-- Your postman link. After you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## 사용량 제한

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

<!--This is where you can give more information about your endpoint parameters. -->

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| ----------|-----------| ----------|----- |
| `start_date` | 선택 사항 <br>(참고 참조) | YYYY-MM-DD 형식의 문자열| 유효하지 않은 전화번호를 검색할 범위의 시작 날짜는 `end_date` 보다 이전이어야 합니다. 이는 API에서 UTC 시간 기준 자정으로 처리됩니다. |
| `end_date` | 선택 사항 <br>(참고 참조) | YYYY-MM-DD 형식의 문자열 | 유효하지 않은 전화번호를 검색할 범위의 종료일입니다. 이는 API에서 UTC 시간 기준 자정으로 처리됩니다. |
| `limit` | 선택 사항 | 정수 | 반환되는 결과 수를 제한하는 선택적 필드입니다. 기본값은 100, 최대값은 500입니다. |
| `offset` | 선택 사항 | 정수 | 검색할 목록의 시작점(선택 사항)입니다. |
| `phone_numbers` | 선택 사항 <br>(참고 참조) | e.164 형식의 문자열 배열 | 제공된 전화번호가 유효하지 않은 것으로 확인되면 해당 전화번호를 반환해 드립니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
`start_date` 와 `end_date` 또는 `phone_numbers` 중 하나를 제공해야 합니다. `start_date`, `end_date`, `phone_numbers` 세 가지를 모두 제공하면 주어진 전화번호를 우선시하고 날짜 범위는 무시합니다.
{% endalert %}

## 요청 예시

<!--The following example demonstrates a request that will pull a list of phone numbers that have been deemed invalid via the API:-->
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 응답

<!-- An example response that defines the different variables returned-->
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    }
  ],
  "message": "success"
}
```

{% endapi %}
