---
nav_title: "POST: 유효하지 않은 전화번호 제거"
article_title: "POST: 잘못된 전화번호 제거"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "이 문서에서는 유효하지 않은 전화번호 제거 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 유효하지 않은 전화번호 제거
{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

> 이 엔드포인트를 사용하여 유효하지 않은 전화번호 목록에서 '유효하지 않은' 전화번호를 제거할 수 있습니다.

유효하지 않은 것으로 표시된 전화번호의 유효성을 다시 검사하는 데 사용할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `sms.invalid_phone_numbers.remove` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| ----------|-----------| ---------|------ |
| `phone_number` | 필수 | e.164 형식의 문자열 배열 | 최대 50개의 전화번호 배열을 수정할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```

{% endapi %}
