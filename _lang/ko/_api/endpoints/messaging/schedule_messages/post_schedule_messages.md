---
nav_title: "POST: 예약된 메시지 만들기"
article_title: "POST: 예약 메시지 만들기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 예약된 메시지 만들기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 예약된 메시지 만들기
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/create
{% endapimethod %}

> 이 엔드포인트를 사용하여 캠페인, 캔버스 또는 기타 메시지를 지정된 시간에 전송하도록 예약하고 해당 메시지를 참조하여 업데이트할 수 있는 식별자를 제공합니다.

세그먼트를 타겟팅하는 경우 예약된 모든 메시지가 전송된 후 요청 기록이 [개발자 콘솔에](https://dashboard.braze.com/app_settings/developer_console/activitylog/) 저장됩니다.

{% alert tip %}
지정된 사용자에게 즉시 메시지를 보내려면 [`/messages/send` 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) 대신 사용하세요.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `messages.schedule.create` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
  // Including 'segment_id' will send to members of that segment
  // Including 'external_user_ids' and/or 'user_aliases' will send to those users
  // Including both a Segment and users will send to the provided users if they are in the segment
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
  "external_user_ids": (optional, array of strings) see external user identifier,
  "user_aliases": (optional, array of user alias object) see user alias,
  "audience": (optional, connected audience object) see connected audience,
  "campaign_id": (optional, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "override_messaging_limits": (optional, bool) ignore frequency capping rules, defaults to false,
  "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  },
  "messages": {
    "apple_push": (optional, apple push object),
    "android_push": (optional, android push object),
    "kindle_push": (optional, kindle/fireOS push object),
    "web_push": (optional, web push object),
    "email": (optional, email object),
    "webhook": (optional, webhook object),
    "content_card": (optional, content card object),
    "sms": (optional, SMS object)
  }
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`broadcast`| 선택 사항 | 부울 | 전체 세그먼트에 캠페인 또는 캔버스가 타겟팅하는 메시지를 보낼 때 `broadcast`을(를) true로 설정해야 합니다. 이 매개 변수의 기본값은 `false` 입니다. <br><br> `broadcast` 이 `true` 으로 설정된 경우 수신자 목록을 포함할 수 없습니다. 그러나 이 플래그를 실수로 설정하면 예상보다 많은 대상에게 메시지를 보낼 수 있으므로 `broadcast: true` 을 설정할 때는 주의하세요. |
| `external_user_ids` | 선택 사항 | 문자열 배열 | [외부 사용자 식별자를]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) 참조하세요. |
| `user_aliases` | 선택 사항 | 사용자 별칭 객체 배열 | [사용자 별칭 개체를]({{site.baseurl}}/api/objects_filters/user_alias_object/) 참조하세요. |
| `audience` | 선택 사항 | 연결된 오디언스 객체 | [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/)을 참조하십시오. |
| `segment_id` | Optional | 문자열 | [세그먼트 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하세요. |
| `campaign_id`|Optional|문자열| [캠페인 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하세요. |
| `send_id` | Optional | 문자열 | [식별자 보내기]({{site.baseurl}}/api/identifier_types/)을 참조하십시오. |
| `override_messaging_limits` | 선택 사항 | 부울 | 캠페인에 대한 빈도 제한 무시, 기본값은 거짓으로 설정됨 |
|`recipient_subscription_state`| Optional | 문자열 | 이를 사용하여 수신 동의한 사용자(`opted_in`), 구독했거나 수신 동의한 사용자(`subscribed`) 또는 구독하지 않은 사용자를 포함한 모든 사용자(`all`)에게만 메시지를 보낼 수 있습니다. <br><br>`all` 사용자를 사용하면 트랜잭션 이메일 메시징에 유용합니다. 기본값은 `subscribed` 입니다. |
| `schedule` | 필수 | 스케줄 객체 | [일정 개체]({{site.baseurl}}/api/objects_filters/schedule_object/) 보기 |
| `messages` | 선택 사항 | 메시징 개체 | [사용 가능한 메시징 개체를]({{site.baseurl}}/api/objects_filters/#messaging-objects) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name" : "example_name",
    "alias_label" : "example_label"
  },
  "segment_id": "segment_identifiers",
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
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": true
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}'
```

## 응답

### 성공 응답의 예

```json
{
    "dispatch_id": (string) the dispatch identifier,
    "schedule_id": (string) the schedule identifier,
    "message": "success"
}
```

{% endapi %}
