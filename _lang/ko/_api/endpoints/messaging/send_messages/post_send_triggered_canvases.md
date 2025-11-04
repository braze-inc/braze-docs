---
nav_title: "POST: API 트리거 배달을 사용하여 캔버스 메시지 보내기"
article_title: "POST: API 트리거 배달을 사용하여 캔버스 메시지 보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 API 트리거 배달 Braze 엔드포인트를 사용한 캔버스 보내기에 대한 자세한 내용을 설명합니다."

---
{% api %}
# API 트리거 배달을 사용하여 캔버스 메시지 보내기
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> 이 엔드포인트를 사용하여 API 트리거 배달을 통해 캔버스 메시지를 전송할 수 있습니다.

API 트리거 전송을 사용하면 메시지 콘텐츠를 Braze 대시보드에 저장하는 동시에 API를 사용하여 메시지를 언제, 누구에게 보낼지 지정할 수 있습니다.

이 엔드포인트로 메시지를 보내려면 먼저 [캔버스 ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (캔버스를 만들 때 생성됨)가 있어야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `canvas.trigger.send` 권한으로 API 키를 생성해야 합니다.

## 사용량 제한

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
  "segment_id": (optional, string) see segment identifier,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent `canvas_entry_properties`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }],
    ...
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| 필수 | 문자열 | [캔버스 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하세요. |
|`canvas_entry_properties`| 선택 사항 | 객체 | 여기에는 [캔버스 항목 속성이]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) 포함됩니다. 개인화 키-값 쌍은 이 요청의 모든 사용자에게 적용됩니다. 캔버스 항목 속성 객체의 최대 크기 제한은 50KB입니다. <br><br>**참고:** [캔버스 컨텍스트 얼리 액세스에]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/) 참여하는 경우 이 매개 변수는 `context` 이며 캔버스 항목 속성을 포함합니다. |
|`broadcast`| 선택 사항 | 부울 | 전체 세그먼트에 캠페인 또는 캔버스가 타겟팅하는 메시지를 보낼 때 `broadcast`을(를) true로 설정해야 합니다. 이 매개변수는 기본적으로 false로 설정됩니다 (2017년 8월 31일 기준). <br><br> `broadcast`가 true로 설정하면 `recipients` 목록을 포함할 수 없습니다. 그러나 이 플래그를 실수로 설정하면 예상보다 많은 대상에게 메시지를 보낼 수 있으므로 `broadcast: true` 을 설정할 때는 주의하세요. |
|`segment_id `| 선택 사항 | 문자열 | [세그먼트 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하세요. |
|`audience`| 선택 사항| 연결된 대상 개체 | [연결된 오디언스를]({{site.baseurl}}/api/objects_filters/connected_audience/) 참조하세요. |
|`recipients`| 선택 사항 | 배열 | [받는 사람 개체를]({{site.baseurl}}/api/objects_filters/recipient_object/) 참조하세요. <br><br>제공하지 않고 `broadcast` 이 true로 설정되어 있으면 캔버스가 타겟팅하는 전체 세그먼트에 메시지가 전송됩니다.<br><br> `recipients` 배열에는 최대 50개의 객체가 포함될 수 있으며, 각 객체에는 하나의 `external_user_id` 문자열과 `canvas_entry_properties` 객체가 포함됩니다. 이 통화에는 `external_user_id`, `user_alias` 또는 `email` 이 필요합니다. 요청은 하나만 지정해야 합니다. <br><br>`email` 이 식별자인 경우 수신자 객체에 다음을 포함해야 합니다. [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) 를 수신자 객체에 포함해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
`recipients` 매개변수의 경우 `send_to_existing_only` 이 `true` 일 때 Braze는 기존 사용자에게만 메시지를 보냅니다. 그러나 이 플래그는 사용자 별칭과 함께 사용할 수 없습니다. <br><br>`send_to_existing_only`가 `false`인 경우 속성 객체를 포함해야 합니다. `send_to_existing_only` 이 `false` **이고** 지정된 `id` 을 가진 사용자가 존재하지 않는 경우, Braze는 메시지를 보내기 전에 해당 ID와 속성을 가진 사용자를 생성합니다.
{% endalert %}

서버 간 호출에 API를 사용하는 고객은 방화벽 뒤에 있는 경우 적절한 API URL을 허용 목록에 추가해야 할 수 있습니다.

{% alert note %}
API 호출에 특정 사용자와 대시보드의 대상 세그먼트를 모두 포함하면 API 호출에 모두 포함되고 세그먼트 필터에 적합한 사용자 프로필에 메시지가 전송됩니다.
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
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## 응답 세부 정보

메시지를 보내는 엔드포인트 응답에는 메시지 발송을 다시 참조할 수 있도록 메시지의 `dispatch_id` 주소가 포함됩니다. `dispatch_id` 은 메시지 발송의 ID(Braze 플랫폼에서 전송된 각 "전송"에 대한 고유 ID)입니다. 자세한 내용은 [디스패치 ID 동작에서]({{site.baseurl}}/help/help_articles/data/dispatch_id/) 확인하세요.

### 성공 응답의 예

`201` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 캔버스가 보관, 중지 또는 일시 중지된 경우 캔버스는 이 엔드포인트를 통해 전송되지 않습니다.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

캔버스가 보관된 경우 `notice` 메시지가 표시됩니다: "캔버스가 보관됩니다. 캔버스를 보관 해제하여 트리거 요청이 적용되도록 하세요." 캔버스가 활성화되어 있지 않으면 `notice` 메시지가 표시됩니다: "캔버스가 일시 중지되었습니다. 캔버스를 다시 시작하여 트리거 요청이 적용되도록 하세요."

요청에 치명적인 오류가 발생하면 오류 코드와 설명은 오류 [및 응답을]({{site.baseurl}}/api/errors/#fatal-errors) 참조하세요.

## 캔버스용 속성 개체

메시징 개체 `attributes` 를 사용하여 `canvas/trigger/send` 엔드포인트를 사용하여 API 트리거 캔버스를 보내기 전에 사용자에 대한 속성 및 값을 추가, 생성 또는 업데이트하세요. 이 API 호출은 캔버스를 처리하고 전송하기 전에 사용자 속성 개체를 처리합니다. 이렇게 하면 [경쟁 조건으로]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) 인한 문제 발생 위험을 최소화할 수 있습니다. 그러나 기본적으로 구독 그룹은 이 방법으로 업데이트할 수 없습니다.

{% alert note %}
이 엔드포인트의 캠페인 버전을 찾고 계신가요? [API 트리거 배달을 사용하여 캠페인 메시지 보내기를]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) 확인하세요.
{% endalert %}

{% endapi %}
