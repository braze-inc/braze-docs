---
nav_title: "POST: 외부 ID 제거"
article_title: "POST: 외부 ID 제거"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "이 문서에서는 외부 ID 제거 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 외부 ID 제거
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

> 이 엔드포인트를 사용하여 더 이상 사용되지 않는 사용자의 이전 외부 ID를 제거하세요. 

요청당 최대 50개의 외부 ID를 보낼 수 있습니다. 

{% alert warning %}
이 엔드포인트는 더 이상 사용되지 않는 ID를 완전히 제거하며 되돌릴 수 없습니다. 이 엔드포인트를 사용하여 시스템에서 사용자와 여전히 연결되어 있는 사용되지 않는 `external_ids` 을 제거하면 해당 사용자의 데이터를 영구적으로 찾을 수 없게 됩니다.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `users.external_ids.remove` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `external_ids` | 필수 | 문자열 배열 | 사용자가 제거할 외부 식별자. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" :[
    "existing_deprecated_external_id_string",
    ...
  ]
}'
```

{% alert important %}
더 이상 사용되지 않는 ID만 제거할 수 있으며, 기본 외부 ID를 제거하려고 하면 오류가 발생합니다.
{% endalert %}

## 응답

응답은 모든 성공적인 제거와 실패한 제거를 관련 오류와 함께 확인합니다. `removal_errors` 필드의 오류 메시지는 원래 요청의 배열에 있는 인덱스를 참조합니다.

```
{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) <minor error message>
}
```

`message` 필드에 유효한 요청이 있으면 `success`를 반환합니다. 보다 구체적인 오류는 `removal_errors` 배열에 캡처됩니다. `message` 필드는 다음과 같은 경우 오류를 반환합니다.
- 잘못된 API 키
- 빈 `external_ids` 배열
- `external_ids` 50개 이상의 항목이 있는 배열
- 속도 제한 초과(분당 1,000건 이상의 요청)

{% endapi %}
