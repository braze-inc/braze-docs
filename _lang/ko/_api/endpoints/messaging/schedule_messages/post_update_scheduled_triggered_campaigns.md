---
nav_title: "POST: 예약된 API 트리거 캠페인 업데이트"
article_title: "POST: 예약된 API 트리거 캠페인 업데이트"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "이 문서에서는 예약된 API 트리거 캠페인 업데이트 Braze 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 예약된 API 트리거 캠페인 업데이트
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> 이 엔드포인트를 사용하여 대시보드에서 생성된 예약된 API 트리거 캠페인을 업데이트하여 메시지 전송을 트리거해야 하는 작업을 결정할 수 있습니다.

템플릿 템플릿이 메시지 자체에 `trigger_properties`를 전달될 수 있습니다.

이 엔드포인트를 사용하여 메시지를 보내려면 [API 트리거 캠페인]({{site.baseurl}}/api/api_campaigns/)을 빌드할 때 생성된 캠페인 ID가 있어야 합니다.

모든 일정은 일정 만들기 요청 또는 이전 업데이트 일정 요청에서 제공한 일정을 완전히 덮어씁니다. 예를 들어, 원래 `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}`를 제공한 다음 업데이트에서 `"schedule" : {"time" : "2015-02-20T14:14:47"}`를 제공하는 경우 이제 사용자의 현지 시간이 아닌 UTC로 제공된 시간에 메시지가 전송됩니다. 전송 예정 시간에 매우 인접하거나 전송되어야 하는 시간 동안 업데이트되된 예약된 트리거는 최선의 노력으로 업데이트되므로 마지막 순간에 변경 사항이 대상 사용자 전체, 일부 또는 전혀 적용되지 않을 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## 필수 구성 요소

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

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|필수|문자열| [캠페인 식별자]({{site.baseurl}}/api/identifier_types/) |
| `schedule_id` | 필수 | 문자열 | 업데이트할 `schedule_id`(일정을 만들기 위한 응답에서 가져옴). |
|`schedule` | 필수 | 객체 | [스케줄 객체]({{site.baseurl}}/api/objects_filters/schedule_object/)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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
