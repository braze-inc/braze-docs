---
nav_title: "受信者オブジェクト"
article_title: API受信者オブジェクト
page_order: 9
page_type: reference
description: "この参照記事では、ろう付けレシピエントオブジェクトのさまざまなコンポーネントについて説明します。"

---

# Recipientsオブジェクト

> 受信者オブジェクトを使用すると、エンドポイントで情報をリクエストまたは書き込みできます。

このオブジェクトには、`external_user_id` または`user_alias` のいずれかが必要です。**リクエストは1つだけ指定する必要があります。**

recipients オブジェクトを使用すると、[user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/)、[trigger properties object]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)、および[Canvas entry properties object]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) を組み合わせることができ。

## オブジェクト本体

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
}]
```

- [ユーザーのエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [外部ユーザ ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)

## 受信者オブジェクトのデデューピング

受信者オブジェクトを使用してAPI コールを行う場合、同じアドレス(つまり、email、push) をターゲットとする重複した受信者が存在する場合、ユーザはデデュープ されます。つまり、同一のユーザが削除され、残りのユーザが削除されます。 

たとえば、同じ`external_user_id` が使用される場合、1 つのメッセージのみが受信されます。この動作の回避策が必要な場合は、複数のAPI コールを実行することを検討してください。

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```