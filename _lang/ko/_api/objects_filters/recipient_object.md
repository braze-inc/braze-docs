---
nav_title: "수신자 오브젝트"
article_title: API 수신자 오브젝트
page_order: 9
page_type: reference
description: "이 참조 문서에서는 Braze 수신자 오브젝트의 다양한 구성요소에 대해 설명합니다."

---

# 수신자 오브젝트

> 수신자 오브젝트를 사용하면 엔드포인트에서 정보를 요청하거나 쓸 수 있습니다.

이 오브젝트에는 `external_user_id`, `user_alias`, `braze_id` 또는 `email` 중 하나를 반드시 포함해야 합니다. **요청에는 하나만 지정해야 합니다.**

수신자 오브젝트를 사용하면 [사용자 별칭 오브젝트]({{site.baseurl}}/api/objects_filters/user_alias_object/), [트리거 등록정보 오브젝트]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), [Canvas 진입 등록정보 오브젝트]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) 및 [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object/)를 결합할 수 있습니다.

## 오브젝트 본문

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "braze_id": (optional, string) see Braze ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "context": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas context object,
  "send_to_existing_only": (optional, boolean) defaults to true; cannot be used with user aliases,
  "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
}]
```

`send_to_existing_only`가 `true`이면 Braze는 기존 사용자에게만 메시지를 전송합니다. 그러나 사용자 별칭에는 이 플래그를 사용할 수 없습니다. `send_to_existing_only`가 `false`이면 반드시 속성을 포함해야 합니다. Braze는 메시지를 전송하기 전에 `id` 및 속성을 가진 사용자를 생성합니다.

- [Braze ID]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)
- [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [외부 사용자 ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [우선순위 지정]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)
- [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object/)

## 수신자 오브젝트 중복 제거

수신자 오브젝트로 API 호출을 수행할 때, **동일한 주소(예: 이메일, 푸시)를 타겟팅하는 중복 수신자가 존재하는 경우 Braze는 사용자를 중복 제거합니다**. 즉, Braze는 동일한 사용자를 제거하고 하나만 남깁니다.

예를 들어, 동일한 `external_user_id`를 사용하면 사용자는 하나의 메시지만 수신합니다. 이 동작에 대한 해결 방법이 필요한 경우 여러 번 API를 호출하는 것을 고려하세요.

동일한 `external_user_id`가 수신자 배열에 여러 번 나타나는 경우, Braze는 메시지를 한 번만 전송하며 배열에서 마지막에 나타나는 항목의 트리거 등록정보를 사용합니다. 이 동작은 결정적이며 배열 순서에 기반합니다.

다음 예시에서 `userid1`은 배열의 마지막에 해당 항목이 나타나므로 `"name": "Beth Test 2"`를 사용하여 하나의 메시지를 수신합니다.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
