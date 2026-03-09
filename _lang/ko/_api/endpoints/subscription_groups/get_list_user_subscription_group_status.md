---
nav_title: "GET: 사용자의 구독 그룹 상태 목록"
article_title: "GET: 사용자의 구독 그룹 상태 나열"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 사용자의 구독 그룹 상태 Braze 엔드포인트 나열에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자의 구독 그룹 상태 나열
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> 이 엔드포인트를 사용하여 구독 그룹에 속한 사용자의 구독 상태를 가져오세요.

이러한 그룹은 **정기구독 그룹** 페이지에서 사용할 수 있습니다. 이 엔드포인트의 응답에는 API 호출에서 요청한 특정 구독 그룹에 대한 외부 ID와 구독 중, 구독 취소 또는 알 수 없음이 포함됩니다. 이는 후속 API 호출에서 구독 그룹 상태를 업데이트하거나 호스팅된 웹 페이지에 표시하는 데 사용할 수 있습니다.

**이메일 구독 그룹에** 대한 이 엔드포인트의 예제를 보거나 테스트하려면 다음과 같이 하세요:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

예제를 보거나 **SMS 구독 그룹에** 대한 이 엔드포인트를 테스트하려면 다음과 같이 하세요:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

**WhatsApp 그룹에** 대한 이 엔드포인트의 예시를 보거나 테스트하려면 다음과 같이 하세요:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `subscription.status.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids)  | 필수 | 문자열 | 구독 그룹의 `id`. |
| `external_id`  |  필수* | 문자열 | 사용자의 `external_id` (최소 1개, 최대 50개 `external_ids`)를 포함해야 합니다. <br><br>`external_id` 및 `email`/`phone` 을 모두 제출한 경우, 제공된 `external_id` 만 결과 쿼리에 적용됩니다. |
| `email` | 필수* | 문자열 | 사용자의 이메일 주소입니다. 최대 50개의 문자열 배열로 전달할 수 있습니다.<br><br> 이메일 주소와 전화번호를 모두 제출하면( `external_id` 없이) 오류가 발생합니다. |
| `phone` | 필수* | 문자열의 [E.164](https://en.wikipedia.org/wiki/E.164) 형식 | 사용자의 전화번호입니다. 이메일이 포함되지 않은 경우 전화번호를 하나 이상 포함해야 합니다(최대 50개).<br><br> 이메일 주소와 전화번호를 모두 제출하면( `external_id` 없이) 오류가 발생합니다. |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

* `external_id` 또는 `email` 또는 `phone` 중 하나가 사용자당 필요합니다.

- SMS 및 WhatsApp 구독 그룹의 경우 `external_id` 또는 `phone` 이 필요합니다.  둘 다 제출하면 `external_id` 만 쿼리에 사용되며 해당 사용자에게 전화 번호가 적용됩니다.
- 이메일 구독 그룹의 경우 `external_id` 또는 `email` 이 필요합니다.  둘 다 제출하면 `external_id` 만 쿼리에 사용되며 해당 사용자에게 이메일 주소가 적용됩니다.

## 예시 요청

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Response

모든 성공적인 응답은 구독 그룹의 상태 및 사용자 기록에 따라 `Subscribed`, `Unsubscribed` 또는 `Unknown` 로 반환됩니다.

```json
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% alert important %}
이 엔드포인트는 사용자의 글로벌 구독 상태와 무관하게 구독 그룹 상태를 독립적으로 반환합니다. 사용자가 전역적으로 탈퇴한 경우, Braze 대시보드에서는 해당 사용자가 각 구독 그룹에서 탈퇴한 상태로 표시됩니다. 그러나 이 엔드포인트는 여전히 마지막으로 저장된 구독 그룹 상태(예: `Subscribed`)를 반환합니다. 글로벌 구독 상태가 개별 구독 그룹을 덮어쓰지 않으면서도 이를 우선시하기 때문입니다.<br><br>Braze는 개별 구독 그룹 상태를 보존하므로, 사용자가 전체적으로 재구독할 경우 각 구독 그룹은 이전에 저장된 상태로 복원됩니다. 사용자의 유효한 구독 상태를 확인하려면, 해당 사용자의 글로벌 구독 상태와 본 엔드포인트에서 반환된 구독 그룹 상태를 모두 확인하십시오.
{% endalert %}

{% endapi %}
