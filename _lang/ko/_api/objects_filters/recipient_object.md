---
nav_title: "수신자 개체"
article_title: API 수신자 개체
page_order: 9
page_type: reference
description: "이 참조 문서에서는 Braze 수신자 객체의 다양한 구성 요소에 대해 설명합니다."

---

# 수신자 개체

> 수신자 개체를 사용하면 엔드포인트에서 정보를 요청하거나 쓸 수 있습니다.

이 객체에는 `external_user_id` 또는 `user_alias` 이 필요합니다. **요청은 하나만 지정해야 합니다.**

수신자 객체를 사용하면 [사용자 별칭 객체]({{site.baseurl}}/api/objects_filters/user_alias_object/), [트리거 속성 객체]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) 및 [캔버스 항목 속성 객체]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)를 결합할 수 있습니다.

## 개체 본문

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
}]
```

- [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [외부 사용자 ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)

## 수신자 개체 중복 제거

수신자 개체로 API 호출을 할 때 **동일한 주소(이메일, 푸시)를 타겟팅으로 하는 중복된 수신자가 있는 경우, 중복 제거**가 이루어집니다. 이는 중복된 사용자가 제거되고 한 명만 남는다는 의미입니다. 

예를 들어 동일한 `external_user_id`를 사용하는 경우 하나의 메시지만 수신됩니다. 이 동작에 대한 해결 방법이 필요한 경우 여러 번 API를 호출하는 것을 고려하세요.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```