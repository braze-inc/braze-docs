---
nav_title: "POST: 하드 반송된 이메일을 제거하십시오."
article_title: "POST: 하드 반송 이메일 제거"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "이 기사에서는 Remove 하드 반송 이메일 주소 Braze 엔드포인트에 대한 세부 정보를 설명합니다."

---
{% api %}
# 하드 반송된 이메일을 제거하십시오.
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

> 이 엔드포인트를 사용하여 이메일 제공업체가 관리하는 Braze 반송 목록 및 반송 목록에서 이메일 주소를 제거할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `email.bounce.remove` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| ----------|-----------| ---------|------ |
| `email` | 필수 | 문자열 또는 배열 | 수정할 이메일 주소를 문자열로 입력하거나 수정할 이메일 주소를 최대 50개까지 배열할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```

{% endapi %}
