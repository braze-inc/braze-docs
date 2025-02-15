---
nav_title: "POST: [엔드포인트 이름]"
article_title: "레이아웃 예시: POST: 사용자 추적"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
excerpt_separator: ""

description: "이 문서에서는 이 POST [엔드포인트 이름] Braze 엔드포인트에 대한 자세한 내용과 사용법을 설명합니다."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# [엔드포인트 이름]

{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
이 엔드포인트를 사용하여 Braze의 유효하지 않은 전화번호 목록에서 "유효하지 않은" 전화번호를 제거하세요. 유효하지 않은 것으로 표시된 전화번호의 유효성을 다시 확인하는 데 사용할 수 있습니다.

<!-- Your postman link. Once you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## 사용량 제한

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

<!--This is where you can give more information about your endpoint request body. -->

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

### 요청 매개변수

<!--This is a place for you to describe additional details for the parameters in the request body.-->

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| ----------|-----------| ---------|------ |
| `phone_number` | 필수 | e.164 형식의 문자열 배열 | 최대 50개의 전화번호 배열을 수정할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시

<!--The following example demonstrates a request that will remove specific SMS numbers from Braze's invalid phone number list via the API:-->

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```
{% endapi %}
