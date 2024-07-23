---
nav_title: "GET: Export Canvas Details(캔버스 세부 정보 내보내기)"
article_title: "GET: Export Canvas Details(캔버스 세부 정보 내보내기)"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 캔버스 내보내기 세부 정보 Braze 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# Export Canvas details(캔버스 세부 정보 내보내기)
{% apimethod get %}
/canvas/details
{% endapimethod %}

> 이 엔드포인트를 사용하여 이름, 생성 시간, 현재 상태 등과 같은 캔버스에 대한 메타데이터를 내보낼 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5188873c-13a3-4aaf-a54b-9fa1daeac5f8 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `canvas.details`가 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | 필수 | 문자열 | [캔버스 API 식별자]({{site.baseurl}}/api/identifier_types/) 참고 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/details?canvas_id={{canvas_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답

{% alert note %}
모든 캔버스 단계에는 `{name, next_step_id}` 데이터 배열인 `next_paths` 필드가 있습니다. 전체 단계 및 메시지 단계의 경우 필드가 `next_step_ids` 표시되지만 다른 캔버스 흐름 단계에 대한 데이터는 포함되지 않습니다.
{% endalert %}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "created_at": (string) the date created as ISO 8601 date,
  "updated_at": (string) the date updated as ISO 8601 date,
  "name": (string) the Canvas name,
  "description": (string) the Canvas description,
  "archived": (boolean) whether this Canvas is archived,
  "draft": (boolean) whether this Canvas is a draft,
  "schedule_type": (string) the type of scheduling action,
  "first_entry": (string) the date of first entry as ISO 8601 date,
  "last_entry": (string) the date of last entry as ISO 8601 date,
  "channels": (array of strings) step channels used with Canvas,
  "variants": [
    {
      "name": (string) the name of variant,
      "id": (string) the API identifier of the variant,
      "first_step_ids": (array of strings) the API identifiers for first steps in variant,
      "first_step_id": (string) the API identifier of first step in variant (deprecated in November 2017, only included if the variant has only one first step)
    },
    ... (more variations)
  ],
  "tags": (array of strings) the tag names associated with the Canvas,
  "teams" : (array) the names of the Teams associated with the Canvas,
  "steps": [
    {
      "name": (string) the name of step,
      "type" (string) the type of Canvas component,
      "id": (string) the API identifier of the step,
      "next_step_ids": (array of strings) IDs for next steps that are full steps or Message steps,
      "next_paths": { (array of objects)
      // for Decision Splits, this property should evaluate to "Yes" or "No"
      // for Audience Path and Action Paths, this property should evaluate to the group name
      // for Experiment Paths, this property should evaluate to the path name
      // for other steps, this property should evaluate to "null"
        "name": (string) name the name of step,
        "next_step_id": (string) IDs for next steps that are full steps or Message steps,
        }
      "channels": (array of strings) the channels used in step,
      "messages": {
          "message_variation_id": (string) {  // <=This is the actual id
              "channel": (string) the channel type of the message (for example, "email"),
              // channel-specific fields for this message, see Campaign Details endpoint API Response for example message responses
          }
      }
    },
    ... (more steps)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
