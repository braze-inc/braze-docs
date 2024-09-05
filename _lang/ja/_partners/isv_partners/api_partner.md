---
nav_title: APIパートナー統合
alias: /api_partner_integration/
hidden: true
---

# APIパートナーとの統合

Alloys ISVパートナーは、API Requestsの`partner` フィールドにパートナー名を追加する必要があり、Brazeはパートナーからの受信リクエストなどAPIパートナーの利用状況を追跡できる。実装を開発する際には、以下の[/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)エンドポイント構造を参照すること。

## パートナー・リクエスト本体

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