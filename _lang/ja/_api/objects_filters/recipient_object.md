---
nav_title: "受信者オブジェクト"
article_title: API受信者オブジェクト
page_order: 9
page_type: reference
description: "この参考記事では、Braze 受信者オブジェクトのさまざまなコンポーネントについて説明します。"

---

# 受信者オブジェクト

> 受信者オブジェクトは、エンドポイントに情報を要求したり書き込んだりすることができる。

このオブジェクトには、`external_user_id` 、`user_alias` 、`email` のいずれかが必要である。**リクエストでは 1 つだけ指定する必要があります。**

{% alert important %}
メールアドレスによる受信者の指定は、現在早期アクセス中である。この早期アクセスへ参加することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

受信者オブジェクトは、[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)、[トリガープロパティオブジェクト]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)、[キャンバスエントリプロパティオブジェクトを]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)組み合わせることができます。

## オブジェクト本体

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
}]
```

- [ユーザーのエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [外部ユーザ ID]({{site.baseurl}}/api/basics/#user-ids)
- [優先順位付け]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)

## 受信者オブジェクトのデデュープ

受信者オブジェクトを使用して API 呼び出しを行うときに、**同じアドレス (つまり、メール、プッシュ) を対象とする重複した受信者が存在する場合**、ユーザーは重複排除され、同一のユーザーが削除されて 1 人のユーザーが残ります。 

たとえば、同じ `external_user_id` が使用される場合、受信されるメッセージは 1 つだけです。この動作を回避する必要がある場合は、複数のAPIコールを行うことを検討すること。

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```