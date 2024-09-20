---
nav_title: "POST: 사용자의 구독 그룹 상태 업데이트"
article_title: "POST: 사용자의 구독 그룹 상태 업데이트"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 업데이트 사용자의 구독 그룹 상태 Braze 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."
---
{% api %}
# 사용자의 구독 그룹 상태 업데이트
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/subscription/status/set
{% endapimethod %}

> 이 엔드포인트를 사용하여 Braze 대시보드에서 최대 50명의 사용자 구독 상태를 일괄 업데이트할 수 있습니다. 

**구독 그룹 페이지**로 이동하여 구독 그룹 `subscription_group_id`에 액세스할 수 있습니다.

**이메일 구독 그룹에** 대한 예제를 보거나 이 엔드포인트를 테스트하려는 경우:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

**SMS 구독 그룹에** 대한 예제를 보거나 이 엔드포인트를 테스트하려는 경우:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## 사전 요구 사항

이 엔드포인트를 사용하려면 `subscription.status.set` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## 요청 본문

{% tabs %}
{% tab SMS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
   // SMS subscription group - one of external_id or phone is required
 }
```
\* SMS 구독 그룹: `external_id` 또는 `phone`만 허용됩니다.

{% endtab %}
{% tab Email %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
   // Email subscription group - one of external_id or email is required
   // Note that sending an email address that is linked to multiple profiles will update all relevant profiles
 }
```
\* 이메일 구독 그룹: `email` 또는 `external_id` 중 하나가 필요합니다.
{% endtab %}
{% endtabs %}

이 속성은 사용자 프로필 정보를 업데이트하는 데 사용해서는 안 됩니다. 대신 [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)프로퍼티를 사용하세요.

{% alert tip %}
[/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)엔드포인트를 통해 새 사용자를 생성할 때 사용자 속성 객체 내에 구독 그룹을 설정할 수 있습니다. 이렇게 하면 한 번의 API 호출로 사용자를 생성하고 구독 그룹 상태를 설정할 수 있습니다.
{% endalert %}

## 요청 파라미터

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|--|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids)| 필수 | 문자열 | 구독 `id` 그룹의 이름입니다.|
| `subscription_state` | 필수 | 문자열 | 사용 가능한 값은 `unsubscribed` (구독 그룹에 속하지 않음) 또는 `subscribed` (구독 그룹에 있음).|
| `external_id` | 필수* | 문자열 배열 | 사용자 또는 사용자들의 `external_id` 수는 최대 50개의 `id`가 포함할 수 있습니다.
| `email` | 필수* | 문자열 또는 문자열 배열 | 사용자의 이메일 주소는 문자열 배열로 전달될 수 있습니다. 이메일 주소를 하나 이상 포함해야 합니다 (최대 50개). <br><br>동일한 워크스페이스의 여러 사용자(`external_id`)가 동일한 이메일 주소를 공유하는 경우 이메일 주소를 공유하는 모든 사용자가 구독 그룹 변경 사항으로 업데이트됩니다. |
| `phone` | 필수* | [E.164](https://en.wikipedia.org/wiki/E.164) 형식의 문자열 | 사용자의 전화번호는 문자열 배열로 전달될 수 있습니다. 전화번호를 하나 이상 포함해야 합니다 (최대 50개).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시

### 이메일

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "email": ["example1@email.com", "example2@email.com"]
}
'
```

### SMS

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}
'
```

## 성공 응답 예시

`201` 상태 코드는 다음 응답 본문을 반환할 수 있습니다.

```json
{
    "message": "success"
}
```

{% alert important %}
엔드포인트는 `email` 또는 `phone` 값만 받아들이고 둘 다 받아들이지는 않습니다. 둘 다 제공되면 `{"message":"Either an email address or a phone number should be provided, but not both."}`와 같은 응답을 받게 됩니다.
{% endalert %}

{% endapi %}

