---
nav_title: "POST: 차단 목록 이메일"
article_title: "POST: 차단 목록 이메일"
search_tag: Endpoint
page_order: 8
layout: api_page
page_type: reference
description: "이 문서에서는 차단 목록 이메일 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 차단 목록 이메일
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blocklist
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용자의 이메일 수신을 취소하고 하드 바운스로 표시할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `email.blacklist` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blocklist_email1","blocklist_email2"]
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| -----------|----------| --------|------- |
| `email` | 필수 | 문자열 또는 배열 | 차단할 이메일 주소를 문자열로 입력하거나 최대 50개의 이메일 주소 배열을 차단 목록에 추가합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blocklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blocklist_email1","blocklist_email2"]
}'
```

{% endapi %}
