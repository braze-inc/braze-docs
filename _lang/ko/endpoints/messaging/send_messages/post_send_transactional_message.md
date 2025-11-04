---
nav_title: "POST: API 트리거 전송을 사용하여 트랜잭션 이메일 보내기"
article_title: "POST: API 트리거 배달을 사용하여 트랜잭션 이메일 보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 API 트리거 배달 Braze 엔드포인트를 사용하여 트랜잭션 이메일 메시지 보내기 기능에 대해 자세히 설명합니다."

---

{% api %}
# API 트리거 전송을 사용하여 트랜잭션 이메일 보내기
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> 이 엔드포인트를 사용하여 지정된 사용자에게 즉각적인 일회성 트랜잭션 메시지를 보낼 수 있습니다.

이 엔드포인트는 Braze [트랜잭션 이메일 캠페인]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) 생성 및 해당 캠페인 ID와 함께 사용됩니다.

{% alert important %}
트랜잭션 이메일은 현재 일부 Braze 패키지의 일부로 제공됩니다. 자세한 내용은 Braze 고객 성공 관리자에게 문의하세요.
{% endalert %}

[보내기 트리거 캠페인 엔드포인트와]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) 마찬가지로, 이 캠페인 유형을 사용하면 메시지 콘텐츠를 Braze 대시보드 내에 보관하면서 API를 통해 메시지를 언제, 누구에게 보낼지 지정할 수 있습니다. 메시지를 보낼 오디언스 또는 세그먼트를 허용하는 보내기 트리거 캠페인 엔드포인트와 달리, 이 캠페인 유형은 주문 확인 또는 비밀번호 재설정과 같은 1:1 알림 메시징을 위해 특별히 제작된 것이므로 이 엔드포인트에 대한 요청은 `external_user_id` 또는 `user_alias`로 단일 사용자를 지정해야 합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `transactional.send` 권한으로 API 키를 생성해야 합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `campaign_id` | Required | 문자열 | 캠페인의 ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| Optional | 문자열 |  Base64 호환 문자열입니다. 다음 정규식에 대해 유효성을 검사합니다.<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>이 선택적 필드를 사용하면 트랜잭션 HTTP 이벤트 포스트백에서 전송되는 이벤트에 포함될 이 특정 전송에 대한 내부 식별자를 전달할 수 있습니다. 전달되면 이 식별자는 중복 제거 키로도 사용되며, Braze는 이 키를 24시간 동안 저장합니다. <br><br>다른 요청에 동일한 식별자를 전달해도 24시간 동안은 Braze에서 새로운 전송 인스턴스가 생성되지 않습니다.|
|`trigger_properties`|선택 사항|객체|트리거 속성을 참조하십시오. 이 요청에서 사용자에게 적용될 개인화 키-값 쌍입니다. |
|`recipient`|필수|객체| 이 메시지를 타겟팅하는 사용자입니다. `attributes` 및 단일 `external_user_id` 또는 `user_alias`를 포함할 수 있습니다.<br><br>Braze에 아직 존재하지 않는 외부 사용자 ID를 제공하는 경우, `attributes` 개체에 필드를 전달하면 Braze에서 이 사용자 프로필이 생성되고 새로 생성된 사용자에게 이 메시지가 전송됩니다. <br><br>`attributes` 객체의 서로 다른 데이터를 사용하여 동일한 사용자에게 여러 요청을 보내는 경우 `first_name`, `last_name`, `email` 속성이 동기식으로 업데이트되고 메시지에 템플릿이 적용됩니다. 사용자 지정 속성에는 이와 같은 보호 기능이 없으므로 이 API를 통해 사용자를 업데이트하고 다른 사용자 지정 속성 값을 빠르게 연속해서 전달할 때는 주의해서 진행하세요.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## 응답

트랜잭션 이메일 보내기 엔드포인트는 이 메시지 전송의 인스턴스를 나타내는 `dispatch_id` 으로 응답합니다. 이 식별자는 트랜잭션 HTTP 이벤트 포스트백의 이벤트와 함께 단일 사용자에게 전송된 개별 이메일의 상태를 추적하는 데 사용할 수 있습니다.

### 응답 예시

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## 문제 해결

엔드포인트는 경우에 따라 오류 코드와 사람이 읽을 수 있는 메시지를 반환할 수도 있는데, 대부분은 유효성 검사 오류입니다. 다음은 잘못된 요청을 할 때 발생할 수 있는 몇 가지 일반적인 오류입니다.

| 오류 | 문제 해결 |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | 제공된 캠페인 ID는 거래 캠페인용이 아닙니다. |
| `The external reference has been queued.  Please retry to obtain send_id.` | 최근에 external_send_id이(가) 생성되었습니다. 새 메시지를 보내려면 새 external_send_id을(를) 시도해 보세요. |
| `Campaign does not exist` | 제공한 캠페인 ID가 기존 캠페인과 일치하지 않습니다. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | 제공된 캠페인 ID는 보관된 캠페인에 해당합니다. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | 제공된 캠페인 ID는 일시 중지된 캠페인에 해당합니다. |
| `campaign_id must be a string of the campaign api identifier` | 제공한 캠페인 ID가 올바른 형식이 아닙니다. |
| `Error authenticating credentials` | 제공된 API 키가 유효하지 않습니다. |
| `Invalid whitelisted IPs `| 요청을 전송하는 IP 주소가 IP 화이트리스트에 없는 경우(사용 중인 경우) |
| `You do not have permission to access this resource` | 사용된 API 키에 이 작업을 수행할 수 있는 권한이 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze의 대부분의 엔드포인트에는 너무 많은 요청을 한 경우 429 응답 코드를 반환하는 속도 제한이 구현되어 있습니다. 트랜잭션 전송 엔드포인트는 다르게 작동합니다. 할당된 전송률 한도를 초과하는 경우 당사 시스템은 계속해서 API 호출을 수집하고 성공 코드를 반환하며 메시지를 전송하지만 해당 메시지는 해당 기능에 대해 계약된 SLA의 적용을 받지 않을 수 있습니다. 이 기능에 대한 자세한 정보가 필요한 경우 문의해 주세요.

## 트랜잭션 HTTP 이벤트 포스트백

{% multi_lang_include http_event_postback.md %}

{% endapi %}
