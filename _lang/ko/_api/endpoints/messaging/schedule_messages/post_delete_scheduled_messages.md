---
nav_title: "POST: 예약된 메시지 삭제"
article_title: "POST: 예약된 메시지 삭제"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 예약된 메시지 삭제 Braze 엔드포인트에 대해 자세히 설명합니다."

---
{% api %}
# 예약된 메시지 삭제
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/delete
{% endapimethod %}

> 이 엔드포인트를 사용하여 보내기 전에 이전에 예약한 메시지를 취소할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5e89355c-0a5d-4d8b-8d89-2fd99bac36b0 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `messages.schedule.delete` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | 필수 | 문자열 | 삭제할 `schedule_id`(스케줄 생성에 대한 응답에서 가져옴)입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
