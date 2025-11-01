---
nav_title: "개체 식별을 위한 별칭"
article_title: 객체 식별을 위한 API 별칭
page_order: 11
page_type: reference
description: "이 문서에서는 객체 사양을 식별하는 별칭에 대해 설명합니다."

---

# 개체 식별을 위한 별칭

속성 객체에 필드가 있는 API 요청은 지정된 사용자 프로필에 지정된 값으로 해당 이름의 속성을 만들거나 업데이트합니다. 

대시보드의 사용자 프로필에서 이러한 특수 값을 업데이트하거나 사용자에 대한 사용자 지정 속성 데이터를 추가하려면 Braze 사용자 프로필 필드 이름(아래와 같이 나열되거나 [Braze 사용자 프로필 필드]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) 섹션에 나열된 것)을 사용하세요.

## 개체 본문

```json
{
  "aliases_to_identify" : (required, array of aliases to identify object)
  [
    {
      "external_id" : (required, string) see External user ID,
      // external_ids for users that do not exist will return a non-fatal error.
      // See server responses for details.
      "user_alias" : {
        "alias_name" : (required, string) see User aliases,
        "alias_label" : (required, string) see User aliases
      }
    }
  ]
}
```

- [외부 사용자 ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
