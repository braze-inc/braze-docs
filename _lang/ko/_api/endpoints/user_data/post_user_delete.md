---
nav_title: "POST: 사용자 삭제"
article_title: "POST: 사용자 삭제"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 삭제 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자 삭제
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/delete
{% endapimethod %}

> 이 엔드포인트를 사용하여 알려진 사용자 식별자를 지정하여 모든 사용자 프로필을 삭제할 수 있습니다.

하나의 요청에 최대 50개의 `external_ids`, `user_aliases` 또는 `braze_ids`를 포함할 수 있습니다. `external_ids`, `user_aliases`, `braze_ids` 중 하나만 하나의 요청에 포함할 수 있습니다.

{% alert warning %}
사용자 프로필 삭제는 되돌릴 수 없습니다. 데이터에 불일치를 일으킬 수 있는 사용자를 영구적으로 제거합니다. [API를 통해 고객 프로필을 삭제하면]({{site.baseurl}}/help/help_articles/api/delete_user/) 어떤 일이 발생하는지 도움말 설명서에서 자세히 알아보세요.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `users.delete` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External ids for the users to delete,
  "user_aliases" : (optional, array of user alias objects) User aliases for the users to delete,
  "braze_ids" : (optional, array of string) Braze user identifiers for the users to delete
}
```
### 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
| `external_ids` | 선택 사항 | 문자열 배열 | 삭제할 사용자의 외부 식별자입니다. |
| `user_aliases` | 선택 사항 | 사용자 별칭 개체의 배열 | 삭제할 사용자의 [사용자 별칭]({{site.baseurl}}/api/objects_filters/user_alias_object/)입니다. |
| `braze_ids` | 선택 사항 | 문자열 배열 | 삭제할 사용자에 대한 Braze 사용자 식별자입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"],
  "user_aliases": [
    {
      "alias_name": "user_alias1", "alias_label": "alias_label1"
    },
    {
      "alias_name": "user_alias2", "alias_label": "alias_label2"
    }
  ]
}'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "deleted" : (required, integer) number of user ids queued for deletion
}
```
{% endapi %}


