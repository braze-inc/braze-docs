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

## 필수 구성 요소

이 엔드포인트를 사용하려면 `users.delete` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

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

| 매개변수      | 필수 | 데이터 유형                  | 설명                                                                                      |
| -------------- | -------- | -------------------------- | ------------------------------------------------------------------------------------------------ |
| `external_ids` | 선택 사항 | 문자열 배열           | 사용자가 삭제할 외부 식별자.                                                    |
| `user_aliases` | 선택 사항 | 사용자 별칭 객체 배열 | 삭제할 사용자의 사용자 [별칭입니다]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `braze_ids`    | 선택 사항 | 문자열 배열           | 삭제할 사용자의 사용자 아이디를 브레이즈합니다.                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 이메일로 사용자 삭제하기
식별자로 `email`을 지정한 경우 식별자에 `prioritization` 값을 추가로 입력해야 합니다. `prioritization` 은 정렬된 배열이며 여러 사용자가 발견될 경우 삭제할 사용자를 지정해야 합니다. 즉, 우선순위와 일치하는 사용자가 두 명 이상일 경우 사용자를 삭제하지 않습니다.

배열에 허용되는 값은 `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated`이며 이는 가장 최근에 업데이트된 사용자에게 우선순위를 지정하는 것을 의미합니다.

우선순위 배열에는 한 번에 다음 옵션 중 하나만 존재할 수 있습니다.
- `identified` 를 가진 사용자에게 우선순위를 지정하는 것을 말합니다. `external_id`
- `unidentified` 없는 사용자에게 우선순위를 지정하는 것을 말합니다. `external_id`

## 예시 요청
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
  ],
  "email_addresses": [
    {
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
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


