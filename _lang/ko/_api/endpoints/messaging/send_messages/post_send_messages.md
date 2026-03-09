---
nav_title: "POST: API만 사용하여 즉시 메시지 보내기"
article_title: "POST: API만 사용하여 즉시 메시지 보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 API 전용 Braze 엔드포인트를 사용하여 즉시 메시지 보내기 기능에 대해 자세히 설명합니다."

---
{% api %}
# API만 사용하여 즉시 메시지 보내기
{% apimethod postcore_endpoint|https://www.braze.com/docs/core_endpoints  %}
/messages/send
{% endapimethod %}

> 이 엔드포인트를 사용하면 Braze API를 사용하여 지정된 사용자에게 즉시 메시지를 보낼 수 있습니다.

세그먼트를 타겟팅하는 경우 요청에 대한 기록이 [개발자 콘솔](https://dashboard.braze.com/app_settings/developer_console/activitylog/)에 저장됩니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

{% multi_lang_include api/payload_size_alert.md %}

{% alert important %}
API 캠페인에 이 엔드포인트를 사용할 경우, 요청이 성공하려면 수신자가 Braze에 이미 존재해야 합니다. 이는  또는`user_aliases`  `external_user_ids`매개변수에서 사용자를 지정할 때 적용됩니다.
{% endalert %}

### API 호출을 통한 신규 사용자 생성

API를 사용하여 전송의 일환으로 사용자를 생성해야 하는 경우 두 가지 옵션이 있습니다:

#### Option 1: 사용한`/users/track`후 보내기

먼저, [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)엔드포인트를 사용하여 사용자를 생성한 후, 데이터가 전파되기를 기다립니다(일반적으로 몇 분 정도 권장됨). 이후 API 전용 전송을 시작합니다. Braze는 데이터 처리 시간을 보장하지 않으므로`/users/track`, 호출 간 충분한 시간을 두지 않을 경우 [경합 조건이]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) 발생할 수 있습니다.

#### Option 2: API 트리거 캠페인 또는 캔버스 사용

[API 트리거 캠페인]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) 또는 [캔버스]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) 워크플로를 사용하십시오. 이 기능은 수신자가 아직 존재하지 않을 경우 생성할 수 있게 해줍니다. 이 옵션은 백엔드 프로세스를 간소화하지만, Braze 대시보드에서 캠페인 또는 캔버스를 구성해야 합니다.


## 필수 조건

이 엔드포인트를 사용하려면 `messages.send` 권한으로 API 키를 생성해야 합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

## Request body

{% alert tip %}
요청을 완료하려면 본문에 [메시징 객체를]({{site.baseurl}}/api/objects_filters/#messaging-objects) 포함해야 합니다.
{% endalert %}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
   // Including 'segment_id' will send to members of that segment
   // Including 'external_user_ids' and/or 'user_aliases' will send to those users
   // Including both will send to the provided users if they are in the segment
   "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if no external_user_ids or aliases are provided,
   "external_user_ids": (optional, array of strings) see external user identifier,
   "user_aliases": (optional, array of user alias object) see user alias,
   "segment_id": (optional, string) see segment identifier,
   "audience": (optional, connected audience object) see connected audience,
   "campaign_id": (optional*, string) *required if you wish to track campaign stats (for example, sends, clicks, bounces, etc). see campaign identifier,
   "send_id": (optional, string) see send identifier,
   "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
   "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
   "messages": {
     "android_push": (optional, android push object),
     "apple_push": (optional, apple push object),
     "content_card": (optional, content card object),
     "email": (optional, email object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "webhook": (optional, webhook object),
     "whats_app": (optional, WhatsApp object),
     "sms": (optional, SMS object)
   }
 }
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`broadcast`| 선택 사항 | 부울 | 전체 세그먼트에 캠페인 또는 캔버스가 타겟팅하는 메시지를 보낼 때 `broadcast`을(를) true로 설정해야 합니다. 이 매개변수는 기본적으로 false로 설정됩니다 (2017년 8월 31일 기준). <br><br> `broadcast`가 true로 설정하면 `recipients` 목록을 포함할 수 없습니다. 그러나 `broadcast: true`을 설정할 때 주의하십시오. 이 플래그를 의도치 않게 설정하면 메시지를 예상보다 더 많은 오디언스에게 보낼 수 있습니다. |
|`external_user_ids` | 선택 사항 | 문자열 배열 | [외부 사용자 ID를]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) 참조하세요. |
|`user_aliases`| 선택 사항 | 사용자 별칭 객체 배열| [사용자 별칭 개체를]({{site.baseurl}}/api/objects_filters/user_alias_object/) 참조하세요. |
|`segment_id `| Optional | 문자열 | [세그먼트 식별자를]({{site.baseurl}}/api/identifier_types/#segment-identifier) 참조하세요. |
|`audience`| 선택 사항 | 연결된 오디언스 객체 | [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/)을 참조하십시오. |
|`campaign_id`| 선택 사항* | 문자열 | 자세한 내용은 [캠페인 식별자를]({{site.baseurl}}/api/identifier_types/#campaign-identifier/) 참조하세요. <br><br>\*Braze 대시보드에서 캠페인 측정기준(예: _발송_, _클릭_ 또는 _반송_)을 추적하려면 필수입니다. |
|`send_id`| Optional | 문자열 | [식별자 보내기]({{site.baseurl}}/api/identifier_types/#send-identifier)을 참조하십시오. |
|`override_frequency_capping`| 선택 사항 | 부울 | 캠페인의 경우 `frequency_capping` 을 무시하고 기본값은 `false` 입니다. |
|`recipient_subscription_state`| Optional | 문자열 | 이를 사용하여 수신 동의한 사용자(`opted_in`), 구독했거나 수신 동의한 사용자(`subscribed`) 또는 구독하지 않은 사용자를 포함한 모든 사용자(`all`)에게만 메시지를 보낼 수 있습니다. <br><br>`all` 사용자를 사용하면 트랜잭션 이메일 메시징에 유용합니다. 기본값은 `subscribed` 입니다. |
|`messages`| 선택 사항 | 메시징 객체 | [사용 가능한 메시징 개체를]({{site.baseurl}}/api/objects_filters/#messaging-objects) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/send' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name": "example_name",
    "alias_label": "example_label"
  },
  "segment_id": "segment_identifier",
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
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "android_push": "(optional, Android Push Object)",
    "apple_push": "(optional, Apple Push Object)",
    "content_card": "(optional, Content Card Object)",
    "email": "(optional, Email Object)",
    "kindle_push": "(optional, Kindle/FireOS Push Object)",
    "web_push": "(optional, Web Push Object)"
  }
}'
```

## 응답 세부 정보

메시지를 보내는 엔드포인트 응답에는 메시지 발송을 다시 참조할 수 있도록 메시지의 `dispatch_id` 주소가 포함됩니다. `dispatch_id` 은 메시지 발송의 ID로, Braze에서 보낸 각 '전송'의 고유 ID를 의미합니다. 자세한 내용은 [디스패치 ID 동작을]({{site.baseurl}}/help/help_articles/data/dispatch_id/) 참조하세요.

{% endapi %}
