---
nav_title: "POST: API 트리거된 전달을 사용하여 캠페인을 전송하십시오."
article_title: "POST: API 트리거 전송을 사용하여 캠페인 보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 API 트리거 배달 Braze 엔드포인트를 사용하여 캠페인을 보내는 방법에 대해 자세히 설명합니다."

---
{% api %}
# API 트리거 전송을 사용하여 캠페인 메시지 보내기
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> 이 엔드포인트를 사용하면 API 트리거 배달을 사용하여 지정된 사용자에게 즉각적인 일회성 메시지를 보낼 수 있습니다.

API 트리거 전송을 사용하면 메시지 콘텐츠를 Braze 대시보드 내에 보관하면서 API를 사용하여 메시지 전송 시기와 수신자를 지정할 수 있습니다.

세그먼트를 타겟팅하는 경우, 요청 기록이 [개발자 콘솔](https://dashboard.braze.com/app_settings/developer_console/activitylog/)에 저장됩니다. 이 엔드포인트로 메시지를 보내려면 [API 트리거 캠페인]({{site.baseurl}}/api/api_campaigns/)을 구축할 때 생성한 [캠페인 ID](https://www.braze.com/docs/api/identifier_types/)가 있어야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `campaigns.trigger.send` 권한으로 API 키를 생성해야 합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Required|문자열|[캠페인 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하세요. |
|`send_id`| Optional | 문자열 | [식별자 보내기]({{site.baseurl}}/api/identifier_types/)을 참조하십시오. |
|`trigger_properties`| 선택 사항 | 객체 | 트리거 속성을 참조하십시오. 개인화 키-값 쌍은 이 요청의 모든 사용자에게 적용됩니다. |
|`broadcast`| 선택 사항 | 부울 | Braze 대시보드에서 캠페인의 타겟 오디언스으로 구성된 전체 세그먼트에 메시지를 전송할 때 `broadcast`을(true)로 설정해야 합니다. 이 매개변수는 기본적으로 false로 설정됩니다 (2017년 8월 31일 기준). <br><br> `broadcast`가 true로 설정하면 `recipients` 목록을 포함할 수 없습니다. 그러나 이 플래그를 실수로 설정하면 예상보다 많은 대상에게 메시지를 보낼 수 있으므로 `broadcast: true` 을 설정할 때는 주의하세요. |
|`audience`| 선택 사항 | 연결된 오디언스 객체| [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/)을 참조하십시오. `audience`를 포함하면, 메시지는 커스텀 속성 및 구독 상태와 같은 정의된 필터와 일치하는 사용자에게만 전송됩니다. |
|`recipients`| 선택 사항 | 배열 | 수신자 객체를 참조하십시오.<br><br>`send_to_existing_only`가 `false`인 경우 속성 객체를 포함해야 합니다.<br><br>`recipients`이 제공되지 않고 `broadcast`가(true)로 설정된 경우, 메시지는 Braze 대시보드에서 캠페인의 타겟 오디언스로 구성된 전체 세그먼트에 전송됩니다. <br><br> `email` 이 식별자인 경우 수신자 객체에 다음을 포함해야 합니다. [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) 를 수신자 객체에 포함해야 합니다. |
|`attachments`| 선택 사항 | 배열 | `broadcast` 이 true로 설정되어 있으면 `attachments` 목록은 포함할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

- 수신자 배열에는 최대 50개의 개체가 포함될 수 있으며, 각 개체에는 단일 `external_user_id` 문자열과 `trigger_properties` 개체가 포함됩니다.
- `send_to_existing_only`이 `true`(기본값)일 때, Braze는 메시지를 기존 사용자에게만 전송합니다. `external_user_id`이 기존 사용자와 일치하지 않으면, API는 여전히 `201` 성공 응답을 반환하지만, 전송은 내부적으로 `Unknown External User ID` 결과로 취소되며 Currents 이벤트는 생성되지 않습니다. `false`으로 설정되고 속성 객체가 제공되면, Braze는 사용자가 존재하지 않을 경우 새 사용자를 생성합니다. `send_to_existing_only`을 `false`로 설정하는 것은 사용자 별칭에 대해 지원되지 않으며, 새 별칭 전용 사용자는 이 엔드포인트를 통해 생성할 수 없습니다. 별칭 전용 사용자에게 전송하려면, 사용자가 이미 Braze에 존재해야 합니다.

사용자의 구독 그룹 상태는 `attributes` 객체 내에 `subscription_groups` 매개변수를 포함하여 업데이트할 수 있습니다. 자세한 내용은 [사용자 속성 개체]({{site.baseurl}}/api/objects_filters/user_attributes_object)를 참조하십시오.

{% alert note %}
이 엔드포인트에 대해 `segment_id` 매개변수는 지원되지 않습니다. 세그먼트를 타겟팅하려면, Braze 대시보드에서 캠페인의 타겟 오디언스 설정에서 세그먼트를 구성하고 `"broadcast": true`을 사용하거나, [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/) 필터와 함께 `audience` 매개변수를 사용하십시오.
{% endalert %}

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
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## 응답 세부 정보

메시지 전송 엔드포인트 응답에는 메시지의 `dispatch_id`이 포함되어 있어 메시지 전송을 참조할 수 있습니다. `dispatch_id` 은 메시지 발송의 ID로, Braze에서 전송되는 각 전송의 고유 ID입니다. 이 엔드포인트를 사용하면 전체 배치된 사용자 집합에 대해 단일 `dispatch_id` 을 받게 됩니다. 자세한 내용은 `dispatch_id` 에서 [디스패치 ID 동작에]({{site.baseurl}}/help/help_articles/data/dispatch_id/) 대한 문서를 참조하세요.

요청에 치명적인 오류가 발생하면 오류 코드와 설명은 오류 [및 응답을]({{site.baseurl}}/api/errors/#fatal-errors) 참조하세요.

## 캠페인용 속성 개체

Braze에는 `attributes`이라는 메시징 객체가 있어, API 트리거된 캠페인을 전송하기 전에 사용자에 대한 속성과 값을 추가, 생성 또는 업데이트할 수 있습니다. 이 API 호출이 사용자 속성 객체를 처리한 후 캠페인을 처리하고 전송하기 위해 `campaign/trigger/send` 엔드포인트를 사용합니다. 이것은 [경쟁 조건]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/)으로 인해 발생할 수 있는 문제의 위험을 최소화하는 데 도움이 됩니다.

{% alert tip %}
이 엔드포인트의 캔버스 버전을 찾고 있습니까? [API 트리거 배달을 사용하여 캔버스 메시지 보내기를]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint) 확인하세요.
{% endalert %}

{% endapi %}
