---
nav_title: "POST: API 트리거 캔버스 예약하기"
article_title: "POST: API 트리거 캔버스 예약하기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 스케줄 API로 트리거되는 캔버스 브레이즈 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# API 트리거 캔버스 예약하기
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/create
{% endapimethod %}

> 이 엔드포인트를 사용하면 API 트리거 배달을 통해 Canvas 메시지를 예약하여 어떤 작업을 트리거하여 메시지를 전송할지 결정할 수 있습니다.

Canvas의 첫 번째 단계에서 전송되는 메시지에 템플릿이 지정된 `canvas_entry_properties` 을 전달할 수 있습니다.

이 엔드포인트로 메시지를 보내려면 캔버스를 만들 때 생성한 [캔버스 ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)가 있어야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4bc75890-b807-405d-b226-5aca284e6b7d {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `canvas.trigger.schedule.create` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the
  // Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the Canvas
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for the first step for all users in this send; see trigger properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Required|문자열| [캔버스 식별자]({{site.baseurl}}/api/identifier_types/)를 참조하세요. |
| `recipients` | 선택 사항 | 수신자 객체 배열 | 수신자 객체를 참조하십시오. |
| `audience` | 선택 사항 | 연결된 오디언스 객체 | [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/)을 참조하십시오. |
|`broadcast`| 선택 사항 | 부울 | 전체 세그먼트에 캠페인 또는 캔버스가 타겟팅하는 메시지를 보낼 때 `broadcast`을(를) true로 설정해야 합니다. 이 매개변수는 기본적으로 false로 설정됩니다 (2017년 8월 31일 기준). <br><br> `broadcast`가 true로 설정하면 `recipients` 목록을 포함할 수 없습니다. 그러나 `broadcast: true`을 설정할 때 주의하십시오. 이 플래그를 의도치 않게 설정하면 메시지를 예상보다 더 많은 오디언스에게 보낼 수 있습니다. |
| `canvas_entry_properties` | 선택 사항 | 객체 | 이 전송의 모든 사용자에 대한 개인화 키-값 쌍입니다. [캔버스 항목 속성 개체를]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object) 참조하십시오. |
| `schedule` | 필수 | 스케줄 객체 | [일정 개체를]({{site.baseurl}}/api/objects_filters/schedule_object/) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties": {}
    }
  ],
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "broadcast": false,
  "canvas_entry_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## 응답

### 성공 응답의 예

```
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
{
    "dispatch_id": "dispatch_identifier",
    "schedule_id": "schedule_identifier",
    "message": "success"
}
```

{% endapi %}
