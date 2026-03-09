---
nav_title: "受信者オブジェクト"
article_title: API受信者オブジェクト
page_order: 9
page_type: reference
description: "この参考記事では、Braze 受信者オブジェクトのさまざまなコンポーネントについて説明します。"

---

# 受信者オブジェクト

> 受信者オブジェクトは、エンドポイントに情報を要求したり書き込んだりすることができる。

このオブジェクトには`email`、必ず`user_alias`、`external_user_id`またはのいずれか`braze_id`を含めなければならない。**リクエストでは 1 つだけ指定する必要があります。**

受信者オブジェクトは、[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)、[トリガープロパティオブジェクト]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)、[キャンバスエントリプロパティオブジェクト]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)、および[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)を組み合わせることができる。

## オブジェクト本体

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

が`send_to_existing_only`の場合`true`、Brazeは既存ユーザーにのみメッセージを送信する。ただし、このフラグはユーザーエイリアスでは使用できない。が `send_to_existing_only`の場合`false`、属性を含めなければならない。Brazeはメッセージを送信する前に、ユーザーと`id`属性を生成する。

- [Braze ID]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)
- [ユーザーのエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [外部ユーザ ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [優先順位付け]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)
- [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)

## 受信者オブジェクトのデデュープ

受信者オブジェクトでAPI呼び出しを行う際、**同一のアドレス（つまりメールやプッシュ通知）をターゲットとする重複した受信者が存在する場合、Brazeはユーザーを重複排除する**。つまりBrazeは同一のユーザーを削除し、1つだけを残す。

例えば、同じものを使うと、ユーザーは`external_user_id`一つのメッセージしか受け取らない。この動作を回避する必要がある場合は、複数のAPIコールを行うことを検討してください。

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
