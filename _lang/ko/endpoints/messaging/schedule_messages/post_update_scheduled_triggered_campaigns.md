---
nav_title: "POST: 예약된 API 트리거 캠페인 업데이트"
article_title: "POST: 예약된 API 트리거 캠페인 업데이트"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "이 문서에서는 예약된 API 트리거 캠페인 Braze 엔드포인트 업데이트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 예약된 API 트리거 캠페인 업데이트
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> 이 엔드포인트를 사용하여 대시보드에서 생성된 예약된 API 트리거 캠페인을 업데이트하여 어떤 작업을 트리거하여 메시지를 보낼지 결정할 수 있습니다.

메시지 자체에 템플릿이 지정된 `trigger_properties` 을 전달할 수 있습니다.

이 엔드포인트로 메시지를 보내려면 [API 트리거 캠페인을]({{site.baseurl}}/api/api_campaigns/) 만들 때 생성한 캠페인 ID가 있어야 합니다.

모든 일정은 일정 생성 요청 또는 이전 업데이트 일정 요청에서 제공한 일정을 완전히 덮어씁니다. 예를 들어 원래 일정을 `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` 으로 설정했다가 나중에 `"schedule" : {"time" : "2015-02-20T14:14:47"}` 으로 업데이트하면 이제 사용자의 현지 시각이 아닌 UTC로 지정된 시간에 메시지가 전송됩니다.

예약된 트리거는 전송 예정 시간에 매우 가깝게 또는 그 시간에 업데이트되어 마지막 초의 변경 사항이 타겟팅된 사용자 전체, 일부 또는 전혀에게 적용될 수 있도록 최선을 다해 업데이트됩니다. 원래 일정이 현지 시간을 사용했고 어떤 시간대에서든 원래 시간이 이미 지난 경우에는 업데이트가 적용되지 않습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `campaigns.trigger.schedule.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Required|문자열| [캠페인 식별자]({{site.baseurl}}/api/identifier_types/) 보기|
| `schedule_id` | Required | 문자열 | 업데이트할 `schedule_id` (스케줄을 만들기 위한 응답에서 얻은 값)입니다. |
|`schedule` | 필수 | 객체 | [일정 개체를]({{site.baseurl}}/api/objects_filters/schedule_object/) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
