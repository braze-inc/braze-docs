---
nav_title: "POST: API 트리거 전송을 통해 캠페인 보내기"
article_title: "POST: API 트리거 전송을 통해 캠페인 보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 API 트리거 전달 Braze 엔드포인트를 통한 캠페인 전송에 대한 자세한 내용을 설명합니다."

---
{% api %}
# API 트리거 전송을 통해 캠페인 메시지 보내기
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> 이 엔드포인트를 사용하면 API 트리거 배달을 통해 지정된 사용자에게 즉각적인 일회성 메시지를 보낼 수 있습니다. 

API 트리거 전송을 사용하면 메시지 콘텐츠를 Braze 대시보드 내에 보관하는 동시에 API를 통해 메시지 전송 시기와 수신자를 지정할 수 있습니다.

세그먼트를 타겟팅하는 경우 요청에 대한 기록이 [개발자 콘솔](https://dashboard.braze.com/app_settings/developer_console/activitylog/)에 저장됩니다. 이 엔드포인트로 메시지를 보내려면 [API 트리거 캠페인]({{site.baseurl}}/api/api_campaigns/)을 구축할 때 생성한 [캠페인 ID](https://www.braze.com/docs/api/identifier_types/)가 있어야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `campaigns.trigger.send` 권한으로 API 키를 생성해야 합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message will send to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
  ]
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
|`campaign_id`[|필수|String|캠페인 식별자]({{site.baseurl}}/api/identifier_types/) 참조. |
|`send_id`| 선택 사항 | 문자열 | [전송 식별자]({{site.baseurl}}/api/identifier_types/) 참조. |
|`trigger_properties`| 선택 사항 | 개체 | [트리거 속성]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) 보기. 이 요청의 모든 사용자에게 적용될 개인화 키-값 쌍입니다. |
|`broadcast`| 선택 사항 | 부울 | 캠페인 또는 캔버스가 타겟팅하는 전체 세그먼트에 메시지를 보낼 때 `broadcast`를 true로 설정해야 합니다. 이 매개변수의 기본값은 false입니다(2017년 8월 31일 기준). <br><br> `broadcast` 을 true로 설정하면 `recipients` 목록을 포함할 수 없습니다. 그러나 이 플래그를 실수로 설정하면 예상보다 많은 대상에게 메시지를 보낼 수 있으므로 `broadcast: true` 을 설정할 때는 주의하세요. |
|`audience`| 선택 사항 | 연결된 대상 개체| [연결된 대상]({{site.baseurl}}/api/objects_filters/connected_audience/) 보기. |
|`recipients`| 선택 사항 | 배열 | [수신자 개체]({{site.baseurl}}/api/objects_filters/recipient_object/) 보기.<br><br>`send_to_existing_only`가 `false`인 경우 속성 객체를 포함해야 합니다.<br><br>`recipients` 을 제공하지 않고 `broadcast` 을 true로 설정하면 캠페인이 타겟팅하는 전체 세그먼트에 메시지가 전송됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

- 수신자 배열에는 최대 50개의 객체가 포함될 수 있으며, 각 객체에는 단일 `external_user_id` 문자열과 `trigger_properties` 객체가 포함됩니다.
- `send_to_existing_only`가 `true`일 경우, Braze는 기존 사용자에게만 메시지를 보냅니다. 그러나 이 플래그는 사용자 별칭과 함께 사용할 수 없습니다. 
- `send_to_existing_only`가 `false`인 경우 속성을 포함해야 합니다. Braze는 메시지를 보내기 전에 `id` 및 속성을 가진 사용자를 생성합니다.

사용자의 구독 그룹 상태는 `attributes` 객체 내에 `subscription_groups` 매개변수를 포함시켜 업데이트할 수 있습니다. 자세한 내용은 [사용자 속성 개체를]({{site.baseurl}}/api/objects_filters/user_attributes_object) 참조하세요.

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
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
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ]
}'
```

## 응답 세부 정보

메시지를 보내는 엔드포인트 응답에는 메시지 발송을 다시 참조할 수 있도록 메시지의 `dispatch_id`가 포함됩니다. `dispatch_id`는 메시지 발송의 ID로, Braze에서 전송되는 각 전송의 고유 ID입니다. 이 엔드포인트를 사용하면 일괄 처리된 배치된 사용자 집합에 대해 단일 `dispatch_id`를 받게 됩니다. `dispatch_id`에 대한 자세한 내용은 [디스패치 ID 동작]({{site.baseurl}}/help/help_articles/data/dispatch_id/)에 대한 설명서를 참조하세요.

## 보내기 엔드포인트 만들기

**캠페인에서 속성 개체 사용**

Braze에는 API 트리거 캠페인을 보내기 전에 사용자에 대한 속성 및 값을 추가, 생성 또는 업데이트할 수 있는 `attributes`라는 메시징 객체가 있습니다. 이 API 호출로 `campaign/trigger/send` 엔드포인트를 사용하면 캠페인을 처리하고 전송하기 전에 사용자 속성 객체를 처리합니다. 이렇게 하면 [경쟁 조건으로]({{site.baseurl}}/help/best_practices/race_conditions/) 인한 문제 발생 위험을 최소화할 수 있습니다. 

{% alert important %}
이 엔드포인트의 캔버스 버전을 찾고 계신가요? [API 트리거 배달을 통한 캔버스 메시지 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint)를 확인하세요.
{% endalert %}

{% endapi %}
