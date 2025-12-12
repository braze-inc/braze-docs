---
nav_title: "POST: 예약된 API 트리거 캔버스 삭제"
article_title: "POST: 예약된 API 트리거 캔버스 삭제하기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 삭제된 예약 API 트리거 캔버스 Braze 엔드포인트에 대한 세부 정보를 설명합니다."

---
{% api %}
# 예약된 API 트리거 캔버스 삭제
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/delete
{% endapimethod %}

> 삭제 일정 엔드포인트는 이전에 예약한 API 트리거 캔버스를 전송되기 전에 취소할 수 있도록 합니다.

예약된 메시지 또는 트리거가 전송 예정 시간에 매우 가까워지거나 그 사이에 삭제되는 경우 최선을 다해 업데이트되므로 마지막 순간 삭제가 대상 사용자 전체, 일부 또는 아무에게도 적용될 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `canvas.trigger.schedule.delete` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `canvas_id`| Required | 문자열 | [캔버스 식별자]({{site.baseurl}}/api/identifier_types/)를 참조하세요. |
| `schedule_id` | Required | 문자열 | 삭제할 `schedule_id` (일정 만들기 응답에서 얻은 값)입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}
