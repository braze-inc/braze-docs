---
nav_title: "POST: API 트리거 전달을 통해 캔버스 메시지 보내기"
article_title: "POST: API 트리거 전달을 통해 캔버스 메시지 보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 API 트리거 전달 Braze 엔드포인트를 통한 캔버스 보내기에 대한 자세한 내용을 설명합니다."

---
{% api %}
# API 트리거 전달을 통해 캔버스 메시지 보내기
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> 이 엔드포인트를 사용하여 API 트리거 전달을 통해 캔버스 메시지를 전송할 수 있습니다. 

API 트리거 전달을 사용하면 메시지 콘텐츠를 Braze 대시보드에 저장하는 동시에 API를 통해 메시지를 언제, 누구에게 보낼지 지정할 수 있습니다.

이 엔드포인트로 메시지를 보내려면 먼저 [캔버스 ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (캔버스를 만들 때 생성됨)가 있어야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `canvas.trigger.send` 권한으로 API 키를 생성해야 합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent `canvas_entry_properties`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }],
    ...
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
|`canvas_id`| 필수 | 문자열 | [캔버스 식별자]({{site.baseurl}}/api/identifier_types/) 참조. |
|`canvas_entry_properties`| 선택 사항 | 개체 | [캔버스 항목 속성]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) 참조. 이 요청의 모든 사용자에게 적용될 개인화 키-값 쌍입니다. 캔버스 항목 속성 개체의 최대 크기 제한은 50KB입니다. |
|`broadcast`| 선택 사항 | 부울 | 캠페인 또는 캔버스가 타겟팅하는 전체 세그먼트에 메시지를 보낼 때 `broadcast` 을 true로 설정해야 합니다. 이 매개변수의 기본값은 false입니다(2017년 8월 31일 기준). <br><br> `broadcast` 을 true로 설정하면 `recipients` 목록을 포함할 수 없습니다. 그러나 이 플래그를 실수로 설정하면 예상보다 많은 대상에게 메시지를 보낼 수 있으므로 `broadcast: true` 을 설정할 때는 주의하세요. |
|`audience`| 선택 사항| 연결된 대상 개체 | [연결된]({{site.baseurl}}/api/objects_filters/connected_audience/) 오디언스를 참조하세요. |
|`recipients`| 선택 사항 | 배열 | [수신자 개체]({{site.baseurl}}/api/objects_filters/recipient_object/) 참조. 제공하지 않고 `broadcast`가 true로 설정되어 있으면 캔버스가 타겟팅하는 전체 세그먼트에 메시지가 전송됩니다.<br><br> `recipients` 배열에는 최대 50개의 객체가 포함될 수 있으며, 각 객체에는 하나의 `external_user_id` 문자열과 `canvas_entry_properties` 객체가 포함됩니다. 이 통화에는 `external_user_id` 또는 `user_alias` 이메일 주소가 필요합니다. 요청은 하나만 지정해야 합니다. <br><br> `send_to_existing_only`가 `true`인 경우, Braze는 기존 사용자에게만 메시지를 보내지만 이 플래그는 사용자 별칭과 함께 사용할 수 없습니다. `send_to_existing_only`가 `false`이고 지정된 `id`를 가진 사용자가 존재하지 않는 경우, Braze는 메시지를 보내기 전에 해당 ID와 속성을 가진 사용자를 생성합니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

서버 간 호출에 API를 사용하는 고객은 방화벽 뒤에 있는 경우 적절한 API URL을 허용 목록에 추가해야 할 수 있습니다.

{% alert note %}
API 호출에 특정 사용자와 대시보드의 대상 세그먼트를 모두 포함하면 API 호출에 모두 포함되고 세그먼트 필터에 적합한 고객 프로필에 메시지가 전송됩니다.
{% endalert %}

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99},
  "broadcast": false,
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
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "user_identifier",
      "trigger_properties": "",
      "canvas_entry_properties": "",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## 응답 세부 정보

메시지를 보내는 엔드포인트 응답에는 메시지 발송을 다시 참조할 수 있도록 메시지의 `dispatch_id`가 포함됩니다. `dispatch_id`는 메시지 발송의 ID(Braze 플랫폼에서 전송된 각 "전송"에 대한 고유 ID)입니다. 자세한 내용은 [디스패치 ID 동작에서]({{site.baseurl}}/help/help_articles/data/dispatch_id/) 확인하세요.

## 보내기 엔드포인트 만들기

**캔버스에서 속성 개체 사용**

Braze에는 `Attributes`라는 메시징 개체가 있는데, 이 API 호출은 캔버스를 처리하고 전송하기 전에 사용자 속성 개체를 처리하므로 `canvas/trigger/send` 엔드포인트를 사용하여 API 트리거 캔버스를 보내기 전에 사용자에 대한 속성 및 값을 추가, 생성 또는 업데이트할 수 있습니다. 이렇게 하면 [경쟁 조건으로]({{site.baseurl}}/help/best_practices/race_conditions/) 인한 문제 발생 위험을 최소화할 수 있습니다.

{% alert important %}
이 엔드포인트의 캠페인 버전을 찾고 계신가요? [API 트리거 전달을 통해 캠페인 메시지 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)를 확인하세요.
{% endalert %}

{% endapi %}

