---
nav_title: "POST: API 트리거 캠페인 예약하기"
article_title: "POST: API 트리거 캠페인 예약하기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 스케줄 API 트리거 캠페인 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# API 트리거 캠페인 예약하기
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/create
{% endapimethod %}

> 이 엔드포인트를 사용하면 대시보드에서 생성한 캠페인 메시지를 API 트리거 전달을 통해 전송할 수 있으며, 어떤 작업을 트리거하여 메시지를 전송할지 결정할 수 있습니다. 

메시지 자체에 템플릿이 지정된 `trigger_properties`를 전달할 수 있습니다.

이 엔드포인트로 메시지를 보내려면 [API 트리거 캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)을 만들 때 생성한 [캠페인 ID]({{site.baseurl}}/api/identifier_types/)가 있어야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b7e61de7-f2c2-49c9-9e46-b85a0aa01bba {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `campaigns.trigger.schedule.create` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='default' category='message endpoints' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the campaign
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "trigger_properties": (optional, object) personalization key-value pairs for all users in this send; see trigger properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```
## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
|`campaign_id`|필수| 문자열| [캠페인 식별자 참조|]({{site.baseurl}}/api/identifier_types/)
| `send_id` | 선택 사항 | 문자열 | [전송 식별자]({{site.baseurl}}/api/identifier_types/) 참조. |
| `recipients` | 선택 사항 | 수신자 개체의 배열 | [수신자 개체]({{site.baseurl}}/api/objects_filters/recipient_object/) 보기. |
| `audience` | 선택 사항 | 연결된 대상 개체 | [연결된 대상]({{site.baseurl}}/api/objects_filters/connected_audience/) 보기. |
|`broadcast`| 선택 사항 | 부울 | 캠페인 또는 캔버스가 타겟팅하는 전체 세그먼트에 메시지를 보낼 때 `broadcast`를 true로 설정해야 합니다. 이 매개변수의 기본값은 false입니다(2017년 8월 31일 기준). <br><br> `broadcast` 을 true로 설정하면 `recipients` 목록을 포함할 수 없습니다. 그러나 이 플래그를 실수로 설정하면 예상보다 많은 대상에게 메시지를 보낼 수 있으므로 `broadcast: true` 을 설정할 때는 주의하세요. |
| `trigger_properties` | 선택 사항 | 개체 | 이 전송의 모든 사용자에 대한 개인화 키-값 페어입니다. [트리거 속성]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)을 참조하세요. |
| `schedule` | 필수 | 일정 개체 | [일정 개체]({{site.baseurl}}/api/objects_filters/schedule_object/) 보기. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "trigger_properties": {}
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
  "trigger_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## 응답

### 성공 응답 예시

```json
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
