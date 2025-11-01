---
nav_title: "GET: 사용 가능한 이메일 템플릿 목록"
article_title: "GET: 사용 가능한 이메일 템플릿 목록"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 기사에서는 사용 가능한 이메일 템플릿 Braze 엔드포인트에 대한 세부 정보를 설명합니다."

---
{% api %}
# 사용 가능한 이메일 템플릿 목록
{% apimethod get %}
/templates/email/list
{% endapimethod %}

> 이 엔드포인트를 사용하여 Braze 계정에서 사용 가능한 이메일 템플릿 목록을 가져올 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## Prerequisites
이 엔드포인트를 사용하려면 `templates.email.list` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `modified_after`  | 선택 사항 | 문자열 in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format | 주어진 시간 이후에 업데이트된 템플릿만 검색합니다. |
| `modified_before`  |  선택 사항 | 문자열 in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format | 지정된 시간에 업데이트된 템플릿만 검색합니다. |
| `limit` | 선택 사항 | 양수 | 검색할 최대 템플릿 수. 기본값 to 100 if not provided, with a maximum acceptable value of 1000. |
| `offset`  |  선택 사항 | 양수 | 검색 기준에 맞는 나머지 템플릿을 반환하기 전에 건너뛸 템플릿 수. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## 응답 

{% alert important %}
이메일을 위한 드래그 앤 드롭 편집기를 사용하여 작성된 템플릿은 이 응답에 제공되지 않습니다.
{% endalert %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": the number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string) the time the email was created at in ISO 8601,
    "updated_at": (string) the time the email was updated in ISO 8601,
    "tags": (array of strings) tags appended to the template
}
```
{% endapi %}



