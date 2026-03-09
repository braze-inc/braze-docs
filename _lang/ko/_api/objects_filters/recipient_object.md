---
nav_title: "수신자 개체"
article_title: API 수신자 개체
page_order: 9
page_type: reference
description: "이 참조 문서에서는 브레이즈 수신자 객체의 다양한 구성 요소에 대해 설명합니다."

---

# 수신자 개체

> 수신자 개체를 사용하면 엔드포인트에서 정보를 요청하거나 쓸 수 있습니다.

이 객체에는 , `user_alias``email`, `braze_id`, 또는  중`external_user_id` 하나를 반드시 포함해야 합니다. **요청은 하나만 지정해야 합니다.**

수신자 객체를 사용하면 [사용자 별칭 객체]({{site.baseurl}}/api/objects_filters/user_alias_object/), [트리거 속성 객체]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), [캔버스 항목 속성 객체]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) 및 [사용자 속성 객체를]({{site.baseurl}}/api/objects_filters/user_attributes_object/) 결합할 수 있습니다.

## 개체 본문

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

가  일`send_to_existing_only` 때`true`, Braze는 기존 사용자에게만 메시지를 전송합니다. 그러나 사용자 별칭에는 이 플래그를 사용할 수 없습니다. 가 일`send_to_existing_only` 때`false`, 반드시 속성을 포함해야 합니다. Braze는 메시지를 전송하기 전에  및 `id`속성을 가진 사용자를 생성합니다.

- [Braze ID]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)
- [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [External user ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [우선순위 지정]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)
- [사용자 속성 개체]({{site.baseurl}}/api/objects_filters/user_attributes_object/)

## 수신자 개체 중복 제거

수신자 객체로 API 호출을 수행할 때 **동일한 주소(이메일, 푸시)를 타겟팅하는 중복 수신자가 존재하는 경우, Braze는 사용자를 중복 제거합니다**. 즉, Braze는 동일한 사용자를 제거하고 하나의 사용자만 남깁니다.

예를 들어, 동일한 를 사용하면 사용자는 단 `external_user_id`하나의 메시지만 수신합니다. 이 동작에 대한 해결 방법이 필요한 경우 여러 번 API를 호출하는 것을 고려하세요.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
