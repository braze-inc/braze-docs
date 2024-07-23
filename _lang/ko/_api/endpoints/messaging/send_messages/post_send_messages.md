---
nav_title: "POST: API를 통해서만 즉시 메시지 보내기"
article_title: "POST: API를 통해서만 즉시 메시지 보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 API 전용 Braze 엔드포인트를 통해 즉시 메시지 보내기 기능에 대해 자세히 설명합니다."

---
{% api %}
# API를 통해서만 즉시 메시지 보내기
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/send
{% endapimethod %}

> 이 엔드포인트를 사용하면 Braze API를 통해 지정된 사용자에게 즉시 메시지를 보낼 수 있습니다. 

요청을 완료하려면 메시징 객체를 본문에 포함시켜야 합니다.

세그먼트를 타겟팅하는 경우 요청에 대한 기록이 [개발자 콘솔](https://dashboard.braze.com/app_settings/developer_console/activitylog/)에 저장됩니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `messages.send` 권한으로 API 키를 생성해야 합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

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
     "apple_push": (optional, apple push object),
     "android_push": (optional, android push object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "email": (optional, email object),
     "webhook": (optional, webhook object),
     "content_card": (optional, content card object),
     "sms": (optional, SMS object),
     "whats_app": (optional, WhatsApp object)
   }
 }
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
|`broadcast`| 선택 사항 | 부울 | 캠페인 또는 캔버스가 타겟팅하는 전체 세그먼트에 메시지를 보낼 때 `broadcast` 을 true로 설정해야 합니다. 이 매개변수의 기본값은 false입니다(2017년 8월 31일 기준). <br><br> `broadcast` 을 true로 설정하면 `recipients` 목록을 포함할 수 없습니다. 그러나 이 플래그를 실수로 설정하면 예상보다 많은 대상에게 메시지를 보낼 수 있으므로 `broadcast: true` 을 설정할 때는 주의하세요. |
|`external_user_ids` | 선택 사항 | 문자열 배열 | [외부 사용자 ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) 참조. |
|`user_aliases`| 선택 사항 | 사용자 별칭 개체의 배열| [사용자 별칭]({{site.baseurl}}/api/objects_filters/user_alias_object/) 개체를 참조하세요. |
|`segment_id `| 선택 사항 | 문자열 | [세그먼트 식별자]({{site.baseurl}}/api/identifier_types/) 참조. |
|`audience`| 선택 사항 | 연결된 대상 개체 | [연결된 대상]({{site.baseurl}}/api/objects_filters/connected_audience/) 보기. |
|`campaign_id`| 선택 사항* | 문자열 | 자세한 내용은 [캠페인 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하세요. <br><br>\*Braze 대시보드에서 캠페인 통계(예: 전송, 클릭, 바운스 등)를 추적하려는 경우 필수입니다. |
|`send_id`| 선택 사항 | 문자열 | [전송 식별자]({{site.baseurl}}/api/identifier_types/) 참조 |
|`override_frequency_capping`| 선택 사항 | 부울 | 캠페인에 대해 `frequency_capping` 무시, 기본값은 `false`입니다. |
|`recipient_subscription_state`| 선택 사항 | 문자열 | 옵트인한 사용자만(`opted_in`), 구독했거나 옵트인한 사용자만(`subscribed`) 또는 구독하지 않은 사용자를 포함한 모든 사용자(`all`)에게 메시지를 보내려면 이 옵션을 사용합니다. <br><br>`all` 사용자를 사용하면 트랜잭션 이메일 메시징에 유용합니다. 기본값은 `subscribed`입니다. |
|`messages`| 선택 사항 | 메시징 개체 | [사용 가능한 메시징 개체]({{site.baseurl}}/api/objects_filters/#messaging-objects) 보기. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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

메시지를 보내는 엔드포인트 응답에는 메시지 발송을 다시 참조할 수 있도록 메시지의 `dispatch_id`가 포함됩니다. `dispatch_id`는 메시지 발송의 ID로, Braze에서 보낸 각 '전송'의 고유 ID를 의미합니다. 자세한 내용은 [디스패치 ID 동작]({{site.baseurl}}/help/help_articles/data/dispatch_id/)을 참조하세요.

{% endapi %}

