---
nav_title: APIパートナー統合
alias: /api_partner_integration/
hidden: true
---

# APIパートナーとの統合

Alloys ISV パートナーは、API リクエストの `partner` フィールドにパートナー名を追加する必要があります。これにより、Braze はパートナーからの受信リクエストなどの API パートナーの使用状況を追跡できます。実装を開発する際には、以下の[/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)エンドポイント構造を参照すること。

## パートナーリクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object),
   "partner" : (required, string)
}
```