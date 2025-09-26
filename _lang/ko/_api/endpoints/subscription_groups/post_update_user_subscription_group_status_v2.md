---
nav_title: "POST: 사용자의 구독 그룹 상태 업데이트 V2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "이 문서에서는 사용자의 구독 그룹 상태 Braze V2 엔드포인트 업데이트에 대한 자세한 내용을 설명합니다."

platform: API
channel:
  - Email
---

{% api %}
# 사용자의 구독 그룹 상태 업데이트(V2)
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> 이 엔드포인트를 사용하여 Braze 대시보드에서 최대 50명의 사용자의 구독 상태를 일괄 업데이트할 수 있습니다. 

**구독** 그룹 페이지로 이동하여 구독 그룹의 `subscription_group_id` 에 액세스할 수 있습니다.

**이메일 구독 그룹에** 대한 이 엔드포인트의 예제를 보거나 테스트하려면 다음과 같이 하세요:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

예제를 보거나 **SMS 구독 그룹에** 대한 이 엔드포인트를 테스트하려면 다음과 같이 하세요:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

**WhatsApp 그룹에** 대한 이 엔드포인트의 예시를 보거나 테스트하려면 다음과 같이 하세요:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `subscription.status.set` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "subscription_groups":[
    {
      "subscription_group_id": (required, string),
      "subscription_state": (required, string)
      "external_ids": (required*, array of strings),
      "emails": (required*, array of strings),
      "phones": (required*, array of strings in E.164 format),
    }
  ]
}
```
* `emails` 및 `phones` 매개변수 둘 다 포함할 수는 없습니다. 또한 `emails`, `phones`, `external_ids` 으로 개별적으로 보낼 수도 있습니다.

{% alert tip %}
[`/users/track` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 사용하여 새 사용자를 만들 때 사용자 속성 개체 내에서 구독 그룹을 설정하면 한 번의 API 호출로 사용자를 만들고 구독 그룹 상태를 설정할 수 있습니다.
{% endalert %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | 필수 | 문자열 | 구독 그룹의 `id`. |
| `subscription_state` | 필수 | 문자열 | 사용 가능한 값은 `unsubscribed` (구독 그룹에 속하지 않음) 또는 `subscribed` (구독 그룹에 속함)입니다. |
| `external_ids` | 필수* | 문자열 배열 | 사용자(또는 사용자)의 `external_id` 에는 최대 50개의 `id`을 포함할 수 있습니다. |
| `emails` | 필수* | 문자열 또는 문자열 배열 | 사용자의 이메일 주소는 문자열 배열로 전달할 수 있습니다. 이메일 주소를 하나 이상(최대 50개) 포함해야 합니다. <br><br>동일한 워크스페이스에서 여러 사용자(`external_id`)가 동일한 이메일 주소를 공유하는 경우 이메일 주소를 공유하는 모든 사용자에게 구독 그룹 변경 사항이 업데이트됩니다. |
| `phones` | 필수* | 문자열의 [E.164](https://en.wikipedia.org/wiki/E.164) 형식 | 사용자의 전화번호는 문자열 배열로 전달할 수 있습니다. 전화번호를 하나 이상 포함해야 합니다(최대 50개). <br><br>동일한 워크스페이스에서 여러 사용자(`external_id`)가 동일한 전화번호를 공유하는 경우 전화번호를 공유하는 모든 사용자에게 동일한 가입 그룹 변경사항이 업데이트됩니다.|
| `use_double_opt_in_logic` | 선택 사항 | 부울 | 이 매개변수를 생략하거나 `false` 으로 설정하면 사용자는 SMS 이중 옵트인 워크플로에 입력되지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
`emails` 및 `phones` 매개 변수를 모두 포함할 수 없습니다. 또한 `emails`, `phones`, `external_ids` 으로 개별적으로 보낼 수도 있습니다.
{% endalert %}

### 요청 예시

다음 예제에서는 `external_id`를 사용하여 이메일과 SMS에 대해 하나의 API 호출을 수행합니다.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## 이메일

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "emails":["example1@email.com","example2@email.com"]
    }
  ]
}
'
```

## SMS 및 WhatsApp

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "phones":["+12223334444","+15556667777"]
    }
  ]
}
'
```

{% endapi %}
