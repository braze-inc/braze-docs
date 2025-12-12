---
nav_title: "GET: 예정된 캠페인 및 캔버스 목록 보기"
article_title: "GET: 예정된 캠페인 및 캔버스 목록 보기"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "이 문서에서는 예정된 캠페인 목록과 캔버스 브레이즈 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 예정된 캠페인 및 캔버스 목록 보기
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

> 이 엔드포인트를 사용하여 지금부터 요청에 지정된 `end_time` 사이에 예약된 캠페인 및 항목 캔버스에 대한 정보의 JSON 목록을 반환합니다.

매일 반복되는 메시지는 다음 번 발생 시 한 번만 표시됩니다. 이 엔드포인트에서 반환되는 결과에는 Braze 대시보드에서 생성 및 예약된 캠페인과 캔버스가 포함됩니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `messages.schedule_broadcasts` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `end_time` | 필수 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식의 문자열 | 예정된 캠페인 및 캔버스를 검색할 범위의 종료일입니다. 이는 API에서 UTC 시간 기준 자정으로 처리됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "scheduled_broadcasts": [
    {
      "name": (string) the name of the scheduled broadcast,
      "id": (stings) the Canvas or campaign identifier,
      "type": (string) the broadcast type either Canvas or Campaign,
      "tags": (array) an array of tag names formatted as strings,
      "next_send_time": (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
      "schedule_type": (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone,
    },
  ]
}
```

{% endapi %}
